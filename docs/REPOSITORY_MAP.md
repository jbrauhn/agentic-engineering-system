# Repository Map

**Current distribution representation:** revision 5. Revision 4 introduced the organized path layout; revision 3 preserves the prior flat-root representation.

This page is a human/agent navigation aid for the Canonical Agentic Engineering repository. It does **not** redefine release authority or Canonical semantics. The **[release manifest](../canonical_ae_release_manifest.json)** remains authoritative for distribution membership and layer classification.

## Fast paths

### I want to understand AE

Read in this order:

1. **[START HERE](../START_HERE.md)**
2. **[System Rationale](SYSTEM_RATIONALE.md)**
3. **[Contract](../canonical/CONTRACT.md)**
4. **[Level 1 Canonical domains](../canonical/level-1/)**
5. **[Decision Records](../canonical/decisions/dr/)** and **[Architecture Decision Records](../canonical/decisions/adr/)** when you need decision history or machine-reference rationale.

### I want to adopt AE in an organization

1. **[Release manifest](../canonical_ae_release_manifest.json)**
2. **[START HERE](../START_HERE.md)**
3. **[Adoption Starter Pack](../adoption/ADOPTION_STARTER_PACK.md)**
4. **[Level 1 capabilities/OEB domain](../canonical/level-1/E/)** and the other applicable Level 1 domains
5. **[Reference layer](../reference/)** only as conforming examples and executable proof, never as hidden Canonical requirements.

### I want to review or change the Canonical system

1. **[Contract](../canonical/CONTRACT.md)**
2. **[Exact current release manifest](../canonical_ae_release_manifest.json)**
3. affected **[Level 1 domains](../canonical/level-1/)**
4. relevant **[Decision Records](../canonical/decisions/dr/)** / **[ADRs](../canonical/decisions/adr/)**
5. affected **[protocols](../reference/protocols/)**, **[scenarios](../reference/scenarios/)**, and **[validators](../reference/validators/)**
6. applicable **[integrity workflow](../.github/workflows/)**.
7. **[Repository contribution rules](../.github/CONTRIBUTING.md)** for branch, PR, Evidence, Validation, release-impact, and cleanup expectations.

## File families

### Governing Contract

- **[canonical/CONTRACT.md](../canonical/CONTRACT.md)**

Part 1 Goal / Spec / Proof and the governing acceptance boundary.

### Level 1 Canonical semantic domains

- **[canonical/level-1/](../canonical/level-1/)** contains `L1-A_*` through `L1-L_*`.

**“L1” means Level 1.** The letters A–L are semantic design domains. They are **not Contract clause numbers** and they are **not sequential runtime stages**. This directory has the largest hierarchy because the Level 1 artifacts contain the detailed human-readable Canonical system semantics beneath the governing Contract.

| Level 1 domain | Topic |
|---|---|
| **[A](../canonical/level-1/A/)** | identity, scope, system boundaries |
| **[B](../canonical/level-1/B/)** | logical responsibility architecture |
| **[C](../canonical/level-1/C/)** | domain and artifact model |
| **[D](../canonical/level-1/D/)** | lifecycle and state protocol |
| **[E](../canonical/level-1/E/)** | capability contracts and organization engineering baseline |
| **[F](../canonical/level-1/F/)** | authority, policy, and enforcement |
| **[G](../canonical/level-1/G/)** | knowledge, context, memory, handoff, reconstruction |
| **[H](../canonical/level-1/H/)** | Planning, progressive elaboration, Execution readiness |
| **[I](../canonical/level-1/I/)** | Evidence and independent Validation |
| **[J](../canonical/level-1/J/)** | standards applicability and Engineering Health |
| **[K](../canonical/level-1/K/)** | observability, metrics, experiments, and Learning |
| **[L](../canonical/level-1/L/)** | adoption, distribution, conformance, bootstrap, interface parity |

### Decision Records

- **[canonical/decisions/dr/](../canonical/decisions/dr/)**

Durable Canonical design decisions and rationale. Read these when you need to understand why a semantic choice exists or what decision superseded an earlier assumption.

**Known evolution-traceability debt:** issue #2 tracks missing consolidated Decision Register / Experiments ledger coverage and inherited references such as DR-102/103/104 that are named by accepted artifacts but not yet recoverable from this repository. Do not invent those records from memory.

### Architecture Decision Records

- **[canonical/decisions/adr/](../canonical/decisions/adr/)**

Decisions about machine-readable/reference architecture and executable integrity mechanisms. ADRs do not make the selected implementation technology Canonical.

### Release and adoption entry points

- **[Release manifest](../canonical_ae_release_manifest.json)** — exact release identity, authority layers, selectors, status, and acceptance references.
- **[START HERE](../START_HERE.md)** — discoverability and adoption orientation.
- **[Adoption Starter Pack](../adoption/ADOPTION_STARTER_PACK.md)** — reusable conforming implementation guidance.
- **[System Rationale](SYSTEM_RATIONALE.md)** — explanatory current-state and evolution summary.
- **[Part 1 Acceptance Authority Decision](../canonical/governance/part1_acceptance_authority_decision_20260824.json)** — durable Human Owner Part 1 acceptance record.

### Machine-readable reference models

- **[Protocols](../reference/protocols/)**
- **[Scenarios](../reference/scenarios/)**
- **[Fixtures](../reference/fixtures/)**
- **[Reference loops](../reference/loops/)**

These provide machine-readable semantics, fixtures, and reference behavior according to their manifest role. Reference artifacts cannot override the Canonical Core.

### Validators and harnesses

- **[Validators](../reference/validators/)**
- **[Clean-room adoption harness](../tools/clean-room/run_clean_room_adoption.py)**
- **[Distribution assembler](../tools/assemble_distribution.py)**

These exercise integrity, portability, adoption, and distribution behavior. Passing a script does not independently create Human acceptance or organization conformance.

### CI integrity suites

- **[.github/workflows/](../.github/workflows/)**

Nine integrity domains currently exist: lifecycle; capability; authority; context; Planning/Execution; Validation; standards/Engineering Health; observability/Learning; and adoption.

Revision 5 configures all nine to run on every pull request and every push to `main`, giving a stable check set for repository protection and a post-push detection backstop. Issue #12 remains open until GitHub actually enforces those checks before merge and a failing-check block test is demonstrated.

## Authority versus convenience

Do not infer authority from file extension, folder depth, alphabetical order, machine readability, a green workflow, or whether a generated view is easier to read. Use the release manifest, Contract, artifact status, and decision precedence.

## Representation history

- **Revision 2:** exact Human-accepted basis.
- **Revision 3:** acceptance finalization / release-facing representation.
- **Revision 4:** path reorganization for human/agent navigation; Contract/L1/DR/ADR content remained byte-identical.
- **Revision 5:** repository/executable-reference hardening so all nine integrity suites are consistently present on PRs and rerun on `main` pushes; no Canonical Core semantic change.

## Current physical layout

```text
/
├── README.md
├── LICENSE
├── START_HERE.md
├── canonical_ae_release_manifest.json
├── canonical/
│   ├── CONTRACT.md
│   ├── level-1/
│   │   ├── A/
│   │   ├── B/
│   │   └── ... L/
│   ├── decisions/
│   │   ├── dr/
│   │   └── adr/
│   └── governance/
├── adoption/
│   └── ADOPTION_STARTER_PACK.md
├── reference/
│   ├── protocols/
│   ├── scenarios/
│   ├── fixtures/
│   ├── loops/
│   └── validators/
├── tools/
│   ├── assemble_distribution.py
│   └── clean-room/
├── docs/
└── .github/
    ├── CONTRIBUTING.md
    ├── pull_request_template.md
    └── workflows/
```

This is **repository/distribution organization**, not a new Canonical runtime architecture.
