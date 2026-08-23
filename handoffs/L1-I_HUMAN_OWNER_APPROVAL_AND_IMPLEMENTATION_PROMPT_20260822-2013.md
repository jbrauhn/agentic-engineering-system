# Handoff: L1-I Human Owner Approval and Implementation Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Human Owner decision: **APPROVED**.

Proceed with implementation of **L1-I — Validation, Evidence Sufficiency & Independence** using the L1-H closure/design handoff as the inherited baseline and the approved recommendations below.

Read the complete prior handoff before acting:

`handoffs/L1-I_L1-H_CLOSURE_AND_VALIDATION_DESIGN_PROMPT_20260822-2000.md`

Do not reinterpret this approval as permission to reopen higher-authority semantics silently.

---

# 1. Independent Validation — approved universal invariant

Canonical AE shall require **judgment-path independence**.

Minimum universal semantics:

- the work-producing execution path may not issue its own Validation acceptance;
- the Validator must be able to independently resolve the material Evidence and authoritative state needed to judge the declared Validation scope;
- the Validation judgment must be attributable to an identified Validator actor/path with reconstructable provenance;
- provider/test/CI success, executor summary, executor-created Evidence, or role label alone does not create G4 acceptance.

Stronger independence dimensions are **risk/policy-sensitive**, not universal Canonical AE requirements.

Organizations/Product policy may require, as applicable:

- fresh agent/invocation;
- separate actor/identity;
- Human participation;
- different model/provider;
- environment/toolchain separation;
- organizational review separation;
- additional negative testing/reproducibility;
- stronger Evidence breadth/depth.

Do NOT make any of those stronger dimensions universal unless higher authority already requires them.

A same underlying model/provider may be conforming for some scopes if the judgment path is genuinely separate and applicable OEB/Product/risk policy permits it.

---

# 2. Validation Requirement [B]

APPROVED.

Introduce subordinate **Validation Requirement [B]** or semantically equivalent structure.

Do not create a new A1/A2 Validation entity.

It should support, as applicable:

- Validation purpose/type;
- exact Contract revision;
- applicable Contract Proof criteria;
- declared Validation scope;
- applicable Plan/Baseline/Architecture references;
- required Evidence classes/relationships;
- required independence characteristics;
- risk/policy constraints;
- required currentness/effectivity;
- unresolved findings/known limitations;
- authority/approval requirements where applicable;
- expected judgment/routing semantics.

Use operation/scope-specific requirements rather than one giant mandatory form.

---

# 3. Evidence sufficiency

APPROVED.

Evidence sufficiency remains subordinate to the Validation Requirement / Validation judgment.

Do NOT introduce a first-class `Evidence Set` A1/A2 merely for convenience.

A conforming sufficiency assessment should consider as applicable:

- Proof-criterion coverage;
- exact scope/revision relationship;
- source authority;
- provenance/integrity;
- currentness/effectivity;
- independence characteristics where required;
- completeness;
- contradictory/negative Evidence;
- environmental relevance;
- retrievability/reproducibility where applicable;
- known gaps/limitations.

A Validator may use executor-produced Verification results as Evidence, but independent Validation must judge their sufficiency rather than treating them as acceptance.

Preserve:

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

---

# 4. Validation judgment versus lifecycle route

APPROVED: keep these distinct.

R6 owns the independent Validation judgment semantics.

R1 owns lifecycle transition/route semantics.

The Validation Record should be able to express what the Validator concluded independently of the resulting lifecycle route.

Examples:

- judgment: Proof satisfied;
- judgment: Proof not satisfied — Evidence incomplete;
- judgment: Proof not satisfied — implementation defect;
- judgment: Proof not satisfied — reviewed Plan route deficient;
- judgment: Contract/Proof deficiency detected;
- judgment: unable to establish sufficient trustworthy Evidence/current state.

The resulting governed route remains one of the established L1-D outcomes as applicable:

- ACCEPT;
- RETRY_EXECUTION;
- REPLAN;
- PROPOSE_CONTRACT_CHANGE;
- ESCALATE.

Do not let R6 silently become lifecycle control.

The relationship from judgment to route must be deterministic/reconstructable under applicable semantics/policy.

---

# 5. Increment Validation versus final Contract Validation

APPROVED.

Preserve DR-113:

> **Increment acceptance does not imply whole-Contract/Loop acceptance.**

Final Contract-scope Validation may reuse valid prior Increment Evidence and Validation judgments.

Do not require ceremonial rerun of every prior test merely because final Validation occurs.

Final Validation must still reconcile, as applicable:

- cross-Increment interactions;
- integration effects;
- final system/product state;
- unresolved prior limitations/findings;
- multiple historically valid Plan/Contract/Baseline revisions;
- full applicable Contract Proof coverage;
- gaps that local Increment Validation could not observe.

Final acceptance requires independent judgment against the final applicable Contract scope/revision and Proof.

---

# 6. Evidence invalidation / current reliance

APPROVED.

Historical Evidence Records and Validation Records remain non-destructive.

If Evidence is later discovered to be stale, invalid, incomplete, tampered, superseded, or otherwise unreliable:

- do not rewrite the historical Evidence Record;
- do not rewrite the historical Validation judgment;
- create later finding/evidence/Validation/decision state as appropriate;
- update current reliance semantics explicitly;
- revalidate/escalate affected current work when required by scope/policy/risk.

Historical fact remains:

> what Evidence existed and what judgment was issued at that time.

Current reliance may change later without rewriting history.

---

# 7. Risk-sensitive Validation rigor

APPROVED.

Canonical AE should define **assurance/independence dimensions and requirement hooks**, not one universal numeric risk tier model.

Potential dimensions include:

- independence strength;
- Evidence breadth/depth;
- Human participation;
- model/provider diversity;
- environment separation;
- reproducibility;
- negative testing;
- approval/DA requirements;
- additional provenance/currentness requirements.

OEB/Product/System policy may select/strengthen these dimensions by risk/classification/product context.

Do not create one universal risk formula or mandatory assurance-level scale unless later design evidence and Human Owner approval justify it.

Do not permit risk sensitivity to become a loophole where an implementation simply self-declares weak Validation as sufficient; the effective requirement must be explicit, policy-backed, scoped, and reconstructable.

---

# 8. Validator identity / authority / provenance

Preserve:

role ≠ identity ≠ entitlement ≠ OA ≠ DA ≠ independent Validation judgment.

A Validation Record should support reconstructing, as applicable:

- Validator actor/identity;
- Validator type (Human / AI / other agentic system / mixed) where useful;
- exact Validation Requirement/scope;
- independence basis/provenance;
- material Evidence/source references;
- applicable authority/policy context;
- judgment/result/rationale;
- lifecycle route relationship;
- issued time/version.

Do not make the `Validator` role label sufficient by itself.

Do not automatically classify every Validation judgment as Human Decision Authority.

Where Contract/OEB/Product policy requires Human DA or another approval in addition to independent Validation, preserve that as a separate authority requirement.

Validation Capability provider identity and Validator actor identity may differ.

---

# 9. Verification / Evidence versus Validation

APPROVED boundary:

- Verification may be performed during Execution;
- Verification/test/security/static-analysis/eval/CI results may become Evidence;
- the Validator may reuse trustworthy Evidence rather than rerunning every test;
- those results do not become Validation merely because they are green;
- the work-producing path may not convert its own Evidence directly into G4 acceptance.

Preserve:

> **The doer shall not become its own judge.**

Avoid ceremonial duplication: independent judgment does not universally mean independent re-execution of every test.

---

# 10. Context role in Validation

Preserve L1-G:

- Context Package is derived;
- Context Package is not Evidence merely because the Validator consumed it;
- exact material Evidence/source references must remain resolvable;
- stale/inaccessible/conflicting authoritative state cannot be hidden by a summary;
- Context Assembly Receipt is retained only when consequential-use/policy requires it and assembled context materially influenced the judgment beyond directly referenced canonical inputs.

No universal prompt logging or chain-of-thought retention.

---

# 11. Validation Provider versus R6

Preserve the distinction:

- R6 = canonical Evidence & Validation Coordination responsibility;
- External Validation Provider = capability/provider mechanism;
- Validator actor/path = entity/path issuing the independent judgment;
- CI/test/eval/security provider output = Evidence/provider result unless/until canonical Validation semantics are satisfied.

No central Validator service is canonical.

A conforming implementation may combine Humans, AI Validators, CI/test systems, evaluation services, security tools, observability, and other Evidence sources.

---

# 12. Adoption / installation / capability Validation

APPROVED: use the same core Validation protocol with specialized Validation Requirements/scopes.

Do not create a duplicate special Validation entity model for:

- engineering Increment Validation;
- final Contract Validation;
- Organization-specific AE installation/adoption Validation;
- Capability Binding/readiness Validation.

Specialize scope/requirements, not entity type.

---

# 13. Entity admission

APPROVED leading posture: **no new A1/A2 entity is currently warranted.**

Do not introduce convenience entities such as:

- Validation Attempt;
- Validation Session;
- Validation Run;
- Evidence Set;
- Quality Gate;
- Validator Assignment;
- Validation Finding;

unless implementation/design review discovers a genuine independent identity/lifecycle need that passes DR-108.

If such a need appears, stop and surface it to the Human Owner rather than adding it silently.

Use subordinate B semantics, typed relationships, provider references, Evidence Record [A2], and Validation Record [A2] where sufficient.

---

# 14. Machine-readable Validation layer

APPROVED.

Continue the staged ADR-002–006 pattern.

Likely cohesive artifacts may include:

- `validation_protocol.json`
- `validation_scenarios.json`
- `validation_portability_fixtures.json`
- `validate_validation.py` (or another non-awkward cohesive name if preferred)
- `.github/workflows/validation-integrity.yml`

Human semantic artifacts remain normative for meaning.

The executable representation proves semantics; it must not become a production Validator product or universal quality framework.

Create a distinct `validation-integrity` job.

---

# 15. Validation-integrity minimum coverage

At minimum test:

1. executor/work-producing path cannot issue its own G4 acceptance;
2. independent Validator may use executor-produced Evidence without becoming executor;
3. Validation Record references exact Contract/Proof/scope;
4. missing Proof coverage prevents acceptance;
5. stale/wrong-revision Evidence cannot satisfy an exact requirement;
6. contradictory Evidence cannot be silently ignored;
7. provider green/test success does not equal canonical Validation judgment;
8. Context Package alone is not Evidence;
9. Validator independently resolves material Evidence/source state;
10. Validator role label without identity/independence/provenance is insufficient;
11. Human, AI, and mixed Validator paths can conform where policy permits;
12. OEB/Product/risk policy can strengthen independence requirements without changing Canonical Core;
13. Human review or model/provider diversity can be required by policy without becoming universal;
14. Increment acceptance does not auto-accept final Contract;
15. final Contract Validation reuses valid prior Evidence/Validation but reconciles cross-scope/final effects;
16. later Evidence invalidation does not rewrite historical Validation;
17. changed current reliance can trigger revalidation/escalation;
18. Validation judgment and lifecycle route remain distinct but correctly related;
19. Retry preserves failed Validation history;
20. Replan preserves prior Plan/Validation history;
21. Contract deficiency routes through Contract Change/G5 rather than Validator mutation;
22. unresolved Evidence authority/currentness cannot yield acceptance;
23. parallel Evidence aggregation preserves scope/provenance;
24. Evidence/reference manipulation cannot bypass independence;
25. external Validation Provider result alone cannot create G4 acceptance;
26. adoption/installation Validation uses same core semantics;
27. two materially different Validation architectures produce equivalent governed judgments;
28. different model/provider/environment is not universally required;
29. Human Validator is not universally required beyond Contract/policy;
30. no central Validator service is required.

Add any additional scenarios needed to falsify the approved semantics.

---

# 16. Portability proof

Use at least two materially different synthetic Validation architectures.

Example A:

- CI/test/security Evidence;
- independent AI Validator invocation;
- exact source/Evidence resolution;
- Human review required only for policy-designated higher-risk scopes.

Example B:

- different provider/tool stack;
- Human + tool-assisted Validator for selected scopes;
- eval/observability Evidence;
- dynamically specialized independence requirements from organization/Product policy.

Equivalent conformance should preserve:

- exact Contract/Proof/scope;
- Evidence sufficiency result;
- required independence semantics;
- source/currentness/conflict handling;
- Validation judgment;
- resulting lifecycle route relationship;
- durable provenance;
- no self-acceptance.

Do not require identical actor type, model/provider, environment, test stack, or interface.

---

# 17. Issue #12 / issue #6

If `validation-integrity` is introduced, update existing issue #12 to track it with the prior five jobs.

Keep issue #12 OPEN until branch protection/ruleset enforcement actually requires applicable integrity checks and an intentional failing-check merge-block test proves enforcement.

Do not claim checks are merge-required until then.

Keep issue #6 OPEN.

L1-I may consume Access Path/context/evidence interfaces but must not solve or mandate one Portal/CLI/IDE/Dev Container/runtime.

---

# 18. Human Owner-approved decision summary

The following seven recommendations are approved:

1. universal minimum = judgment-path independence, with risk/policy-sensitive strengthening;
2. introduce subordinate Validation Requirement [B];
3. keep Evidence sufficiency inside Validation semantics, no Evidence Set entity;
4. keep independent Validation judgment separate from R1 lifecycle route;
5. final Contract Validation reuses valid prior Increment Evidence/Validation but performs final reconciliation;
6. preserve historical Evidence/Validation records while allowing later evidence invalidation to change current reliance/revalidation needs;
7. implement machine-readable Validation semantics and `validation-integrity` CI, adding it to issue #12.

Supporting consequences in sections 7–17 above are part of this approval.

---

# 19. Implementation authorization

You are authorized to implement L1-I now.

Proceed using the established workflow:

```text
branch
→ semantic Validation/Evidence/Independence artifacts
→ machine-readable protocol/scenarios/portability fixtures
→ validator
→ validation-integrity CI
→ minimum useful DRs/ADR
→ issue #12 update if applicable
→ keep #6 open
→ independent review against Contract + L1-A–H + explicit failure tests
→ correct material findings
→ PR
→ verify all applicable integrity jobs on exact PR head
→ merge
→ write complete next relay handoff to a new unique file
```

Do not introduce Kestrel.

Do not canonize a Validator vendor, model/provider, testing framework, quality framework, central service, universal Human validator, universal provider diversity, universal environment separation, or risk formula.

Do not silently add a new A1/A2 entity.

After merge, the next relay handoff must include a concise L1-I closure plus the next genuine L1 design prompt.

Follow `handoffs/README.md` for the relay.