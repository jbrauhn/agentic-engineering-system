# L1-C — Identity / Revision / Provenance Baseline

**Status:** Approved L1-C semantic baseline  
**Authority:** Contract v1.0; DR-107 federated authoritative state; Human Owner L1-C decision  
**Scope:** Representation-neutral identity, revision, version, provenance, and authoritative-source semantics.

## 1. Core identity model

L1-C separates three concepts.

### Logical identity

The enduring identity of a canonical A1 entity across revisions.

Example conceptually:

`Contract AE-CONTRACT-42`

### Revision identity

The exact immutable revision/state of a revisioned entity used at a point in time.

Example conceptually:

`AE-CONTRACT-42 @ revision-3`

### Human-readable version label

Optional label for human communication, release management, or presentation.

Examples might include `v1.2`, `approved-2026-08-21`, or another organization-selected convention.

A version label does **not** replace exact revision identity.

L1-C does not mandate Git hashes, database IDs, UUIDs, semantic versioning, event sourcing, content-addressing, or another physical identity implementation.

## 2. Exact-revision reference rule

When the truth or authority of a relationship depends on exact state, the reference must resolve to the **exact revision**.

Examples:

- Authority Decision approves/rejects an exact Contract Change Proposal or Contract revision;
- Plan derives from an exact approved Contract revision;
- Plan Review evaluates an exact Plan revision;
- Plan plans against an exact Product/System Baseline revision;
- Validation evaluates an exact Contract revision and Proof Criterion scope;
- evidence interpretation references the relevant exact Plan/Task/architecture state when necessary;
- adoption Validation evaluates exact Canonical AE Release, OEB, Implementation Profile, Product/System Profile, and relevant Capability Binding revisions.

Logical-ID-only references are permitted where the relationship intentionally follows the enduring logical entity and exact revision does not change the assertion's truth.

## 3. Record identity

A2 records normally use a stable **record identity** because the issued record itself is the historical fact.

Examples:

- Authority Decision;
- Plan Review Record;
- Evidence Record;
- Validation Record;
- Handoff Record;
- Learning Record;
- Decision Record / ADR.

Issued records do not require artificial revisioning simply for metadata consistency. Correction or changed understanding is represented by an explicit new/correcting/superseding record when needed.

## 4. Small shared semantic header

Canonical A1/A2 objects shall support a small common traceability mechanism, conceptually including where applicable:

- `canonical_type`;
- logical ID or record ID;
- exact revision ID for revisioned objects;
- authoritative-source declaration/reference;
- provenance.

Additional semantics are used only where meaningful:

- scope;
- lifecycle/status marker;
- actor/authority metadata;
- timestamps;
- integrity identity;
- typed relationships;
- supersession/correction links.

Principle:

> **Common traceability mechanics; entity-specific semantics.**

This is not a requirement for one giant inheritance/base class.

## 5. Authoritative-source integration

Identity does not by itself establish authority.

For material canonical state, the implementation must be able to determine:

- the semantic object/state category;
- logical governing responsibility;
- stable logical/record identity;
- authoritative source for the relevant scope/property/revision;
- allowed writers/authority;
- current revision semantics;
- provenance;
- relationships;
- precedence/reconciliation when several systems participate.

An External Resource Reference may identify provider-owned state while the canonical A1/A2 object preserves AE identity/relationships.

## 6. Provenance baseline

Provenance must be sufficient to reconstruct material facts and decisions, not merely the latest value.

As applicable, provenance should allow later determination of:

- origin/producer;
- actor or automation path;
- authority under which a material change/decision occurred;
- source/provider;
- creation/issuance time;
- relationship to prior/superseded/corrected state;
- relevant rationale/evidence;
- exact referenced revisions.

L1-C defines the semantic requirement, not the final field schema.

## 7. Immutable approved/baselined revisions

For versioned governed entities:

- draft/current working state may evolve according to later lifecycle rules;
- once a revision becomes approved/baselined under canonical governance, that exact revision is immutable;
- later change creates a new revision and explicit supersession/lineage rather than destructive rewriting.

This applies especially to:

- Contract;
- Plan where review/approval semantics make revision exactness material;
- Product/System Baseline;
- Organization Engineering Baseline where baselined/adoption-referenced;
- Product/System Profile where baselined/adoption-referenced;
- Architecture Model where an exact baseline/decision depends on it;
- Capability Binding where governed invocation/Proof depends on exact mapping;
- AE Implementation Profile when installation/adoption Validation references an exact revision.

## 8. Issued record immutability

The following are historical assertions/judgments and shall not be destructively rewritten after issuance:

- Decision Record / ADR;
- Authority Decision;
- Plan Review Record;
- Evidence Record;
- Validation Record;
- Handoff Record;
- Learning Record.

Corrections use an explicit correction/supersession/new judgment relationship while preserving the original historical record.

### Evidence-specific rule

An issued Evidence Record records what evidence existed, its source/reference, and relevant context/provenance at issuance.

If later found stale, invalid, superseded, incomplete, corrupted, or inappropriate for a Proof Criterion, the original record remains historically intact. Later Validation/correction/supersession semantics capture the changed assessment.

## 9. Representation integrity

A canonical entity may have multiple representations.

A conforming implementation must eventually be able to determine which exact canonical revision a material representation corresponds to when ambiguity would affect governance or execution.

Examples:

- Human Plan document and machine-readable Plan representation;
- interactive Plan IG;
- Baseline Manifest representing Product/System Baseline revision;
- architecture visualization representing an Architecture Model revision.

No representation becomes authoritative solely because it is a file, database row, UI object, or provider resource.

## 10. Context provenance hook

Context Package is a derived D object and does not need permanent first-class identity by default.

However, when a consequential governed outcome materially depends on assembled context, the implementation must later be able to preserve sufficient provenance to identify the authoritative/provenance-bearing sources materially used.

L1-C intentionally does not choose among possible mechanisms such as source manifests, assembly receipts, integrity digests, query/input specifications, or provenance attached to the resulting durable record. That mechanism belongs primarily to L1-G.

## 11. Canonical release identity

F-category **Canonical AE Release Manifest** provides an exact release identity/reference for the published Canonical AE Distribution/Core definitions.

An AE Implementation Profile and installation/adoption Validation must be able to identify the exact Canonical AE Release being claimed/evaluated.

Organization-specific implementations reference normative release definitions; they do not mutate them.