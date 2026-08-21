# ADR-001 — Represent Canonical Core responsibilities logically; use C4 Containers for concrete topology

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner  
**Related decision:** DR-021 remains adopted; this ADR clarifies its application and does not supersede it.

## Context

DR-021 adopts C4 as the shared visual architecture discipline. L1-A established the Organization-specific AE Implementation as the operational C4 system of interest.

DR-019 and L1-B establish that Canonical AE does not mandate one physical runtime topology. The seven L1-B responsibilities are semantic duties that may be combined or distributed across organization mechanisms.

Calling those responsibilities C4 Containers would imply separately runnable/deployable applications or data stores that Canonical AE has not required.

## Decision

The **Canonical Core** shall use:

- the existing C4 System Context for the logical operational AE implementation;
- a normative **logical responsibility architecture** for R1–R7;
- other logical/domain/sequence views as later design requires.

The seven canonical logical responsibilities shall **not** be labeled C4 Containers unless a later concrete implementation actually realizes them as such.

The **Executable / Reference Layer** shall create a genuine C4 Container view once its concrete runnable/deployable topology exists.

**Adoption guidance** shall require or strongly support a concrete implementation topology view for an Organization-specific AE Implementation once its actual mechanisms are known. Under the adopted C4 discipline, C4 Container is the default where actual applications/services/data stores fit C4 Container semantics. Complementary views may be used for material non-software/process relationships rather than mislabeling them as Containers.

Concrete architecture shall trace actual mechanisms/components back to the canonical logical responsibilities they realize.

## Alternatives considered

### Define canonical “logical Containers”

This would provide one consistent C4-looking decomposition and let adopters combine/split the boxes.

**Rejected:** it stretches C4 terminology and subtly creates a canonical deployment architecture from what are intended to be topology-neutral responsibilities.

### Avoid C4 below System Context entirely

This would eliminate terminology risk.

**Rejected:** concrete reference and organization implementations will have real software topology for which C4 Container views are useful and already adopted.

## Consequences

1. Canonical responsibility diagrams are explicitly logical architecture, not deployable topology.
2. Reference implementation C4 views remain conforming examples rather than normative AE semantics.
3. Organization-specific concrete views can differ materially while tracing to the same R1–R7 responsibilities.
4. A change in reference components does not reopen Contract v1.0 or DR-106 unless canonical responsibility meaning changes.
5. Current Mermaid diagrams are rendering conveniences; they do not establish Mermaid as a canonical architecture technology.
6. DR-021 remains in force and is clarified rather than superseded.

## Traceability

- DR-019 — logical/distributed AE implementation.
- DR-021 — adopted C4 architecture discipline (inherited Decision Register).
- DR-106 — seven canonical logical responsibilities.
- L1-A Architecture Context Views.
- L1-B Architecture Representation Strategy.
