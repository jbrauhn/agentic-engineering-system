# L1-G — Handoff, Continuation & Reconstruction Model

**Status:** Human Owner-approved L1-G semantic baseline  
**Domain:** existing Handoff Record [A2]; reconstruction/resumption protocol

## 1. Handoff Record remains A2

L1-G does not create a second handoff entity.

Handoff Record is authoritative as the issued record of what was handed off at that time. It is **not** authoritative for the current state of referenced Contract, Plan, Architecture, policy, authority, or provider state.

The receiving actor resolves authoritative references and detects later changes.

## 2. Handoff semantics

A Handoff Record supports as applicable:

- Handoff identity;
- sender/issuing actor;
- intended continuation scope / receiving actor class where relevant;
- issued time;
- Loop / Increment / Task;
- work being continued;
- current governed position at issuance;
- blockers;
- next meaningful action;
- unresolved questions/risks;
- material results since the prior continuation point;
- exact reconstruction anchors for material Contract, Plan/review scope, Baseline, Architecture, OEB/Profile, Decisions, Authority, Evidence/Validation;
- Context Assembly Receipt / provenance reference when required;
- explicit uncertainty / known stale items.

A later source change does not destructively rewrite an old Handoff.

## 3. Conditional requirement

A Handoff A2 is not required for every model invocation or worker call.

Handoff is conditionally required when responsibility/continuation crosses a meaningful actor/session boundary and material continuation state exists that is not adequately reconstructable from other system state alone.

Small worker returns may remain normal result/evidence/provenance semantics.

## 4. Replacement actor reconstruction

A fresh or replacement actor must be able to reconstruct materially equivalent governing understanding from system-owned state, including as applicable:

- controlling exact/effective revisions;
- current work/lifecycle state;
- material Decisions;
- Architecture constraints;
- applicable authority/capability constraints;
- Evidence/Validation state;
- blockers/unresolved material questions.

It need not reproduce identical prose, prompts, token context, reasoning path, or supporting retrieval results.

## 5. Fresh, continuing, and replacement actors

Continuing agents are allowed. Fresh-agent replacement is not mandatory at every lifecycle phase.

Conformance requires that continuation not depend on hidden session state surviving.

A continuing actor and a replacement actor operating from the same authoritative state may have different supporting context, but materially different governing anchors or blockers must be detectable as a reconstruction defect.

## 6. Stale Handoff detection

A Handoff can become stale for a new continuation attempt when referenced governing revisions/effectivity/currentness changed after issuance.

The correct behavior is to resolve the references, detect the difference, and reconstruct current/effective context—not to treat copied Handoff prose as current truth.
