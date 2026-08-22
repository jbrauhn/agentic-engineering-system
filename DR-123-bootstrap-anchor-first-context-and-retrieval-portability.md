# DR-123 — Bootstrap discovery, anchor-first context, and retrieval portability

**Status:** Accepted  
**Scope:** L1-G Knowledge / Context / Memory

## Decision

Adopt a technology-neutral **Context Bootstrap / Discovery Protocol** so a supported Access Path can deterministically discover the applicable AE implementation, release, OEB/Profile, actor/authority context, work scope, governing artifacts, Capability Bindings/Access Paths, continuation state, and Context Requirement before bounded context is assembled.

Context assembly follows the semantic order **anchor-first, relevance-expanding**: required governing anchors first, then current work/dependencies, Architecture neighborhood, material Decisions/Evidence/Handoff, then supporting knowledge until bounded-context constraints are reached.

Conformance is based on equivalent governed reconstruction, not identical retrieved text. Materially different retrieval architectures can conform when they resolve the same required governing anchors, authority restrictions, conflicts/blockers, and required dispositions.

## Rationale

This gives agents and Humans deterministic entry/reconstruction semantics without canonizing Portal, CLI, IDE, RAG, vector search, one environment, or one retrieval algorithm.

## Consequences

- issue #6 remains open for full working-environment experience;
- Bootstrap Descriptor may exist as B state but no Engineering Environment Profile is added;
- relevance algorithms cannot displace mandatory governing anchors;
- retrieval portability can be demonstrated mechanically across different implementations.
