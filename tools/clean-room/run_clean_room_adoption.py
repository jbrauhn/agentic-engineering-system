#!/usr/bin/env python3
import argparse, json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--distribution', required=True)
    ap.add_argument('--baseline', required=True)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()

    dist = Path(a.distribution).resolve()
    baseline_path = Path(a.baseline).resolve()

    # The reference actor reads only the assembled distribution and supplied baseline values.
    # Required capability families come from packaged Canonical capability semantics, never
    # from the supplied baseline's list (which may itself be incomplete).
    manifest = json.loads((dist / 'canonical_ae_release_manifest.json').read_text())
    inventory = json.loads((dist / 'RELEASE_INVENTORY.json').read_text())
    protocol = json.loads((dist / 'reference/protocols/adoption_distribution_protocol.json').read_text())
    capability_contracts = json.loads((dist / 'reference/protocols/capability_contracts.json').read_text())
    baseline = json.loads(baseline_path.read_text())

    required_capabilities = [
        {'capability_id': c['capability_id'], 'name': c['name']}
        for c in capability_contracts['capabilities']
    ]
    baseline_bindings = {c['capability']: c for c in baseline.get('capability_bindings', [])}

    caps = []
    gaps = []
    for required in required_capabilities:
        c = baseline_bindings.get(required['name'])
        if c is None:
            gaps.append({
                'gap_class': 'CAPABILITY',
                'canonical_capability_id': required['capability_id'],
                'capability': required['name'],
                'binding': None,
                'impact': 'BLOCK',
                'reasons': ['required Canonical capability family absent from supplied baseline'],
                'requirement_source': 'reference/protocols/capability_contracts.json'
            })
            continue

        caps.append({
            'canonical_capability_id': required['capability_id'],
            'capability': c['capability'],
            'binding': c['binding'],
            'access_paths': c.get('access_paths', [])
        })
        reasons = []
        if not c.get('agent_operable', False):
            reasons.append('agent interface/access missing')
        if not c.get('entitleable', False):
            reasons.append('scoped entitlement unavailable')
        if not c.get('enforceable', False):
            reasons.append('enforcement insufficient')
        if not c.get('proven', False):
            reasons.append('binding Proof pending')
        if reasons:
            impact = c.get('gap', {}).get('impact', 'CONSTRAIN')
            gaps.append({
                'gap_class': 'CAPABILITY',
                'canonical_capability_id': required['capability_id'],
                'capability': c['capability'],
                'binding': c['binding'],
                'impact': impact,
                'reasons': reasons,
                'requirement_source': 'reference/protocols/capability_contracts.json'
            })

    health = [
        {
            'gap_class': 'ENGINEERING_HEALTH',
            'finding': f['id'],
            'condition': f['condition'],
            'impact': f['impact']
        }
        for f in baseline.get('engineering_health_findings', [])
    ]

    increments = []
    for g in gaps:
        increments.append({
            'increment_id': 'INC-CAP-' + g['capability'].upper().replace(' ', '-').replace('/', '-'),
            'purpose': 'remediate or explicitly disposition capability gap',
            'trace_to': g['binding'] or g['canonical_capability_id'],
            'evidence': ['agent-access/entitlement/enforcement Proof'],
            'validation': 'independent capability/adoption Validation'
        })
    for h in health:
        increments.append({
            'increment_id': 'INC-HEALTH-' + h['finding'],
            'purpose': 'governed engineering-health remediation',
            'trace_to': h['finding'],
            'evidence': ['engineering change Evidence'],
            'validation': 'independent remediation Validation'
        })

    covered_capabilities = {c['capability'] for c in caps} | {g['capability'] for g in gaps}
    distribution_revision = manifest.get('distribution_revision', 1)
    plan = {
        'canonical_type': 'Plan',
        'plan_id': 'PLAN-CLEANROOM-BETA@1',
        'planning_depth': 'L2_L3',
        'planning_method': 'simplest_credible_adoption_planning',
        'input_boundary': {
            'distribution_release': manifest['release_id'],
            'distribution_revision': distribution_revision,
            'inventory_release': inventory['release_id'],
            'inventory_distribution_revision': inventory.get('distribution_revision', 1),
            'supplied_baseline_id': baseline['organization'],
            'hidden_prior_session_inputs': []
        },
        'exact_references': {
            'canonical_release': manifest['release_id'],
            'oeb': baseline['oeb']['revision'],
            'product_profile': baseline['product']['profile'],
            'product_baseline': baseline['product']['baseline'],
            'implementation_profile': baseline['implementation_profile']['revision']
        },
        'canonical_capability_coverage': {
            'requirement_source': 'reference/protocols/capability_contracts.json',
            'required_count': len(required_capabilities),
            'covered_count': len(covered_capabilities),
            'required_capabilities': [c['name'] for c in required_capabilities]
        },
        'capability_bindings': caps,
        'capability_gaps': gaps,
        'engineering_health_gaps': health,
        'agent_access_authority': {
            'identity_source': baseline['authority']['identity_source'],
            'oa_source': baseline['authority']['oa_source'],
            'pep': baseline['authority'].get('pep'),
            'supported_environments': baseline['environments']
        },
        'standards': baseline['standards'],
        'architecture': baseline['architecture'],
        'context_knowledge': baseline['context'],
        'implementation_increments': increments,
        'verification_test_strategy': [
            'prove each required Access Path from supported environments',
            'prove authorized operation succeeds and unauthorized operation denies',
            'prove exact revision/bootstrap reconstruction',
            'prove every Canonical capability family is bound or explicitly gap-classified'
        ],
        'adoption_validation_strategy': {
            'independent': baseline['validation']['installation_independent'],
            'evidence_classes': baseline['validation']['evidence_classes'],
            'target': 'exact release + declared scope + OEB/Product/Profile/Binding revisions'
        },
        'acceptance_proof': [
            'all required capability families accounted for as binding and/or explicit Capability gap',
            'all required capability gaps resolved/dispositioned',
            'bootstrap/interface parity proven',
            'reference loop behavior proven',
            'independent installation/adoption Validation accepted'
        ],
        'traceability': {
            'release_manifest': 'canonical_ae_release_manifest.json',
            'capability_contracts': 'reference/protocols/capability_contracts.json',
            'starter': 'adoption/ADOPTION_STARTER_PACK.md',
            'protocol': 'reference/protocols/adoption_distribution_protocol.json'
        },
        'rubric_claims': protocol['fresh_session_rubric']
    }

    Path(a.output).write_text(json.dumps(plan, indent=2) + '\n')
    print(
        f"derived {plan['plan_id']} from release + supplied baseline only; "
        f"distribution revision {distribution_revision}; "
        f"Canonical capability coverage {len(covered_capabilities)}/{len(required_capabilities)}"
    )


if __name__ == '__main__':
    main()
