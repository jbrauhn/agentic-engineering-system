# L1-H — Planning / Execution Relationship Views

## 1. Core governed route

```text
Approved Contract revision
        │
        ▼
Plan revision
  ├─ plans against exact Product/System Baseline
  ├─ affects Architecture elements/relationships
  ├─ derives Verification/Test Strategy from Proof
  ├─ defines adaptation/elaboration boundaries
  └─ decomposes to L2/L3 work
        │
        ▼
Plan Review exact revision + scope
        │
        ▼
Execution readiness
        │
        ▼
Parallel / bounded execution
        │
        ├─ local adaptation inside reviewed boundary
        ├─ Retry if route remains valid
        ├─ Replan if reviewed route changes
        ├─ Contract Change if Goal/Spec/Proof changes
        └─ Escalate unresolved authority/risk/decision
        │
        ▼
Verification + Evidence reconciliation
        │
        ▼
Independent Validation
```

## 2. Rolling-wave view

```text
AE Loop OPEN

Plan rev4 / scope A reviewed ──► Increment A EXECUTING

Plan rev5 / future scope B ────► Increment B PLANNING

Plan rev3 / scope C reviewed ──► Increment C VALIDATING
```

Later revision B does not invalidate A unless explicit dependency/impact analysis shows A is affected.

## 3. Parallel dependency view

```text
Branch A ──┐
           ├─► reconciliation point ─► Validation-ready evidence set
Branch B ──┘

Branch C ──blocked by shared resource──X
Branch D ──independent────────────────► continues
```

Blocking propagates through meaningful dependencies/barriers, not by default to the whole Loop.

## 4. Worker context/result view

```text
Parent governed scope
   │
   ├─ Context Requirement
   ├─ exact Contract / reviewed Plan / Baseline
   ├─ dependency + authority/capability boundary
   └─ Verification/evidence expectation
           │
           ▼
      worker/subagent
           │
           ▼
result + evidence + blockers + material signals
           │
           ├─ routine result → execution coordination
           ├─ Plan deficiency → Replan signal
           ├─ Contract deficiency → Contract Change Proposal signal
           ├─ architecture decision → ADR/architecture owner
           └─ continuation boundary → Handoff when required
```

## 5. Source-of-truth view

- Plan exact revision: declared authoritative source under R2;
- Work provider: selected operational work properties;
- CI/runtime: provider run state/results;
- Evidence: Evidence Record/reference semantics;
- lifecycle state: R1 canonical semantics;
- authority: R4/L1-F authoritative sources;
- context: R3 derived Context Package;
- orchestration queue/session: derived/ephemeral coordination state.

No queue, scheduler, agent session, Context Package, or provider `Done` status becomes canonical Planning/Execution truth merely because it is convenient.
