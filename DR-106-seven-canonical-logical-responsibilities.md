# DR-106 — Seven canonical logical responsibilities define the L1-B architecture baseline

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Contract v1.0 and DR-019 require a portable AE implementation that is operational and governable without mandating one centralized runtime or deployment topology.

L1-B therefore needs to define the minimum internal architecture in terms of required **logical responsibilities**, not implementation components.

A topology-first decomposition such as Planner Service, Executor Service, Validation Service, Memory Service, Policy Service, or Capability Gateway would turn lifecycle phases and design conveniences into accidental canonical components.

## Decision

Every conforming Organization-specific AE Implementation shall realize these seven **canonical logical responsibilities**:

1. **R1 — Lifecycle State & Transition Governance**
2. **R2 — Durable Engineering State, Identity & Traceability**
3. **R3 — Context & Knowledge Coordination**
4. **R4 — Authority, Policy & Decision Coordination**
5. **R5 — Capability Binding & Governed Invocation**
6. **R6 — Evidence & Validation Coordination**
7. **R7 — Observability, Metrics & Learning**

These responsibilities are not mandatory services, microservices, applications, databases, agent personas, runtimes, or products.

An implementation may combine several responsibilities into one mechanism, distribute one responsibility across several mechanisms, and use existing organization products/providers, provided the canonical responsibility semantics and applicable Proof remain satisfied.

> **Canonical logical responsibility ≠ implementation component.**

### Named sub-responsibility

**Architecture Model Stewardship** is a named sub-responsibility of R2 so architecture remains first-class governed engineering state without creating a canonical Architecture Service.

### Planning and Execution

Planning and Execution remain canonical lifecycle behaviors, not separate top-level L1-B architecture components. Humans/agents perform them through the seven responsibilities and bound capabilities.

### Validation independence

R6 must preserve an independent Validation judgment path from the work-producing execution path. Physical separation is not required at this architecture level; downstream Validation design defines risk/policy-specific independence.

## Alternatives considered

### Lifecycle-phase/component architecture

Create canonical Planner, Executor, Validator, Memory, Policy, and Gateway components.

**Rejected:** easy to visualize but prematurely freezes topology, agent persona assumptions, and runtime boundaries.

### Smaller collapsed responsibility set

Collapse context into durable state, authority into capability invocation, Validation into lifecycle, and observability into state.

**Rejected:** physical combination is allowed, but the semantic distinctions are material to Contract requirements and must remain independently testable.

### Larger responsibility set

Elevate architecture, standards applicability, policy enforcement, Planning, Execution, and dedicated agent roles into separate top-level responsibilities.

**Rejected:** those either belong as sub-domains/hooks, distributed boundary behavior, lifecycle behaviors, or roles rather than invariant internal responsibilities.

## Consequences

1. L1-C domain/artifact design must identify which responsibility governs each material state concept without turning responsibility boxes into stores.
2. Later lifecycle, authority, capability, context, Planning/Execution, and Validation design refine the semantics inside these responsibility boundaries.
3. Reference and organization-specific implementations must map real mechanisms/components to R1–R7 and prove the responsibilities operate.
4. Multiple materially different physical topologies can remain conforming.
5. Absence can be analyzed separately for Loop operability versus full AE conformance.
6. Policy Enforcement Points remain distributed boundary mechanisms rather than an eighth canonical responsibility/component.
7. Human Decision Authority must remain operable without the future Portal.

## Traceability

- Contract v1.0: Spec §§1–16, especially lifecycle, system-owned memory, capability model, authority/enforcement, Planning/Execution, Validation, and observability/learning.
- DR-017 — approved Contract baseline.
- DR-019 — logical/distributed AE implementation.
- L1-A System Identity & Boundary Baseline.
- L1-B Canonical Logical Responsibility Model.