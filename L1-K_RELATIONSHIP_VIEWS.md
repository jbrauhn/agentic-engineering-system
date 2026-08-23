# L1-K — Observability / Experiment / Learning Relationship Views

## 1. Federated measurement

```text
Provider telemetry / billing / CI / work history [C]
        ↓ referenced by
Metric definition / measurement semantics [B]
        ↓ may support
Evidence Record [A2] / Experiment [A1] / Health Finding [A2]
        ↓ may support
Validation / Decision / Learning Record [A2]
```

Dashboard/report `[D]` is a projection and does not replace the authoritative provider/reference chain.

## 2. Minimum measures

```text
Canonical lifecycle history ──→ total time / phase time / Loop and Validation counts
Provider effort sources ──────→ Human effort
Provider usage/billing ───────→ agent/model cost
Quality method + Evidence ────→ quality assessment
Organization sources ─────────→ additional measures
```

All retain explicit definition, scope, units, time, source, provenance, and limitations as applicable.

## 3. Experiment

```text
Question / hypothesis
  ↓
Experiment [A1] PROPOSED → ACTIVE → CONCLUDED
                         ↘ CANCELLED
  ↓
measurement definitions + provider observations/Evidence
  ↓
result + limitations
  ↓
conclusion bounded by design/Evidence strength
  ↓
Learning / Decision / follow-on Experiment
```

## 4. Loop learning disposition

```text
Loop closure
  ↓
learning disposition
  ├─ material Learning created
  ├─ existing Learning qualified/reinforced/superseded
  ├─ Experiment updated/concluded
  └─ no material learning identified
```

## 5. Governed feedback

```text
Learning Record
   ↓ informs
Recommendation / proposal
   ↓
Decision / ADR / governed configuration or work change
```

Learning does not self-authorize mutation. Pre-authorized adaptive behavior may execute only inside existing OA/policy/adaptation boundaries.

## 6. R7 boundary

R7 owns semantic meaning and durable Experiment/Learning relationships. External telemetry providers may own raw data. R2 remains authoritative-state ownership; R3 provides bounded context; R4 governs authority; R6 judges Evidence sufficiency/Validation. R7 does not become a central runtime or warehouse.
