# L1-B — Architecture Representation Strategy

**Status:** Approved L1-B baseline  
**Architecture authority:** DR-021 remains the adopted architecture discipline below Contract level. This L1-B strategy clarifies correct use; it does not supersede DR-021.

## 1. Decision intent

Canonical AE must describe its logical responsibilities precisely without pretending that those responsibilities are separately runnable software applications or data stores.

C4 remains useful and adopted, but C4 view types shall be used according to what they actually represent.

## 2. Canonical Core architecture views

The Canonical Core uses:

1. the existing **C4 System Context** for the logical Organization-specific AE Implementation established in L1-A;
2. a **normative logical responsibility architecture** for R1–R7 and their relationships;
3. later domain/state/sequence/decision views as needed by subsequent L1 design.

The R1–R7 responsibility boxes are **not C4 Containers**.

They do not imply:

- separate applications;
- independently deployable services;
- microservices;
- databases;
- dedicated agent runtimes;
- a network boundary;
- one-to-one component ownership.

The semantic architecture is normative; the current Markdown/Mermaid rendering is a repository visualization convenience unless a later decision changes that representation mechanism.

## 3. Why no normative Canonical Core C4 Container view exists yet

A C4 Container view is intended to show actual applications, services, data stores, or other separately runnable/deployable elements inside a software system.

The technology-neutral Canonical Core deliberately does not know whether an organization will realize R1–R7 through:

- one agent platform;
- multiple agent runtimes;
- Work Management workflows;
- source-control artifacts;
- a policy engine;
- a capability broker;
- direct APIs;
- multiple enterprise products;
- or another distributed topology.

Labeling the seven responsibilities as canonical Containers would silently introduce a topology that Contract v1.0 and DR-019 intentionally leave variable.

## 4. Executable / Reference Layer

When the Part 1 reference implementation has concrete software/runtime structure, the Executable / Reference Layer shall create a **genuine C4 Container view** for that reference topology.

That view can show actual elements such as applications, runtimes, stores, adapters, provider integrations, or other concrete implementation components.

The reference Container view is **conforming reference architecture**, not the normative definition of the seven responsibilities.

A future implementation may combine or split reference Containers while remaining conforming if it preserves canonical semantics and Proof.

## 5. Organization-specific AE Implementation

Adoption guidance shall require or strongly support a concrete implementation topology view once the organization's actual mechanisms are known.

Under the adopted C4 discipline, the expected default is a **C4 Container view** where the implementation contains software applications/services/data stores that fit C4 Container semantics.

An adopter's concrete view should make visible as applicable:

- which real component(s) realize each canonical logical responsibility;
- which components combine multiple responsibilities;
- where one responsibility is distributed;
- actual data stores/systems of record;
- agent runtimes/hosts;
- provider products and interfaces;
- PEP/enforcement locations;
- Human interaction mechanisms;
- External Capability Provider relationships;
- Target Product/System relationships.

If a material part of the implementation does not map cleanly to C4 software Containers, complementary views may be used rather than mislabeling organizational/process mechanisms as software.

## 6. Traceability between logical and concrete architecture

A concrete reference or organization implementation shall eventually be able to show a mapping approximately equivalent to:

`R1–R7 logical responsibility → concrete implementation component(s)/mechanism(s) → capability/provider bindings → authoritative state/source → implementation Proof`

This traceability is more important than preserving a one-box-to-one-container visual correspondence.

## 7. Relationship to DR-021

This strategy **clarifies**, rather than rejects, the adopted C4 decision.

- C4 System Context remains appropriate for the logical operational AE system boundary.
- C4 Containers become appropriate when actual runnable/deployable topology exists.
- Canonical logical responsibilities are represented as logical architecture because they intentionally do not prescribe that topology.

A future evidence-backed decision could change the adopted representation approach without reopening Contract v1.0 unless the change alters canonical AE meaning.