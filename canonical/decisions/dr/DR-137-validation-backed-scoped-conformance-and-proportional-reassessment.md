# DR-137 — Validation-backed scoped conformance and proportional reassessment

**Status:** Adopted

## Decision

An Organization-specific AE Implementation begins Candidate and becomes Conforming only through applicable independent adoption Validation against exact release, scope and governing revisions. Conformance status is a derived projection, not an editable authority field, provider-success state, certification claim, or special Validation ontology.

Historical Validation remains immutable. Later release/baseline/binding/policy/interface/Evidence change never silently rebases historical conformance. Current reliance may require proportional reassessment when material assumptions change; unaffected Evidence may be reused.

## Consequences

- No new L1-L A1/A2 type is introduced.
- Existing Contract/L1 semantics remain authoritative.
- Technology-specific packaging and UX mechanisms remain replaceable.
