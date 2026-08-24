# ADR-007 — Machine-readable Validation protocol and integrity check

## Status

Accepted for the L1-I reference/repository layer.

## Context

L1-I introduces semantic Validation requirements, judgment-path independence, Evidence sufficiency/current reliance, final reconciliation, and judgment-to-route semantics that are precise enough to test mechanically. Prior ADR-002 through ADR-006 establish a staged pattern in which Human semantic artifacts remain normative for meaning while machine representations prove structural expressiveness and cross-domain consistency.

## Decision

For this repository:

- use `validation_protocol.json` as the Stage-1 conforming machine representation;
- use `validation_scenarios.json` for valid and intentionally invalid semantic fixtures;
- use `validation_portability_fixtures.json` for materially different conforming architectures;
- use `validate_validation.py` as a dependency-light Python reference validator;
- run `.github/workflows/validation-integrity.yml` on PRs/pushes to `main`.

The validator cross-checks existing lifecycle, capability, authority, context, and Planning/Execution machine artifacts rather than replacing them with L1-I-local copies.

Human L1-I semantic artifacts remain normative for meaning in Stage 1. JSON/Python/GitHub Actions are repository/reference choices, not Canonical AE technology requirements.

## Consequences

`validation-integrity` must prove at least:

- no executor self-acceptance;
- exact Contract/Proof/scope control;
- Evidence sufficiency/currentness/conflict behavior;
- independent source resolution and Validator provenance;
- judgment vs lifecycle-route separation;
- final Contract reconciliation;
- historical non-destructive invalidation/revalidation;
- policy-sensitive strengthening without universal Human/provider/environment requirements;
- reuse of one core protocol across adoption/capability scopes;
- portability across materially different Validation architectures.

The workflow is evidence, but it is not repository-enforced until issue #12's branch-protection closure condition is satisfied.

## Rejected alternatives

- prose-only Validation semantics;
- production Validator service/quality framework as canonical implementation;
- JSON as sole normative semantic authority immediately;
- one universal assurance-tier/risk formula.
