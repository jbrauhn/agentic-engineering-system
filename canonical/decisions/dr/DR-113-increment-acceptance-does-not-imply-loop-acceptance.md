# DR-113 — Increment acceptance does not imply whole-Contract or Loop acceptance

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

L2 Execution Increments can be independently Validated and accepted. However, Contract Proof may include cross-Increment behavior, integration effects, final-state requirements, architecture/security/performance consequences, or Proof Criteria that span more than one Increment.

Therefore counting accepted Increments is insufficient to prove the final Contract outcome.

## Decision

An Execution Increment may independently terminate with disposition **ACCEPTED** based on an independent Validation Record covering that Increment scope.

However:

> **All Increments individually ACCEPTED does not automatically prove that the overall Contract has been satisfied.**

Before an AE Loop may transition to `CLOSED / ACCEPTED`, an independent final Validation judgment must cover the **final applicable Contract scope/revision and Proof**.

The final Validation may:

- reuse Evidence Records from earlier work;
- reference prior Increment Validation Records;
- rely on already-validated Proof Criteria where still valid;
- add integration/final-state evidence where required.

It does not require ceremonial re-execution of valid lower-level tests.

Where accepted work was governed by different exact Contract revisions during an approved revision-effectivity transition, final acceptance must explicitly reconcile that work against the final applicable Contract scope/revision.

Loop closure also requires a learning disposition, but not necessarily a Learning Record when no material learning exists.

## Alternatives considered

### Accept Loop when all Increments are accepted

Simple and easy to automate, but can miss Contract-level integration/final-state Proof and hides the effect of Contract revision transitions.

### Re-run every lower-level Validation at final closure

Provides strong repetition but is wasteful and ceremonial when prior Evidence/Validation remains valid.

### Independent final Contract-scope judgment that reuses valid prior evidence — selected

Preserves whole-outcome assurance without unnecessary repetition.

## Consequences

1. G4 applies both to bounded Increment acceptance and final Contract/Loop acceptance, with different declared scopes.
2. final Loop acceptance requires a final Contract-scope Validation Record rather than a derived count of accepted Increments.
3. final acceptance must reconcile revision effectivity where accepted work spans earlier Contract revisions.
4. provider `Done`, Task COMPLETE, or Increment acceptance cannot independently close the Loop.

## Traceability

- Contract v1.0 Proof and independent Validation requirements.
- DR-016 — Proof belongs to Contract.
- DR-080–083 — Verification/Validation distinction and independent judgment.
- DR-109 — exact revision identity/history.
- DR-112 — Contract revision effectivity.
- Human Owner L1-D Increment Validation vs Loop/Contract acceptance refinement.
