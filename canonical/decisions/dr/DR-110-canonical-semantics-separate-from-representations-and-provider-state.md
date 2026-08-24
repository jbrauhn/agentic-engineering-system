# DR-110 — Keep canonical semantics separate from representations and provider-owned state

**Status:** Adopted  
**Decision Date:** 2026-08-21  
**Decision Authority:** Human Owner

## Context

Portable AE must remain usable across materially different Work Management, source control, CI/CD, observability, architecture, knowledge and developer environments.

Two recurring failure modes threaten that portability:

1. treating a serialized artifact/view as the canonical domain object; and
2. copying provider-owned operational state into AE until AE becomes a shadow database of organization tools.

The same concern applies to conformance: an editable profile field must not become an alternate truth source for an independent Validation judgment.

## Decision

Canonical AE separates **domain semantics** from both **representations** and **provider-owned resource state**.

### Product/System Baseline

- **Product/System Baseline — L1** is the A1 domain entity.
- A **Baseline Manifest** is a representation/snapshot of one exact Baseline revision.
- The Baseline references persistent constituent state; it does not own the Product/System Profile, Architecture Model, DR/ADRs, standards state, engineering-health state, or other durable entities merely because they form the baseline.

### Plan

- Plan is one A1 entity with exact revisions.
- Human-readable, machine-readable, interactive Plan IG and generated views may be multiple conforming representations of the same Plan revision.
- representation integrity must eventually allow correspondence to the exact Plan revision to be proven.

### Executable Task and Work Management

- Executable Task — L3 is canonical A1 work semantics.
- provider Work Item is externally authoritative/provider-owned state reached through an External Resource Reference.
- AE keeps only portable Task semantics it actually needs and shall not create a shadow Work Management database.
- property-level authority determines which provider fields remain authoritative.

### External Resource Reference

AE adopts a **generic canonical External Resource Reference core with capability-specific extensions**. The reference identifies provider/binding/resource context without copying the provider object's ownership into AE.

### Architecture

Architecture Model is the A1 domain entity. An architecture diagram/file/provider representation is not automatically the model ontology and may be authoritative representation, external reference, or derived view according to the declared source model.

### Evidence

Evidence Record is A2 canonical provenance/reference; evidence bytes/data may remain authoritative in external provider systems. Historical Evidence Records are not rewritten when later judged stale/invalid/inadequate.

### Context and handoff

Context Package is D-derived and disposable/reconstructable; Handoff Record is A2 durable continuation state. Consequential context provenance must remain reconstructable when required, but L1-C does not create a separate Context Provenance A1/A2 entity.

### Implementation Profile and conformance

AE Implementation Profile is the durable canonical representation of a socio-technical Organization-specific AE Implementation; it is not the running implementation itself.

Conformance is evidence-backed by applicable installation/adoption Validation Record(s). A profile field may project/display conformance but cannot create it through manual editing.

### Heterogeneous working environments

No `Engineering Environment Profile`, mandatory IDE, Dev Container, CLI, local daemon, agent host, or Portal is introduced by L1-C.

Open issue #6 preserves the design principle:

> **AE should require interface parity, not environment uniformity.**

## Alternatives considered

### Make provider objects the canonical domain

Reduces duplication initially but binds AE semantics to provider object models and breaks portability/replacement.

### Copy provider state into an AE-owned canonical database

Creates one queryable model but duplicates authoritative properties, creates synchronization conflicts, and contradicts DR-107 federated authority.

### Treat canonical files as the ontology

Easy to implement but couples semantics to Markdown/YAML/repository layout and confuses representation with identity.

### Separate canonical semantics from representation/provider state — selected

Preserves portability, source-of-truth clarity and future schema flexibility while still allowing executable provider integration.

## Consequences

1. later schemas represent canonical semantics, not provider replicas.
2. Capability Binding + External Resource Reference becomes the portable bridge to provider resources.
3. adoption tooling must distinguish the running implementation from its AE Implementation Profile.
4. conformance projection must resolve back to authoritative Validation records.
5. L1-G must define minimal durable context-provenance mechanics without turning Context Package into truth.
6. later developer-experience design must satisfy issue #6 through interface parity rather than environment uniformity.

## Traceability

- Contract v1.0: portability, Work Management, memory/state, architecture, evidence/Validation and adoption requirements.
- DR-025 — L1 Product/System baseline.
- DR-033 — one Plan with Human/machine representations.
- DR-040–043 — system memory, handoff, compaction.
- DR-060–062 — capability/provider boundary direction.
- DR-107 — federated authoritative state/property-level authority.
- L1-C Canonical Domain / Artifact Model.
- L1-C External Resource Reference Model.
- L1-C Planning Depth Domain Model.
- Open issue #6.