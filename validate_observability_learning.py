#!/usr/bin/env python3
import json, sys
from pathlib import Path

def load(p): return json.loads(Path(p).read_text())
def merged(d,s): x=dict(d); x.update(s); return x

def cross(protocol,lifecycle,cap,auth,context,planning,validation,standards):
 e=[]
 ds=protocol['domain_semantics']
 expected={'metric_definition':'B','provider_measurement_resource':'C','dashboard_analytics_view':'D','experiment':'A1','learning_record':'A2','effective_observability_configuration':'D'}
 for k,v in expected.items():
  if ds.get(k)!=v:e.append(f'domain drift {k}')
 for r in protocol['cross_domain_expectations']['lifecycle_rules']:
  if not lifecycle.get('rules',{}).get(r): e.append('lifecycle rule missing '+r)
 ops={o['operation_id'] for c in cap.get('capabilities',[]) for o in c.get('operations',[])}
 for o in protocol['cross_domain_expectations']['observability_capability_operations']:
  if o not in ops:e.append('capability op missing '+o)
 for r in protocol['cross_domain_expectations']['authority_rules']:
  if not auth.get('rules',{}).get(r):e.append('authority rule missing '+r)
 for r in protocol['cross_domain_expectations']['context_rules']:
  if not context.get('rules',{}).get(r):e.append('context rule missing '+r)
 if planning.get('verification_chain')!=protocol['cross_domain_expectations']['planning_execution_verification_chain']:
  e.append('planning verification chain drift')
 for r in protocol['cross_domain_expectations']['validation_rules']:
  if not validation.get('rules',{}).get(r):e.append('validation rule missing '+r)
 for r in protocol['cross_domain_expectations']['standards_health_rules']:
  if not standards.get('rules',{}).get(r):e.append('standards-health rule missing '+r)
 required=['federated_r7_boundary','minimum_measures_are_neutral_observations','no_faster_cheaper_auto_better','no_universal_roi_formula','lifecycle_metrics_use_canonical_history','telemetry_not_evidence_by_default','telemetry_not_learning_by_default','experiment_a1_existing_identity','experiment_conclusion_strength_bounded_by_design_evidence','learning_record_material_only','learning_informative_not_self_authorizing','preauthorized_adaptation_allowed_within_boundary','adaptation_cannot_expand_authority','no_universal_prompt_logging','no_chain_of_thought_retention','no_central_r7_service_required','no_new_l1k_a1_a2_required']
 for r in required:
  if not protocol.get('rules',{}).get(r):e.append('required rule missing '+r)
 ids={m['id'] for m in protocol.get('minimum_measure_categories',[])}
 need={'total_time_to_outcome','phase_time','loop_count','failed_validation_loops','human_effort','agent_model_cost','quality_assessment','organization_selected'}
 if ids!=need:e.append('minimum measure set drift')
 return e

def rank(s):
 order={'DESCRIPTIVE':1,'ASSOCIATIONAL':2,'CAUSAL':3}
 return order.get(s,0)

def validate(s,protocol):
 if s.get('new_entity') in {'MetricRecord','MetricDefinition','MeasurementRecord','PerformanceReport'}:return 'METRIC_ENTITY_INFLATION'
 if s.get('new_entity')=='Observation':return 'OBSERVATION_ENTITY_INFLATION'
 if s.get('central_r7_required'):return 'CENTRAL_R7_NOT_CANONICAL'
 if s.get('universal_prompt_logging'):return 'PROMPT_LOGGING_NOT_CANONICAL'
 if s.get('chain_of_thought_retention'):return 'COT_RETENTION_NOT_CANONICAL'
 if s.get('universal_surveillance'):return 'UNIVERSAL_SURVEILLANCE_NOT_CANONICAL'
 if s.get('unauthorized_observability_access'):return 'OBSERVABILITY_ACCESS_VIOLATION'
 if s.get('classification_violation'):return 'OBSERVABILITY_CLASSIFICATION_VIOLATION'
 if s.get('measurement'):
  for k in ['measure_id','scope','window','units','source_ref','definition_revision','provenance']:
   if not s.get(k):return 'MEASUREMENT_SEMANTICS_INCOMPLETE'
  if s.get('auto_better'):return 'MEASUREMENT_NEUTRALITY_VIOLATION'
  if s.get('universal_roi'):return 'UNIVERSAL_ROI_PROHIBITED'
  if s.get('universal_score'):return 'UNIVERSAL_PERFORMANCE_SCORE_PROHIBITED'
  if s.get('raw_telemetry_auto_evidence'):return 'TELEMETRY_NOT_EVIDENCE_BY_DEFAULT'
  if s.get('raw_telemetry_auto_learning'):return 'TELEMETRY_NOT_LEARNING_BY_DEFAULT'
  if s.get('dashboard_as_authority'):return 'DASHBOARD_NOT_AUTHORITY'
  if not s.get('material_reference_reconstructable'):return 'MATERIAL_MEASUREMENT_REFERENCE_REQUIRED'
  if s.get('provider_label_as_canonical'):return 'CANONICAL_LIFECYCLE_SOURCE_REQUIRED'
  if not s.get('telemetry_scope_matches'):return 'TELEMETRY_SCOPE_MISMATCH'
  if (not s.get('telemetry_complete') or not s.get('telemetry_current')) and not s.get('current_reliance_qualified'):return 'CURRENT_RELIANCE_REASSESSMENT_REQUIRED'
  if s.get('measure_id')=='human_effort' and s.get('human_effort_basis') not in protocol['human_effort_basis_types']:return 'HUMAN_EFFORT_BASIS_REQUIRED'
  if s.get('measure_id')=='agent_model_cost':
   if s.get('cost_basis') not in protocol['cost_basis_types']:return 'COST_BASIS_REQUIRED'
   if not s.get('cost_units'):return 'COST_UNITS_REQUIRED'
  if s.get('measure_id')=='quality_assessment' and not s.get('quality_method'):return 'QUALITY_METHOD_REQUIRED'
 if s.get('provider_metric_auto_validation'):return 'PROVIDER_METRIC_NOT_VALIDATION'
 if s.get('health_tool_score_auto_finding'):return 'TOOL_SCORE_NOT_HEALTH_FINDING'
 if s.get('experiment'):
  if not s.get('experiment_id'):return 'EXPERIMENT_ID_REQUIRED'
  if s.get('experiment_state') not in protocol['experiment_lifecycle']['states']:return 'EXPERIMENT_STATE_INVALID'
  if s.get('experiment_transition_from') or s.get('experiment_transition_to'):
   pair=[s.get('experiment_transition_from'),s.get('experiment_transition_to')]
   if pair not in protocol['experiment_lifecycle']['allowed_transitions']:return 'EXPERIMENT_TRANSITION_INVALID'
  if s.get('material_active_change') and not s.get('change_versioned'):return 'EXPERIMENT_CHANGE_VERSIONING_REQUIRED'
  if s.get('experiment_state')=='CONCLUDED' and s.get('history_rewritten'):return 'EXPERIMENT_HISTORY_NON_DESTRUCTIVE'
  if rank(s.get('claim_strength'))>rank(s.get('design_support_strength')):return 'EXPERIMENT_CLAIM_EXCEEDS_EVIDENCE'
  if s.get('predetermined_ae_win'):return 'EXPERIMENT_NOT_PREDETERMINED'
  if s.get('observation_entity_required'):return 'EXPERIMENT_OBSERVATION_ENTITY_INFLATION'
 if s.get('learning'):
  if not s.get('learning_conclusion'):return 'LEARNING_CONCLUSION_REQUIRED'
  if not s.get('learning_evidence'):return 'LEARNING_EVIDENCE_REQUIRED'
  if not s.get('learning_material') and s.get('learning_forced'):return 'NO_CEREMONIAL_LEARNING_RECORD'
  if s.get('learning_source') is not None and s.get('learning_source') not in protocol['learning_sources']:return 'LEARNING_SOURCE_INVALID'
  if not s.get('durable_learning_provenance'):return 'LEARNING_PROVENANCE_DURABILITY_REQUIRED'
  if s.get('learning_history_rewritten'):return 'LEARNING_HISTORY_NON_DESTRUCTIVE'
  if s.get('learning_silent_mutation'):return 'LEARNING_NOT_SELF_AUTHORIZING'
 if s.get('loop_learning_disposition') not in protocol['loop_learning_dispositions']:return 'LEARNING_DISPOSITION_INVALID'
 if s.get('preauthorized_adaptation'):
  if not (s.get('oa_boundary_valid') and s.get('policy_boundary_valid') and s.get('adaptation_inside_boundary')):return 'ADAPTATION_BOUNDARY_REQUIRED'
  if s.get('authority_expanded'):return 'ADAPTATION_CANNOT_EXPAND_AUTHORITY'
  if s.get('policy_weakened'):return 'ADAPTATION_CANNOT_WEAKEN_POLICY'
  if s.get('contract_redefined'):return 'ADAPTATION_CANNOT_REDEFINE_CONTRACT'
 if s.get('later_invalid_telemetry') and not s.get('current_reliance_qualified'):return 'CURRENT_RELIANCE_REASSESSMENT_REQUIRED'
 return None

def portability(f):
 fail=[]; a=f['implementations']['A']; b=f['implementations']['B']
 if a['central_r7_service'] or b['central_r7_service']:fail.append('CENTRAL_R7_NOT_CANONICAL')
 if a['telemetry_topology']==b['telemetry_topology']:fail.append('PORTABILITY_TOPOLOGIES_NOT_DIFFERENT')
 for c in f['cases']:
  for k in f['equivalence_fields']:
   if c['A'].get(k)!=c['B'].get(k):fail.append(c['id']+':MISMATCH:'+k)
 return fail

def main():
 if len(sys.argv)!=11:
  print('usage: validate_observability_learning.py protocol scenarios portability lifecycle capability authority context planning validation standards_health');return 2
 protocol,fixtures,port,lifecycle,cap,auth,context,planning,validation,standards=[load(x) for x in sys.argv[1:]]
 errs=cross(protocol,lifecycle,cap,auth,context,planning,validation,standards)
 if errs:
  for x in errs:print('FAIL cross-domain:',x)
  return 1
 fails=[]
 for raw in fixtures['scenarios']:
  s=merged(fixtures['defaults'],raw); err=validate(s,protocol); got='FAIL' if err else 'PASS'; exp=raw['expect']; ee=raw.get('expected_error'); ok=got==exp and (exp!='FAIL' or err==ee)
  print(('PASS' if ok else 'FAIL')+f": {raw['id']} expected={exp}"+(f'/{ee}' if ee else '')+f' got={got}'+(f'/{err}' if err else ''))
  if not ok:fails.append(raw['id'])
 pf=portability(port)
 for x in pf:print('FAIL portability:',x)
 fails += pf
 if fails:
  print('observability-learning-integrity FAILED:',', '.join(fails));return 1
 print(f"observability-learning-integrity PASSED: {len(fixtures['scenarios'])} semantic scenarios + {len(port['cases'])} portability cases")
 return 0
if __name__=='__main__':raise SystemExit(main())
