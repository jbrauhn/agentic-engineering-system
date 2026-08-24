# L1-D — Canonical Lifecycle / State Protocol

**Status:** Approved L1-D semantic baseline  
**Authority:** Contract v1.0; DR-017; DR-019; DR-106; DR-107; DR-108–110; Human Owner L1-D decision  
**Scope:** Canonical lifecycle/state semantics only. This does not prescribe a centralized workflow engine, runtime, queue, database, agent topology, provider workflow, Portal, CLI, IDE, or developer environment.

## 1. Canonical shape

Canonical AE uses a **composite/scoped lifecycle-state protocol**.

The familiar Human-readable projection:

`Work arrives → Loop Context → Contract → Planning → Plan Review → Execution → Validation → Learning / durable state`

remains useful, but it is not sufficient as canonical machine truth.

Canonical lifecycle truth is composed from the applicable combination of:

- AE Loop control state;
- scope-specific lifecycle position;
- artifact/revision state;
- evidence-backed gate evaluation;
- blocking conditions;
- routes/dispositions;
- exact governing revisions;
- append-only or otherwise non-destructively reconstructable transition history.

A Human-facing `current phase` may be derived as a D/view projection. It shall not override the underlying scoped facts.

## 2. Why the Loop does not have one exclusive phase

A valid AE Loop may simultaneously contain:

- Increment A — EXECUTING;
- Increment B — PLANNING;
- Increment C — VALIDATING.

The Loop can remain `OPEN` while those scope-specific positions coexist. This supports rolling-wave Planning, parallel Tasks, independent Increment Validation, and later orchestrator/worker patterns without making the top-level lifecycle a waterfall workflow.

## 3. AE Loop control state

The canonical Loop control states are deliberately small:

- **OPEN** — the Loop remains active and can continue governed work;
- **SUSPENDED** — Loop-wide governed continuation is not currently possible;
- **CLOSED** — the Loop no longer accepts normal lifecycle work.

`SUSPENDED` is used only when the Loop as a whole cannot meaningfully continue. A blocked Task, Increment, decision request, or Contract-change question does not automatically suspend the Loop if unaffected governed work can continue.

### Loop terminal disposition

A `CLOSED` Loop has one terminal disposition:

- **ACCEPTED**;
- **CANCELLED**;
- **SUPERSEDED**.

Cancellation reasons carry lower-level explanations such as duplicate, external termination, cost/risk stop, or abandoned work rather than proliferating canonical terminal states.

`SUPERSEDED` remains distinct because the replacement relationship is traceably meaningful.

## 4. L2 Execution Increment lifecycle

Active lifecycle positions:

- **PLANNING**;
- **READY**;
- **EXECUTING**;
- **VALIDATING**.

Terminality is orthogonal to active lifecycle position. A terminal Increment has one disposition:

- **ACCEPTED**;
- **CANCELLED**;
- **SUPERSEDED**.

> **Lifecycle position describes active governed work. Terminal disposition describes how that scope ended.**

Blocking is also orthogonal. An Increment may be `EXECUTING + blocked` or `PLANNING + blocked` without inventing additional compound workflow states.

### Meaning

**PLANNING** — the bounded Increment/scope is being defined or refined and does not yet satisfy all execution gates.

**READY** — the exact applicable Contract/Plan/Baseline context and required gates for this execution scope have been established.

**EXECUTING** — authorized engineering work is occurring within reviewed Plan boundaries.

**VALIDATING** — the bounded Increment outcome is undergoing independent Validation.

**Terminal / ACCEPTED** — an independent Validation Record accepts the Increment scope. This does not establish whole-Contract or Loop acceptance.

## 5. L3 Executable Task portable state

Canonical AE uses only the small execution projection needed for portable coordination:

- **NOT_STARTED**;
- **ACTIVE**;
- **COMPLETE**.

Blocking may be represented orthogonally where canonically relevant.

Work Management provider workflows remain provider-owned and can be richer. A Capability Binding may map provider state into this projection.

> **Task COMPLETE means execution work for that Task is complete. It does not establish independent Validation or Increment/Loop acceptance.**

Therefore:

`Provider Work Item = Done` **≠** `AE Validation = Accepted`.

## 6. Artifact/revision state remains separate from lifecycle position

Contract and Plan revision state is not encoded as Loop phase.

### Contract revision

Existing Contract semantics remain in force, including draft/proposed/approved/superseded behavior and immutable approved revisions.

Governed Planning/Execution/Validation scopes must identify the exact approved Contract revision that currently governs them.

### Plan revision

A Plan revision can be drafted, reviewed, superseded, or otherwise governed through its own record semantics. A mutable `reviewed=true` field is not the source of truth for review; the authoritative historical fact is the applicable Plan Review Record against an exact Plan revision and explicit review scope.

## 7. Blocking conditions

A blocking condition prevents one or more protected transitions without necessarily changing the underlying lifecycle position.

Examples include:

- pending Human Decision;
- authority cannot currently be established;
- authoritative Contract/Plan/Baseline revision unavailable;
- required Plan Review cannot be verified;
- unresolved Contract-effectivity question;
- escalation requiring disposition.

Blocking conditions are scope-aware. Only a Loop-wide unresolved condition normally moves Loop control to `SUSPENDED`.

## 8. Routes/dispositions are not phases

Canonical controlled routes include:

- **ACCEPT**;
- **RETRY_EXECUTION**;
- **REPLAN**;
- **PROPOSE_CONTRACT_CHANGE**;
- **ESCALATE**.

Cancellation/supersession are terminal dispositions rather than normal lifecycle phases.

A route selects governed direction after an outcome; it does not become another long-lived workflow phase by default.

## 9. Local adaptation boundary

> **Execution may adapt within the reviewed Plan's authorized adaptation boundaries. It may not silently change the reviewed Plan or approved Contract.**

- local adaptation inside reviewed boundaries stays in Execution;
- material Plan change routes to Replan, a new Plan revision, and applicable re-review;
- Goal/Spec/Proof change routes through a Contract Change Proposal and Human Decision Authority before a new Contract revision can govern affected work.

L1-D establishes the route distinction but does not define the later L1-H threshold for what constitutes a material Plan change.

## 10. Contract revision effectivity

Every governed active Execution/Validation scope must have an explicitly determinable **governing exact Contract revision**.

When a Contract Change Proposal is approved and creates a new Contract revision:

1. the new revision becomes an approved Contract revision;
2. affected active scopes undergo explicit impact/effectivity evaluation;
3. affected scopes may not continue under assumptions invalidated by the new revision;
4. unaffected scopes may continue under a prior exact Contract revision only when that continuation is explicitly determined valid;
5. no scope silently switches to the new revision;
6. no scope silently continues under a superseded assumption.

Multiple exact Contract revisions may therefore remain operationally relevant within one Loop for explicitly bounded scopes during a transition period.

For every governed active scope the implementation must be able to answer:

> **Which exact Contract revision governs this work right now, and why?**

This is revision effectivity, not competing Contract identity.

## 11. Final Loop acceptance

Increment acceptance does not imply whole-Contract acceptance.

> **All Increments individually ACCEPTED does not automatically prove that the overall Contract has been satisfied.**

Before `Loop = CLOSED / ACCEPTED`, an independent final Validation judgment must cover the final applicable Contract scope/revision and its Proof.

That final judgment may reuse Evidence Records and prior Increment Validation Records where still valid and may add integration/final-state evidence as needed. It does not require re-running lower-level tests ceremonially.

The final acceptance step must reconcile any accepted work that remains traceable to earlier Contract revisions so earlier revision effectivity does not become invisible.

## 12. Learning at closure

Every Loop requires a **learning disposition**, not necessarily a Learning Record.

- material learning exists → create applicable Learning Record(s) or another governed durable disposition;
- no material learning exists → record that fact as subordinate closure state.

A Loop shall not generate meaningless Learning Records simply to satisfy a checkbox.

## 13. Interface neutrality

The lifecycle protocol is a semantic contract and must remain callable/enforceable from heterogeneous working environments.

It shall not assume one:

- IDE;
- Dev Container;
- CLI;
- local daemon;
- remote workspace;
- CI environment;
- agent runtime;
- Portal.

Issue #6 remains open and preserves the principle:

> **AE should require interface parity, not environment uniformity.**
