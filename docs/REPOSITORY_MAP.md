# Repository Map

This page is a human/agent navigation aid for the Canonical Agentic Engineering repository. It does **not** redefine release authority or Canonical semantics. The release manifest remains authoritative for distribution membership and layer classification.

## Fast paths

### I want to understand AE

Read in this order:

1. [`../START_HERE.md`](../START_HERE.md)
2. [`../SYSTEM_RATIONALE.md`](../SYSTEM_RATIONALE.md)
3. [`../CONTRACT.md`](../CONTRACT.md)
4. the applicable `L1-*.md` semantic artifacts
5. supporting `DR-*.md` and `ADR-*.md` records when you need the decision history or machine-reference rationale.

### I want to adopt AE in an organization

1. [`../canonical_ae_release_manifest.json`](../canonical_ae_release_manifest.json)
2. [`../START_HERE.md`](../START_HERE.md)
3. [`../ADOPTION_STARTER_PACK.md`](../ADOPTION_STARTER_PACK.md)
4. Canonical capability definitions and applicable L1 semantics
5. reference fixtures/validators only as conforming examples, never as hidden Canonical requirements.

### I want to review or change the Canonical system

1. [`../CONTRACT.md`](../CONTRACT.md)
2. exact current release manifest
3. affected `L1-*.md` artifacts
4. relevant `DR-*.md` / `ADR-*.md`
5. affected machine-readable protocol/scenario files and integrity validators
6. applicable GitHub Actions integrity workflow.

## File families

### Governing Contract

- `CONTRACT.md`

Part 1 Goal / Spec / Proof and the governing acceptance boundary.

### L1 semantic artifacts

- `L1-A_*` through `L1-L_*`

Human-readable Canonical semantics. The L1 letters are design domains, not runtime stages.

Broad topic map:

| L1 | Topic |
|---|---|
| A | identity, scope, system boundaries |
| B | logical responsibility architecture |
| C | domain and artifact model |
| D | lifecycle and state protocol |
| E | capability contracts and organization engineering baseline |
| F | authority, policy, and enforcement |
| G | knowledge, context, memory, handoff, reconstruction |
| H | Planning, progressive elaboration, Execution readiness |
| I | Evidence and independent Validation |
| J | standards applicability and Engineering Health |
| K | observability, metrics, experiments, and Learning |
| L | adoption, distribution, conformance, bootstrap, interface parity |

### Decision Records

- `DR-*.md`

Durable Canonical design decisions and rationale. Read these when you need to understand why a semantic choice exists or what decision superseded an earlier assumption.

### Architecture Decision Records

- `ADR-*.md`

Decisions about machine-readable/reference architecture and executable integrity mechanisms. ADRs do not make the selected implementation technology Canonical.

### Release and adoption entry points

- `canonical_ae_release_manifest.json` — exact release identity, authority layers, selectors, status, and acceptance references.
- `START_HERE.md` — discoverability and adoption orientation.
- `ADOPTION_STARTER_PACK.md` — reusable conforming implementation guidance.
- `SYSTEM_RATIONALE.md` — explanatory current-state and evolution summary.
- `part1_acceptance_authority_decision_20260824.json` — durable Human Owner Part 1 acceptance record.

### Machine-readable Canonical/reference models

Common families include:

- `*_protocol.json`
- `*_scenarios.json`
- `*_portability_fixtures.json`
- `capability_contracts.json`
- `synthetic_organization_fixture.json`
- `reference_ae_loops.json`

These provide machine-readable semantics, fixtures, and reference behavior according to their manifest role. Reference artifacts cannot override the Canonical Core.

### Validators and harnesses

- `validate_*.py`
- `run_clean_room_adoption.py`
- `assemble_distribution.py`

These exercise integrity, portability, adoption, and distribution behavior. Passing a script does not independently create Human acceptance or organization conformance.

### CI integrity suites

- `.github/workflows/*-integrity.yml`

Nine integrity domains currently exist:

1. lifecycle
2. capability
3. authority
4. context
5. Planning / Execution
6. Validation
7. standards / Engineering Health
8. observability / Learning
9. adoption

Issue #12 tracks actual repository merge-gate enforcement. The workflows exist and function; they are not yet proven as branch-protection-enforced gates.

## Authority versus convenience

The repository contains different kinds of material side by side. Do not infer authority from:

- file extension;
- alphabetical order;
- proximity in the root listing;
- whether something is machine readable;
- whether a workflow is green;
- whether a generated view is easier to read.

Use the release manifest, Contract, artifact status, and decision precedence.

## Why the accepted Part 1 root is still flat

Part 1 was developed with root-level artifact names that became part of the accepted release representation and SHA-256 inventory. Moving those files now would alter artifact paths and require updates to:

- release selectors;
- inventory/path identity;
- internal references and links;
- workflow path filters;
- executable validators or harness assumptions where applicable;
- current release representation/reassessment evidence.

For that reason, the first repository-hygiene step is a better navigation layer rather than duplicate files or silent path changes.

## Recommended future physical layout

If a controlled non-semantic repository/distribution representation revision is authorized, the target shape should be closer to:

```text
/
├── README.md
├── canonical/
│   ├── CONTRACT.md
│   ├── l1/
│   ├── decisions/
│   │   ├── dr/
│   │   └── adr/
│   └── release/
├── adoption/
│   ├── START_HERE.md
│   └── ADOPTION_STARTER_PACK.md
├── reference/
│   ├── protocols/
│   ├── fixtures/
│   ├── loops/
│   └── validators/
├── tools/
│   ├── assemble_distribution.py
│   └── clean-room/
├── docs/
│   └── explanatory material
└── .github/
    └── workflows/
```

That structure is a repository organization proposal, **not** a new Canonical architecture. A future refactor should preserve semantic identity/history, update the manifest and references deterministically, rerun applicable integrity suites, and publish the resulting representation revision explicitly.
