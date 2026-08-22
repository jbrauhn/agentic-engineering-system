# DR-114 — Capability Contracts separate implementation readiness from runtime authorization

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

Contract v1.0 requires canonical capability operations, agent-accessible interfaces, scoped entitlements, authority/policy enforcement, and implementation Proof. A single `available=true` or `capability=conforming` flag cannot distinguish provider support, agent-operability, current actor authority, or proven behavior.

## Decision

Canonical AE uses three layers:

1. Canonical Capability Contract Definition [F];
2. Organization Capability Binding [A1];
3. runtime request authorization/use.

Binding readiness is evaluated by operation/scope/context using:

SUPPORTED, BOUND, DISCOVERABLE, REACHABLE, ENTITLEABLE, ENFORCEABLE, PROVEN.

Each dimension evaluates SATISFIED / UNSATISFIED / UNKNOWN / NOT_APPLICABLE and must resolve to evidence/provenance where relevant. PROVEN resolves to applicable Validation/Evidence.

Runtime authorization separately evaluates identity, current entitlement, OA/applicable DA/policy, PEP enforcement, provider condition, and execution using L1-D ALLOWED / DENIED / BLOCKED semantics.

`agent_access_required` means a governed machine-accessible path is usable by or on behalf of an appropriately authorized agent; it does not prescribe direct provider calls or credential handling.

Capability assessment uses Validation Record + Evidence Records + subordinate findings. No new Capability Assessment A2 record is introduced.

## Consequences

- a healthy binding may correctly deny an actor;
- broad admin credentials do not prove entitleability or agent-operability;
- Human Decision Authority remains legitimate Human work;
- routine Human transcription for required agent operations is a capability deficiency;
- Work Management direct governed agent administration is mechanically testable.

## Traceability

Contract §§2, 6, 7, 15, 18–19; DR-106 R4/R5/R6; DR-107; DR-108–110; DR-111–113; Human Owner L1-E D1–D7, D11–D15.
