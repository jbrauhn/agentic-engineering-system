# Handoff: L1-G Closure and L1-H Planning / Execution Design Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` for the next relay handoff.

---

# 1. Current authoritative repository state

L1-G — Knowledge / Context / Memory is complete, independently reviewed, machine-validated, and merged to `main`.

## Merge record

- PR: **#15 — Establish L1-G knowledge, context, and memory baseline**
- PR head reviewed/tested: `fc0311666005f2c69c8b3271679fc690e8f57b30`
- Merge commit on `main`: **`0dc7216eb091498c69d7935ae04d7f096ce4a3ad`**
- Merge completed: 2026-08-22

All four applicable PR integrity jobs passed on the exact PR head before merge:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`
- `context-integrity`

`context-integrity` passed **56 semantic scenarios + 4 retrieval-portability cases**.

Repository protection remains a known governance gap:

- `main` is still `protected:false`;
- the integrity jobs run automatically but are not verified repository-enforced required checks;
- issue #12 remains OPEN and now tracks all four jobs.

Issue #6 also remains OPEN for the complete Engineering Team Interface / Working Environment experience.

No Kestrel material was introduced.

---

# 2. L1-G durable artifacts now on `main`

## Human semantic artifacts

1. `L1-G_CANONICAL_KNOWLEDGE_CONTEXT_MEMORY_MODEL.md`
2. `L1-G_CONTEXT_REQUIREMENT_PACKAGE_MODEL.md`
3. `L1-G_CONTEXT_ASSEMBLY_PROVENANCE_MODEL.md`
4. `L1-G_HANDOFF_CONTINUATION_RECONSTRUCTION_MODEL.md`
5. `L1-G_CONTEXT_BOOTSTRAP_DISCOVERY_PROTOCOL.md`
6. `L1-G_BOUNDED_SELECTION_CURRENTNESS_SOURCE_MODEL.md`
7. `L1-G_KNOWLEDGE_WRITE_PROMOTION_SECURITY_MODEL.md`
8. `L1-G_CONTEXT_RELATIONSHIP_VIEWS.md`

## Decisions

9. `DR-121-system-owned-memory-context-requirements-and-reconstruction.md`
10. `DR-122-context-provenance-handoff-currentness-source-authority-and-security.md`
11. `DR-123-bootstrap-anchor-first-context-and-retrieval-portability.md`
12. `ADR-005-machine-readable-context-and-integrity.md`

Do not reuse DR-120. The inherited Decision Register already uses DR-120 for separation of standards/practices/protocols/house conventions.

## Machine-readable / executable reference layer

13. `context_protocol.json`
14. `context_scenarios.json`
15. `context_portability_fixtures.json`
16. `validate_context.py`
17. `.github/workflows/context-integrity.yml`

Human L1-G artifacts remain normative for meaning. JSON/Python/GitHub Actions are repository/reference implementation choices under ADR-005, following ADR-002/003/004.

---

# 3. Final L1-G semantic baseline

## Central memory principle

> **Canonical AE treats memory as a system property, not a central memory database.**

The System remembers because:

- durable engineering state has authoritative owners;
- durable references survive actors/sessions;
- retrieval reconstructs relevant information;
- Handoff preserves continuation state when required;
- material discoveries are promoted into the correct semantic owner;
- provenance/currentness/authority remain reconstructable.

> **The agent does not own memory; the system owns memory. Agents read and write under governed rules.**

This does **not** imply one physical storage system.

## R2 / R3 separation

**R2 — Durable Engineering State, Identity & Traceability** owns/guides:

- semantic ownership;
- authoritative source;
- identity/revision;
- provenance;
- durable relationships.

**R3 — Context & Knowledge Coordination** coordinates:

- retrieval;
- source resolution;
- bounded context assembly;
- Handoff/continuation;
- reconstruction;
- semantic promotion into R2 owners.

R3 may search, summarize, index, cache, vectorize, rank, and assemble. It does not become owner of Contract, Plan, Architecture, Evidence, Authority, Work, provider state, or other R2-governed truth merely because it presents that state to an actor.

## Six semantic memory/context layers

1. **AUTHORITATIVE_DURABLE_STATE**
2. **DURABLE_REFERENCE_KNOWLEDGE**
3. **CONTINUATION_STATE**
4. **DERIVED_RETRIEVAL_STATE**
5. **BOUNDED_CURRENT_CONTEXT**
6. **EPHEMERAL_SESSION_STATE**

Derived retrieval state includes indexes, embeddings, vector stores, caches, generated summaries, projections, rankings, and similar aids. These are never authoritative by default.

No generic canonical `Knowledge Item`, `Memory Record`, `Memory Store`, or universal shadow repository was introduced.

---

# 4. Context Requirement [B]

L1-G introduces subordinate:

> **Context Requirement [B] — what information must be resolvable for this actor/action/task before governed work can proceed correctly?**

It may define as applicable:

- purpose/lifecycle action/canonical operation;
- required governing anchors;
- required source/authority quality;
- exact-revision or scope-effectivity relationship;
- currentness/freshness relationship;
- security/access requirement;
- supporting context categories;
- failure disposition;
- assembly bounds.

Requirement classes:

- **REQUIRED_GOVERNING**
- **REQUIRED_OPERATIONAL**
- **SUPPORTING**

These are use semantics, not trust scores.

No new A1/A2 was required. DR-121 explicitly extends/clarifies the L1-C subordinate/derived catalog without changing the L1-C entity-admission rule.

---

# 5. Context Package [D]

Context Package remains the existing derived category:

> **A bounded, purpose-specific, disposable, reconstructable derived view for a current actor/action/task/decision.**

It may carry as applicable:

- package instance/purpose;
- consumer/runtime context;
- implementation/Product scope;
- Loop/Increment/Task;
- Context Requirement;
- assembly time;
- source refs;
- exact revisions/digests;
- source authority/currentness/effectivity;
- access/security constraints;
- selected material;
- conflicts/unavailable sources;
- bounds;
- Assembly Receipt reference.

It may include excerpts, structured facts, summaries, references, links, and retrieval affordances.

> **Bounded context can preserve exactness through resolvable references rather than loading every authoritative byte simultaneously.**

Context Package may never become a shadow Contract, Plan, Architecture, Decision, Evidence, policy, Work Management, or authority store.

When sources change, do not mutate an old package to pretend it was always current. Reassemble/create a new package or identify the old one as stale for the new use.

> **Context invalidation is not authoritative source-state mutation.**

---

# 6. Context Assembly Receipt / Source Manifest [B]

No Context Provenance A2 was created.

Use subordinate **Context Assembly Receipt / Source Manifest [B]** when consequential use or policy requires durable reconstructability beyond direct references.

It can support:

- purpose/Context Requirement;
- assembly time;
- authoritative source references;
- exact revisions/digests;
- retrieval/index sources;
- selection/exclusion outcomes;
- currentness/effectivity checks;
- authorization/access outcomes or refs;
- unresolved conflicts;
- assembly mechanism/version if materially relevant;
- optional integrity digest.

Durable retention is required when assembled context materially contributes to a durable consequential outcome and the basis cannot otherwise be reconstructed adequately from direct canonical references.

Potential examples include Validation, Authority Decision, Plan Review, material engineering/architecture Decision, Handoff, or protected transition depending on policy/risk.

Routine low-risk context does not require permanent receipt retention.

Do not require storing:

- chain of thought;
- secrets/credentials;
- every prompt;
- duplicated source bodies solely for provenance.

This avoids a provenance/audit swamp.

---

# 7. Handoff, continuation, and replacement actors

Handoff Record remains the existing **A2**. L1-G did not create a second Handoff type.

Handoff is authoritative for:

> **what was handed off at issuance**

not for:

> current Contract/Plan/Architecture/Authority/policy/provider state.

A receiving actor must resolve the current/effective authoritative references and detect later changes.

A Handoff can include:

- identity/sender;
- continuation scope;
- issued time;
- Loop/Increment/Task;
- current governed position at issuance;
- blockers/next action/unresolved questions;
- material results;
- exact reconstruction anchors for Contract, Plan/review, Baseline, Architecture, OEB/Profile, Decisions, Authority, Evidence/Validation;
- Assembly Receipt reference when required;
- uncertainty/known stale items.

Handoff is **conditionally required**, not mandatory for every model/worker invocation. It is required when a meaningful continuation boundary exists and material continuation state is not adequately reconstructable from other durable system state alone.

## Resumability invariant

> **Loss of actor/session-local context must not prevent an appropriately authorized replacement actor from reconstructing the material governed state necessary to continue the work.**

Fresh agent is not mandatory at every phase. Continuing agents are allowed.

Replacement need not reproduce identical prose, prompts, tokens, reasoning, or supporting retrieval. It must reconstruct materially equivalent governing understanding, including exact/effective revisions, lifecycle/work state, material Decisions, Architecture constraints, authority/capability constraints, Evidence/Validation, blockers, and unresolved material questions.

Material difference in governing understanding from the same authoritative state should be detectable.

---

# 8. Context Bootstrap / Discovery Protocol

A supported Access Path must allow a Human/agent/runtime to deterministically discover, as applicable:

1. Organization-specific AE Implementation;
2. Canonical AE release;
3. exact OEB revision;
4. exact Product/System Profile;
5. actor/authority context;
6. Product/System/work scope;
7. Loop/Increment/Task;
8. exact/effective Contract, Plan/review, Baseline, Architecture, Decisions, Validation state;
9. Capability Bindings + Access Paths;
10. applicable Handoff/continuation state;
11. Context Requirement;
12. bounded current Context Package.

A subordinate **Bootstrap Descriptor [B]** or semantic equivalent is allowed.

No Engineering Environment Profile was introduced.

Bootstrap can be realized by injected config, local machine metadata, runtime service, API, MCP, source-controlled material, Work Management, future Portal, or another conforming mechanism.

No Portal/CLI/IDE/daemon/agent-host/runtime/file naming convention is canonical.

Preserve issue #6 principle:

> **AE should require interface parity, not environment uniformity.**

Issue #6 remains OPEN because the complete working-environment UX/bootstrap mechanism remains downstream.

---

# 9. Bounded selection/currentness/source authority

## Anchor-first, relevance-expanding

Semantic assembly order:

1. required governing anchors;
2. current work/dependencies;
3. relevant Architecture neighborhood;
4. material Decisions/Evidence/Handoff;
5. supporting knowledge by relevance;
6. stop at bounded-context constraints.

This is not a retrieval algorithm.

Mandatory governing anchors cannot lose a relevance/popularity contest to semantically similar supporting material.

## Currentness modes

- **EXACT_REVISION**
- **EFFECTIVE_FOR_SCOPE**
- **CURRENT_AT_USE**
- **BEST_AVAILABLE / SUPPORTING**

Central invariant:

> **Correct/effective revision beats newest revision.**

Examples:

- a reviewed Plan revision for an active Increment may remain governing even when a newer Plan exists elsewhere;
- an older Contract revision may remain effective for an explicitly unaffected active scope after a Contract change;
- authority/revocation often requires CURRENT_AT_USE;
- a historical exact revision is valid when intentionally requested and resolvable.

Dispositions:

- required governing source stale/wrong → refresh/reassemble;
- required protected-use source currentness/authority UNKNOWN → BLOCKED;
- optional stale support → DEGRADE/CONSTRAIN as appropriate;
- requested exact historical → valid if resolvable.

## Source authority

Reuse DR-107. No context-specific truth system or trust score.

Metadata may distinguish orthogonally:

- authority relationship: AUTHORITATIVE / NON_AUTHORITATIVE / UNKNOWN;
- derivation: issued/source vs index/summary/cache/retrieval aid;
- currentness: satisfies / stale / unknown / intentionally historical.

Unresolved competing authoritative claims for the same material property/scope/version cannot be silently ranked into truth. Protected use blocks when required authoritative state cannot be established.

If authoritative source is unavailable, a cache/vector/summary does not become authoritative merely because it exists.

---

# 10. Knowledge capability and semantic promotion

L1-E Knowledge capability remains:

- `knowledge.read`
- `knowledge.query`
- `knowledge.write`
- `knowledge.reference`

`knowledge.write` remains a **protected operation**.

Core invariant:

> **`knowledge.write` persistence does not make information canonical truth.**

Reference-knowledge path:

```text
information
→ governed Knowledge provider
→ durable reference resource
→ provenance
→ External Resource Reference where useful
```

Canonical semantic promotion path:

```text
ephemeral discovery
→ determine materiality
→ identify semantic owner
→ establish source/conflict/evidence
→ authorize/validate as required
→ update correct canonical owner
→ preserve provenance
→ refresh derived index/context
```

Possible semantic owners include Contract Change Proposal, Plan, Architecture Model, DR/ADR, Evidence, Learning, Authority, Work, or another established owner.

The governing question is:

> **Where does this fact belong canonically?**

not “which memory store remembers it?”

Knowledge write cannot bypass Contract immutability, issued-record immutability, R2 ownership, DR-107, or L1-F authority/PEP enforcement.

---

# 11. Compaction and session loss

> **Compaction is not canonical state.**

Before intentional context discard/compaction, material state that would otherwise be lost must already be durable in its semantic owner or appropriate Handoff.

Automatic session loss must also be survivable because material engineering state should not have been session-only.

Summaries/compaction may assist retrieval but cannot replace exact Contract, Plan, Architecture, Authority Decision, Evidence, Validation, or authoritative provider state.

---

# 12. Security / information access

L1-F governs context retrieval/use.

Preserve:

`source exists ≠ actor may retrieve ≠ source may appear in Context Package ≠ summary may reveal it`.

> **A derived Context Package may not grant broader information access than the actor has to underlying information, absent an explicitly authorized and proven sanitization/declassification transformation.**

Stale authorization does not authorize indefinitely. Protected use re-evaluates current authority as required.

Later access revocation does not magically erase information already exposed. Conforming behavior supports, as applicable:

- no further governed retrieval;
- invalidation of continued protected use;
- blocking protected actions;
- provider/runtime purge/reset where supported/required.

No secret credential material belongs in context provenance.

---

# 13. Context versus Evidence / Validation

Context Package is **not automatically Evidence**.

Validation still evaluates exact Contract/Proof against Evidence and authoritative state.

If assembled context materially influenced a durable judgment beyond direct Evidence/Contract/Proof references, retain sufficient contextual basis through direct references and/or Context Assembly Receipt under the consequential-use rule.

No universal prompt logging is required.

---

# 14. Retrieval portability Proof

Two materially different synthetic retrieval architectures were implemented:

### Implementation A

- direct structured canonical repositories/sources;
- keyword/search index.

### Implementation B

- external canonical sources;
- knowledge service;
- vector/RAG retrieval.

Conformance does not require identical text/context package.

Equivalent governed reconstruction requires equivalent:

- governing Contract;
- Plan/review;
- Baseline/Architecture;
- work/governed anchors;
- material authority restrictions;
- source conflicts/blockers;
- no unauthorized leakage;
- required dispositions.

Supporting retrieved material may differ.

---

# 15. Machine-readable/executable L1-G

`context_protocol.json` encodes the Stage-1 conforming machine representation.

`validate_context.py` cross-checks real merged:

- L1-E Knowledge capability operations and protected `knowledge.write`;
- L1-D Contract revision-effectivity requirement;
- L1-F policy results and INDETERMINATE fail-closed rule.

The `context-integrity` workflow runs on PRs/pushes to `main`.

On PR #15 exact head `fc0311666005f2c69c8b3271679fc690e8f57b30`, it passed:

> **56 semantic scenarios + 4 retrieval-portability cases**

Coverage includes:

- Context Package derived/non-authoritative;
- exact historical resolution;
- effective-old revision beating newest;
- missing anchor failure;
- stale-summary rejection;
- vector/index non-authority;
- CURRENT_AT_USE unknown blocking;
- stale supporting degradation;
- source-authority conflict;
- inaccessible supporting vs required source behavior;
- unauthorized derived-summary leak;
- authorized sanitization transformation;
- fresh-agent reconstruction;
- hidden-chat dependency rejection;
- continuing/replacement equivalence and drift detection;
- Handoff live-reference use and stale detection;
- compaction survivability;
- `knowledge.write` non-promotion;
- semantic-owner promotion;
- generic memory entity rejection;
- consequential provenance and routine no-receipt behavior;
- heterogeneous/bootstrap access path;
- secret provenance rejection;
- confident-summary cannot hide missing anchor;
- Context Package reassembly after source change;
- Context Package not Evidence;
- mandatory-anchor priority;
- Knowledge-provider shadow-truth rejection;
- revoked access/current authority;
- conditional Handoff;
- authoritative-source unavailable/cache does not become authority.

All inherited `lifecycle-integrity`, `capability-integrity`, and `authority-integrity` jobs also passed on the same PR head.

---

# 16. Independent review findings and dispositions

No Contract contradiction was found. No new A1/A2 type was warranted.

Material design findings resolved before merge:

1. **L1-C extension clarity** — Context Requirement [B], Receipt [B], Bootstrap Descriptor [B], and Context Package [D] explicitly extend/clarify lower-category semantics without changing the A1/A2 admission rule.
2. **R2/R3 shadow-truth risk** — artifacts and tests explicitly keep R2 source ownership separate from R3 retrieval/context coordination.
3. **Decision-number collision** — inherited DR-120 exists, so L1-G uses DR-121/122/123.
4. **Cross-domain executable drift risk** — context validator reads actual L1-D/E/F machine artifacts rather than recreating local copies.

Anti-pattern review passed for:

- no generic memory entity;
- no vector/RAG/cache/summary authority promotion;
- no naive latest-revision semantics;
- no hidden actor/session dependency;
- no Handoff-as-current-truth;
- no compaction-as-state;
- no `knowledge.write` promotion bypass;
- no source-conflict silent ranking;
- no unauthorized summary leak;
- no Context-Package-as-Evidence assumption;
- no universal prompt/audit logging;
- no Portal/CLI/IDE/runtime dependency;
- no environment uniformity;
- no Kestrel;
- no downstream standards or Validation-risk design.

---

# 17. Open issues after L1-G

## Issue #6 — OPEN

Engineering Team Interface / Working Environment remains unresolved at full UX/installation/runtime level.

L1-E Access Path + L1-G Bootstrap/Context semantics now provide substantial semantic hooks, but issue #6 still asks:

> A developer or agent has opened its normal engineering environment. How does it actually use this AE implementation?

Do not close or solve this implicitly during L1-H unless Planning/Execution reveals a necessary semantic hook.

## Issue #12 — OPEN

Now tracks:

- lifecycle-integrity;
- capability-integrity;
- authority-integrity;
- context-integrity.

`main` remains unprotected. Do not claim checks are merge-required.

Closure Proof remains:

> intentionally failing applicable check is prevented from merging by repository rules.

---

# 18. What L1-H inherits

The next unresolved core semantic domain is **L1-H — Planning / Execution**.

Do not revisit L1-E Capability Contracts as if capability-interface design were still pending; L1-E deliberately pulled that domain forward.

L1-H must consume:

## From Contract v1.0

- architecture-aware Planning;
- credible Contract → Proof route;
- decomposition/dependencies;
- capability/authority/evidence/Validation/risk/constraints as applicable;
- bounded Execution;
- agents may adapt within Contract/architecture/OA/standards/policy/Plan boundaries;
- agents surface risks/architecture/evidence/Contract-change issues rather than hiding them;
- speed does not bypass Verification/Validation.

## From inherited Planning decisions

Relevant adopted Decision Register semantics include:

- **DR-020** — Planning is architecture-aware; every Plan references canonical architecture and affected elements/relationships.
- **DR-021** — C4 is currently the adopted architecture visualization baseline below Contract (Context + Container default, Component where useful; not immutable Contract meaning).
- **DR-022** — significant architecture decisions become ADRs with context/options/rationale/tradeoffs/consequences/affected architecture.
- **DR-023** — Planning creates executable L2/L3 boundaries, dependencies/parallelism/topology/context/verification.
- **DR-024** — Contract sits above planning depth.
- **DR-025** — L1 is durable Product/System baseline.
- **DR-026** — ongoing Loops use L2/L3 against L1; architecture-impacting L1 change uses ADR.
- **DR-027** — L4 is an agent micro-plan, ephemeral by default.
- **DR-028** — Planning Depth is mandatory.
- **DR-029** — Planning Method is mandatory.
- **DR-033** — Plan is dual-format/multi-representation: one Plan identity with Human/machine/IG views, not separate Plans.
- **DR-034** — exact Plan revision receives Plan Review; material Plan change requires appropriate re-review.
- **DR-110** — progressive elaboration remains a design principle.

Verify these inherited decisions from authoritative sources before relying on them if the relevant register material is not yet fully migrated into the minimal repo.

## From L1-C

- Plan [A1];
- Execution Increment L2 [A1];
- Executable Task L3 [A1];
- L4 micro-plan [E] ephemeral;
- Verification/Test Strategy [B] belongs to Plan and is derived from Contract Proof;
- Product/System Baseline L1 is durable persistent state, not another Plan;
- Executable Task is distinct from provider Work Item;
- Architecture Model is first-class and Plans can reference affected Architecture Elements/Relationships;
- exact revision / provenance / relationship semantics.

## From L1-D

- composite/scoped lifecycle protocol;
- Loop has no exclusive canonical current phase;
- L2 positions PLANNING / READY / EXECUTING / VALIDATING;
- L3 minimal portable execution state;
- Plan Review gate is exact Plan revision + explicit declared execution scope;
- Retry/Replan/Contract Change/Escalate are routes, not phases;
- Plan review can be scope-aware for rolling-wave work;
- local adaptation may not silently change reviewed Plan or approved Contract;
- Contract effectivity can differ explicitly across concurrent scopes;
- final Increment acceptance does not imply whole-Contract acceptance.

## From L1-E

Planning/Execution can depend on canonical provider-neutral operations such as:

- source reads/writes/compare/review submission;
- pipeline run/status/result/evidence;
- model invoke/metadata;
- execution start/status/result/cancel when applicable;
- identity context/scoped credential use;
- tool discovery/describe/invoke/result;
- telemetry emit/query/read;
- knowledge read/query/write/reference;
- work create/query/read/update/transition/relationships/annotations/references/artifacts/complete;
- Validation request/status/result/evidence.

Capability Binding resolution is scope-aware/deterministic and direct Human mechanical middleware does not satisfy required agent-operability.

## From L1-F

Execution actions are governed by:

- identity;
- binding-determined technical entitlement;
- OA;
- DA/Authority Decision where applicable;
- policy PERMIT/DENY/INDETERMINATE;
- distributed PEP;
- ALLOWED/DENIED/BLOCKED runtime outcome;
- least privilege;
- expiry/revocation;
- self-escalation prohibition;
- pre-change-state authorization for authority-changing actions;
- bypass-path Proof.

Planning must not confuse desired execution with authorized execution.

## From L1-G

Planning/Execution actors obtain current governed context through:

- Context Requirement;
- Bootstrap/discovery;
- exact/effective governing anchors;
- anchor-first bounded context;
- Context Package [D];
- Handoff continuation when required;
- system-owned reconstruction;
- semantic-owner promotion for material discoveries.

Planning/Execution must not depend on hidden chat/session memory or allow an L4 micro-plan to become undeclared durable truth.

---

# 19. L1-H design mission

Design the minimum canonical **Planning / Execution semantics** needed so an Organization-specific AE Implementation can transform an approved Contract + Product/System Baseline + current Context into a reviewed, architecture-aware, executable Plan and then allow capable agents/Humans to adapt and execute within governed boundaries—without canonizing one planning methodology, agent orchestrator, coding workflow, work-breakdown template, branch strategy, model-routing algorithm, or runtime topology.

Do **not** implement L1-H immediately.

The next session should first perform dialectic design and present the consequential Human Owner decision set. No GitHub writes for L1-H until Human Owner approval unless the Human Owner explicitly directs otherwise.

---

# 20. Core L1-H tensions to resolve

## A. What exactly is a canonical Plan?

L1-C says Plan [A1], but L1-H must now define its minimum behavioral content without turning it into a giant document template.

Likely concerns:

- exact Contract revision;
- Product/System Baseline revision;
- Architecture impact;
- scope/decomposition;
- L2/L3 boundaries;
- dependencies/parallelism;
- capability requirements;
- authority requirements;
- Verification/Test Strategy from Proof;
- evidence-generation plan;
- Validation readiness;
- context/handoff expectations;
- risks/constraints/assumptions;
- adaptation boundaries;
- Planning Depth and Method;
- review scope.

Test whether each truly belongs in canonical Plan semantics versus an implementation-specific representation.

## B. Planning Method versus canonical Planning semantics

DR-029 says Planning Method is mandatory, but Canonical AE should not freeze one methodology.

Determine what every Planning Method must accomplish/prove versus what can vary.

Possible implementation methods may include collaborative Human–AI planning, hierarchical decomposition, dependency-first planning, architecture walk, risk-first planning, iterative/rolling-wave planning, or another method.

The invariant should likely be outputs/coverage/proof, not one procedure—but test that assumption.

## C. Planning Depth

Clarify the relationship among:

- L1 persistent Product/System Baseline;
- Plan [A1];
- L2 Execution Increment;
- L3 Executable Task;
- L4 ephemeral actor micro-plan.

Planning Depth should match work/risk/uncertainty rather than forcing every request through maximum decomposition.

Need explicit progressive elaboration behavior.

## D. Rolling-wave Planning

L1-D already permits one Loop to contain different Plan revisions for different explicit scopes.

L1-H must define safe semantics for:

- Plan scope declarations;
- when later increments may remain less detailed;
- when execution of reviewed scope can proceed while future scope is still being planned;
- how dependencies across different Plan revisions are governed;
- how a new Plan revision affects already-executing/unaffected scopes;
- re-review triggers.

Avoid both waterfall serialization and ambiguous mixed-plan execution.

## E. Plan Review boundary

L1-D establishes G2 and exact Plan revision + explicit scope.

L1-H should define what review evaluates sufficiently to make `reviewed_for_execution` meaningful without stealing L1-J independent Validation.

Plan Review likely evaluates the **credibility/safety/completeness of the proposed route**, not whether the final outcome satisfies Contract Proof.

Keep Plan Review ≠ Verification ≠ final Validation.

## F. Execution adaptation boundary

Need a precise canonical test for:

1. local execution adaptation allowed within reviewed Plan;
2. material Plan change requiring Replan/re-review;
3. Contract-impacting discovery requiring Contract Change Proposal/Human gate.

This is a high-value decision.

Avoid two extremes:

- agents mechanically follow obsolete Plan steps even when harmless adaptation is obvious;
- agents silently rewrite material Plan/Contract semantics in the name of autonomy.

## G. Execution topology / multi-agent behavior

Do not canonize one orchestrator, planner agent, executor agent, subagent tree, queue, model-routing strategy, or fresh-agent pattern.

Canonical AE may need semantic concepts for:

- parallelizable work;
- dependencies;
- task assignment/responsibility;
- bounded execution scopes;
- result/handoff/evidence return;
- independent judgment constraints;
- failure/retry;
- work ownership/claiming.

Test what must be canonical versus implementation policy.

## H. L4 micro-plan

DR-027 says L4 is ephemeral by default.

Define when an L4 discovery becomes material and must be promoted to:

- Plan revision;
- Decision/ADR;
- Contract Change Proposal;
- Evidence;
- Learning;
- Handoff;
- Work update;
- Architecture update;
- other semantic owner.

L1-G semantic promotion should be reused rather than inventing a second persistence model.

## I. Verification strategy versus execution evidence

Contract Proof remains in Contract.

Plan owns Verification/Test Strategy derived from Proof.

Execution should produce evidence according to the Plan but may discover better/new verification methods.

Need rules for:

- adding verification without unnecessarily revising Plan;
- changing material evidence strategy;
- failed verification during execution;
- differentiating engineering Verification from independent Validation.

Do not steal L1-J detailed evidence/Validation design, but preserve clean hooks.

## J. Architecture-aware Planning

Planning must structurally reference affected Architecture Model elements/relationships, not merely include a prose claim that architecture was considered.

Need decide minimum architecture-impact semantics:

- affected elements/relationships;
- proposed changes;
- expected invariant boundaries;
- required ADR trigger;
- unresolved architecture questions;
- architecture-health remediation opportunities.

Do not make C4 notation itself an immutable Plan semantic.

## K. Capability / authority planning

Plan should identify required canonical operations and authority assumptions early enough to prevent execution-time surprises.

But avoid duplicating full Capability Binding or L1-F policy data into Plan.

Likely Plan references requirements/bindings/authority constraints rather than shadow copies them.

Need decide what unresolved capability/authority state does to Plan Review / READY transition.

## L. Context Planning

Use L1-G Context Requirements where execution/review/Validation needs known context.

Do not embed giant prompts or static context dumps into Plan.

Need decide whether Plan can declare context requirements for increments/tasks/decision points and how they remain current through rolling-wave execution.

## M. Side quests / discoveries / interrupts

Engineering agents often find unrelated-but-important work.

Need canonical routing for discoveries that are:

- required to complete current Contract;
- useful but out of scope;
- architecture debt;
- engineering-health finding;
- security issue;
- standards concern;
- new opportunity;
- Contract contradiction.

Avoid letting useful discoveries silently expand scope while also avoiding loss of valuable agent-detected work.

## N. Completion semantics

Task/provider Done does not mean Increment/Loop accepted.

L1-H should define what Execution completion means before handoff to independent Validation:

- planned work/evidence sufficiently produced;
- outstanding deviations known;
- material findings routed;
- execution state/provenance durable;
- Validation request ready.

Do not redefine final Validation acceptance.

---

# 21. Specific Human Owner decisions the next session should test

At minimum analyze these before implementation. Do not assume one DR per question.

1. What is the minimum canonical Plan semantic model?
2. What does a conforming Planning Method have to accomplish without prescribing a method?
3. How is Planning Depth selected/escalated/de-escalated?
4. How do Plan, L2, L3, and L4 relate operationally?
5. How does progressive/rolling-wave elaboration work without ambiguous mixed revisions?
6. What exact scope semantics must Plan Review cover?
7. What does Plan Review evaluate versus independent Validation?
8. What is the canonical test for local adaptation vs material Plan change vs Contract change?
9. Can execution continue under an older reviewed Plan scope after a new Plan revision exists elsewhere, and under what explicit conditions?
10. What execution/dependency/parallelism semantics are canonical without prescribing orchestration topology?
11. How are task assignment/claiming and actor responsibility represented without tying AE to one Work Management system?
12. What material L4 discoveries must be promoted and to which semantic owners?
13. What minimum Verification/Test Strategy semantics must Plan own relative to Contract Proof?
14. When does an evidence/verification-strategy change require Plan revision/re-review?
15. What minimum Architecture impact representation must Planning produce?
16. When does Planning trigger an ADR versus ordinary Plan detail?
17. What capability-operation requirements belong in Plan and what stays in Capability Binding/OEB?
18. What authority assumptions/requirements belong in Plan without shadowing L1-F policy state?
19. How should Plan declare/use Context Requirements without embedding static prompt context?
20. How are side quests/out-of-scope discoveries captured, prioritized, and prevented from silently expanding the Contract?
21. What conditions establish `Execution complete / ready for independent Validation`?
22. What machine-readable Planning/Execution semantics and fixtures become useful now?
23. Should a new `planning-execution-integrity` check be introduced, and what meaningful failures must it catch?
24. If a new integrity job is added, update issue #12 rather than creating another governance issue.

For each consequential choice provide:

- leading recommendation;
- strongest credible alternative;
- tradeoff/consequence;
- Contract / DR / L1-A–G traceability.

---

# 22. Machine-verifiable direction for L1-H

Do not add CI as ritual, but L1-H now has enough precise semantics that an executable reference model will likely be useful.

Potential machine artifacts, only after Human Owner approval, may include semantic equivalents of:

- `planning_execution_protocol.json`
- Plan/scoped review fixtures
- rolling-wave/mixed-revision fixtures
- adaptation/replan/Contract-change fixtures
- architecture-impact fixtures
- capability/authority/context requirement fixtures
- execution-completion/Validation-readiness fixtures
- `validate_planning_execution.py`
- `.github/workflows/planning-execution-integrity.yml`

A meaningful validator should catch failures such as:

- Plan does not reference exact Contract/Baseline;
- reviewed scope does not cover executing Increment;
- Plan revision changed materially but stale review is reused;
- L4 change silently changes Plan or Contract;
- Plan says architecture-aware but references no affected architecture where material;
- required capability operation unavailable/ambiguous but Plan pretends execution-ready;
- authority prerequisite unknown/denied but Plan pretends ready;
- required governing context unresolved/stale but Execution begins;
- provider Task Done treated as final AE acceptance;
- material deviation hidden rather than routed;
- side quest silently expands Contract scope;
- executor self-validates outcome;
- execution completion lacks required evidence/known-deviation disposition.

Any executable model must cross-check the existing L1-D/E/F/G machine artifacts instead of recreating local shadow definitions.

---

# 23. L1-H scope guardrails

Do **not** in L1-H:

- reopen approved Contract v1.0 without a real contradiction;
- canonize one Agile/Scrum/SAFe/Kanban method;
- canonize one planning algorithm;
- canonize one planner/executor agent persona;
- require fresh agent every phase;
- canonize one multi-agent framework/orchestrator;
- canonize one branch/PR/repository workflow universally;
- canonize one model/provider or model-routing strategy;
- turn Plan into a giant mandatory document template;
- duplicate Capability Binding, authority policy, or Context Package state into Plan;
- make Work Management provider status canonical AE acceptance;
- make C4 an immutable Contract invariant;
- solve detailed Standards applicability prematurely;
- steal detailed L1-J Validation/evidence-risk design;
- solve issue #6 developer experience unless a narrow semantic hook is genuinely required;
- introduce Kestrel.

---

# 24. Independent review expected before L1-H closure

After implementation, independently test at least:

- Contract fidelity;
- inherited Planning DR fidelity;
- L1-C entity/revision fidelity;
- L1-D scoped lifecycle/gate fidelity;
- L1-E capability-operability fidelity;
- L1-F authority/PEP fidelity;
- L1-G context/reconstruction fidelity;
- architecture-aware Planning actually structural rather than ceremonial;
- rolling-wave concurrency without ambiguous governing Plan revision;
- Plan Review not collapsing into Validation;
- adaptation autonomy without silent Plan/Contract mutation;
- side-quest value preservation without scope creep;
- L4 ephemerality with correct semantic promotion;
- multi-agent portability;
- provider/workflow neutrality;
- Human comprehensibility;
- agent-operability;
- evidence/Validation-readiness hooks;
- no giant planning bureaucracy for simple work;
- no hidden session dependency;
- machine/reference model parity.

Stop and surface only if a real Contract contradiction or a genuinely new A1/A2 admission need appears.

---

# 25. Next genuine Human Owner decision gate

The first L1-H decision question should be framed around this:

> **What is the minimum canonical Plan + bounded-Execution contract that preserves architecture-aware intent, exact reviewed scope, progressive/rolling-wave elaboration, agent adaptation, capability/authority/context requirements, Verification strategy, and durable deviation/evidence routing—while allowing materially different planning methods, agent topologies, Work Management systems, and engineering workflows to conform?**

A particularly consequential sub-question is:

> **What exact semantic test distinguishes an allowed local Execution adaptation from a material Plan change requiring Replan/re-review, and from a Contract-impacting change requiring Human-governed Contract change?**

Do not implement L1-H until the Human Owner reviews/approves the consequential decision set.

---

# 26. Required next-session workflow

1. Read this handoff completely.
2. Re-read `handoffs/README.md`.
3. Verify `main` and relevant inherited artifacts/decisions.
4. Perform dialectic L1-H design only.
5. Present consequential decision set to Human Owner with recommendations/alternatives/tradeoffs/traceability.
6. Make **no L1-H GitHub writes** until Human Owner approval unless explicitly directed otherwise.
7. After eventual L1-H implementation/merge, create a new uniquely named relay handoff under `handoffs/` on `ae-session-relay` and give the Human Owner only the required short summary + copy/paste handoff pointer.
