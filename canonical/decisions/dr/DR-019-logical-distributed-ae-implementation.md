# DR-019 — Canonical AE defines a logical system boundary, not a mandatory centralized runtime

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Organizations use materially different source-control, work-management, CI/CD, identity, policy, runtime, observability, knowledge/memory, validation, model, and tool ecosystems.

AE must remain portable while still being more than documentation. Requiring one centralized AE control-plane product would simplify implementation topology but would bind canonical AE to an architecture pattern that evidence may later show is inappropriate for some organizations.

## Decision

The Canonical AE System defines a **logical system/runtime boundary and required behavior**, but does **not** require one mandatory centralized physical AE runtime or control-plane product.

An Organization-specific AE Implementation may distribute AE behavior across multiple organization systems and External Capability Providers.

A distributed realization is conforming only when it preserves applicable canonical:

- lifecycle semantics;
- artifact/state semantics;
- authority and enforcement behavior;
- Capability Contracts and required agent-accessible operations;
- durable-state requirements;
- evidence and Validation model;
- installation/adoption Proof.

> **Logical/distributed does not mean documentation-only.**

Part 1 must provide executable/reference behavior sufficient to prove that canonical AE can be instantiated, operated, governed, checked, and validated.

## Alternatives considered

### Mandatory centralized AE runtime/control plane

Advantages include a tangible deployment unit, simpler central enforcement, and potentially simpler lifecycle orchestration.

Disadvantages include reduced portability, premature topology lock-in, and unnecessary duplication of enterprise capabilities already provided by organization systems.

### Logical/distributed AE implementation — selected

Canonical behavior and interfaces remain stable while physical topology can adapt to organization constraints and later evidence.

## Consequences

1. External Capability Providers remain separate products/services while participating operationally through governed bindings.
2. Provider physical boundaries do not imply absence from AE's operational environment.
3. The future Portal cannot become a hidden mandatory runtime dependency.
4. Architecture must define logical responsibility and enforcement semantics clearly enough that distributed implementations remain recognizably AE.
5. Conformance requires demonstrated operation, not copied documentation.
6. L1-B must design logical architecture before selecting any reference physical topology.

## Traceability

- Contract v1.0: Goal; Spec §2, §4, §6, §18, §19; Proof I and M; Non-Goals.
- L1-A System Identity & Boundary Baseline.
