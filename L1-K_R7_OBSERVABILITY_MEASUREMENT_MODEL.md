# L1-K — R7 Observability and Measurement Model

**Status:** Human Owner-approved L1-K semantic baseline  
**Authority:** Contract v1.0; DR-101; DR-107; L1-D through L1-J; Human Owner L1-K approval

## 1. Purpose

R7 makes AE behavior and engineering outcomes observable enough to support evidence, experiments, decisions, learning, and improvement without making one telemetry product, dashboard, metric engine, or warehouse canonical.

> **Measurement is observation. Interpretation is a separate act.**

Canonical AE requires neutral, reproducible measurement semantics. It does not declare that faster, cheaper, fewer Loops, more automation, or any other direction is inherently better.

## 2. Federated R7 boundary

Raw operational data may remain authoritative in external provider systems `[C]`, including logs, traces, telemetry series, CI/CD timing, Work Management history, runtime events, model/provider usage, billing data, and product/engineering measurements.

R7 canonically owns the semantics needed to use those sources:

- measure definition and exact definition revision;
- purpose/question;
- population and scope;
- start/stop or time window;
- units;
- authoritative source/reference;
- computation/aggregation semantics;
- inclusion/exclusion rules;
- provenance;
- currentness/effectivity;
- data quality/completeness/known limitations;
- relationships to Evidence, Experiment, Decision, and Learning.

R7 does not require a central telemetry store or one observability service.

Dashboards, scorecards, reports, summaries, and analytics projections remain derived `[D]`. A display of a number does not become source authority merely because it is convenient for a Human or agent.

## 3. Measure definitions are subordinate [B]

Metric/measure definitions are versioned subordinate semantics coordinated through the applicable OEB, Product/System Profile, or other governed configuration. L1-K does not add a first-class Metric, Measurement, Observation, Metric Record, or Performance Report entity.

A governed measurement should be reconstructable enough that another capable actor can determine what was measured and how.

### Required semantic fields as applicable

- semantic measure ID/name;
- purpose/question;
- population/scope;
- canonical start/end or time window;
- units;
- source/provider reference;
- computation/aggregation semantics;
- inclusion/exclusion rules;
- exact definition revision/effectivity;
- data-quality/completeness limitations;
- provenance.

## 4. Canonical minimum measure categories

Canonical AE shall support at least:

1. **Total time to outcome** — explicit outcome scope and start/end semantics.
2. **Phase time** — identifies the canonical AE interval/phase semantics measured.
3. **Loop count** — derived from canonical AE Loop semantics rather than provider workflow labels.
4. **Failed Validation loops** — derived from canonical Validation/lifecycle history, not a provider's status vocabulary.
5. **Human effort** — measured, reported, estimated, or derived basis is explicit.
6. **Agent/model cost** — actual or estimated source/calculation basis, units/currency, and scope are explicit.
7. **Quality assessment** — method, scope, and Evidence/result basis are identifiable without one universal quality score.
8. **Organization-selected measures** — organizations/products may add measures relevant to their own outcomes and engineering questions.

These are required observability categories, not targets.

## 5. Lifecycle-derived measures

Where a measure depends on AE lifecycle timing or counts, canonical transition/history semantics are the semantic source. Jira/GitHub/provider status labels may be implementation inputs, but they cannot silently redefine canonical phase, Loop, retry, replan, Validation, or acceptance meaning.

## 6. Measurement versus Evidence

Provider telemetry or a computed metric is not automatically Evidence. When a measurement materially supports Contract Proof, Validation, Experiment, Decision, Engineering Health Finding, or Learning, the durable artifact must reference enough identity, scope, definition, provenance, integrity/currentness, and limitations for the reliance to be reconstructable.

Independent Validation remains responsible for Evidence sufficiency when measurement supports Contract Proof.

## 7. Neutrality and analysis

Canonical AE does not define:

- universal targets;
- universal ROI formula;
- universal performance score;
- universal quality score;
- a rule that lower time/cost or fewer loops is improvement.

ROI, tradeoff analysis, productivity analysis, and other organization-specific interpretations may be derived from governed measurements plus relevant outcome/value information.

## 8. Privacy, security, and minimization

Observability is governed engineering access, not universal surveillance.

Collection, access, retention, and derived use remain subject to identity, authority, classification/information handling, least privilege, policy, purpose, and retention rules.

Canonical AE does not require universal prompt logging or chain-of-thought retention. Collect and retain the information materially needed for governed engineering and measurement under applicable policy.

## 9. OEB / Product specialization

OEB may coordinate organization metric definitions/defaults, required categories, telemetry bindings, cost-accounting conventions, quality/outcome methods, experiment rigor defaults, retention/access rules, Learning promotion guidance, and organization-selected measures.

Product/System Profile may tighten, narrow, specialize, or add Product-specific requirements. It may not silently weaken higher Canonical, security, privacy, or authority constraints.

The effective observability/metric configuration is derived `[D]`, not a new A1 entity.
