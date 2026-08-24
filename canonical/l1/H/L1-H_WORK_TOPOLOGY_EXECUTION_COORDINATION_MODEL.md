# L1-H — Work Topology and Execution Coordination Model

## 1. Canonical work topology

Canonical AE describes governed relationships among work scopes without requiring a DAG engine, scheduler, queue, worker pool, swarm, branch strategy, or central orchestrator.

The topology supports, as applicable:

- L2 Execution Increments and L3 Executable Tasks;
- dependency edges;
- ordering constraints;
- barriers;
- independent branches;
- shared-resource/conflict declarations;
- merge/reconciliation points;
- scope-specific authority/capability differences;
- context boundaries;
- evidence aggregation/reconciliation.

The topology is semantic state. A provider graph or in-memory scheduler may project/use it but cannot be the only durable source of material work meaning.

## 2. Parallel execution

Independent ready scopes may execute concurrently.

A blocked branch does not automatically block unrelated valid work. Blocking propagates only through declared dependencies, barriers, shared-resource conflicts, safety constraints, or another explicit relationship making continuation invalid or unsafe.

Unsafe parallel continuation is prohibited when a shared dependency/resource conflict or barrier cannot be satisfied.

## 3. Dependency and barrier semantics

A dependency identifies a relationship in which one scope's valid progress/result affects another. A barrier expresses a condition that must be satisfied before a scope crosses a specified execution boundary.

A material dependency change affecting an executing scope triggers reassessment. If the reviewed route no longer remains valid, route to Replan rather than silently continuing.

## 4. Merge / reconciliation points

Parallel branches must have a defined reconciliation path when their results jointly affect architecture, shared resources, Proof/evidence, or Validation readiness.

Reconciliation may include source integration, dependency resolution, evidence aggregation, architecture consistency checks, or another implementation-specific mechanism. Canonical AE requires the semantic outcome, not one merge technology.

## 5. Execution coordination

Execution coordinates:

- readiness establishment;
- bounded worker/task dispatch;
- dependency/barrier awareness;
- authority/capability/context applicability;
- results/evidence/provenance;
- adaptation/route decisions;
- reconciliation and Validation readiness;
- durable promotion of material discoveries.

It does not require a canonical execution service or central coordinator.

## 6. Provider Work Management boundary

Provider workflow status may help coordinate execution but does not determine Canonical AE readiness, completion, or acceptance. Canonical Executable Task remains distinct from the provider Work Item that may realize it.
