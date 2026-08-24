# Canonical Agentic Engineering System

**Part 1 status:** Human Owner accepted  
**Current release representation:** distribution revision 5 · `HUMAN_OWNER_ACCEPTED`

Canonical Agentic Engineering (AE) is a portable, governed socio-technical engineering system for Human–AI engineering. It defines how engineering intent moves through an approved Contract, architecture-aware Planning, bounded Execution, Evidence, independent Validation, and Learning while preserving durable state, explicit authority, and technology portability.

This repository contains the **Canonical AE System definition and its executable/reference proof layer**. It is not an AI coding tool, a required Portal, a required agent runtime, or a vendor-specific implementation.

## Start here

If you are new to the project, do **not** work through the repository alphabetically.

1. **[START_HERE.md](START_HERE.md)** — orientation, authority, adoption path, and linked first actions.
2. **[canonical_ae_release_manifest.json](canonical_ae_release_manifest.json)** — exact release identity, status, authority layers, and distribution selectors.
3. **[canonical/CONTRACT.md](canonical/CONTRACT.md)** — governing Goal / Spec / Proof for Part 1.
4. **[canonical/level-1/](canonical/level-1/)** — detailed Canonical semantic domains L1-A through L1-L.
5. **[docs/SYSTEM_RATIONALE.md](docs/SYSTEM_RATIONALE.md)** — concise explanation of how the system fits together and why major decisions were made.
6. **[adoption/ADOPTION_STARTER_PACK.md](adoption/ADOPTION_STARTER_PACK.md)** — derive an organization-specific implementation Plan from the Canonical system.
7. **[Repository Map](docs/REPOSITORY_MAP.md)** — what the file families mean and where to look for a specific concern.

## What Part 1 defines

The accepted Canonical system covers:

- system identity, boundaries, and technology neutrality;
- logical responsibility architecture (`R1`–`R7`);
- durable domain/artifact semantics;
- lifecycle, gates, backward routes, and revision effectivity;
- ten Canonical capability categories and organization-specific bindings;
- identity, entitlement, Operational Authority, Decision Authority, policy, and enforcement;
- durable knowledge, context, memory, handoff, and reconstruction;
- architecture-aware Planning and bounded Execution;
- Evidence and independent Validation;
- standards applicability and Engineering Health Findings;
- observability, experiments, metrics, Learning, and governed feedback;
- adoption, clean-room discoverability, interface parity, conformance, and release integrity.

## Canonical lifecycle

```text
Work arrives
    ↓
Loop Context
    ↓
Contract — Goal / Spec / Proof
    ↓
Architecture-aware Planning
    ↓
Plan Review
    ↓
Bounded Execution → Evidence
    ↓
Independent Validation
    ↓
Accept / Retry Execution / Replan / Propose Contract Change / Escalate
    ↓
Learning / durable state
```

The work-producing path may verify its own work, but it may not issue its own Validation acceptance.

## Repository authority layers

The exact release manifest controls distribution membership and authority classification. In simplified form:

| Layer | Purpose | Typical files |
|---|---|---|
| **Canonical Core** | Normative system semantics | [Contract](canonical/CONTRACT.md), [Level 1 domains](canonical/level-1/), [Decision Records](canonical/decisions/dr/), [ADRs](canonical/decisions/adr/) |
| **Adoption Starter Pack** | Conforming implementation guidance | [START HERE](START_HERE.md), [Adoption Starter Pack](adoption/ADOPTION_STARTER_PACK.md) |
| **Executable Reference Layer** | Replaceable executable proof/reference implementation | [protocols](reference/protocols/), [validators](reference/validators/), [fixtures](reference/fixtures/), [reference loops](reference/loops/), [integrity workflows](.github/workflows/) |
| **Supporting explanatory/governance content** | Rationale and durable acceptance state | [System Rationale](docs/SYSTEM_RATIONALE.md), [Part 1 Authority Decision](canonical/governance/part1_acceptance_authority_decision_20260824.json) |

Lower layers cannot override higher Canonical authority.

## Accepted release lineage

Part 1 acceptance and later repository representations are deliberately distinct:

- **Human-accepted basis:** `main@6c2424d5aea415819b276dfc6988aa9f964c6e62`, distribution revision `2`, transport SHA-256 `24131b15f6e960afa5463418bbf99c321c68eae01606aadd44e5dbb9df46887e`.
- **Acceptance finalization:** distribution revision `3`, represented by merge `2e144d21535f8bf838f9a6c064ebd967f8b491ce`; this recorded the already-issued Human Owner acceptance without changing Canonical Core semantics.
- **Repository organization:** distribution revision `4`, introduced by merge `214585801cf66e0d7bb2c1713143f273a16115ad`; this reorganized paths for human/agent navigation without changing Contract/L1/DR/ADR content.
- **Repository hardening:** distribution revision `5`; this standardizes all nine integrity workflows so they are present on every pull request and rerun on every push to `main`. It does not change Canonical Core semantics or the accepted revision-2 basis.

The historical release ID/version retain their candidate-era labels. Acceptance is established by the [release manifest](canonical_ae_release_manifest.json) plus the durable [Human Owner Authority Decision](canonical/governance/part1_acceptance_authority_decision_20260824.json), not by README prose.

## Adoption boundary

A Canonical AE release is **not** the same thing as an organization-specific AE implementation.

An adopter supplies its own organization/product baseline, maps all required Canonical capabilities to real providers and access paths, establishes authority/policy/enforcement, resolves bootstrap/context, implements gaps, produces Evidence, and obtains independent adoption Validation. An organization implementation begins **Candidate** and becomes Conforming only through applicable Validation.

## Technology and product boundary

Canonical AE deliberately does **not** require:

- GitHub, GitLab, Jira, or any particular provider;
- one model vendor;
- one agent framework;
- one Portal, CLI, IDE, Dev Container, or runtime;
- one central AE database;
- one policy engine or authorization DSL.

A future Portal can be a separate product that consumes or is engineered through AE. It is not part of the Canonical system and is not required for AE to operate.

## Repository organization

The live representation organizes Canonical, adoption, reference, tooling, and explanatory material into dedicated directories. **`level-1/` means Level 1**; its A–L folders are semantic domains, not Contract clause numbers or runtime stages. See the [Repository Map](docs/REPOSITORY_MAP.md).

## Repository governance

Repository implementation follows branch → pull request → integrity checks → review → merge. The intended process and cleanup rules are documented in **[CONTRIBUTING.md](.github/CONTRIBUTING.md)**.

All nine integrity workflows are configured to run on every pull request and on every push to `main`. GitHub issue **#12** remains open until `main` branch/ruleset protection actually requires those checks and an intentionally failing check is demonstrated to block merge. Until then, the checks are functioning evidence and a detection backstop, but not yet repository-enforced merge gates.

---

For authoritative release state, start with **[canonical_ae_release_manifest.json](canonical_ae_release_manifest.json)**. For a human introduction, start with **[START_HERE.md](START_HERE.md)**.
