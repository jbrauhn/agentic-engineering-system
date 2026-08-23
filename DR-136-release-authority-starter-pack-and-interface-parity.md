# DR-136 — Release authority, Starter Pack, and interface parity

**Status:** Adopted

## Decision

Adopt a release/distribution model centered on the existing Canonical AE Release Manifest `[F]`. The Manifest identifies exact release/version, semantic layer membership, authority class, provenance/integrity and evolution information. Core is normative; Starter Pack and Reference Layer conform to Core and cannot redefine it. Reference packaging may use SHA-256/GitHub/Python, but no repository/package/signing technology is Canonical.

Adopt a minimal discoverable Starter Pack using existing canonical identities. Reuse L1-G Bootstrap Descriptor/Context Requirements for environment-neutral discovery. Canonical requirement is interface parity: each supported Human/agent environment can resolve equivalent governing state and required operations through governed Access Paths. Environment uniformity and an Environment Profile entity are rejected.

Passing materially different environment portability Proof resolves the broad Canonical question captured in issue #6; future UX mechanics remain organization/product choices.

## Consequences

- No new L1-L A1/A2 type is introduced.
- Existing Contract/L1 semantics remain authoritative.
- Technology-specific packaging and UX mechanisms remain replaceable.
