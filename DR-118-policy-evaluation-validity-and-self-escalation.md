# DR-118 — Policy evaluation, precedence, validity, and self-escalation

**Status:** Adopted — Human Owner L1-F approval

## Decision

Protected authority/policy evaluation uses **PERMIT / DENY / INDETERMINATE**. Runtime continues to use **ALLOWED / DENIED / BLOCKED**.

Required authority that cannot be established reliably produces INDETERMINATE and therefore BLOCKED. A deterministic authoritative rule such as `no qualifying authority = DENY` produces DENY, not INDETERMINATE.

Policy precedence/combination may vary by organization, but must be deterministic. Canonical constraints cannot be weakened downstream, unresolved applicable policy conflict cannot produce PERMIT, and permitted exceptions must be explicit/authorized/scoped/provenanced.

Credential, entitlement, OA, and DA lifetimes are independent. Authority supports expiry/revocation/supersession/condition invalidation without rewriting history.

Authority-changing mutations use pre-change authority state. An actor cannot use the effects of its own authority mutation to authorize that mutation.

Delegation is optional and, when supported, is explicit, non-amplifying, bounded, provenanced, and cannot delegate Canonical Human-reserved DA to AI.
