# L1-E — Capability Binding Model

**Status:** Approved L1-E semantic baseline  
**Domain object:** Capability Binding [A1]

## 1. Purpose

A Capability Binding maps a Canonical Capability Contract to organization technology/mechanisms for a declared scope.

Bindings are:

- many-to-many;
- scope-aware;
- versioned;
- provider-specific below the canonical operation layer;
- capable of exposing multiple governed access paths.

One provider may realize several canonical capabilities. One capability may have multiple bindings across products, repositories, environments, classifications, resources, or other declared scopes.

## 2. Minimum semantics

A binding identifies, as applicable:

- binding identity/revision;
- Canonical AE Release and Capability Contract reference;
- provider/mechanism reference;
- scope selector;
- canonical-operation → provider-operation mapping;
- Access Path Descriptors;
- provider/source-of-truth authority semantics where relevant;
- readiness/Proof Validation references;
- provenance.

## 3. Deterministic Binding Resolution

A canonical operation + declared scope resolves to exactly one deterministic **binding plan**.

Normally that plan contains one Capability Binding.

A binding plan may contain an explicitly declared composition of several bindings where the canonical semantic operation genuinely requires composition.

Composition must be:

- explicit;
- deterministic;
- scope-correct;
- semantics-preserving;
- traceable to the bindings/providers actually used.

Binding Resolution remains runtime/subordinate semantics unless later identity/lifecycle evidence justifies promotion under DR-108.

## 4. Ambiguity is invalid configuration

If multiple candidate bindings claim the same canonical operation/scope and no deterministic resolution exists:

> **The configuration is invalid.**

AE shall not:

- try providers until something works;
- select whichever responds first;
- silently switch source of truth;
- silently change authority semantics.

## 5. Provider fallback

Fallback is organization implementation policy, not a universal Canonical Capability Contract feature.

Configured fallback must preserve:

- canonical semantic result;
- deterministic selection;
- identity/authority semantics;
- source-of-truth rules;
- evidence/provenance.

No opportunistic failover.

## 6. Access Path Descriptor [B]

Each binding may contain subordinate Access Path Descriptors identifying:

- access-path scoped identity;
- canonical operations exposed;
- interface/mechanism description;
- deterministic discovery information;
- identity-context requirements;
- supported consumer/runtime context selectors or constraints;
- reachability/readiness Evidence references;
- provenance.

L1-E deliberately does not freeze an environment taxonomy such as Dev Container, IDE, CI runner, remote workspace, or headless agent.

> **AE should require interface parity, not environment uniformity.**

For every required agent-accessible operation and declared supported consumer/runtime context, at least one governed, deterministic, discoverable, proven access path must exist.

## 7. Capability discovery

An authorized actor/runtime must be able to determine without trial-and-error:

- applicable Canonical Capability Contract;
- resolved binding/binding plan;
- supported canonical operations;
- applicable access path;
- declared scope;
- identity/access requirements;
- current authorization prerequisites;
- expected result/evidence semantics.

Discovery may use configuration, local machine-readable metadata, runtime service, API, MCP, or another mechanism. No central registry is canonical.
