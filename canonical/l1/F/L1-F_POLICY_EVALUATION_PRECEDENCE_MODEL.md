# L1-F — Policy Evaluation & Precedence Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Policy result

Final protected-operation authority evaluation uses:

- **PERMIT**
- **DENY**
- **INDETERMINATE**

Subordinate policy modules/sources may use **NOT_APPLICABLE**.

## 2. Meanings

**PERMIT** — applicable authoritative facts authorize the request, subject to any required conditions/obligations.

**DENY** — authoritative facts deterministically forbid the request.

**INDETERMINATE** — required authoritative state or deterministic policy resolution cannot currently be established reliably.

Absence of an explicit grant may be DENY when authoritative policy defines `no qualifying authority = DENY`.

For a protected operation, INDETERMINATE is never permission.

## 3. Conditions / obligations

PERMIT may carry required enforceable conditions without prescribing a universal DSL.

Examples:

- environment restriction;
- exact approval reference;
- time boundary;
- evidence/audit obligation;
- resource constraint.

Required conditions must be carried to an applicable PEP and enforced as part of protected-operation Proof.

## 4. Precedence and combination

Canonical requirements:

1. Canonical authority constraints cannot be weakened downstream.
2. Organization/Product policy precedence or combination is deterministic.
3. Product/System specialization may tighten/narrow but cannot silently weaken mandatory organization controls.
4. Exceptions, where permitted, are explicit, authorized, scoped, versioned/provenanced, and bounded by time/condition where applicable.
5. No unresolved applicable policy conflict may produce PERMIT.

Unresolved applicable conflict therefore yields:

`INDETERMINATE → BLOCKED`.

Canonical AE does not require one universal combining algorithm such as global deny-overrides.

## 5. RBAC / ABAC / ReBAC portability

Role is relevant context but is not itself canonical authority.

RBAC-only, ABAC, ReBAC, task/resource policy, and mixed implementations may conform if they can express and enforce the required scoped semantics and produce equivalent canonical results.

## 6. Provider entitlement interaction

Policy PERMIT does not grant provider entitlement.

- `PERMIT + entitlement present + enforcement + provider operability → ALLOWED`
- `PERMIT + entitlement missing → BLOCKED`
- `DENY → DENIED`
- `INDETERMINATE → BLOCKED`
