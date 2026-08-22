#!/usr/bin/env python3
import json
import sys
from pathlib import Path

EXPECTED_CAPABILITIES={"source_control","ci_cd","models","runtime_execution","identity_access","governed_tool_access","observability","knowledge_memory","work_management","validation"}
READINESS_DIMS={"SUPPORTED","BOUND","DISCOVERABLE","REACHABLE","ENTITLEABLE","ENFORCEABLE","PROVEN"}
READINESS_STATES={"SATISFIED","UNSATISFIED","UNKNOWN","NOT_APPLICABLE"}

class CapabilityError(Exception):
    def __init__(self,code,message): super().__init__(message); self.code=code; self.message=message

def fail(code,msg): raise CapabilityError(code,msg)
def load(path): return json.loads(Path(path).read_text(encoding="utf-8"))

def indexes(defs):
    return ({c["capability_id"]:c for c in defs["capabilities"]},{o["operation_id"]:(c,o) for c in defs["capabilities"] for o in c["operations"]})

def validate_definitions(defs):
    ids=[c["capability_id"] for c in defs.get("capabilities",[])]
    if set(ids)!=EXPECTED_CAPABILITIES or len(ids)!=len(set(ids)): fail("CAPABILITY_SET_MISMATCH","expected exactly ten unique Contract capability IDs")
    if set(defs.get("readiness_dimensions",[]))!=READINESS_DIMS: fail("READINESS_DIMENSION_MISMATCH","")
    if set(defs.get("readiness_evaluation_states",[]))!=READINESS_STATES: fail("READINESS_STATE_MISMATCH","")
    if set(defs.get("runtime_outcomes",[]))!={"ALLOWED","DENIED","BLOCKED"}: fail("RUNTIME_OUTCOME_MISMATCH","")
    seen=set()
    for c in defs["capabilities"]:
        if not c.get("purpose"): fail("CAPABILITY_PURPOSE_MISSING",c["capability_id"])
        for o in c.get("operations",[]):
            oid=o["operation_id"]
            if oid in seen: fail("DUPLICATE_OPERATION",oid)
            seen.add(oid)
            if o.get("requirement_class") not in {"REQUIRED","CONDITIONAL_REQUIRED"}: fail("BAD_REQUIREMENT_CLASS",oid)
            for f in ("purpose","agent_access_required","protected_operation"):
                if f not in o or (f=="purpose" and not o[f]): fail("OPERATION_METADATA_MISSING",f"{oid}:{f}")
    wm={o["operation_id"] for c in defs["capabilities"] if c["capability_id"]=="work_management" for o in c["operations"] if o["requirement_class"]=="REQUIRED"}
    req={"work.create","work.query","work.read","work.update","work.transition","work.relationship.manage","work.annotation.add","work.reference.associate","work.artifact.associate","work.complete"}
    if wm!=req: fail("WORK_MANAGEMENT_SET_MISMATCH","")
    rops={o["operation_id"]:o for c in defs["capabilities"] if c["capability_id"]=="runtime_execution" for o in c["operations"]}
    if rops["execution.cancel"]["requirement_class"]!="CONDITIONAL_REQUIRED": fail("EXECUTION_CANCEL_NOT_CONDITIONAL","")
    if "credential.establish_scoped_use" not in seen: fail("SCOPED_CREDENTIAL_USE_MISSING","")
    return indexes(defs)

def required_ops(cap,b):
    cond=b.get("conditional_applicability",{})
    return [o["operation_id"] for o in cap["operations"] if o["requirement_class"]=="REQUIRED" or (o["requirement_class"]=="CONDITIONAL_REQUIRED" and cond.get(o["operation_id"]) is True)]

def template_ops(template):
    return {"WORK_MANAGEMENT_COMPLETE":["work.create","work.query","work.read","work.update","work.transition","work.relationship.manage","work.annotation.add","work.reference.associate","work.artifact.associate","work.complete"],"RUNTIME_ATOMIC":["execution.start","execution.status","execution.result.read"],"IDENTITY_MEDIATED":["identity.authenticate","identity.context.read","credential.establish_scoped_use"],"KNOWLEDGE_COMPLETE":["knowledge.read","knowledge.query","knowledge.write","knowledge.reference"],"VALIDATION_PARTIAL_REQUEST":["validation.request","validation.status"],"VALIDATION_PARTIAL_RESULT":["validation.result.read","validation.evidence.read"]}.get(template,[])

def template_cap(template):
    return {"WORK_MANAGEMENT_COMPLETE":"work_management","RUNTIME_ATOMIC":"runtime_execution","IDENTITY_MEDIATED":"identity_access","KNOWLEDGE_COMPLETE":"knowledge_memory","VALIDATION_PARTIAL_REQUEST":"validation","VALIDATION_PARTIAL_RESULT":"validation"}.get(template)

def expand_binding(raw,profiles):
    b=dict(raw); b["capability_id"]=template_cap(b["template"]); ops=template_ops(b["template"])
    for rem in b.get("remove_operations",[]):
        if rem in ops: ops.remove(rem)
    shape=b.get("provider_shape","DEFAULT")
    b["operation_mappings"]={op:f"{b['provider_id']}::{shape}::{op.replace('.','_')}" for op in ops}
    contexts=b.get("supported_contexts",["headless-agent"]); b["supported_contexts"]=contexts; mechmap=b.get("mechanisms_by_context",{})
    b["access_paths"]=[{"context":ctx,"mechanism":mechmap.get(ctx,b.get("mechanism","GOVERNED_API")),"discovery_ref":f"DISC::{b['binding_id']}::{ctx}","operations":list(ops),"evidence_ref":f"EVIDENCE::ACCESS::{b['binding_id']}::{ctx}"} for ctx in contexts]
    profile=profiles[b.get("readiness_profile","PROVEN_HEALTHY")]
    b["readiness"]={d:{"state":profile[d],"evidence_ref":f"EVIDENCE::{b['binding_id']}::{d}",**({"validation_ref":f"VALIDATION::{b['binding_id']}"} if d=="PROVEN" and profile[d]=="SATISFIED" else {})} for d in READINESS_DIMS}
    b.setdefault("proof_environment","sandbox"); b.setdefault("actual_binding_exercised",True)
    return b

def validate_readiness(b,opmeta):
    for d in READINESS_DIMS:
        ev=b["readiness"][d]; st=ev["state"]
        if st not in READINESS_STATES: fail("BAD_READINESS_STATE",f"{b['binding_id']}:{d}")
        if st=="SATISFIED" and not ev.get("evidence_ref"): fail("READINESS_WITHOUT_EVIDENCE",f"{b['binding_id']}:{d}")
        if d=="PROVEN" and st=="SATISFIED" and not ev.get("validation_ref"): fail("PROVEN_WITHOUT_VALIDATION",b["binding_id"])
        if d=="ENTITLEABLE" and st=="UNSATISFIED": fail("ENTITLEABILITY_FAILED",b["binding_id"])
        if st=="UNKNOWN" and opmeta.get("protected_operation"): fail("UNKNOWN_REQUIRED_READINESS",b["binding_id"])

def validate_binding(caps,ops,b,allow_partial=False):
    cap=caps[b["capability_id"]]; mapped=b["operation_mappings"]
    for oid in required_ops(cap,b):
        if oid not in mapped:
            if allow_partial: continue
            fail("MISSING_REQUIRED_OPERATION",f"{b['binding_id']}:{oid}")
        _,meta=ops[oid]; validate_readiness(b,meta)
        if meta["agent_access_required"]:
            paths=[p for p in b["access_paths"] if oid in p["operations"]]
            if not paths: fail("AGENT_ACCESS_PATH_MISSING",f"{b['binding_id']}:{oid}")
            if any(p["mechanism"]=="HUMAN_UI_ONLY" for p in paths): fail("MECHANICAL_HUMAN_INTERMEDIARY",f"{b['binding_id']}:{oid}")
            for ctx in b["supported_contexts"]:
                if not any(p["context"]==ctx and p.get("discovery_ref") and p.get("evidence_ref") for p in paths): fail("ACCESS_CONTEXT_NOT_PROVEN",f"{b['binding_id']}:{oid}:{ctx}")
    if b["capability_id"]=="knowledge_memory" and b.get("knowledge_write_bypasses_authoritative_ownership"): fail("KNOWLEDGE_OWNERSHIP_BYPASS",b["binding_id"])
    if b["capability_id"]=="identity_access" and b.get("raw_secret_delivered_to_agent") is True: fail("RAW_SECRET_AGENT_REQUIREMENT",b["binding_id"])
    if b["proof_environment"] not in {"sandbox","test","lower","simulation-plus-integration","production-safe-read"}: fail("UNSAFE_PROOF_ENVIRONMENT",b["binding_id"])
    if not b.get("actual_binding_exercised"): fail("DOCS_ONLY_PROOF",b["binding_id"])

def resolve(bindings,request):
    candidates=[b for b in bindings if request["operation"] in b["operation_mappings"]]
    if not candidates: fail("NO_APPLICABLE_BINDING",request["operation"])
    if len(candidates)>1: fail("AMBIGUOUS_BINDING",request["operation"])
    return candidates[0]

def runtime_outcome(req):
    if req.get("provider_condition")=="UNAVAILABLE": return "BLOCKED"
    if not req.get("identity_established"): return "BLOCKED"
    if req.get("current_entitlement") is False: return "DENIED" if req.get("oa")=="DENIED" and req.get("pep")=="ENFORCED" else "BLOCKED"
    if req.get("oa")=="DENIED": return "DENIED"
    if req.get("oa") in (None,"UNKNOWN"): return "BLOCKED"
    if req.get("pep")!="ENFORCED": return "BLOCKED"
    return "ALLOWED"

def validate_composition(bindings,plan):
    if plan.get("mode")!="COMPOSITION" or not plan.get("deterministic") or not plan.get("rationale"): fail("AMBIGUOUS_BINDING","composition")
    ids={b["binding_id"] for b in bindings}
    if not set(plan["binding_ids"]).issubset(ids): fail("BAD_BINDING_COMPOSITION","unknown member")
    covered=set()
    for b in bindings:
        if b["binding_id"] in plan["binding_ids"]: covered |= set(b["operation_mappings"])
    if not set(plan["operation_set"]).issubset(covered): fail("BAD_BINDING_COMPOSITION","incomplete coverage")

def run_scenario(caps,ops,profiles,sc):
    comp_ids=set(sc.get("resolution_plan",{}).get("binding_ids",[])); bindings=[expand_binding(b,profiles) for b in sc.get("bindings",[])]
    for b in bindings: validate_binding(caps,ops,b,allow_partial=b["binding_id"] in comp_ids)
    if sc.get("resolution_plan"): validate_composition(bindings,sc["resolution_plan"])
    if sc.get("request"):
        b=resolve(bindings,sc["request"]); got=runtime_outcome(sc["request"])
        if sc["request"].get("expected_outcome") and got!=sc["request"]["expected_outcome"]: fail("RUNTIME_OUTCOME_MISMATCH",got)
        if sc.get("assert_binding_proof_remains")=="PROVEN" and b["readiness"]["PROVEN"]["state"]!="SATISFIED": fail("BINDING_PROOF_MUTATED_BY_RUNTIME",b["binding_id"])

def validate_oeb_case(case):
    o=case.get("oeb",{})
    for f in ("oeb_id","revision","canonical_release"):
        if not o.get(f): fail("OEB_METADATA_MISSING",f)
    p=case.get("profile")
    if p:
        if p.get("base_oeb_revision")!=o["revision"]: fail("PROFILE_OEB_REVISION_MISMATCH",case["id"])
        if set(p.get("remove_constraints",[])) & set(o.get("mandatory_constraints",[])) and not p.get("exception_refs"): fail("PROFILE_SILENT_WEAKENING",case["id"])
    for w in case.get("active_work",[]):
        if not w.get("governing_oeb_revision"): fail("OEB_HISTORY_MISSING",case["id"])
        if w["governing_oeb_revision"]!=o["revision"] and "reassessment_required_by_policy" not in w: fail("OEB_REASSESSMENT_HOOK_MISSING",case["id"])

def run_cases(caps,ops,fixtures):
    failed=[]
    for sc in fixtures["scenarios"]:
        err=None
        try: run_scenario(caps,ops,fixtures["readiness_profiles"],sc)
        except CapabilityError as e: err=e.code
        got="FAIL" if err else "PASS"; exp=sc["expect"]; exerr=sc.get("expected_error"); ok=got==exp and (exp!="FAIL" or err==exerr)
        print(("PASS" if ok else "FAIL")+f": {sc['id']} expected={exp}"+(f"/{exerr}" if exerr else "")+f" got={got}"+(f"/{err}" if err else ""))
        if not ok: failed.append(sc["id"])
    if failed: fail("CAPABILITY_FIXTURES_FAILED",", ".join(failed))
    print(f"capability-integrity PASSED: {len(fixtures['scenarios'])} scenario fixtures")

def run_oeb(path):
    data=load(path); failed=[]
    for c in data["cases"]:
        err=None
        try: validate_oeb_case(c)
        except CapabilityError as e: err=e.code
        got="FAIL" if err else "PASS"; exp=c["expect"]; exerr=c.get("expected_error"); ok=got==exp and (exp!="FAIL" or err==exerr)
        print(("PASS" if ok else "FAIL")+f": {c['id']} expected={exp}"+(f"/{exerr}" if exerr else "")+f" got={got}"+(f"/{err}" if err else ""))
        if not ok: failed.append(c["id"])
    if failed: fail("OEB_FIXTURES_FAILED",", ".join(failed))
    print(f"oeb-integrity PASSED: {len(data['cases'])} scenario fixtures")

def main():
    try:
        defs=load(sys.argv[1]); fixtures=load(sys.argv[2]); caps,ops=validate_definitions(defs); run_cases(caps,ops,fixtures)
        if len(sys.argv)>3: run_oeb(sys.argv[3])
    except CapabilityError as e:
        print(f"FAIL: {e.code}: {e.message}"); return 1
    return 0

if __name__=="__main__": raise SystemExit(main())
