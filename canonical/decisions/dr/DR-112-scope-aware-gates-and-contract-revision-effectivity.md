# DR-112 — Gates are exact-scope/exact-revision and Contract revision effectivity is explicit

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner

## Context

DR-109 requires exact revision identity at governance boundaries. Rolling-wave Planning means different Execution Increments may legitimately use different exact Plan revisions. Approved Contract changes can also occur while bounded work is active.

A lifecycle model that relies on `current Plan`, `current Contract`, or editable approval flags would allow stale review, silent Contract switching, and ambiguous authority.

## Decision

Canonical lifecycle governance uses five explicit gate families:

1. **G1 — Contract Approval Gate**;
2. **G2 — Plan Review Gate**;
3. **G3 — Authority Gate**;
4. **G4 — Validation Acceptance Gate**;
5. **G5 — Contract Change Gate**.

Gate evaluation states are:

- SATISFIED;
- UNSATISFIED;
- UNKNOWN.

A gate evaluation is a projection of authoritative records/revisions/evidence, not independently editable truth. For protected gates, `UNKNOWN` is not equivalent to approval and fails closed.

## Scope-aware Plan Review

A Plan Review applies to:

> **an exact Plan revision + an explicit declared execution scope.**

Review scope must be reconstructable through typed scope anchors. Plan rev5 does not inherit rev4 review. A new Plan revision does not automatically invalidate an already-authorized unaffected scope governed by a prior exact reviewed revision.

## Contract revision effectivity

Every governed active Execution/Validation scope must have an explicitly determinable governing exact Contract revision.

When an approved Contract Change Proposal creates a new Contract revision:

1. the new revision becomes approved;
2. every active governed scope receives explicit effectivity evaluation;
3. affected scopes may not continue under invalidated assumptions;
4. unaffected scopes may continue under a prior exact revision only when explicitly determined valid;
5. no scope silently switches revision;
6. no scope silently retains invalid assumptions.

Multiple exact Contract revisions may remain operationally relevant inside one Loop during a controlled transition, but only for explicitly bounded scopes with deterministic effectivity.

## Human Decision and Contract change

A proposed Contract change has no governing authority until Human Decision Authority approves it. Existing approved Contract revision remains authoritative until then.

Pending Human Decision is represented through existing lifecycle position + blocking/decision-needed semantics + exact target/scope/revision. No Portal or standardized approval interface is required.

## Transition outcomes

Protected transition requests result in:

- ALLOWED;
- DENIED;
- BLOCKED.

DENIED means established facts make the transition invalid/unauthorized. BLOCKED means a potentially valid transition cannot proceed until a required prerequisite/state/authority is resolved.

## Alternatives considered

### Whole-Plan review only

Simpler, but any Plan revision becomes a synchronization barrier across all active work and undermines rolling-wave Planning.

### Automatically move all active scopes to newest Contract revision

Simpler current-state model, but silently changes the governing basis of in-flight work and destroys historical/revision correctness.

### Let implementation policy decide whether UNKNOWN means allowed

Rejected for protected transitions because missing authority/state must not become implicit authorization.

## Consequences

1. lifecycle state must carry/reconstruct exact governing Contract/Plan/Baseline revisions at material transitions.
2. machine fixtures/validators must mechanically reject stale Plan review, wrong Contract revision, unknown required authority, and ambiguous Contract effectivity.
3. downstream OA/DA and Planning domains refine detailed authority/material-change policy without changing these lifecycle semantics.
4. effectivity is revision governance, not a second Contract identity.

## Traceability

- Contract v1.0 authority, Contract-change, Planning, Validation, and fail-closed semantics.
- DR-012/013 — approved Contract immutability/change proposal.
- DR-034 — Plan Review and re-review semantics.
- DR-109 — exact revision identity.
- DR-110 — representation/provider separation.
- Human Owner L1-D D5–D9 plus Contract revision-effectivity refinement.
