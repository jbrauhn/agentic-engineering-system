#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def merged(defaults, scenario):
    result = dict(defaults)
    result.update(scenario)
    return result


def validate_cross_domain(protocol, lifecycle, capabilities, authority, context, planning):
    errors = []

    g4 = lifecycle.get("gates", {}).get("G4_VALIDATION_ACCEPTANCE")
    if not g4 or not g4.get("independent_judgment_required"):
        errors.append("L1-D G4 independent judgment invariant missing")

    lifecycle_routes = set(lifecycle.get("routes", []))
    if not set(protocol.get("lifecycle_routes", [])).issubset(lifecycle_routes):
        errors.append("L1-I lifecycle routes drift from L1-D")

    validation_cap = next((c for c in capabilities.get("capabilities", []) if c.get("capability_id") == "validation"), None)
    cap_ops = {o.get("operation_id") for o in (validation_cap or {}).get("operations", [])}
    required_ops = set(protocol.get("cross_domain_expectations", {}).get("validation_capability_operations", []))
    if not required_ops.issubset(cap_ops):
        errors.append("L1-I Validation capability operations drift from L1-E")

    if set(protocol.get("cross_domain_expectations", {}).get("authority_runtime_outcomes", [])) != set(authority.get("runtime_outcomes", [])):
        errors.append("L1-I authority runtime outcomes drift from L1-F")

    for rule in protocol.get("cross_domain_expectations", {}).get("context_rules", []):
        if not context.get("rules", {}).get(rule):
            errors.append(f"L1-G context rule missing or false: {rule}")

    expected_chain = protocol.get("cross_domain_expectations", {}).get("planning_execution_verification_chain", [])
    if planning.get("verification_chain") != expected_chain:
        errors.append("L1-I Verification/Evidence chain drifts from L1-H")

    if not protocol.get("rules", {}).get("judgment_path_independence_universal"):
        errors.append("judgment-path independence invariant missing")
    if not protocol.get("rules", {}).get("validation_judgment_distinct_from_lifecycle_route"):
        errors.append("R6 judgment/R1 route separation missing")
    if not protocol.get("rules", {}).get("no_new_validation_a1_a2_required"):
        errors.append("entity-admission guardrail missing")
    if protocol.get("validation_requirement_type") != "B":
        errors.append("Validation Requirement must remain subordinate B")

    return errors


def validate_scenario(s):
    if s.get("new_validation_entity_type"):
        return "VALIDATION_ENTITY_INFLATION"
    if s.get("central_validator_required"):
        return "CENTRAL_VALIDATOR_NOT_CANONICAL"
    if not s.get("same_core_protocol", True):
        return "ONE_CORE_VALIDATION_PROTOCOL_REQUIRED"
    if s.get("fresh_provider_required_without_policy"):
        return "UNIVERSAL_STRENGTHENING_PROHIBITED"
    if s.get("human_validator_required_without_policy"):
        return "UNIVERSAL_HUMAN_VALIDATOR_PROHIBITED"

    if not s.get("record_contract_revision"):
        return "EXACT_CONTRACT_REQUIRED"
    if s.get("record_contract_revision") != s.get("requirement_contract_revision"):
        return "WRONG_CONTRACT_REVISION"
    if s.get("validator_path") == s.get("producer_path"):
        return "SELF_ACCEPTANCE"
    if s.get("role_label_only") or not s.get("validator_identity") or not s.get("independence_provenance"):
        return "VALIDATOR_IDENTITY_PROVENANCE_REQUIRED"

    required_ind = set(s.get("policy_required_independence", []))
    satisfied_ind = set(s.get("policy_satisfied_independence", []))
    if not required_ind.issubset(satisfied_ind):
        return "POLICY_INDEPENDENCE_UNSATISFIED"
    if s.get("human_da_required") and not s.get("human_da_satisfied"):
        return "SEPARATE_AUTHORITY_REQUIREMENT_UNSATISFIED"

    if s.get("evidence_reference_manipulation"):
        return "EVIDENCE_REFERENCE_INDEPENDENCE_BYPASS"
    if not s.get("parallel_evidence_scope_provenance_preserved"):
        return "PARALLEL_EVIDENCE_SCOPE_PROVENANCE_REQUIRED"

    if s.get("later_invalidation") and s.get("historical_records_rewritten"):
        return "HISTORY_MUST_BE_NON_DESTRUCTIVE"
    if s.get("later_invalidation") and not s.get("revalidation_or_escalation_triggered"):
        return "CURRENT_RELIANCE_RESPONSE_REQUIRED"

    # Increment acceptance can never substitute for final Contract Validation.
    if s.get("scope_type") == "FINAL_CONTRACT" and s.get("increment_acceptance_used_as_final"):
        return "INCREMENT_NOT_FINAL_CONTRACT"

    if s.get("validator_mutates_contract"):
        return "VALIDATOR_CANNOT_MUTATE_CONTRACT"
    if s.get("judgment") == "CONTRACT_OR_PROOF_DEFICIENCY_DETECTED" and not s.get("g5_route_used"):
        return "CONTRACT_DEFICIENCY_REQUIRES_G5_ROUTE"

    allowed_routes = {
        "PROOF_SATISFIED": {"ACCEPT"},
        "PROOF_NOT_SATISFIED_EVIDENCE_INCOMPLETE": {"RETRY_EXECUTION", "ESCALATE"},
        "PROOF_NOT_SATISFIED_IMPLEMENTATION_DEFECT": {"RETRY_EXECUTION", "REPLAN"},
        "PROOF_NOT_SATISFIED_PLAN_ROUTE_DEFICIENT": {"REPLAN"},
        "CONTRACT_OR_PROOF_DEFICIENCY_DETECTED": {"PROPOSE_CONTRACT_CHANGE"},
        "UNABLE_TO_ESTABLISH_TRUSTWORTHY_EVIDENCE_OR_STATE": {"ESCALATE"},
    }
    if s.get("route") not in allowed_routes.get(s.get("judgment"), set()):
        return "JUDGMENT_ROUTE_MISMATCH"
    if s.get("route") == "RETRY_EXECUTION" and not s.get("prior_failed_validation_preserved"):
        return "FAILED_VALIDATION_HISTORY_REQUIRED"
    if s.get("route") == "REPLAN" and not s.get("prior_plan_validation_history_preserved"):
        return "PRIOR_PLAN_VALIDATION_HISTORY_REQUIRED"

    # Acceptance-specific sufficiency. Non-accept judgments may validly diagnose missing/indeterminate Evidence.
    if s.get("judgment") == "PROOF_SATISFIED":
        if not s.get("independent_source_resolution"):
            return "MATERIAL_SOURCE_NOT_INDEPENDENTLY_RESOLVED"
        if s.get("provider_green_only"):
            return "PROVIDER_GREEN_NOT_VALIDATION"
        if s.get("context_package_only"):
            return "CONTEXT_PACKAGE_NOT_EVIDENCE"
        if s.get("validation_provider_only") and s.get("provider_result_is_canonical_judgment"):
            return "PROVIDER_RESULT_NOT_CANONICAL_JUDGMENT"

        required_proof = set(s.get("required_proof", []))
        covered_proof = set(s.get("covered_proof", []))
        if not required_proof.issubset(covered_proof):
            return "PROOF_COVERAGE_INCOMPLETE"
        if not s.get("evidence_authoritative"):
            return "EVIDENCE_AUTHORITY_INDETERMINATE"
        if not s.get("evidence_integrity"):
            return "EVIDENCE_INTEGRITY_FAILED"
        if s.get("evidence_currentness") != "CURRENT" or s.get("evidence_reliance") in {"UNRELIABLE", "UNKNOWN"}:
            return "EVIDENCE_NOT_CURRENT_RELIABLE"
        if s.get("contradictory_evidence") and not s.get("contradiction_dispositioned"):
            return "CONTRADICTORY_EVIDENCE_UNRESOLVED"

        # Full final reconciliation is required to support final Contract acceptance.
        if s.get("scope_type") == "FINAL_CONTRACT":
            if not s.get("final_reconciliation"):
                return "FINAL_RECONCILIATION_REQUIRED"
            if s.get("reused_prior_validation") and not s.get("current_reliance_rechecked"):
                return "REUSED_EVIDENCE_RELIANCE_NOT_RECHECKED"
            if not s.get("cross_scope_reconciled"):
                return "FINAL_CROSS_SCOPE_RECONCILIATION_REQUIRED"

    return None


def validate_portability(fixtures):
    failures = []
    impls = fixtures.get("implementations", {})
    a = impls.get("A", {})
    b = impls.get("B", {})
    if not a or not b:
        failures.append("PORTABILITY_IMPLEMENTATIONS_MISSING")
        return failures
    if a.get("central_validator_service") or b.get("central_validator_service"):
        failures.append("CENTRAL_VALIDATOR_NOT_CANONICAL")
    if a.get("validator_topology") == b.get("validator_topology") and a.get("evidence_topology") == b.get("evidence_topology"):
        failures.append("PORTABILITY_TOPOLOGIES_NOT_MATERIALLY_DIFFERENT")

    fields = fixtures.get("equivalence_fields", [])
    for case in fixtures.get("cases", []):
        av = case.get("A", {})
        bv = case.get("B", {})
        for field in fields:
            if av.get(field) != bv.get(field):
                failures.append(f"{case.get('id')}:PORTABILITY_SEMANTIC_MISMATCH:{field}")
        if not av.get("independent") or not bv.get("independent"):
            failures.append(f"{case.get('id')}:PORTABILITY_INDEPENDENCE_MISSING")
    return failures


def main():
    if len(sys.argv) != 9:
        print("usage: validate_validation.py validation_protocol.json validation_scenarios.json validation_portability_fixtures.json lifecycle_protocol.json capability_contracts.json authority_protocol.json context_protocol.json planning_execution_protocol.json")
        return 2

    protocol, fixtures, portability, lifecycle, capabilities, authority, context, planning = [load(p) for p in sys.argv[1:]]

    cross_errors = validate_cross_domain(protocol, lifecycle, capabilities, authority, context, planning)
    if cross_errors:
        for err in cross_errors:
            print("FAIL cross-domain:", err)
        return 1

    defaults = fixtures.get("defaults", {})
    failures = []
    for raw in fixtures.get("scenarios", []):
        s = merged(defaults, raw)
        error = validate_scenario(s)
        got = "FAIL" if error else "PASS"
        expected = raw.get("expect")
        expected_error = raw.get("expected_error")
        ok = got == expected and (expected != "FAIL" or error == expected_error)
        status = "PASS" if ok else "FAIL"
        print(
            f"{status}: {raw.get('id')} expected={expected}"
            + (f"/{expected_error}" if expected_error else "")
            + f" got={got}"
            + (f"/{error}" if error else "")
        )
        if not ok:
            failures.append(raw.get("id"))

    portability_failures = validate_portability(portability)
    for failure in portability_failures:
        print("FAIL portability:", failure)
    failures.extend(portability_failures)

    if failures:
        print("validation-integrity FAILED:", ", ".join(failures))
        return 1

    print(f"validation-integrity PASSED: {len(fixtures.get('scenarios', []))} semantic scenarios + {len(portability.get('cases', []))} portability cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
