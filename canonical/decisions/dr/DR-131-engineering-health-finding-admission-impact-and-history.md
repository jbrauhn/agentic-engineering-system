# DR-131 — Engineering Health Finding admission, impact, and historical/current-state semantics

**Status:** Adopted  
**Date:** 2026-08-22

## Decision

Canonical AE adds **Engineering Health Finding [A2]** as a first-class durable record.

This explicitly extends the L1-C A2 catalog under DR-108; the historical L1-C baseline is not rewritten.

A finding represents an underlying engineering condition, not merely violation of a named framework. It carries durable identity because the condition can span Loops, remediation attempts, architecture/work scopes, Evidence, Decisions, and baseline revisions.

Portable health impact is:

- BLOCK;
- CONSTRAIN;
- DEGRADE;
- NONE_OBSERVE.

This is engineering-health effect and remains distinct from Capability Gap impact.

Issued findings are non-destructive historical records. Current disposition is derived from later authoritative facts and uses the smallest useful vocabulary:

- ACTIVE;
- DEFERRED;
- ACCEPTED_RISK;
- REMEDIATED;
- SUPERSEDED;
- QUALIFIED_UNKNOWN.

No universal numeric severity/maturity score is canonical.

## DR-108 admission rationale

Independent identity protects meaning because a material finding can:

- span multiple Loops;
- survive multiple remediation attempts;
- preserve independent Evidence/provenance/currentness;
- affect multiple architecture elements/resources;
- relate to multiple remediation work items/Contracts;
- remain relevant after the discovery session;
- be deferred, risk-accepted, remediated, superseded, or qualified without erasing history.

## Rejected alternatives

- Subordinate-only finding attached to one assessment: loses durable cross-loop remediation history.
- Universal health score/maturity tier: over-constrains organizations and hides the underlying condition.
- Framework-name findings: makes named practices accidental Canonical AE requirements.
- Rewrite finding after remediation: destroys historical truth.

## Traceability

Contract §§9–10, 12, 18 Proof K–L; DR-107; DR-108; L1-C durable-record semantics; L1-H routing; L1-I independent remediation Validation.