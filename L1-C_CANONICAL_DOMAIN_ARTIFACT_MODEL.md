# L1-C — Canonical Domain / Artifact Model

**Status:** Approved L1-C semantic baseline  
**Authority:** Contract v1.0; DR-017; DR-019; DR-106; DR-107; Human Owner L1-C decision  
**Scope:** Canonical domain semantics only. This document does not define file formats, schemas, database models, provider technologies, or repository layout.

## 1. Core distinction

> **Canonical domain entity ≠ serialized artifact or implementation object.**

A canonical entity or record has semantic meaning independent of whether an implementation represents it in Markdown, YAML, JSON, a database, a provider object, generated UI, or another conforming form.

Likewise:

> **Artifact representation ≠ authoritative source automatically.**

Authority is established through the federated authoritative-state model in DR-107.

## 2. Entity-admission rule

Independent canonical identity is added only when it materially protects system meaning across time and cannot be achieved cleanly with a value, subordinate record, typed relationship, external reference, derived view, or ephemeral operating state.

A strong candidate commonly needs several of the following:

- stable identity across time;
- its own governed lifecycle/change semantics;
- independent revision/supersession;
- direct authority/approval targeting;
- traceability from other canonical objects;
- authoritative-source declaration;
- independently meaningful provenance;
- survival across agent/session loss;
- reuse/reference across AE Loops;
- state meaning independent of a particular representation/provider object.

Hard test:

> **Would confusing two instances or revisions cause a material governance, authority, traceability, continuation, or Validation error?**

The burden of proof is on **adding identity**.

## 3. Canonical semantic categories

### A1 — First-class durable entity

A stateful/versioned canonical concept with stable logical identity and durable semantic meaning.

### A2 — First-class durable record

An independently referenceable durable assertion, judgment, evidence, handoff, rationale, or conclusion. A2 records are normally immutable after issuance.

### B — Canonical value / subordinate object

Has canonical semantics but normally exists within the identity/lifecycle of another entity rather than needing independent global identity.

### C — External Resource Reference

Canonical AE reference to an externally authoritative/provider-owned resource. AE owns the reference/relationship semantics; the provider may remain authoritative for selected properties.

### D — Derived view / projection / context product

Useful to humans/agents but reconstructable from authoritative/provenance-bearing state and not inherently authoritative truth.

### E — Ephemeral operating state

Temporary actor/session state that has no inherent durability requirement unless material information is promoted to the durable entity/record that semantically owns it.

### F — Normative definition / release object

Versioned definitions published as part of the Canonical AE Distribution rather than operational state of one Organization-specific AE Implementation or AE Loop.

## 4. A1 — First-class durable entities

### Organization Engineering Baseline

**Why independent identity is necessary:** the organization's engineering environment evolves independently, applies across products/Loops, and implementation/adoption claims must reference an exact baseline revision.

The OEB may reference organization policies, authority defaults, standards/practices, constraints, architecture expectations, evidence/Validation expectations, capability environment, risk/classification context, and known engineering-health conditions.

### Product/System Profile

**Why independent identity is necessary:** durable governed representation of the external Target Product/System is reused across many Loops and can evolve independently from any one Loop or Plan.

### AE Implementation Profile

**Why independent identity is necessary:** an Organization-specific AE Implementation needs a durable canonical representation of its declared scope, Canonical AE Release reference, OEB/Product Profile revisions, bindings/configuration references, and conformance claim context.

The **AE Implementation Profile is not the running socio-technical implementation itself**.

A displayed/stored conformance state in the Profile is a projection/claim backed by applicable installation/adoption Validation records; it is not independently authoritative truth.

### Capability Binding

**Why independent identity is necessary:** mappings from canonical Capability Contracts/operations to organization provider mechanisms can change independently, have scope/authority implications, and must be referenced by governed operations and implementation Proof.

### Product/System Baseline — L1

**Why independent identity is necessary:** DR-025 establishes L1 as durable Product/System state that persists across normal Loops and that Plans must plan against precisely.

The **Product/System Baseline is the canonical domain entity**.

A **Baseline Manifest** is a representation/snapshot of an exact baselined revision. It may identify authoritative revisions such as:

- Product/System Profile;
- Architecture Model;
- relevant DR/ADR records;
- applicable standards state;
- relevant engineering-health state;
- other durable baseline material.

The Baseline does **not own** those referenced entities. Each approved/baselined Baseline revision is immutable.

### AE Loop

**Why independent identity is necessary:** one bounded lifecycle execution needs durable correlation of state, transitions, exact Contract/Plan references, work, actors, evidence, Validation, routing, and outcomes.

> **AE Loop is coordination/correlation, not aggregate ownership.**

Persistent architecture, baselines, decisions, learning, and organization state may span many Loops and are referenced rather than absorbed into a Loop aggregate.

### Contract

**Why independent identity is necessary:** Contract is the governed statement of Goal + Spec + Proof; exact approved revisions are targets of authority, Planning, evidence, and Validation.

Approved Contract revisions are immutable.

### Contract Change Proposal

**Why independent identity is necessary:** a proposed Contract change has its own trigger/evidence, rationale, exact proposed change, downstream impact, Human Decision Authority disposition, and provenance. It cannot be represented safely as an in-place edit to the approved Contract.

### Plan

**Why independent identity is necessary:** a Plan has its own revision/review lifecycle and must reference exact Contract and Product/System Baseline revisions. One Plan revision may have multiple conforming representations.

The Plan owns the Verification/test strategy derived from Contract Proof; Proof remains part of the Contract.

### Execution Increment — L2

**Why independent identity is necessary:** a bounded delivery increment has durable scope, dependencies, decomposition, progress/evidence relationships, and lifecycle meaning independent of individual Tasks or provider work items.

### Executable Task — L3

**Why independent identity is necessary:** canonical task semantics must survive changes in Work Management provider and allow Contract/Plan, dependencies, authority, and evidence to reference work independent of Jira/Plane/etc.

Anti-duplication rule:

> **AE shall not create a shadow Work Management database merely to preserve canonical Task identity.**

The canonical Task contains only AE-required portable semantics. Provider-owned operational properties remain authoritative in Work Management according to declared property-level authority.

### Architecture Model

**Why independent identity is necessary:** architecture is first-class governed engineering state used across Loops by Planning, decisions, evidence, and Validation. It must be distinguishable from any one diagram or file representation.

Architecture Model Stewardship remains under R2.

### Experiment

**Why independent identity is necessary:** a formal experiment has a durable lifecycle—question/hypothesis, setup/context, measurement approach, execution, result, and conclusion—and may span multiple observations before conclusion.

## 5. A2 — First-class durable records

### Decision Record / ADR

**Why independent identity is necessary:** consequential rationale and what was decided may span many Loops, be referenced independently, and later be superseded/challenged. ADR is an architecture-specific semantic subtype of Decision Record.

### Authority Decision

**Why independent identity is necessary:** approval/rejection by an eligible authority of a precise proposal/action/transition/revision must remain independently provable and reconstructable.

### Plan Review Record

**Why independent identity is necessary:** independent review of an exact Plan revision is a durable governance fact; materially changed Plans require new/re-review evidence rather than rewriting the prior review.

### Evidence Record

**Why independent identity is necessary:** material evidence may physically remain in CI/CD, source control, observability, test/artifact systems, yet be reused across Proof criteria/Validation attempts and require stable provenance/reference.

> **Evidence Record ≠ evidence bytes.**

An issued Evidence Record preserves what evidence existed and its context/provenance at issuance. Later discovery that evidence is stale, invalid, superseded, incomplete, or inappropriate does not rewrite that historical record; later assessment/correction/Validation semantics record the changed understanding.

### Validation Record

**Why independent identity is necessary:** independent outcome judgment must identify exactly what Contract revision/Proof was judged, which evidence was used, who/what performed Validation, independence provenance, rationale, outcome, and lifecycle route.

**Installation/Adoption Validation is a use/subtype of this same A2 Validation Record semantics, not an additional first-class record type.** Its target and Proof context concern the Organization-specific AE Implementation and applicable adoption requirements rather than a normal engineering-work Contract outcome.

### Handoff Record

**Why independent identity is necessary:** structured continuation across actors/sessions must durably preserve the continuation boundary and references to authoritative state. It is not equivalent to compaction or a Context Package.

### Learning Record

**Why independent identity is necessary:** material evidence-backed conclusions may originate from experiments, Loops, Validation failures, incidents, side quests, or other discoveries and may influence future Planning/decisions across Loops.

## 6. B — Canonical values and subordinate objects

The following have canonical meaning but do not currently justify global first-class identity:

### Contract-scoped

- Goal;
- Spec;
- Spec Statement/Requirement;
- Non-goal;
- Proof;
- Proof Criterion.

Proof Criteria shall be stably addressable **within the exact Contract revision** so Evidence/Validation can target them precisely.

### AE Loop-scoped

- Loop Context;
- lifecycle/work classification;
- current Loop state;
- gate state;
- Loop Transition Event/Record.

Transition history must be append-only/reconstructable, but individual transitions need not be global A1/A2 entities.

### Plan-scoped

- Planning Depth;
- Planning Method;
- Verification/Test Strategy;
- risk/constraint statements;
- allowed adaptation boundaries;
- capability/authority/context needs;
- dependency descriptions.

### Architecture-scoped

- Architecture Element — addressable subordinate object with stable identity scoped to the logical Architecture Model/Target Product/System;
- Architecture Relationship — typed/addressable subordinate relationship;
- Architecture Representation metadata.

### Other subordinate concepts

- Plan Review findings;
- Evidence Set / evidence selection for a Validation attempt;
- Experiment measurements/results details;
- Capability Binding operation mappings;
- actor/role references;
- standards applicability state pending L1-E refinement;
- authority/policy configuration references;
- conformance projection/status on the Implementation Profile.

## 7. C — Provider-owned objects represented by External Resource References

Examples include:

- Work Management item;
- source-control commit/PR/branch;
- CI/CD run/job/test report;
- artifact-store object;
- observability trace/log/metric series;
- provider identity/group/entitlement object;
- model-provider invocation record;
- external policy record;
- external architecture source;
- externally stored evidence bytes/data.

A provider object does not become a canonical AE entity merely because its API exposes an object type.

## 8. D — Derived views/projections/context products

Examples:

- Context Package;
- search index;
- vector representation/embedding;
- generated summary;
- dashboard/status projection;
- rendered Contract/Plan page;
- Plan IG;
- generated architecture visualization when derived from an authoritative Architecture Model;
- context compaction;
- recommendation/ranking projection;
- conformance projection from authoritative Validation records.

A derived object may be cached or persisted operationally, but deletion/reconstruction must not destroy canonical truth.

### Context provenance hook

Context Package content is disposable, but material context provenance may not be.

When a consequential decision/action/Plan/Validation/risk acceptance materially depends on assembled context, later Context/Memory design must preserve enough provenance to determine which authoritative/provenance-bearing sources materially informed it. L1-C does not create a new first-class Context Provenance entity; the mechanism is deferred to L1-G.

## 9. E — Ephemeral operating state

Examples:

- L4 agent micro-plan;
- scratch execution sequencing;
- exploratory reasoning;
- temporary tool/session state;
- local retries with no material durable consequence.

### L4 promotion rule

L4 is ephemeral by default. Material information discovered during L4 is promoted into the durable object that semantically owns it, for example:

- consequential choice → DR/ADR;
- changed Plan assumption → Plan revision;
- Contract issue → Contract Change Proposal;
- continuation need → Handoff Record;
- evidence → Evidence Record;
- learning → Learning Record.

L4 is not persisted merely because it existed.

## 10. F — Normative definitions/release objects

These belong to the Canonical AE Distribution, not one operational Loop:

- Canonical AE Release Manifest;
- canonical type/domain definitions;
- canonical relationship-type definitions;
- canonical lifecycle semantics;
- Capability Contract Definitions;
- canonical responsibility/role definitions;
- future canonical schemas/validators.

An Organization-specific AE Implementation references but does not mutate these normative definitions.

The **Canonical AE Release Manifest** must allow an implementation to identify the exact Canonical AE release/Core definition it claims to implement.

## 11. Representation principles

### Plan

One Plan entity/revision may have multiple conforming representations, including machine-readable form, Human-readable document, interactive Plan IG, or generated views. These are representations of one Plan revision, not competing Plan entities.

Later integrity rules must make it possible to determine whether multiple representations correspond to the same canonical Plan revision.

### Product/System Baseline

The Product/System Baseline is the canonical A1 entity. A Baseline Manifest is a representation/snapshot of an exact Baseline revision, not the ontology itself.

### Architecture

A diagram file is not automatically the Architecture Model. An Architecture Representation may be authoritative, externally referenced, or derived depending on the implementation's declared authority/source model.

## 12. Open design concern preserved

L1-C deliberately does **not** create an `Engineering Environment Profile` entity.

Open issue **#6 — Engineering Team Interface / Working Environment — interface parity across heterogeneous development environments** preserves the principle:

> **AE should require interface parity, not environment uniformity.**

Current entities—especially AE Implementation Profile, Capability Binding, Product/System Baseline, Contract, Plan, and Context/Handoff semantics—must remain extensible enough for later Adoption/Capability/Runtime/Developer-Experience design to define how humans and agents access AE from heterogeneous working environments.