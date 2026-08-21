# L1-B — State Ownership / System-of-Record Baseline

**Status:** Approved L1-B baseline  
**Authority:** Contract v1.0 system-owned-memory requirement + DR-019 + Human Owner L1-B decision  
**Scope:** Semantic ownership and authoritative-source rules. Detailed artifact schemas belong to L1-C.

## 1. Architectural invariant

AE uses **federated authoritative state with explicit semantic ownership**.

AE does **not** require one canonical database or one physical state repository.

> **For each material canonical state element and declared scope/version, a conforming AE implementation must be able to determine the authoritative source at that point in time.**

The implementation may use many physical systems of record, but it must operate under **one semantic ownership model**.

Distributed persistence must not become distributed ambiguity.

## 2. What “the system owns memory/state” means

AE owns the canonical meaning and governance of durable engineering state even when an organization-selected provider physically stores the authoritative record.

For material state, AE must be able to establish as applicable:

- what the state means in canonical AE;
- stable identity/reference;
- logical governing responsibility;
- authoritative source for the declared scope;
- current version/current-state semantics;
- allowed writers and applicable authority;
- provenance expectations;
- references/relationships to other AE state;
- conflict/precedence/reconciliation behavior where multiple systems participate;
- synchronization expectations where replicas/projections exist;
- what happens when sources disagree;
- how a current context can be reconstructed.

Replicas, indexes, search stores, projections, caches, vector representations, synchronized copies, and convenience views may exist. They must not silently become co-authoritative.

## 3. Authoritative-source declaration rule

For every material canonical state category, an Organization-specific AE Implementation must eventually be able to declare at least:

1. **Canonical state type/category** — what semantic AE state is being represented.
2. **Logical governing responsibility** — which R1–R7 responsibility governs its canonical meaning/ownership.
3. **Stable identity/reference mechanism** — how the state is uniquely/reliably referenced across systems and time.
4. **Authoritative source for the declared scope** — the source whose value wins for the specified property/scope/version.
5. **Allowed writers / authority** — who/what may change the authoritative state and under what governed authority.
6. **Version/current-state semantics** — how current, historical, draft, approved, superseded, or immutable versions are distinguished.
7. **Provenance expectations** — origin, change actor/path, rationale/evidence where applicable.
8. **Relevant references/relationships** — material links to Contract, Plan, architecture, work, decision, evidence, Validation, standards, capability bindings, etc.
9. **Conflict / precedence / reconciliation behavior** — what happens when several participating systems disagree or synchronized copies diverge.
10. **Synchronization expectations** — where replicas/projections must be refreshed and what staleness is acceptable, if relevant.

L1-B defines this semantic requirement. L1-C will determine the canonical domain/artifact model and machine-readable representation.

## 4. Initial state-ownership baseline

| State category | Logical governing responsibility | Example physical authoritative source(s) — not canonical | L1-B ownership meaning |
|---|---|---|---|
| AE Loop state / transition history | **R1** | Work Management; workflow state; canonical artifact store | R1 governs lifecycle meaning, gates, valid transitions, and provenance even if another system persists the value. |
| Contract / approved version / change proposal | **R2**, with decision authority through **R4** | Source Control; artifact repository | R2 governs identity/version/relationships; R4 supplies required approval/decision state. |
| Plan / Plan Review record | **R2**, lifecycle use through **R1** | Source Control; Work Management; artifact repository | Plan state must have stable identity/version and traceability to Contract, work, evidence and review outcome. |
| Architecture representations / relationships | **R2 — Architecture Model Stewardship** | Source Control; architecture repository; model store | Architecture remains governed first-class engineering state usable by humans/agents and traceable to engineering work. |
| Work item / dependency workflow state | **R2 semantic relationship**, provider may own operational property | Work Management provider | Provider can remain authoritative for selected workflow fields while AE owns canonical meaning/reference and cross-artifact relationship. |
| Decision / approval / OA-DA outcome | **R4** with durable identity/traceability through **R2** | Policy/identity system; Work Management; source-controlled decision artifact | Eligible authority, actor, proposal/rationale and approval/rejection must remain durably reconstructable. |
| Capability/provider binding | **R5** with identity/provenance through **R2** | Configuration repository; runtime config; integration registry | Binding states which provider/interface realizes a canonical operation for a declared scope. |
| Invocation result / operation provenance | **R5**, related through **R2/R7** | Provider audit log; integration log; observability backend; AE artifact | Must support reconstruction of canonical operation → bound provider operation → scoped result/denial where material. |
| Proof criteria / evidence relationships | **R6**, identity/traceability through **R2** | Contract artifact; CI/CD; evidence store; source control | R6 governs Proof-to-evidence evaluation relationship; physical evidence can remain in provider systems. |
| Validation result / rationale / provenance | **R6** | Validation provider; source control; artifact repository | Validation judgment state and independence provenance must be authoritative and routable to R1. |
| Standards applicability state | **R2** for durable state; later standards design refines governing mechanics | Standards/profile artifact; policy store | L1-B reserves durable identity/relationship hooks without defining applicability algorithms. |
| Context / handoff state | **R3** with source identities through **R2** | Knowledge/Memory provider; artifact store | Handoff/context records must point back to authoritative state and preserve enough provenance for continuation. |
| Metrics / experiment / learning results | **R7**, durable learning through **R2** | Observability backend; experiment artifact; knowledge store | R7 governs meaning/relationship to AE operation; concluded learning becomes durable system state. |

The table gives initial ownership boundaries, not final artifact schemas.

## 5. Property-level authority is allowed

One semantic object may legitimately span several systems when authoritative properties are explicit.

Example:

- Work Management may be authoritative for a work item's status, assignee, and dependency links.
- Source Control may be authoritative for the approved Plan artifact referenced by that item.
- R4-controlled decision state may be authoritative for whether a protected transition is approved.
- R1 remains authoritative for the **canonical meaning** of the corresponding AE Loop transition.

This is acceptable if the implementation declares which property/source wins and how the relationships are reconstructed.

It is not acceptable to say that “Git, Jira/Plane, chat, a vector database, and agent memory all contain the truth” without precedence and ownership semantics.

## 6. Conflict and disagreement rules

L1-B does not define every reconciliation algorithm, but every conforming implementation must have a deterministic policy for material disagreement.

At minimum:

1. identify the affected canonical state/property;
2. resolve the declared authoritative source for the relevant scope/version;
3. treat non-authoritative copies as stale, conflicting, or erroneous rather than silently merging them as equal truth;
4. preserve conflict/reconciliation provenance when material;
5. fail closed for protected actions/transitions when authoritative state or required authority cannot be established.

## 7. Context reconstruction requirement

R3 may use indexes, embeddings, caches, prior handoffs, summaries, or other implementation mechanisms, but context reconstruction must be anchored to authoritative or provenance-bearing state governed through this model.

Loss of a conversational session must not make material engineering state unrecoverable.

A fresh/replacement actor should be able to determine:

- current Loop/task;
- current Contract and relevant Plan;
- authoritative architecture/work/decision state;
- applicable authority/policy context;
- relevant evidence/Validation state;
- where each material fact came from.

## 8. Loop operability vs AE conformance

An isolated Loop may sometimes continue when an authoritative provider is temporarily unavailable by using permitted cached/contextual data or deferring a transition.

That does not erase the conformance obligation.

A conforming implementation must still demonstrate the full system-owned-state model, authoritative-source declarations, provenance/traceability, and deterministic behavior when sources disagree.

Detailed outage, staleness, Block/Constrain/Degrade, and recovery rules belong downstream.