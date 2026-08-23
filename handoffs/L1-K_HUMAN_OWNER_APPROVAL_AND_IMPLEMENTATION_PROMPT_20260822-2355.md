# Handoff: L1-K Human Owner Approval and Implementation Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving implementation/design session: read this file completely before acting. This is the Human Owner approval for **L1-K — Observability, Metrics, Experiments & Learning**. Implement against the current `main` baseline and follow `handoffs/README.md` when creating the next relay handoff.

---

# 1. Human Owner decision

The Human Owner **APPROVES all five L1-K design recommendations** from the independent reviewer, plus the measurement clarification below.

Implementation is authorized subject to the inherited Contract, L1-A through L1-J decisions, and the guardrails in this handoff.

Do not reopen approved semantics without a material contradiction, failed executable proof, or independent-review finding. If a genuine Contract contradiction appears, stop and surface it rather than silently changing the approved design.

The prior closure/design handoff is:

`handoffs/L1-K_L1-J_CLOSURE_AND_OBSERVABILITY_METRICS_LEARNING_DESIGN_PROMPT_20260822-2147.md`

Preserve its inherited baseline, issue #6/#12 status, entity-admission discipline, portability requirements, privacy/security constraints, and failure tests.

---

# 2. Human Owner clarification — measurement semantics

The Contract-listed measures are **required neutral observability data points**, not normative claims about what direction is good.

Canonical AE must support measurement of at least:

- total time to outcome;
- phase time;
- Loop count;
- failed Validation loops;
- Human effort;
- agent/model cost;
- quality assessment;
- organization-selected additional measures.

The purpose is to establish enough trustworthy data that an organization can answer questions such as:

- overall engineering cost;
- potential ROI;
- time-to-outcome differences;
- experiment results;
- process effectiveness;
- quality/outcome tradeoffs;
- model/context/planning/execution comparisons.

Canonical AE does **not** state that faster, cheaper, fewer loops, more automation, or any other direction is inherently better.

A measurement is an observation. Its interpretation depends on the question, context, comparison, and relevant Evidence.

Do not introduce:

- universal target values;
- a universal AE performance score;
- a universal ROI formula;
- a rule that lower time/cost automatically means improvement.

ROI and other organization-specific analyses may be derived from these measurements plus relevant value/outcome information.

---

# 3. Approved Decision 1 — federated R7 boundary

Approve a **federated R7 semantic boundary**.

Raw/provider-owned operational data may remain authoritative in external systems/resources `[C]`, including as applicable:

- logs;
- traces;
- telemetry events/series;
- runtime observations;
- model/provider usage and billing records;
- CI/CD timing/results;
- Work Management timestamps/state history;
- other provider measurements.

Canonical R7 owns the **semantic meaning needed to use those sources**, including:

- measurement/metric definition and scope;
- units/time windows/population;
- provenance/source/currentness;
- experiment relationships;
- Evidence relationships;
- interpretation/learning promotion;
- durable Learning/Experiment semantics.

R7 does **not** require a central telemetry warehouse or one observability service.

Dashboards, scorecards, summaries, and analytics views remain derived `[D]` unless a later DR-108 admission establishes an independent identity need.

When provider telemetry becomes material to Proof, Validation, Experiment, Decision, or Learning, the durable AE artifact must reference it with sufficient scope/provenance/definition/currentness to reconstruct what was relied upon.

Do not copy all raw telemetry into Canonical AE merely for self-containment.

---

# 4. Approved Decision 2 — metric definitions are versioned subordinate semantics; no new Metric entity

Do **not** add a new first-class `Metric Definition`, `Metric Record`, `Measurement Record`, `Observation`, `Performance Report`, or similar A1/A2 entity unless implementation produces a genuine DR-108 independent-identity case.

Metric/measure definitions should initially be versioned subordinate `[B]` semantics coordinated through the appropriate OEB/Product-System/configuration context.

A meaningful governed measure should resolve, as applicable:

- semantic measure/metric ID or name;
- purpose/question;
- population/scope;
- start/stop or time window;
- units;
- authoritative source/provider reference;
- computation/aggregation semantics;
- inclusion/exclusion rules;
- exact definition revision/effectivity;
- data quality/completeness/known limitations;
- provenance.

For **quality assessment**, Canonical AE requires that quality/outcome assessment be measurable and its method/result identifiable, but it must not impose one universal quality score or quality model.

For **Human effort**, measured, reported, estimated, or otherwise derived values may be valid if the basis is explicit.

For **agent/model cost**, actual or estimated values may be valid if the calculation basis, units/currency, scope, and provider/source basis are explicit.

Metric values may remain provider-owned/external or derived until materially referenced as Evidence or used by Experiment/Learning/Decision semantics.

---

# 5. Approved Decision 3 — Experiment [A1] lifecycle and proportional rigor

Operationalize existing **Experiment [A1]** with the smallest useful lifecycle:

- `PROPOSED`
- `ACTIVE`
- `CONCLUDED`
- `CANCELLED` as a terminal exit where appropriate.

An inconclusive experiment is still `CONCLUDED`; inconclusive describes the result, not a separate lifecycle state.

An Experiment should preserve, as applicable:

- stable Experiment identity;
- question/hypothesis;
- scope/context;
- baseline/comparator where meaningful;
- intervention/change under study;
- measurement plan;
- Evidence/observations/provider references;
- limitations/confounders/uncertainty;
- result;
- conclusion;
- resulting Learning/Decision/ADR/configuration relationships;
- provenance and relevant revisions/currentness.

An ACTIVE Experiment may evolve its setup/measurement plan where governed and traceable, but material changes must be versioned/provenanced so prior observations are not silently reinterpreted.

Once CONCLUDED, issued result/conclusion/history is non-destructive. Later evidence may qualify, supersede, or overturn current reliance through later authoritative records rather than rewriting history.

Preserve the invariant:

> The strength of an Experiment conclusion must not exceed the strength of the Experiment design and Evidence.

Do not canonize one statistical, scientific, randomized, A/B, or causal method. Rigor must be proportional to the question and Evidence needed.

Preserve DR-102: comparison of governed AE against lighter workflows is an Experiment, not predetermined proof that AE is superior.

Do not create first-class Experiment Run/Observation entities unless DR-108 later proves an independent lifecycle need.

---

# 6. Approved Decision 4 — Learning Record [A2] materiality threshold

Do **not** create a Learning Record for every Loop, metric movement, observation, Validation result, or Experiment update.

Use the Human Owner-approved materiality test:

> **Would losing this evidence-backed conclusion materially reduce the quality of future engineering decisions?**

Potential future decisions include, as applicable:

- Planning Depth/Method;
- architecture;
- context strategy;
- capability/provider choices;
- standards/practices;
- model placement/routing;
- execution topology;
- engineering practice;
- validation strategy;
- governance/policy proposals;
- other material AE or engineering decisions.

A material `Learning Record [A2]` should preserve, as applicable:

- conclusion;
- supporting Evidence/source/Experiment/Loop/Validation/Finding/incident/other discovery;
- scope/conditions under which the learning is believed to apply;
- confidence/limitations/uncertainty;
- provenance;
- currentness/effectivity where meaningful;
- what future decisions/work it informs;
- relationships to later qualification, reinforcement, contradiction, supersession, Decision, ADR, OEB/Product changes, or future Experiments.

Loop closure retains the inherited **learning disposition** requirement but must not manufacture ceremonial A2 records.

Minimum useful disposition semantics should support outcomes equivalent to:

- material Learning Record created;
- existing Learning Record qualified/reinforced/superseded where meaningful;
- Experiment updated/concluded where relevant;
- **no material learning identified**.

Use the smallest semantic vocabulary that proves these outcomes without artifact theater.

---

# 7. Approved Decision 5 — Learning informs governed change; no opaque self-modification

A Learning Record is **informative, not self-authorizing**.

Canonical feedback path should remain equivalent to:

```text
Measurement / Evidence / Experiment
    ↓
Learning Record (when material)
    ↓
recommendation / proposal / decision input
    ↓
normal governed Decision / ADR / OEB / Product Profile / Plan / other authorized change mechanism
```

Learning by itself must not silently mutate:

- Contract;
- OEB;
- Product/System Profile;
- capability binding;
- standards profile;
- authority or policy;
- Planning Method/Depth;
- model routing/placement;
- context strategy;
- execution topology;
- Validation semantics;
- other governed canonical/organization state.

**Pre-authorized adaptive behavior is allowed** when the adaptation remains inside explicit Operational Authority/policy/adaptation boundaries that were established through normal governance.

Example: an organization may authorize a bounded rule allowing a lower-cost model for a defined low-risk work class when declared conditions are met. The system may then adapt inside that approved boundary with appropriate provenance, observability, and reversibility/monitoring where material.

An AI actor may not use its own metrics/learning to expand its authority, weaken policy, redefine Contract success, or self-authorize consequential changes.

This permits adaptive AE without creating an opaque self-modifying engineering system.

---

# 8. Inherited observability / Evidence / privacy semantics to implement, not reopen

Preserve inherited semantics:

- provider telemetry/metrics are not automatically Evidence;
- a dashboard/screenshot/summary does not become authoritative merely because it displays a number;
- material telemetry becomes usable Evidence when referenced with sufficient identity, scope, definition, provenance, integrity/currentness, and relevant limitations;
- independent Validation determines Evidence sufficiency when telemetry/metrics support Contract Proof;
- metric/dashboard success is not independent Validation by itself;
- Context/retrieval/index summaries do not become telemetry/metric/Learning authority;
- later-discovered stale/invalid/incomplete telemetry does not destructively rewrite historical Experiment/Evidence/Learning records; later qualification/correction changes current reliance explicitly;
- observability remains subject to identity, authority, classification/information handling, least privilege, policy, and retention rules;
- Canonical AE must not require universal prompt logging;
- Canonical AE must not require chain-of-thought retention;
- observability must not become universal surveillance;
- collect/retain the information materially needed for governed engineering and measurement, subject to applicable organization policy.

---

# 9. OEB / Product-System specialization

OEB may coordinate/reference, as applicable:

- organization metric definitions/defaults;
- required measurement categories;
- telemetry/provider source bindings;
- cost-accounting conventions;
- quality/outcome assessment conventions;
- experiment governance/default rigor expectations;
- information-handling/retention/access constraints;
- Learning promotion/materiality guidance;
- organization-selected engineering/product measures.

Product/System Profile may tighten, narrow, specialize, or add Product-specific metrics/telemetry/experiment constraints.

It may not silently weaken mandatory higher security, privacy, authority, or Canonical measurement semantics.

Effective metric/observability configuration remains derived rather than a new A1 entity.

---

# 10. Canonical minimum measures — implementation intent

Implement Contract §16 named measurement categories as a portable minimum semantic set.

The implementation must demonstrate that materially different provider stacks can produce equivalent canonical meaning for these measures without requiring identical tools or calculation plumbing.

Do not encode provider workflow labels as canonical lifecycle truth.

Where lifecycle timing/counts are derived from canonical AE lifecycle state, use canonical transition/history semantics as the semantic source rather than vendor labels.

Examples:

- total time to outcome should be resolvable against an explicit start/end/outcome scope rather than an ambiguous elapsed number;
- phase time should identify which canonical phase/interval is measured;
- Loop count/retry/replan/failed Validation counts should derive from canonical AE lifecycle semantics rather than Jira/GitHub/provider status names;
- Human effort should expose its measurement/estimate basis;
- agent/model cost should expose provider/source and calculation basis;
- quality assessment should expose the assessment method/Evidence basis without requiring one universal numeric score.

The measures exist to support analysis; interpretation remains a separate governed/experimental step.

---

# 11. Entity-admission decision

Existing canonical identities remain sufficient for L1-K unless executable design proves otherwise:

- `Experiment [A1]`
- `Learning Record [A2]`
- `Evidence Record [A2]`
- provider telemetry/resources `[C]`
- dashboards/projections `[D]`
- subordinate metric/measurement definitions `[B]`

Leading implementation posture: **no new A1/A2 L1-K entity**.

If implementation reveals a genuine independent lifecycle/identity need, explicitly run DR-108 reasoning and return to the Human Owner rather than adding the entity silently.

---

# 12. Machine/reference implementation authorization

Implement a staged machine/reference L1-K layer consistent with ADR-002 through ADR-008 patterns, likely with cohesive names equivalent to:

- `observability_learning_protocol.json`
- `observability_learning_scenarios.json`
- `observability_learning_portability_fixtures.json`
- `validate_observability_learning.py`
- `.github/workflows/observability-learning-integrity.yml`

Exact cohesive naming may vary.

Human semantic artifacts remain normative for meaning. JSON/Python/GitHub Actions/telemetry providers remain repository/reference implementation choices, not Canonical AE technology requirements.

If a new `observability-learning-integrity` job is created, update issue #12 to track it as the eighth integrity job and keep issue #12 OPEN until GitHub repository protection/rulesets actually require applicable checks and a deliberate failing-check merge-block test proves enforcement.

Keep issue #6 OPEN. L1-K must not mandate one Portal, CLI, IDE, Dev Container, telemetry UI, analytics platform, runtime, or developer environment.

---

# 13. Minimum machine/falsification scenarios

The machine/reference layer should cover at least these semantic classes, expanded where implementation/review finds gaps:

1. Contract minimum measures are representable with explicit scope/unit/time/source/provenance semantics;
2. measurements remain neutral data and no rule treats faster/cheaper as automatically better;
3. ROI can be derived externally/organizationally without a universal Canonical ROI formula;
4. raw provider telemetry does not automatically become canonical Learning;
5. raw provider telemetry does not automatically become Evidence;
6. dashboard/summary does not become authoritative source by itself;
7. provider telemetry can remain external while durable AE artifacts preserve material reference/provenance;
8. ambiguous denominator/scope/time window cannot support a claimed comparison;
9. stale/wrong-scope/incomplete telemetry cannot silently support current Learning/Experiment conclusions;
10. lifecycle timing/count metrics use canonical lifecycle semantics rather than provider labels;
11. Human effort exposes measured/reported/estimated basis;
12. agent/model cost exposes source/calculation basis and remains provider-neutral;
13. quality assessment is required without one universal quality score;
14. organization-selected measures coexist with Canonical minimum measures;
15. no new Metric/Measurement/Observation A1/A2 is required for normal operation;
16. Experiment has stable A1 identity and small approved lifecycle;
17. ACTIVE Experiment material changes remain versioned/provenanced;
18. CONCLUDED Experiment history is non-destructive;
19. inconclusive result can still conclude an Experiment;
20. causal/strength claims cannot exceed design/Evidence;
21. lighter-baseline comparison remains Experiment rather than predetermined AE win;
22. raw Experiment observations do not each require a first-class entity;
23. Learning Record requires material evidence-backed conclusion;
24. trivial/noisy metric movement does not force Learning Record;
25. Loop can close with `no material learning identified`;
26. Learning may arise from Experiment, Loop, Validation failure, incident, side quest, Health remediation, or other material discovery;
27. Learning does not silently mutate Contract/OEB/Profile/Plan/Capability Binding/standards/policy/model routing/context/execution topology;
28. pre-authorized low-risk adaptive behavior can operate inside explicit OA/policy/adaptation boundaries;
29. adaptation cannot self-expand authority or weaken policy;
30. learning-informed consequential change routes through normal Decision/ADR/authority/change semantics;
31. learning/experiment provenance survives actor/session loss;
32. later invalid telemetry/Evidence qualifies/supersedes current reliance without rewriting historical records;
33. observability access/classification/security constraints prevent unauthorized exposure;
34. no universal prompt logging is required;
35. no chain-of-thought retention is required;
36. provider metric/result is not independent Validation by itself;
37. Engineering Health Finding may consume metric Evidence without tool score becoming the finding;
38. two materially different telemetry/analytics/experiment implementations produce equivalent canonical measurement/Experiment/Learning semantics;
39. no central Observability/R7 service or telemetry warehouse is required;
40. no convenience metric/report entity inflation without DR-108.

---

# 14. Portability Proof

Use at least two materially different synthetic implementations.

Implementation A may use an OpenTelemetry/Grafana-like topology, source-controlled metric definitions, agent-assisted Experiment analysis, model/runtime provider cost metadata, and Learning Records in durable engineering knowledge.

Implementation B should use a materially different enterprise telemetry/SIEM/APM/analytics topology, different timing/cost sources, Human+tool experiment analysis, different dashboard/storage mechanisms, and different provider semantics.

Equivalent canonical meaning must preserve:

- measure definition/scope/time/unit;
- source/provenance/currentness/limitations;
- Contract minimum measure semantics;
- neutral interpretation boundary;
- Experiment identity/hypothesis/setup/Evidence/result/conclusion;
- material-learning threshold;
- Learning provenance/scope/limitations;
- non-destructive history/current reliance;
- Decision/change relationships;
- bounded pre-authorized adaptation;
- information-handling rules.

Do not require identical telemetry provider, metric engine, dashboard, statistical method, model/provider, storage system, billing model, or quality model.

---

# 15. Independent review requirements

Before merge, perform independent review against Contract v1.0, L1-A through L1-J, DR-107/108, and the Human Owner approvals above.

At minimum challenge:

1. required measurements accidentally encode a preferred direction/value;
2. faster/cheaper is treated as automatic AE success;
3. one universal ROI/performance/quality score appears;
4. every telemetry point becomes canonical state;
5. dashboard becomes source of truth;
6. R7 becomes a mandatory centralized service;
7. provider-specific telemetry/analytics technology becomes Canonical;
8. provider metric is confused with Evidence or Validation;
9. metric lacks scope/window/unit/source but still supports a claim;
10. every Loop produces ceremonial Learning Record;
11. every Experiment observation becomes first-class entity;
12. Experiment history is destructively rewritten;
13. causal certainty exceeds design/Evidence;
14. governed AE is assumed superior rather than experimentally evaluated;
15. Learning silently mutates governed state;
16. AI actor self-modifies authority/core behavior from its own metrics;
17. stale/invalid telemetry remains current authority without qualification;
18. historical Learning/Experiment records are rewritten after contradiction;
19. observability requires prompt/chain-of-thought retention;
20. telemetry leaks information beyond authorization/classification;
21. one telemetry warehouse/provider is required for conformance;
22. health tool score auto-becomes Health Finding;
23. Learning replaces Decision/ADR semantics;
24. Experiment replaces normal lifecycle/authority;
25. new A1/A2 exists only for implementation convenience;
26. Human effort/cost/quality definitions are too vague to reproduce;
27. provider workflow labels replace canonical lifecycle timing/count semantics;
28. pre-authorized adaptation can escape its approved boundary.

Correct material findings before merge and record independent-review evidence in the PR discussion/review record.

---

# 16. Decision/ADR grouping

Do not manufacture a DR for each bullet.

Likely minimum coherent grouping:

1. R7 federated observability/measurement/metric semantic boundary and Canonical minimum measures;
2. Experiment A1 lifecycle, measurement integrity, and conclusion semantics;
3. Learning Record materiality, Loop learning disposition, and governed feedback/adaptation semantics;
4. ADR for machine-readable observability/learning protocol and integrity CI.

Adjust only if implementation review identifies a genuinely independent consequential decision. Check current Decision Register identifiers before assigning numbers.

---

# 17. Authorized implementation sequence

Proceed with the normal governed implementation pattern:

```text
1. verify current main / inherited L1-A through L1-J decisions
2. verify DR-100 through DR-105 current authority/status
3. create L1-K implementation branch
4. implement human semantic R7/measurement artifacts
5. implement Canonical minimum measurement semantics
6. implement Experiment A1 lifecycle/integrity semantics
7. implement Learning A2 materiality/disposition/feedback semantics
8. implement OEB/Product specialization and privacy/security hooks
9. implement machine protocol/scenarios/portability fixtures
10. implement validator
11. add observability-learning integrity workflow
12. run all applicable inherited + new integrity checks
13. update issue #12 to track new job and keep it OPEN
14. keep issue #6 OPEN
15. perform independent review/falsification
16. correct material findings
17. open PR
18. verify applicable integrity jobs on exact final PR head
19. merge only after review/evidence is clean
20. verify main at merge commit
21. write the complete next handoff to a new unique file under `handoffs/` on `ae-session-relay`
```

Do not merge `ae-session-relay` into `main`.

---

# 18. Closure / next handoff requirements

After L1-K is complete, the next relay handoff must include at least:

- PR number/title;
- exact tested PR head;
- merge commit;
- final L1-K semantic artifacts;
- final Canonical minimum measure definitions/semantics;
- final R7/provider boundary;
- Experiment A1 lifecycle/result/history semantics;
- Learning A2 threshold/disposition/feedback semantics;
- bounded adaptation semantics;
- privacy/security/data-minimization treatment;
- OEB/Product specialization;
- machine protocol/validator/workflow;
- scenario and portability counts;
- all applicable CI results on exact head;
- independent-review findings and corrections;
- issue #12 status;
- issue #6 status;
- final DRs/ADR;
- whether any Contract contradiction or new A1/A2 entity need emerged;
- the next genuine L1 domain/design question.

The Human-facing completion response should remain very short: one short summary plus the next handoff title/repo/branch/exact path.

---

# 19. Human Owner collaboration rule for future gates

For future Human Owner decision gates, package decisions for human review concisely.

Each consequential decision should state:

- the question in plain language;
- the recommendation;
- only the minimum explanation/tradeoff needed to decide.

Do not require the Human Owner to read long design memos when a concise decision package is sufficient.

The Human Owner will approve or challenge each item as required.

Follow `handoffs/README.md` for all subsequent relay traffic.