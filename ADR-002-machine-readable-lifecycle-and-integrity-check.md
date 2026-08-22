# ADR-002 — Use a conforming JSON lifecycle representation with a Python integrity validator and GitHub Actions CI

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner  
**Scope:** This repository / Part 1 reference implementation. This ADR does not make JSON, Python, or GitHub Actions canonical AE technology.

## Context

L1-D is the first point where Canonical AE lifecycle semantics are precise enough to validate mechanically. Contract v1.0 requires machine-verifiable integrity, and DR-109/DR-111/DR-112 now provide stable state, revision, gate, and transition semantics.

A prose-only lifecycle would delay proof that the protocol is precise enough to execute and validate. Conversely, immediately making the first convenient DSL the definition of AE would prematurely freeze representation technology.

## Decision

### Stage 1 authority

During L1-D:

- Human semantic lifecycle artifacts remain **normative for meaning**;
- `lifecycle_protocol.json` is a **conforming machine-readable representation** of structural protocol facts;
- `validate_lifecycle.py` validates structural integrity and scenario behavior;
- `lifecycle_scenarios.json` contains valid and intentionally invalid fixtures;
- `.github/workflows/lifecycle-integrity.yml` runs the executable check on PRs to `main` and pushes to `main`.

### Repository technology choice

This repository uses:

- **JSON** for the current machine-readable lifecycle representation;
- **Python 3 standard library** for the validator;
- **GitHub Actions** for CI.

Reasons:

- dependency-light;
- easy to diff/review;
- readable by humans and agents;
- broadly supported;
- sufficient for the approved L1-D structural semantics without adopting a workflow/statechart framework.

These are conforming implementation choices below canonical AE semantics.

### Promotion criteria

The machine representation may later be promoted through an explicit lower-level decision to normative structural authority only after evidence shows that it can faithfully express and validate at least:

- all required protocol semantics;
- valid scenario traces;
- known invalid routes;
- scope-aware Plan Review;
- Contract revision effectivity;
- blocking conditions;
- exact-revision gates;
- rolling-wave/parallel scopes;
- final Contract-scope Validation/reconciliation;
- controlled Human/machine structural drift.

If promoted, machine structural facts may become normative for state IDs, route IDs, gate IDs, transition structure, terminal dispositions, and other declared structural constraints. Human semantic artifacts remain normative for meaning, rationale, interpretation, and semantics not encoded structurally.

No uncontrolled dual authority is permitted.

## Validator scope

The initial `lifecycle-integrity` check validates real invariants, including:

- parseable machine definitions/fixtures;
- unique identifiers;
- state/route/gate references resolve;
- terminal dispositions are valid;
- required gate and route families exist;
- stale Plan Review is rejected;
- wrong Contract revision is rejected;
- unreviewed Execution is rejected;
- unknown authority fails closed;
- Contract change without Human approval is rejected;
- self-Validation acceptance is rejected;
- provider `Done` cannot imply AE acceptance;
- ambiguous Contract effectivity is rejected;
- rolling-wave/parallel Increments are representable;
- explicitly unaffected work can continue under a prior exact Contract revision after valid effectivity determination;
- final Loop acceptance requires final Contract-scope Validation and revision reconciliation.

## Alternatives considered

### Prose-only L1-D

Advantages: avoids representation choice now.

Rejected because machine-verifiable lifecycle integrity is now meaningful and delaying it would leave exact-revision/gate semantics untested.

### Make JSON immediately normative AE semantics

Advantages: one executable source immediately.

Rejected because the first encoding has not yet proved adequate expressiveness/parity and JSON is an implementation representation, not what AE fundamentally means.

### Adopt SCXML/XState/BPMN/statechart framework now

Advantages: mature workflow/state-machine semantics.

Rejected because the approved AE model is scoped/composite and revision/gate/effectivity-oriented; adopting a larger framework now would add topology/DSL assumptions before evidence shows the need.

## Consequences

1. CI deferral ends with L1-D because executable canonical-system behavior now exists.
2. repository lifecycle changes should be accompanied by fixture/validator updates where applicable.
3. later schema/domain work can build on this executable pattern without treating JSON/Python/GitHub Actions as canonical requirements.
4. if branch-protection tooling cannot make `lifecycle-integrity` required, that limitation must be recorded as a repository-governance gap rather than falsely claiming enforcement.
5. issue #6 remains compatible because the protocol/validator does not depend on a developer IDE, Portal, Dev Container, or agent host.

## Traceability

- Contract v1.0 machine-verifiable integrity Proof.
- DR-109 — exact revision identity and machine-validation direction.
- DR-111 — composite/scoped lifecycle protocol.
- DR-112 — exact-scope gates and Contract effectivity.
- DR-113 — final Contract acceptance.
- Human Owner L1-D D13/D14 and CI authorization.
