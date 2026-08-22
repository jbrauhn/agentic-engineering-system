# ADR-004 — Machine-readable authority model and authority-integrity

**Status:** Adopted — Human Owner L1-F approval

## Context

L1-D and L1-E established a staged pattern: Human semantic artifacts remain normative for meaning while machine-readable JSON plus Python validators provide executable reference behavior and CI proof.

L1-F needs to prove authorization semantics across materially different authority implementations without creating a canonical policy DSL or production IAM engine.

## Decision

Use repository/reference:

- `authority_protocol.json` — conforming machine representation of authority result vocabulary, Human-reserved classes, operation Authority Requirements, assignment/validity/enforcement invariants;
- `authority_scenarios.json` — valid/invalid semantic fixtures;
- `authority_portability_fixtures.json` — materially different synthetic authority implementations expected to produce equivalent canonical outcomes;
- `validate_authority.py` — dependency-light Python reference validator;
- `.github/workflows/authority-integrity.yml` — repository CI job.

Human L1-F semantic artifacts remain normative for meaning. JSON/Python/GitHub Actions are repository/reference choices, not Canonical AE technology requirements.

`authority-integrity` loads the existing L1-E capability definition so every `protected_operation` must have an Authority Requirement.

## Non-goals

This ADR does not define a production authorization engine, policy DSL, IAM provider, PDP topology, or canonical RBAC/ABAC model.
