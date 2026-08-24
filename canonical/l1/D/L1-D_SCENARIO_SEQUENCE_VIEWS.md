# L1-D — Lifecycle Scenario / Sequence Views

**Status:** Approved L1-D semantic baseline  
**Purpose:** Human-readable traces used to test the scoped lifecycle protocol. The machine fixtures provide executable counterparts.

## 1. Happy path

```text
Loop OPEN
  Contract rev2 approved
  Product/System Baseline rev8
  Increment A = PLANNING
      ↓ exact Plan rev4 + scope A passes Plan Review
  Increment A = READY
      ↓ required authority established
  Increment A = EXECUTING
      ↓ Tasks execute; provider Done may map to Task COMPLETE
      ↓ Evidence Records produced
  Increment A = VALIDATING
      ↓ independent Validation accepts Increment scope
  Increment A = terminal / ACCEPTED
      ↓ final independent Validation evaluates final Contract scope/rev2
      ↓ learning disposition completed
Loop CLOSED / ACCEPTED
```

## 2. Retry

```text
Increment A = VALIDATING
  Validation Record V1 = failed execution-level outcome
      ↓ RETRY_EXECUTION
Increment A = EXECUTING
  Contract rev2 remains valid
  Plan rev4 / scope A remains reviewed
      ↓ corrected work + new Evidence
Increment A = VALIDATING
  Validation Record V2 = accepted
Increment A = terminal / ACCEPTED
```

V1 remains immutable and traceable.

## 3. Replan

```text
Increment A = VALIDATING
  Validation V1 finds Plan defect
      ↓ REPLAN
Increment A = PLANNING
  Plan rev4 remains historical
  Plan Review rev4/scope A remains historical
      ↓ create Plan rev5
      ↓ review Plan rev5 / scope A
Increment A = READY
      ↓ authority
Increment A = EXECUTING
      ↓ new evidence
Increment A = VALIDATING
```

Rev4 review cannot satisfy rev5 execution.

## 4. Contract change with effectivity

```text
Loop OPEN
Contract rev2 approved

Increment A = EXECUTING
  governed by Contract rev2
  Plan rev4 / scope A reviewed

Increment B = PLANNING
  governed by Contract rev2

Finding: Goal/Spec/Proof issue affecting B
      ↓ Contract Change Proposal CCP-1
      ↓ Human Decision Authority approves
Contract rev3 approved

Effectivity determination:
  A = UNAFFECTED
      explicit determination permits A to continue under rev2
  B = AFFECTED
      B rebinds to rev3
      B remains/returns PLANNING
      new Plan revision + applicable review required

No scope silently switches Contract revision.
```

Before final `Loop CLOSED / ACCEPTED`, final Validation reconciles accepted work under rev2 and rev3 against the final applicable Contract scope.

## 5. Escalation

```text
Increment B = EXECUTING
  authority/uncertainty cannot be resolved locally
      ↓ ESCALATE
Increment B remains at its lifecycle position + blocking condition
Loop remains OPEN if A/C can continue
      ↓ eligible authority / decision / assistance resolves condition
      ↓ resume / Retry / Replan / Contract Change / Cancel / Supersede
```

If the unresolved condition prevents all meaningful governed continuation, Loop control may become `SUSPENDED` until resolved.

## 6. Stale Plan review — invalid

```text
Plan rev4 / scope A reviewed
Plan changes materially → rev5
Execution request uses rev5 / scope A
      ↓
G2 does not resolve for rev5
      ↓
DENIED or BLOCKED
```

## 7. Unauthorized protected transition — invalid

```text
Increment A = READY
Actor requests EXECUTING
G3 Authority = UNKNOWN or UNSATISFIED
      ↓
UNKNOWN ≠ SATISFIED
      ↓
BLOCKED or DENIED
```

No provider/runtime failure becomes implicit authorization.

## 8. Provider Done does not equal AE acceptance — invalid inference

```text
Plane issue ENG-491 = Done
      ↓ Capability Binding may map
Canonical Task = COMPLETE
      ↓
NO independent Validation Record
      ↓
Increment cannot become ACCEPTED
Loop cannot become ACCEPTED
```

## 9. Rolling-wave / parallel Increments

```text
AE Loop = OPEN
Contract rev2 approved
Baseline rev8

Increment A
  Plan rev4 / scope A reviewed
  EXECUTING

Increment B
  Plan rev5 being refined
  PLANNING

Increment C
  Plan rev3 / scope C reviewed
  VALIDATING
```

The scoped facts are canonical. A single Human-facing phase such as `Execution` is only a derived summary.

## 10. Pending Human Decision without Portal

```text
Current lifecycle position unchanged
+
blocking condition: decision_required
  target: exact Contract Change Proposal / revision / scope
  eligible authority: Human Decision Authority
  rationale/provenance
      ↓
Authority Decision issued through any conforming interface
      ↓
gate resolves
      ↓
next valid route
```

No approval screen, Portal inbox, CLI, or provider status is canonical.

## 11. Increment acceptance does not prove Contract acceptance

```text
Increment A = ACCEPTED
Increment B = ACCEPTED
Increment C = ACCEPTED
      ↓
NOT YET Loop ACCEPTED solely from count
      ↓
Final Validation Record evaluates final applicable Contract scope/revision
  reuses valid prior Evidence/Increment Validation
  adds integration/final evidence where needed
      ↓
G4 final acceptance satisfied
      ↓
learning disposition
      ↓
Loop CLOSED / ACCEPTED
```
