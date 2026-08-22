# L1-G — Canonical Knowledge / Context / Memory Model

**Status:** Human Owner-approved L1-G semantic baseline  
**Authority:** Contract v1.0; DR-107–119; L1-C domain semantics; Human Owner L1-G approval  
**Scope:** Provider-neutral knowledge, context, continuation, and reconstruction semantics. This artifact does not prescribe a vector database, RAG stack, memory service, agent framework, model context strategy, conversation store, Portal, CLI, or centralized memory runtime.

## 1. Central principle

> **Canonical AE treats memory as a system property, not a central memory database.**

The AE System remembers because durable state has authoritative owners, durable references survive sessions, retrieval can reconstruct relevant information, handoffs preserve continuation state, and material discoveries are promoted to the correct durable semantic owner.

> **The agent does not own memory; the system owns memory. Agents read and write under governed rules.**

System ownership means responsibility for persistence, source authority, retrieval, continuation, provenance, reconstruction, and promotion. It does not mean one physical data store.

## 2. R2 and R3 separation

- **R2 Durable Engineering State, Identity & Traceability** governs semantic ownership, authoritative source, identity, revision, provenance, and durable relationships.
- **R3 Context & Knowledge Coordination** resolves and assembles bounded context, coordinates retrieval, handoff, continuation, reconstruction, and promotion to R2-governed owners.

R3 may retrieve, summarize, index, cache, and assemble. R3 does not become the owner of Contract, Plan, Architecture, Evidence, Authority, provider-owned state, or other R2-governed truth merely because it presents that state to an actor.

## 3. Six semantic layers

### 3.1 Authoritative durable engineering state

Examples include Contract, Plan, Product/System Baseline, Architecture Model, Decisions/ADRs, Evidence, Validation, Authority state, Work references, OEB/Profile state, and provider-owned authoritative properties.

Authority is determined by DR-107 and the owning domain. Knowledge-provider storage is not automatically authoritative.

### 3.2 Durable reference / knowledge state

Durable documentation, Learning Records, standards/policy references, externally authoritative resources, and similar information may be stored or referenced through the Knowledge capability. Its authority is independently determined.

### 3.3 Continuation state

Handoff Record [A2] and other approved durable continuation anchors preserve what another actor needs to continue responsibly.

### 3.4 Derived retrieval state

Search indexes, embeddings, vector stores, caches, generated summaries, projections, ranking state, and similar navigation/retrieval aids are derived. They may accelerate retrieval but do not become authoritative merely because they are useful or machine-readable.

### 3.5 Bounded current context

Context Package [D] is a purpose-specific derived assembly for a current actor/action/task/decision. It is disposable and reconstructable.

### 3.6 Ephemeral actor/session state

Conversation state, scratch work, transient tool state, L4 micro-plans, and temporary reasoning/session context are ephemeral unless material information is promoted to the proper durable owner or Handoff.

## 4. No generic canonical memory object

Canonical AE does not introduce a generic `Knowledge Item`, `Memory Record`, `Memory Store`, or universal shadow state repository.

Material engineering state already has semantic owners. If a later durable concept independently passes the L1-C admission test, that specific type may be introduced by a later decision.

A generic memory bucket would create ambiguous co-truth and weaken the source-ownership model.

## 5. Derived does not mean unimportant

Derived retrieval/context state can be operationally important and may need integrity, provenance, security, and currentness controls. But operational importance does not change its authority category.

A Context Package, vector hit, generated summary, or cached fact can be wrong, stale, unauthorized, or incomplete even when produced by a trusted AE implementation.

## 6. Resumability invariant

> **Loss of actor/session-local context must not prevent an appropriately authorized replacement actor from reconstructing the material governed state necessary to continue the work.**

No material engineering state may exist only in private conversation/session memory.

Replacement does not require identical prose, prompt text, token context, reasoning, or supporting retrieval results. It requires materially equivalent governing understanding from authoritative state.

## 7. Compaction invariant

> **Compaction is not canonical state.**

Before system-managed context is intentionally discarded or compacted, material state that would otherwise be lost must already be promoted to its durable semantic owner or an appropriate Handoff/continuation record.

Automatic actor/session loss must also be survivable because material state should not have been session-only in the first place.

## 8. Technology neutrality

Conforming implementations may use direct structured reads, repositories, document systems, search engines, databases, vector/RAG retrieval, knowledge services, caches, generated summaries, or combinations of them.

Canonical conformance depends on reconstruction and governed outcomes, not on retrieving identical text through identical technology.
