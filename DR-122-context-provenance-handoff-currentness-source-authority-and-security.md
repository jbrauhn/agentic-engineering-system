# DR-122 — Context provenance, Handoff, currentness, source authority, and security

**Status:** Accepted  
**Scope:** L1-G Knowledge / Context / Memory

## Decision

Use **Context Assembly Receipt / Source Manifest [B]** as lightweight provenance retained durably when consequential use or policy requires it; do not add a Context Provenance A2 record or universal prompt logging. This clarifies the L1-C context-provenance hook without changing the historical L1-C entity taxonomy.

Handoff Record remains the existing A2 continuation record and is authoritative only for what was handed off at issuance, not for current state of referenced artifacts. Receiving actors resolve current/effective authoritative references.

Context currentness is requirement-relative: `EXACT_REVISION`, `EFFECTIVE_FOR_SCOPE`, `CURRENT_AT_USE`, or `BEST_AVAILABLE/SUPPORTING`. Correct/effective revision beats naïve latest-revision selection.

Reuse DR-107 source authority. Unresolved competing authority claims cannot be silently ranked into truth; protected use blocks when required authoritative state cannot be established.

Derived context cannot grant broader information access than underlying sources absent an explicitly authorized/proven sanitization or declassification transformation.

## Rationale

Context must be trustworthy enough for consequential engineering without becoming an audit-record swamp, a second truth system, or an information-leak path.

## Consequences

- old Context Packages and Handoffs remain historical rather than silently rewritten;
- required currentness failures trigger reassembly/blocking rather than confident stale summaries;
- supporting stale context may degrade/constrain without always blocking;
- material context basis remains reconstructable when direct references alone are insufficient;
- context access remains subject to L1-F authority and source restrictions.
