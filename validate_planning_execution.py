#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def evaluate(s):
    t = s["type"]
    f = s.get("facts", {})

    if t == "PLAN_CONTROL":
        if not f.get("approved_contract"):
            return "CONTRACT_NOT_APPROVED"
        if not f.get("contract_exact"):
            return "EXACT_CONTRACT_REQUIRED"
        if not f.get("baseline_exact"):
            return "EXACT_BASELINE_REQUIRED"
        if f.get("architecture_applicable") and not f.get("affected_architecture"):
            return "AFFECTED_ARCHITECTURE_REQUIRED"

    elif t == "ROLLING_WAVE":
        if f.get("changed_scope_inherits_review"):
            return "STALE_PLAN_REVIEW_INHERITANCE"
        if f.get("old_scope_continues") and f.get("later_revision_future_only") and f.get("impact_analysis") != "NO_EFFECT":
            return "IMPACT_ANALYSIS_REQUIRED"

    elif t == "ELABORATION":
        if not f.get("inside_envelope"):
            if not (f.get("new_plan_revision") and f.get("new_review")):
                return "ELABORATION_REQUIRES_NEW_PLAN_REVIEW"

    elif t == "READINESS":
        checks = [
            ("approved_effective_contract", "CONTRACT_NOT_APPROVED"),
            ("scoped_plan_review", "PLAN_REVIEW_NOT_READY"),
            ("effective_baseline", "BASELINE_NOT_READY"),
            ("dependencies_resolved", "DEPENDENCIES_NOT_RESOLVED"),
            ("context_ready", "CONTEXT_NOT_READY"),
            ("capabilities_ready", "CAPABILITY_NOT_READY"),
        ]
        for key, err in checks:
            if not f.get(key):
                return err
        if f.get("authority_outcome") != "ALLOWED":
            return "AUTHORITY_NOT_ALLOWED"
        if not f.get("technical_ready"):
            return "TECHNICAL_PREREQUISITE_NOT_READY"
        if not f.get("verification_strategy"):
            return "VERIFICATION_STRATEGY_REQUIRED"
        if not f.get("adaptation_boundary"):
            return "ADAPTATION_BOUNDARY_REQUIRED"
        if f.get("blocking"):
            return "BLOCKING_CONDITION_PRESENT"

    elif t == "DEPENDENCY":
        if f.get("dependency_changed") and f.get("affects_executing_scope") and not f.get("reassessed"):
            return "DEPENDENCY_REASSESSMENT_REQUIRED"

    elif t == "ROUTE":
        if f.get("contract_semantic_change"):
            expected = "PROPOSE_CONTRACT_CHANGE"
        elif f.get("unresolved_authority_risk"):
            expected = "ESCALATE"
        elif f.get("material_plan_change"):
            expected = "REPLAN"
        elif f.get("execution_failure") and f.get("reviewed_route_still_valid"):
            expected = "RETRY_EXECUTION"
        elif f.get("inside_adaptation_boundary"):
            expected = "LOCAL_ADAPTATION"
        else:
            expected = "REPLAN"
        if f.get("selected_route") != expected:
            return "ROUTE_MISMATCH"

    elif t == "WORKER":
        if f.get("changes_governed_plan_directly"):
            return "WORKER_CANNOT_MUTATE_GOVERNED_PLAN_CONTRACT"
        if f.get("material_discovery") and not f.get("promoted_to_owner"):
            return "MATERIAL_DISCOVERY_NOT_PROMOTED"

    elif t == "MICROPLAN":
        if f.get("l4_discarded") and not f.get("material_state_elsewhere"):
            return "EPHEMERAL_MICROPLAN_STATE_LOSS"

    elif t == "VALIDATION_BOUNDARY":
        if f.get("provider_done") and f.get("ae_acceptance") and not f.get("independent_validation"):
            return "PROVIDER_STATUS_NOT_VALIDATION"
        if f.get("executor_created_evidence") and f.get("ae_acceptance") and not f.get("independent_validation"):
            return "EXECUTOR_CANNOT_SELF_VALIDATE"

    elif t == "PARALLEL":
        if f.get("shared_conflict") and f.get("conflicting_branches_continue"):
            return "SHARED_CONFLICT_MUST_BLOCK"
        if f.get("independent") and f.get("blocked_branch") and not f.get("unrelated_branch_continues"):
            return "UNRELATED_SCOPE_MUST_NOT_AUTO_FREEZE"

    elif t == "VERIFICATION":
        if not f.get("proof_trace"):
            return "VERIFICATION_NOT_TRACEABLE_TO_PROOF"
        if f.get("parallel_work") and not f.get("parallel_evidence_reconciled"):
            return "PARALLEL_EVIDENCE_NOT_RECONCILED"

    elif t == "ARCHITECTURE":
        if f.get("architecture_applicable") and not f.get("affected_architecture_identified"):
            return "AFFECTED_ARCHITECTURE_REQUIRED"
        if f.get("consequential_choice") and not f.get("adr_created"):
            return "ADR_REQUIRED"
        if f.get("route_material_change") and f.get("route") != "REPLAN":
            return "ARCHITECTURE_CHANGE_REQUIRES_REPLAN"
        if f.get("baseline_silent_mutation"):
            return "BASELINE_SILENT_MUTATION_PROHIBITED"

    elif t == "RECOVERY":
        if f.get("orchestrator_lost") and not (f.get("material_state_durable") and f.get("reconstructable")):
            return "MATERIAL_STATE_NOT_RECOVERABLE"

    elif t == "REVISION_EFFECTIVITY":
        if f.get("selected_revision") != f.get("effective_revision"):
            return "WRONG_EFFECTIVE_REVISION"

    elif t == "HUMAN_COLLABORATION":
        if f.get("human_role") == "CLERICAL_PROXY" and f.get("agent_operable_operation") and f.get("human_required"):
            return "MECHANICAL_HUMAN_MIDDLEWARE"

    elif t == "ENTITY_ADMISSION":
        if f.get("new_a1_a2_execution_entity") and not f.get("identity_need_proven"):
            return "EXECUTION_ENTITY_INFLATION"

    else:
        return "UNKNOWN_SCENARIO_TYPE"

    return None


def cross_domain_checks(protocol, lifecycle, capabilities, authority, context):
    errors = []

    required_rules = [
        "rolling_wave_planning_allowed",
        "changed_scope_no_stale_review_inheritance",
        "parallel_independent_scopes_allowed",
        "local_adaptation_not_plan_mutation",
        "executor_cannot_silently_change_plan_or_contract",
        "executor_evidence_not_validation_acceptance",
        "material_state_survives_orchestrator_session_loss",
        "no_central_orchestrator_required",
        "no_new_execution_a1_a2_required",
        "correct_effective_revision_beats_latest"
    ]
    for rule in required_rules:
        if protocol.get("rules", {}).get(rule) is not True:
            errors.append(f"protocol rule missing/false: {rule}")

    lifecycle_routes = set(lifecycle.get("routes", []))
    for route in protocol["cross_domain_expectations"]["lifecycle_routes"]:
        if route not in lifecycle_routes:
            errors.append(f"lifecycle route missing: {route}")

    g2 = lifecycle.get("gates", {}).get("G2_PLAN_REVIEW", {})
    if not g2.get("exact_revision_required") or not g2.get("explicit_scope_required"):
        errors.append("L1-D G2 must remain exact-revision + explicit-scope")
    if lifecycle.get("rules", {}).get("provider_done_does_not_imply_acceptance") is not True:
        errors.append("L1-D provider Done boundary missing")
    if lifecycle.get("rules", {}).get("self_validation_acceptance_prohibited") is not True:
        errors.append("L1-D self-validation boundary missing")

    capability_ops = {
        op["operation_id"]
        for cap in capabilities.get("capabilities", [])
        for op in cap.get("operations", [])
    }
    for op in protocol["cross_domain_expectations"]["required_capability_operations"]:
        if op not in capability_ops:
            errors.append(f"required L1-E capability operation missing: {op}")

    authority_runtime = set(authority.get("runtime_outcomes", []))
    for outcome in protocol["cross_domain_expectations"]["authority_runtime_outcomes"]:
        if outcome not in authority_runtime:
            errors.append(f"L1-F runtime outcome missing: {outcome}")
    if authority.get("rules", {}).get("entitlement_is_not_authority") is not True:
        errors.append("L1-F entitlement/OA distinction missing")

    context_rules = context.get("rules", {})
    for rule in protocol["cross_domain_expectations"]["context_rules"]:
        if context_rules.get(rule) is not True:
            errors.append(f"L1-G context rule missing/false: {rule}")

    return errors


def validate_portability(fixtures):
    errors = []
    if fixtures.get("implementations", {}).get("A", {}).get("topology") == fixtures.get("implementations", {}).get("B", {}).get("topology"):
        errors.append("portability implementations must be materially different")

    keys = ["contract", "plan", "baseline", "review_scope", "route", "blockers", "validation_ready", "recoverable"]
    for case in fixtures.get("cases", []):
        a = case["A"]
        b = case["B"]
        for key in keys:
            if a.get(key) != b.get(key):
                errors.append(f"{case['id']}: governed outcome differs for {key}")
    return errors


def main():
    if len(sys.argv) != 8:
        print("usage: validate_planning_execution.py protocol scenarios portability lifecycle capabilities authority context")
        return 2

    protocol, scenarios, portability, lifecycle, capabilities, authority, context = map(load, sys.argv[1:])

    failures = []
    for scenario in scenarios.get("scenarios", []):
        error = evaluate(scenario)
        got = "FAIL" if error else "PASS"
        expected = scenario.get("expect")
        expected_error = scenario.get("expected_error")
        ok = got == expected and (expected != "FAIL" or error == expected_error)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {scenario['id']} expected={expected}" + (f"/{expected_error}" if expected_error else "") + f" got={got}" + (f"/{error}" if error else ""))
        if not ok:
            failures.append(scenario["id"])

    cross_errors = cross_domain_checks(protocol, lifecycle, capabilities, authority, context)
    for err in cross_errors:
        print("FAIL: cross-domain:", err)
    failures.extend([f"cross:{e}" for e in cross_errors])

    portability_errors = validate_portability(portability)
    for err in portability_errors:
        print("FAIL: portability:", err)
    failures.extend([f"portability:{e}" for e in portability_errors])

    if failures:
        print("planning-execution-integrity FAILED:", ", ".join(failures))
        return 1

    print(f"planning-execution-integrity PASSED: {len(scenarios.get('scenarios', []))} semantic scenarios + {len(portability.get('cases', []))} portability cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
