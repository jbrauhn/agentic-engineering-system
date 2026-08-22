# Handoff: L1-H Human Owner Approval and Implementation Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` when creating the next relay handoff.

---

# 1. Human Owner decision

The Human Owner approves the L1-H recommendations presented by the review session.

Proceed with L1-H — Planning & Execution Coordination implementation using the decisions and guardrails below.

You are authorized to make GitHub writes for L1-H after incorporating these decisions.

Do not reopen L1-A through L1-G unless a genuine contradiction is discovered.

---

# 2. Approved Decision 1 — Canonical Plan semantic minimum

A conforming Plan revision must carry enough semantics to be executable, reviewable, architecture-aware, traceable to Contract Proof, and bounded for governed adaptation, without becoming a giant mandatory form.

The Plan must support, as applicable:

- exact governing Contract revision;
- exact Product/System Baseline revision;
- declared Plan scope/outcome;
- affected architecture elements/relationships;
- L2/L3 decomposition or explicit progressive-elaboration rules;
- dependency/sequencing constraints;
- parallelizable topology where applicable;
- Planning Depth;
- Planning Method;
- Context Requirements;
- required Capability Operations/Bindings;
- inherited authority/policy/approval requirements;
- Verification/Test Strategy derived from Contract Proof;
- evidence-production expectations;
- Validation-readiness/handoff expectations;
- relevant risks/constraints/assumptions;
- permitted adaptation boundaries;
- explicitly deferred future detail.

Conditionally applicable semantics may be represented through typed relationships/subordinate structures rather than one universal fixed form.

Do not turn Plan into a workflow checklist or provider-specific task schema.

Preserve:

> **One Plan may have multiple conforming representations; representation is not a second Plan entity.**

---

# 3. Approved Decision 2 — Progressive elaboration / rolling-wave Planning

Rolling-wave Planning is approved.

Future detail may be elaborated without creating a new Plan revision only when the new detail remains inside an explicitly reviewed elaboration envelope.

Approved invariant:

> **Previously deferred detail may be elaborated without a new Plan revision only when that elaboration remains within explicitly reviewed scope, constraints, dependencies, architecture assumptions, authority/capability requirements, verification expectations, and adaptation boundaries.**

A new Plan revision plus applicable re-review is required when later elaboration materially changes any reviewed semantic boundary, including as applicable:

- reviewed scope;
- dependency topology;
- architecture commitments/assumptions;
- authority or capability assumptions;
- verification/evidence route;
- sequencing/barriers;
- material risk/constraint assumptions;
- permitted adaptation boundary;
- another reviewed semantic that could change execution meaning.

A previously reviewed scope may continue under its exact reviewed Plan revision when a later Plan revision affects only future/unaffected scope and deterministic dependency-impact analysis shows no effect on the active scope.

Changed scope may not silently inherit prior Plan Review.

Do not serialize all Planning merely because another scope is still being elaborated.

---

# 4. Approved Decision 3 — Readiness for execution

An L2/L3 scope is ready for governed execution when the implementation can establish, as applicable:

- approved/effective Contract exact revision;
- exact governing Plan revision and valid Plan Review for the declared scope;
- exact/effective Product/System Baseline;
- dependencies/barriers sufficiently resolved for the scope;
- required Context Requirement is satisfiable and bounded governed context can be reconstructed;
- required Capability Operations resolve through valid Capability Bindings/Access Paths;
- applicable authority can be evaluated under L1-F;
- required technical prerequisites are available;
- Verification/Test Strategy and evidence expectations for the scope are defined;
- adaptation boundaries for the scope are known;
- no unresolved blocking condition prevents valid execution.

Provider workflow state such as `Ready`, `In Progress`, or `Done` does not itself establish AE readiness, completion, Validation, or acceptance.

Canonical Executable Task remains distinct from provider Work Item.

Do not duplicate provider-owned workflow properties unless AE has a semantic reason to own a different authoritative property.

---

# 5. Approved Decision 4 — Parallelism / execution topology

Canonical AE must support safe parallel work without requiring a canonical DAG engine, scheduler, queue, swarm, worker pool, branch strategy, or central orchestrator.

Define provider-neutral semantics for:

- dependencies;
- barriers;
- independent work branches;
- shared-resource conflicts;
- merge/reconciliation points;
- authority/capability differences by scope;
- context boundaries;
- evidence aggregation/reconciliation.

Independent valid scopes may execute concurrently.

A blocked branch does not automatically block unrelated valid work.

Shared dependencies or resource conflicts must prevent unsafe parallel continuation when required.

The canonical model should describe a work topology, not prescribe one orchestration technology.

---

# 6. Approved Decision 5 — Local adaptation versus Retry / Replan / Contract Change / Escalate

Use a semantic decision test rather than one numeric materiality threshold.

## Local adaptation

Execution may proceed under the same reviewed Plan when an implementation adjustment remains inside the reviewed Plan's explicit adaptation boundaries and does not materially alter the approved/reviewed engineering route.

Local adaptation must not materially change, as applicable:

- reviewed scope/outcome;
- Contract Goal/Spec/Proof;
- dependency/barrier semantics;
- architecture commitments/assumptions requiring new decision/review;
- authority/capability requirements;
- Verification/Test Strategy or evidence route;
- material risk/constraint assumptions;
- another declared Plan boundary.

Do not make the boundary so narrow that ordinary implementation detail causes needless Replan.

## Retry

Use Retry for execution failure where the reviewed Plan route remains valid and another execution attempt is appropriate within the same governing semantics.

Retry after failed Validation must preserve prior Validation history and follow L1-D route semantics.

## Replan

Replan is required when the reviewed engineering route materially changes while the approved Contract remains valid.

Replan creates a new Plan revision and requires applicable review for affected scope.

## Contract Change

If Goal, Spec, Proof, or another Contract-level semantic must change, route to Contract Change Proposal under existing G5/Human Decision Authority semantics.

Execution and Planning may propose Contract change; they may not silently mutate the Contract.

## Escalate

Use Escalate when a required risk/decision/authority/policy issue cannot be resolved within the actor's authority or current governed execution route.

Escalation blocks only the affected scope unless continuation of other scope is no longer meaningful/safe.

Approved summary:

> **implementation adjustment inside reviewed boundaries → local adaptation**
>
> **transient execution failure while route remains valid → Retry**
>
> **material reviewed-route change with Contract still valid → Replan**
>
> **Goal / Spec / Proof change → Contract Change**
>
> **unresolved authority/risk/decision issue → Escalate**

Preserve the L1-D invariant:

> **Execution may adapt within the reviewed Plan's authorized adaptation boundaries. It may not silently change the reviewed Plan or approved Contract.**

---

# 7. Approved Decision 6 — No new first-class execution entities by default

Do not introduce new A1/A2 types for convenience.

Concepts such as:

- Execution Attempt / Run;
- Execution Result;
- Work Decomposition / Execution Topology;
- Adaptation Record;
- Execution Coordination State;
- Verification Result;
- Worker Result;

should remain subordinate B semantics, provider-owned/resource references, Evidence relationships, transition/history semantics, or derived views unless a genuine independent identity/lifecycle requirement clearly passes DR-108.

If implementation review reveals that a new A1/A2 type is materially necessary for governance, traceability, continuation, authority, or Validation meaning across time, stop and surface that entity-admission decision to the Human Owner before silently adding it.

L4 micro-plan remains ephemeral by default.

Do not create durable micro-plan clutter merely because a worker generated one.

Material information discovered through L4 must be promoted to its proper durable semantic owner.

---

# 8. Approved Decision 7 — Machine-verifiable L1-H

L1-H should continue the staged executable pattern established in L1-D through L1-G.

Human semantic artifacts remain normative for meaning initially.

Introduce a cohesive machine-readable/reference layer, likely equivalent to:

- `planning_execution_protocol.json`
- `planning_execution_scenarios.json`
- `planning_execution_portability_fixtures.json`
- `validate_planning_execution.py`
- `.github/workflows/planning-execution-integrity.yml`

Naming may vary if a better cohesive choice exists.

The executable layer proves semantic behavior. It is not a production planner/orchestrator.

If `planning-execution-integrity` is introduced, update existing issue #12 to track it and keep issue #12 OPEN until repository rules actually require applicable checks and an intentional failing-check merge-block test proves enforcement.

Do not claim successful CI is merge-required while `main` remains unprotected.

---

# 9. Supporting rule — Verification / Evidence versus Validation

Preserve:

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

Intermediate verification may be part of Execution.

Execution success, test success, CI success, or executor-created Evidence does not create Validation acceptance.

Provider `Done` does not mean AE Accepted.

The doer must not become its own judge.

Evidence may remain physically/provider-owned when Evidence Records or references preserve the required provenance/relationships.

Parallel work must be reconcilable into a coherent Validation-ready evidence set.

---

# 10. Supporting rule — Architecture during Planning / Execution

Planning must identify affected architecture as already required by inherited decisions.

During Execution:

- ordinary architecture/model updates inside the reviewed route may be part of execution;
- a consequential architecture choice requiring an ADR must create/relate the ADR under inherited semantics;
- if architecture discovery materially changes the reviewed engineering route, route to Replan;
- if architecture discovery exposes a Contract deficiency, route to Contract Change Proposal;
- do not make every implementation/code change an ADR.

Do not silently mutate the durable Product/System Baseline underneath active work.

Baseline advancement should remain governed and tied to accepted/validated resulting state rather than becoming an untracked mid-execution mutation.

---

# 11. Supporting rule — Worker/subagent context and return semantics

L1-H consumes L1-G Context Requirement semantics.

A delegated worker/subagent receives bounded task-specific context rather than an accidental full transcript dump.

At minimum, worker context should make resolvable, as applicable:

- exact/effective Contract;
- exact reviewed Plan revision/scope;
- L2/L3 work scope;
- relevant Product/System Baseline/architecture neighborhood;
- dependencies/barriers;
- applicable authority/capability constraints;
- adaptation boundary;
- Verification/evidence expectations;
- relevant Handoff/continuation state.

A worker return should preserve/reference:

- result/outcome;
- evidence/provenance;
- blockers/failures;
- discovered dependency/resource conflict;
- material architecture issue;
- Plan-deficiency signal;
- Contract-deficiency signal;
- any material information requiring promotion to a durable owner.

Do not require a formal Handoff for every worker result.

Use Handoff when meaningful continuation/responsibility transfer requires it under L1-G.

Fresh workers are allowed but not universally required.

Continuing workers are allowed as long as material engineering state does not exist only in hidden session memory.

---

# 12. Supporting rule — Human collaboration versus clerical middleware

Preserve Human thinking partnership.

Human participation may legitimately include:

- engineering judgment;
- reasoning about alternatives;
- Human-reserved DA;
- organization-reserved approval;
- contextual expertise;
- risk/tradeoff judgment.

Do not create new universal Human gates merely because a Planning/Execution decision looks consequential unless higher canonical authority already reserves that decision to Humans.

A Human required only to translate/copy an already-known agent intent between systems is mechanical middleware and should be treated as a capability/access-path deficiency where the relevant canonical operation is required to be agent-operable.

Preserve:

> **Human judgment is a feature. Human transcription is usually a defect.**

---

# 13. Planning / Execution source-of-truth federation

Preserve DR-107 and prior domain boundaries.

Examples:

- exact Plan revision may be authoritative in source control or another declared provider;
- Work Management may own selected provider workflow properties;
- CI/runtime may own run state/results;
- Evidence Records may reference provider evidence rather than duplicating bytes;
- AE lifecycle semantics remain canonical AE truth rather than provider status;
- Context Package remains derived;
- an orchestrator queue/session/in-memory graph cannot become the only source of material Planning/Execution state.

A conforming implementation must be able to reconstruct material Planning/Execution state after orchestrator/session loss.

The system owns durable state; orchestration may project/use it.

---

# 14. Portability proof

Prove equivalent canonical Planning/Execution semantics across at least two materially different synthetic implementations.

A useful shape is:

## Implementation A

- source-controlled Plan;
- Jira/Plane-like Work Management;
- CI jobs;
- multiple stateless/fresh workers;
- provider-native source-control branch workflow.

## Implementation B

- workflow/issue-provider Plan representation;
- different Work Management provider;
- long-lived agent/runtime;
- direct tool/API execution;
- materially different orchestration/topology.

Equivalent conformance should preserve:

- exact Contract/Plan/Baseline control;
- reviewed-scope semantics;
- dependency/barrier/parallelism meaning;
- authority/capability constraints;
- same adaptation-versus-Replan-versus-Contract-Change decision for equivalent facts;
- same blockers/dispositions;
- same evidence/Validation readiness;
- same detection of material Plan/Contract deviation;
- recoverability after orchestration/session loss.

Do not require identical:

- task counts;
- worker counts;
- unconstrained execution order;
- branch strategy;
- provider workflow statuses;
- orchestration technology.

---

# 15. Machine integrity scenarios

At minimum mechanically test equivalent semantics for:

1. unapproved Contract cannot produce executable reviewed work;
2. Plan references exact Contract + Product/System Baseline;
3. affected architecture is identified where applicable;
4. reviewed scope A may execute while scope B remains under Planning;
5. changed scope cannot silently inherit stale Plan Review;
6. unaffected scope can continue under prior reviewed Plan revision when later revision only affects future scope and dependency-impact analysis shows no effect;
7. dependency change affecting executing scope triggers reassessment/Replan rather than silent continuation;
8. future detail inside reviewed elaboration envelope can be elaborated without needless Plan revision;
9. detail outside the reviewed envelope requires new Plan revision/review;
10. local adaptation inside declared boundary succeeds without Replan;
11. material Plan deviation routes to Replan;
12. Goal/Spec/Proof deviation routes to Contract Change Proposal rather than Plan mutation;
13. worker cannot silently alter Contract or reviewed Plan;
14. L4 micro-plan can disappear without losing material state;
15. missing required capability/authority/context blocks rather than creating Human mechanical proxy;
16. provider task status does not establish AE Validation acceptance;
17. executor-created evidence cannot self-create Validation acceptance;
18. parallel independent branches may proceed concurrently;
19. blocked branch does not automatically freeze unrelated valid work;
20. shared dependency/barrier prevents unsafe parallel execution;
21. worker result promotes material Plan/architecture/Contract issue instead of hiding it;
22. Verification/Test Strategy remains traceable to Contract Proof;
23. Evidence from parallel branches can be reconciled for Validation;
24. orchestrator/session loss cannot destroy the only material Planning/Execution state;
25. two materially different Planning/Execution architectures preserve equivalent governed outcomes;
26. no central orchestrator/planner/workflow technology is required;
27. latest Plan/Contract revision is not selected merely because it is newest when another exact revision remains effective for scope;
28. Human collaboration can occur without converting Human participation into mandatory clerical middleware.

Cross-check existing lifecycle, capability, authority, and context machine definitions rather than restating local substitutes where practical.

---

# 16. Issue #6

Keep issue #6 OPEN.

L1-H may add semantics for:

- discovering current Plan/work topology;
- invoking Planning/Execution operations through Access Paths;
- obtaining context/authority/capabilities/evidence relationships;
- worker/parent coordination semantics.

Do not solve the complete developer experience or mandate Portal/CLI/IDE/Dev Container/agent host/runtime.

Preserve:

> **AE should require interface parity, not environment uniformity.**

---

# 17. Independent review requirements

Before merge, independently challenge L1-H against at least:

- Plan becoming a giant workflow form;
- accidental serialization of rolling-wave work;
- stale review inheritance;
- provider Work Management becoming canonical truth;
- hidden central scheduler/orchestrator dependency;
- hidden worker session state becoming durable truth;
- executor silently changing Plan/Contract;
- adaptation boundaries too narrow or too permissive;
- architecture-impacting change bypassing ADR/Plan review;
- unsafe races on shared dependencies/resources;
- blocked work freezing unrelated valid scope;
- technical capability being mistaken for OA;
- Human clerical middleware hiding capability/access gaps;
- Verification/Evidence becoming self-Validation;
- Plan lacking a credible route from Contract Proof to Verification/Evidence;
- L4 micro-plans becoming durable clutter/shadow Plans;
- Context Package becoming Plan/execution authority;
- newest revision being selected instead of effective revision;
- orchestrator crash destroying material state;
- portability requiring identical topology rather than equivalent semantics;
- new A1/A2 entities being added for implementation convenience rather than domain necessity.

If a genuine Contract contradiction or new A1/A2 need emerges, surface it explicitly rather than resolving it silently.

---

# 18. Expected durable L1-H package

Use the smallest useful artifact set. Do not freeze filenames solely because they appeared in prior brainstorming.

Expect semantics equivalent to:

1. Canonical Plan semantic model;
2. Planning Depth / Planning Method + progressive-elaboration model;
3. L2/L3 decomposition / dependency / parallelism model;
4. Execution coordination model;
5. Adaptation / Retry / Replan / Contract Change / Escalation decision model;
6. Verification / Evidence during Execution model;
7. Architecture / ADR / Baseline interaction model;
8. Worker/subagent context-result model;
9. Planning/Execution state federation / recovery model;
10. relationship views;
11. machine-readable Planning/Execution protocol;
12. scenarios / portability fixtures;
13. validator;
14. `planning-execution-integrity` workflow;
15. minimum necessary DRs/ADR.

Do not create a giant orchestration subsystem simply to fill the artifact list.

---

# 19. Implementation authorization

Proceed with the normal implementation loop:

```text
branch
→ semantic artifacts
→ machine representation / scenarios / portability fixtures
→ validator
→ planning-execution-integrity CI
→ minimum DRs / ADR
→ update issue #12 if applicable
→ keep issue #6 open
→ independent review
→ correct material findings
→ PR
→ verify all applicable CI on exact PR head
→ merge
→ new relay handoff
```

Do not introduce Kestrel.

Do not canonize a planner, orchestrator, workflow/DAG engine, branch strategy, Work Management provider workflow, CI/CD topology, model/provider, worker count, or one Planning Method.

Do not solve standards applicability or the full developer-experience problem here.

---

# 20. Closure / next handoff

After L1-H implementation and independent verification are complete, write the full next handoff to a new unique file under `handoffs/` on `ae-session-relay`.

The closure handoff must include:

- final Plan semantics;
- rolling-wave/elaboration-envelope semantics;
- readiness semantics;
- parallelism/dependency/barrier semantics;
- local adaptation versus Retry/Replan/Contract Change/Escalate rules;
- entity-admission decisions;
- Verification/Evidence versus Validation treatment;
- architecture/ADR/Baseline handling;
- worker/subagent context/result handling;
- Human collaboration/mechanical-intermediary boundary;
- source-of-truth/recovery model;
- machine/reference artifacts;
- integrity/portability results;
- independent-review findings/dispositions;
- issue #12 status;
- issue #6 status;
- PR/head/merge commit;
- next L1 domain and next genuine Human Owner decision gate.

Do not overwrite prior relay handoffs.

Do not merge `ae-session-relay` into `main`.