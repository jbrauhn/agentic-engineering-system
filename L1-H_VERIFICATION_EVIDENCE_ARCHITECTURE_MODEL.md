# L1-H — Verification, Evidence, Architecture, and Baseline Interaction Model

## 1. Verification / Evidence / Validation separation

> **Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.**

Intermediate Verification may occur throughout Execution. Test success, CI success, execution success, or executor-produced Evidence never creates Validation acceptance by itself.

The doer shall not become its own judge.

## 2. Verification/Test Strategy

For each applicable Proof criterion or evidence expectation, the Plan identifies enough strategy to establish:

- what will be verified/tested;
- where/when verification occurs;
- which capability/provider mechanism may perform it;
- expected evidence/provenance;
- how parallel evidence will be reconciled;
- what Validation will later need to evaluate.

The strategy may be progressively elaborated within a reviewed envelope, but a material change to the Verification/evidence route requires Replan/re-review.

## 3. Evidence production

Execution may create Evidence Records or durable references to provider-owned evidence. Physical evidence bytes do not have to be copied into AE state when exact identity/provenance/relationships remain reconstructable.

Parallel work must reconcile evidence so the Validation scope can determine which Contract/Proof criteria the combined result addresses.

## 4. Architecture interaction

Planning references affected Architecture Model elements/relationships. During Execution:

- ordinary model updates within the reviewed route may occur as governed work;
- consequential architecture decisions create/relate ADRs under inherited semantics;
- material architecture-route change triggers Replan;
- Contract-level deficiency triggers Contract Change Proposal.

Architecture state remains first-class R2 state rather than an executor-local diagram or context projection.

## 5. Product/System Baseline

Execution must not silently mutate the durable Product/System Baseline underneath active work.

The active scope continues against the exact/effective Baseline identified by its reviewed Plan. Resulting accepted/validated engineering state may later advance the Baseline through governed baseline-update semantics. L1-H establishes this boundary but does not define a separate Baseline-advancement workflow engine.

## 6. Validation readiness

A scope is Validation-ready only when required work has produced/referenced the evidence and reconciliation state needed for independent Validation against the applicable exact Contract/Proof. Provider task completion is insufficient.
