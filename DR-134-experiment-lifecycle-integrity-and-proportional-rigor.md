# DR-134 — Experiment lifecycle, measurement integrity, and proportional rigor

**Status:** Adopted

## Decision

Operationalize existing `Experiment [A1]` with `PROPOSED → ACTIVE → CONCLUDED`, plus terminal `CANCELLED` where appropriate. Inconclusive is a result, not a lifecycle state.

Material ACTIVE setup/measurement changes require versioning/provenance. CONCLUDED history is non-destructive. Conclusion strength may not exceed design/Evidence strength. No one statistical/causal method is canonical.

No first-class Experiment Run or Observation entity is added.

## Rationale

Experiment identity already passes DR-108. Additional run/observation identities are not needed for normal traceability and would inflate the model.

## Consequences

DR-102, DR-103, and DR-104 remain open experiments. L1-K gives them operating semantics but does not resolve them. Governed-AE-vs-lighter comparison remains a genuine experiment, not predetermined proof.
