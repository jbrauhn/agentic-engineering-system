# ADR-009 — Machine-readable observability / experiment / learning protocol and integrity CI

**Status:** Adopted

## Decision

Provide a staged JSON/Python/GitHub Actions reference representation for L1-K:

- `observability_learning_protocol.json`
- `observability_learning_scenarios.json`
- `observability_learning_portability_fixtures.json`
- `validate_observability_learning.py`
- `.github/workflows/observability-learning-integrity.yml`

Human L1-K semantic artifacts remain normative for meaning. JSON, Python, GitHub Actions, and any telemetry provider are repository/reference implementation choices rather than Canonical AE technologies.

The validator cross-checks inherited L1-D through L1-J machine semantics rather than creating local substitutes for lifecycle, capabilities, authority, context, Planning/Execution, Validation, or standards/health.

## Rationale

The Contract requires a reference layer and machine-verifiable integrity. L1-K includes enough exact semantic boundaries to falsify common metric/learning errors.

## Consequences

`observability-learning-integrity` becomes another meaningful repository check. Issue #12 remains open until branch/ruleset enforcement actually requires applicable checks and a deliberate failing-check merge-block proves enforcement.
