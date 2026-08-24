# DR-107 — AE uses federated authoritative state with explicit semantic ownership

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Contract v1.0 requires durable system-owned memory/state, stable identifiers, versioning/provenance, relationships/traceability, and reconstructable context. DR-019 permits distributed implementation across existing organization systems and External Capability Providers.

A single canonical AE database would simplify consistency but would force organizations to duplicate or migrate authoritative enterprise state and would bias AE toward a centralized product topology.

The opposite extreme—allowing truth to be spread across Git, Work Management, chat, vector stores, agent memory, policy systems, and other providers without explicit ownership—would make state ambiguous and violate the system-owned-memory requirement.

## Decision

AE shall use **federated authoritative state with explicit semantic ownership**.

> **For each material canonical state element and declared scope/version, a conforming AE implementation must be able to determine the authoritative source at that point in time.**

The Canonical Core does not require one physical database or state repository.

A conforming implementation shall define, as applicable, for material state:

- canonical state type/category;
- logical governing responsibility;
- stable identity/reference;
- authoritative source for the declared scope/property/version;
- allowed writers / authority;
- current-version semantics;
- provenance expectations;
- material relationships/references;
- conflict/precedence/reconciliation behavior;
- synchronization expectations where multiple representations participate;
- behavior when authoritative state cannot be established.

Replicas, indexes, projections, search stores, caches, synchronized copies, vector representations, summaries, and context packages may exist but shall not silently become co-authoritative.

> **One semantic ownership model; potentially many physical systems of record.**

## Alternatives considered

### One canonical AE state repository

**Advantages:** simpler querying, consistency, schema enforcement, audit, and context reconstruction.

**Disadvantages:** centralizes topology, duplicates existing authoritative systems, creates synchronization burden, and can force organizations to migrate ownership unnecessarily.

### Unconstrained distributed state

**Advantages:** easiest integration with existing tools and minimal central design.

**Rejected:** creates ambiguous truth, stale context, unclear precedence, and hidden dependence on conversational/agent memory.

### Federated authoritative state with explicit semantic ownership — selected

Preserves portability while making source-of-truth, identity, provenance, and reconciliation deterministic.

## Consequences

1. R2 governs semantic state identity/traceability but is not a central database.
2. Property-level authority may be distributed: e.g., Work Management can own selected workflow fields while Source Control owns versioned artifacts and R4 governs decision state.
3. L1-C must design domain/artifact semantics that can express stable identity, versions, relationships, and authoritative-source declarations without assuming one storage technology.
4. R3 context construction must remain anchored to authoritative/provenance-bearing state rather than treating embeddings, summaries, or conversation as independent truth.
5. Protected actions/transitions shall fail closed where required authoritative state or authority cannot be established.
6. Later capability/adoption design must classify provider outages, stale replicas, missing interfaces, and unresolved conflicts for Loop operability and conformance impact.
7. Implementations must define deterministic precedence/reconciliation for material disagreement between participating systems.

## Traceability

- Contract v1.0: Spec §3, §11, §12; portability and traceability requirements.
- DR-019 — logical/distributed AE implementation.
- DR-106 — seven canonical logical responsibilities.
- L1-B State Ownership / System-of-Record Baseline.