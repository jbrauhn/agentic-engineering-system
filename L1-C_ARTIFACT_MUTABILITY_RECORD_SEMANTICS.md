# L1-C — Artifact Mutability / Record Semantics

**Status:** Approved L1-C semantic baseline  
**Scope:** Semantic change/history classes. Detailed lifecycle state machines remain downstream.

## 1. Why mutability is a domain concern

AE must distinguish current state from historical fact. If an approved Contract, Plan Review, Validation judgment, or Evidence Record can be silently edited in place, later agents cannot reconstruct what was actually approved, reviewed, produced, or judged.

L1-C therefore defines five mutability classes without prescribing storage technology.

## 2. Versioned governed entity

Examples:

- Organization Engineering Baseline;
- Product/System Profile;
- AE Implementation Profile;
- Capability Binding;
- Product/System Baseline — L1;
- Contract;
- Contract Change Proposal while being prepared;
- Plan;
- Architecture Model.

Rules:

1. a logical entity may have multiple revisions;
2. a working/draft revision may evolve subject to later lifecycle rules;
3. once a revision is approved/baselined/issued at a governance boundary, that exact revision becomes immutable;
4. later change produces a new revision with explicit lineage/supersession rather than destructive editing;
5. decisions/reviews/Validation must continue to resolve to the exact revision they originally targeted.

### Product/System Baseline

The Baseline logical entity evolves by new baselined revisions. A Baseline Manifest may represent/snapshot one exact revision but does not become the canonical entity merely because it is serialized.

### Contract

Approved Contract revision is immutable. Approved Contract Change Proposal leads to a new Contract revision; the prior approved revision remains reconstructable.

### Plan representations

One Plan revision may have multiple conforming representations. Changing presentation alone need not create a semantic Plan revision if integrity rules can establish that semantic content is unchanged; material Plan change creates a new revision and triggers applicable review semantics.

## 3. Operational stateful entity

Examples:

- AE Loop;
- Execution Increment — L2;
- Executable Task — L3;
- Experiment while active.

Rules:

1. current operational state may advance/change;
2. material transitions must remain reconstructable through append-only transition/event/provenance semantics;
3. provider-owned operational fields may change according to the provider's authoritative state model;
4. AE must not duplicate provider state merely to create a second mutable copy;
5. when a particular state snapshot is used at a governance/evidence boundary, the relevant exact state/revision/reference must be reconstructable.

## 4. Issued immutable record

Examples:

- Decision Record / ADR;
- Authority Decision;
- Plan Review Record;
- Evidence Record;
- Validation Record;
- Handoff Record;
- Learning Record.

An issued record is a durable historical assertion.

Rules:

1. do not destructively rewrite what was originally issued;
2. corrections use an explicit correction/supersession/replacement record or relationship;
3. changed judgment uses a new judgment rather than silently editing the old one;
4. later invalidation does not erase historical provenance;
5. records can reference exact entity revisions and external resources.

### Evidence refinement

Evidence Record records what evidence existed and what AE knew about its source/context at issuance.

If later found stale, invalid, superseded, incomplete, corrupted, or inappropriate:

- preserve the original Evidence Record;
- record the later assessment through Validation, correction/supersession, or another appropriate record;
- ensure current consumers can distinguish historical issuance from current validity without rewriting history.

### Validation refinement

A later Validation attempt does not edit a prior Validation Record. Each issued judgment remains a discrete historical fact and may route the Loop differently.

### Learning refinement

Learning may later be qualified/corrected/superseded. The original Learning Record remains historical; updated understanding is represented explicitly.

## 5. Derived view / projection / context product

Examples:

- Context Package;
- dashboard;
- search/vector index;
- generated summary;
- Plan IG;
- rendered architecture visualization;
- Baseline Manifest when used as a representation of a Baseline revision;
- conformance projection derived from Validation.

Rules:

1. derived content can be rebuilt/discarded when its source/provenance obligations are satisfied;
2. derived content must not silently become authoritative truth;
3. when a consequential governed outcome materially depends on a derived context, sufficient source provenance must be retained elsewhere or with the resulting durable record;
4. representation integrity must make exact semantic revision correspondence determinable where material.

## 6. Ephemeral operating state

Examples:

- L4 agent micro-plan;
- temporary scratch reasoning/sequencing;
- transient tool/session state;
- local retries with no material durable consequence.

Rules:

1. no durability expectation by default;
2. ephemeral state must not become the only location of material engineering truth;
3. material facts/decisions/evidence/continuation needs are promoted to their owning durable semantic objects;
4. loss of ephemeral state must not make the AE System unable to reconstruct required durable state.

## 7. Correction and supersession semantics

L1-C does not freeze relationship vocabulary, but the domain must support explicit semantics equivalent to:

- `supersedes`;
- `corrects`;
- `replaces` where materially distinct from supersession;
- `amends` for draft/pre-issuance contexts where allowed;
- `invalidates_for` / later judgment relationships as downstream design requires.

A correction must preserve the identity of the original historical record and the identity of the correcting record.

## 8. Provider-owned mutable state

Provider resources may remain authoritative for selected operational properties.

Example:

`Executable Task AE-TASK-147`

AE canonical semantics may own:

- task identity;
- intended engineering work;
- parent increment;
- canonical dependencies required by AE;
- Contract/Plan traceability;
- authority/evidence relationships.

Work Management may remain authoritative for declared properties such as:

- workflow status;
- assigned actor;
- provider-specific dependency fields;
- provider timestamps/comments.

The exact split is downstream. The L1-C rule is:

> **Do not duplicate a provider property unless AE has a semantic reason to own another authoritative property.**

## 9. Conformance status is not an editable fact

The AE Implementation Profile may state intended/claimed scope and Candidate status.

Evidence-backed Conforming state must be traceable to applicable installation/adoption Validation Record(s).

If a Profile displays/stores conformance status, that value is a projection/cache of the authoritative Validation basis and must not diverge from it.

A manual `conforming=true` flag cannot create conformance.

## 10. Downstream hooks

- L1-D defines detailed lifecycle/state-machine transitions.
- L1-F refines authority/decision change rules.
- L1-G refines context provenance and retention.
- Validation design refines judgment/correction/independence semantics.
- schema work later expresses these classes mechanically without changing their meaning.