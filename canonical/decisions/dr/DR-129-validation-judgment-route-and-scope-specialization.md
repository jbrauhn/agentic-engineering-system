# DR-129 — Validation judgment, lifecycle route, and scope specialization

## Status

Adopted for L1-I.

## Decision

1. R6 independent Validation judgment and R1 lifecycle route are distinct semantics.
2. Validation Record expresses the exact judgment, rationale, Evidence basis, independence provenance, and scope; R1 retains lifecycle routes `ACCEPT`, `RETRY_EXECUTION`, `REPLAN`, `PROPOSE_CONTRACT_CHANGE`, and `ESCALATE`.
3. Judgment-to-route mapping must be deterministic/reconstructable under applicable facts/policy, but R6 does not directly become lifecycle control.
4. Contract/Proof deficiency routes through Contract Change Proposal + existing G5/Human Decision Authority; Validator may not mutate Contract.
5. One core Validation protocol is reused for engineering Increment, final Contract, installation/adoption, Capability Binding/readiness, and other governed Validation scopes. Specialize Validation Requirement/scope, not entity type.
6. Validation judgment is not automatically Human DA; separate authority requirements remain separate when Contract/OEB/Product policy requires them.

## Rationale

Making the Validation result identical to a lifecycle route would collapse R6 judgment into R1 control and obscure why a route was selected. Creating separate Validation entity models for adoption or capability assessment would duplicate semantics and increase reconciliation burden.

## Consequences

- failed Validation history remains durable through Retry/Replan;
- final Contract acceptance remains a distinct independent judgment;
- provider Validation mechanisms/results do not automatically become canonical Validation Records;
- adoption/conformance remains Validation-backed rather than mutable status state.

## Traceability

Contract lifecycle/Validation; DR-083; DR-113; L1-D R1 routes/G4/G5; L1-C Validation Record; L1-E Validation capability; L1-F Human DA; L1-H adaptation/backward-route model.
