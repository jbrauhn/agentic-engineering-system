# L1-K — Experiment A1 Lifecycle and Integrity Model

**Status:** Human Owner-approved L1-K semantic baseline

## 1. Existing identity

`Experiment [A1]` remains the canonical first-class entity for formal AE experiments. No Experiment Run or Observation entity is added in L1-K.

## 2. Small lifecycle

Canonical lifecycle:

- `PROPOSED`
- `ACTIVE`
- `CONCLUDED`
- `CANCELLED`

`CONCLUDED` and `CANCELLED` are terminal for that Experiment revision/history. An inconclusive result is still `CONCLUDED`; inconclusive describes the result, not a lifecycle state.

## 3. Minimum semantics as applicable

An Experiment preserves:

- stable identity;
- question/hypothesis;
- scope/context;
- baseline/comparator where meaningful;
- intervention/change under study;
- measurement plan and exact applicable metric definitions;
- Evidence/observations/provider references;
- limitations/confounders/uncertainty;
- result;
- conclusion;
- relationships to Learning, Decision, ADR, OEB/Product/configuration changes, or follow-on Experiment;
- provenance and relevant revisions/currentness.

## 4. Active evolution

An ACTIVE Experiment may evolve its setup or measurement plan. Material changes must be versioned/provenanced so observations produced under an earlier setup are not silently reinterpreted as though they were produced under the later design.

## 5. Conclusion strength

> **The strength of an Experiment conclusion must not exceed the strength of the Experiment design and Evidence.**

Canonical AE does not mandate randomized trials, A/B tests, a statistical package, a scientific method template, or one causal framework. Rigor is proportional to the question, risk, and Evidence needed.

Claims that imply causality require design/Evidence capable of supporting that strength. Otherwise the conclusion must remain appropriately limited.

## 6. Non-destructive history

Once CONCLUDED, the issued Experiment result/conclusion/history is non-destructive. Later Evidence can qualify, contradict, or supersede current reliance through later authoritative state, Learning, Decision, or Experiment records rather than rewriting historical truth.

## 7. Existing experiments remain experiments

DR-102, DR-103, and DR-104 remain open experiments. L1-K gives them durable operating semantics; it does not resolve their hypotheses.

Comparison of governed AE to lighter workflows remains an Experiment, not predetermined evidence that governed AE is superior.
