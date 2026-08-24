# DR-109 — Separate logical identity from exact revision and preserve immutable history

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

AE decisions, Plan Reviews, evidence interpretation and Validation must remain reconstructable after canonical entities change. A single mutable “current object” identity would make later actors unable to know exactly which Contract, Plan, Baseline, architecture, binding, or implementation state was approved or judged.

DR-107 additionally requires deterministic authoritative-source semantics across distributed systems.

## Decision

Canonical AE separates:

1. **logical identity** — enduring identity of an A1 entity;
2. **exact revision identity** — precise revision/state of a revisioned entity;
3. **optional human-readable version label** — presentation/release convenience only.

When authority, approval, review, evidence interpretation, or Validation depends on exact state, relationships must reference the **exact revision**.

L1-C does not mandate Git hashes, database IDs, UUIDs, semantic versioning, event sourcing, content-addressing, or another physical identity mechanism.

### Mutability classes

Canonical AE distinguishes:

- **versioned governed entity**;
- **operational stateful entity**;
- **issued immutable record**;
- **derived view/projection**;
- **ephemeral operating state**.

Approved/baselined revisions are immutable. Issued judgments/history are not destructively rewritten.

Change/correction uses a new revision, correcting/superseding record, explicit correction, or new judgment as semantically appropriate.

### Evidence history

An issued Evidence Record preserves what evidence existed and its provenance/context at issuance. Later determination that the evidence is stale, invalid, superseded, incomplete, or inappropriate does not rewrite the historical record; later assessment is represented explicitly.

### Small shared traceability mechanism

A1/A2 objects share only the common semantics needed for traceability—canonical type, logical/record identity, revision where applicable, authoritative-source declaration/reference, and provenance—with additional metadata only where semantically meaningful.

This is not a mandatory inheritance/base-class implementation.

### Typed relationships

Traceability uses explicit typed semantic relationships rather than relying on filenames, directory nesting, prose, or provider hierarchy.

Relationships are normally subordinate semantic edges rather than global entities. Exact-revision endpoints are required where relationship truth depends on exact state.

## Alternatives considered

### One mutable object/current version

Simpler operationally but loses exact historical targets for approvals/reviews/Validation and encourages destructive rewriting.

### Mandate an event-sourced/content-addressed identity architecture

Provides strong historical integrity but improperly freezes an implementation technology in the Canonical Core.

### Logical identity + revision identity + immutable issued history — selected

Preserves exact governance and portability without dictating persistence technology.

## Consequences

1. L1-D lifecycle design must preserve revision exactness at gates/transitions.
2. machine-readable schemas must eventually validate revision-specific references where required.
3. Plan representations and Baseline Manifests must be relatable to exact canonical revisions.
4. issued records can be corrected/superseded but not silently rewritten.
5. fresh agents can reconstruct what was actually approved/reviewed/validated rather than only current state.
6. DR-107 authoritative-source declarations remain separate from identity: knowing an ID does not itself establish which source is authoritative.

## Traceability

- Contract v1.0: immutable approved Contract behavior, traceability, evidence/Validation requirements.
- DR-012/013 — approved Contract immutability/change proposals.
- DR-034 — Plan Review exactness/re-review.
- DR-080–083 — Verification/Validation semantics.
- DR-107 — federated authoritative state.
- L1-C Identity / Revision / Provenance Baseline.
- L1-C Artifact Mutability / Record Semantics.
- L1-C Canonical Relationship / Traceability Model.