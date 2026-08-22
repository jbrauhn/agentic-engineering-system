# L1-F — Distributed Enforcement / PEP / Bypass Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Distributed PEPs

PEPs may exist at or near:

- provider APIs;
- agent/runtime boundaries;
- brokers;
- gateways;
- source-control systems;
- CI/CD systems;
- deployment boundaries;
- data/service boundaries;
- other protected resources.

No centralized PEP is canonical.

## 2. Responsibility separation

- R4 coordinates authority/policy/decisions.
- R5 resolves/invokes Capability Bindings.
- PEP enforces the applicable authorization result and required conditions.

Policy decision ≠ PEP enforcement.

## 3. Enforcement Proof

For each protected canonical operation/binding, implementation Proof should identify as applicable:

- enforcement boundary;
- PEP/mechanism;
- authority/identity facts consumed;
- required obligations/conditions enforced;
- unauthorized-use denial evidence;
- fail-closed behavior when required authority cannot be established;
- materially equivalent bypass-path assessment for the governed actor/scope.

A PERMIT without an applicable enforceable boundary does not establish protected-operation Proof.

## 4. Bypass-path invariant

> **Protected-operation Proof must account for materially equivalent bypass paths available to the governed actor through the identities, credentials, Access Paths, and runtime/working context in the declared protected scope.**

If the governed integration denies an operation but the same governed actor/runtime can perform materially equivalent action through an ungoverned raw credential/interface, enforcement Proof fails unless the alternate path is equivalently governed.

## 5. Scope boundary

The bypass test does not require proof that:

- no enterprise administrator exists;
- the same Human has no separately governed administrator identity outside the runtime;
- no unrelated operational staff can access the resource.

The test concerns identities/credentials/access paths actually available to the governed actor in the declared execution context.

If the actor can switch to another identity within its governed runtime and bypass enforcement, that identity is relevant.
