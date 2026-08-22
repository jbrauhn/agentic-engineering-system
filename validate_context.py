#!/usr/bin/env python3
import json, sys
from pathlib import Path

def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))

def err(code): return code

def eval_scenario(s, protocol):
    k=s['kind']; f=s['facts']
    if k=='package_authority':
        return err('CONTEXT_PACKAGE_NOT_AUTHORITATIVE') if f.get('package_authoritative') else None
    if k=='anchor_resolution':
        mode=f['mode']; src=f.get('sources',[]); selected=None
        auth=[x for x in src if x.get('authority')=='AUTHORITATIVE']
        if mode=='EXACT_REVISION':
            selected=next((x for x in auth if x.get('revision')==f.get('required_revision')),None)
        elif mode=='EFFECTIVE_FOR_SCOPE':
            cand=[x for x in auth if x.get('effective_for_scope')]
            selected=cand[0] if len(cand)==1 else None
        elif mode=='CURRENT_AT_USE':
            cand=[x for x in auth if x.get('currentness')=='SATISFIED']
            selected=cand[0] if len(cand)==1 else None
        if not selected: return err('REQUIRED_ANCHOR_UNRESOLVED')
        if selected.get('revision')!=f.get('expected_selected_revision'): return err('WRONG_REVISION_SELECTED')
        return None
    if k=='summary_override':
        if f.get('selected_revision')==f.get('summary_revision') and f.get('summary_revision')!=f.get('authoritative_revision'): return err('DERIVED_STATE_OVERRIDES_AUTHORITY')
        return None
    if k=='retrieval_authority':
        if f.get('claims_authoritative') and f.get('derivation')!='ISSUED_SOURCE': return err('DERIVED_STATE_NOT_AUTHORITY')
        return None
    if k=='current_at_use':
        disposition='READY'
        if f.get('protected_use') and f.get('currentness')!='SATISFIED': disposition='BLOCKED'
        return None if disposition==f.get('expected_disposition') else err('CURRENTNESS_DISPOSITION_MISMATCH')
    if k=='supporting_stale':
        disposition='DEGRADE' if f.get('requirement_class')=='SUPPORTING' and f.get('currentness')=='STALE' else 'READY'
        return None if disposition==f.get('expected_disposition') else err('SUPPORTING_DISPOSITION_MISMATCH')
    if k=='authority_conflict':
        authorities=[x for x in f.get('sources',[]) if x.get('authority')=='AUTHORITATIVE']
        if len(authorities)>1 and f.get('protected_use'):
            return err('SOURCE_AUTHORITY_CONFLICT')
        if len(authorities)>1 and not f.get('protected_use') and not f.get('unresolved_exposed'):
            return err('SOURCE_CONFLICT_HIDDEN')
        return None
    if k=='unauthorized_source':
        if not f.get('access_allowed') and f.get('source_included'): return err('UNAUTHORIZED_SOURCE_INCLUDED')
        disp='BLOCKED' if f.get('requirement_class')!='SUPPORTING' else 'DEGRADE'
        return None if disp==f.get('expected_disposition') else err('ACCESS_DISPOSITION_MISMATCH')
    if k=='derived_leak':
        if not f.get('underlying_access') and f.get('derived_visible') and not (f.get('authorized_transform') and f.get('transformation_proven')):
            return err('UNAUTHORIZED_DERIVED_LEAK')
        return None
    if k=='reconstruction':
        if f.get('hidden_session_required'): return err('HIDDEN_SESSION_DEPENDENCY')
        if set(f.get('required_anchors',[])) - set(f.get('resolved_anchors',[])): return err('RECONSTRUCTION_ANCHOR_MISSING')
        return None
    if k=='actor_equivalence':
        return None if f.get('continuing')==f.get('replacement') else err('GOVERNING_UNDERSTANDING_DRIFT')
    if k=='handoff_resolution':
        if not f.get('uses_authoritative_references') or f.get('treats_copied_summary_as_current'): return err('HANDOFF_NOT_CURRENT_SOURCE_TRUTH')
        return None
    if k=='handoff_stale':
        changed=f.get('issued_revision')!=f.get('current_effective_revision')
        if changed and not (f.get('stale_detected') and f.get('reassembled')): return err('STALE_HANDOFF_UNDETECTED')
        return None
    if k=='compaction':
        return None if f.get('material_state_durable_before_compaction') else err('MATERIAL_STATE_LOST_ON_COMPACTION')
    if k=='knowledge_write':
        if f.get('canonical_claim') and not f.get('semantic_owner_promotion'): return err('KNOWLEDGE_WRITE_NOT_CANONICAL_PROMOTION')
        return None
    if k=='promotion':
        if not f.get('semantic_owner'): return err('SEMANTIC_OWNER_REQUIRED')
        if not f.get('source_conflict_resolved'): return err('PROMOTION_SOURCE_CONFLICT')
        if not f.get('provenance'): return err('PROMOTION_PROVENANCE_REQUIRED')
        if not f.get('authorization_satisfied'): return err('PROMOTION_NOT_AUTHORIZED')
        return None
    if k=='generic_knowledge_entity':
        return err('GENERIC_KNOWLEDGE_ENTITY_PROHIBITED') if f.get('generic_entity_required') else None
    if k=='consequential_provenance':
        if f.get('consequential') and f.get('material_context') and not f.get('direct_refs_complete') and not f.get('receipt_retained'):
            return err('CONSEQUENTIAL_CONTEXT_BASIS_NOT_RECONSTRUCTABLE')
        return None
    if k=='routine_provenance':
        return err('PROVENANCE_AUDIT_SWAMP') if f.get('routine') and f.get('permanent_receipt_required') else None
    if k=='bootstrap':
        if set(f.get('discoveries',[]))!=set(protocol['bootstrap_discoveries']): return err('BOOTSTRAP_DISCOVERY_INCOMPLETE')
        if f.get('requires_specific_environment'): return err('ENVIRONMENT_UNIFORMITY_ASSUMPTION')
        return None
    if k=='provenance_secret':
        return err('SECRET_IN_CONTEXT_PROVENANCE') if f.get('stores_secret') else None
    if k=='missing_anchor_summary':
        if not f.get('required_anchor_resolved') and f.get('behavior')!='BLOCK': return err('REQUIRED_ANCHOR_UNRESOLVED')
        return None
    if k=='context_invalidation':
        if f.get('source_changed') and f.get('old_package_mutated_current'): return err('OLD_CONTEXT_MUTATED_TO_CURRENT')
        if f.get('source_changed') and not f.get('new_package_created'): return err('CONTEXT_REASSEMBLY_REQUIRED')
        return None
    if k=='validation_evidence':
        return err('CONTEXT_PACKAGE_NOT_EVIDENCE') if f.get('package_is_evidence') else None
    if k=='anchor_priority':
        return err('MANDATORY_ANCHOR_DISPLACED') if f.get('mandatory_anchor_omitted_due_to_relevance') else None
    if k=='provider_shadow':
        return err('KNOWLEDGE_PROVIDER_SHADOW_AUTHORITY') if f.get('provider_copy_claims_canonical_authority') else None
    if k=='revoked_access':
        if f.get('current_policy')!='PERMIT' and (f.get('new_retrieval_allowed') or f.get('protected_use_allowed')): return err('STALE_CONTEXT_AUTHORIZATION')
        return None
    if k=='handoff_required':
        if f.get('meaningful_boundary') and f.get('material_state_not_otherwise_reconstructable') and not f.get('handoff_present'): return err('HANDOFF_REQUIRED_FOR_CONTINUATION')
        return None
    if k=='source_unavailable_cache':
        if not f.get('authoritative_source_available') and f.get('cache_promoted_authoritative'): return err('CACHE_NOT_AUTHORITY')
        disp='BLOCKED' if not f.get('authoritative_source_available') else 'READY'
        if 'expected_disposition' in f and disp!=f['expected_disposition']: return err('SOURCE_UNAVAILABLE_DISPOSITION_MISMATCH')
        return None
    return err('UNKNOWN_SCENARIO_KIND')

def static_checks(protocol, capabilities, lifecycle, authority):
    failures=[]
    rules=protocol.get('rules',{})
    required_rules=['memory_is_system_property_not_store','no_generic_knowledge_item_or_memory_record','context_package_not_authoritative','replacement_actor_reconstructable','anchor_first_relevance_expanding','correct_effective_beats_latest','knowledge_write_does_not_create_canonical_truth','semantic_owner_promotion_required_for_canonical_state','derived_context_no_broader_access_than_source']
    for r in required_rules:
        if rules.get(r) is not True: failures.append(f'protocol rule missing/false: {r}')
    if protocol.get('domain_semantics',{}).get('context_package')!='D': failures.append('Context Package must remain D')
    if protocol.get('domain_semantics',{}).get('context_assembly_receipt')!='B': failures.append('Context Assembly Receipt must remain B')
    if protocol.get('domain_semantics',{}).get('handoff_record')!='A2': failures.append('Handoff must remain existing A2')
    km=next((c for c in capabilities.get('capabilities',[]) if c.get('capability_id')=='knowledge_memory'),None)
    if not km: failures.append('L1-E Knowledge / Memory capability missing')
    else:
        ops={o.get('operation_id'):o for o in km.get('operations',[])}
        for op in ['knowledge.read','knowledge.query','knowledge.write','knowledge.reference']:
            if op not in ops: failures.append(f'L1-E knowledge operation missing: {op}')
        if 'knowledge.write' in ops and not ops['knowledge.write'].get('protected_operation'): failures.append('knowledge.write must remain protected')
    if lifecycle.get('rules',{}).get('contract_revision_effectivity_required') is not True: failures.append('L1-D Contract effectivity rule missing')
    if set(authority.get('policy_results',[]))!={'PERMIT','DENY','INDETERMINATE'}: failures.append('L1-F policy results drift')
    if authority.get('rules',{}).get('indeterminate_never_permits_protected_operation') is not True: failures.append('L1-F INDETERMINATE fail-closed rule missing')
    return failures

def portability_checks(data):
    failures=[]
    for c in data.get('cases',[]):
        a,b=c['implementation_a'],c['implementation_b']
        for key in ['governing_anchors','authority_restrictions','blockers','unauthorized_leak']:
            if a.get(key)!=b.get(key): failures.append(f"{c['id']}: governed outcome differs for {key}")
        if a.get('architecture')==b.get('architecture'): failures.append(f"{c['id']}: architectures are not materially different")
    return failures

def main():
    if len(sys.argv)!=7:
        print('usage: validate_context.py context_protocol.json context_scenarios.json context_portability_fixtures.json capability_contracts.json lifecycle_protocol.json authority_protocol.json')
        return 2
    protocol, scenarios, ports, caps, life, auth=map(load,sys.argv[1:])
    failures=static_checks(protocol,caps,life,auth)
    for s in scenarios.get('scenarios',[]):
        e=eval_scenario(s,protocol)
        got='FAIL' if e else 'PASS'; exp=s['expect']; exp_err=s.get('expected_error')
        ok=(got==exp and (exp!='FAIL' or e==exp_err))
        print(f"{'PASS' if ok else 'FAIL'}: {s['id']} expected={exp}" + (f'/{exp_err}' if exp_err else '') + f' got={got}' + (f'/{e}' if e else ''))
        if not ok: failures.append(s['id'])
    pf=portability_checks(ports)
    for c in ports.get('cases',[]):
        bad=[x for x in pf if x.startswith(c['id']+':')]
        print(f"{'FAIL' if bad else 'PASS'}: {c['id']} retrieval architectures preserve governed outcome" + (f' errors={bad}' if bad else ''))
    failures.extend(pf)
    if failures:
        print('context-integrity FAILED:')
        for f in failures: print(' -',f)
        return 1
    print(f"context-integrity PASSED: {len(scenarios.get('scenarios',[]))} semantic scenarios + {len(ports.get('cases',[]))} portability cases")
    return 0

if __name__=='__main__': raise SystemExit(main())
