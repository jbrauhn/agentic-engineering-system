#!/usr/bin/env python3
import argparse
import copy
import json
import sys
from pathlib import Path


class LifecycleError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


def fail(code, message):
    raise LifecycleError(code, message)


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure_unique(values, label):
    if len(values) != len(set(values)):
        fail("STRUCTURE_DUPLICATE_ID", f"Duplicate value in {label}")


def validate_protocol(protocol):
    required = ["loop", "increment", "task", "gates", "routes", "rules", "transitions"]
    for key in required:
        if key not in protocol:
            fail("STRUCTURE_MISSING_SECTION", f"Missing protocol section {key}")

    for key in ["control_states", "terminal_dispositions"]:
        ensure_unique(protocol["loop"][key], f"loop.{key}")
    ensure_unique(protocol["increment"]["active_positions"], "increment.active_positions")
    ensure_unique(protocol["increment"]["terminal_dispositions"], "increment.terminal_dispositions")
    ensure_unique(protocol["task"]["execution_states"], "task.execution_states")
    ensure_unique(list(protocol["gates"].keys()), "gates")
    ensure_unique(protocol["routes"], "routes")

    transition_ids = [transition["id"] for transition in protocol["transitions"]]
    ensure_unique(transition_ids, "transitions")

    gate_ids = set(protocol["gates"])
    routes = set(protocol["routes"])
    increment_states = set(protocol["increment"]["active_positions"])
    increment_terminals = set(protocol["increment"]["terminal_dispositions"])
    loop_states = set(protocol["loop"]["control_states"])
    loop_terminals = set(protocol["loop"]["terminal_dispositions"])

    for transition in protocol["transitions"]:
        scope_type = transition["scope_type"]
        if scope_type == "EXECUTION_INCREMENT":
            if "source" in transition and transition["source"] not in increment_states:
                fail("STRUCTURE_BAD_STATE_REF", f"{transition['id']} source does not exist")
            if "target" in transition and transition["target"] not in increment_states:
                fail("STRUCTURE_BAD_STATE_REF", f"{transition['id']} target does not exist")
            if (
                "target_terminal_disposition" in transition
                and transition["target_terminal_disposition"] not in increment_terminals
            ):
                fail("STRUCTURE_BAD_TERMINAL_REF", f"{transition['id']} invalid Increment terminal disposition")
        elif scope_type == "AE_LOOP":
            if "source" in transition and transition["source"] not in loop_states:
                fail("STRUCTURE_BAD_STATE_REF", f"{transition['id']} source does not exist")
            if "target" in transition and transition["target"] not in loop_states:
                fail("STRUCTURE_BAD_STATE_REF", f"{transition['id']} target does not exist")
            if (
                "target_terminal_disposition" in transition
                and transition["target_terminal_disposition"] not in loop_terminals
            ):
                fail("STRUCTURE_BAD_TERMINAL_REF", f"{transition['id']} invalid Loop terminal disposition")
        else:
            fail("STRUCTURE_BAD_SCOPE_TYPE", f"{transition['id']} has unsupported scope type")

        for gate in transition.get("required_gates", []):
            if gate not in gate_ids:
                fail("STRUCTURE_BAD_GATE_REF", f"{transition['id']} references unknown gate {gate}")
        if "route" in transition and transition["route"] not in routes:
            fail("STRUCTURE_BAD_ROUTE_REF", f"{transition['id']} references unknown route {transition['route']}")

    required_routes = {"ACCEPT", "RETRY_EXECUTION", "REPLAN", "PROPOSE_CONTRACT_CHANGE", "ESCALATE"}
    if not required_routes.issubset(routes):
        fail("STRUCTURE_REQUIRED_ROUTE_MISSING", "Required canonical backward/controlled route missing")

    required_gates = {
        "G1_CONTRACT_APPROVAL",
        "G2_PLAN_REVIEW",
        "G3_AUTHORITY",
        "G4_VALIDATION_ACCEPTANCE",
        "G5_CONTRACT_CHANGE",
    }
    if required_gates != gate_ids:
        fail("STRUCTURE_GATE_SET_MISMATCH", "Canonical gate family set is incomplete or unexpected")

    return {transition["id"]: transition for transition in protocol["transitions"]}


def scope_anchor_covers(review_scope, scope_id, allowed_types):
    covered = False
    for anchor in review_scope or []:
        if anchor.get("type") not in allowed_types:
            fail("BAD_REVIEW_SCOPE_ANCHOR", f"Unsupported review scope anchor {anchor}")
        if anchor.get("type") == "EXECUTION_INCREMENT" and anchor.get("id") == scope_id:
            covered = True
    return covered


def gate_key(scope, gate):
    return f"{scope}::{gate}"


def validate_exact_refs(scope, obj, step):
    if step.get("presented_contract_revision") != obj.get("contract_revision"):
        fail("PRESENTED_CONTRACT_MISMATCH", f"{scope} presented Contract revision does not match governing effectivity")
    if step.get("presented_baseline_revision") != obj.get("baseline_revision"):
        fail("PRESENTED_BASELINE_MISMATCH", f"{scope} presented Baseline revision does not match")
    if obj.get("plan_revision") is not None and step.get("presented_plan_revision") != obj.get("plan_revision"):
        fail("PRESENTED_PLAN_MISMATCH", f"{scope} presented Plan revision does not match")


def check_gate(protocol, state, scope, gate_id, is_loop=False):
    gate = state["gates"].get(gate_key(scope, gate_id))
    if not gate:
        fail("MISSING_GATE", f"{scope} missing required gate {gate_id}")

    status = gate.get("status")
    if status == "UNKNOWN":
        fail("UNKNOWN_GATE", f"{scope} gate {gate_id} is UNKNOWN")
    if status != "SATISFIED":
        fail("UNSATISFIED_GATE", f"{scope} gate {gate_id} is not satisfied")
    if not gate.get("record"):
        fail("GATE_WITHOUT_AUTHORITY_RECORD", f"{scope} gate {gate_id} lacks authoritative record reference")

    contract_revision = (
        state["loop"]["approved_contract_revision"] if is_loop else state["increments"][scope]["contract_revision"]
    )

    if gate_id == "G1_CONTRACT_APPROVAL":
        if gate.get("target_contract_revision") != contract_revision:
            fail("STALE_CONTRACT_APPROVAL", f"{scope} Contract approval gate targets wrong revision")
    elif gate_id == "G2_PLAN_REVIEW":
        increment = state["increments"][scope]
        if gate.get("target_plan_revision") != increment.get("plan_revision"):
            fail("STALE_PLAN_REVIEW", f"{scope} Plan Review targets stale Plan revision")
        if not scope_anchor_covers(gate.get("review_scope"), scope, set(protocol["review_scope_anchor_types"])):
            fail("PLAN_REVIEW_SCOPE_MISMATCH", f"{scope} is not covered by declared review scope")
    elif gate_id == "G4_VALIDATION_ACCEPTANCE":
        if gate.get("target_contract_revision") != contract_revision:
            fail("STALE_VALIDATION_TARGET", f"{scope} Validation targets wrong Contract revision")
        if gate.get("validator") == gate.get("producer"):
            fail("SELF_VALIDATION", f"{scope} validator and producer are the same")

    return gate


def run_scenario(protocol, transitions, fixture):
    state = copy.deepcopy(fixture["initial"])
    state.setdefault("gates", {})
    state.setdefault("failed_validations", {})
    state.setdefault("blocks", {})
    state.setdefault("learning_disposition", None)
    state.setdefault("final_reconciliation", None)
    state.setdefault("history", [])
    state["loop"].setdefault("terminal_disposition", None)

    for increment in state.get("increments", {}).values():
        increment.setdefault("terminal_disposition", None)
        increment.setdefault("blocked", False)
        increment.setdefault("tasks", {})

    loop_id = state["loop"]["id"]

    for step in fixture.get("steps", []):
        action = step["action"]

        if action == "set_gate":
            gate_id = step["gate"]
            if gate_id not in protocol["gates"]:
                fail("UNKNOWN_GATE_ID", gate_id)
            status = step["status"]
            if status not in protocol["gate_evaluation_states"]:
                fail("BAD_GATE_STATUS", status)
            if status == "SATISFIED" and not step.get("record"):
                fail("GATE_WITHOUT_AUTHORITY_RECORD", f"{gate_id} SATISFIED without record")
            if gate_id == "G2_PLAN_REVIEW" and status == "SATISFIED":
                if not step.get("target_plan_revision") or not step.get("review_scope"):
                    fail("INCOMPLETE_PLAN_REVIEW_GATE", "Plan Review gate lacks exact revision/scope")
                scope_anchor_covers(step["review_scope"], step["scope"], set(protocol["review_scope_anchor_types"]))
            if gate_id == "G4_VALIDATION_ACCEPTANCE" and status == "SATISFIED":
                if step.get("validator") == step.get("producer"):
                    fail("SELF_VALIDATION", "Work producer cannot self-satisfy Validation acceptance")
            state["gates"][gate_key(step["scope"], gate_id)] = copy.deepcopy(step)

        elif action == "transition":
            transition_id = step["transition"]
            if transition_id not in transitions:
                fail("UNKNOWN_TRANSITION", transition_id)
            transition = transitions[transition_id]
            scope = step["scope"]
            is_loop = transition["scope_type"] == "AE_LOOP"

            if is_loop:
                if scope != loop_id:
                    fail("SCOPE_TYPE_MISMATCH", f"{scope} is not the Loop")
                obj = state["loop"]
                current = obj["state"]
                if "source" in transition and current != transition["source"]:
                    fail("INVALID_SOURCE_STATE", f"{transition_id} requires {transition['source']}, found {current}")
                if transition.get("source_any_nonclosed") and current == "CLOSED":
                    fail("INVALID_SOURCE_STATE", f"{transition_id} cannot originate from CLOSED")
                if step.get("presented_contract_revision") != obj.get("approved_contract_revision"):
                    fail("PRESENTED_CONTRACT_MISMATCH", "Loop transition uses wrong Contract revision")
            else:
                if scope not in state["increments"]:
                    fail("UNKNOWN_SCOPE", scope)
                obj = state["increments"][scope]
                if obj.get("terminal_disposition"):
                    fail("TERMINAL_SCOPE_TRANSITION", f"{scope} already terminal")
                if obj.get("blocked"):
                    fail("BLOCKED_SCOPE_TRANSITION", f"{scope} has unresolved blocking condition")
                current = obj.get("position")
                if "source" in transition and current != transition["source"]:
                    fail("INVALID_SOURCE_STATE", f"{transition_id} requires {transition['source']}, found {current}")
                if transition.get("source_any_active") and current not in protocol["increment"]["active_positions"]:
                    fail("INVALID_SOURCE_STATE", f"{transition_id} requires active Increment")
                validate_exact_refs(scope, obj, step)

            for gate_id in transition.get("required_gates", []):
                check_gate(protocol, state, scope, gate_id, is_loop=is_loop)

            if transition.get("requires_failed_validation") and not state["failed_validations"].get(scope):
                fail("FAILED_VALIDATION_REQUIRED", f"{transition_id} requires prior failed Validation")

            if is_loop and transition.get("requires_all_increments_terminal"):
                nonterminal = [
                    key for key, value in state["increments"].items() if not value.get("terminal_disposition")
                ]
                if nonterminal:
                    fail("NONTERMINAL_INCREMENT", f"Loop cannot close with active Increments: {nonterminal}")

            if is_loop and transition.get("requires_learning_disposition") and state["learning_disposition"] is None:
                fail("LEARNING_DISPOSITION_REQUIRED", "Loop closure requires learning disposition")

            if is_loop and transition.get("requires_final_contract_scope_validation"):
                gate = state["gates"].get(gate_key(scope, "G4_VALIDATION_ACCEPTANCE"))
                if not gate or not gate.get("final_contract_scope"):
                    fail("FINAL_CONTRACT_VALIDATION_REQUIRED", "Loop ACCEPTED requires final Contract-scope Validation")
                reconciliation = state.get("final_reconciliation")
                if not reconciliation:
                    fail("FINAL_RECONCILIATION_REQUIRED", "Loop ACCEPTED requires Contract revision reconciliation")
                if reconciliation.get("final_contract_revision") != state["loop"]["approved_contract_revision"]:
                    fail("FINAL_RECONCILIATION_STALE", "Final reconciliation does not target current approved Contract revision")
                accepted = {
                    key: value["contract_revision"]
                    for key, value in state["increments"].items()
                    if value.get("terminal_disposition") == "ACCEPTED"
                }
                if reconciliation.get("scope_contract_revisions") != accepted:
                    fail("FINAL_RECONCILIATION_INCOMPLETE", "Accepted scope Contract revisions not fully reconciled")

            prior = obj.get("state") if is_loop else obj.get("position")
            if "target" in transition:
                if is_loop:
                    obj["state"] = transition["target"]
                else:
                    obj["position"] = transition["target"]
            if "target_terminal_disposition" in transition:
                obj["terminal_disposition"] = transition["target_terminal_disposition"]
                if not is_loop:
                    obj["position"] = None
            state["history"].append(
                {"scope": scope, "transition": transition_id, "prior": prior, "result": "ALLOWED"}
            )

        elif action == "record_failed_validation":
            state["failed_validations"][step["scope"]] = step["record"]

        elif action == "change_plan_revision":
            increment = state["increments"][step["scope"]]
            increment["plan_revision"] = step["new_plan_revision"]
            increment["position"] = "PLANNING"

        elif action == "contract_change_approved":
            if not step.get("authority_decision_record"):
                fail("CONTRACT_CHANGE_NOT_APPROVED", "Approved Contract change requires Human Authority Decision record")
            new_revision = step.get("new_contract_revision")
            if not new_revision:
                fail("CONTRACT_CHANGE_NO_NEW_REVISION", "Missing new Contract revision")

            active = {
                key: value for key, value in state["increments"].items() if not value.get("terminal_disposition")
            }
            effectivity = step.get("effectivity") or {}
            if set(effectivity) != set(active):
                fail("AMBIGUOUS_CONTRACT_EFFECTIVITY", "Every active governed Increment requires explicit effectivity determination")

            prior_loop_revision = state["loop"]["approved_contract_revision"]
            for scope_id, increment in active.items():
                determination = effectivity[scope_id]
                if not determination.get("determination_record"):
                    fail("AMBIGUOUS_CONTRACT_EFFECTIVITY", f"{scope_id} lacks effectivity determination provenance")
                classification = determination.get("classification")

                if classification == "UNAFFECTED":
                    if determination.get("governing_contract_revision") != increment.get("contract_revision"):
                        fail("BAD_UNAFFECTED_EFFECTIVITY", f"{scope_id} silently changed Contract revision")
                elif classification == "AFFECTED":
                    if determination.get("governing_contract_revision") != new_revision:
                        fail("BAD_AFFECTED_EFFECTIVITY", f"{scope_id} affected scope must explicitly bind new revision")
                    increment["contract_revision"] = new_revision
                    action_needed = determination.get("action")
                    if action_needed == "REPLAN":
                        increment["position"] = "PLANNING"
                        if not determination.get("new_plan_revision"):
                            fail("AFFECTED_SCOPE_REPLAN_MISSING_PLAN", f"{scope_id} replan lacks new Plan revision")
                        increment["plan_revision"] = determination["new_plan_revision"]
                    elif action_needed == "BLOCK":
                        increment["blocked"] = True
                    else:
                        fail("AFFECTED_SCOPE_ACTION_REQUIRED", f"{scope_id} affected scope lacks governed action")
                else:
                    fail("BAD_EFFECTIVITY_CLASSIFICATION", f"{scope_id} classification must be AFFECTED/UNAFFECTED")

            state["loop"]["approved_contract_revision"] = new_revision
            state["history"].append(
                {
                    "scope": loop_id,
                    "event": "contract_change_approved",
                    "prior_contract_revision": prior_loop_revision,
                    "new_contract_revision": new_revision,
                }
            )

        elif action == "escalate":
            scope = step["scope"]
            if not step.get("reason"):
                fail("ESCALATION_REASON_REQUIRED", "Escalation requires reason")
            if scope == loop_id:
                state["loop"]["state"] = "SUSPENDED"
                state["blocks"][scope] = step["reason"]
            else:
                state["increments"][scope]["blocked"] = True
                state["blocks"][scope] = step["reason"]

        elif action == "resolve_block":
            scope = step["scope"]
            state["blocks"].pop(scope, None)
            if scope == loop_id:
                if state["loop"]["state"] == "SUSPENDED":
                    state["loop"]["state"] = "OPEN"
            else:
                state["increments"][scope]["blocked"] = False

        elif action == "learning_disposition":
            state["learning_disposition"] = {"material_learning": bool(step.get("material_learning"))}

        elif action == "final_reconciliation":
            if step.get("final_contract_revision") != state["loop"]["approved_contract_revision"]:
                fail("FINAL_RECONCILIATION_STALE", "Final reconciliation targets wrong Contract revision")
            state["final_reconciliation"] = copy.deepcopy(step)

        elif action == "provider_status":
            increment = state["increments"][step["scope"]]
            task = increment.setdefault("tasks", {}).setdefault(step["task"], {"state": "NOT_STARTED"})
            task["provider_status"] = step.get("provider_status")

        elif action == "set_task_state":
            if step["state"] not in protocol["task"]["execution_states"]:
                fail("BAD_TASK_STATE", step["state"])
            increment = state["increments"][step["scope"]]
            task = increment.setdefault("tasks", {}).setdefault(step["task"], {"state": "NOT_STARTED"})
            task["state"] = step["state"]

        elif action == "assert_concurrency":
            for scope_id, expected in step["positions"].items():
                actual = state["increments"][scope_id].get("position")
                if actual != expected:
                    fail("CONCURRENCY_ASSERTION_FAILED", f"{scope_id}: expected {expected}, got {actual}")

        elif action == "assert_loop_state":
            if state["loop"]["state"] != step["state"]:
                fail("LOOP_STATE_ASSERTION_FAILED", f"Expected {step['state']}, got {state['loop']['state']}")

        else:
            fail("UNKNOWN_FIXTURE_ACTION", action)

    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("protocol")
    parser.add_argument("fixtures")
    args = parser.parse_args()

    protocol = load_json(args.protocol)
    fixtures = load_json(args.fixtures)

    try:
        transitions = validate_protocol(protocol)
    except LifecycleError as error:
        print(f"PROTOCOL FAIL [{error.code}] {error.message}")
        return 1

    failures = []
    for fixture in fixtures.get("scenarios", []):
        got = "PASS"
        error_code = None
        try:
            run_scenario(protocol, transitions, fixture)
        except LifecycleError as error:
            got = "FAIL"
            error_code = error.code

        expected = fixture.get("expect")
        expected_error = fixture.get("expected_error")
        ok = got == expected and (
            expected != "FAIL" or expected_error is None or error_code == expected_error
        )
        status = "PASS" if ok else "FAIL"
        error_text = f"/{error_code}" if error_code else ""
        expected_error_text = f"/{expected_error}" if expected_error else ""
        print(
            f"{status}: {fixture['id']} expected={expected}{expected_error_text} "
            f"got={got}{error_text}"
        )
        if not ok:
            failures.append(fixture["id"])

    if failures:
        print("lifecycle-integrity FAILED:", ", ".join(failures))
        return 1

    print(f"lifecycle-integrity PASSED: {len(fixtures.get('scenarios', []))} scenario fixtures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
