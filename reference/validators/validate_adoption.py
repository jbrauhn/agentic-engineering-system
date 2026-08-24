#!/usr/bin/env python3
import copy
import hashlib
import json
import sys
from pathlib import Path


def load(p):
    return json.loads(Path(p).read_text())


def merged(d, s):
    x = dict(d)
    x.update(s)
    return x


def canonical_capability_map(capability_contracts):
    return {c['name']: c['capability_id'] for c in capability_contracts['capabilities']}


def cross(protocol, context, cap, auth, lifecycle, validation, standards, obs):
    e = []
    if context.get('domain_semantics', {}).get('bootstrap_descriptor') != 'B':
        e.append('Bootstrap Descriptor drift')
    have = set(context.get('bootstrap_discoveries', []))
    for x in protocol['cross_domain_expectations']['context_bootstrap_discoveries']:
        if x not in have:
            e.append('context discovery missing ' + x)
    captext = json.dumps(cap)
    for x in protocol['cross_domain_expectations']['capability_impacts']:
        if x not in captext:
            e.append('capability impact missing ' + x)
    authtext = json.dumps(auth)
    for x in protocol['cross_domain_expectations']['authority_runtime_outcomes']:
        if x not in authtext:
            e.append('authority outcome missing ' + x)
    ltext = json.dumps(lifecycle)
    for x in protocol['cross_domain_expectations']['lifecycle_routes']:
        if x not in ltext:
            e.append('lifecycle route missing ' + x)
    if protocol['cross_domain_expectations']['validation_scope'] not in validation.get('validation_scope_types', []):
        e.append('installation adoption validation scope missing')
    if not standards.get('rules', {}).get('capability_gap_distinct_from_health_finding'):
        e.append('health/capability separation missing')
    if not obs.get('rules', {}).get('learning_record_material_only'):
        e.append('learning semantics missing')
    return e


def validate(s):
    if not s.get('release_identity'):
        return 'RELEASE_IDENTITY_REQUIRED'
    if not s.get('layer_distinction') or s.get('core_authority_ambiguous'):
        return 'DISTRIBUTION_LAYER_AUTHORITY_REQUIRED' if not s.get('layer_distinction') else 'CORE_AUTHORITY_MUST_BE_DETERMINATE'
    if not s.get('reference_technology_replaceable'):
        return 'REFERENCE_TECHNOLOGY_MUST_BE_REPLACEABLE'
    if s.get('starter_redefines_core'):
        return 'STARTER_CANNOT_REDEFINE_CORE'
    if s.get('candidate_self_conforming') or not s.get('independent_adoption_validation'):
        return 'CONFORMANCE_REQUIRES_VALIDATION' if s.get('candidate_self_conforming') else 'INDEPENDENT_ADOPTION_VALIDATION_REQUIRED'
    if not s.get('exact_revisions'):
        return 'EXACT_CONFORMANCE_TARGET_REQUIRED'
    if s.get('provider_install_success') and s.get('claims_conformance_from_install'):
        return 'PROVIDER_INSTALL_NOT_CONFORMANCE'
    if not s.get('partial_scope_explicit'):
        return 'SCOPED_CONFORMANCE_MUST_BE_EXPLICIT'
    if s.get('silent_rebase'):
        return 'NO_SILENT_REBASE'
    if s.get('material_drift') and not s.get('reassessment'):
        return 'MATERIAL_DRIFT_REASSESSMENT_REQUIRED'
    if not s.get('historical_reconstructable'):
        return 'HISTORICAL_CONFORMANCE_RECONSTRUCTABLE_REQUIRED'
    if s.get('fresh_session') and s.get('hidden_context'):
        return 'FRESH_SESSION_HIDDEN_CONTEXT_PROHIBITED'
    if s.get('fresh_session') and s.get('required_semantic_input_missing'):
        return 'FRESH_SESSION_REQUIRED_INPUT_MISSING'
    if s.get('fresh_session') and not s.get('cleanroom_plan_rubric_complete'):
        return 'FRESH_SESSION_RUBRIC_COMPLETE_REQUIRED'
    if s.get('fresh_session') and s.get('fresh_session_one_provider_optimized'):
        return 'FRESH_SESSION_PROVIDER_NEUTRAL'
    if not s.get('capability_gap_distinct_health'):
        return 'CAPABILITY_HEALTH_GAPS_DISTINCT'
    if s.get('technical_available') and not s.get('agent_operable'):
        return 'AGENT_OPERABILITY_REQUIRED'
    if s.get('technical_available') and not s.get('entitleable'):
        return 'ENTITLEABILITY_REQUIRED'
    if not s.get('work_allowed'):
        return 'DIRECT_AGENT_WORK_MANAGEMENT_REQUIRED'
    if not s.get('work_denied_out_scope'):
        return 'OUT_OF_SCOPE_OPERATION_MUST_DENY'
    if s.get('human_mechanical_proxy'):
        return 'NO_ROUTINE_HUMAN_MECHANICAL_PROXY'
    if s.get('mandatory_environment_mechanism'):
        return 'NO_MANDATORY_ENVIRONMENT_MECHANISM'
    if s.get('missing_interface') and s.get('gap_impact') not in {'BLOCK', 'CONSTRAIN', 'DEGRADE'}:
        return 'MISSING_INTERFACE_MUST_BE_GAP'
    if s.get('derived_view_authority'):
        return 'DERIVED_VIEW_NOT_AUTHORITY'
    if not s.get('integrity_without_git'):
        return 'DISTRIBUTION_INTEGRITY_NOT_GIT_REQUIRED'
    if not s.get('start_here'):
        return 'START_HERE_REQUIRED'
    if s.get('field_guide_override'):
        return 'FIELD_GUIDE_NOT_CANONICAL_AUTHORITY'
    if s.get('new_entity') is not None:
        return 'ADOPTION_ENTITY_INFLATION'
    if s.get('kestrel_present'):
        return 'KESTREL_PROHIBITED_GENERIC_INPUT'
    if not s.get('final_install_accept_independent'):
        return 'INSTALL_ACCEPTANCE_INDEPENDENT_VALIDATION_REQUIRED'
    if s.get('final_part1_self_accept'):
        return 'FINAL_PART1_ACCEPTANCE_HUMAN_OWNER'
    if not s.get('distribution_provenance'):
        return 'DISTRIBUTION_PROVENANCE_REQUIRED'
    if s.get('latest_release_used_without_effectivity'):
        return 'CORRECT_EFFECTIVE_RELEASE_REQUIRED'
    if s.get('drift_trivial') and s.get('full_revalidation_for_trivial'):
        return 'REASSESSMENT_MUST_BE_PROPORTIONAL'
    if s.get('adoption_special_validation_entity'):
        return 'USE_EXISTING_VALIDATION_RECORD'
    if s.get('adoption_plan_entity') or not s.get('normal_plan'):
        return 'USE_NORMAL_PLAN'
    if s.get('gap_reports_authoritative'):
        return 'GAP_VIEWS_DERIVED_ONLY'
    if s.get('universal_score'):
        return 'NO_UNIVERSAL_CONFORMANCE_SCORE'
    if s.get('certification_claim'):
        return 'CONFORMANCE_NOT_CERTIFICATION'
    if s.get('reference_loop_bypasses_authority'):
        return 'REFERENCE_LOOP_MUST_USE_NORMAL_GOVERNANCE'
    if s.get('backward_path') and s.get('history_rewritten'):
        return 'BACKWARD_ROUTE_HISTORY_NON_DESTRUCTIVE'
    if s.get('bootstrap_descriptor_duplicated'):
        return 'REUSE_BOOTSTRAP_DESCRIPTOR'
    return None


def verify_distribution(dist, manifest):
    e = []
    inv = load(dist / 'RELEASE_INVENTORY.json')
    if inv['release_id'] != manifest['release_id']:
        e.append('release inventory identity mismatch')
    roles = {x['role'] for x in inv['artifacts']}
    for r in ['RELEASE_AUTHORITY', 'CANONICAL_CORE', 'ADOPTION_STARTER_PACK', 'EXECUTABLE_REFERENCE_LAYER', 'SUPPORTING_SYSTEM_RATIONALE']:
        if r not in roles:
            e.append('missing distribution role ' + r)
    for x in inv['artifacts']:
        p = dist / x['path']
        if not p.exists():
            e.append('inventory missing ' + x['path'])
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != x['sha256']:
            e.append('digest mismatch ' + x['path'])
    for req in ['START_HERE.md', 'adoption/ADOPTION_STARTER_PACK.md', 'docs/SYSTEM_RATIONALE.md', 'canonical/CONTRACT.md', 'canonical_ae_release_manifest.json', 'reference/protocols/capability_contracts.json']:
        if not (dist / req).exists():
            e.append('distribution required file missing ' + req)
    if (dist / 'reference/fixtures/clean_room_adoption_baseline.json').exists():
        e.append('clean-room supplied baseline leaked into distribution')
    if any(x['path'].startswith('handoffs/') for x in inv['artifacts']):
        e.append('relay handoff state leaked into distribution')
    return e


def validate_loops(loops):
    e = []
    h = loops['happy_path']
    req = ['LOOP_CONTEXT', 'CONTRACT_APPROVED', 'ARCHITECTURE_AWARE_PLANNING', 'PLAN_REVIEW_ACCEPTED', 'READINESS_AUTHORITY_ALLOWED', 'BOUNDED_EXECUTION', 'VERIFICATION_EVIDENCE', 'INDEPENDENT_VALIDATION', 'ACCEPT', 'LEARNING_DISPOSITION']
    if h['stages'] != req:
        e.append('happy path stage drift')
    if h['authority_outcome'] != 'ALLOWED' or not h['work_management_direct_agent_allowed']:
        e.append('happy path authority/work management failure')
    if not h['validator_independent'] or h['validation_judgment'] != 'PROOF_SATISFIED' or h['route'] != 'ACCEPT':
        e.append('happy path validation failure')
    b = loops['backward_path']
    if b['route'] not in {'RETRY_EXECUTION', 'REPLAN', 'PROPOSE_CONTRACT_CHANGE'}:
        e.append('backward route invalid')
    if b['history_rewritten']:
        e.append('backward history rewrite')
    if b['route'] == 'REPLAN' and (b['new_plan'] == b['initial_plan'] or b['new_plan_review'] == b['initial_plan_review']):
        e.append('replan exact revision/review missing')
    r = loops['health_remediation']
    if not r['normal_lifecycle'] or not r['validator_independent'] or r['original_finding_rewritten']:
        e.append('health remediation governance failure')
    return e


def validate_capability_coverage(plan, capability_contracts):
    e = []
    canonical = canonical_capability_map(capability_contracts)
    required = set(canonical)
    bound = {c.get('capability') for c in plan.get('capability_bindings', []) if c.get('capability')}
    gaps = {g.get('capability') for g in plan.get('capability_gaps', []) if g.get('capability')}
    covered = bound | gaps

    missing = sorted(required - covered)
    if missing:
        e.append('cleanroom required capability neither bound nor gap-classified: ' + ', '.join(missing))

    omitted_bindings = required - bound
    unclassified_omissions = sorted(omitted_bindings - gaps)
    if unclassified_omissions:
        e.append('cleanroom omitted required capability family not explicit gap: ' + ', '.join(unclassified_omissions))

    coverage = plan.get('canonical_capability_coverage', {})
    if coverage.get('requirement_source') != 'reference/protocols/capability_contracts.json':
        e.append('cleanroom capability requirement source is not canonical packaged capability semantics')
    if coverage.get('required_count') != len(required):
        e.append('cleanroom canonical capability required count mismatch')
    if coverage.get('covered_count') != len(covered):
        e.append('cleanroom canonical capability covered count mismatch')
    if set(coverage.get('required_capabilities', [])) != required:
        e.append('cleanroom canonical capability catalog mismatch')

    for name in omitted_bindings:
        matches = [g for g in plan.get('capability_gaps', []) if g.get('capability') == name]
        if not matches:
            continue
        if not any(g.get('binding') is None and g.get('canonical_capability_id') == canonical[name] for g in matches):
            e.append('cleanroom missing-family gap lacks canonical identity/binding absence for ' + name)

    return e


def validate_capability_omission_regression(plan, capability_contracts):
    """Prove that deleting any wholly omitted required family gap makes validation fail."""
    e = []
    required = set(canonical_capability_map(capability_contracts))
    bound = {c.get('capability') for c in plan.get('capability_bindings', []) if c.get('capability')}
    omitted_bindings = sorted(required - bound)
    if not omitted_bindings:
        e.append('capability omission regression fixture lost all omitted required families')
        return e

    for name in omitted_bindings:
        mutated = copy.deepcopy(plan)
        mutated['capability_gaps'] = [g for g in mutated.get('capability_gaps', []) if g.get('capability') != name]
        errors = validate_capability_coverage(mutated, capability_contracts)
        if not errors:
            e.append('deleting required capability family gap passed silently: ' + name)
    return e


def validate_plan(plan, protocol, baseline, capability_contracts):
    e = []
    if plan.get('canonical_type') != 'Plan':
        e.append('cleanroom output not normal Plan')
    refs = plan.get('exact_references', {})
    expected = {
        'canonical_release': 'CAE-P1-CANDIDATE-2026-08-23',
        'oeb': baseline['oeb']['revision'],
        'product_profile': baseline['product']['profile'],
        'product_baseline': baseline['product']['baseline'],
        'implementation_profile': baseline['implementation_profile']['revision']
    }
    for k, v in expected.items():
        if refs.get(k) != v:
            e.append('cleanroom exact ref mismatch ' + k)
    if set(plan.get('rubric_claims', [])) != set(protocol['fresh_session_rubric']):
        e.append('cleanroom rubric incomplete')
    if plan.get('input_boundary', {}).get('hidden_prior_session_inputs') != []:
        e.append('cleanroom hidden inputs')
    if not plan.get('capability_bindings') or 'capability_gaps' not in plan or 'engineering_health_gaps' not in plan:
        e.append('cleanroom gap/binding reasoning incomplete')
    e.extend(validate_capability_coverage(plan, capability_contracts))
    e.extend(validate_capability_omission_regression(plan, capability_contracts))
    if not plan.get('implementation_increments'):
        e.append('cleanroom implementation credibility missing')
    if not plan.get('verification_test_strategy') or not plan.get('adoption_validation_strategy', {}).get('independent'):
        e.append('cleanroom evidence/validation design missing')
    if not plan.get('traceability'):
        e.append('cleanroom traceability missing')
    return e


def validate_synthetic_capability_coverage(synthetic, capability_contracts):
    e = []
    required = set(canonical_capability_map(capability_contracts))
    bound = {c.get('capability') for c in synthetic.get('capability_bindings', []) if c.get('capability')}
    missing = required - bound
    explicit = {g.get('capability') for g in synthetic.get('capability_gaps', []) if g.get('capability')}
    if explicit != missing:
        e.append(
            'synthetic omitted capability gaps do not match canonical missing families: '
            f"missing={sorted(missing)} explicit={sorted(explicit)}"
        )
    for g in synthetic.get('capability_gaps', []):
        if g.get('capability') in missing and g.get('impact') not in {'BLOCK', 'CONSTRAIN', 'DEGRADE'}:
            e.append('synthetic omitted capability gap lacks valid impact: ' + str(g.get('capability')))
    return e


def portability(f):
    e = []
    a = f['implementations']['A']
    b = f['implementations']['B']
    if a['environment'] == b['environment'] or a['bootstrap'] == b['bootstrap'] or a['source_control'] == b['source_control'] or a['iam'] == b['iam']:
        e.append('portability implementations not materially different')
    if a.get('portal_required') or b.get('portal_required'):
        e.append('portal made mandatory')
    for c in f['cases']:
        for k in f['equivalence_fields']:
            if c['A'].get(k) != c['B'].get(k):
                e.append(c['id'] + ': mismatch ' + k)
    return e


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 16:
        print('usage: reference/validators/validate_adoption.py protocol scenarios portability manifest synthetic loops cleanplan baseline distribution context capability authority lifecycle validation standards observability')
        raise SystemExit(2)

    protocol, fixtures, port, manifest, synthetic, loops, plan, baseline = [load(x) for x in args[:8]]
    dist = Path(args[8])
    context, cap, auth, lifecycle, validation, standards, obs = [load(x) for x in args[9:]]
    failures = []

    for x in cross(protocol, context, cap, auth, lifecycle, validation, standards, obs):
        print('FAIL cross-domain:', x)
        failures.append(x)

    for raw in fixtures['scenarios']:
        s = merged(fixtures['defaults'], raw)
        err = validate(s)
        got = 'FAIL' if err else 'PASS'
        exp = raw['expect']
        ee = raw.get('expected_error')
        ok = got == exp and (exp != 'FAIL' or err == ee)
        print(('PASS' if ok else 'FAIL') + f": {raw['id']} expected={exp}" + (f'/{ee}' if ee else '') + f' got={got}' + (f'/{err}' if err else ''))
        if not ok:
            failures.append(raw['id'])

    groups = [
        (verify_distribution(dist, manifest), 'distribution'),
        (validate_loops(loops), 'reference-loop'),
        (validate_plan(plan, protocol, baseline, cap), 'clean-room'),
        (validate_synthetic_capability_coverage(synthetic, cap), 'synthetic-capability-coverage'),
        (portability(port), 'portability')
    ]
    for group, name in groups:
        for x in group:
            print('FAIL ' + name + ':', x)
            failures.append(name + ':' + x)

    if synthetic.get('kestrel_present'):
        failures.append('synthetic:kestrel')
    caps = synthetic['capability_bindings']
    if not any(c.get('gap') for c in caps) and not synthetic.get('capability_gaps'):
        failures.append('synthetic:no capability gap')
    if not synthetic.get('engineering_health_findings'):
        failures.append('synthetic:no health finding')
    if not any(c.get('technical_available') and (not c.get('agent_operable', True) or not c.get('entitleable', True)) for c in caps):
        failures.append('synthetic:no technically-available operability failure')
    wm = next((c for c in caps if c['capability'] == 'Work Management'), None)
    if not wm or not wm.get('allowed_operation') or not wm.get('denied_operation'):
        failures.append('synthetic:work management proof incomplete')

    if failures:
        print('adoption-integrity FAILED:', '; '.join(failures))
        raise SystemExit(1)

    required_count = len(canonical_capability_map(cap))
    plan_bound = {c['capability'] for c in plan['capability_bindings']}
    omitted_count = len(set(canonical_capability_map(cap)) - plan_bound)
    print(
        f"adoption-integrity PASSED: {len(fixtures['scenarios'])} semantic scenarios + "
        f"{len(port['cases'])} portability cases + distribution/reference-loop/clean-room integration proof + "
        f"{required_count}/{required_count} Canonical capability families accounted for + "
        f"{omitted_count} omitted-family negative regression cases"
    )
