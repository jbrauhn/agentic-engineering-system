# DR-116 — OEB coordinates authoritative organization state and Product/System specialization cannot silently weaken it

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

Contract v1.0 makes the Organization Engineering Baseline an adoption artifact broader than a tool map. L1-C establishes OEB and Product/System Profile as A1 entities. L1-E must make them operational without creating a giant shadow configuration store.

## Decision

The OEB is a durable versioned organization-level engineering operating baseline coordinating organization defaults, constraints, capability-realization references, governance references, and engineering expectations.

The OEB references authoritative organization state rather than automatically owning/copying it.

Precedence:

Canonical AE mandatory semantics → OEB → Product/System Profile → derived effective configuration → governed AE work.

Product/System Profile may tighten, narrow, and specialize. It may not silently weaken higher-authority mandatory semantics/policy/security/governance.

DR-109 exact revision history applies. A new OEB revision does not silently rebase active work. Later policy/effectivity semantics may explicitly require reassessment.

## Consequences

- historical OEB context remains reconstructable;
- Product/System specialization does not become last-writer-wins;
- detailed exception, standards, authority, and OEB-effectivity mechanics remain downstream;
- effective configuration remains a derived projection unless later identity evidence justifies promotion.

## Traceability

Contract §5 and §§18–19; DR-107–110; Human Owner L1-E D16–D18.
