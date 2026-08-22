# ADR-003 — Use conforming JSON capability definitions with Python capability-integrity CI

**Status:** Adopted  
**Decision Date:** 2026-08-22  
**Decision Authority:** Human Owner  
**Scope:** This repository / Part 1 reference layer. JSON, Python, and GitHub Actions are not Canonical AE technology requirements.

## Context

ADR-002 established staged machine authority for lifecycle semantics. L1-E now has enough stable capability, binding, readiness, OEB, and Proof semantics for machine-verifiable portability/adoption tests.

## Decision

Stage 1:

- Human semantic L1-E artifacts are normative for meaning.
- `capability_contracts.json` is a conforming machine representation of the ten capability/operation definitions.
- `capability_scenarios.json` contains provider/binding/runtime scenarios.
- `oeb_fixtures.json` contains OEB/Product specialization scenarios.
- `validate_capabilities.py` validates structural and semantic invariants.
- `.github/workflows/capability-integrity.yml` runs the repository check on PRs/pushes to `main`.

The representation uses synthetic provider shapes rather than importing a real vendor object model as hidden canonical semantics.

## Minimum executable invariants

The validator demonstrates, among other things:

- exactly ten capability IDs;
- unique operations with requirement/access/proof metadata;
- Work Management minimum operation set;
- two materially different provider shapes satisfying the same Work Management Contract;
- missing operation failure;
- Human-UI-only mechanical intermediary failure;
- broad-admin-only entitleability failure;
- runtime OA denial leaving healthy binding Proof intact;
- unauthorized PEP denial;
- ambiguous binding rejection;
- transient provider outage causing runtime BLOCK without rewriting installation Proof;
- artifact association without binary-upload requirement;
- heterogeneous access paths;
- atomic execution without meaningless cancel requirement;
- mediated Identity & Access without raw agent secrets;
- Knowledge write cannot bypass authoritative ownership;
- explicit deterministic binding composition;
- safe sandbox Proof;
- OEB Product/System specialization and no silent weakening;
- newer OEB revision does not silently rebase active work.

## Authority staging

The machine representation is not the sole source of Canonical AE meaning. Promotion to normative structural authority requires a later explicit decision and evidence that Human/machine semantic parity can be controlled.

## Repository governance

`capability-integrity` is operational CI. Repository protection must not be claimed until branch rules actually require the applicable integrity jobs. Issue #12 tracks that gap.

## Traceability

ADR-002; Contract machine-verifiable integrity Proof; DR-114–116; Human Owner L1-E D20.
