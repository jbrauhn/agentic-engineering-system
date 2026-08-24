# DR-121 — System-owned memory, Context Requirements, and reconstructable actors

**Status:** Accepted  
**Scope:** L1-G Knowledge / Context / Memory

## Decision

Canonical AE treats memory as a **system behavior**, not a central memory store.

This decision explicitly extends/clarifies the L1-C subordinate/derived catalog with Context Requirement [B] and later L1-G subordinate context semantics; it does not rewrite the L1-C A1/A2 admission rule or promote Context Package beyond D.

The system owns responsibility for authoritative durable state, durable references, continuation, retrieval, reconstruction, provenance, and semantic promotion. Agents do not own durable engineering memory.

Introduce **Context Requirement [B]** to specify what governing/operational/supporting information must be resolvable for a purpose before governed work can proceed correctly.

Preserve **Context Package [D]** as derived/disposable/reconstructable. Do not add a generic Knowledge Item, Memory Record, or Memory Store canonical entity.

Continuing agents are allowed, but loss of actor/session-local context must not prevent an appropriately authorized replacement actor from reconstructing materially equivalent governing understanding from system-owned state.

## Rationale

A storage-centric memory model would either canonize one technology or create shadow truth. A context-reconstruction model preserves portability while making the Contract's system-owned-memory invariant testable.

## Consequences

- no material state may exist only in private session memory;
- summaries/indexes/vector state remain derived;
- context quality can be tested through Context Requirements rather than retrieval implementation;
- R2 remains owner of durable engineering truth while R3 coordinates retrieval/context;
- future implementation may use diverse storage and retrieval technologies without redefining AE.
