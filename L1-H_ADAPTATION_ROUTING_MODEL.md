# L1-H — Adaptation and Routing Model

## 1. Semantic decision test

Canonical AE uses a semantic boundary test rather than one universal numeric materiality threshold.

### LOCAL_ADAPTATION

Use local adaptation when an implementation adjustment remains within the reviewed Plan's explicit adaptation boundaries and does not materially change the reviewed engineering route.

Local adaptation must not materially alter, as applicable:

- reviewed scope/outcome;
- Contract Goal/Spec/Proof;
- dependency/barrier meaning;
- architecture commitments/assumptions requiring new decision/review;
- authority/capability requirements;
- Verification/Test Strategy or evidence route;
- material risk/constraint assumptions;
- another declared Plan boundary.

Ordinary implementation detail should fit here when the reviewed route remains intact.

### RETRY_EXECUTION

Use Retry when execution failed or produced an inadequate implementation/result, but the reviewed Plan route remains valid and another attempt is appropriate under the same governing semantics.

Retry preserves prior failed execution/Verification/Validation history and uses L1-D route semantics.

### REPLAN

Use Replan when the Contract remains valid but the reviewed engineering route materially changes.

Replan creates a new Plan revision and requires applicable review for affected scope. Prior Plan/review/history remain intact.

### PROPOSE_CONTRACT_CHANGE

Use Contract Change Proposal when Goal, Spec, Proof, or another Contract-level semantic must change.

Planning/Execution may propose the change but may not silently mutate the Contract. G5 and Human Decision Authority remain controlling.

### ESCALATE

Use Escalate when a required risk, decision, authority, policy, or unresolved condition cannot be resolved inside the actor's authority/current governed route.

Escalation blocks only affected scope unless other work can no longer continue meaningfully or safely.

## 2. Summary invariant

> implementation adjustment inside reviewed boundaries → local adaptation  
> transient execution failure while route remains valid → Retry  
> material reviewed-route change with Contract valid → Replan  
> Goal / Spec / Proof change → Contract Change  
> unresolved authority/risk/decision issue → Escalate

> **Execution may adapt within the reviewed Plan's authorized adaptation boundaries. It may not silently change the reviewed Plan or approved Contract.**

## 3. Architecture-triggered routing

- ordinary architecture/model updates inside the reviewed route may execute normally;
- a consequential architecture choice requiring an ADR creates/relates an ADR;
- architecture discovery that materially changes the reviewed route triggers Replan;
- architecture discovery exposing Contract deficiency triggers Contract Change Proposal;
- not every code or implementation change becomes an ADR.

## 4. Worker signals

Worker results may signal `PLAN_DEFICIENCY`, `CONTRACT_DEFICIENCY`, `ARCHITECTURE_DECISION_REQUIRED`, `DEPENDENCY_CONFLICT`, `AUTHORITY_BLOCK`, or similar subordinate conditions. These signals route material information to the proper durable semantic owner; they do not themselves rewrite Plan/Contract state.
