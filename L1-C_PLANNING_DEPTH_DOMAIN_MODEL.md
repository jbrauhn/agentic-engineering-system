# L1-C — Planning Depth Domain Model

**Status:** Approved L1-C semantic baseline  
**Authority:** inherited Planning decisions DR-023–DR-035; Human Owner L1-C decision  
**Scope:** Domain semantics for Contract, Plan, L1/L2/L3/L4. Planning methods/execution algorithms remain downstream.

## 1. Preserve the adopted hierarchy

Canonical planning/work depth remains:

```text
Contract
  ↓ constrains
Plan
  ↓ plans against
L1 — Product/System Baseline
  ↓ Plan decomposes work into
L2 — Execution Increment
  ↓ decomposes into
L3 — Executable Task
  ↓ may be locally executed through
L4 — Agent micro-plan
```

This is **not** one polymorphic `PlanItem` hierarchy.

Each level has different durability and governance semantics.

## 2. Contract remains above Planning

Contract defines:

- Goal;
- Spec;
- Proof;
- Non-goals where applicable.

Proof remains part of Contract.

Planning does not rewrite Proof. Planning derives the **Verification/Test Strategy** and route by which Execution will produce evidence against Contract Proof.

## 3. Plan — A1

Plan is the governed architecture-aware route from approved Contract intent to execution/evidence.

A Plan revision references:

- exact Contract revision;
- exact Product/System Baseline revision it plans against;
- architecture elements/relationships affected as applicable;
- decomposition into L2/L3 work;
- Verification/Test Strategy derived from Proof;
- dependencies/risks/constraints;
- required capabilities/authority/context;
- allowed adaptation boundaries.

### One Plan, multiple representations

DR-033 remains explicit:

> **One Plan entity/revision may have multiple conforming representations.**

Examples:

- machine-readable representation;
- Human-readable document;
- interactive Plan IG;
- generated views.

They are not separate competing Plan entities.

Representation integrity must later allow a Human/agent to determine whether the representations correspond to the same canonical Plan revision.

## 4. L1 — Product/System Baseline — A1

The canonical entity is **Product/System Baseline**.

It is durable Product/System state that persists across normal AE Loops and is not another Plan.

A Baseline revision can reference exact revisions of persistent state such as:

- Product/System Profile;
- Architecture Model;
- relevant DRs/ADRs;
- applicable standards state;
- relevant engineering-health state;
- other durable baseline material.

### Baseline Manifest

A **Baseline Manifest** is a representation/snapshot of one exact Product/System Baseline revision.

It can enumerate the constituent authoritative revisions used to establish the baseline.

> **Product/System Baseline = domain entity. Baseline Manifest = representation/snapshot.**

The Baseline does not aggregate ownership of the referenced entities.

## 5. L2 — Execution Increment — A1

Execution Increment is the bounded slice of engineering work a Plan intends to deliver/validate together.

Its canonical semantics may include:

- stable identity;
- parent Plan relationship;
- intended bounded outcome/scope;
- dependencies;
- contained/decomposed L3 Tasks;
- relevant architecture/work references;
- progress/outcome relationships;
- evidence/Validation relationships as appropriate.

Detailed state machine and sizing method are downstream.

## 6. L3 — Executable Task — A1

Executable Task is the smallest canonical durable work unit that AE needs to coordinate/trace independently.

Canonical semantics are intentionally minimal and provider-neutral:

- stable identity;
- intended engineering work;
- parent Execution Increment;
- dependencies required by AE semantics;
- Contract/Plan traceability;
- relevant architecture relationships;
- authority/evidence relationships as needed.

### Provider Work Item is not the Task ontology

A Task can be `realized_by` an External Resource Reference to a Work Management item.

Provider properties may remain authoritative in Work Management.

> **Do not build a shadow Work Management database.**

L1-C does not decide the exact field split. Later Work Management/Capability design shall work backwards from lifecycle needs and retain only canonical Task semantics that AE actually requires.

## 7. L4 — Agent micro-plan — E

L4 is local execution planning inside an actor/agent context.

It is ephemeral by default and does not become a canonical durable object simply because an agent reasoned through steps.

### Promotion rule

Material information is promoted according to semantic ownership:

- consequential engineering choice → DR/ADR;
- changed reviewed Plan assumption → new Plan revision/review as applicable;
- Contract issue → Contract Change Proposal;
- continuation across actor/session boundary → Handoff Record;
- produced material evidence → Evidence Record;
- durable conclusion → Learning Record.

This preserves agent adaptability without losing material system state.

## 8. AE Loop relationship to planning depth

AE Loop is the durable coordination/correlation context.

It may reference:

- exact Contract revision;
- exact Plan revision;
- exact Product/System Baseline revision;
- L2/L3 work;
- relevant Decisions, Evidence, Validation, Handoffs and Learning.

It does **not** own the persistent Product/System Baseline, Architecture Model, OEB, Product/System Profile, DR/ADR history, or Learning Records merely because the Loop used them.

## 9. Plan Review

Plan Review Record is an A2 issued record that evaluates an exact Plan revision.

Material Plan change after review requires applicable re-review/new review rather than editing the prior Plan Review Record.

The detailed review method remains downstream.

## 10. Verification/Test Strategy vs Proof

Proof Criterion belongs to Contract revision.

Verification/Test Strategy belongs to Plan revision.

Relationship conceptually:

```text
Contract revision / Proof Criterion
        ↓ drives
Plan revision / Verification-Test Strategy
        ↓ guides
Execution + Verification
        ↓ produces
Evidence Records
        ↓ used by
Independent Validation
```

This preserves the distinction between defining what must be proven and planning how evidence will be generated/checked.

## 11. Architecture-aware Planning

Plan references structural Architecture Element identities rather than depending only on prose or diagram filenames.

At minimum the domain supports relationships such as:

- Plan affects Architecture Element;
- Task affects/implements change to Architecture Element;
- Plan plans against Architecture Model/Baseline revision;
- ADR affects Architecture Element/Relationship.

Detailed architecture-impact analysis remains downstream.

## 12. Context and working environment

Planning-depth entities remain independent of a particular developer/agent environment.

Open issue **#6** later determines how a Human/agent in heterogeneous environments obtains the correct Contract, Plan, Baseline, architecture, capabilities, context, and authority.

L1-C does not assume the Plan is delivered through a Portal, local file, IDE extension, Dev Container, CLI, or one agent host.