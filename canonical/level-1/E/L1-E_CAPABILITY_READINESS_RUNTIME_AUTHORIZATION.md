# L1-E — Capability Readiness and Runtime Authorization

**Status:** Approved L1-E semantic baseline

## 1. Installation/binding readiness

Evaluate readiness per Capability Binding + operation + declared scope + supported consumer/runtime context.

Dimensions:

- **SUPPORTED** — the provider/mechanism can technically perform the canonical semantic operation.
- **BOUND** — the organization implementation has mapped the canonical operation for the declared scope.
- **DISCOVERABLE** — applicable binding/access path can be deterministically discovered.
- **REACHABLE** — a governed machine-accessible path is reachable from the declared supported context.
- **ENTITLEABLE** — the provider/access model can grant the required least-privilege scoped entitlement without relying on broad administrator authority.
- **ENFORCEABLE** — protected use can be constrained at an applicable PEP/boundary.
- **PROVEN** — Evidence/Validation demonstrates actual usable behavior.

Each dimension evaluates to:

- **SATISFIED**
- **UNSATISFIED**
- **UNKNOWN**
- **NOT_APPLICABLE**

These values are projections/assessment results, not independently editable truth.

SATISFIED must resolve to supporting provenance/evidence where relevant. `PROVEN = SATISFIED` must resolve to applicable Validation/Evidence.

For required protected operations:

> **UNKNOWN must not silently become SATISFIED.**

## 2. Runtime request admissibility

Readiness does not answer whether a particular actor can invoke the operation now.

Runtime evaluates:

1. identity established;
2. current provider/system entitlement;
3. current Operational Authority and applicable Decision Authority/policy;
4. applicable PEP enforcement;
5. provider operational condition;
6. provider execution;
7. result/evidence.

Outcome:

- **ALLOWED** — established facts permit execution and applicable enforcement permits it.
- **DENIED** — established facts forbid the request.
- **BLOCKED** — potentially valid request cannot proceed because required state/authority/capability cannot currently be established.

## 3. Critical distinctions

- **ENTITLEABLE ≠ currently entitled**
- **currently entitled ≠ Operational Authority**
- **Operational Authority ≠ Decision Authority**
- **policy decision ≠ PEP enforcement**
- **broad administrator capability ≠ agent-operability**
- **runtime DENIED ≠ unhealthy binding**
- **provider outage ≠ automatically failed installation Proof**

A transient outage may BLOCK current work while the historical binding Validation remains valid. Persistent availability/reliability problems may later create a readiness deficiency through new evidence/Validation.
