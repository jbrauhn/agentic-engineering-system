# L1-A — System Identity & Boundary Baseline

**Status:** Approved L1-A baseline  
**Authority:** Agentic Engineering System Contract v1.0 + Human Owner L1-A decisions  
**Scope:** System identity, vocabulary, system boundaries, distribution/implementation distinction, conformance boundary, and adopter-facing relationship model.

## 1. Formal system identity

**Agentic Engineering (AE)** is a **portable, governed socio-technical engineering system for Human–AI engineering**.

The public shorthand is **Agentic Engineering System**.

AE is a system rather than only a method or operating model because it includes not only practices and artifacts, but also executable capability requirements, agent-operable interfaces, governed authority and enforcement, durable system-owned state, evidence, independent Validation, humans, and AI agents.

A documentation-only adoption is therefore insufficient to constitute a conforming AE implementation.

## 2. Purpose

AE provides a technology-neutral system for humans and AI agents to perform governed engineering work through canonical lifecycle semantics, durable artifacts/state, architecture-aware Planning, bounded Execution, evidence, independent Validation, and learning.

Part 1 publishes a versioned distribution that an implementation team can instantiate in an organization without redefining core AE semantics.

## 3. Stable L1-A vocabulary

### Canonical AE System

The **Canonical AE System** is the invariant conceptual and normative meaning of Agentic Engineering defined by the normative Canonical Core.

It answers: **What does Agentic Engineering fundamentally mean?**

### Canonical Core

The **Canonical Core** is the normative part of the published distribution. It defines the invariant AE semantics that conforming layers and organization-specific implementations must preserve.

### Canonical AE System Distribution

The **Canonical AE System Distribution** is the versioned Part 1 product that is published for adopters.

It contains:

1. **Canonical Core — normative**
2. **Adoption Starter Pack — conforming to the Canonical Core**
3. **Executable / Reference Layer — conforming to the Canonical Core**

The Starter Pack helps instantiate the Core. The Executable / Reference Layer demonstrates that the Core can actually operate. Neither may quietly redefine canonical semantics.

### Organization-specific AE Implementation

An **Organization-specific AE Implementation** is the operational realization of the Canonical AE System within an organization.

It binds canonical semantics to organization-specific inputs such as:

- Organization Engineering Baseline;
- Product/System Profile where applicable;
- policies and standards;
- identity and authority configuration;
- capability/provider bindings;
- actual models, tools, platforms, and runtime choices;
- durable implementation state.

**AE System Instance** is not the preferred formal term because it can imply one centrally deployed software application. AE does not require that topology.

### Candidate AE Implementation

A **Candidate AE Implementation** is an organization-specific implementation being built, configured, or assessed that has not yet demonstrated applicable installation/adoption Proof for its declared scope.

### Conforming AE Implementation

A **Conforming AE Implementation** is an evidence-backed system state meaning:

> For its declared implementation scope, the organization-specific AE implementation has demonstrated the mandatory canonical semantics and applicable Capability Contract and installation requirements defined by the Canonical AE System.

Conforming does **not** mean externally certified, accredited, universally mature, or endorsed by a central certification authority. An organization may self-validate or use whatever independent review its governance requires.

Detailed conformance states and scoring are intentionally deferred to later capability, adoption, and Validation design.

### AE Loop

An **AE Loop** is one bounded execution of the canonical AE lifecycle inside an organization-specific AE implementation.

An AE Loop is not the AE System itself.

**AE Loop** is the preferred canonical term because **AE Engineering Loop** is redundant while **Loop** alone is too ambiguous outside local context.

### External Capability Provider

An **External Capability Provider** is a separate product or service that satisfies one or more canonical AE Capability Contracts and is bound into an organization-specific AE implementation.

Canonical specializations are:

- Source Control;
- CI/CD;
- Models;
- Runtime / Execution;
- Identity & Access;
- Governed Tool Access;
- Observability;
- Knowledge / Memory;
- Work Management;
- Validation.

A provider being physically outside the AE system boundary does not make it operationally unimportant.

> **Physical system boundary and AE operational participation are not the same thing.**

### Target Product/System

The **Target Product/System** is the external engineered subject.

AE governs engineering **of** the Target Product/System. The Product/System itself does not become an AE component merely because AE engineers it.

AE may own or maintain durable governed engineering representation/state about it, including:

- Product/System Profile;
- architecture references/models;
- work state;
- Contracts;
- Plans;
- evidence;
- Validation state;
- decisions;
- applicable standards;
- context/knowledge.

Agents may modify the Target Product/System only through governed Capability Contracts and Operational Authority.

### Future AE Portal

The future **AE Portal** is an optional client / Human–AI interaction product over AE.

It may provide conversation, lifecycle/artifact visualization, shared visual reasoning, architecture interaction, sketch/photo/tablet-to-diagram workflows, and decision/evidence interaction.

It is not part of the canonical Part 1 runtime requirement and does not define AE.

Architectural test:

> **If the Portal disappeared tomorrow, the Canonical AE System and a conforming organization-specific AE implementation must still function.**

## 4. Normative and conforming boundaries

| Concept | Relationship to canonical AE | May vary by organization? |
|---|---|---|
| Canonical Core | **Normative** | No, except through approved canonical change control |
| Adoption Starter Pack | Conforming support layer | Its implementation/presentation may evolve while preserving Core semantics |
| Executable / Reference Layer | Conforming proof/reference layer | Its technologies and reference patterns may evolve while preserving Core semantics |
| Organization-specific AE Implementation | Conforming operational realization | Yes: profiles, bindings, tools, policies, standards, runtime topology, etc. |
| External Capability Provider | Bound provider satisfying Capability Contract | Yes |
| Target Product/System | External engineered subject | Yes |
| Future AE Portal | Optional client/product | Yes; not required |
| Field Guide | External learning/explanation surface | Yes; not canonical source of truth |

## 5. Logical system boundary

AE defines a **logical system/runtime boundary**, not one mandatory centralized physical control-plane application.

A conforming implementation may distribute AE behavior across organization technology such as agent hosts, source control, work management, CI/CD, identity/policy systems, knowledge stores, observability, validators, model providers, and other capability bindings.

The implementation remains recognizably AE only if the distributed realization preserves the canonical lifecycle, artifact/state semantics, authority/enforcement behavior, Capability Contracts, durable-state requirements, evidence/Validation model, and applicable installation Proof.

> **Logical/distributed does not mean documentation-only.**

Part 1 must include executable/reference behavior sufficient to prove that canonical AE can be instantiated, operated, governed, checked, and validated.

## 6. Inside / outside relationship model

### Inside the Canonical AE System Distribution

- normative Canonical Core;
- conforming Adoption Starter Pack;
- conforming Executable / Reference Layer;
- canonical system rationale and consequential system decisions;
- reference behavior and validation material required by Contract v1.0.

### Inside an Organization-specific AE Implementation

Depending on the adopted architecture and bindings, the logical implementation includes:

- canonical lifecycle behavior;
- instantiated canonical artifacts/state;
- Organization Engineering Baseline and applicable profiles;
- authority/policy configuration and enforcement relationships;
- capability bindings;
- durable engineering representation/state;
- evidence and Validation state;
- organization-specific configuration needed to operate AE.

The logical implementation may span multiple physical products/services.

### External but operationally participating

- External Capability Providers;
- Target Product/System;
- organization policy/governance authorities and systems where separately bounded;
- model/provider services where separately bounded;
- optional Portal/client.

### External and explanatory/reference only

- Field Guide learning website;
- external standards bodies and source standards documents;
- other reference material not instantiated as AE state.

## 7. Conformance boundary

A team has not demonstrated a conforming AE implementation merely because it:

- copied AE templates;
- read the Field Guide;
- uses AI agents;
- uses Contract terminology;
- stores architecture documents;
- manually imitates selected lifecycle steps.

Conformance requires evidence, for the declared scope, that mandatory canonical semantics and applicable installation/Capability Contract requirements actually operate.

The detailed Proof belongs to downstream Capability Model, Adoption, Validation, and installation design.

Three diagnostic dimensions are preserved for that later work and must not be collapsed:

1. **Capability availability** — does the canonical capability exist?
2. **Capability operability / entitlement** — is it sufficiently agent-operable under governed scoped authority?
3. **Engineering health** — is the engineering environment healthy enough that agents are not merely amplifying material weaknesses?

Capability gaps and engineering-health findings have different meanings and consequences.

## 8. Adopter test

A fresh implementation team should be able to answer the following from this baseline:

- **What is Agentic Engineering?** A portable, governed socio-technical engineering system for Human–AI engineering.
- **What is the Canonical AE System?** The invariant conceptual/normative AE meaning defined by the Canonical Core.
- **What did I receive?** A versioned Canonical AE System Distribution containing the normative Core plus conforming Starter and Reference layers.
- **What does my organization instantiate?** An Organization-specific AE Implementation.
- **What must remain invariant?** Mandatory canonical semantics and applicable canonical contracts/rules.
- **What may vary?** Organization profiles, technology/provider bindings, policies, standards configurations, runtime topology, and other implementation choices not frozen by higher authority.
- **What are External Capability Providers?** Separate products/services bound to AE through canonical Capability Contracts.
- **Is my Target Product/System part of AE?** No. It is the external engineered subject; its governed engineering representation/state may be held by AE.
- **Where does the Portal fit?** Optional client/interaction product; not required and not canonical AE itself.
- **When is the result conforming?** When applicable mandatory canonical semantics and installation/Capability Contract requirements have been demonstrated with evidence for a declared scope.
- **Why no giant central runtime?** Portability requires canonical behavior and interfaces, not one physical topology.
- **Why is documentation alone insufficient?** AE includes executable capabilities, agent-operable interfaces, enforcement, durable state, evidence, and Validation behavior.

## 9. Implementation-team use

An implementation team uses this artifact to classify each discovered or proposed element as:

- canonical invariant;
- conforming distribution support;
- organization-specific implementation state/configuration;
- external capability binding;
- external engineered subject;
- optional client/reference surface.

That classification is an input to L1-B architecture, the domain model, Capability Contracts, and the Adoption Starter Pack.
