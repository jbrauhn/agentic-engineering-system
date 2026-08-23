# Handoff: L1-H Closure and L1-I Validation / Evidence / Independence Design Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` when creating the next relay handoff.

---

# 1. Current authoritative repository state

L1-H — Planning & Execution Coordination is complete, independently reviewed, machine-validated, and merged to `main`.

## Merge record

- PR: **#16 — Establish L1-H planning and execution coordination baseline**
- exact reviewed/tested PR head: **`def5fdf9adebd7b61f6afbacf4932794c5269429`**
- merge commit on `main`: **`ca1a63e748539d3a193c7be7f54a58a437faeec2`**
- merge date: 2026-08-22
- changed files: 16
- additions: 1082

All five applicable PR integrity jobs passed on the exact PR head before merge:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`
- `context-integrity`
- `planning-execution-integrity`

The new `planning-execution-integrity` suite passed:

> **52 semantic scenarios + 4 portability cases**

`main` remains unprotected. Repository branch-protection/ruleset enforcement is still **off**, so successful checks must not be described as merge-required/repository-enforced. Issue #12 remains OPEN and tracks this governance gap.

Issue #6 remains OPEN. L1-H did not impose one developer/agent environment, Portal, CLI, IDE, Dev Container, agent host, runtime, or orchestration interface.

No Kestrel material was introduced.

---

# 2. L1-H durable artifacts now on `main`

## Semantic artifacts

1. `L1-H_CANONICAL_PLAN_MODEL.md`
2. `L1-H_PROGRESSIVE_ELABORATION_READINESS_MODEL.md`
3. `L1-H_WORK_TOPOLOGY_EXECUTION_COORDINATION_MODEL.md`
4. `L1-H_ADAPTATION_ROUTING_MODEL.md`
5. `L1-H_VERIFICATION_EVIDENCE_ARCHITECTURE_MODEL.md`
6. `L1-H_WORKER_CONTEXT_RESULT_RECOVERY_MODEL.md`
7. `L1-H_RELATIONSHIP_VIEWS.md`

## Decisions

8. `DR-124-plan-semantics-progressive-elaboration-and-readiness.md`
9. `DR-125-work-topology-and-adaptation-routing.md`
10. `DR-126-execution-evidence-worker-recovery-and-federation.md`
11. `ADR-006-machine-readable-planning-execution-and-integrity.md`

## Machine/reference artifacts

12. `planning_execution_protocol.json`
13. `planning_execution_scenarios.json`
14. `planning_execution_portability_fixtures.json`
15. `validate_planning_execution.py`
16. `.github/workflows/planning-execution-integrity.yml`

Human L1-H semantic artifacts remain normative for meaning. JSON/Python/GitHub Actions remain conforming repository/reference implementation choices rather than Canonical AE technology requirements.

---

# 3. Final L1-H Plan semantics

A Plan is the governed, architecture-aware route from an exact approved Contract toward its Proof.

A conforming Plan revision supports, as applicable:

- exact governing Contract revision;
- exact Product/System Baseline revision;
- declared Plan scope/outcome;
- affected Architecture Model elements/relationships;
- L2/L3 decomposition or explicit progressive-elaboration rules;
- dependencies, sequencing constraints, and barriers;
- parallelizable work topology;
- Planning Depth;
- Planning Method;
- Context Requirements;
- required Capability Operations/Bindings;
- inherited authority/policy/approval requirements;
- Verification/Test Strategy derived from Contract Proof;
- evidence-production expectations;
- Validation-readiness/continuation expectations;
- material risks, constraints, assumptions, unresolved questions;
- permitted adaptation boundaries;
- explicitly deferred future detail and its elaboration envelope.

Conditionally applicable semantics may use typed subordinate structures/relationships rather than forcing one giant mandatory form.

Preserve:

> **One Plan may have multiple conforming representations; representation is not a second Plan entity.**

Plan is not a provider workflow, task-board schema, branch strategy, scheduler, or orchestration product.

---

# 4. Rolling-wave / elaboration-envelope semantics

Rolling-wave Planning is canonical-valid.

> **Previously deferred detail may be elaborated without a new Plan revision only when it remains inside an explicitly reviewed elaboration envelope.**

The envelope may constrain:

- scope;
- dependencies/barriers;
- architecture commitments/assumptions;
- authority/capability requirements;
- Verification/evidence route;
- sequencing;
- material risk/constraint assumptions;
- adaptation boundaries.

A new Plan revision + applicable review is required when later elaboration materially changes a reviewed semantic boundary.

Changed scope cannot silently inherit prior Plan Review.

A previously reviewed active scope may continue under its exact older Plan revision when a later revision affects only future/unaffected scope **and deterministic dependency/impact analysis establishes no effect** on the active scope.

Do not serialize all work merely because future scope remains under Planning.

---

# 5. Final execution-readiness semantics

An L2/L3 scope is ready for governed execution when the implementation can establish, as applicable:

1. approved/effective exact Contract revision;
2. exact governing Plan revision + valid scoped Plan Review;
3. exact/effective Product/System Baseline;
4. dependencies/barriers sufficiently resolved;
5. required Context Requirement satisfiable and bounded context reconstructable;
6. required Capability Operations resolvable through valid Bindings/Access Paths;
7. applicable authority evaluable under L1-F;
8. technical prerequisites available;
9. Verification/Test Strategy and evidence expectations defined;
10. adaptation boundaries known;
11. no unresolved blocking condition prevents valid execution.

Provider workflow labels (`Ready`, `In Progress`, `Done`, etc.) do not establish AE readiness, completion, Validation, or acceptance.

Canonical Executable Task remains distinct from provider Work Item.

---

# 6. Parallelism / dependency / barrier semantics

Canonical AE now defines provider-neutral work-topology semantics for:

- L2/L3 work scopes;
- dependencies;
- ordering constraints;
- barriers;
- independent branches;
- shared-resource conflicts;
- merge/reconciliation points;
- scope-specific authority/capability/context differences;
- evidence aggregation/reconciliation.

No canonical DAG engine, scheduler, queue, swarm, worker pool, branch strategy, or central orchestrator is required.

Independent ready scopes may execute concurrently.

A blocked branch does not automatically freeze unrelated valid work.

Blocking propagates only through meaningful dependencies/barriers/shared-resource conflicts/safety constraints or another explicit relationship making continuation invalid or unsafe.

Unsafe parallel continuation is prohibited where shared dependencies/resources or barriers require coordination.

Parallel branches must have a reconciliation path when their results jointly affect shared state, architecture, Proof/evidence, or Validation readiness.

---

# 7. Local adaptation versus backward routes

The final L1-H semantic routing rule is:

> **implementation adjustment inside reviewed boundaries → local adaptation**  
> **execution failure while reviewed route remains valid → Retry**  
> **material reviewed-route change while Contract remains valid → Replan**  
> **Goal / Spec / Proof or other Contract-level change → Contract Change Proposal**  
> **unresolved authority/risk/decision/policy issue → Escalate**

## Local adaptation

Allowed only inside reviewed Plan adaptation boundaries without material change to the reviewed engineering route.

## Retry

Used when execution failed but the reviewed Plan route remains valid. Prior failure/Verification/Validation history remains durable.

## Replan

Required for material reviewed-route change with Contract still valid. Creates a new Plan revision and applicable review for affected scope.

## Contract Change

Required for Goal/Spec/Proof or other Contract-level semantic change. Planning/Execution may propose but may not silently mutate Contract. Existing G5/Human Decision Authority remains controlling.

## Escalate

Used when a required risk/authority/policy/decision issue cannot be resolved within the current actor authority/governed route. Only affected scope blocks unless wider continuation becomes invalid/unsafe.

Preserve inherited invariant:

> **Execution may adapt within the reviewed Plan's authorized adaptation boundaries. It may not silently change the reviewed Plan or approved Contract.**

---

# 8. Entity-admission result

L1-H introduced **no new A1/A2 execution entity**.

The following remain subordinate B semantics, provider resources/references, Evidence relationships, lifecycle/history state, or derived/ephemeral state unless future evidence passes DR-108:

- Execution Attempt / Run;
- Execution Result;
- Work Decomposition / Execution Topology;
- Adaptation Record;
- Execution Coordination State;
- Verification Result;
- Worker Result.

L4 agent micro-plan remains ephemeral by default.

Before ephemeral L4/session/orchestrator state is intentionally discarded, material information that would otherwise be lost must already exist in its proper durable semantic owner or approved continuation state.

---

# 9. Verification / Evidence versus Validation treatment

Preserve this chain exactly:

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

Intermediate Verification may happen during Execution.

Execution success, test success, CI success, provider `Done`, or executor-created Evidence does **not** create Validation acceptance.

The doer shall not become its own judge.

Evidence may remain physically/provider-owned when Evidence Records/references preserve the required identity, provenance, and relationships.

Parallel evidence must be reconcilable for the applicable Validation scope.

This L1-H boundary is the main reason the next design domain should now be Validation itself.

---

# 10. Architecture / ADR / Baseline handling

Planning identifies affected architecture.

During Execution:

- ordinary Architecture Model changes inside the reviewed route may occur as governed work;
- consequential architecture choices requiring ADR create/relate ADRs under inherited semantics;
- architecture discovery materially changing the reviewed route → Replan;
- architecture discovery exposing Contract deficiency → Contract Change Proposal;
- not every implementation/code change becomes an ADR.

Product/System Baseline must not be silently mutated underneath active work.

Active work remains governed by the exact/effective Baseline identified by its reviewed Plan. Resulting accepted/validated state may later advance the Baseline through governed baseline-update semantics.

---

# 11. Worker/subagent context and result semantics

Delegated workers/subagents receive bounded task-specific context using L1-G Context Requirements rather than full transcript dumps.

Resolvable worker context includes, as applicable:

- exact/effective Contract;
- exact reviewed Plan revision/scope;
- L2/L3 work scope;
- Product/System Baseline / architecture neighborhood;
- dependencies/barriers/shared-resource constraints;
- authority/capability requirements;
- adaptation boundary;
- Verification/evidence expectations;
- relevant continuation/Handoff state.

Worker result remains subordinate by default and preserves/references as applicable:

- result/outcome;
- evidence/provenance;
- blockers/failures;
- dependency/resource conflict;
- architecture issue;
- Plan-deficiency signal;
- Contract-deficiency signal;
- material promotion requirement;
- reconciliation/next-step needs.

Workers may signal deficiencies but may not rewrite Plan/Contract authority.

Small worker results do not automatically require Handoff A2. Use Handoff only when L1-G continuation semantics require it.

Fresh or continuing workers are both valid so long as material state is not hidden/session-only.

---

# 12. Human collaboration / mechanical intermediary boundary

Legitimate Human participation includes:

- engineering judgment;
- alternatives/tradeoff reasoning;
- Human-reserved DA;
- organization-reserved approval;
- contextual expertise;
- material risk judgment.

L1-H adds no new universal Human gates merely because a Planning/Execution choice appears consequential.

A Human required only to copy/click/translate/upload/trigger an already-determined agent intent is mechanical middleware where the canonical operation should be agent-operable.

Preserve:

> **Human judgment is a feature. Human transcription is usually a defect.**

---

# 13. Planning / Execution source-of-truth and recovery

DR-107 federation remains controlling.

Examples:

- exact Plan revision: declared authoritative source;
- Work Management: selected provider-owned workflow properties;
- CI/runtime: provider run state/results;
- Evidence Records/references: material Evidence identity/provenance;
- R1: Canonical AE lifecycle meaning;
- R4: authority/policy/decision state;
- R3 Context Package: derived context, not Plan/execution authority;
- orchestrator queue/session/in-memory graph: derived/ephemeral coordination state.

A conforming implementation must reconstruct material Planning/Execution state after orchestrator/session loss.

The system owns durable state. Orchestration may project/use it.

---

# 14. Machine/reference proof result

`planning-execution-integrity` passed **52 semantic scenarios + 4 portability cases** on exact PR head `def5fdf9adebd7b61f6afbacf4932794c5269429`.

Coverage included:

- unapproved Contract rejection;
- exact Contract/Baseline control;
- affected architecture requirement;
- concurrent reviewed/executing + planning scopes;
- stale review inheritance rejection;
- unaffected older reviewed scope continuation only with deterministic no-impact analysis;
- inside/outside elaboration-envelope behavior;
- readiness across context/capability/authority/dependencies/technical/Verification boundaries;
- dependency change reassessment;
- all five adaptation/backward routes;
- worker Plan mutation rejection;
- worker material-discovery promotion;
- L4 state-loss rejection;
- provider Done ≠ Validation;
- executor Evidence ≠ self-Validation;
- safe independent parallel work;
- unrelated branch non-freezing;
- unsafe shared conflict blocking;
- Proof→Verification traceability;
- parallel Evidence reconciliation;
- architecture/ADR/Replan rules;
- silent Baseline mutation rejection;
- orchestrator-loss recovery;
- effective revision over newest revision;
- Human judgment vs clerical proxy;
- execution entity-inflation rejection.

Portability compared materially different implementations:

## Implementation A

- source-controlled Plan;
- Jira/Plane-like Work Management;
- CI jobs;
- multiple stateless/fresh workers;
- provider-native branch workflow.

## Implementation B

- workflow-provider Plan representation;
- different Work Management provider;
- long-lived agent/runtime;
- direct tool/API execution;
- materially different orchestration topology.

Equivalent conformance preserved governed Contract/Plan/Baseline, review scope, routing, blockers, Validation readiness, and recoverability without requiring identical orchestration.

All inherited `lifecycle-integrity`, `capability-integrity`, `authority-integrity`, and `context-integrity` jobs also passed on the exact same head.

---

# 15. Independent-review result

Independent review challenged:

- giant Plan/workflow-form inflation;
- rolling-wave serialization;
- stale review inheritance;
- provider Work Management becoming canonical truth;
- hidden central scheduler/orchestrator dependency;
- hidden worker-session durable state;
- executor Plan/Contract mutation;
- adaptation boundary misclassification;
- architecture/ADR bypass;
- unsafe dependency/resource races;
- blocked scope freezing unrelated work;
- technical capability being confused with OA;
- Human clerical middleware;
- Verification/Evidence self-Validation;
- missing Proof→Verification/evidence route;
- durable L4 shadow Plans;
- Context Package becoming execution authority;
- naive latest-revision selection;
- orchestrator crash destroying material state;
- topology-specific portability;
- A1/A2 entity inflation.

No Contract contradiction, new A1/A2 requirement, or material unresolved L1-H defect remained before merge.

---

# 16. Issue status

## Issue #12 — repository integrity enforcement

**OPEN.**

It now tracks five meaningful integrity jobs:

1. `lifecycle-integrity`
2. `capability-integrity`
3. `authority-integrity`
4. `context-integrity`
5. `planning-execution-integrity`

`main` protection remains disabled. Do not describe these checks as repository-enforced until branch/ruleset enforcement exists and an intentional failing-check merge-block test proves it.

## Issue #6 — Engineering Team Interface / Working Environment

**OPEN.**

L1-H provides Plan/work topology, worker coordination, Access Path consumption, context, authority/capability, and evidence semantics, but still does not solve the full Human/agent working-environment UX.

Preserve:

> **AE should require interface parity, not environment uniformity.**

---

# 17. Next genuine L1 design domain

## Recommended next domain: L1-I — Validation, Evidence Sufficiency & Independence

Rationale:

L1-H now ends at a coherent Validation-ready boundary. Contract v1.0 already requires independent Validation and defines lifecycle routes, and L1-C/D/E/F/G/H have provided the durable records, exact-revision gates, Capability Contract, authority, context, evidence-generation, and routing semantics needed to finally design Validation precisely.

The remaining gap is not “does Validation exist?” It is:

> **What minimum canonical Validation protocol lets materially different implementations independently judge whether exact Contract Proof has been satisfied using trustworthy Evidence, with sufficient independence, provenance, authority, and risk-sensitive rigor—without canonizing one validator product, one model/provider, mandatory physical separation, one quality framework, or one universal risk formula?**

This is the next Human Owner decision gate.

Do **not** implement L1-I from this handoff. The receiving session should perform the dialectic design/review, present the consequential decisions to the Human Owner, and make no L1-I GitHub writes until Human Owner approval.

---

# 18. L1-I inherited baseline — do not reopen silently

## Contract / lifecycle

- Proof is established before Execution.
- Execution produces/references Evidence.
- independent Validation evaluates the actual outcome against applicable Contract/Proof.
- Validation may reject apparent success for insufficient Evidence, unmet Contract, unintended effects, or failed intended outcome.
- Validation routes already include: Accept, Retry execution, Replan, propose Contract change, Escalate.
- core maxim: **The doer shall not become its own judge.**

## L1-C

- `Evidence Record [A2]` exists.
- `Validation Record [A2]` exists.
- Evidence Record is not evidence bytes; provider-owned evidence may remain external.
- issued Validation/Evidence records are historically immutable/non-destructive.
- exact-revision identity/provenance applies.

## L1-D

- G4 `VALIDATION_ACCEPTANCE` exists.
- G4 requires exact Contract revision and independent judgment.
- Increment ACCEPTED does not imply whole-Contract/Loop acceptance.
- final Loop `CLOSED / ACCEPTED` requires independent final Contract-scope Validation and reconciliation.
- Retry/Replan/Contract Change/Escalate routes already exist.

## L1-E

Validation Capability Contract operations already exist:

- `validation.request`
- `validation.status`
- `validation.result.read`
- `validation.evidence.read`

R6 coordination is not synonymous with one external Validation Provider.

## L1-F

- identity/entitlement/OA/DA/policy/PEP semantics apply to Validation operations where protected/applicable.
- role label alone is not authority.
- Human DA is required only where Contract/higher policy reserves it; do not make all Validation Human approval by default.

## L1-G

- Context Package is derived and is **not automatically Evidence**.
- consequential Validation may reference Context Assembly Receipt when additional assembled context materially influenced judgment beyond direct canonical references.
- source authority/currentness/security rules apply to Validation inputs.

## L1-H

Preserve exactly:

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

Executor-created Evidence, CI success, provider Done, and test success do not self-create Validation acceptance.

Parallel Evidence must be reconcilable for the applicable Validation scope.

---

# 19. L1-I design questions — consequential Human Owner decisions

The receiving session should challenge and refine the following. Present a leading recommendation + strongest credible alternative for consequential choices.

## Decision area A — Validation Requirement / scope model

Question:

> What exactly must a Validator be told about what is being judged?

Consider a subordinate **Validation Requirement [B]** or equivalent, not automatically a new A1/A2 entity.

Potential semantics:

- Validation purpose/type;
- exact Contract revision;
- applicable Proof criteria;
- declared Validation scope (Increment, integrated result, final Contract scope, adoption/installation, other governed scope);
- applicable Plan/Baseline/architecture references;
- required Evidence classes/relationships;
- required independence characteristics;
- risk/policy constraints;
- required currentness/effectivity;
- unresolved findings/known limitations;
- authority/approval requirements where applicable;
- expected outcome/routing semantics.

Decide whether this adds useful precision or becomes another procedural form.

Do not create a second Validation entity if existing Validation Record + subordinate requirement semantics suffice.

---

## Decision area B — What “independent Validation” canonically means

Current invariant:

> **minimum architecture requirement = independence of the Validation judgment path from the work-producing execution path.**

Need to define the minimum semantic test.

Possible independence dimensions include, as applicable:

- actor/identity separation;
- agent/model invocation separation;
- session/context separation;
- inability of work-producing actor to issue its own acceptance;
- independent access to Evidence/source state rather than trusting executor summary;
- independent authority to form the Validation judgment;
- organizational review separation;
- model/provider diversity;
- environment/toolchain separation;
- Human participation.

Do **not** assume every dimension must be mandatory.

Central question:

> What is the minimum invariant that makes the judgment meaningfully independent, and which stronger independence dimensions should be risk/policy-sensitive rather than universal?

Strong alternatives to test:

1. **judgment-path independence** as the invariant, with risk-sensitive strengthening;
2. require a fresh separate actor/agent instance for every Validation;
3. require separate provider/model/environment;
4. require Human Validator for material work.

Leading hypothesis to test: keep only judgment-path independence universal; express stronger separation through Validation Requirement/OEB/Product policy/risk classification.

A same underlying model used through a genuinely separate Validator invocation may or may not be sufficient depending on risk/policy—do not settle this by intuition alone.

---

## Decision area C — Validator role, identity, and authority

Already inherited:

- Validator role can be Human, fresh AI, other agentic system, or mixed Human–AI, subject to independence/risk/authority/policy.
- role ≠ identity ≠ authority.

Need to decide:

- what minimum identity/provenance must a Validation Record carry;
- whether validator needs OA for `validation.request` versus authority to issue the Validation judgment;
- whether a Validation judgment itself is DA or a separate R6 judgment semantic;
- when Human DA is additionally required by Contract/organization policy;
- how external Validation provider identity and independent Validator actor identity relate.

Avoid making “Validator” a magic privileged role label.

---

## Decision area D — Evidence sufficiency model

Need a canonical semantics for deciding whether Evidence is sufficient without creating a universal test framework.

Potential factors:

- applicable Proof criterion coverage;
- exact scope/revision relationship;
- source authority;
- provenance/integrity;
- currentness/effectivity;
- evidence independence where required;
- completeness;
- contradictory evidence;
- negative evidence/failures;
- environmental relevance;
- reproducibility/retrievability where applicable;
- known gaps/limitations.

Question:

> Should Evidence sufficiency be a subordinate assessment inside Validation, a typed Evidence Set/projection, or another concept?

Leading hypothesis: keep Evidence sufficiency subordinate to Validation Record/Requirement; avoid a new A1/A2 `Evidence Set` unless identity/lifecycle evidence passes DR-108.

---

## Decision area E — Evidence invalidation / supersession

Preserve historical non-destructive semantics.

If Evidence is later discovered stale, invalid, incomplete, tampered, or superseded:

- do not rewrite the historical Evidence Record or old Validation judgment;
- create later finding/evidence/Validation/decision state that changes current reliance as appropriate;
- determine whether affected accepted work must be revalidated/escalated.

Need to define the current-reliance semantics without making historical truth mutable.

---

## Decision area F — Validation result versus lifecycle route

L1-D already has routes:

- ACCEPT;
- RETRY_EXECUTION;
- REPLAN;
- PROPOSE_CONTRACT_CHANGE;
- ESCALATE.

Need decide whether the Validation Record's **judgment result** should be identical to those routes or whether judgment and resulting lifecycle route are distinct concepts.

Example tension:

```text
judgment: Proof not satisfied because evidence is incomplete
route: RETRY_EXECUTION
```

versus:

```text
validation result = RETRY_EXECUTION
```

Leading hypothesis: distinguish the independent judgment from the R1 lifecycle disposition/route so R6 does not become lifecycle control, while retaining deterministic mapping/provenance between them.

Test whether that adds useful precision or needless vocabulary.

---

## Decision area G — Increment Validation versus final Contract Validation

DR-113 is authoritative:

> Increment acceptance does not imply whole-Contract/Loop acceptance.

Need precise reconciliation semantics for final Contract Validation:

- may reuse valid prior Increment Validation/Evidence;
- should not rerun everything ceremonially;
- must reconcile cross-Increment/integration/final-state effects;
- must account for multiple effective Contract/Plan revisions where historically valid;
- must prove final applicable Contract/Proof;
- must detect gaps that local Increment Validation could not see.

Question:

> What minimum final-reconciliation proof is canonical without prescribing one integration-test process?

---

## Decision area H — Risk-sensitive Validation rigor

Contract requires independent Validation but does not define one risk-level taxonomy.

Need to decide whether Canonical AE should define:

- universal Validation assurance levels;
- only a risk/policy hook requiring organization-defined rigor;
- a small canonical dimension model without fixed levels.

Possible dimensions:

- independence strength;
- Evidence breadth/depth;
- Human participation;
- model/provider diversity;
- environment separation;
- reproducibility;
- required negative testing;
- approval/DA requirements.

Leading hypothesis: canonicalize **dimensions/requirements**, not universal numeric risk tiers, unless implementation-team adoption would otherwise be ambiguous.

---

## Decision area I — Verification versus independent Validation

Prevent these anti-patterns:

- executor tests its own work and calls that Validation;
- CI green = Accepted;
- static analysis = Validation by default;
- reviewer trusts executor summary without independently resolving material state;
- the same workflow step produces work and self-issues G4 acceptance.

But also avoid ceremonial duplicate testing.

Need define how Verification artifacts can legitimately become Evidence used by an independent Validator without requiring the Validator to rerun every test.

---

## Decision area J — Context in Validation

L1-G says Context Package is not automatically Evidence.

Need define:

- when Validator may rely on bounded Context Package for navigation/reasoning;
- when exact direct Evidence/source references are required;
- when Context Assembly Receipt must be retained because assembled context materially influenced judgment;
- how stale/inaccessible/conflicting source context blocks or qualifies Validation.

Do not introduce universal prompt logging or chain-of-thought retention.

---

## Decision area K — Validation Provider versus R6 responsibility

Preserve:

- R6 = canonical Evidence & Validation Coordination semantics;
- External Validation Provider = one capability/provider mechanism;
- Validator actor = role-bearing actor/entity making independent judgment;
- provider test/eval product ≠ independent judgment automatically.

Need ensure a conforming implementation can combine:

- Human review;
- AI Validator;
- CI/test results;
- security/static-analysis tools;
- evaluation services;
- observability evidence;
- multiple mechanisms.

No central Validator Service or one vendor should become canonical.

---

## Decision area L — Adoption / installation Validation

Existing L1-C/L1-A semantics use the normal Validation Record for adoption/conformance assessment rather than creating an eighth special Validation entity.

Need decide whether L1-I should explicitly generalize the same Validation protocol across:

- engineering work Validation;
- final Contract Validation;
- Organization-specific AE installation/adoption Validation;
- Capability Binding Validation.

Leading hypothesis: same core Validation semantics, specialized Validation Requirements/scopes.

---

# 20. Candidate machine-testable L1-I behaviors

If the Human Owner later approves L1-I, likely introduce `validation-integrity` using the staged ADR-002–006 pattern.

Before approval, only design the semantics.

Candidate future tests should include at least:

1. executor cannot issue its own G4 acceptance;
2. independent Validator can use executor-produced Evidence without becoming executor;
3. Validation Record references exact Contract/Proof/scope;
4. missing Proof coverage prevents acceptance;
5. stale/wrong-revision Evidence cannot satisfy exact requirement;
6. contradictory Evidence cannot be silently ignored;
7. provider green/test success does not equal Validation judgment;
8. Context Package alone is not Evidence;
9. Validator can independently resolve material Evidence/source state;
10. Validator role label without identity/authority/provenance is insufficient;
11. same implementation supports Human, AI, and mixed Validator actors where policy permits;
12. stronger independence requirements can be imposed by OEB/Product/risk without changing canonical core;
13. risk-sensitive requirement can require Human review or model/provider diversity without making it universal;
14. Increment acceptance does not auto-accept final Contract;
15. final Contract Validation reuses valid prior Evidence/Validation while reconciling cross-scope effects;
16. later Evidence invalidation does not rewrite historical Validation;
17. current reliance can trigger revalidation/escalation after Evidence invalidation;
18. Validation judgment and lifecycle route remain correctly related;
19. Retry route preserves failed Validation history;
20. Replan route preserves prior Plan/Validation history;
21. Contract deficiency routes through G5 rather than Validator editing Contract;
22. unresolved Evidence authority/currentness blocks or produces appropriate non-acceptance state;
23. parallel Evidence aggregates without losing scope/provenance;
24. work-producing actor cannot manipulate Evidence references to bypass independence;
25. external Validation Provider result alone does not become G4 acceptance unless canonical independent judgment semantics are satisfied;
26. adoption/installation Validation uses same core protocol without a new entity type;
27. two materially different Validation architectures produce equivalent governed judgments;
28. no separate model/provider/environment is universally required unless risk/policy says so;
29. no Human Validator is universally required beyond existing Human-reserved authority/policy;
30. no central Validator service is required.

---

# 21. Candidate portability proof for L1-I

Test at least two materially different synthetic implementations.

## Implementation A

- CI/test/security Evidence;
- independent AI Validator invocation;
- exact source/evidence resolution;
- organization policy requires Human review only for high-risk scopes.

## Implementation B

- different provider stack;
- Human + tool-assisted Validator for some scopes;
- evaluation service / observability Evidence;
- dynamic organization policy for independence requirements.

Equivalent canonical outcome should preserve:

- exact Contract/Proof/scope being judged;
- Evidence coverage/sufficiency result;
- required independence semantics;
- source/currentness/conflict handling;
- judgment/result;
- resulting lifecycle route;
- durable Validation provenance;
- no self-acceptance.

Do not require identical Validator actor type, model/provider, testing stack, physical environment, or review interface.

---

# 22. Entity-admission guardrail for L1-I

Existing first-class records already include:

- Evidence Record [A2];
- Validation Record [A2].

Do not add convenience entities such as:

- Validation Attempt;
- Validation Session;
- Validation Run;
- Evidence Set;
- Quality Gate;
- Validator Assignment;
- Validation Finding;

unless implementation/design review shows a genuine independent identity/lifecycle need that passes DR-108.

Prefer subordinate B semantics, typed relationships, External Resource References, or provider-owned objects where sufficient.

If a new A1/A2 need genuinely emerges, stop and surface it to the Human Owner.

---

# 23. Issue #12 and issue #6 for future L1-I

If a future `validation-integrity` job is implemented after Human Owner approval:

- update existing issue #12 to track it;
- do not create another repository-governance issue;
- keep #12 OPEN until branch protection/ruleset enforcement is configured and proven by an intentional failing-check merge block.

Keep issue #6 OPEN. Validation design may consume Access Paths / working-environment interfaces, but must not solve or mandate one Portal/CLI/IDE/runtime.

---

# 24. L1-I independent-review failure tests

The design session should challenge at least:

1. Can executor/test author self-issue Validation acceptance?
2. Can provider green status become G4 truth?
3. Can Validator trust an executor summary instead of authoritative Evidence?
4. Can Context Package become Evidence merely because it was consumed?
5. Can stale/wrong-revision Evidence satisfy Proof?
6. Can contradictory Evidence be silently discarded?
7. Can Evidence authority/provenance be ambiguous at acceptance?
8. Can role label `Validator` substitute for identity/independence/authority?
9. Can independence become cosmetic (same execution path simply relabeled)?
10. Does the model accidentally require a fresh model/provider/environment for every Validation?
11. Does it accidentally require Human review universally?
12. Does risk sensitivity become so vague that implementations can self-declare weak Validation as sufficient?
13. Does a universal risk-tier scheme over-constrain organizations/products?
14. Can Increment acceptance incorrectly imply final Contract acceptance?
15. Can final Validation become a ceremonial rerun rather than reconciliation?
16. Can later-invalid Evidence rewrite historical Validation instead of preserving history?
17. Can Validator mutate Contract/Plan instead of routing Retry/Replan/Contract Change?
18. Can R6 become a central Validator service requirement?
19. Can Validation Capability provider result be confused with canonical independent judgment?
20. Can adoption/conformance Validation create a duplicate special entity model?
21. Can Evidence bytes be unnecessarily copied into AE and create shadow truth?
22. Can parallel Evidence lose scope/provenance during aggregation?
23. Does a new entity get added only for implementation convenience?
24. Can Human DA and Validation judgment become conflated?
25. Can G4 acceptance occur while required authority/currentness/context is INDETERMINATE?

---

# 25. Scope guardrails for the L1-I design session

Do NOT introduce or assume:

- Kestrel material;
- one Validator product/service;
- one AI model/provider;
- mandatory model-provider diversity for all work;
- mandatory physical environment separation for all work;
- universal Human Validator requirement;
- one risk formula or scoring model without Human Owner approval;
- one testing framework;
- one quality framework;
- one CI/CD provider;
- one policy engine;
- new generic Quality Gate entity;
- detailed standards-applicability algorithm;
- full developer-environment solution;
- universal prompt/chain-of-thought logging.

Use existing canonical identities, exact revisions, Evidence/Validation records, authority, context, capability, and lifecycle routes.

---

# 26. Required output of the receiving L1-I design session

Do **not** implement L1-I yet.

Produce a dialectic design proposal for Human Owner review that includes:

1. precise Validation scope/requirement model;
2. minimum independence invariant;
3. risk-sensitive strengthening model and strongest alternative;
4. Validator identity/authority/provenance semantics;
5. Evidence sufficiency model;
6. Evidence invalidation/current-reliance semantics;
7. Validation judgment versus lifecycle-route semantics;
8. Increment versus final Contract Validation reconciliation;
9. Verification/Evidence versus Validation boundary;
10. Context/provenance role in Validation;
11. Validation Provider versus R6 responsibility boundary;
12. adoption/installation Validation relationship;
13. entity-admission review;
14. likely machine-testable protocol/fixtures after approval;
15. portability proof design;
16. minimum necessary future DR/ADR grouping;
17. consequential Human Owner decision set with leading recommendation + strongest credible alternative + tradeoff + inherited authority/traceability.

If a Contract contradiction is found, stop and surface it.

If a new A1/A2 entity appears necessary, explicitly run DR-108 admission reasoning and surface it rather than silently adding it.

No L1-I GitHub writes until Human Owner approval.

---

# 27. Relay requirement

When the L1-I design/review session is complete and the Human Owner later approves/refines it, the implementing session must use a new relay handoff file.

Do not overwrite this file or prior handoffs.

Follow `handoffs/README.md`.
