# DR-108 — Canonical domain taxonomy and minimum durable object set

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Contract v1.0, DR-106 and DR-107 require durable, traceable, provider-neutral engineering state across materially different implementations. L1-C must define semantic objects without turning every useful concept, provider API object, document heading, or temporary context into a canonical entity.

Over-modeling creates identity inflation and brittle schemas. Under-modeling makes approval, revision, handoff, evidence, Validation, adoption, and learning ambiguous.

## Decision

Canonical AE uses the following semantic categories:

- **A1 — First-class durable entity**;
- **A2 — First-class durable record**;
- **B — Canonical value/subordinate object**;
- **C — External Resource Reference**;
- **D — Derived view/projection/context product**;
- **E — Ephemeral operating state**;
- **F — Normative definition/release object**.

Admission principle:

> **Independent canonical identity must materially protect system meaning across time and must not be added when a value, relationship, reference, subordinate record, or derived view is sufficient.**

Hard test:

> **Would confusing two instances/revisions cause a material governance, authority, traceability, continuation, or Validation error?**

The burden is on adding identity.

### A1 entity set

L1-C establishes these A1 concepts:

1. Organization Engineering Baseline;
2. Product/System Profile;
3. AE Implementation Profile;
4. Capability Binding;
5. Product/System Baseline — L1;
6. AE Loop;
7. Contract;
8. Contract Change Proposal;
9. Plan;
10. Execution Increment — L2;
11. Executable Task — L3;
12. Architecture Model;
13. Experiment.

### A2 record set

L1-C establishes these A2 concepts:

1. Decision Record / ADR;
2. Authority Decision;
3. Plan Review Record;
4. Evidence Record;
5. Validation Record;
6. Handoff Record;
7. Learning Record.

### Important exclusions

- AE Loop is a coordination/correlation entity, not aggregate owner of all persistent engineering state.
- Architecture Element remains an addressable subordinate object, not a global A1 entity.
- Proof Criterion remains subordinate to an exact Contract revision but is stably addressable within it.
- Context Package is derived, not authoritative state.
- L4 agent micro-plan is ephemeral by default.
- provider work items/commits/CI runs/traces/etc. remain external resources unless separate AE semantics justify a canonical object.
- no `Engineering Environment Profile` is created in L1-C; issue #6 preserves that open design concern.

## Alternatives considered

### Treat most durable artifacts as one generic entity type

Simplifies schema design but erases meaningful differences between versioned stateful entities, issued judgments/records, derived products, and provider references.

### Create first-class objects for most named concepts

Makes every concept directly addressable but creates identity inflation and turns provider/document implementation details into Canonical Core semantics.

### Minimal semantic taxonomy with explicit admission burden — selected

Preserves governance/traceability where identity matters while keeping the Canonical Core small and provider-neutral.

## Consequences

1. L1-C and later schemas must preserve A1/A2/B/C/D/E/F distinctions.
2. Promotion/demotion of a concept is a semantic change requiring explicit rationale; it is not driven by file layout or provider object models.
3. Domain entities remain distinct from serialized representations.
4. The entity set can be extended later when downstream lifecycle/authority evidence demonstrates independent identity is necessary.
5. R1–R7 ownership is defined in the L1-C Entity Classification & Ownership Matrix.

## Traceability

- Contract v1.0: Spec §§3, 9, 11, 12, 15–19.
- DR-025 — L1 durable Product/System baseline.
- DR-033 — dual-format/multiple Plan representations.
- DR-040–043 — system-owned memory, structured handoff, compaction distinction.
- DR-080–083 — Verification/Validation distinction and independent judgment.
- DR-106 — seven canonical logical responsibilities.
- DR-107 — federated authoritative state.
- Human Owner L1-C decision D1–D15.