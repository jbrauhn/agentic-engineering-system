# DR-133 — Federated R7 measurement semantics and neutral minimum measures

**Status:** Adopted

## Decision

Canonical AE uses a federated R7 boundary. Raw telemetry/operational measurement may remain authoritative in provider systems `[C]`; R7 owns portable measurement definitions, scope/unit/time/source/provenance/currentness/limitations, Experiment relationships, and Learning promotion semantics.

Metric/measurement definitions remain subordinate `[B]`; dashboards/reports remain derived `[D]`. No new Metric/Measurement/Observation/Performance Report A1/A2 is admitted.

Canonical AE shall support neutral measurement of total time to outcome, phase time, Loop count, failed Validation loops, Human effort, agent/model cost, quality assessment, and organization-selected measures.

These are observations, not targets. Faster, cheaper, fewer Loops, or more automation are not automatically better. No universal ROI/performance/quality score is introduced.

## Rationale

The Contract requires measurable system performance but portability requires provider-neutral semantics. Making each metric point canonical state would duplicate telemetry systems and create false authority.

## Consequences

Lifecycle-derived measures use canonical lifecycle semantics rather than provider labels. Material measurement used for Evidence/Experiment/Learning/Decision preserves reconstructable source/definition/provenance/currentness. Privacy/security/retention remain governed and no prompt/chain-of-thought logging requirement is created.

## Relationship to earlier decisions

Operationalizes adopted DR-101. DR-100 remains provisional terminology and is not promoted by this decision.
