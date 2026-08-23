#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--distribution',required=True); ap.add_argument('--baseline',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 dist=Path(a.distribution).resolve(); baseline_path=Path(a.baseline).resolve()
 # The reference actor reads only the assembled distribution and supplied baseline values.
 manifest=json.loads((dist/'canonical_ae_release_manifest.json').read_text())
 inventory=json.loads((dist/'RELEASE_INVENTORY.json').read_text())
 protocol=json.loads((dist/'adoption_distribution_protocol.json').read_text())
 baseline=json.loads(baseline_path.read_text())
 caps=[]; gaps=[]
 for c in baseline['capability_bindings']:
  caps.append({'capability':c['capability'],'binding':c['binding'],'access_paths':c.get('access_paths',[])})
  reasons=[]
  if not c.get('agent_operable',False): reasons.append('agent interface/access missing')
  if not c.get('entitleable',False): reasons.append('scoped entitlement unavailable')
  if not c.get('enforceable',False): reasons.append('enforcement insufficient')
  if not c.get('proven',False): reasons.append('binding Proof pending')
  if reasons:
   impact=c.get('gap',{}).get('impact','CONSTRAIN')
   gaps.append({'gap_class':'CAPABILITY','capability':c['capability'],'binding':c['binding'],'impact':impact,'reasons':reasons})
 health=[{'gap_class':'ENGINEERING_HEALTH','finding':f['id'],'condition':f['condition'],'impact':f['impact']} for f in baseline.get('engineering_health_findings',[])]
 increments=[]
 for g in gaps:
  increments.append({'increment_id':'INC-CAP-'+g['capability'].upper().replace(' ','-').replace('/','-'),'purpose':'remediate or explicitly disposition capability gap','trace_to':g['binding'],'evidence':['agent-access/entitlement/enforcement Proof'],'validation':'independent capability/adoption Validation'})
 for h in health:
  increments.append({'increment_id':'INC-HEALTH-'+h['finding'],'purpose':'governed engineering-health remediation','trace_to':h['finding'],'evidence':['engineering change Evidence'],'validation':'independent remediation Validation'})
 plan={
  'canonical_type':'Plan','plan_id':'PLAN-CLEANROOM-BETA@1','planning_depth':'L2_L3','planning_method':'simplest_credible_adoption_planning',
  'input_boundary':{'distribution_release':manifest['release_id'],'inventory_release':inventory['release_id'],'supplied_baseline_id':baseline['organization'],'hidden_prior_session_inputs':[]},
  'exact_references':{'canonical_release':manifest['release_id'],'oeb':baseline['oeb']['revision'],'product_profile':baseline['product']['profile'],'product_baseline':baseline['product']['baseline'],'implementation_profile':baseline['implementation_profile']['revision']},
  'capability_bindings':caps,'capability_gaps':gaps,'engineering_health_gaps':health,
  'agent_access_authority':{'identity_source':baseline['authority']['identity_source'],'oa_source':baseline['authority']['oa_source'],'pep':baseline['authority'].get('pep'),'supported_environments':baseline['environments']},
  'standards':baseline['standards'],'architecture':baseline['architecture'],'context_knowledge':baseline['context'],
  'implementation_increments':increments,
  'verification_test_strategy':['prove each required Access Path from supported environments','prove authorized operation succeeds and unauthorized operation denies','prove exact revision/bootstrap reconstruction'],
  'adoption_validation_strategy':{'independent':baseline['validation']['installation_independent'],'evidence_classes':baseline['validation']['evidence_classes'],'target':'exact release + declared scope + OEB/Product/Profile/Binding revisions'},
  'acceptance_proof':['all required capability gaps resolved/dispositioned','bootstrap/interface parity proven','reference loop behavior proven','independent installation/adoption Validation accepted'],
  'traceability':{'release_manifest':'canonical_ae_release_manifest.json','starter':'ADOPTION_STARTER_PACK.md','protocol':'adoption_distribution_protocol.json'},
  'rubric_claims':protocol['fresh_session_rubric']
 }
 Path(a.output).write_text(json.dumps(plan,indent=2)+'\n'); print(f"derived {plan['plan_id']} from release + supplied baseline only")
if __name__=='__main__': main()
