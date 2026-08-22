# Handoff: L1-F Closure and L1-G Knowledge / Context / Memory Design Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then follow `handoffs/README.md` for the next relay handoff.

---

# 1. Current authoritative repository state

L1-F — Authority, Policy & Enforcement is complete, independently reviewed, machine-validated, and merged to `main`.

## Merge record

- PR: **#14 — Establish L1-F authority, policy, and enforcement baseline**
- PR head reviewed/tested: `ac286c134f0f551a7633195cf8846eab4ac5c64e`
- Merge commit on `main`: **`371b6dbdf07fa5fa9f970424748dfab1e136ea25`**
- Merge completed: 2026-08-22

All three applicable PR integrity jobs passed on the exact PR head before merge:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`

`authority-integrity` passed **36 semantic authority scenarios + 4 portability cases**.

Repository protection remains a known governance gap:

- `main` is still not branch-protection/ruleset-enforced for these jobs;
- successful jobs must not be described as merge-required yet;
- issue #12 remains OPEN and tracks this.

No Kestrel material was introduced.

---

# 2. L1-F durable artifacts now on `main`

## Semantic artifacts

1. `L1-F_CANONICAL_AUTHORITY_MODEL.md`
2. `L1-F_AUTHORIZATION_REQUEST_CONTEXT_MODEL.md`
3. `L1-F_OPERATIONAL_AUTHORITY_MODEL.md`
4. `L1-F_DECISION_AUTHORITY_MODEL.md`
5. `L1-F_AUTHORITY_ASSIGNMENT_MODEL.md`
6. `L1-F_POLICY_EVALUATION_PRECEDENCE_MODEL.md`
7. `L1-F_DELEGATION_SELF_ESCALATION_GUARDRAILS.md`
8. `L1-F_DISTRIBUTED_ENFORCEMENT_PEP_BYPASS_MODEL.md`
9. `L1-F_AUTHORITY_SOURCE_OF_TRUTH_PROVENANCE.md`
10. `L1-F_OEB_PRODUCT_AUTHORITY_SPECIALIZATION.md`
11. `L1-F_AUTHORITY_CAPABILITY_LIFECYCLE_RELATIONSHIP_VIEWS.md`

## Decision records

- `DR-117-authority-semantics-and-authority-assignment.md`
- `DR-118-policy-evaluation-validity-and-self-escalation.md`
- `DR-119-distributed-enforcement-bypass-and-authority-provenance.md`
- `ADR-004-machine-readable-authority-and-integrity.md`

## Machine-readable / executable reference artifacts

- `authority_protocol.json`
- `authority_scenarios.json`
- `authority_portability_fixtures.json`
- `validate_authority.py`
- `.github/workflows/authority-integrity.yml`

---

# 3. Final L1-F canonical definitions

## Entitlement

> **A technically enforceable permission/capability available to an authenticated identity within a provider/system.**

Entitlement is a technical prerequisite. It is not proof of AE authority.

## Operational Authority — OA

> **Operational Authority is the effective scoped authority of an actor to perform or request one or more operational canonical AE actions against specified resources/context under applicable conditions.**

OA answers:

> **May this actor perform this operation in this governed work context?**

OA is an effective semantic result, not one storage mechanism.

It may be established through:

- Authority Assignment [A2];
- externally authoritative assignment/reference;
- dynamic policy derivation;
- relationship/task/resource policy;
- another reconstructable authoritative mechanism.

## Decision Authority — DA

> **Decision Authority is the effective scoped authority of an actor to make or approve a governed decision of a specified decision class.**

DA answers:

> **May this actor decide this question?**

DA does not itself grant provider execution permission.

## Authority Decision [A2]

> **An immutable durable governance record showing that an actor with applicable DA exercised that authority against an exact target/scope/revision.**

Authority Decision is an exercise of DA, not the DA itself.

## Policy decision

Final authority/policy evaluation uses:

- `PERMIT`
- `DENY`
- `INDETERMINATE`

Subordinate policy sources may use `NOT_APPLICABLE`.

For protected operations:

> **INDETERMINATE is never permission.**

## Policy Enforcement Point — PEP

> **A mechanism at or near a protected boundary that prevents the protected effect from occurring unless applicable authorization requirements are satisfied and that enforces required authorization conditions.**

Policy decision ≠ PEP enforcement.

---

# 4. Policy result versus runtime outcome

L1-F preserves the L1-D runtime vocabulary:

- `ALLOWED`
- `DENIED`
- `BLOCKED`

Canonical mapping:

```text
PERMIT
+ required technical prerequisites
+ applicable entitlement
+ applicable enforcement
+ provider operability
→ ALLOWED
```

```text
DENY
→ DENIED
```

```text
INDETERMINATE
→ BLOCKED
```

```text
PERMIT
+ missing required technical entitlement
→ BLOCKED
```

Absence of a grant is not automatically INDETERMINATE.

If authoritative policy deterministically defines:

`no qualifying authority = DENY`

then result = DENY / DENIED.

If required authority cannot be reliably established or policy conflict remains unresolved:

INDETERMINATE / BLOCKED.

---

# 5. Authority Request / Requirement model

L1-F introduces subordinate:

- **Authorization Request Context [B]**
- **Authority Requirement [B]**

Principle:

> **Common authorization semantics; operation-specific required context.**

Common request facts can identify as applicable:

- request/correlation identity;
- actor;
- authenticated identity;
- canonical operation;
- target resource/decision target;
- organization/Product-System scope;
- evaluation time;
- Capability Binding/binding plan;
- Access Path.

Governed-work context can include:

- AE Loop;
- Execution Increment;
- Executable Task;
- exact Contract revision;
- exact Plan revision/review scope;
- Product/System Baseline revision;
- exact OEB revision;
- exact Product/System Profile revision.

Authority/security context can include:

- provider entitlement;
- OA basis;
- DA basis;
- Authority Assignment;
- Authority Decision;
- policy sources;
- classification/environment/risk;
- conditions/obligations;
- validity;
- delegation;
- revocation.

Every L1-E protected operation resolves to an L1-F Authority Requirement through the machine protocol's canonical protected-operation default plus any future operation-specific override.

Technical entitlement is **binding-determined**, not assumed to have one universal provider shape.

---

# 6. Authority Assignment [A2]

L1-F introduces:

> **Authority Assignment [A2]**

for cases where authority is explicitly issued, assigned, or delegated as independently meaningful governed authority state.

It may represent:

- Operational Authority Assignment;
- Decision Authority Assignment;
- Delegated Authority Assignment.

Minimum semantics support as applicable:

- assignment identity;
- authority kind;
- holder/subject;
- issuer/authoritative source;
- operations or decision classes;
- resource/scope;
- organization/Product-System;
- Loop/task scope;
- conditions;
- valid-from/valid-until;
- delegation semantics;
- source assignment;
- provenance.

Issued history is non-destructive.

Expiration/revocation/supersession does not rewrite what was issued.

## L1-C relationship

DR-117 explicitly **extends the L1-C A2 catalog** with Authority Assignment.

The L1-C entity-admission rule is unchanged; the historical L1-C baseline is not silently rewritten.

Primary logical responsibility: R4.  
Collaborators: R2 for durable identity/traceability; R5 where assignments participate in protected capability use.

## Federation rule

Do not create an AE-owned shadow copy of every external IAM grant.

Apply DR-107:

- preserve semantic identity;
- know authoritative source;
- preserve exact assignment/reference when required;
- preserve scope/validity/provenance/relationships;
- allow physical authoritative state to remain external.

Effective OA/DA may also be dynamically derived; an Authority Assignment artifact is not mandatory for every conforming authority model.

---

# 7. Canonical Human-reserved Decision Authority

L1-F deliberately **does not add new universally Human-reserved decision classes** beyond adopted higher authority.

Contract v1.0 explicitly preserves Human authority over:

- engineering intent;
- material risk acceptance;
- consequential tradeoffs;
- Contract approval;
- Contract change;
- any future decision class explicitly assigned by higher canonical authority to Human Decision Authority.

The machine protocol checks this exact five-class baseline and fails if L1-F silently expands it.

Organizations may reserve additional decisions to Humans based on regulation, classification, risk, safety, product criticality, architecture governance, production impact, business policy, etc.

Those are organization-reserved Human DA, not universal Canonical AE Human reservations.

Precedence:

```text
Canonical AE authority constraints
→ Organization authority baseline
→ Product/System specialization
→ Loop/task context
```

No silent weakening.

---

# 8. Policy / precedence / conditions

Canonical AE does not prescribe one policy language or combining algorithm.

Requirements:

1. Canonical constraints cannot be weakened downstream.
2. Organization/Product policy precedence or combination is deterministic.
3. Product/System specialization may tighten/narrow but not silently weaken mandatory organization controls.
4. Exceptions, where allowed, are explicit, authorized, scoped, versioned/provenanced, and time/condition bounded where applicable.
5. No unresolved applicable policy conflict can produce PERMIT.

Thus:

`unresolved applicable conflict → INDETERMINATE → BLOCKED`.

A PERMIT may carry enforceable conditions/obligations such as:

- environment restriction;
- exact approval reference;
- time boundary;
- evidence/audit requirement;
- resource scope.

No universal obligation DSL was created.

Required obligations must reach and be enforced by an applicable PEP.

---

# 9. Least privilege / validity / revocation

Approved principle:

> **Authority and technical entitlement should use the smallest enforceable scope sufficient to perform the authorized work reliably and safely.**

Do not require absurd per-call token granularity.

But broad administrator access cannot be accepted merely for convenience when a meaningfully narrower enforceable scope exists.

Preserve:

```text
credential lifetime
≠ entitlement lifetime
≠ OA lifetime
≠ DA lifetime
```

Authority supports as applicable:

- not-yet-valid;
- active;
- expired;
- revoked;
- superseded;
- invalidated by condition change.

A valid credential does not extend expired/revoked authority.

Credential refresh does not silently renew OA/DA.

Later revocation affects future effective authority; it does not rewrite historical authorization truth.

---

# 10. Delegation / self-escalation

Delegation is optional.

If supported:

- explicit;
- delegator authorized to delegate;
- no amplification beyond delegable scope;
- resource/operation/decision/time/conditions remain bounded;
- provenance retained;
- onward delegation only when explicitly allowed;
- Canonical Human-reserved DA cannot be delegated to AI.

Critical invariant:

> **An actor may not use the effect of an authority-changing operation to authorize that same authority-changing operation.**

Authority-changing mutations use **pre-change authoritative state**.

This covers changes to OA/DA assignments, entitlements, authority-relevant roles/groups, policy, Capability Bindings, OEB/Profile authority configuration, approval state, and PEP configuration.

Document appearance ≠ authoritative approval.

---

# 11. Distributed PEP / bypass-path model

No central PDP/PEP is canonical.

PEPs may be distributed at provider, runtime, broker, gateway, SCM, CI/CD, deployment, data/service, or other protected boundaries.

Preserve responsibility separation:

- R4 = authority/policy/decision coordination;
- R5 = binding/invocation;
- PEP = enforcement.

Approved bypass invariant:

> **Protected-operation Proof must account for materially equivalent bypass paths available to the governed actor through the identities, credentials, Access Paths, and runtime/working context in the declared protected scope.**

If the preferred governed integration denies an operation but the same governed actor/runtime can perform the materially equivalent action through an ungoverned credential/interface, enforcement Proof fails unless the alternate path is equivalently governed.

Do NOT fail because an unrelated enterprise administrator or a separate admin identity unavailable to the governed runtime exists.

If the governed actor can switch to another identity inside the runtime and bypass enforcement, that identity is relevant.

---

# 12. Federated authority source-of-truth / provenance

No central AE authority database was introduced.

Apply DR-107.

Material authority facts have determinable authoritative sources, including as applicable:

- identity;
- entitlement;
- OA;
- DA;
- Authority Assignment;
- Authority Decision;
- organization/Product policy;
- revocation;
- approval;
- PEP configuration.

Caches/projections are derived and cannot silently become co-authoritative.

If required freshness cannot be established:

`INDETERMINATE → BLOCKED`.

Authorization evaluation provenance remains subordinate **B semantics**, not a new A2 record for every authorization check.

Retention is risk/operation/policy-sensitive.

Where durable reconstruction is required, provenance can support actor/identity, operation, target, Loop/task, relevant Contract/Plan/OEB revisions, entitlement/OA/DA bases, policy sources, effective policy result, obligations, PEP, runtime result, provider effect, and Evidence references.

Do not retain credential secret material merely for provenance.

---

# 13. OEB / Product-System authority specialization

An exact OEB revision may identify/reference:

- identity sources;
- entitlement models/sources;
- OA baseline/policy;
- DA assignments/reservations;
- Human-reserved constraints;
- delegation policy;
- validity/revocation expectations;
- policy sources;
- precedence/combination semantics;
- protected-operation classes;
- PEP mappings;
- provenance/audit expectations;
- governed exception mechanisms.

OEB coordinates references; it is not the IAM/policy engine.

Product/System Profile may tighten/narrow.

It may not silently weaken Canonical Human reservations or mandatory organization/security controls.

---

# 14. L1-F machine/reference model and CI

Human semantic artifacts remain normative for meaning.

Machine/reference layer:

- `authority_protocol.json`
- `authority_scenarios.json`
- `authority_portability_fixtures.json`
- `validate_authority.py`
- `.github/workflows/authority-integrity.yml`

JSON/Python/GitHub Actions are repository/reference choices, not Canonical AE technologies.

The validator loads:

- `authority_protocol.json`
- `authority_scenarios.json`
- `authority_portability_fixtures.json`
- existing `capability_contracts.json`
- existing `lifecycle_protocol.json`

and checks cross-domain consistency.

## Authority-integrity result

PR #14 authority run passed:

- **36 semantic scenarios**
- **4 portability cases**

Coverage includes:

- explicit OA;
- dynamic OA;
- entitlement but no OA → DENIED;
- OA but missing entitlement → BLOCKED;
- INDETERMINATE → BLOCKED;
- deterministic no-grant DENY;
- expired OA with technically valid credential;
- revoked OA overriding stale cached PERMIT;
- enforceable PERMIT obligations;
- missing PEP failure;
- unresolved policy conflict;
- governed-actor bypass;
- unrelated enterprise administrator excluded from bypass scope;
- alternate runtime identity bypass;
- provider outage after PERMIT;
- Human Contract-change DA/G5;
- AI self-approval rejection;
- wrong DA scope;
- stale target;
- forged Authority Decision;
- G5 mismatch;
- expired Human DA;
- self-granted OA/entitlement/policy rejection;
- valid independently authorized authority mutation;
- delegation success/overscope/onward/Human-to-AI guardrails;
- historical authority preservation;
- external authoritative assignments without AE shadow copies.

Portability models:

**Implementation A**
- role/scoped policy;
- explicit Authority Assignment;
- provider-native entitlement.

**Implementation B**
- attribute/resource/task policy;
- dynamic OA;
- external entitlement source.

Equivalent cases produced equivalent canonical policy/runtime outcomes.

---

# 15. Independent review findings / dispositions

Material findings corrected before merge:

## Finding 1 — technical-entitlement overconstraint

Initial machine draft modeled provider entitlement as one universally shaped required field on every protected operation.

**Disposition:** changed to `BINDING_DETERMINED` technical-entitlement semantics. The resolved binding determines what technical prerequisite is applicable. Runtime still proves that missing required technical entitlement after policy PERMIT results in BLOCKED.

## Finding 2 — L1-C A2 catalog extension clarity

Authority Assignment is a legitimate new A2 type, but the old approved L1-C catalog did not list it.

**Disposition:** do not silently rewrite the historical L1-C baseline. DR-117 and the L1-F Authority Assignment artifact explicitly state that L1-F extends the A2 catalog while preserving the L1-C admission rule.

## Finding 3 — staging PEP field-name typo

An unreferenced staging blob had a suspected malformed PEP-proof field name.

**Disposition:** committed protocol uses `authority_identity_facts_consumed`; validator checks that exact field.

## Other review conclusions

- No new universal Human-reserved decision classes beyond Contract/higher authority.
- Role label remains policy context, not authority; L1-E protected operations require effective OA.
- External authoritative assignments and dynamic authority can satisfy Canonical AE without shadow IAM records.
- No unresolved policy conflict yields permission.
- PEP and policy decision remain distinct.
- Self-escalation prohibited using pre-change authority.
- Bypass scope is implementable and actor/runtime-specific.
- Later revocation preserves historical truth.
- No central PDP/PEP/authority DB became canonical.
- No policy DSL became canonical.
- Issue #6 environment neutrality preserved.
- No Contract contradiction found.

---

# 16. Open issues after L1-F

## Issue #6 — remains OPEN

**Engineering Team Interface / Working Environment — interface parity across heterogeneous development environments**

Principle remains:

> **AE should require interface parity, not environment uniformity.**

L1-F did not solve Dev Container/IDE/Portal/CLI/local daemon/agent-host design.

Access Path remains the L1-E interface hook.

## Issue #12 — remains OPEN

**Repository governance — require applicable integrity checks before main merge**

Now tracks:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`

Do not close or claim merge-enforced until repository protection/rules actually require the applicable jobs and a deliberately failing check is proven to block merge.

Current `main` remains unprotected as of L1-F closure.

---

# 17. What L1-G inherits

Proceed next to:

# **L1-G — Knowledge / Context / Memory**

This is the next genuine design domain.

L1-G inherits these higher-authority facts:

## Contract v1.0

> durable engineering knowledge and workflow state belong to the **AE System**, not one agent/model invocation/conversation.

The system supports:

- durable system-owned state;
- bounded context;
- structured handoffs;
- traceable artifacts;
- resumable work;
- replacement/continuation by another agent where useful;
- reconstruction of relevant context from canonical system state.

No one context strategy is immutable.

Invariant:

> **loss of one conversational session shall not imply loss of the engineering system's durable knowledge or workflow state.**

## L1-B responsibilities

R2 — Durable Engineering State, Identity & Traceability
- governs authoritative durable engineering state and relationships.

R3 — Context & Knowledge Coordination
- turns durable system-owned state into bounded trustworthy context usable by Humans/agents;
- supports retrieval, context assembly, structured handoffs, continuation/resumption, provenance awareness.

Important boundary:

> **R3 does not become a new source of truth merely because it assembles context.**

## L1-C domain semantics

- **Context Package [D]** — derived/disposable/reconstructable.
- **Handoff Record [A2]** — durable continuation artifact.
- **L4 micro-plan [E]** — ephemeral by default.
- material facts discovered in ephemeral work are promoted to the durable semantic owner.
- compaction is not canonical state.
- material context provenance may need durability even when the Context Package is disposable; L1-C intentionally deferred the exact mechanism to L1-G.

## L1-E Knowledge / Memory capability

Required canonical operations:

- `knowledge.read`
- `knowledge.query`
- `knowledge.write`
- `knowledge.reference`

Knowledge writes remain constrained by R2 authoritative ownership and immutability semantics.

The Knowledge capability is storage/access, not authority to rewrite approved Contracts or other authoritative records.

## L1-F authority

Context/knowledge access must honor:

- identity;
- provider entitlement where applicable;
- OA;
- policy;
- classification/environment/resource restrictions;
- protected write enforcement;
- provenance;
- fail-closed semantics where required authority cannot be established.

Do not leak secrets into context provenance merely for traceability.

## Issue #6

L1-G is likely to provide an important semantic hook for the unanswered question:

> **A Human or agent enters a supported working environment. How does it discover which AE implementation it is in and obtain the correct Contract, Plan, Product/System Baseline, architecture, policies, capabilities, authority context, and current work context?**

Do not solve the UI/CLI/IDE/runtime mechanism yet, but L1-G should define the context/bootstrap semantics an implementation must make possible.

---

# 18. Primary L1-G design question

> **What is the minimum canonical Knowledge / Context / Memory model that lets a Human or agent reconstruct trustworthy, bounded, current-enough engineering context from federated authoritative state; continue or hand off work across session/agent loss; use lossy retrieval/indexing safely; and promote material learning back into the correct durable semantic owner—without making one vector database, RAG stack, memory store, context-window strategy, agent framework, or conversational history mechanism part of Canonical AE?**

Treat this as a semantic information-flow / continuation problem, not a “which memory database?” question.

Do NOT make GitHub writes until the Human Owner approves the L1-G decision set.

---

# 19. L1-G dialectic design areas to test

The next proposal should explicitly test at least the following.

## 19.1 Durable truth versus retrieval/index memory

Preserve:

```text
Authoritative durable engineering state
≠ knowledge provider storage automatically
≠ search index
≠ vector embedding
≠ generated summary
≠ conversation history
≠ current Context Package
```

A vector index or RAG store may help retrieval without becoming source of truth.

Test how a context result resolves back to authoritative sources/revisions.

## 19.2 What “the system owns memory” actually means

Challenge whether “memory” should remain an umbrella term or be decomposed into clearer semantics such as:

- authoritative engineering state;
- durable knowledge/reference state;
- continuation/handoff state;
- derived retrieval/index state;
- bounded current context;
- ephemeral actor/session state.

Avoid anthropomorphic memory categories if they do not improve implementation precision.

## 19.3 Context Package semantics

Context Package remains [D].

Determine minimum semantics such as:

- target actor/task/Loop;
- purpose/context intent;
- selected source references;
- exact revisions where material;
- source authority/trust classification;
- assembly time;
- freshness/validity information;
- selection/exclusion rationale where useful;
- unresolved/uncertain facts;
- authorization/access constraints;
- size/budget constraints;
- reconstruction information.

Do not turn Context Package into another authoritative document.

## 19.4 Context provenance / assembly receipt

L1-C left this open.

Test alternatives:

### Candidate A
A subordinate **Context Assembly Receipt / Source Manifest [B]** attached to or referenced by a Context Package/Handoff/material output.

### Candidate B
A first-class durable Context Provenance record.

Apply the L1-C admission test.

Question:

> **Would confusing two context assemblies or losing the source/revision selection materially break governance, reproducibility, continuation, or Validation often enough to warrant independent A2 identity?**

Likely leading hypothesis: keep assembly provenance subordinate/durable-as-needed unless evidence shows independent lifecycle/identity is required.

Do not create A2 merely because provenance is useful.

## 19.5 Handoff Record semantics

Handoff [A2] is already approved.

Define its minimum continuation semantics without copying the whole world:

- work/Loop/task being continued;
- current state/position;
- exact authoritative artifact references;
- material decisions already made;
- material unresolved questions/risks;
- evidence/results that matter;
- blocked/next-action state;
- context/provenance references;
- what the receiving actor should reconstruct rather than trust from summary text.

Preserve:

> **Handoff references authoritative state; it does not replace it.**

## 19.6 Compaction / summaries

Preserve inherited principle:

> **Compaction ≠ canonical state.**

Test rules for lossy summaries:

- may assist context construction;
- must be identifiable as derived;
- must preserve/source references for material claims;
- cannot silently replace exact Contract/Plan/decision/evidence state;
- should be regenerated when stale or inconsistent.

## 19.7 Fresh agent / continuing agent / replacement

Canonical AE must support multiple context strategies.

Test whether conformance requires that a fresh authorized agent can reconstruct enough context to continue work from canonical state without hidden conversation memory.

Also preserve that continuing agents are allowed.

Do not require fresh-agent replacement every Loop.

## 19.8 Context bootstrap / entry point

Define semantics for an actor entering AE and answering:

- Which Organization-specific AE Implementation is this?
- Which Canonical AE release/OEB/Product Profile applies?
- What Loop/task am I acting in?
- What Contract/Plan/Baseline/architecture/decisions apply?
- What capabilities/Access Paths are available?
- What authority context is relevant?
- What current handoff/context state exists?

Do not prescribe Portal/CLI/IDE/MCP/bootstrap file yet.

Likely output is a canonical **context-discovery/bootstrap protocol**, not one client implementation.

## 19.9 Bounded context selection

Context cannot mean “load everything.”

Test canonical constraints for:

- relevance to current work;
- authority/source trust;
- exact revision where material;
- freshness/currentness;
- information classification/access;
- dependency/architecture neighborhood;
- evidence/decision history;
- size/token/runtime limits;
- avoiding irrelevant context overload.

Do not canonize one token budget or model context-window strategy.

## 19.10 Staleness / currentness

Define what happens when:

- source changed after context assembly;
- Plan/Contract/OEB revision changes;
- authority/policy revokes access;
- cached context has unknown freshness;
- provider/index is stale.

Potential invariant:

> **Derived context cannot override newer authoritative state.**

Decide when stale context means:

- regenerate;
- mark degraded;
- block protected action;
- another explicit disposition.

Coordinate with L1-D/L1-F fail-closed semantics without overblocking low-risk read-only reasoning.

## 19.11 Knowledge write / promotion semantics

Define how material information becomes durable engineering knowledge.

A conversation statement, scratch note, or model summary should not automatically become canonical truth.

Test a promotion path such as:

```text
ephemeral discovery
→ classify semantic owner
→ validate/authorize as required
→ write/update correct A1/A2/B object or authoritative external reference
→ preserve provenance
→ context/index can later retrieve it
```

The important question:

> **Where does this fact belong canonically?**

rather than:

> “Which memory store should remember it?”

## 19.12 Conflicting knowledge / source reconciliation

Federated authoritative state can contain conflict or stale replicas.

Define semantics for:

- authoritative source known;
- conflicting non-authoritative copy;
- two sources claiming authority for same property/scope;
- source unavailable;
- source superseded;
- uncertain/unverified information.

Do not let context assembly silently choose whichever source is easiest to retrieve.

## 19.13 Context trust labels / claim provenance

Test whether context items need canonical trust/source semantics such as:

- authoritative;
- authoritative reference;
- issued historical record;
- derived;
- external/unverified;
- stale/unknown-currentness.

Avoid creating a bloated ontology unless these labels materially protect behavior.

## 19.14 Retrieval / Knowledge capability portability

Use at least two materially different synthetic implementations:

- Implementation A: repository/docs/work-management + keyword/search index;
- Implementation B: knowledge service/vector retrieval + external canonical sources.

Both should reconstruct equivalent canonical context when given the same authoritative inputs.

Do not canonize RAG/vector search.

## 19.15 Context security / least exposure

Use L1-F authority semantics.

A context package should not expose information merely because a retrieval index contains it.

Test:

- authorized actor receives permitted sources;
- inaccessible/classified source excluded/redacted per policy;
- derived summary cannot leak restricted source content;
- stale authorization cache cannot retain access indefinitely;
- context package provenance does not store credentials/secrets.

Do not design the enterprise classification system itself.

## 19.16 Context and Validation

Validation may need exact context/provenance to know what evidence/Contract state was evaluated.

Decide when a context assembly used for a consequential judgment must be reconstructable.

Do not make every routine prompt permanently auditable.

## 19.17 Metrics / observability hook

L1-G may expose later measurement hooks such as:

- context assembly time;
- source retrieval failures;
- stale-context detections;
- context size;
- handoff/resumption success;
- missing-context replans;
- retrieval quality.

Do not steal L1-K metrics/learning design; only create necessary hooks.

---

# 20. Likely L1-G entity-admission questions

Explicitly test whether L1-G needs any new A1/A2 objects.

Current leading hypothesis:

- **Context Package remains D**.
- **Handoff Record remains A2**.
- search index/vector representation remains D/provider state.
- context assembly/source manifest likely remains B or durable subordinate provenance.
- no generic “Memory Record” should be created unless a specific independent identity/lifecycle requirement passes DR-108.

Possible genuine admission questions:

1. Does a **Context Assembly Receipt / Source Manifest** need first-class identity or only subordinate identity?
2. Does a durable **Knowledge Item** entity add value, or would it create a shadow store beside existing Contracts/Plans/ADRs/Learning/Architecture/provider-owned knowledge?
3. Is a **Context Bootstrap/Discovery Result** a D projection or does its conformance role require a durable record?

Be conservative about new entities.

---

# 21. Machine-readable context model / CI decision

Test whether L1-G should continue the staged pattern:

Human L1-G semantics
= normative for meaning.

Machine context definitions/scenarios
= conforming executable representation.

Python validator
= repository/reference implementation.

GitHub Actions
= repository CI.

Potential job:

**`context-integrity`**

Do not create a production RAG engine.

Meaningful candidate tests:

- Context Package cannot become authoritative truth.
- Handoff references exact authoritative sources rather than replacing them.
- vector/index/summary cannot be authoritative for protected exact-revision facts.
- fresh agent can reconstruct a synthetic Loop from canonical state + handoff without hidden conversation history.
- stale Contract/Plan/OEB source is detected.
- conflicting source-of-truth declarations fail or become explicit unresolved state.
- unauthorized source is excluded from context.
- derived summary cannot leak inaccessible source content.
- material durable fact is promoted to the correct semantic owner rather than generic chat memory.
- compaction loss does not destroy canonical state.
- two materially different retrieval implementations produce equivalent required canonical context.
- context bootstrap works across heterogeneous Access Paths without assuming one environment.

If `context-integrity` is added, update issue #12 to track it and keep #12 open.

---

# 22. Expected Human Owner decision areas for L1-G

Explicitly analyze at least:

1. What exactly does “the AE System owns memory” mean after L1-C/B/E?
2. What categories of state/context/memory are canonical versus derived/ephemeral?
3. What are the precise semantics of Context Package [D]?
4. What minimum context provenance must be retained?
5. Does context provenance need a new A2 record, or remain B/durable-as-needed?
6. What exact minimum semantics belong in Handoff Record [A2]?
7. How are compaction/summaries constrained?
8. What conformance requirement exists for fresh-agent reconstruction?
9. What bootstrap/discovery semantics must an actor receive on entering an AE implementation?
10. How does context selection stay bounded/relevant without one token-budget algorithm?
11. What freshness/staleness semantics are canonical?
12. When must stale/unknown context block work versus simply degrade/rebuild?
13. How are conflicting/ambiguous authoritative sources handled?
14. What trust/source labels are actually necessary?
15. How are material ephemeral discoveries promoted into durable semantic owners?
16. Should Canonical AE have a generic Knowledge Item entity at all?
17. How should Knowledge provider writes interact with R2 authoritative ownership?
18. How does context access enforce L1-F authority/classification constraints?
19. How does Context/Handoff interact with exact Contract/Plan/OEB revisions?
20. What context used for consequential Validation/decisions must be reconstructable?
21. What portability Proof demonstrates equivalent behavior across non-vector and vector/RAG implementations?
22. Should L1-G introduce machine-readable context scenarios / `context-integrity`?
23. If so, what checks are meaningful rather than prompt-format lint?
24. Does issue #12 expand to `context-integrity`?
25. What L1-G hooks partially answer issue #6 without solving the developer experience?

For each consequential choice provide:

- leading recommendation;
- strongest credible alternative;
- tradeoff/consequence;
- Contract / DR / L1-A–F traceability.

Do not make GitHub writes until the Human Owner approves the L1-G decision set.

---

# 23. Expected durable L1-G artifacts after approval

Do not freeze filenames yet, but expect semantics equivalent to:

1. **Canonical Knowledge / Context / Memory Model**
2. **Context Package / Context Assembly Model**
3. **Context Provenance / Source Manifest Model**
4. **Handoff / Continuation Model**
5. **Fresh-Agent Reconstruction / Resumption Protocol**
6. **Context Bootstrap / Discovery Model**
7. **Authoritative Source / Retrieval / Conflict Model**
8. **Freshness / Staleness / Invalidation Model**
9. **Knowledge Write / Promotion Model**
10. **Context Security / Authority Integration Model**
11. **Context / Architecture / Contract / Plan / Evidence relationship views**
12. **machine-readable context definitions/scenarios** — if approved
13. **synthetic retrieval implementation A/B fixtures** — if approved
14. **context validator + valid/invalid fixtures** — if approved
15. **`context-integrity` CI** — if approved
16. **minimum necessary DRs/ADRs**

Do not create a giant “memory subsystem” simply to fill the artifact set.

---

# 24. Independent review expectations after L1-G implementation

Review from at least:

- Contract fidelity;
- R2 versus R3 responsibility separation;
- durable authoritative-state ownership;
- context provenance;
- fresh-agent resumability;
- provider/retrieval portability;
- L1-F authority/security;
- L1-E Knowledge capability compatibility;
- L1-D exact-revision/lifecycle compatibility;
- Handoff semantics;
- issue #6 environment neutrality;
- implementation-team usability.

Specific failure tests:

1. Can a conversation transcript become authoritative merely because an agent remembers it?
2. Can a vector index or embedding become the source of truth?
3. Can a summary silently replace an exact Contract/Plan/decision revision?
4. Can Context Package become a new shadow canonical document?
5. Can a fresh agent continue only if it has hidden prior-session memory?
6. Can a Handoff duplicate stale facts instead of resolving authoritative references?
7. Can stale context override newer authoritative state?
8. Can context assembly choose between conflicting authoritative claims without explicit resolution?
9. Can an unauthorized source leak through a derived summary?
10. Can a model write a claim into a generic “memory” store and thereby make it canonical?
11. Can compaction destroy the only copy of material engineering state?
12. Can context provenance become an audit swamp where every prompt is permanently stored without need?
13. Can a missing source/revision be hidden by a confident generated summary?
14. Can context bootstrap accidentally require one Portal/CLI/IDE/runtime?
15. Can two materially different retrieval architectures produce equivalent canonical context?
16. Can context size/model-window constraints accidentally become Canonical AE requirements?
17. Can provider-owned knowledge state be copied into AE and become ambiguous co-truth?
18. Can a continuing agent and a fresh replacement agent reach materially different governed understanding from the same canonical state without the discrepancy being detectable?

---

# 25. Next response required from receiving session

Before any GitHub write, give the Human Owner the **L1-G dialectic design proposal** covering:

1. precise Knowledge / Context / Memory definitions;
2. authoritative state versus retrieval/index/summary boundaries;
3. Context Package semantics;
4. context provenance/source-manifest recommendation and entity-admission decision;
5. Handoff Record minimum semantics;
6. fresh/continuing/replacement-agent model;
7. bootstrap/discovery protocol;
8. bounded context selection model;
9. freshness/staleness/invalidation semantics;
10. source conflict/authority handling;
11. knowledge write/promotion model;
12. security/authority integration;
13. context relationship to Contract/Plan/Baseline/Architecture/Evidence/Validation;
14. portability proof across materially different retrieval implementations;
15. machine-readable context / `context-integrity` recommendation;
16. issue #12 recommendation;
17. issue #6 semantic-hook treatment;
18. genuine Human Owner decision set;
19. durable L1-G artifacts those decisions would produce.

Do not make GitHub writes until Human Owner approval.

---

# 26. Relay protocol reminder

After L1-G work is eventually completed, write the complete next handoff to a **new unique file** under `handoffs/` on `ae-session-relay`.

Do not overwrite this file.

Do not merge `ae-session-relay` into `main`.
