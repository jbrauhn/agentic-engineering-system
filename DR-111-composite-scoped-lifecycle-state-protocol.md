# DR-111 — Canonical AE uses a composite/scoped lifecycle-state protocol

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

The canonical lifecycle is often shown as:

`Context → Contract → Planning → Review → Execution → Validation → Learning/closure`.

That projection is useful to humans but is insufficient as canonical state truth because one AE Loop may contain multiple L2 Execution Increments and L3 Tasks in different governed positions at the same time.

A single exclusive Loop phase would either prohibit legitimate rolling-wave/parallel work or force implementations to hide real lifecycle state in provider-specific exceptions.

## Decision

Canonical AE uses a **composite/scoped lifecycle-state protocol**.

Canonical lifecycle truth is composed from:

- Loop control state;
- scope-specific lifecycle position;
- artifact/revision state;
- gate evaluation backed by authoritative records;
- blocking conditions;
- routes/dispositions;
- exact governing revisions;
- non-destructively reconstructable transition history.

### Loop control

Loop control states:

- OPEN;
- SUSPENDED;
- CLOSED.

A CLOSED Loop has terminal disposition:

- ACCEPTED;
- CANCELLED;
- SUPERSEDED.

### L2 Execution Increment

Active lifecycle positions:

- PLANNING;
- READY;
- EXECUTING;
- VALIDATING.

Terminal disposition is orthogonal:

- ACCEPTED;
- CANCELLED;
- SUPERSEDED.

Blocking is also orthogonal.

### L3 Executable Task

Portable canonical execution projection:

- NOT_STARTED;
- ACTIVE;
- COMPLETE.

Provider workflow remains provider-owned; Task COMPLETE does not establish independent Validation or higher-scope acceptance.

### Derived phase

A Human-facing `current phase` may be derived from scoped state, but it is not canonical truth and may not override the underlying lifecycle facts.

## Alternatives considered

### One exclusive Loop finite-state machine

Advantages: simple visualization and implementation.

Rejected as canonical truth because it cannot faithfully represent concurrent Planning, Execution, and Validation scopes without either contradiction or serialized workflow behavior.

### Let each provider define lifecycle state

Advantages: minimal Canonical Core modeling.

Rejected because replacing Work Management/runtime technology would change AE meaning and provider `Done` could be mistaken for governed acceptance.

## Consequences

1. R1 governs lifecycle semantics without implying one workflow engine.
2. One Loop can legitimately contain different active Increment positions.
3. provider status may map/project canonical state through Capability Bindings but does not own AE lifecycle semantics automatically.
4. later Human views may summarize state without becoming authoritative.
5. issue #6 remains compatible because lifecycle semantics do not require one interface/runtime/environment.

## Traceability

- Contract v1.0 lifecycle and bounded Execution/Validation semantics.
- DR-019 — logical/distributed implementation.
- DR-106 — R1 Lifecycle State & Transition Governance.
- DR-107 — federated authoritative state.
- DR-108–110 — domain categories, exact revisions, provider/representation separation.
- Human Owner L1-D Decision D1–D4, D8, D10–D12.
