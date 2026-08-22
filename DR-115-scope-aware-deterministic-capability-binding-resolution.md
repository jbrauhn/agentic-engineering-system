# DR-115 — Capability Bindings are scope-aware and resolve deterministically

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

Organizations may use multiple providers for the same capability across products, repositories, environments, classifications, or other scopes. One provider may also realize several canonical capabilities. Canonical AE cannot assume one capability equals one provider.

## Decision

Capability Bindings are many-to-many, scope-aware, and versioned.

A canonical operation + declared scope resolves to exactly one deterministic binding plan. The plan normally contains one binding and may contain an explicitly declared composition where the semantic operation genuinely requires several bindings.

Ambiguous candidate resolution is invalid configuration. AE shall not try providers opportunistically, select the first responder, silently switch source of truth, or silently change authority semantics.

Provider fallback is organization policy, not universal Canonical Capability behavior, and must preserve deterministic selection, canonical result semantics, identity/authority, source-of-truth, and evidence/provenance.

Access Path Descriptor is a subordinate [B] concept within binding semantics. It supports interface parity through extensible consumer/runtime-context selectors without defining a canonical environment taxonomy.

## Consequences

- provider replacement does not change canonical operation semantics;
- deterministic discovery becomes a canonical semantic requirement;
- issue #6 gains an access-path hook without being closed;
- explicit composition is possible without creating a new A1 Binding Resolution entity.

## Traceability

Contract §§4–7, 18–19; DR-019; DR-107; DR-110; ADR-001; Human Owner L1-E D8–D10 and D19.
