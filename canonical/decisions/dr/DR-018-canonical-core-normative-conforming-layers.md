# DR-018 — Canonical Core is normative; distribution support layers and implementations conform

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Part 1 must publish something an implementation team can actually receive and use. The approved Contract defines three related distribution layers: Canonical Core, Adoption Starter Pack, and Executable / Reference Layer.

Without an authority distinction between those layers, a convenience in a starter template or reference implementation could accidentally redefine what Agentic Engineering fundamentally means.

## Decision

The **Canonical Core is normative**.

The **Adoption Starter Pack conforms to the Canonical Core**.

The **Executable / Reference Layer conforms to the Canonical Core**.

An **Organization-specific AE Implementation** is an operational realization of the Canonical Core using organization-specific baselines, profiles, policies, authority configuration, capability/provider bindings, and technology. It may be **Candidate** while being built or assessed and becomes **Conforming** only after applicable adoption/installation Proof is demonstrated for its declared scope.

The Starter Pack helps instantiate the Core. The Executable / Reference Layer proves/reference-demonstrates that the semantics can operate. Neither may independently redefine canonical semantics.

## Alternatives considered

### Entire distribution is equally normative

This is simpler to explain and could simplify conformance testing, but it would risk turning reference implementation technologies, packaging choices, or starter conveniences into permanent AE semantics.

### Canonical Core normative; other layers conforming — selected

This creates a clear authority boundary while still requiring the supporting layers to remain consistent with the Core.

## Consequences

1. Published distributions must identify normative versus conforming content.
2. Conforming layers may evolve independently when they preserve Canonical Core meaning.
3. Organization implementations may vary technology and topology while preserving mandatory canonical semantics.
4. Conformance does not imply external certification.
5. Reference behavior is evidence that the Core is operable, not an alternate definition of the Core.
6. Later repository information architecture must make the authority distinction discoverable to humans and agents.

## Traceability

- Contract v1.0: Spec §4, §18, §19; Proof A, I, M; Portability Principle.
- L1-A System Identity & Boundary Baseline.
