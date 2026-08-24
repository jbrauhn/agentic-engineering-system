# L1-H — Canonical Plan Semantic Model

**Status:** Human Owner-approved L1-H semantic baseline  
**Authority:** Contract v1.0; DR-020–035; DR-108–123; Human Owner L1-H approval  
**Scope:** Provider-neutral Planning semantics. A Plan is not a provider workflow, scheduler, task board, or orchestration product.

## 1. Plan purpose

A Plan is the governed, architecture-aware route from an exact approved Contract toward its Proof. It must be executable, reviewable, traceable, and bounded enough for safe adaptation without becoming a giant universal form.

> **One Plan may have multiple conforming representations; representation is not a second Plan entity.**

## 2. Minimum semantics

A conforming Plan revision supports, as applicable:

- exact governing Contract revision;
- exact Product/System Baseline revision;
- declared Plan scope and intended outcome;
- affected Architecture Model elements/relationships;
- L2 Execution Increment / L3 Executable Task decomposition, or explicit progressive-elaboration rules;
- dependency, sequencing, and barrier constraints;
- parallelizable work topology where applicable;
- Planning Depth and Planning Method;
- Context Requirements;
- required Capability Operations and applicable Binding expectations;
- inherited authority/policy/approval requirements;
- Verification/Test Strategy derived from Contract Proof;
- evidence-production expectations;
- Validation-readiness and continuation/handoff expectations;
- material risks, constraints, assumptions, and unresolved questions;
- permitted adaptation boundaries;
- explicitly deferred future detail and its elaboration envelope.

Conditionally applicable semantics may be expressed through typed subordinate structures and relationships. Absence of an irrelevant section does not make a Plan nonconforming.

## 3. Exact-revision control

Planning references exact/effective governed state rather than selecting the newest revision by default.

A Plan revision identifies the exact Contract and Product/System Baseline against which it was created/reviewed. A later revision does not silently rewrite historical Plan meaning or automatically invalidate unrelated scope.

## 4. Planning Depth / Method

Planning Depth expresses how far decomposition has been carried for the declared scope. Planning Method identifies the method used to obtain a credible route. Canonical AE requires both concepts but does not require one method or one universal depth.

Depth must be sufficient for the scope being authorized to execute. Future detail may remain deferred under an approved elaboration envelope.

## 5. Plan Review relationship

Plan Review applies to an exact Plan revision and explicit scope under L1-D G2 semantics.

Changed scope may not inherit review merely because it descends from or resembles a reviewed Plan. Unaffected scope may continue under an older reviewed Plan revision only when deterministic impact analysis establishes that later Plan changes do not alter its reviewed semantics or dependencies.

## 6. Proof → Verification → Evidence → Validation

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

A Plan therefore explains how the work intends to establish the Contract's Proof without allowing executor-created evidence or test success to become self-Validation.

## 7. Provider independence

Canonical Plan semantics are independent of Jira/Plane/Azure DevOps/GitHub, source-control layout, CI topology, branch strategy, scheduler, worker count, or orchestration runtime.

Provider objects may realize or reference Plan/work semantics, but provider status does not become Canonical AE lifecycle or Validation truth.
