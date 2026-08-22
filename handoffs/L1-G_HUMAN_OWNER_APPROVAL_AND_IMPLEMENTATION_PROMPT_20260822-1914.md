# Handoff: L1-G Human Owner Approval and Implementation Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` when creating the next handoff.

---

# Human Owner Decision — L1-G

The Human Owner approves the L1-G recommendations presented in the review session.

You are authorized to implement **L1-G — Knowledge / Context / Memory** under the constraints below.

The core approved principle is:

> **Canonical AE should treat “memory” as a system property, not a central memory database.**

The system remembers because durable state has authoritative owners, durable references survive sessions, retrieval can reconstruct relevant information, handoffs preserve continuation state, and material discoveries are promoted back into the correct durable semantic owner.

Do not make one vector database, RAG stack, memory service, agent framework, context-window strategy, or conversation history mechanism canonical AE architecture.

---

# 1. Approved decision — Memory is a system behavior, not a store

APPROVED.

Preserve the distinction:

```text
Authoritative durable engineering state
≠ Knowledge provider storage automatically
≠ search index
≠ vector embedding
≠ generated summary
≠ conversation history
≠ current Context Package
```

Use the following semantic decomposition:

1. **Authoritative durable engineering state**
   - Contract, Plan, Architecture, Baselines, Decisions, Evidence, Validation, Authority state, provider-owned authoritative properties, etc.

2. **Durable reference / knowledge state**
   - documentation, externally authoritative/reference resources, Learning, standards/policy references, and similar durable information whose authority is independently determined.

3. **Continuation state**
   - Handoff Record and other approved continuation anchors.

4. **Derived retrieval state**
   - search indexes, embeddings, vector stores, caches, summaries, projections, and other reconstructable navigation/retrieval aids.

5. **Bounded current context**
   - Context Package assembled for a current purpose.

6. **Ephemeral actor/session state**
   - conversation state, scratch work, transient tool state, L4 micro-plan, temporary reasoning/session context.

Preserve:

> **The agent does not own memory; the system owns memory. Agents read/write under rules.**

This means the AE System owns responsibility for persistence, source authority, retrieval, continuation, provenance, reconstruction, and promotion.

It does NOT mean AE owns one central memory database.

Do not create a generic canonical `Memory Store`, `Memory Record`, or universal shadow state repository.

---

# 2. Approved decision — Add Context Requirement [B]

APPROVED.

Introduce a subordinate **Context Requirement [B]**.

Its purpose is to answer:

> **What information must be resolvable for this actor/action/task before governed work can proceed correctly?**

This is the approved mechanism for making “good context” testable without prescribing retrieval technology.

Context Requirement should support, as applicable:

- purpose / lifecycle action / canonical operation;
- required governing anchors;
- required authority/source quality;
- required exact revision/effectivity relationship;
- required currentness/freshness relationship;
- required security/access conditions;
- optional/supporting context categories;
- failure disposition when required context cannot be established.

Example conceptually:

```text
Begin Execution for Increment A

requires:
  AE Loop
  Increment
  governing Contract exact/effective revision
  reviewed Plan exact revision + declared scope
  Product/System Baseline
  applicable Architecture neighborhood
  relevant authority requirements
  Capability Binding / Access Path information

supporting:
  related historical decisions
  relevant prior findings / learning
```

Do not make Context Requirement an A1/A2 entity unless implementation review produces a new identity/lifecycle argument that passes the L1-C admission test.

---

# 3. Context Package remains derived [D]

Preserve the inherited L1-C decision:

> **Context Package remains D — derived, disposable, reconstructable.**

It does not become authoritative truth merely because an actor consumes it.

Minimum semantics should support as applicable:

- package-instance identity/reference;
- purpose/context intent;
- intended actor/consumer/runtime context;
- Organization-specific AE Implementation;
- Product/System scope;
- Loop / Increment / Task scope;
- Context Requirement reference;
- assembly time;
- source references;
- exact revisions/digests where material;
- source authority relationship;
- currentness/effectivity result;
- access/security constraints;
- selected material/references;
- unresolved conflict/unavailable-source indications;
- assembly bounds/constraints;
- Context Assembly Receipt / Source Manifest reference where retained.

A Context Package may contain:

- excerpts;
- structured facts;
- summaries;
- references;
- retrieval affordances.

It need not copy every authoritative byte into the model window.

Preserve:

> **Bounded context can preserve exactness through resolvable references rather than loading every authoritative byte simultaneously.**

No Context Package becomes a shadow Contract, Plan, Architecture Model, Decision Register, Evidence store, or policy store.

---

# 4. Approved decision — Keep context provenance lightweight

APPROVED.

Do NOT create a new Context Provenance A2 record at L1-G.

Use subordinate:

> **Context Assembly Receipt / Source Manifest [B]**

retained durably **when needed**.

It should support, as applicable:

- Context Package / purpose / Context Requirement reference;
- assembly time;
- authoritative source references;
- exact revisions/digests where material;
- retrieval/index sources used;
- selection/exclusion outcomes;
- currentness checks;
- authorization/access outcomes or references;
- unresolved conflicts;
- assembly mechanism/version when materially relevant;
- optional package integrity digest.

Do NOT require storing:

- private chain-of-thought;
- credentials/secrets;
- every prompt;
- complete duplicated source bodies solely for provenance.

Approved principle:

> **Material context provenance may be durable without context provenance becoming a first-class domain entity.**

## Consequential-use trigger

Do not retain every routine context assembly permanently.

Durable context provenance should be required when assembled context materially contributes to a durable consequential outcome whose basis otherwise cannot be adequately reconstructed from direct canonical references.

Potential examples depending on policy/risk:

- Validation judgment;
- Human Authority Decision;
- Plan Review;
- material architecture/engineering decision;
- Handoff;
- protected transition;
- other durable governed judgment.

If the durable output already directly references all material authoritative inputs, a separate full receipt may be unnecessary.

Avoid an audit-record swamp.

---

# 5. Handoff Record [A2] semantics

Handoff Record already exists as A2. Do not introduce a second handoff entity.

Define its continuation semantics approximately as:

- Handoff identity;
- sender/issuing actor;
- intended continuation scope / receiving actor class where relevant;
- issued time;
- Loop / Increment / Task;
- what work is being continued;
- current governed position;
- blockers;
- next meaningful action;
- unresolved questions/risks;
- material results since the prior continuation point;
- exact reconstruction anchors for material Contract, Plan/review scope, Baseline, Architecture, OEB/Profile, Decisions, Authority, Evidence/Validation;
- Context Assembly Receipt / provenance reference when required;
- explicit uncertainty / known stale items.

Critical distinction:

> **A Handoff Record is authoritative as the issued record of what was handed off at that time. It is not authoritative for the current state of the Contract, Plan, architecture, policy, or other referenced artifacts.**

The receiving actor resolves authoritative references and detects later change.

A later Contract/Plan/OEB change does not destructively rewrite an old Handoff.

## Conditional requirement

Do NOT require a Handoff A2 for every model invocation or worker call.

Handoff is conditionally required when responsibility/continuation crosses a meaningful actor/session boundary and material continuation state exists that is not adequately reconstructable from other system state alone.

Small worker returns/results may remain ordinary result/evidence/provenance semantics.

---

# 6. Fresh / continuing / replacement actor model

APPROVED.

Continuing agents are allowed.

Fresh-agent replacement is not mandatory at every lifecycle phase.

But preserve the conformance invariant:

> **Loss of actor/session-local context must not prevent an appropriately authorized replacement actor from reconstructing the material governed state necessary to continue the work.**

No material engineering state may exist only in private conversation/session memory.

A replacement actor does NOT need:

- identical prose;
- identical prompt text;
- identical token context;
- identical reasoning;
- identical supporting retrieval results.

It must be able to reconstruct materially equivalent **governing understanding**, including as applicable:

- controlling exact/effective revisions;
- current work/lifecycle state;
- material decisions;
- architecture constraints;
- applicable authority/capability constraints;
- evidence/Validation state;
- blockers/unresolved material questions.

Differences in governed understanding from the same authoritative state should be detectable through the approved integrity scenarios.

---

# 7. Context Bootstrap / Discovery Protocol

APPROVED as a canonical semantic protocol, NOT a technology.

A Human/agent entering through a supported Access Path must be able to deterministically discover, as applicable:

1. Which Organization-specific AE Implementation is this?
2. Which Canonical AE release applies?
3. Which exact OEB revision applies?
4. Which exact Product/System Profile applies?
5. Who is the actor / what authority context matters?
6. Which Product/System/work scope is being entered?
7. Which Loop / Increment / Task applies?
8. Which exact/effective Contract, Plan/review scope, Baseline, Architecture, Decisions, and Validation state apply?
9. Which Capability Bindings and Access Paths apply?
10. Is there an applicable Handoff/continuation state?
11. Which Context Requirement applies?
12. Assemble bounded current context.

Use a subordinate **Bootstrap Descriptor [B]** or semantically equivalent discovery metadata if useful.

Do NOT create an `Engineering Environment Profile` A1 merely for bootstrap.

Do NOT prescribe:

- Portal;
- CLI;
- IDE;
- bootstrap filename;
- MCP server;
- local daemon;
- agent host;
- REST endpoint;
- one runtime.

Issue #6 remains OPEN.

Preserve:

> **AE should require interface parity, not environment uniformity.**

L1-E Access Path + L1-G Bootstrap/Context semantics should create a meaningful semantic hook without solving the broader developer-experience mechanism.

---

# 8. Bounded context selection

APPROVED leading model:

> **Anchor-first, relevance-expanding context assembly.**

This is semantic ordering, not a retrieval algorithm.

Conceptually:

```text
FIRST
required governing anchors

THEN
current work objects / dependencies

THEN
relevant architecture neighborhood

THEN
material decisions / evidence / handoff

THEN
supporting knowledge by relevance

STOP
when bounded-context constraints are reached
```

Context selection should consider as applicable:

- Context Requirement;
- authority/source quality;
- scope;
- exact revision/effectivity;
- currentness;
- dependency relationships;
- architecture proximity;
- information-access policy;
- materiality;
- runtime/model/resource limits.

Do NOT make canonical:

- token count;
- model context-window size;
- top-k;
- embedding model;
- chunk size;
- reranker;
- one retrieval algorithm.

Mandatory governing anchors must not lose a popularity/relevance contest to semantically similar retrieved text.

---

# 9. Currentness / staleness / effectivity

APPROVED refinement:

> **Correct/effective revision beats newest revision.**

Do not use a simplistic `latest = correct` rule.

Context sources should support requirement-relative currentness semantics equivalent to:

## EXACT_REVISION

That exact revision is required.

A newer revision does not make the intentionally requested historical/exact revision invalid.

## EFFECTIVE_FOR_SCOPE

The system must identify which exact revision governs the declared work scope.

This must be compatible with L1-D Contract revision effectivity and rolling-wave behavior.

## CURRENT_AT_USE

The source must be current enough at protected use time.

Examples may include:

- authority/revocation state;
- operational provider facts;
- other policy-required current state.

## BEST_AVAILABLE / SUPPORTING

Supporting information may assist reasoning without being a gating authoritative anchor.

Stale/missing supporting information may DEGRADE rather than BLOCK.

## Dispositions

Use semantics approximately like:

```text
required governing source known stale/wrong revision
→ REFRESH / REASSEMBLE

required protected-use state freshness/authority UNKNOWN
→ BLOCKED until resolved

optional/supporting source unavailable/stale
→ DEGRADE / CONSTRAIN as applicable

historical source intentionally requested
→ valid when exact historical revision resolves
```

Do not silently mutate an old Context Package to claim it is current.

Generate/reconstruct a new package.

Preserve:

> **Context invalidation is not authoritative source-state mutation.**

---

# 10. Source authority / conflict handling

Reuse DR-107.

Do not create a context-specific competing truth model.

## Authoritative source known

Use it.

A conflicting index/cache/summary/non-authoritative copy is identified as conflicting/stale/non-authoritative.

## Two sources claim authority for the same property/scope/version

Context assembly may NOT silently choose the easiest/highest-ranked source.

Represent unresolved source authority conflict explicitly.

For protected use:

> unresolved authority conflict → required state cannot be established → BLOCKED.

For exploratory reasoning, the unresolved conflict may be exposed as unresolved context.

## Authoritative source unavailable

Do NOT promote a cache/vector/summary result to authoritative truth.

Treat authority/currentness as unknown according to Context Requirement.

## Source metadata

Avoid a single generic “trust score.”

Use orthogonal semantics sufficient to distinguish as applicable:

- authority relationship: AUTHORITATIVE / NON_AUTHORITATIVE / UNKNOWN;
- derivation relationship: source/issued vs derived/indexed/summarized;
- currentness relationship: satisfies requirement / stale / unknown / intentionally historical.

Reuse existing domain identity/revision/provenance semantics rather than creating a large new trust ontology.

---

# 11. Approved decision — No generic Knowledge Item / Memory Record

STRONGLY APPROVED.

Do NOT add generic:

- `Knowledge Item [A1]`;
- `Memory Record [A1]`;
- universal canonical memory object.

Material engineering state already has semantic owners, including:

- Contract;
- Plan;
- Architecture;
- Decision/ADR;
- Evidence;
- Validation;
- Learning;
- Handoff;
- Authority;
- Work/provider state;
- External Resource References.

A generic Knowledge Item would create a shadow source of truth.

If later evidence identifies a specific durable object with independent identity/lifecycle that passes DR-108, admit that specific type then.

Do not pre-create a universal bucket.

---

# 12. Knowledge write / semantic promotion

APPROVED.

`knowledge.write` means persistence through the Knowledge capability.

It does NOT mean the information becomes canonical truth.

Preserve two paths.

## Reference-knowledge persistence

```text
information
→ governed Knowledge provider
→ durable external/reference resource
→ provenance
→ External Resource Reference where useful
```

This may support documentation, reference notes, source material, searchable organizational knowledge, etc.

Authority remains independently determined.

## Canonical promotion

```text
ephemeral discovery
→ determine materiality
→ identify semantic owner
→ establish source/conflict/evidence
→ authorize/validate as required
→ write/update the correct canonical owner
→ preserve provenance
→ refresh derived indexes/context
```

The correct destination may be, for example:

- Contract Change Proposal;
- Plan revision;
- Architecture Model;
- Decision/ADR;
- Evidence Record;
- Learning Record;
- Authority state;
- Work state;
- another canonical owner.

The key question is:

> **Where does this fact belong canonically?**

not:

> “Which memory store should remember it?”

Generic `knowledge.write` may not bypass:

- Contract immutability/change control;
- R2 ownership;
- issued-record immutability;
- DR-107 source authority;
- L1-F authority/PEP enforcement.

---

# 13. Compaction / summaries

Preserve:

> **Compaction ≠ canonical state.**

Summaries/compaction may assist:

- compression;
- retrieval;
- context assembly;
- handoff.

They cannot silently replace exact:

- Contract;
- Plan;
- Architecture;
- Authority Decision;
- Evidence;
- Validation;
- authoritative provider state.

Adopt the invariant:

> **Before system-managed context is intentionally discarded or compacted, material state that would otherwise be lost must already have been promoted to its durable semantic owner or an appropriate Handoff/continuation record.**

Automatic actor/session loss must also be survivable because material state should never have been session-only in the first place.

Where summaries are used for continuation, preserve source/revision references for material claims as applicable.

---

# 14. Context security / authority integration

L1-F authority applies to retrieval and context assembly.

Preserve:

```text
source exists
≠ actor may retrieve
≠ source may appear in Context Package
≠ derived summary may reveal it
```

Adopt:

> **A derived Context Package may not grant broader information access than the actor has to the underlying information, absent an explicitly authorized and proven sanitization/declassification transformation.**

By default, derived summaries cannot bypass source restrictions.

Also preserve:

- Context Assembly Receipt stores references/provenance, not credentials/secrets;
- stale authorization does not indefinitely authorize retrieval;
- protected actions re-evaluate current authority as required rather than trusting old Context Package state;
- source classification/access constraints are honored without designing the enterprise classification system itself.

Do not claim information already exposed to an actor is magically erased by later revocation.

Canonical behavior should instead support as applicable:

- no further governed retrieval;
- invalidation of continued protected use;
- blocking protected actions based on revoked authority;
- provider/runtime purge/reset where organization mechanisms support/require it.

---

# 15. Context relationship to Validation / consequential judgments

A Context Package is NOT automatically Evidence.

Validation still evaluates exact Contract/Proof using Evidence Records and other authoritative state.

Where a consequential judgment materially depended on assembled context beyond direct canonical references, retain sufficient source basis according to the consequential-use provenance rule.

Example:

```text
Validation Record
  ├─ exact Contract / Proof
  ├─ Evidence Records
  └─ Context Assembly Receipt
     when additional assembled context materially influenced judgment
```

The same concept may apply under policy to:

- Plan Review;
- Authority Decision;
- architecture/engineering decisions;
- other protected durable judgments.

Do NOT require universal prompt logging.

---

# 16. Retrieval portability Proof

APPROVED.

Use at least two materially different synthetic retrieval implementations.

Example:

## Implementation A

```text
canonical repositories/docs/work system
+ direct structured reads
+ keyword/search index
```

## Implementation B

```text
external canonical sources
+ knowledge service
+ vector/RAG retrieval
```

Do NOT require identical retrieved text or identical Context Package formatting.

Equivalent conformance outcome means the implementations reconstruct the same **required governed context**, such as:

- same governing exact/effective Contract;
- same applicable Plan/review scope;
- same required Baseline/Architecture anchors;
- same current work state;
- same material decisions;
- same authority restrictions;
- no unauthorized source leakage;
- no hidden unresolved authority/source conflict;
- same required blockers/dispositions.

Supporting/background context may differ.

This proves portability without canonizing vector/RAG retrieval.

---

# 17. Approved decision — Make L1-G machine-testable

APPROVED.

Continue the staged machine-authority model from ADR-002/003/004.

Human L1-G semantic artifacts:
= normative for meaning.

Machine-readable context definitions/scenarios:
= conforming executable representation.

Python validator:
= repository/reference implementation.

GitHub Actions:
= repository CI implementation.

None become Canonical AE technology requirements.

Recommended artifacts:

- `context_protocol.json`
- `context_scenarios.json`
- `context_portability_fixtures.json`
- `validate_context.py`
- `.github/workflows/context-integrity.yml`

Create a distinct:

> **`context-integrity`**

job.

Do NOT build a production RAG system, vector DB, context service, or agent-memory framework.

The executable layer proves semantics only.

---

# 18. Required context-integrity tests

At minimum test meaningful scenarios equivalent to:

1. Context Package cannot become authoritative truth.
2. Required Contract/Plan/OEB references resolve correctly.
3. Correct/effective revision beats naïve latest-revision selection.
4. Intentionally historical exact revision remains valid for an exact historical requirement.
5. Stale summary cannot override newer authoritative state.
6. Vector/index result cannot become authoritative merely through retrieval.
7. Required CURRENT_AT_USE authority/currentness UNKNOWN blocks protected use.
8. Optional stale supporting source degrades/constrains rather than always blocking.
9. Conflicting authority claims become explicit unresolved state.
10. Unauthorized source is excluded from context.
11. Derived summary cannot leak inaccessible source material.
12. Fresh agent reconstructs required Loop context without hidden prior conversation history.
13. Continuing and replacement actors obtain equivalent governing anchors.
14. Handoff resolves authoritative references rather than treating copied summary as current truth.
15. Stale Handoff is detectable against current authoritative state.
16. Compaction/session loss does not destroy the only copy of material state.
17. Ephemeral discovery cannot become canonical merely through `knowledge.write`.
18. Correct semantic-owner promotion succeeds.
19. No generic Knowledge Item entity is required for correct operation.
20. Consequential context provenance is retained where required.
21. Routine low-risk assembly need not create permanent audit/provenance records.
22. Context bootstrap works through heterogeneous Access Paths without assuming one environment.
23. Retrieval Implementation A and B satisfy the same Context Requirement / governed outcome.
24. Context provenance does not store credentials/secrets.

Where useful, the context validator should cross-check existing machine definitions from:

- lifecycle;
- capability;
- authority.

Do not validate prompt prose formatting merely to have another CI job.

---

# 19. Issue #12

If `context-integrity` is implemented, update existing open issue #12 to track:

- `lifecycle-integrity`;
- `capability-integrity`;
- `authority-integrity`;
- `context-integrity`.

Do not create a second repository-governance issue for the same concern.

Keep #12 OPEN.

Do not claim any check is merge-required until repository protection/rules actually enforce it.

Closure still requires an intentionally failing applicable integrity check to be prevented from merging.

---

# 20. Issue #6

Keep issue #6 OPEN.

L1-G may add:

- Context Requirement semantics;
- bootstrap/discovery semantics;
- reconstruction/resumption semantics.

Do NOT solve the full developer/agent working-environment experience.

Do not mandate:

- Portal;
- IDE;
- CLI;
- Dev Container;
- local daemon;
- agent host;
- one bootstrap mechanism.

Preserve:

> **AE should require interface parity, not environment uniformity.**

---

# 21. Decision-record grouping

Do NOT create 21 Decision Records.

Use the minimum durable grouping that preserves consequential rationale and future supersession.

A likely structure is approximately:

1. system-owned knowledge/context/memory semantics + Context Requirement + fresh-agent reconstruction + no generic Knowledge Item;
2. context provenance / Handoff / currentness / authoritative-source conflict / security semantics;
3. bootstrap / bounded context selection / retrieval portability;
4. machine-readable context model / `context-integrity` ADR.

Exact grouping may change if implementation cohesion indicates a better structure.

Do not silently rewrite historical L1-B/C decisions; later DRs should explicitly extend/clarify them where necessary.

---

# 22. Expected durable L1-G semantic package

After implementation, expect the minimum useful package to cover semantics equivalent to:

1. **Canonical Knowledge / Context / Memory Model**
2. **Context Requirement & Context Package Model**
3. **Context Assembly Receipt / Provenance Model**
4. **Handoff / Continuation Model**
5. **Fresh-Agent Reconstruction / Resumption Protocol**
6. **Context Bootstrap / Discovery Protocol**
7. **Bounded Context Selection Model**
8. **Currentness / Staleness / Invalidation Model**
9. **Authoritative Source / Conflict Model**
10. **Knowledge Write / Semantic Promotion Model**
11. **Context Security / Authority Integration Model**
12. **Context relationships to Contract / Plan / Baseline / Architecture / Evidence / Validation**
13. machine-readable context definitions/scenarios
14. synthetic retrieval A/B fixtures
15. context validator
16. `context-integrity`
17. minimum DRs/ADR

Do not create artifacts just to fill the list if two topics are cleaner as one coherent semantic artifact.

Do not create a giant Memory subsystem architecture.

---

# 23. Independent review requirements

After implementation, perform an independent review against:

- Contract v1.0;
- L1-A through L1-F;
- R2 versus R3 responsibility separation;
- DR-107 federated authoritative state;
- L1-C domain taxonomy/admission rules;
- L1-D exact-revision/effectivity/lifecycle semantics;
- L1-E Knowledge capability and Access Path semantics;
- L1-F authority/security/fail-closed semantics;
- issue #6 environment neutrality;
- issue #12 repository-governance status;
- explicit Human Owner approvals in this handoff.

At minimum challenge:

1. Can conversation history become authoritative merely because an agent remembers it?
2. Can vector/index/embedding state become source of truth?
3. Can summary/compaction silently replace exact Contract/Plan/Decision state?
4. Can Context Package become a shadow canonical document?
5. Can an agent continue only if hidden session memory survives?
6. Can Handoff duplicate stale facts instead of resolving current authoritative references?
7. Can stale context override newer/effective authoritative state?
8. Can a naïve “latest revision” rule override the actually effective revision?
9. Can context assembly silently arbitrate conflicting authority claims?
10. Can inaccessible information leak through derived summary/context?
11. Can `knowledge.write` make a claim canonical without semantic-owner promotion?
12. Can compaction destroy the only copy of material engineering state?
13. Can context provenance become a permanent record of every prompt without need?
14. Can missing source/revision be hidden by a confident summary?
15. Can bootstrap accidentally require one Portal/CLI/IDE/runtime?
16. Can two materially different retrieval architectures satisfy the same Context Requirement?
17. Can context-size/token-window assumptions become canonical requirements?
18. Can provider-owned knowledge be duplicated into AE and become ambiguous co-truth?
19. Can continuing and replacement actors reach materially different governed understanding from the same authoritative state without detection?
20. Does consequential-use provenance remain sufficient without creating a new A2 Context Provenance record?
21. Does Context Requirement add useful semantic precision without becoming an orchestration/retrieval algorithm?

Correct material findings before merge.

If implementation reveals a genuine Contract contradiction or new A1/A2 identity need, stop and surface it rather than silently broadening the approved model.

---

# 24. Scope guardrails

Do NOT introduce:

- Kestrel material;
- canonical vector DB/RAG implementation;
- canonical memory database;
- generic Knowledge Item/Memory Record entity;
- one agent framework;
- one model/context-window strategy;
- Portal/CLI/IDE requirement;
- detailed developer-experience solution for issue #6;
- standards applicability algorithm;
- detailed downstream metrics/learning design;
- universal prompt logging;
- hidden source-of-truth copies.

Use open interfaces and organization implementation choice below canonical semantics.

---

# 25. GitHub authorization

The Human Owner has approved the L1-G recommendations.

You are authorized to implement L1-G.

Proceed with the normal repository workflow:

```text
branch from current main
→ semantic artifacts
→ machine-readable context protocol/scenarios
→ portability fixtures
→ context validator
→ context-integrity CI
→ minimum DRs/ADR
→ update issue #12 if context-integrity is introduced
→ keep issue #6 open
→ independent review
→ correct material findings
→ PR
→ verify applicable CI on exact PR head
→ merge
```

Do not modify or merge `ae-session-relay` into `main`.

---

# 26. Closure / next handoff requirement

After L1-G is complete and merged:

1. Independently verify the merge, exact PR head, applicable integrity jobs, issue #6, issue #12, and material review findings.
2. Determine the next genuine L1 design domain and Human Owner decision gate.
3. Write the **complete next handoff payload verbatim** to a NEW unique file under `handoffs/` on `ae-session-relay`.
4. Do not overwrite this file or any prior handoff.
5. Give the Human Owner only:
   - a very short human-readable summary; and
   - a very short copy/paste block containing the next handoff title, repository, branch, and exact path.

Follow `handoffs/README.md`.
