# L1-I — Validation Judgment, Lifecycle Route, and Final Reconciliation Model

## Purpose

Keep independent Validation judgment semantics in R6 distinct from R1 lifecycle routing while preserving deterministic traceability between them, and define final Contract-scope reconciliation without ceremonial retesting.

## Validation judgment [R6]

A Validation Record [A2] issues an independent judgment against an exact Validation Requirement and declared scope.

Canonical judgment classes include, at minimum:

- `PROOF_SATISFIED`;
- `PROOF_NOT_SATISFIED_EVIDENCE_INCOMPLETE`;
- `PROOF_NOT_SATISFIED_IMPLEMENTATION_DEFECT`;
- `PROOF_NOT_SATISFIED_PLAN_ROUTE_DEFICIENT`;
- `CONTRACT_OR_PROOF_DEFICIENCY_DETECTED`;
- `UNABLE_TO_ESTABLISH_TRUSTWORTHY_EVIDENCE_OR_STATE`.

Organizations may add finer-grained subordinate findings, but they must not erase these core semantic distinctions when applicable.

## Lifecycle route [R1]

The resulting lifecycle route remains an R1 concern using the established L1-D vocabulary:

- `ACCEPT`;
- `RETRY_EXECUTION`;
- `REPLAN`;
- `PROPOSE_CONTRACT_CHANGE`;
- `ESCALATE`.

Validation judgment and lifecycle route are related but not identical.

Examples:

- `PROOF_SATISFIED` → normally `ACCEPT` when all other applicable gates/authority are satisfied;
- `PROOF_NOT_SATISFIED_EVIDENCE_INCOMPLETE` → often `RETRY_EXECUTION` or `ESCALATE`, depending on whether the reviewed route remains valid and missing Evidence can be produced;
- `PROOF_NOT_SATISFIED_IMPLEMENTATION_DEFECT` → usually `RETRY_EXECUTION` when the reviewed route remains valid, otherwise `REPLAN`;
- `PROOF_NOT_SATISFIED_PLAN_ROUTE_DEFICIENT` → `REPLAN`;
- `CONTRACT_OR_PROOF_DEFICIENCY_DETECTED` → `PROPOSE_CONTRACT_CHANGE`;
- `UNABLE_TO_ESTABLISH_TRUSTWORTHY_EVIDENCE_OR_STATE` → `ESCALATE` or another policy-defined non-accept route, never implicit acceptance.

The exact mapping may depend on declared scope/policy/facts, but it must be deterministic and reconstructable. R6 does not silently mutate lifecycle state.

## Acceptance invariant

G4 acceptance requires:

- exact Contract revision;
- applicable Proof criteria/scope;
- independent Validation judgment;
- sufficient trustworthy Evidence/current state;
- required independence characteristics;
- any separate applicable authority/approval requirements.

Provider status, executor Evidence, or external Validation-provider result alone cannot issue G4 acceptance.

## Retry / Replan / Contract Change history

- Retry preserves failed Validation history and normally keeps the reviewed route when it remains valid.
- Replan preserves prior Plan revisions, Plan Reviews, Evidence, and Validation history; affected scope requires a new Plan revision/review before execution.
- Contract deficiency preserves current Contract/Validation history and routes through Contract Change Proposal + existing G5/Human Decision Authority. Validator cannot edit Contract semantics directly.

## Increment versus final Contract Validation

Increment Validation judges a bounded scope. Increment `ACCEPTED` does not imply final Contract/Loop acceptance.

Final Contract-scope Validation may reuse valid prior Increment Evidence and Validation Records. Canonical AE does not require ceremonial rerun of every prior test.

Final Validation must reconcile, as applicable:

- all applicable Contract Proof criteria;
- cross-Increment interactions;
- integration effects;
- final system/product state;
- unresolved prior findings/limitations;
- multiple historically valid Plan/Contract/Baseline revisions;
- final effective Contract revision/scope;
- gaps that local Increment Validation could not observe;
- current reliance of Evidence/prior Validation being reused.

Final acceptance requires an independent judgment against the final applicable Contract scope/revision and Proof.

## Final-reconciliation minimum

A conforming implementation must be able to show:

1. which prior Evidence/Validation judgments are reused;
2. why they remain applicable/reliable for the final scope;
3. which cross-scope/final-state concerns required additional Evidence or judgment;
4. how the final applicable Contract Proof is completely covered;
5. how unresolved contradictions/limitations were dispositioned;
6. the independent Validator path/provenance for final judgment.

No specific integration-test framework or rerun process is canonical.

## Adoption / installation / capability Validation

The same core protocol applies to:

- engineering Increment Validation;
- final Contract Validation;
- Organization-specific AE installation/adoption Validation;
- Capability Binding/readiness Validation;
- other governed scopes.

Specialize the Validation Requirement/scope. Do not create duplicate Validation entity types.
