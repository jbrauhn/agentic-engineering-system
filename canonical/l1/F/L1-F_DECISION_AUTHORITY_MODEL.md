# L1-F — Decision Authority Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Definition

> **Decision Authority is the effective scoped authority of an actor to make or approve a governed decision of a specified decision class.**

DA is distinct from provider entitlement, OA, and provider write access.

## 2. Minimum semantics

DA must support/reconstruct as applicable:

- decision class;
- subject/authority holder;
- organization/Product-System/Contract/other decision scope;
- limits/conditions;
- validity/time constraints;
- delegation rules;
- authoritative source;
- provenance.

## 3. Authority Decision [A2]

An Authority Decision is the immutable durable record that an actor with applicable DA exercised that authority against an exact target/scope/revision.

It must identify, as applicable:

- decision ID;
- actor and authenticated identity;
- DA basis/source;
- decision class;
- exact target/revision;
- scope;
- decision outcome;
- decision time;
- provenance.

Document appearance is not approval. A record that says "Human approved" without authoritative identity, applicable DA, exact target, source, and provenance is not an authoritative Authority Decision.

## 4. Canonical Human-reserved Decision Authority

L1-F inventories but does not expand the Contract's Human-reserved authority.

Contract v1.0 explicitly preserves Human authority over:

- engineering intent;
- material risk acceptance;
- consequential tradeoffs;
- Contract approval;
- Contract change;
- other decisions explicitly assigned to Human Decision Authority by higher canonical authority.

Canonical Human-reserved classes cannot be delegated to AI or weakened by organization policy.

## 5. Organization-reserved Human Decision Authority

Organizations may reserve additional decisions to Humans based on regulation, classification, risk, safety, product criticality, architecture governance, production impact, business policy, or another organizational concern.

Those reservations are governed organization policy and do not redefine Canonical AE.

## 6. Contract-change proving path

L1-F reuses L1-D:

`Contract Change Proposal exact revision → eligible Human DA → Authority Decision → G5 SATISFIED → new Contract revision approval → effectivity evaluation`.

L1-F does not create a second Contract-change lifecycle.
