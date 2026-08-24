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


def validate_cross_domain(protocol, lifecycle, capabilities, authority, context, planning, validation):
    errors = []
    domain = protocol.get("domain_semantics", {})
    if domain.get("standards_applicability") != "B":
        errors.append("Standards applicability must remain subordinate B")
    if domain.get("engineering_health_finding") != "A2":
        errors.append("Engineering Health Finding must be explicit A2 extension")
    if domain.get("effective_standards_health_view") != "D" or domain.get("health_current_disposition") != "D":
        errors.append("Effective/current standards-health views must remain derived D")

    lifecycle_routes = set(lifecycle.get("routes", []))
    if not set(protocol.get("cross_domain_expectations", {}).get("lifecycle_routes", [])).issubset(lifecycle_routes):
        errors.append("L1-J lifecycle routes drift from L1-D")
    if set(protocol.get("cross_domain_expectations", {}).get("capability_operational_impacts", [])) != set(capabilities.get("operational_impacts", [])):
        errors.append("L1-J capability impact reference drifts from L1-E")
    for rule in protocol.get("cross_domain_expectations", {}).get("authority_rules", []):
        if not authority.get("rules", {}).get(rule):
            errors.append(f"L1-F authority rule missing or false: {rule}")
    for rule in protocol.get("cross_domain_expectations", {}).get("context_rules", []):
        if not context.get("rules", {}).get(rule):
            errors.append(f"L1-G context rule missing or false: {rule}")
    if not set(protocol.get("cross_domain_expectations", {}).get("planning_execution_routes", [])).issubset(set(planning.get("execution_routes", []))):
        errors.append("L1-J planning/execution routes drift from L1-H")
    if planning.get("verification_chain") != protocol.get("cross_domain_expectations", {}).get("planning_execution_verification_chain", []):
        errors.append("L1-J Proof/Verification/Evidence/Validation chain drifts from L1-H")
    for rule in protocol.get("cross_domain_expectations", {}).get("validation_rules", []):
        if not validation.get("rules", {}).get(rule):
            errors.append(f"L1-I Validation rule missing or false: {rule}")

    required_rules = [
        "standards_applicability_subordinate_b", "engineering_health_finding_a2_explicit_extension",
        "historical_l1c_not_rewritten", "applicability_distinct_from_application_disposition",
        "mandatory_cannot_use_proportional_omission", "correct_effective_version_beats_latest",
        "standards_do_not_replace_contract_proof", "framework_name_not_health_condition",
        "capability_gap_distinct_from_health_finding", "remediation_validation_independent",
        "health_history_non_destructive", "current_health_disposition_derived",
        "no_universal_maturity_score", "no_universal_named_framework",
        "no_central_standards_health_service_required"
    ]
    for rule in required_rules:
        if not protocol.get("rules", {}).get(rule):
            errors.append(f"L1-J required rule missing or false: {rule}")
    return errors


def validate_scenario(s):
    # Entity and architecture guardrails.
    entity = s.get("new_convenience_entity")
    if entity == "HealthAssessment":
        return "HEALTH_ENTITY_INFLATION"
    if entity == "StandardsApplicabilityDetermination":
        return "APPLICABILITY_ENTITY_INFLATION"
    if s.get("central_standards_health_service_required"):
        return "CENTRAL_STANDARDS_HEALTH_SERVICE_NOT_CANONICAL"
    if s.get("universal_maturity_score_required"):
        return "UNIVERSAL_MATURITY_SCORE_PROHIBITED"
    if s.get("universal_named_framework_required"):
        return "UNIVERSAL_FRAMEWORK_PROHIBITED"
    if s.get("universal_remediation_before_adoption") or s.get("low_impact_blocks_adoption"):
        return "NO_UNIVERSAL_REMEDIATION_BEFORE_ADOPTION"
    if s.get("universal_human_da_for_applicability"):
        return "UNIVERSAL_APPLICABILITY_HUMAN_DA_PROHIBITED"
    if s.get("universal_independent_validation_for_finding"):
        return "UNIVERSAL_FINDING_INDEPENDENCE_PROHIBITED"
    if not s.get("health_a2_extension_explicit"):
        return "HEALTH_A2_EXTENSION_MUST_BE_EXPLICIT"
    if s.get("historical_l1c_rewritten"):
        return "HISTORICAL_L1C_MUST_NOT_BE_REWRITTEN"
    if s.get("collapsed_applicability_disposition"):
        return "APPLICABILITY_DISPOSITION_MUST_REMAIN_DISTINCT"
    if s.get("standards_applicability_authorizes_operation"):
        return "STANDARDS_NOT_AUTHORIZATION_POLICY"
    if s.get("copied_standard_becomes_authority"):
        return "COPIED_STANDARD_NOT_SOURCE_AUTHORITY"

    # Standards are conditional context: an Engineering Health Finding does not require a standards source.
    if s.get("standards_context_present", True):
        if not s.get("source_reference") or not s.get("source_authoritative"):
            return "AUTHORITATIVE_STANDARD_SOURCE_REQUIRED"
        if not s.get("effectivity_basis_known"):
            return "EFFECTIVITY_BASIS_REQUIRED"
        if not s.get("applicability_rationale"):
            return "APPLICABILITY_RATIONALE_REQUIRED"

        character = s.get("requirement_character")
        applicability = s.get("applicability")
        disposition = s.get("disposition")

        if disposition == "PROPORTIONATELY_NOT_USED" and character != "ADVISORY":
            return "PROPORTIONAL_OMISSION_ADVISORY_ONLY"
        if character == "CONDITIONAL":
            if s.get("conditional_trigger_met") and applicability != "APPLIES":
                return "CONDITIONAL_TRIGGER_REQUIRES_APPLIES"
            if not s.get("conditional_trigger_met") and applicability not in {"CONDITIONAL_PENDING", "DOES_NOT_APPLY"}:
                return "CONDITIONAL_TRIGGER_STATE_INVALID"
            if applicability == "CONDITIONAL_PENDING" and s.get("protected_work_proceeds"):
                return "CONDITIONAL_PENDING_FAILS_CLOSED"

        if applicability == "UNRESOLVED_REQUIRES_DECISION" and character in {"MANDATORY", "CONDITIONAL"} and s.get("protected_work_proceeds"):
            return "UNRESOLVED_MANDATORY_FAILS_CLOSED"

        if disposition == "AUTHORIZED_EXCEPTION_WAIVER":
            if not s.get("exception_allowed") or not s.get("exception_authority"):
                return "EXCEPTION_AUTHORITY_REQUIRED"
            if not s.get("exception_scope_version_exact"):
                return "EXCEPTION_SCOPE_VERSION_REQUIRED"
            if not s.get("exception_provenance"):
                return "EXCEPTION_PROVENANCE_REQUIRED"

        if s.get("selected_version") != s.get("effective_version") and s.get("newer_version_auto_selected"):
            return "LATEST_VERSION_NOT_EFFECTIVE_BY_DEFAULT"
        if s.get("newly_effective_requirement") and s.get("active_work_affected") and not s.get("effectivity_impact_handled"):
            return "NEW_EFFECTIVE_REQUIREMENT_REASSESSMENT_REQUIRED"
        if s.get("product_weakens_mandatory"):
            return "PRODUCT_CANNOT_SILENTLY_WEAKEN"
        if s.get("standards_replace_contract_proof"):
            return "STANDARDS_NOT_SECOND_CONTRACT"
        if s.get("context_summary_as_authority"):
            return "CONTEXT_NOT_STANDARD_AUTHORITY"
        if s.get("effective_view_authoritative_shadow"):
            return "EFFECTIVE_VIEW_MUST_BE_DERIVED"

        if applicability == "APPLIES" and disposition == "SATISFIED":
            if s.get("checklist_only"):
                return "CHECKLIST_NOT_EVIDENCE"
            if character in {"MANDATORY", "CONDITIONAL"} and not s.get("evidence_demonstrated"):
                return "APPLICATION_EVIDENCE_REQUIRED"

    # Capability gap and engineering-health separation.
    if s.get("missing_canonical_capability_operation") and s.get("mislabeled_capability_gap_as_health"):
        return "CAPABILITY_GAP_NOT_HEALTH_SUBSTITUTE"
    if s.get("serious_health_ignored_due_capabilities"):
        return "SERIOUS_HEALTH_CANNOT_BE_IGNORED"

    # Engineering Health Finding A2 semantics.
    if s.get("health_finding"):
        if not s.get("finding_id"):
            return "HEALTH_FINDING_IDENTITY_REQUIRED"
        if not s.get("finding_scope"):
            return "HEALTH_FINDING_SCOPE_REQUIRED"
        if not s.get("underlying_condition") or s.get("framework_name_as_condition"):
            return "UNDERLYING_HEALTH_CONDITION_REQUIRED"
        if not s.get("health_evidence_refs"):
            return "HEALTH_FINDING_EVIDENCE_REQUIRED"
        if not s.get("health_provenance"):
            return "HEALTH_FINDING_PROVENANCE_REQUIRED"
        if not s.get("health_currentness_basis"):
            return "HEALTH_FINDING_CURRENTNESS_REQUIRED"
        if s.get("tool_output_only_is_authoritative_finding"):
            return "TOOL_OUTPUT_NOT_AUTHORITATIVE_FINDING"
        if s.get("health_history_rewritten"):
            return "HEALTH_HISTORY_NON_DESTRUCTIVE"

        current = s.get("health_current_disposition")
        basis = s.get("current_disposition_basis")
        valid_basis = {
            "ACTIVE": {"ISSUED_FINDING", "CURRENT_EVIDENCE", "OTHER_AUTHORITATIVE_STATE"},
            "DEFERRED": {"DECISION_RECORD", "AUTHORITY_DECISION", "OTHER_AUTHORITATIVE_STATE"},
            "ACCEPTED_RISK": {"AUTHORITY_DECISION"},
            "REMEDIATED": {"VALIDATION_RECORD"},
            "SUPERSEDED": {"SUPERSEDING_FINDING"},
            "QUALIFIED_UNKNOWN": {"CURRENTNESS_OR_EVIDENCE_ASSESSMENT", "OTHER_AUTHORITATIVE_STATE"}
        }
        if basis not in valid_basis.get(current, set()):
            return "CURRENT_DISPOSITION_REQUIRES_AUTHORITATIVE_BASIS"

    # Remediation and lifecycle routing.
    if s.get("remediation") and s.get("remediation_success_claimed"):
        if (not s.get("remediation_validation_independent")) or s.get("remediation_producer") == s.get("remediation_validator"):
            return "REMEDIATION_REQUIRES_INDEPENDENT_VALIDATION"
    if s.get("contract_deficiency") and s.get("route") != "PROPOSE_CONTRACT_CHANGE":
        return "CONTRACT_DEFICIENCY_REQUIRES_G5_ROUTE"
    if s.get("reviewed_route_changes") and not s.get("inside_adaptation_boundary") and s.get("route") != "REPLAN":
        return "ROUTE_REPLAN_REQUIRED"
    if s.get("unresolved_risk_authority_policy"):
        if s.get("route") != "ESCALATE" or s.get("protected_work_proceeds"):
            return "UNRESOLVED_GOVERNANCE_REQUIRES_ESCALATION"
    if s.get("explicit_deferral_or_risk_acceptance") and not s.get("deferral_risk_provenance"):
        return "DEFERRAL_RISK_PROVENANCE_REQUIRED"
    return None


def validate_portability(fixtures):
    failures = []
    impls = fixtures.get("implementations", {})
    a = impls.get("A", {})
    b = impls.get("B", {})
    if not a or not b:
        return ["PORTABILITY_IMPLEMENTATIONS_MISSING"]
    if a.get("central_standards_health_service") or b.get("central_standards_health_service"):
        failures.append("CENTRAL_STANDARDS_HEALTH_SERVICE_NOT_CANONICAL")
    if a.get("numeric_maturity_model_required") or b.get("numeric_maturity_model_required"):
        failures.append("UNIVERSAL_MATURITY_SCORE_PROHIBITED")
    if a.get("standards_topology") == b.get("standards_topology") and a.get("assessment_topology") == b.get("assessment_topology"):
        failures.append("PORTABILITY_TOPOLOGIES_NOT_MATERIALLY_DIFFERENT")
    if a.get("framework_vocabulary") == b.get("framework_vocabulary"):
        failures.append("PORTABILITY_FRAMEWORKS_NOT_MATERIALLY_DIFFERENT")

    fields = fixtures.get("equivalence_fields", [])
    for case in fixtures.get("cases", []):
        av = case.get("A", {})
        bv = case.get("B", {})
        for field in fields:
            if av.get(field) != bv.get(field):
                failures.append(f"{case.get('id')}:PORTABILITY_SEMANTIC_MISMATCH:{field}")
    return failures


def main():
    if len(sys.argv) != 10:
        print("usage: validate_standards_health.py standards_health_protocol.json standards_health_scenarios.json standards_health_portability_fixtures.json lifecycle_protocol.json capability_contracts.json authority_protocol.json context_protocol.json planning_execution_protocol.json validation_protocol.json")
        return 2

    protocol, fixtures, portability, lifecycle, capabilities, authority, context, planning, validation = [load(p) for p in sys.argv[1:]]
    cross_errors = validate_cross_domain(protocol, lifecycle, capabilities, authority, context, planning, validation)
    if cross_errors:
        for error in cross_errors:
            print("FAIL cross-domain:", error)
        return 1

    defaults = fixtures.get("defaults", {})
    failures = []
    for raw in fixtures.get("scenarios", []):
        scenario = merged(defaults, raw)
        error = validate_scenario(scenario)
        got = "FAIL" if error else "PASS"
        expected = raw.get("expect")
        expected_error = raw.get("expected_error")
        ok = got == expected and (expected != "FAIL" or error == expected_error)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {raw.get('id')} expected={expected}" + (f"/{expected_error}" if expected_error else "") + f" got={got}" + (f"/{error}" if error else ""))
        if not ok:
            failures.append(raw.get("id"))

    portability_failures = validate_portability(portability)
    for failure in portability_failures:
        print("FAIL portability:", failure)
    failures.extend(portability_failures)
    if failures:
        print("standards-health-integrity FAILED:", ", ".join(failures))
        return 1
    print(f"standards-health-integrity PASSED: {len(fixtures.get('scenarios', []))} semantic scenarios + {len(portability.get('cases', []))} portability cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())