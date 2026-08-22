# DR-119 — Distributed enforcement, bypass-path Proof, and federated authority provenance

**Status:** Adopted — Human Owner L1-F approval

## Decision

Canonical AE requires enforceable protected-operation boundaries but does not require one centralized PDP/PEP or authority database.

PEPs may be distributed. R4 coordinates authority/policy/decisions; R5 resolves/invokes capability bindings; PEPs enforce applicable decisions/conditions.

Protected-operation Proof must account for materially equivalent bypass paths available to the governed actor through identities, credentials, Access Paths, and runtime/working context in the declared protected scope. Unrelated enterprise administrators or separate identities unavailable to the governed runtime are outside this bypass test.

Authority state follows DR-107 federated authoritative-state semantics. Authorization evaluation provenance remains subordinate B semantics with risk/operation/policy-sensitive retention rather than making every runtime evaluation A2.

OEB/Product-System authority configuration references authoritative identity, entitlement, OA/DA, policy, enforcement, validity/revocation, provenance, and exception mechanisms without becoming the IAM/policy engine.
