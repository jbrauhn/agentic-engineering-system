# ADR-010 — Machine-readable adoption/distribution protocol and integrity CI

**Status:** Adopted as repository/reference architecture choice

## Decision

Represent the L1-L reference adoption/distribution semantics with JSON fixtures/protocols and Python reference validators/packaging/clean-room harnesses, exercised by a separate `adoption-integrity` GitHub Actions workflow.

Human semantic L1-L artifacts remain normative for meaning. JSON, Python, SHA-256, repository paths and GitHub Actions are reference choices.

The integration job cross-checks inherited L1-D through L1-K machine semantics and exercises end-to-end adoption behavior rather than replacing the domain validators.

## Rationale

L1-L is the Part 1 integration boundary. A distinct integration suite makes release classification, bootstrap parity, Candidate→Conforming rules, synthetic imperfections, reference loops and fresh-session input boundaries executable without overloading any one domain validator.

## Consequences

- `adoption-integrity` becomes the ninth meaningful repository integrity job.
- issue #12 remains open until repository protection actually requires applicable checks and a failing-check merge-block test proves enforcement.
- the reference packager creates an exact SHA-256 payload inventory without making SHA-256 or Git canonical technology.
