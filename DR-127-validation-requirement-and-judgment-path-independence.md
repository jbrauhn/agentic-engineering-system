# DR-127 — Validation Requirement and judgment-path independence

## Status

Adopted for L1-I.

## Decision

1. Canonical AE introduces subordinate **Validation Requirement [B]** semantics rather than a new Validation entity.
2. The universal minimum for independent Validation is **judgment-path independence** from the work-producing execution path.
3. The work-producing path may create Evidence but may not issue its own G4 acceptance.
4. The Validator must independently resolve material Evidence/authoritative state needed by the declared requirement and must have reconstructable actor/path provenance.
5. Stronger dimensions such as fresh actor, Human participation, provider/model diversity, environment separation, negative testing, and reproducibility are policy/risk-sensitive, not universal Canonical AE requirements.
6. Role label alone is not independence, identity, authority, or Validation judgment.

## Rationale

Requiring every Validation to use a separate Human, model provider, environment, or organization would over-constrain portable implementations and conflate risk-specific assurance with fundamental AE meaning. Requiring only a favorable test/provider result would allow self-acceptance. Judgment-path independence is the smallest universal invariant that preserves the maxim: **the doer shall not become its own judge**.

## Consequences

- the same underlying model/provider can conform for some scopes if the judgment path is genuinely independent and policy permits it;
- OEB/Product policy can strengthen independence without changing Canonical Core;
- G4 acceptance fails closed when required independence or material source state cannot be established;
- no `Validation Attempt`, `Validator Assignment`, or similar convenience entity is created.

## Traceability

Contract v1.0 Validation and Human authority semantics; DR-080–083; DR-108; DR-113; L1-D G4; L1-F authority; L1-G context; L1-H Verification/Evidence boundary.
