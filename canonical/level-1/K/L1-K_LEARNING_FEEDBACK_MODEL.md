# L1-K — Learning, Loop Disposition, and Governed Feedback Model

**Status:** Human Owner-approved L1-K semantic baseline

## 1. Learning Record threshold

`Learning Record [A2]` is for material evidence-backed conclusions, not routine logging.

Materiality test:

> **Would losing this evidence-backed conclusion materially reduce the quality of future engineering decisions?**

If no, a new Learning Record is not required.

## 2. Learning sources

Material Learning may arise from:

- Experiment;
- AE Loop outcome;
- Validation failure;
- incident;
- side quest / evidence-backed discovery;
- Engineering Health remediation;
- architecture or operational evidence;
- other governed engineering discovery.

A metric movement by itself is not Learning.

## 3. Learning Record semantics

A material Learning Record preserves, as applicable:

- conclusion;
- supporting Evidence/source/Experiment/Loop/Validation/Finding/incident references;
- scope and conditions where the conclusion is believed to apply;
- confidence/limitations/uncertainty;
- provenance;
- currentness/effectivity where meaningful;
- future decisions/work it informs;
- later reinforcement/qualification/contradiction/supersession relationships;
- related Decision, ADR, OEB/Product, Plan, standards, capability, model/context/execution, or future Experiment relationships.

Issued Learning Records are non-destructive historical records. Later contradiction changes current reliance through later authoritative records; it does not erase what was concluded earlier.

## 4. Loop learning disposition

L1-D's Loop-closure learning disposition remains required, but it does not require ceremonial A2 creation.

Minimum disposition semantics:

- `MATERIAL_LEARNING_CREATED`
- `EXISTING_LEARNING_QUALIFIED_REINFORCED_OR_SUPERSEDED`
- `EXPERIMENT_UPDATED_OR_CONCLUDED`
- `NO_MATERIAL_LEARNING_IDENTIFIED`

The disposition is a closure fact, not itself a new first-class Learning entity.

## 5. Learning is informative, not self-authorizing

Canonical feedback path:

```text
Measurement / Evidence / Experiment
    ↓
Learning Record (when material)
    ↓
recommendation / proposal / decision input
    ↓
normal governed Decision / ADR / OEB / Product / Plan / other authorized change mechanism
```

Learning alone cannot silently mutate Contract, OEB, Product/System Profile, Capability Binding, standards, authority/policy, Planning Method/Depth, model routing, context strategy, execution topology, Validation semantics, or other governed state.

## 6. Bounded pre-authorized adaptation

Adaptive behavior is allowed when a prior governed decision has established explicit Operational Authority, policy, scope, conditions, and adaptation boundaries.

An implementation may, for example, choose a lower-cost model for a defined low-risk class when the approved policy says the conditions are met. The adaptation must remain within that boundary and preserve material provenance/observability and reversibility/monitoring where required.

An AI actor cannot use its own measurements or Learning to expand its authority, weaken policy, redefine Contract Proof, or authorize a consequential change outside the prior boundary.

## 7. Current reliance

Later invalid, stale, incomplete, or contradictory telemetry/Evidence may qualify or supersede current reliance on Experiment/Learning conclusions. Historical Experiment, Evidence, Validation, and Learning records remain intact.

## 8. DR-105 operationalization

DR-105 remains adopted: the system learns from completed work. L1-K operationalizes this as durable material Learning plus governed feedback, not opaque self-modification.
