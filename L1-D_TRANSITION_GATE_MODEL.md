# L1-D — Canonical Transition / Gate Model

**Status:** Approved L1-D semantic baseline  
**Scope:** Governed transition, gate, exact-revision, authority, and blocking semantics. This does not prescribe a workflow engine or policy implementation.

## 1. Keep the control concepts distinct

Canonical AE distinguishes:

- **lifecycle position** — active governed position of a scope;
- **entity/revision status** — state of Contract, Plan, or other domain object;
- **gate** — evidence-backed prerequisite for a protected transition;
- **transition** — governed movement between canonical positions/states;
- **route/disposition** — controlled direction selected after an outcome;
- **blocking condition** — prerequisite/condition preventing continuation without necessarily changing lifecycle position;
- **Authority Decision** — durable A2 governance record;
- **provider workflow status** — provider-owned operational state;
- **phase projection** — D/derived Human-facing summary.

These concepts shall not be collapsed into one provider-style status field.

## 2. Canonical gate families

### G1 — Contract Approval Gate

Question:

> Is the exact Contract revision presented for this governed use approved?

A `SATISFIED` projection must resolve to the authoritative approval/decision provenance for that exact revision.

### G2 — Plan Review Gate

Question:

> Has the exact Plan revision received the required review disposition for the explicit declared execution scope being requested?

The authoritative fact is the applicable **Plan Review Record**, not an editable Plan status.

Review scope shall be unambiguous and reconstructable. Typed scope anchors may include:

- Execution Increment identity;
- Executable Task identity;
- Architecture Element/Relationship identity;
- another typed scope descriptor defined later.

`the relevant parts of the Plan` is not sufficient scope identification.

### G3 — Authority Gate

Question:

> Is the identified actor authorized to perform this protected action/transition against this scope/resource under applicable Operational Authority, Decision Authority, identity, and policy conditions?

The detailed OA/DA/entitlement grammar remains downstream. L1-D requires only that the gate be evaluable and fail closed where required authority cannot be established.

### G4 — Validation Acceptance Gate

Question:

> Does an independent Validation Record accept this exact governed scope against the applicable Contract/Proof/evidence context?

The gate must resolve to the exact Validation Record and the exact Contract/Proof scope it judged.

### G5 — Contract Change Gate

Question:

> Has the Contract Change Proposal received the required Human Decision Authority disposition so that a new Contract revision may become approved/authoritative for affected work?

A proposal has no governing authority merely because it exists.

## 3. Gate state is a projection, not independent truth

Gate evaluation states are:

- **SATISFIED**;
- **UNSATISFIED**;
- **UNKNOWN**.

A cached/displayed gate state may be used operationally, but it must resolve to authoritative records/revisions/evidence.

Examples:

`G2 SATISFIED` → exact Plan Review Record → exact Plan revision → explicit review scope → applicable disposition.

`G1 SATISFIED` → exact Contract revision → applicable Authority Decision/approval provenance.

`G4 SATISFIED` → exact Validation Record → exact Contract/Proof scope → evidence context.

> **A gate evaluation is not an independently editable governance fact.**

## 4. Fail-closed semantics

For a required protected gate:

> **UNKNOWN ≠ SATISFIED.**

A transition request with an unresolved required prerequisite results in either:

- **DENIED** — the requested transition is invalid or unauthorized under established facts; or
- **BLOCKED** — the transition could become permitted when a missing prerequisite or authoritative fact is resolved.

Provider/network/state lookup failure does not imply authorization.

## 5. Revision coherence

A protected transition must evaluate the exact artifact revisions that govern the requested scope.

Examples:

### Stale Plan review

Plan Review Record covers `Plan rev4 / Increment A`.

Execution request uses `Plan rev5 / Increment A`.

Result: the rev4 review cannot satisfy G2 for rev5. Execution is denied/blocked until the applicable review exists.

### Contract mismatch

An execution scope is governed by `Contract rev2`.

A later `Contract rev3` is approved.

The implementation must not silently substitute rev3 for rev2 or assume rev2 remains valid. Revision effectivity must be explicitly evaluated for that scope.

## 6. Scope-aware Plan Review

Plan Review is defined by:

> **exact Plan revision + explicit declared review scope**.

This permits rolling-wave Planning without silently transferring review authority.

Example:

- Plan rev4 reviewed for Increment A;
- Increment A may execute under rev4/scope A;
- Plan rev5 changes Increment B;
- Increment B needs the applicable rev5/scope B review;
- rev5 does not silently inherit rev4 review;
- rev5 does not automatically invalidate A if A's reviewed governing scope is unchanged and remains valid.

Review scope is a subordinate typed value/descriptor, not a new A1/A2 entity unless later identity/lifecycle evidence justifies promotion under DR-108.

## 7. Contract revision effectivity

When a new Contract revision is approved, every active governed Execution/Validation scope must receive an explicit effectivity determination.

Minimum effectivity semantics:

- scope identity;
- prior governing exact Contract revision;
- newly approved Contract revision;
- classification such as affected/unaffected;
- rationale/provenance or governing determination record/reference;
- resulting governing Contract revision for that scope;
- required route when affected (for example Replan/block pending impact handling).

Rules:

1. no active scope silently switches Contract revision;
2. no active scope silently continues under invalidated assumptions;
3. unaffected scope continuation under an older revision requires an explicit valid determination;
4. affected scope must be rebound/replanned/reviewed as required before protected continuation;
5. final Loop acceptance reconciles accepted work against the final applicable Contract scope/revision.

## 8. Transition request protocol

Every canonical protected transition must be evaluable from semantics equivalent to:

1. scope type and identity;
2. current canonical state/lifecycle position;
3. requested transition or route;
4. exact governing Contract revision;
5. exact Plan revision where applicable;
6. exact Product/System Baseline revision where applicable;
7. required gates;
8. gate evaluation plus authoritative record references;
9. actor identity/role and authority context;
10. blocking conditions;
11. valid source/target structural rule;
12. resulting state/disposition if allowed;
13. transition provenance/history record.

Different implementations may realize this through distributed mechanisms. R1 owns the semantics, not one central server.

## 9. Transition results

A protected transition request results in one of:

- **ALLOWED** — transition occurs and durable history records it;
- **DENIED** — invalid/unauthorized transition; protected state does not advance;
- **BLOCKED** — potentially valid transition awaiting resolvable prerequisite/authority/state.

Denied and blocked protected attempts must preserve enough provenance for later governance/reconstruction where material.

## 10. Pending Human Decision

Pending Human Decision is normally represented as:

- existing lifecycle position;
- blocking condition / decision required;
- exact target/scope/revision;
- eligible authority requirement;
- rationale/proposal/reference.

The eventual Authority Decision resolves the gate and determines the next valid route.

No Portal, approval screen, notification service, or Work Management status is canonical.

## 11. Transition Record / Event

Loop Transition Record/Event remains a B/subordinate record under DR-108.

Minimum applicable semantics:

- Loop identity;
- transition scoped identity;
- scope type + scope identity;
- prior lifecycle position/state;
- requested transition/route;
- result: ALLOWED / DENIED / BLOCKED;
- resulting state/disposition where applicable;
- actor identity/role;
- exact governing Contract revision;
- exact Plan revision where applicable;
- exact Product/System Baseline revision where applicable;
- gate evaluations plus authoritative record references;
- Authority Decision references where applicable;
- Plan Review references where applicable;
- Validation references where applicable;
- reason/disposition;
- timestamp/provenance.

Fields irrelevant to a particular transition are not forced.

History shall be append-only or otherwise non-destructively reconstructable. This does not mandate event sourcing.
