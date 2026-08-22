# Handoff: L1-G Closure and L1-H Planning / Execution Coordination Design Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` when creating the next relay handoff.

---

# 1. Current authoritative repository state

L1-G — Knowledge / Context / Memory is complete, independently reviewed, machine-validated, and merged to `main`.

## Merge record

- PR: **#15 — Establish L1-G knowledge, context, and memory baseline**
- PR head reviewed/tested: **`fc0311666005f2c69c8b3271679fc690e8f57b30`**
- Merge commit on `main`: **`0dc7216eb091498c69d7935ae04d7f096ce4a3ad`**
- Merge completed: 2026-08-22

All four applicable PR integrity jobs passed on the exact PR head before merge:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`
- `context-integrity`

`context-integrity` passed **56 semantic scenarios + 4 retrieval-portability cases**.

Repository protection remains a known governance gap:

- `main` remains unprotected;
- the integrity jobs run and passed, but are not repository-enforced merge requirements;
- issue #12 remains OPEN and tracks required-check enforcement.

Issue #6 remains OPEN. L1-G added semantic bootstrap/reconstruction hooks but did not solve the complete engineering-team working-environment experience.

No Kestrel material was introduced.

---

# 2. L1-G durable artifacts now on `main`

## Human semantic artifacts

- `L1-G_CANONICAL_KNOWLEDGE_CONTEXT_MEMORY_MODEL.md`
- `L1-G_CONTEXT_REQUIREMENT_PACKAGE_MODEL.md`
- `L1-G_CONTEXT_ASSEMBLY_PROVENANCE_MODEL.md`
- `L1-G_HANDOFF_CONTINUATION_RECONSTRUCTION_MODEL.md`
- `L1-G_CONTEXT_BOOTSTRAP_DISCOVERY_PROTOCOL.md`
- `L1-G_BOUNDED_SELECTION_CURRENTNESS_SOURCE_MODEL.md`
- `L1-G_KNOWLEDGE_WRITE_PROMOTION_SECURITY_MODEL.md`
- `L1-G_CONTEXT_RELATIONSHIP_VIEWS.md`

## Decisions

- `DR-121-system-owned-memory-context-requirements-and-reconstruction.md`
- `DR-122-context-provenance-handoff-currentness-source-authority-and-security.md`
- `DR-123-bootstrap-anchor-first-context-and-retrieval-portability.md`
- `ADR-005-machine-readable-context-and-integrity.md`

## Machine-readable / executable reference artifacts

- `context_protocol.json`
- `context_scenarios.json`
- `context_portability_fixtures.json`
- `validate_context.py`
- `.github/workflows/context-integrity.yml`

---

# 3. L1-G canonical baseline inherited by later domains

The following semantics are now fixed inputs unless explicitly superseded by higher authority.

## Memory is a system property, not a store

> **Canonical AE treats memory as a system property, not a central memory database.**

The system remembers because durable state has authoritative owners, durable references survive sessions, retrieval reconstructs governed information, Handoff preserves continuation where needed, and material discoveries are promoted into the correct semantic owner.

Do not introduce a generic canonical Memory Store, Memory Record, Knowledge Item, vector database, RAG architecture, agent-memory framework, or conversation-history source of truth.

## R2 versus R3

- **R2 — Durable Engineering State, Identity & Traceability** owns authoritative durable engineering state semantics.
- **R3 — Context & Knowledge Coordination** discovers, retrieves, assembles, bounds, reconstructs, and hands off context without becoming a competing owner of canonical truth.

R3 retrieval cannot turn an index/cache/vector/summarization layer into authoritative state.

## Context Requirement [B]

A subordinate Context Requirement defines what information must be resolvable for an actor/action/task before governed work can proceed correctly.

It may declare:

- purpose/action;
- required governing anchors;
- required source/authority quality;
- exact-revision/effectivity requirements;
- freshness/currentness requirements;
- security/access requirements;
- supporting context categories;
- failure disposition;
- assembly bounds.

It is not A1/A2.

## Context Package [D]

Context Package remains derived, disposable, bounded, and reconstructable.

It is not authoritative truth and does not become a shadow Contract, Plan, Architecture Model, Evidence store, Decision Register, policy store, or provider source of truth.

Exactness may be preserved through resolvable references rather than copying every authoritative byte into model context.

## Context Assembly Receipt / Source Manifest [B]

Subordinate provenance structure retained when consequential-use/policy requires it.

No Context Provenance A2 was created.

Routine low-risk context assembly does not require permanent prompt/provenance logging.

## Handoff Record [A2]

Existing Handoff Record remains the durable continuation record.

It is authoritative for what was handed off at issuance, not for the current state of the referenced Contract/Plan/OEB/architecture/policy/etc.

Receivers resolve authoritative references and detect later change.

Handoff is conditional, not required for every model/worker invocation.

## Replacement-actor invariant

> **Loss of actor/session-local context must not prevent an appropriately authorized replacement actor from reconstructing the material governed state necessary to continue the work.**

Material engineering state may not exist only in private conversation/session memory.

Continuing agents are allowed. Fresh agents are not mandatory at every phase.

## Bootstrap / Discovery

A Human/agent entering through a supported Access Path must be able to deterministically discover the applicable AE implementation, Canonical release, OEB/Profile revisions, actor/authority context, work scope, Loop/Increment/Task, governing artifacts/state, Capability Bindings/Access Paths, Handoff state, and Context Requirement before assembling bounded context.

No Portal/CLI/IDE/Dev Container/daemon/agent host/bootstrap filename is canonical.

## Anchor-first context assembly

> **Anchor-first, relevance-expanding context assembly.**

Required governing anchors come before work/dependencies, architecture neighborhood, material decisions/evidence/Handoff, and supporting knowledge.

Mandatory anchors cannot lose a relevance/popularity contest to semantically similar retrieved text.

No token count, top-k, embedding model, chunk size, reranker, or context-window size is canonical.

## Currentness/effectivity

> **Correct/effective revision beats newest revision.**

Currentness is requirement-relative:

- `EXACT_REVISION`
- `EFFECTIVE_FOR_SCOPE`
- `CURRENT_AT_USE`
- `BEST_AVAILABLE_SUPPORTING`

A newer revision does not invalidate an intentionally required historical exact revision.

Contract revision effectivity remains compatible with L1-D rolling-wave semantics.

Old Context Packages are not mutated to claim currentness; context is reassembled/reconstructed.

## Source authority/conflict

Reuse DR-107 federated authoritative state.

A derived index/cache/summary cannot become authoritative merely because it is accessible.

Unresolved competing authoritative claims cannot be silently ranked into truth.

For protected use, unresolved required authority/currentness conflict blocks.

## Knowledge write / semantic promotion

`knowledge.write` persists information through a Knowledge capability. It does **not** make the information canonical truth.

Material discoveries become canonical only through semantic-owner promotion into the correct owner, such as Contract Change Proposal, Plan revision, Architecture Model, Decision/ADR, Evidence, Learning, Authority, Work state, etc., subject to their own authority/revision/immutability semantics.

## Compaction

> **Compaction ≠ canonical state.**

Before intentional compaction/discard of system-managed actor context, material state that would otherwise be lost must already be promoted to its durable semantic owner or appropriate Handoff/continuation state.

## Context security

A derived Context Package cannot reveal information beyond what the actor is authorized to access unless an explicitly authorized/proven transformation permits it.

Stale Context Package authority cannot continue to authorize protected retrieval/actions after revocation.

## Context and Validation

Context Package is not Evidence merely because a Validator used it.

Consequential judgments may retain a Context Assembly Receipt when assembled context materially influenced the judgment and direct canonical references alone cannot reconstruct the basis.

## Retrieval portability

Two materially different retrieval architectures can conform if they reconstruct equivalent required governed context and blockers/dispositions. Supporting/background text may differ.

The reference proof compared:

- direct structured canonical sources + keyword/search index;
- external canonical sources + knowledge service + vector/RAG retrieval.

---

# 4. L1-G independent verification completed by receiving session

The receiving session independently verified after the Human Owner supplied the L1-G implementation handoff:

- `main` is at merge commit `0dc7216eb091498c69d7935ae04d7f096ce4a3ad`;
- PR #15 is merged;
- exact PR head is `fc0311666005f2c69c8b3271679fc690e8f57b30`;
- all four applicable integrity jobs passed on that exact head;
- `context-integrity` passed 56 semantic scenarios + 4 portability cases;
- the executable suite explicitly covers the required Human Owner failure classes, including derived-state authority, exact/effective revisions, stale-summary/vector rejection, authority conflict, access leakage, fresh/replacement actor reconstruction, Handoff freshness, compaction survivability, knowledge-write promotion, conditional provenance, heterogeneous bootstrap, revoked access, provider shadow truth, and authoritative-source outage;
- issue #6 remains OPEN;
- issue #12 remains OPEN and now tracks all four integrity jobs;
- `main` remains unprotected, so checks are operational but not merge-required.

No corrective L1-G follow-up was required by this verification.

---

# 5. Next L1 domain

The next genuine L1 domain is:

> **L1-H — Planning & Execution Coordination**

This is not a restart of the earlier Planning discussion. L1-C through L1-G have already fixed the nouns, identities, lifecycle states, authority model, capability semantics, and context/reconstruction behavior.

L1-H must now define the minimum portable protocol that turns governed intent into executable engineering work and manages bounded adaptation during execution.

Do **not** implement L1-H in the first receiving response.

The next session should perform dialectic design, surface the genuine Human Owner decisions, and stop before GitHub writes unless the Human Owner approves the L1-H decision set.

---

# 6. Primary L1-H Human Owner decision gate

> **What is the minimum canonical Planning and Execution Coordination protocol that transforms an approved Contract plus Product/System Baseline and governed context into an architecture-aware, reviewable, scope-aware Plan; decomposes that Plan into parallelizable L2/L3 work; gives authorized agents freedom to execute within explicit adaptation boundaries; and deterministically routes material deviation to Retry, Replan, Contract Change, or Escalation—without making one planner, orchestrator, agent framework, workflow engine, branch strategy, or task technology part of what Agentic Engineering fundamentally means?**

This is the central L1-H design question.

---

# 7. Fixed inherited Planning decisions that L1-H must preserve

The inherited Decision Register already establishes important Planning semantics. Verify the exact records on `main`/the historical Decision Register before designing, but preserve at least these adopted meanings:

## Architecture-aware Planning — DR-020

Every Plan references canonical architecture and identifies affected architecture elements/relationships.

Architecture is an active Planning input, not passive documentation.

## C4 architecture decision — DR-021

C4 remains an adopted visual architecture choice below Contract authority, not an immutable Contract semantic. L1-H must not make one architecture notation part of Planning semantics.

## ADR requirement — DR-022

Significant architecture decisions become ADRs containing context, alternatives, rationale, tradeoffs, consequences, and affected architecture.

## L2/L3 Planning decomposition — DR-023

Planning creates executable L2/L3 boundaries, dependencies/parallelism, topology/context/verification semantics.

## Contract above Planning depth — DR-024

Contract sits above Planning depth. Planning does not rewrite Goal/Spec/Proof.

## L1 durable baseline — DR-025

L1 is the durable Product/System Baseline against which normal Loops plan.

## Ongoing Loop use of L1/L2/L3 — DR-026

Normal Loops derive L2/L3 against persistent L1; architecture-impacting L1 changes use the adopted architecture-decision mechanism.

## L4 micro-plan — DR-027

L4 is agent-local/ephemeral by default. Material information discovered through L4 must be promoted to the durable owner; do not persist micro-plans merely because they existed.

## Planning Depth — DR-028

Planning Depth is mandatory Planning semantics.

## Planning Method — DR-029

Planning Method is mandatory Planning semantics, but the canonical system must not freeze one universal method.

## Plan dual-format — DR-033

One Plan may have Human-readable, machine-readable, interactive/IG, or other conforming representations. Representation is not a second Plan entity.

## Plan Review — DR-034 plus L1-D

Plan Review applies to an **exact Plan revision + declared execution scope**.

Rolling-wave Planning is valid. One scope may execute under a reviewed Plan revision while another scope is still being planned under another revision, provided the exact scope/revision relationship remains deterministic.

No changed scope inherits prior review silently.

---

# 8. Fixed L1-C domain semantics L1-H must use

Existing first-class domain objects include:

- Contract [A1]
- Plan [A1]
- Product/System Baseline — L1 [A1]
- Execution Increment — L2 [A1]
- Executable Task — L3 [A1]
- Architecture Model [A1]
- Contract Change Proposal [A1]
- Decision/ADR [A2]
- Plan Review Record [A2]
- Evidence Record [A2]
- Validation Record [A2]

L4 micro-plan remains ephemeral [E].

Planning Depth, Planning Method, Verification/Test Strategy, and architecture element/relationship references are subordinate semantics [B].

Do not invent new A1/A2 execution/planning objects unless a new identity/lifecycle need clearly passes the L1-C admission test.

A particular concept being useful in an orchestrator does not make it a canonical entity.

---

# 9. Fixed L1-D lifecycle semantics L1-H must use

AE uses a composite/scoped lifecycle protocol, not one global phase field.

## Loop control

- OPEN
- SUSPENDED
- CLOSED

with terminal disposition:

- ACCEPTED
- CANCELLED
- SUPERSEDED

## L2 active positions

- PLANNING
- READY
- EXECUTING
- VALIDATING

with terminal dispositions orthogonal to active position.

## L3 portable execution state

- NOT_STARTED
- ACTIVE
- COMPLETE

Provider workflow remains provider-owned and may be richer.

## Gates

- G1 Contract Approval
- G2 Plan Review
- G3 Authority
- G4 Validation Acceptance
- G5 Contract Change

## Backward routes

- Retry Execution
- Replan
- Propose Contract Change
- Escalate

These are routes/dispositions, not phases.

## Adaptation boundary already fixed at high level

Execution may adapt within the reviewed Plan's authorized adaptation boundaries.

It may not silently change the reviewed Plan or approved Contract.

L1-H must make that distinction operationally precise enough for an implementation to behave consistently without becoming a giant rules engine.

---

# 10. Fixed L1-E capability semantics L1-H must use

Planning/Execution must work backwards through Canonical Capability Operations and scope-aware Capability Bindings.

Capability Binding readiness remains separate from current runtime authorization.

L1-H should consume, not redefine:

- Source Control operations;
- CI/CD operations;
- Models;
- Runtime/Execution;
- Identity & Access;
- Governed Tool Access;
- Observability;
- Knowledge/Memory;
- Work Management;
- Validation.

Work Management remains direct governed agent-operable for required operations.

Canonical Executable Task remains distinct from provider Work Item.

Provider workflow fields do not become canonical Planning/Execution truth merely because the provider exposes them.

---

# 11. Fixed L1-F authority semantics L1-H must use

Planning and Execution actions are governed through the L1-F protocol:

- entitlement ≠ OA ≠ DA;
- protected operations use authoritative identity/authority/policy facts;
- `PERMIT / DENY / INDETERMINATE` remain distinct from runtime `ALLOWED / DENIED / BLOCKED`;
- INDETERMINATE is never permission for protected operations;
- required conditions/obligations must reach enforcement;
- authority-changing actions use pre-change authority;
- distributed PEPs are valid;
- bypass-path Proof is scoped to identities/access paths available to the governed actor/runtime;
- Canonical Human-reserved authority is limited to what Contract/higher decisions actually establish.

L1-H must not quietly create new universal Human approval gates merely because a Planning/Execution choice sounds important.

If an organization wants additional Human gates, use organization-reserved DA/policy semantics.

---

# 12. Fixed L1-G context semantics L1-H must use

Planning/Execution must declare/consume Context Requirements rather than assume an agent's session contains the right information.

For Planning/Execution scopes, Context Requirements can include, as applicable:

- exact/effective Contract revision;
- Product/System Baseline;
- Architecture Model/neighborhood;
- reviewed Plan revision/scope;
- current work/dependencies;
- authority/policy state;
- Capability Bindings/Access Paths;
- Handoff/continuation state;
- Evidence/Validation state;
- current operational facts.

Correct/effective revision beats newest revision.

A Context Package remains derived and cannot become a hidden Plan or execution state store.

---

# 13. Core L1-H design areas to resolve

The receiving session should analyze these as one coherent protocol and identify the smallest set of genuine Human Owner decisions.

## A. Canonical Plan semantic minimum

What must every conforming Plan revision say, independent of format/tool?

Candidate required semantics to test—not automatically approve—include:

- exact Contract revision;
- exact Product/System Baseline revision;
- Plan scope;
- intended outcome/route to Contract Proof;
- affected Architecture elements/relationships;
- decomposition into L2/L3 or rules for progressive elaboration;
- dependencies and sequencing constraints;
- parallelizable work/topology;
- Planning Depth;
- Planning Method;
- Context Requirements;
- required Capability Operations/Bindings;
- authority/approval requirements inherited from policy;
- Verification/Test Strategy derived from Contract Proof;
- evidence-production expectations;
- Validation preparation/handoff expectations;
- risks/constraints/assumptions as applicable;
- permitted adaptation boundaries;
- explicit items deferred to later Planning depth.

Do not turn this into a mandatory 40-field form if some semantics are conditionally applicable or represented through typed relationships.

## B. Progressive elaboration / rolling-wave Planning

Define when a Plan may be partially elaborated while some scopes execute.

Questions:

- What is the minimum planning completeness required before one L2 scope can become READY?
- Can a parent Plan revision contain reviewed scope A while scope B remains under elaboration?
- When later elaboration changes only future/unaffected scope, what prior review remains valid?
- How are dependency changes detected when already-executing scope may be affected?
- Is a new Plan revision always required for elaborating previously unspecified future detail, or can subordinate work objects be added within previously reviewed boundaries?

Preserve exact-revision + scope-aware Plan Review.

## C. Decomposition semantics

Define the canonical relationship among:

- Plan;
- L2 Execution Increment;
- L3 Executable Task;
- provider work items.

The Plan should create a credible executable topology, not merely a narrative.

But avoid making every provider task field canonical.

Questions:

- What minimum semantics make an L2/L3 decomposition executable and traceable?
- How are dependencies represented canonically versus provider-native?
- How is parallelism represented without requiring one DAG/orchestration technology?
- What makes a task “ready enough” for authorized execution?
- What task state remains provider-owned versus AE-owned?

## D. Planning topology / parallelism

Canonical AE should support multi-agent parallel work where safe/useful.

Design semantics for:

- independent branches of work;
- dependencies/barriers;
- shared-resource conflicts;
- merge/reconciliation points;
- context boundaries;
- authority/capability differences among work scopes;
- evidence aggregation.

Do not canonize one scheduler, DAG engine, swarm framework, queue, worker pool, branch strategy, or number of agents.

## E. Execution coordination

Define what “bounded Execution” requires beyond L1-D lifecycle state.

Candidate semantics to test:

- exact governing Contract/Plan/Baseline scope;
- actor/identity/authority context;
- executable task/increment scope;
- Context Requirement;
- required Capability Bindings;
- permitted adaptation boundary;
- evidence/provenance capture expectation;
- resource/runtime limits where organization policy requires;
- outcome/result relationships;
- blockers/failures surfaced rather than hidden.

Do not make one Execution Controller or central orchestrator canonical.

## F. Local adaptation versus Plan revision

This is likely one of the most important L1-H decisions.

Current invariant:

> Execution may adapt within the reviewed Plan's authorized adaptation boundaries. Material Plan change routes to Replan. Goal/Spec/Proof change routes to Contract Change Proposal.

L1-H should define a portable decision test for:

### Local adaptation

May proceed under the existing reviewed Plan when the change does not materially alter the reviewed route/scope/architecture/authority/Proof assumptions or other declared boundary.

### Plan change / Replan

Required when the reviewed route materially changes but Contract remains valid.

### Contract change

Required when Goal/Spec/Proof must change.

Avoid pretending there is one universal numeric materiality threshold.

Prefer semantic tests tied to approved Plan boundaries and organization policy.

## G. Execution deviation / failure routing

Distinguish at least conceptually:

- expected local retry within Plan boundary;
- Retry Execution after failed Validation;
- blocked capability/authority/context prerequisite;
- execution-discovered Plan deficiency → Replan;
- Contract deficiency → Contract Change Proposal;
- unresolved risk/decision/authority issue → Escalate.

Do not create twenty lifecycle states.

## H. Verification/evidence during Execution

Contract Proof defines what evidence must ultimately exist.

Plan owns Verification/Test Strategy for how evidence will be produced/checked.

Execution must produce/reference Evidence without letting the executor self-accept the outcome.

Questions:

- What minimum execution evidence/provenance is canonical?
- What evidence can remain provider-owned with Evidence Record references?
- When is intermediate Verification a local execution activity versus independent Validation?
- How should parallel branches aggregate evidence before Validation?
- What makes an apparent execution success insufficient to proceed?

Preserve:

> **The doer shall not become its own judge.**

## I. Plan/Execution relationship to architecture changes

Planning must identify affected architecture.

During Execution:

- architecture understanding may improve;
- an architectural decision may become necessary;
- actual architecture may diverge from assumed state.

Define routing without making every code edit an ADR.

Questions:

- When is architecture update simply part of executing the reviewed Plan?
- When does a consequential architecture choice require ADR?
- When does architecture impact invalidate/review the Plan?
- How is the Product/System Baseline updated after accepted work versus mutated mid-execution?

## J. Context boundaries for workers/subagents

L1-G means workers receive Context Requirements and bounded context, not an accidental transcript dump.

Questions:

- What minimum context must a delegated L3 worker receive?
- What material result/provenance must return?
- When is a worker return enough versus a formal Handoff?
- How does parent coordination detect that a worker discovered a Plan/Contract/architecture issue?

Do not require fresh workers universally.

## K. Human interaction during Planning/Execution

Preserve Human thinking partnership without turning Planning into form filling.

Distinguish:

- Human reserved DA;
- organization-reserved approvals;
- Human engineering collaboration;
- Human mechanical intermediary anti-pattern.

A Human helping reason about a Plan is valid.

A Human being required only to copy agent-created tasks into Jira is a capability failure.

## L. Planning/Execution portability Proof

Plan to prove equivalent semantics across at least two materially different execution topologies, for example:

### Implementation A

```text
source-controlled Plan
+ Jira/Plane Work Management
+ CI jobs
+ several stateless/fresh workers
+ provider-native branch workflow
```

### Implementation B

```text
workflow/issue provider Plan representation
+ different Work Management
+ long-lived agent/runtime
+ direct tool/API execution
+ materially different provider orchestration
```

Equivalent conformance should preserve:

- same Contract/Plan/Baseline control;
- same reviewed scopes;
- same dependency/parallelism semantics;
- same authority constraints;
- same adaptation-versus-Replan decisions for equivalent facts;
- same evidence/Validation readiness;
- same detection of material Plan/Contract deviation.

Do not require identical task counts, worker counts, execution order where unconstrained, provider statuses, or orchestration technology.

---

# 14. Potential domain/entity questions

Do not automatically add any of these. Apply DR-108's identity admission test.

Potential concepts that may appear during design:

- Execution Attempt / Run;
- Execution Result;
- Work Decomposition / Execution Topology;
- Adaptation Record;
- Execution Coordination State;
- Verification Result;
- Worker Result.

Leading caution:

Most may be better represented as subordinate B semantics, provider references, Evidence Records, or relationships rather than new A1/A2 entities.

A concept should become first-class only if independent identity/lifecycle materially protects governance, traceability, continuation, authority, or Validation meaning across time.

If a genuinely new A1/A2 need emerges, surface it explicitly to the Human Owner before implementation.

---

# 15. Planning/Execution source-of-truth boundary

L1-H must preserve federated state and avoid shadow orchestration.

Examples:

- Plan exact revision may be canonically authoritative in source control or another declared system;
- provider Work Management may remain authoritative for selected provider workflow fields;
- CI/runtime may remain authoritative for run state/results;
- Evidence Records reference provider evidence rather than copying every byte;
- AE lifecycle state remains canonical AE semantics rather than provider status;
- Context Packages remain derived;
- an orchestrator's in-memory queue cannot become the only source of material engineering state.

A conforming implementation must be able to reconstruct required Planning/Execution state after orchestrator/session loss.

---

# 16. Candidate machine-verifiable L1-H layer

After Human Owner semantic approval, L1-H will likely be the next machine-testable domain.

Do not implement this yet during the design response.

A plausible staged representation might include:

- `planning_execution_protocol.json`
- `planning_execution_scenarios.json`
- `planning_execution_portability_fixtures.json`
- `validate_planning_execution.py`
- `.github/workflows/planning-execution-integrity.yml`

or another cohesive naming choice.

Human semantic artifacts should remain normative for meaning initially, following ADR-002/003/004/005.

The executable representation should prove semantics, not become a production planner/orchestrator.

Potential executable tests after approval should include at least:

1. unapproved Contract cannot produce executable reviewed work;
2. Plan references exact Contract + Baseline;
3. Plan identifies affected architecture where applicable;
4. reviewed scope A can execute while scope B remains under Planning;
5. changed scope cannot silently inherit stale Plan Review;
6. unaffected scope can continue when later Plan revision affects only future scope and dependency analysis confirms no impact;
7. dependency change that affects executing scope triggers reassessment/Replan rather than silent continuation;
8. local adaptation within declared boundary succeeds without unnecessary Plan revision;
9. material Plan deviation triggers Replan;
10. Goal/Spec/Proof deviation triggers Contract Change Proposal rather than Plan mutation;
11. worker cannot alter Contract silently;
12. L4 micro-plan can disappear without losing material state;
13. missing required capability/authority/context blocks rather than creating a Human mechanical proxy;
14. provider task status does not establish AE Validation acceptance;
15. executor-generated evidence cannot self-create Validation acceptance;
16. parallel independent branches can proceed concurrently;
17. blocked branch does not necessarily stop unrelated valid work;
18. shared dependency/barrier prevents unsafe parallel work;
19. worker result promotes material Plan/architecture/Contract issue rather than hiding it;
20. Plan Verification Strategy remains traceable to Contract Proof;
21. Evidence from parallel work can be reconciled for Validation;
22. provider/orchestrator loss does not destroy the only copy of material planning/execution state;
23. two materially different execution architectures preserve equivalent governed outcomes;
24. no central orchestrator/planner technology is required.

Cross-check the existing lifecycle, capability, authority, and context machine definitions where useful.

---

# 17. Repository-governance implication

If a new Planning/Execution integrity job is eventually implemented, update **existing issue #12** rather than creating another repository-governance issue for the same concern.

Keep issue #12 OPEN until repository rules actually require the applicable jobs and a deliberate failing-check merge-block test proves enforcement.

Do not claim successful CI is repository-enforced before then.

---

# 18. Issue #6 interaction

Keep issue #6 OPEN during L1-H unless the Human Owner explicitly changes scope.

L1-H may clarify semantic needs from the working environment, such as:

- how a practitioner/agent sees the current Plan/work topology;
- how Planning/Execution actions are invoked through Access Paths;
- how context, authority, capability, work, and evidence become available.

But do not solve the complete developer experience or mandate one Portal/CLI/IDE/Dev Container/runtime.

Preserve:

> **AE should require interface parity, not environment uniformity.**

---

# 19. Independent review requirements for the L1-H design response

Before asking for Human Owner approval, challenge the proposed L1-H design against at least:

1. Does Plan become a giant workflow form instead of a semantic engineering route?
2. Does the model accidentally serialize all rolling-wave work?
3. Can future Plan elaboration silently invalidate or inherit review for already-executing scopes?
4. Can provider Work Management become canonical AE truth?
5. Can a scheduler/orchestrator become required Canonical AE architecture?
6. Can a worker's hidden session state become the only place material work knowledge exists?
7. Can an executor silently alter Plan or Contract?
8. Is local adaptation so narrow that every implementation detail causes Replan?
9. Is local adaptation so broad that material Plan changes bypass review?
10. Can architecture-impacting work occur without required architecture/ADR handling?
11. Can parallel work race on shared dependencies/resources without explicit coordination semantics?
12. Can blocked work unnecessarily freeze unrelated valid scope?
13. Can an agent act with technical capability but without OA?
14. Can Human mechanical mediation hide a missing capability?
15. Can Evidence/Verification become self-Validation?
16. Can a Plan claim Proof without a credible Verification/evidence route?
17. Can L4 micro-plans become durable clutter or shadow Plans?
18. Can Context Package become the actual Plan/execution state store?
19. Can a newer Plan/Contract revision be selected merely because it is latest rather than effective for the scope?
20. Can an orchestrator crash destroy the only copy of task/dependency/adaptation state?
21. Can two materially different planning/execution implementations conform without identical orchestration?
22. Are new A1/A2 entities being added only because they are convenient implementation records?
23. Does the design preserve Human thinking partnership without making Humans clerical middleware?
24. Does the design remain technology-neutral enough to hand to a fresh implementation team?

Surface any genuine Contract contradiction instead of resolving it silently.

---

# 20. Expected L1-H design response

The next session should provide a **design proposal only**, not repository implementation.

At minimum include:

1. proposed canonical Plan minimum semantics;
2. Planning Depth / Planning Method treatment;
3. progressive elaboration / rolling-wave rules;
4. L2/L3 decomposition and dependency/parallelism semantics;
5. bounded Execution coordination semantics;
6. local adaptation versus Replan versus Contract Change decision test;
7. execution failure/deviation routing;
8. Verification/evidence relationship during Execution;
9. architecture-change/ADR interaction;
10. worker/subagent context/result semantics;
11. Human collaboration versus Human mechanical intermediary boundary;
12. source-of-truth/federation model for Planning/Execution;
13. portability proof across materially different Planning/Execution architectures;
14. proposed machine-verifiable layer after approval;
15. proposed smallest useful DR/ADR grouping;
16. explicit domain/entity admission decisions;
17. independent-review findings/risks;
18. a concise Human Owner decision set with leading recommendation, strongest credible alternative, tradeoff/consequence, and traceability.

Do not create GitHub artifacts/branch/PR for L1-H until the Human Owner approves the semantic decision set.

---

# 21. Key guardrails

Do NOT introduce:

- Kestrel material;
- canonical planner product;
- canonical execution orchestrator;
- canonical agent/swarm framework;
- canonical workflow/DAG engine;
- one source-control branch strategy;
- one Work Management provider workflow;
- one CI/CD topology;
- one model/provider;
- one task-count/decomposition recipe;
- one Planning Method for every work class;
- universal fresh-agent requirement;
- universal Human approval for every consequential-looking action unless higher canonical authority already requires it;
- generic new durable entities without DR-108 admission reasoning;
- hidden session state as durable work truth;
- self-Validation acceptance;
- provider Done = AE Accepted;
- Context Package as Plan/state authority;
- detailed standards-applicability algorithm;
- full developer-experience solution for issue #6.

Use the simplest semantic model that remains portable, governable, agent-operable, architecture-aware, traceable, resumable, verifiable, evolvable, and Human-comprehensible.

---

# 22. Closure requirement for the next design session

The next session should stop after presenting the L1-H design and Human Owner decision set.

It should not implement L1-H until Human Owner approval is supplied.

When the Human Owner later approves/refines the L1-H design, that implementation session should follow the normal:

```text
branch
→ semantic artifacts
→ machine representation/fixtures if approved
→ validator/CI
→ minimum DRs/ADR
→ issue #12 update if applicable
→ keep #6 open unless scope changes
→ independent review
→ correct findings
→ PR
→ verify applicable CI on exact head
→ merge
→ new relay handoff
```

Follow `handoffs/README.md` for every relay transition.
