# Agentic Engineering System — Contract v1.0

**Status:** Approved  
**Human Owner Decision:** Approved 2026-08-21  
**Scope:** Part 1 — Canonical Agentic Engineering System  
**Lifecycle Context:** Inception / Architecture → Initial Build

> **Canonical AE System — the authoritative, technology-neutral definition of Agentic Engineering.**

## Goal

Create a **canonical, portable, technology-neutral Agentic Engineering System** that enables organizations to perform governed Human–AI engineering from **Loop Context and Contract through Planning, Execution, evidence, independent Validation, and learning**.

The System must provide enough engineering structure, semantics, interfaces, enforcement, reference behavior, and validation that an implementation team—human or agentic—can adopt and implement AE without first inventing its own method for Agentic Engineering.

The AE System must preserve human judgment, authority, accountability, engineering discipline, and appropriate controls while using AI agents to substantially increase engineering speed, scale, and automation **without sacrificing—and where evidence supports it, improving—engineering quality**.

Part 1 shall produce a **versioned canonical AE System distribution that can be handed directly to an implementation team**.

---

# Spec

## 1. Canonical AE lifecycle

The System shall define the lifecycle and semantics for:

**Work arrives → Loop Context → Contract → Architecture-aware Planning → Plan Review → Bounded Execution → Independent Validation → Learning / durable system state**

Validation shall support controlled outcomes including:

- Accept
- Retry execution
- Replan
- Propose Contract change
- Escalate

Agents may identify the need for a Contract change and propose one at any point where new evidence justifies it.

Agents may not silently redefine an approved Contract or approve their own Contract changes where Human Decision Authority applies.

**The doer shall not become its own judge.**

## 2. Human–AI authority and governed enforcement

The Human Owner remains part of the engineering system.

AE shall explicitly distinguish:

- technical access from Operational Authority;
- Operational Authority from Decision Authority;
- an action an agent can technically perform from an action it is authorized to perform;
- agent recommendations from decisions reserved to humans or another authorized decision authority.

Humans retain authority over intent, material risk acceptance, consequential tradeoffs, Contract approval/change, and other decisions assigned to Human Decision Authority.

AI agents operate as **thinking partners and executors** within governed boundaries.

Authority shall not exist only as documentation.

Where an action is protected, appropriate technical or procedural boundaries shall be capable of enforcing:

- identity;
- resource scope;
- permitted operation;
- task or Contract scope;
- relevant policy;
- time or condition limitations where applicable;
- required approval state.

Where required authority cannot be established, protected operations shall **fail closed** rather than assuming permission.

Possession of credentials or technical capability shall not by itself imply authority.

## 3. The system owns memory

Durable engineering knowledge and workflow state belong to the **AE System**, not to one agent, model invocation, or conversational session.

Critical state shall not depend upon an agent remembering prior conversation.

The System shall support:

- durable system-owned state;
- bounded context;
- structured handoffs;
- traceable artifacts;
- resumable work;
- replacement or continuation by another agent where useful;
- reconstruction of relevant context from canonical system state.

AE may use fresh agents, continuing agents, or other context strategies as appropriate.

No single context strategy is an immutable Contract requirement.

The invariant is that **loss of one conversational session shall not imply loss of the engineering system's durable knowledge or workflow state**.

## 4. Portable canonical semantics

The canonical AE System shall separate **invariant AE semantics** from **organization-specific implementation**.

Core AE concepts shall not depend upon a specific:

- model or AI provider;
- orchestration technology;
- source-control platform;
- CI/CD platform;
- work-management platform;
- runtime;
- observability platform;
- cloud provider;
- architecture notation;
- organization;
- product or system.

The canonical System shall be specific about:

- required behavior;
- lifecycle semantics;
- artifact semantics;
- capability contracts;
- required interfaces and operations;
- authority;
- evidence;
- states;
- traceability;
- validation;

while remaining technology-neutral about how an organization implements them.

## 5. Organization Engineering Baseline

AE shall provide a method for establishing an **Organization Engineering Baseline** during adoption.

The Baseline shall be capable of representing more than technology mappings.

It shall describe relevant aspects of the environment in which AE will operate, including as applicable:

- canonical capability bindings to organization technology;
- available interfaces and integration methods;
- agent-accessible operations;
- identity and entitlement mechanisms;
- Operational Authority defaults and boundaries;
- policy-enforcement mechanisms;
- applicable standards and engineering practices;
- architecture expectations;
- evidence expectations;
- Verification and Validation expectations;
- organization risk posture;
- information classifications or handling categories where relevant;
- security constraints;
- compliance or regulatory constraints;
- infrastructure/runtime constraints;
- important organizational or product constraints;
- known engineering-health conditions.

A Product/System Profile may further specialize this baseline for a specific implementation target.

## 6. Canonical AE Capability Model

AE requires the following canonical capabilities:

- Source Control
- CI/CD
- Models
- Runtime / Execution
- Identity & Access
- Governed Tool Access
- Observability
- Knowledge / Memory
- Work Management
- Validation

The organization maps its technology into these capability contracts.

The capability model shall work **backwards from the AE lifecycle**.

For every canonical capability, the System shall define:

### Required lifecycle operations

What operations must the capability expose for AE to perform its lifecycle?

### Required agent-accessible operations

Which operations must be technically usable by an authorized agent without inserting a human as a mechanical intermediary?

### Minimum entitlement semantics

What scope must be expressible when granting an operation, such as:

- agent identity;
- action;
- resource;
- task;
- Contract;
- repository;
- environment;
- duration;
- condition.

### Denial impact

For each materially required operation, AE shall be able to determine whether absence or denial would:

- **Block AE** — the relevant lifecycle function cannot be performed;
- **Constrain AE** — AE can operate but loses a material capability or requires an alternate mode;
- **Degrade AE** — AE remains functional but with reduced efficiency, visibility, quality, or automation.

### Authority and policy interaction

Capability operations shall be subject to applicable:

- Operational Authority;
- identity;
- least privilege;
- Zero Trust principles;
- policy enforcement;
- resource boundaries.

### Implementation Proof

Each capability contract shall define how an implementation demonstrates that the capability is actually usable by AE.

The key design question is:

> **What denial, missing interface, or missing entitlement would make AE unable to perform its lifecycle without inserting a human as a mechanical intermediary?**

This requirement does **not** imply broad standing agent permissions.

An installed system must instead be capable of granting the required **scoped authority when the lifecycle requires it**, using least privilege and appropriate policy enforcement.

## 7. Agent-accessible Work Management is a canonical requirement

The canonical Work Management capability must support governed direct agent interaction sufficient for authorized agents to:

- create work items;
- read and query work items;
- update or modify work items;
- maintain status or state;
- maintain relationships and dependencies;
- attach evidence, references, comments, or relevant artifacts;
- close or complete work items when authorized.

The **capability** must support these agent operations.

This does not mean every agent receives every entitlement.

Zero Trust, Operational Authority, identity, resource scope, task scope, and policy determine:

- which agent;
- may perform which operation;
- against which resource;
- for which task;
- under which conditions.

Routine work-item administration is a major source of mechanical engineering work that agents can perform effectively.

An implementation that requires a human intermediary to perform routine work-item administration **does not fully satisfy the canonical AE Work Management capability**.

## 8. Capability-gap detection

AE shall identify when an adopting organization is missing or inadequately implements a capability required for effective AE operation.

A capability deficiency shall be made explicit rather than silently worked around.

The System shall identify:

- the affected capability;
- the missing operation, interface, entitlement, enforcement mechanism, or other deficiency;
- the lifecycle function affected;
- why the deficiency matters;
- whether it blocks, constrains, or degrades AE;
- potential remediation paths.

Reference guidance may identify common, mature, or widely used implementation choices without making those choices canonical requirements.

## 9. Engineering-health assessment

AE shall help identify **material engineering deficiencies that could cause agents to amplify existing system weaknesses**.

Engineering-health findings are distinct from missing AE capabilities.

Relevant areas may include:

- architecture understanding;
- architecture documentation and visualization;
- system boundaries and responsibilities;
- modularity;
- separation of concerns;
- coupling;
- change amplification;
- maintainability;
- code structure;
- automated testing;
- verification capability;
- CI/CD discipline;
- observability;
- identity and security boundaries;
- decision history;
- documentation and knowledge quality;
- standards applicability;
- technical debt.

The canonical Contract shall express the underlying engineering concerns rather than freezing named methods or practices as immutable requirements.

Named practices, frameworks, patterns, and techniques may be adopted through:

- standards profiles;
- Decision Records;
- ADRs;
- implementation guidance;
- reference material.

AE shall apply engineering judgment and context rather than treating engineering maturity as a universal binary checklist.

## 10. Agent-assisted engineering improvement

An organization does not need mature engineering practices before adopting AE.

Where deficiencies are identified, AE shall support converting appropriate findings into governed engineering work that agents can materially help perform.

Examples can include:

- reconstructing system understanding;
- developing architecture views;
- documenting boundaries and responsibilities;
- recovering decision history;
- improving automated verification;
- improving observability;
- reducing problematic coupling;
- improving modularity and maintainability;
- restructuring code;
- resolving other relevant engineering deficiencies.

Remediation work shall use the same AE lifecycle, authority, evidence, traceability, and independent Validation model as other engineering work.

The objective is not simply to generate an assessment.

**AE should help the organization improve the engineering baseline it discovers.**

## 11. Architecture and traceability

AE shall require a durable architecture representation that is usable by both humans and agents.

The architecture model shall support appropriate:

- system context;
- boundaries;
- responsibilities;
- relationships;
- dependencies;
- architectural decisions;
- traceability into Contracts, Plans, implementation work, evidence, and Validation.

The Contract does not mandate one immutable architecture notation or framework.

Specific architecture approaches may be adopted through Decision Records and standards profiles.

Architecture shall function as part of active engineering work rather than existing only as passive documentation.

## 12. Durable engineering knowledge and identifiers

The System shall maintain traceable engineering knowledge including appropriate:

- architecture artifacts;
- Contracts;
- Plans;
- work items;
- evidence;
- Validation results;
- decisions and ADRs;
- applicable standards;
- capability bindings;
- authority and policy configuration;
- organization baseline data;
- learning and experiment results.

Stable identifiers, versioning, provenance, relationships, and machine-readable structures shall be used where they materially improve human or agent understanding and system operation.

## 13. Standards and applicability

Engineering standards and practices shall be treated as **context-aware constraints, guidance, and evidence sources**, not universal checklists.

The System shall support determining:

- which standards or engineering principles apply;
- why they apply;
- where they apply;
- what evidence demonstrates appropriate application;
- when a practice is unnecessary or disproportionate.

AE shall favor the **simplest useful engineering pattern** rather than equating greater process weight with greater maturity.

## 14. Planning and Execution

Planning shall be architecture-aware and shall establish a credible route from the approved Contract to its Proof.

Plans shall identify appropriate:

- work decomposition;
- dependencies;
- architecture impact;
- capability needs;
- authority needs;
- evidence expectations;
- Validation strategy;
- risks;
- constraints.

Execution shall give capable agents sufficient freedom to reason, adapt, use approved tools, and produce evidence while remaining bounded by:

- the approved Contract;
- applicable architecture;
- Operational Authority;
- applicable standards and policy;
- the Plan and its allowed adaptation boundaries.

Agents shall be encouraged to surface newly discovered risks, architecture concerns, evidence gaps, and potential Contract-change proposals rather than hiding them to preserve apparent Plan success.

## 15. Validation and evidence

Proof shall be established before Execution as part of the Contract.

Execution shall produce evidence against that Proof.

Independent Validation shall determine whether the intended outcome was actually achieved.

Validation shall be capable of rejecting apparently successful Execution when:

- evidence is insufficient;
- the implementation does not satisfy the Contract;
- important unintended effects exist;
- the intended outcome was not achieved.

The System shall distinguish:

- Verification performed during engineering;
- evidence generated by work;
- independent Validation of the outcome.

## 16. Observability, metrics, experiments, and learning

AE shall make its own operation observable enough to determine whether the System improves engineering outcomes.

The System shall support measures such as:

- total time to outcome;
- phase time;
- loop count;
- failed Validation loops;
- human effort;
- agent/model cost;
- quality assessment;
- other organization-selected measures.

Experiments shall preserve:

- the question or hypothesis;
- relevant setup;
- evidence;
- result;
- conclusion;
- resulting system decision where one exists.

Concluded experiments and meaningful learning shall become durable system knowledge.

## 17. Decision history and System Rationale

The canonical AE System shall maintain an understandable **About / System Rationale** view that explains:

- what AE is;
- why it exists;
- the major ideas behind the design;
- significant current decisions;
- how the System has evolved;
- important experiments and what was learned.

The Decision Register and ADRs remain authoritative detailed decision history.

The System Rationale shall help humans understand that history and shall be maintained as the System evolves.

The Field Guide may teach and visualize this information, but the **Field Guide is a learning website and is not the canonical source of truth for AE**.

## 18. Concrete Part 1 Adoption Deliverable

Part 1 shall produce a **versioned Canonical AE System distribution** suitable for handoff to an implementation team.

The release shall contain three related semantic layers.

Specific filenames, directory structures, serialization formats, and implementation technologies shall be established later through architecture and design decisions rather than frozen by this Contract.

### A. Canonical Core

The authoritative, technology-neutral AE method and system definition.

It shall contain the canonical semantics for:

- lifecycle;
- domain/artifact model;
- Contract;
- Planning;
- Execution;
- Validation and evidence;
- architecture;
- authority and governance;
- capability contracts;
- standards/applicability;
- context and memory;
- identifiers, versioning, provenance, and traceability;
- decisions and ADRs;
- metrics, experiments, and learning.

### B. Adoption Starter Pack

A reusable implementation package that a human or agentic implementation team can instantiate for an organization.

Its semantics shall support:

- an implementation START HERE experience;
- implementation-agent guidance;
- Organization Engineering Baseline;
- Product/System Profile;
- capability bindings;
- required agent-access and entitlement assessment;
- authority and policy profile;
- standards/practices profile;
- architecture expectations;
- evidence/Validation profile;
- engineering-health assessment;
- capability-gap report;
- engineering-health gap report;
- implementation-Plan structure;
- installation acceptance and Proof.

The Adoption Starter Pack shall help transform the canonical AE System into an organization-specific implementation without redefining canonical AE semantics.

### C. Executable / Reference Layer

Part 1 shall contain enough executable and reference behavior to demonstrate that AE is a working system rather than a collection of ideas.

This layer shall include appropriate:

- machine-readable schemas or equivalent structured definitions;
- validators;
- automated integrity checks;
- reference artifacts;
- synthetic imperfect organization baseline;
- complete reference AE loop;
- at least one controlled backward/failure route;
- capability-gap detection;
- engineering-health detection;
- governed agent-assisted remediation;
- capability usability/entitlement Proof;
- adoption-readiness test.

The executable/reference layer is not required to be a production universal orchestration platform.

Its purpose is to **prove the canonical System can be instantiated, operated, checked, and validated**.

## 19. Intended Adoption Experience

The canonical distribution shall support an implementation flow approximately equivalent to:

**Canonical AE release**  
→ instantiate Adoption Starter Pack  
→ establish Organization Engineering Baseline  
→ establish Product/System Profile where applicable  
→ map organization technology into capability contracts  
→ verify required agent-accessible operations and scoped entitlements  
→ identify capability gaps  
→ identify engineering-health gaps  
→ configure standards, policies, authority, and architecture expectations  
→ derive organization-specific implementation Plan  
→ implement required capability/provider bindings  
→ execute a reference AE loop  
→ independently validate the installation

The exact user experience and implementation mechanics may evolve.

The semantic outcome shall remain stable.

---

# Non-Goals

Part 1 does **not**:

- implement Kestrel;
- use Kestrel as an input to the generic canonical design;
- optimize the canonical System around one organization's stack;
- mandate a particular model or provider;
- mandate a particular orchestration framework;
- mandate a particular source-control platform;
- mandate a particular CI/CD platform;
- mandate one immutable architecture notation;
- make one agent-context strategy immutable;
- require broad standing agent permissions;
- make every named engineering principle or framework a Contract-level requirement;
- create a universal compliance checklist;
- build the future AE Portal;
- reproduce the Field Guide as the canonical System;
- replace consequential Human Decision Authority;
- claim certification or standards conformance that has not been demonstrated;
- require a production-grade universal orchestration runtime as a condition of completing Part 1.

---

# Proof

Contract v1.0 is satisfied when evidence demonstrates all of the following.

## A. Versioned canonical distribution

Part 1 produces an identifiable, versioned Canonical AE System release containing the:

- Canonical Core;
- Adoption Starter Pack;
- Executable / Reference Layer.

An implementation team can obtain the published release and identify its version, authoritative content, and applicable validation mechanisms.

## B. Canonical completeness and coherence

The canonical release materially defines the lifecycle, domain/artifact model, architecture semantics, capability contracts, authority model, Planning, Execution, Validation, evidence, memory/state model, standards/applicability, Organization Engineering Baseline, observability, learning, and governance required by this Contract.

Material concepts are internally coherent and traceable.

## C. Machine-verifiable integrity

Canonical artifacts that can reasonably be validated mechanically have schemas, validation rules, tests, or equivalent automated checks.

Automated execution demonstrates that these checks function.

## D. Happy-path reference AE loop

At least one complete reference engineering loop demonstrates:

**Loop Context → Contract → Architecture-aware Planning → Plan Review → Bounded Execution → evidence → Independent Validation → learning**

including appropriate:

- authority;
- capability use;
- system-owned state;
- traceability;
- evidence;
- Validation.

## E. Non-happy-path reference AE loop

At least one reference loop shall demonstrate a controlled backward route resulting from new evidence or failed Validation.

The example shall exercise at least one of:

- Validation → Retry Execution;
- Validation → Replan;
- Execution or Validation → Contract-change proposal;
- another explicitly governed backward route.

The example shall show that failure or discovery does not require abandoning lifecycle control or silently rewriting prior intent.

## F. Synthetic imperfect organization baseline

Part 1 shall include a deliberately generic synthetic organization used as an adoption fixture.

Kestrel shall not be an input.

The synthetic organization shall contain:

- plausible technology bindings;
- policy and authority context;
- standards/practice context;
- architecture expectations;
- evidence/Validation expectations;
- relevant constraints;
- intentional capability and engineering imperfections.

It shall not assume an unrealistically mature organization.

## G. Capability-operation and entitlement assessment

For the synthetic organization, the System shall evaluate required capability operations and determine whether appropriate agent-accessible interfaces and scoped entitlement mechanisms exist.

The assessment shall demonstrate classification of relevant deficiencies as:

- Block;
- Constrain;
- Degrade.

At least one example shall demonstrate that a technically available capability is still insufficient because required agent access, entitlement semantics, or enforceable authority is missing.

## H. Work Management Proof

The synthetic implementation shall demonstrate that an authorized agent can directly perform the required canonical Work Management operations without a human acting as routine administrative intermediary.

The demonstration shall also show that operations outside the agent's granted authority can be denied.

## I. Technology portability

Materially different example technology choices shall be capable of satisfying the same canonical capability contracts without changing core AE semantics.

Changing provider bindings shall not require redefining:

- lifecycle semantics;
- Contract semantics;
- Planning semantics;
- evidence semantics;
- authority semantics;
- Validation semantics;
- core artifact semantics.

## J. Capability-gap detection

The synthetic organization shall contain at least one meaningful missing or inadequate canonical capability.

AE shall identify:

- the deficiency;
- the affected lifecycle function;
- why it matters;
- whether it blocks, constrains, or degrades AE;
- an appropriate remediation path.

## K. Engineering-health detection

The synthetic baseline shall contain representative engineering deficiencies.

AE shall identify material concerns using contextual engineering reasoning in areas such as:

- architecture understanding;
- maintainability;
- modularity;
- coupling;
- change amplification;
- verification;
- observability;
- knowledge quality;
- another materially relevant engineering-health concern.

Named practices may inform the assessment but shall not substitute for explaining the underlying engineering condition.

## L. Governed agent-assisted remediation

At least one identified engineering deficiency shall be converted into governed AE work.

Agents shall materially assist in remediation.

The resulting work shall produce evidence, preserve traceability, and undergo independent Validation.

The Proof shall demonstrate that AE can improve an imperfect engineering baseline rather than merely report deficiencies.

## M. Reproducible fresh-session adoption test

A fresh implementation/planning session shall receive **only**:

1. the published versioned Canonical AE System distribution; and
2. the supplied Organization Engineering Baseline and Product/System Profile or equivalent supplied baseline.

The session shall not rely on:

- hidden prior conversation;
- unpublished design knowledge;
- previous implementation-session memory;
- Kestrel material;
- unstated core semantics.

From those inputs, the fresh session shall derive an organization-specific AE implementation Plan.

### Adoption Test Evaluation Rubric

The result passes only if all of the following are satisfied:

**1. Canonical semantic fidelity**  
The session uses the published lifecycle, artifacts, capability model, authority model, and Validation semantics without materially redefining them.

**2. Baseline comprehension**  
The Plan correctly incorporates the supplied organization/product technology, policies, standards, constraints, architecture expectations, and relevant risk context.

**3. Capability binding completeness**  
Required canonical capabilities are mapped to organization implementations or explicitly identified as gaps.

**4. Agent-access and entitlement correctness**  
Required agent-accessible operations, entitlement needs, Operational Authority, and policy-enforcement requirements are identified.

**5. Gap reasoning**  
Capability deficiencies are distinguished from engineering-health deficiencies and are appropriately classified/prioritized.

**6. Implementation credibility**  
The resulting Plan describes a credible route to an operable organization-specific AE implementation rather than a generic restatement of the Canonical Core.

**7. Evidence and Validation design**  
The Plan identifies how the installation and important capability bindings will be proven usable and independently validated.

**8. Traceability**  
Material implementation decisions and work can be traced back to the canonical requirement, organization baseline, identified gap, or applicable decision.

Failure of any rubric dimension requires correction, Replan, or explicit disposition before adoption-readiness Proof passes.

## N. Independent system review

The completed Part 1 System shall receive independent review from relevant perspectives including:

- adopting organization;
- architecture;
- Planning;
- Execution;
- Validation;
- governance/security;
- portability;
- implementation-team usability;
- future product/client use.

Material findings shall be resolved, explicitly accepted by appropriate authority, or converted into governed future work.

## O. Human Owner acceptance

Mechanical checks and agent reviews support acceptance but do not replace it.

**Final Part 1 acceptance is a Human Owner decision against the assembled Proof.**

---

# Portability Principle

**Canonical AE System → Organization Engineering Baseline → Organization-specific AE implementation**

The canonical AE System defines the authoritative, technology-neutral semantics.

The Organization Engineering Baseline describes the environment into which those semantics will be implemented.

The organization-specific AE implementation binds those canonical semantics to real technologies, policies, authority mechanisms, standards, and engineering conditions.

---

## Contract Change Control

This approved Contract is the authoritative Part 1 baseline.

- Agents may not silently change Goal, Spec, or Proof.
- Material Contract changes require a versioned Contract-change proposal and Human Owner approval.
- Implementation convenience, architecture decisions, standards choices, tools, and experiments may not quietly redefine Contract meaning.
- Lower-level design decisions must remain subordinate to Contract invariants.

Design test:

> **If evidence later shows a better way to do this, would changing it alter what Agentic Engineering fundamentally means?**

If yes, the matter may belong at the Contract/system-semantic level. If no, prefer the appropriate lower layer such as a Decision Record, ADR, standards/profile configuration, architecture, Plan, capability binding, reference pattern, experiment, or implementation choice.
