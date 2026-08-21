# L1-C — Canonical Relationship / Traceability Model

**Status:** Approved L1-C semantic baseline  
**Scope:** Representation-neutral typed relationship semantics. This is not a closed relationship vocabulary or graph-storage prescription.

## 1. Principle

AE requires explicit cross-artifact traceability.

> **Filenames, directory nesting, prose references, UI placement, and provider parent/child hierarchy are not sufficient canonical traceability mechanisms.**

The domain therefore supports typed semantic edges between canonical entities/records/subordinate objects and External Resource References.

## 2. Relationship semantic shape

A canonical relationship must be able to express, as applicable:

- source endpoint reference;
- relationship type/meaning;
- target endpoint reference;
- exact revision specificity for either endpoint when required;
- scope/context if the relationship is not globally true;
- provenance where material;
- effective/supersession semantics where material.

L1-C does not mandate graph databases, RDF, link files, database foreign keys, or another physical implementation.

## 3. Relationship identity

Relationships are normally **not** globally independent A1/A2 objects.

A typed edge is sufficient when its meaning is governed by its endpoints and provenance.

Admission rule for promotion:

> If a relationship develops its own independent lifecycle, authority, material provenance/history, or governance needs that cannot be represented safely as edge metadata, promotion to a durable entity/record should be considered.

## 4. Exact-revision endpoint rule

Use an exact revision endpoint whenever the assertion's truth depends on the specific revision.

Examples:

- Plan revision derives from Contract revision;
- Plan Review evaluates Plan revision;
- Authority Decision approves Contract Change Proposal revision;
- Validation evaluates Contract revision;
- Evidence supports Proof Criterion within Contract revision;
- Plan plans against Product/System Baseline revision;
- adoption Validation evaluates AE Implementation Profile/OEB/Capability Binding revisions.

A logical-identity endpoint is appropriate for durable relationships such as `Product/System Profile represents Target Product/System` where the relationship intentionally follows future revisions.

## 5. Initial relationship families

This is a minimum semantic challenge set, not a frozen exhaustive vocabulary.

### Lifecycle / Contract / Planning

- `AE Loop uses Contract revision`
- `AE Loop uses Plan revision`
- `AE Loop plans_against Product/System Baseline revision`
- `Plan derives_from Contract revision`
- `Plan plans_against Product/System Baseline revision`
- `Plan decomposes_to Execution Increment`
- `Execution Increment decomposes_to Executable Task`
- `Contract Change Proposal proposes_change_to Contract revision`
- `Authority Decision approves/rejects proposal/transition/action/revision`
- `new revision supersedes prior revision`

### Architecture

- `Plan affects Architecture Element`
- `Executable Task affects/implements change to Architecture Element`
- `Decision Record / ADR affects Architecture Element/Relationship/Model`
- `Architecture Representation represents Architecture Model revision`
- `Product/System Baseline references Architecture Model revision`

### Provider / capability

- `Capability Binding realizes Capability Contract Definition`
- `Executable Task realized_by External Work Resource Reference`
- `Evidence Record references External Resource Reference`
- `AE Implementation Profile uses Capability Binding revision`

### Proof / evidence / Validation

- `Evidence Record supports Proof Criterion`
- `Validation Record evaluates Contract revision`
- `Validation Record evaluates Proof Criterion(s)`
- `Validation Record uses Evidence Record(s)`
- `Validation Record routes AE Loop outcome`
- later assessment `invalidates/qualifies evidence_for` a particular use where downstream semantics require it.

### Decisions / review

- `Plan Review Record evaluates Plan revision`
- `Decision Record informs/affects Plan/Architecture/Capability/Guidance`
- `Authority Decision disposes Contract Change Proposal`

### Context / continuation

- `Handoff Record continues AE Loop / Increment / Task`
- `Handoff Record references authoritative state`
- consequential durable outcome may carry `informed_by` provenance to authoritative source references used in context assembly.

### Learning

- `Experiment produces Learning Record`
- `AE Loop / Validation failure / incident produces Learning Record`
- `Learning Record informs Decision Record / planning guidance / future Experiment`

### Adoption

- `AE Implementation Profile implements Canonical AE Release Manifest`
- `AE Implementation Profile uses OEB revision`
- `AE Implementation Profile uses Product/System Profile revision`
- `AE Implementation Profile uses Capability Binding revision(s)`
- `Installation/Adoption Validation evaluates implementation profile + applicable exact inputs`
- `conformance projection derived_from Validation Record(s)`

## 6. Proof Criterion addressing

Proof Criterion remains subordinate to an exact Contract revision, but it must be stably addressable within that scope.

Therefore an Evidence relationship conceptually targets:

`Contract logical ID + exact Contract revision + Proof Criterion scoped ID`

not an ambiguous prose phrase such as “supports the performance proof.”

## 7. Architecture Element addressing

Architecture Element remains B-category but must have stable addressable identity scoped to the logical Architecture Model / Target Product/System.

A Plan or ADR can therefore target an element across Architecture Model revisions when appropriate, while still recording the exact Architecture Model revision that supplied the planning context when exactness matters.

## 8. External references and provider authority

A relationship to a provider object terminates in a canonical **External Resource Reference**, not in a copied provider object pretending to be AE-owned state.

Example:

`Executable Task AE-TASK-147 --realized_by--> ExternalResourceReference(Work Management binding X, provider resource ENG-491)`

The relationship preserves AE meaning while provider property authority remains declared separately.

## 9. Provenance expectations

Material relationships created by decisions, approvals, Validation, synchronization/reconciliation, or automation must preserve enough provenance to identify how/why the relationship became part of authoritative AE state.

Routine deterministic relationships may use implementation-level provenance rather than becoming separate records.

## 10. Consistency and reconciliation

Where multiple representations/systems expose the same semantic relationship:

- authoritative-source declaration determines which source/property governs;
- non-authoritative copies are projections/caches/references;
- conflicts follow DR-107 deterministic precedence/reconciliation;
- protected decisions/actions fail closed where material relationship truth cannot be established.

## 11. Machine-readable readiness

The relationship model is intentionally schema-ready:

- endpoints are typed/addressable;
- revision specificity is explicit;
- relationship type is explicit;
- provenance/scope hooks exist.

L1-C does not yet select a serialization or implement validators.