# L1-B — Canonical Logical Responsibility Model

**Status:** Approved L1-B baseline  
**Authority:** Agentic Engineering System Contract v1.0 + DR-017 + DR-018 + DR-019 + Human Owner L1-B decision  
**Scope:** Minimum logical responsibilities that every conforming Organization-specific AE Implementation must realize. This document does not define deployable components or physical topology.

## 1. Core architectural distinction

**Canonical logical responsibility** = behavior, state stewardship, coordination, or control semantics that every conforming AE implementation must realize.

**Implementation component** = a concrete service, application, agent runtime, database, workflow engine, provider product, process, or other mechanism that realizes one or more canonical logical responsibilities.

> **Canonical logical responsibility ≠ implementation component.**

An organization may:

- combine several responsibilities into one implementation mechanism;
- distribute one responsibility across several mechanisms;
- realize responsibilities partly through existing organization products and External Capability Providers;
- choose different physical topologies from another conforming organization.

Conformance attaches to required behavior, semantics, authority, state, evidence, and Proof—not to accidental deployment topology.

## 2. Impact vocabulary used in L1-B

L1-B distinguishes two questions without attempting the later full Block / Constrain / Degrade model.

### Loop operability impact

Could a particular AE Loop technically continue if the responsibility were unavailable or materially impaired?

### AE conformance impact

Could the Organization-specific AE Implementation still satisfy the full approved Contract if the responsibility were unavailable or materially impaired?

A responsibility can therefore be non-blocking for one isolated engineering action while still being mandatory for AE conformance.

## 3. Canonical responsibility set

### R1 — Lifecycle State & Transition Governance

**Purpose**  
Govern the canonical state and valid transitions of an AE Loop without requiring a centralized workflow engine.

**Why it must exist**  
The Contract defines a governed lifecycle with explicit backward routes and Human Decision Authority gates. Without a canonical responsibility for state and transition semantics, lifecycle meaning can degrade into advisory prose interpreted differently by whichever actor or tool happens to be operating.

**Authority**  
Contract Spec §1, §2, §14, §15; DR-019 logical/distributed implementation.

**Inputs**

- current AE Loop state;
- Contract and Contract-change state;
- Plan / Plan Review state;
- required Human or other authority decisions;
- Validation result;
- applicable gates and constraints.

**Outputs**

- current canonical Loop state;
- permitted / denied transition;
- required gate or decision;
- Accept, Retry, Replan, Contract-change proposal, or Escalation routing;
- transition history and provenance.

**State governed or referenced**

- Loop state;
- transition history;
- gate satisfaction state;
- references to decision and Validation outcomes.

**Major interactions**

- R2 for durable state and traceability;
- R4 for authority and decision outcomes;
- R6 for Validation outcomes;
- Human Owner, Engineering Practitioner, AI Agent, and Independent Validator roles.

**Likely capability dependencies**  
Work Management, Knowledge / Memory, Identity & Access, Validation; implementation-specific additional capabilities may apply.

**Authority / enforcement implications**  
R1 must not manufacture authority. A protected transition is allowed only when the required decision/authority state is established through R4 and enforceable implementation boundaries.

**Evidence made possible**  
Reconstructable lifecycle position, transition rationale, decision/gate provenance, backward-route history.

**Absence impact**

- Loop operability: a task might still be performed ad hoc, but canonical lifecycle control is not reliable.
- AE conformance: **not conforming**; canonical lifecycle semantics cannot be demonstrated.

**Logical distinctness**  
R1 is canonically distinct as a semantic responsibility. It may be physically combined with work-management workflows, an agent runtime, artifact state, or other mechanisms.

---

### R2 — Durable Engineering State, Identity & Traceability

**Purpose**  
Govern the canonical meaning, stable identity, authority/source relationships, versioning, provenance, and traceability of durable AE engineering state.

**Why it must exist**  
The Contract states that the system owns memory and that durable knowledge/workflow state cannot depend on one agent or conversation. Distributed physical persistence is acceptable; ambiguous semantic ownership is not.

**Authority**  
Contract Spec §3, §9, §11, §12, §13; Proof B/C/M; DR-019.

**Inputs**

- Contracts and versions/change proposals;
- Plans and review records;
- architecture representations and references;
- work/dependency references;
- decisions and ADRs;
- evidence and Validation references;
- standards-applicability state;
- capability-binding references;
- durable learning and experiment records.

**Outputs**

- stable identities/references;
- authoritative-source declarations;
- current-version semantics;
- provenance;
- relationships and traceability;
- retrievable durable engineering state.

**State governed or referenced**  
Cross-cutting durable AE state and its semantic ownership. Physical records may remain authoritative in bound organization systems.

#### Architecture Model Stewardship — named R2 sub-responsibility

Architecture is first-class governed engineering state, not a generic storage concern. R2 must preserve architecture representations that are:

- identifiable;
- versioned/provenanced where appropriate;
- relational;
- usable by humans and agents;
- retrievable into context;
- traceable to Contracts, Plans, work, decisions, evidence, and Validation;
- maintainable when architecture-significant change occurs according to later design.

This does **not** imply a separate Architecture Service or architecture repository.

**Major interactions**  
All other responsibilities depend on R2's identity, source-of-truth, provenance, and relationship semantics.

**Likely capability dependencies**  
Source Control, Work Management, Knowledge / Memory; other providers may physically hold authoritative records.

**Authority / enforcement implications**  
Allowed writers, authoritative source, and change authority must be knowable for material state.

**Evidence made possible**  
Traceable intent → plan → work → evidence → Validation; resumability and state reconstruction.

**Absence impact**

- Loop operability: an isolated task may proceed using local context or provider state.
- AE conformance: **not conforming**; system-owned durable state and traceability cannot be demonstrated.

**Logical distinctness**  
R2 is distinct from R3: R2 answers what authoritative durable state exists, what it means, and how it relates. R3 answers what trustworthy subset is needed now and how it is packaged for an actor.

---

### R3 — Context & Knowledge Coordination

**Purpose**  
Construct bounded, trustworthy, task-relevant context from system-owned state and relevant permitted external knowledge; support structured handoff and continuation/resumption.

**Why it must exist**  
Durable state alone does not ensure usable agent/human context. AE must survive conversational loss and must not rely on an indefinitely accumulating session.

**Authority**  
Contract Spec §3, §11, §14; Proof M.

**Inputs**

- Loop/task identity;
- R2 authoritative state and relationships;
- architecture and decision context;
- standards/policy context as applicable;
- prior handoffs/evidence;
- permitted external knowledge.

**Outputs**

- bounded context packages;
- structured handoffs;
- continuation/resumption context;
- provenance-aware retrieval results.

**State governed or referenced**

- context/handoff records;
- references to authoritative source state;
- context-construction provenance where material.

**Major interactions**  
R2, planning/execution actors, R4, R6, R7.

**Likely capability dependencies**  
Knowledge / Memory, Source Control, Work Management, Models; Identity & Access may constrain retrieval.

**Authority / enforcement implications**  
Context construction must respect access, classification, resource, task, and policy boundaries.

**Evidence made possible**  
A fresh or replacement actor can reconstruct sufficient context without hidden conversation history.

**Absence impact**

- Loop operability: improvised context may allow a single task to continue.
- AE conformance: **not conforming** if resumability/system-owned-context obligations are not met.

**Logical distinctness**  
R3 is not a vector database, RAG product, context window, or memory technology. It may be realized through any suitable combination.

---

### R4 — Authority, Policy & Decision Coordination

**Purpose**  
Coordinate and preserve identity/actor context, Operational Authority (OA), Decision Authority (DA), policy outcomes, proposals/rationale, approval/rejection, and Human decision gates.

**Why it must exist**  
The Contract requires enforceable governed authority and explicit Human Decision Authority without assuming any one user interface.

**Authority**  
Contract Spec §2, §6, §14; L1-A actor/role model; DR-019.

**Inputs**

- authenticated actor identity/context;
- requested decision or protected operation/transition;
- OA/DA and organization policy context;
- resource/task/Contract scope;
- proposal and rationale;
- prior approval state.

**Outputs**

- authority/policy decision state;
- approval/rejection;
- eligible authority requirement;
- escalation requirement;
- decision provenance consumable by R1 and R5.

**State governed or referenced**

- decision/approval records;
- actor/authority association;
- proposal/rationale provenance;
- policy outcome references.

**Major interactions**  
Human Owner, Organization Governance / Policy Authority, R1, R5, R2.

**Likely capability dependencies**  
Identity & Access, Governed Tool Access, Work Management and/or Knowledge / Memory for durable decision records.

**Authority / enforcement implications**  
R4 coordinates policy/authority decisions. It is **not** the universal Policy Enforcement Point (PEP). Enforcement may occur at provider, broker, runtime, or protected-resource boundaries.

**Evidence made possible**  
Who approved/rejected what, under what authority and scope, with preserved rationale/provenance.

**Absence impact**

- Loop operability: unprotected work may technically proceed.
- AE conformance: **not conforming** for a system that cannot establish/gate required authority or Human decisions.

**Logical distinctness**  
No canonical approval UI is required. CLI, API, source-controlled decision artifact, work-management interaction, enterprise approval product, future Portal, or other interface may realize the interaction.

---

### R5 — Capability Binding & Governed Invocation

**Purpose**  
Translate canonical AE capability operations into organization-specific provider operations and support their governed invocation under scoped authority.

**Canonical translation**

`canonical AE operation → organization binding → scoped authorized provider operation → result/evidence`

**Why it must exist**  
Technology-neutral capability semantics cannot become real engineering operations unless an implementation maps them to actual provider interfaces and can invoke those interfaces under governed authority.

**Authority**  
Contract Spec §2, §6, §7, §18, §19; DR-019.

**Inputs**

- canonical capability operation;
- provider binding/configuration;
- actor/task/Contract/resource scope;
- R4 authority/policy outcome as required;
- provider interface/entitlement context.

**Outputs**

- scoped provider invocation;
- result/denial/error;
- operation provenance/evidence;
- updated references/state where applicable.

**State governed or referenced**

- capability binding definitions;
- operation mappings;
- provider/interface references;
- invocation provenance.

**Major interactions**  
R4 for authority decisions; R2 for binding/state identity; agents/humans; all External Capability Providers; PEPs at protected boundaries.

**Likely capability dependencies**  
Potentially all ten canonical capabilities. Identity & Access and Governed Tool Access are especially cross-cutting.

**Authority / enforcement implications**  
R5 does not imply one central gateway or network hop. It carries/uses scoped authority and reaches provider operations through whatever conforming mechanism exists. PEPs perform actual enforcement at/near protected boundaries.

**Evidence made possible**  
Which canonical operation was bound to which provider operation, under what scope/authority, and with what result.

**Absence impact**

- Loop operability: agents may still perform manual/unstructured integrations, often with human mediation.
- AE conformance: **not conforming** when required canonical operations cannot be bound and used by authorized agents as required.

**Logical distinctness**  
Binding and governed invocation are one canonical responsibility. Authorization decision (R4) and enforcement (PEP) remain logically distinct.

---

### R6 — Evidence & Validation Coordination

**Purpose**  
Maintain Proof-to-evidence traceability, preserve Validation judgment independence, record Validation outcomes/provenance, and route outcomes back into lifecycle governance.

**Why it must exist**  
Independent Validation is Contract-level and the doer may not become its own judge.

**Authority**  
Contract Spec §1, §12, §15; Proof D/E/H/O.

**Inputs**

- Contract Proof;
- execution/verification evidence;
- relevant architecture/state/context;
- Validator identity/role and applicable authority;
- risk/policy context as applicable.

**Outputs**

- Validation result;
- rationale and evidence relationships;
- Validation provenance;
- Accept/Retry/Replan/Contract-change/Escalation outcome supplied to R1.

**State governed or referenced**

- Proof/evidence relationship;
- Validation record/state;
- Validator provenance and independence-relevant references.

**Major interactions**  
Independent Validator role, R1, R2, R3, R4, R7.

**Likely capability dependencies**  
Validation, CI/CD, Source Control, Observability, Work Management, Knowledge / Memory, Identity & Access.

**Authority / enforcement implications**  
The Validation judgment path must be logically independent from the work-producing execution path. This does not require physical infrastructure separation, a dedicated product, or a permanent Validator persona.

**Evidence made possible**  
A reconstructable judgment showing how Proof was evaluated against evidence and by what independent path.

**Absence impact**

- Loop operability: execution may technically occur.
- AE conformance: **not conforming**; Independent Validation cannot be demonstrated.

**Logical distinctness**  
R6 may share physical infrastructure with execution but must preserve independent judgment semantics. Detailed risk-based independence rules are downstream.

---

### R7 — Observability, Metrics & Learning

**Purpose**  
Define AE semantics for operational observation, measurement, experiments, failures/outcomes, and how concluded learning becomes durable system state.

**Why it must exist**  
The Contract requires AE to make its own operation observable enough to evaluate outcomes and preserve meaningful learning.

**Authority**  
Contract Spec §16, §17; Proof A/B/N; Goal quality wording.

**Inputs**

- lifecycle events;
- provider/invocation events;
- Validation outcomes and failures;
- time/cost/quality observations;
- experiment evidence and conclusions.

**Outputs**

- AE operational measures;
- experiment/result records;
- findings;
- durable learning inputs to R2/R3;
- evidence for later system improvement decisions.

**State governed or referenced**

- metric/measurement semantics;
- experiment/result records;
- concluded learning and related provenance.

**Major interactions**  
R1, R2, R5, R6, Human Owner / implementation team.

**Likely capability dependencies**  
Observability, Knowledge / Memory, Work Management, CI/CD; Models may assist analysis but are not required as the meaning of R7.

**Authority / enforcement implications**  
Metrics are diagnostic unless later evidence and approved decisions promote them into policy or gates.

**Evidence made possible**  
Measured AE outcomes, loop/phase behavior, experiment evidence, quality-protection evidence, durable learning.

**Absence impact**

- Loop operability: one isolated engineering action may still occur.
- AE conformance: **not conforming**; the approved Contract's observability/learning requirements are unsatisfied.

**Logical distinctness**  
External Observability Providers collect/store telemetry. R7 defines what AE observations mean and how they relate to Loops, artifacts, experiments, outcomes, and learning.

## 4. Responsibilities intentionally not elevated to top-level canonical responsibilities

### Planning / Execution Coordination

Planning and Execution remain canonical lifecycle behaviors, not mandatory architecture components. Human/agent actors perform them using R1–R7 and bound capabilities. No canonical Planner Service, Executor Service, Planner Agent, or Executor Agent is implied.

### Architecture / Engineering Model

Architecture remains first-class governed state through **Architecture Model Stewardship within R2**. L1-B does not establish a separate Architecture Service.

### Standards Applicability

L1-B provides state/relationship hooks through R2/R3/R4/R6. Detailed applicability mechanics belong downstream.

### Policy Enforcement

Enforcement is performed through distributed PEPs at protected boundaries; it is not one mandatory AE component. R4 coordinates policy/authority decisions and R5 performs governed use/invocation.

### Planner / Executor / Validator agents

These are roles or possible actor/agent instances, not canonical components. Role ≠ actor ≠ model ≠ agent instance ≠ authority.

### Central Memory Store

Rejected as canonical topology. AE requires durable, reconstructable state with explicit semantic ownership, not one database.

### Capability Gateway

Rejected as mandatory topology. R5 requires binding/invocation semantics but not one gateway or universal network hop.

## 5. Implementation-team mapping rule

An implementation team shall eventually be able to map:

`Canonical logical responsibility → organization mechanism(s) → External Capability Provider(s) → authoritative state/source → governed interfaces/authority → implementation Proof`

Different mappings may conform when they preserve the same canonical responsibility semantics.