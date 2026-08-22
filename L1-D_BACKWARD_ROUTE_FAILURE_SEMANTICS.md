# L1-D — Backward Route / Failure Semantics

**Status:** Approved L1-D semantic baseline

## 1. Principle

Retry, Replan, Contract Change, and Escalate are **routes/dispositions**, not lifecycle phases.

Backward routing preserves prior approved/reviewed/failed history. It does not rewrite the record to make the earlier path appear successful.

## 2. Retry Execution

Typical source condition:

- independent Validation finds an execution/implementation defect;
- governing Contract remains valid;
- reviewed Plan remains valid for the affected scope.

Canonical route:

`VALIDATING → RETRY_EXECUTION → EXECUTING`

Consequences:

- failed Validation Record remains immutable;
- governing Contract revision normally remains unchanged;
- governing reviewed Plan revision/scope normally remains unchanged;
- new/revised execution produces new Evidence Records;
- subsequent independent Validation produces a new Validation Record.

Retry shall not be used to hide a Plan or Contract defect.

## 3. Replan

Typical source condition:

- Execution or Validation shows the Plan is inadequate;
- Contract remains valid.

Canonical route:

`EXECUTING or VALIDATING → REPLAN → PLANNING → new Plan revision → applicable Plan Review → READY / EXECUTING`

Consequences:

- prior Plan revision remains historical;
- prior Plan Review Record remains historical;
- failed Validation/finding remains historical;
- affected scope cannot reuse stale review for the new Plan revision;
- re-review targets the new exact Plan revision and explicit declared scope.

## 4. Contract Change

Typical source condition:

- Goal, Spec, or Proof appears wrong, incomplete, or no longer appropriate.

Canonical route:

`finding → Contract Change Proposal → Human Decision Authority → approved/rejected`

Before approval:

- current approved Contract remains governing authority;
- proposal has no governing effect;
- affected protected work does not proceed as though the proposal were approved.

If rejected:

- current approved Contract remains authoritative;
- work resumes/replans/escalates/cancels as appropriate.

If approved:

- new Contract revision is created/approved;
- prior approved revision remains historical and immutable;
- active scopes undergo explicit Contract revision effectivity evaluation;
- affected scopes rebind/replan/re-review as required;
- explicitly unaffected scopes may continue under prior exact revision only with a valid effectivity determination;
- no active scope silently changes governing Contract revision.

## 5. Contract revision effectivity

An approved new Contract revision does not automatically rewrite the governing revision of every active scope.

For each active governed scope, the implementation must determine:

- prior exact governing Contract revision;
- new approved Contract revision;
- whether the scope is affected;
- why;
- resulting governing exact Contract revision;
- required route/action;
- provenance of that determination.

Ambiguous effectivity blocks protected continuation for the affected/uncertain scope.

Final Loop acceptance must reconcile accepted work against the final applicable Contract scope/revision so earlier revision effectivity cannot disappear from final Proof evaluation.

## 6. Escalate

Escalate is a route plus blocking/coordination semantics.

It preserves:

- current lifecycle position;
- affected scope;
- reason/uncertainty;
- exact governing revisions;
- authority/decision needed;
- provenance.

Affected protected work does not silently continue.

Possible resolution routes include:

- resume;
- Retry Execution;
- Replan;
- Contract Change Proposal;
- Cancel;
- Supersede;
- another later-defined valid disposition.

Scope-local escalation does not automatically set the entire Loop to `SUSPENDED`. Loop control moves to `SUSPENDED` only when the unresolved condition prevents meaningful Loop-wide governed continuation.

## 7. Stale review

Failure case:

1. Plan rev4 / scope A passes Plan Review.
2. Plan materially changes to rev5.
3. Execution is requested for rev5 / scope A.

Required behavior:

- rev4 review does not satisfy G2 for rev5;
- transition is DENIED or BLOCKED;
- execution begins only after applicable review of rev5/scope A.

A Plan revision can coexist with older reviewed Plan revisions for different scopes. Review authority never transfers implicitly.

## 8. Unknown authority or authoritative state

Examples:

- Authority Decision cannot be established;
- Contract authoritative revision cannot be established;
- Plan Review Record cannot be verified;
- required Capability Binding is ambiguous;
- Validation/evidence provenance cannot be established.

For protected transitions:

> **Unknown required authority/state is not approval.**

The result is DENIED when established facts make the action invalid/unauthorized, or BLOCKED when a missing prerequisite may later be resolved.

Read-only/degraded activities may continue only where downstream authority/policy design explicitly permits them.

## 9. Increment cancellation and supersession

An Increment can terminate without terminating the Loop.

Terminal dispositions:

- ACCEPTED;
- CANCELLED;
- SUPERSEDED.

Cancellation reasons carry explanatory detail rather than creating provider-style terminal states.

A superseded Increment should preserve a typed relationship to its replacement where one exists.

## 10. Increment acceptance versus Loop acceptance

Increment acceptance is an independent judgment over the Increment scope.

It does not prove the whole Contract because final Proof may include:

- cross-Increment/integration behavior;
- cumulative architecture/security/performance effects;
- final-state requirements;
- Proof Criteria spanning several Increments.

Therefore `all Increments ACCEPTED` is insufficient by itself for `Loop CLOSED / ACCEPTED`.

Loop acceptance requires an independent final Validation judgment covering the final applicable Contract scope/revision. It may reuse valid prior Evidence/Validation records and add only the integration/final evidence needed.

## 11. Self-acceptance prohibition

The work-producing actor/path cannot create authoritative acceptance merely by changing lifecycle state or a provider status.

G4 Validation Acceptance must resolve to an independent Validation Record satisfying later risk/policy-specific independence requirements.

`execution state mutation → accepted` without independent Validation is invalid.
