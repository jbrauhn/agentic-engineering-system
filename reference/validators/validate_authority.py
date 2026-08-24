#!/usr/bin/env python3
import json
import sys
from pathlib import Path

EXPECTED_HUMAN_RESERVED = {
    "engineering.intent",
    "risk.material_acceptance",
    "tradeoff.consequential",
    "contract.approval",
    "contract.change.approval",
}
ACTIVE = "ACTIVE"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def protected_operations(capabilities):
    out = set()
    for cap in capabilities.get("capabilities", []):
        for op in cap.get("operations", []):
            if op.get("protected_operation") is True:
                out.add(op["operation_id"])
    return out


def structural_errors(protocol, capabilities, lifecycle):
    errors = []
    if set(protocol.get("policy_results", [])) != {"PERMIT", "DENY", "INDETERMINATE"}:
        errors.append("policy result vocabulary mismatch")
    if set(protocol.get("runtime_outcomes", [])) != {"ALLOWED", "DENIED", "BLOCKED"}:
        errors.append("runtime outcome vocabulary mismatch")

    reserved = {x["decision_class"] for x in protocol.get("canonical_human_reserved_decision_classes", [])}
    if reserved != EXPECTED_HUMAN_RESERVED:
        errors.append(f"Human-reserved catalog drift: {sorted(reserved)}")

    reqs = protocol.get("operation_authority_requirements", {})
    default = reqs.get("default_for_l1e_protected_operation", {})
    required_true = ("identity_required", "oa_required", "policy_evaluation_required", "pep_required")
    for field in required_true:
        if default.get(field) is not True:
            errors.append(f"protected-operation default must require {field}")
    if default.get("provider_entitlement_requirement") not in {"BINDING_DETERMINED", "REQUIRED", "NOT_APPLICABLE"}:
        errors.append("protected-operation default must declare technical entitlement semantics")
    if default.get("conditions_must_reach_enforcement") is not True:
        errors.append("PERMIT conditions must reach enforcement")

    protected = protected_operations(capabilities)
    if not protected:
        errors.append("no L1-E protected operations found")
    overrides = reqs.get("overrides", {})
    unknown = set(overrides) - protected
    if unknown:
        errors.append(f"authority override references non-protected operations: {sorted(unknown)}")
    # Every protected operation resolves to an Authority Requirement through the default + optional override.
    for op in protected:
        merged = dict(default)
        merged.update(overrides.get(op, {}))
        for field in required_true:
            if merged.get(field) is not True:
                errors.append(f"{op} lacks required authority semantic {field}")

    assignment = protocol.get("authority_assignment_semantics", {})
    if assignment.get("record_type") != "A2":
        errors.append("Authority Assignment must be A2")
    if assignment.get("ae_owned_shadow_copy_required_for_external_assignment") is not False:
        errors.append("external authority must not require AE shadow assignment")
    if assignment.get("issued_history_non_destructive") is not True:
        errors.append("Authority Assignment issued history must be non-destructive")

    rules = protocol.get("rules", {})
    required_rules = [
        "entitlement_is_not_authority", "oa_is_effective_not_storage_specific",
        "da_is_not_provider_execution_permission", "indeterminate_never_permits_protected_operation",
        "canonical_constraints_not_weakened_downstream", "policy_combination_deterministic",
        "unresolved_policy_conflict_not_permit", "permit_conditions_must_be_enforced",
        "credential_entitlement_oa_da_lifetimes_independent", "historical_authorization_non_destructive",
        "delegation_optional", "delegation_non_amplifying", "canonical_human_da_not_delegable_to_ai",
        "authority_change_uses_pre_change_state", "self_escalation_prohibited", "authority_state_federated",
        "authorization_cache_not_authoritative", "distributed_peps_allowed",
        "protected_operation_requires_enforcement", "bypass_assessment_scoped_to_governed_actor_context",
        "authorization_provenance_retention_risk_policy_sensitive",
        "technical_entitlement_requirement_is_binding_specific", "no_policy_dsl_required", "no_central_pdp_or_pep_required"
    ]
    for rule in required_rules:
        if rules.get(rule) is not True:
            errors.append(f"required authority rule false/missing: {rule}")

    gates = lifecycle.get("gates", {})
    if "G1_CONTRACT_APPROVAL" not in gates or "G5_CONTRACT_CHANGE" not in gates:
        errors.append("L1-D G1/G5 gates missing")
    if gates.get("G5_CONTRACT_CHANGE", {}).get("human_decision_required") is not True:
        errors.append("L1-D G5 must require Human decision")
    dre = protocol.get("decision_requirements", {})
    if dre.get("contract.approval", {}).get("lifecycle_gate") != "G1_CONTRACT_APPROVAL":
        errors.append("Contract approval must link G1")
    cc = dre.get("contract.change.approval", {})
    if cc.get("lifecycle_gate") != "G5_CONTRACT_CHANGE" or cc.get("human_da_required") is not True:
        errors.append("Contract change approval must link Human DA + G5")

    pep = set(protocol.get("pep_proof_requirements", []))
    for field in {"enforcement_boundary", "pep_mechanism", "authority_identity_facts_consumed",
                  "conditions_obligations_enforced", "unauthorized_denial_evidence",
                  "fail_closed_when_required_authority_unknown", "governed_actor_bypass_path_assessment"}:
        if field not in pep:
            errors.append(f"PEP Proof field missing: {field}")
    return errors


def policy_and_runtime(facts):
    if not facts.get("identity", True):
        return "INDETERMINATE", "BLOCKED"

    bypass = facts.get("bypass") or {}
    if bypass.get("equivalent") and bypass.get("available_to_governed_runtime") and not bypass.get("equivalently_governed"):
        return None, "BYPASS_PATH_UNGOVERNED"

    if facts.get("policy_conflict") == "UNRESOLVED":
        return "INDETERMINATE", "BLOCKED"

    validity = facts.get("oa_validity", ACTIVE)
    if validity in {"EXPIRED", "REVOKED", "SUPERSEDED", "CONDITION_INVALID", "NOT_YET_VALID"}:
        policy = "DENY"
    elif facts.get("authoritative_revocation"):
        policy = "DENY"
    else:
        oa = facts.get("oa", "INDETERMINATE")
        if oa in {"PERMIT", "DENY", "INDETERMINATE"}:
            policy = oa
        elif oa == "ABSENT":
            policy = "DENY" if facts.get("absence_policy") == "DENY" else "INDETERMINATE"
        else:
            return None, "BAD_OA_RESULT"

    if policy == "DENY":
        return policy, "DENIED"
    if policy == "INDETERMINATE":
        return policy, "BLOCKED"

    if not facts.get("pep", True):
        return None, "PEP_REQUIRED"
    if facts.get("obligations") and not facts.get("obligations_enforced"):
        return None, "OBLIGATION_NOT_ENFORCED"
    if facts.get("entitlement", "PRESENT") == "MISSING":
        return policy, "BLOCKED"
    if facts.get("provider", "AVAILABLE") != "AVAILABLE":
        return policy, "BLOCKED"
    return policy, "ALLOWED"


def evaluate_decision(s):
    if s.get("decision_class") in EXPECTED_HUMAN_RESERVED and s.get("actor_kind") != "HUMAN":
        return "HUMAN_DA_REQUIRED"
    if s.get("da") != "PERMIT" or s.get("da_validity", ACTIVE) != ACTIVE:
        return "DA_NOT_ACTIVE"
    if not s.get("da_scope_match"):
        return "DA_SCOPE_MISMATCH"
    if not s.get("authoritative_decision"):
        return "AUTHORITY_DECISION_INVALID"
    if not s.get("exact_target"):
        return "EXACT_TARGET_REQUIRED"
    if s.get("decision_class") == "contract.change.approval":
        if s.get("gate") != "G5_CONTRACT_CHANGE" or not s.get("gate_target_match"):
            return "GATE_TARGET_MISMATCH"
    return None


def evaluate_other(s):
    kind = s["kind"]
    if kind == "mutation":
        if s.get("uses_postchange_authority") or (s.get("actor_is_subject") and not s.get("prechange_authorized")):
            return "SELF_ESCALATION"
        return None
    if kind == "delegation":
        if not s.get("delegator_authorized"):
            return "DELEGATOR_NOT_AUTHORIZED"
        if not s.get("within_delegable_scope"):
            return "DELEGATION_AMPLIFIES_AUTHORITY"
        if s.get("is_onward") and not s.get("onward_allowed"):
            return "ONWARD_DELEGATION_NOT_ALLOWED"
        if s.get("human_reserved_to_ai"):
            return "CANONICAL_HUMAN_DA_NOT_DELEGABLE_TO_AI"
        return None
    if kind == "history":
        return "HISTORY_REWRITTEN" if s.get("historical_record_mutated") else None
    if kind == "federation":
        if not s.get("authoritative_source_known"):
            return "AUTHORITY_SOURCE_UNKNOWN"
        if s.get("shadow_copy_claimed_required"):
            return "SHADOW_AUTHORITY_COPY_REQUIRED"
        return None
    return "UNKNOWN_SCENARIO_KIND"


def check_scenario(s):
    kind = s["kind"]
    if kind == "operation":
        policy, runtime_or_error = policy_and_runtime(s)
        if policy is None:
            error = runtime_or_error
            got = "FAIL"
        else:
            error = None
            got = "PASS"
            if policy != s.get("expected_policy") or runtime_or_error != s.get("expected_runtime"):
                return False, f"policy/runtime mismatch got={policy}/{runtime_or_error}"
    elif kind == "decision":
        error = evaluate_decision(s)
        got = "FAIL" if error else "PASS"
    else:
        error = evaluate_other(s)
        got = "FAIL" if error else "PASS"

    expected = s.get("expect", "PASS")
    if got != expected:
        return False, f"expected={expected} got={got}/{error}"
    if expected == "FAIL" and s.get("expected_error") != error:
        return False, f"expected_error={s.get('expected_error')} got={error}"
    return True, "ok"


def portability_errors(fixtures):
    errors = []
    impls = fixtures.get("implementations", {})
    if len(impls) < 2:
        return ["need at least two authority implementations"]
    models = {v.get("model") for v in impls.values()}
    if len(models) < 2:
        errors.append("authority portability implementations are not materially different")
    for case in fixtures.get("cases", []):
        outcomes = []
        for _name in sorted(impls):
            p, r = policy_and_runtime(case["facts"])
            outcomes.append((p, r))
        if len(set(outcomes)) != 1:
            errors.append(f"{case['id']} implementations disagree: {outcomes}")
        if outcomes[0] != (case["expected_policy"], case["expected_runtime"]):
            errors.append(f"{case['id']} wrong canonical outcome: {outcomes[0]}")
        print(f"PASS: {case['id']} equivalent={outcomes[0]}")
    return errors


def main():
    if len(sys.argv) != 6:
        print("usage: validate_authority.py authority_protocol.json authority_scenarios.json authority_portability_fixtures.json capability_contracts.json lifecycle_protocol.json")
        return 2
    protocol, scenarios, portability, capabilities, lifecycle = map(load, sys.argv[1:])
    failures = structural_errors(protocol, capabilities, lifecycle)
    for s in scenarios.get("scenarios", []):
        ok, detail = check_scenario(s)
        print(f"{'PASS' if ok else 'FAIL'}: {s['id']} {detail}")
        if not ok:
            failures.append(s["id"])
    failures += portability_errors(portability)
    if failures:
        print("authority-integrity FAILED:")
        for f in failures:
            print(" -", f)
        return 1
    print(f"authority-integrity PASSED: {len(scenarios.get('scenarios', []))} semantic scenarios + {len(portability.get('cases', []))} portability cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
