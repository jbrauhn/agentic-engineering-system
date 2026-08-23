# DR-128 — Evidence sufficiency, current reliance, and final reconciliation

## Status

Adopted for L1-I.

## Decision

1. Evidence sufficiency remains subordinate to Validation Requirement / Validation judgment; no first-class `Evidence Set` is introduced.
2. Sufficiency considers applicable Proof coverage, exact scope/revisions, source authority, provenance/integrity, currentness/effectivity, required independence characteristics, completeness, contradictions/negative Evidence, environmental relevance, reproducibility/retrievability where required, and known limitations.
3. Historical Evidence Records and Validation Records remain non-destructive even if later reliance changes.
4. Current reliance is explicit subordinate state; later stale/invalid/tampered/superseded Evidence can require revalidation/escalation without rewriting history.
5. Final Contract Validation may reuse valid Increment Evidence/Validation but must reconcile cross-Increment/integration/final-state effects, current reliance, historically valid revisions, unresolved limitations, and complete final Contract Proof.
6. Increment acceptance does not imply whole-Contract/Loop acceptance.

## Rationale

A separate Evidence Set entity would add identity without independent lifecycle need. Requiring final Validation to rerun every prior test would be ceremonial and expensive, while simply aggregating Increment acceptance would miss integration/final-state defects. Explicit current reliance preserves historical truth while allowing current governance to respond to later Evidence invalidation.

## Consequences

- Evidence bytes may remain provider-owned when canonical Evidence identity/provenance is preserved;
- contradictory material Evidence cannot be silently discarded;
- newest Evidence is not automatically correct for an exact requirement;
- final reconciliation is semantic, not tied to one integration-test technology.

## Traceability

DR-108/109; DR-113; L1-C Evidence/Validation records; L1-D final Contract-scope Validation; L1-G currentness/source authority; L1-H parallel Evidence and Proof→Verification chain.
