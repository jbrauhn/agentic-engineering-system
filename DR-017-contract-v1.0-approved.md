# DR-017 — Contract v1.0 is the authoritative Part 1 baseline

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Decision

Agentic Engineering System **Contract v1.0** is approved as the authoritative Contract for Part 1 of the Canonical Agentic Engineering System.

The previously reviewed Contract v0.9 state is superseded as a proposal and is not authoritative.

The approved Contract establishes the invariant Goal, Spec, Non-Goals, Proof, portability principle, Part 1 distribution concept, and Contract change-control boundary.

## Final Goal amendment

The approved Goal states that AE shall use AI agents to substantially increase engineering speed, scale, and automation:

> **without sacrificing—and where evidence supports it, improving—engineering quality.**

Quality is therefore protected and measured. AE does not claim that every implementation automatically improves quality.

## Consequences

1. Agents may not silently change Goal, Spec, or Proof.
2. Any material Contract change requires a versioned Contract-change proposal and Human Owner approval.
3. Lower-level architecture, standards, tooling, provider, context, orchestration, protocol, and implementation choices may evolve without reopening the Contract when they do not change fundamental AE meaning.
4. Design work shall use the following test when deciding whether a matter belongs in the Contract:

   > **If evidence later shows a better way to do this, would changing it alter what Agentic Engineering fundamentally means?**

5. C4 remains an adopted lower-level AE decision unless separately superseded; it is not frozen as an immutable Contract requirement.
6. Fresh-agent continuation remains a supported design pattern, not a Contract invariant. Durable system-owned state is the invariant.
7. Part 1 shall produce a versioned distribution composed conceptually of:
   - Canonical Core;
   - Adoption Starter Pack;
   - Executable / Reference Layer.
8. Kestrel remains outside Part 1 input and is not used to shape the generic canonical design.

## Traceability

- Authoritative artifact: `CONTRACT.md`
- Related prior decisions: DR-010 through DR-016, DR-040 through DR-043, DR-050 through DR-052, DR-060 through DR-062, DR-070 through DR-074, DR-080 through DR-083, DR-090 through DR-094, DR-101, DR-105.
- Architecture-specific decisions remain subordinate to the Contract and may be superseded independently where appropriate.
