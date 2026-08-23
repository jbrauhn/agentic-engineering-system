# DR-130 — Standards source, applicability, effectivity, and exception semantics

**Status:** Adopted  
**Date:** 2026-08-22

## Decision

Canonical AE references authoritative standards/practices without becoming a standards repository.

Standards applicability remains subordinate **[B]** semantics associated with versioned OEB/Product/work scope and authoritative references.

Requirement character supports at least:

- MANDATORY;
- CONDITIONAL;
- ADVISORY;
- REFERENCE.

Applicability and application/disposition remain distinct. `DOES_NOT_APPLY`, advisory proportional omission, authorized exception/waiver, nonconformance/not-demonstrated, and unresolved applicability are not interchangeable.

Exact/effective source version governs. Newer versions do not silently rebase active/historical work.

Exceptions/waivers reuse existing authority/decision semantics and require eligible authority, exact scope/version, provenance, and effectivity where applicable.

Applicable standards may constrain Planning/Architecture/Verification/Evidence/Validation but do not become a second Contract or silently rewrite Contract Proof.

## Rationale

This satisfies Contract §13 while preserving technology neutrality, federated source authority, proportional engineering judgment, and the established no-silent-rebase model.

## Rejected alternatives

- Copy all standards into AE: creates shadow authority and portability problems.
- One universal compliance checklist: contradicts context-aware applicability and proportionality.
- First-class Applicability Determination entity: independent identity is not currently needed beyond versioned profile/work-scope semantics.
- Latest-version-wins: destroys historical/effectivity reconstruction.

## Traceability

Contract §§5, 12–15; DR-107; DR-108; DR-116; L1-F authority; L1-G currentness/source authority; L1-H routing; L1-I Evidence/Validation.