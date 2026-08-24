# Canonical Agentic Engineering System

**Part 1 status:** Human Owner accepted  
**Current release representation:** distribution revision 4 · `HUMAN_OWNER_ACCEPTED`

Canonical Agentic Engineering (AE) is a portable, governed socio-technical engineering system for Human–AI engineering. It defines how engineering intent moves through an approved Contract, architecture-aware Planning, bounded Execution, Evidence, independent Validation, and Learning while preserving durable state, explicit authority, and technology portability.

This repository contains the **Canonical AE System definition and its executable/reference proof layer**. It is not an AI coding tool, a required Portal, a required agent runtime, or a vendor-specific implementation.

## Start here

If you are new to the project, do **not** work through the repository alphabetically.

1. **[START_HERE.md](START_HERE.md)** — orientation, authority, adoption path, and first actions.
2. **[canonical_ae_release_manifest.json](canonical_ae_release_manifest.json)** — exact release identity, status, authority layers, and distribution selectors.
3. **[canonical/CONTRACT.md](canonical/CONTRACT.md)** — governing Goal / Spec / Proof for Part 1.
4. **[docs/SYSTEM_RATIONALE.md](docs/SYSTEM_RATIONALE.md)** — concise explanation of how the system fits together and why major decisions were made.
5. **[adoption/ADOPTION_STARTER_PACK.md](adoption/ADOPTION_STARTER_PACK.md)** — derive an organization-specific implementation Plan from the Canonical system.
6. **[Repository Map](docs/REPOSITORY_MAP.md)** — what the file families mean and where to look for a specific concern.

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
| **Canonical Core** | Normative system semantics | `canonical/CONTRACT.md`, `canonical/l1/*/L1-*.md`, `canonical/decisions/dr/DR-*.md`, `Acanonical/decisions/dr/DR-*.md` |
| **Adoption Starter Pack** | Conforming implementation guidance | `START_HERE.md`, `adoption/ADOPTION_STARTER_PACK.md` |
| **Executable Reference Layer** | Replaceable executable proof/reference implementation | `reference/protocols/*_protocol.json`, validators, fixtures, reference loops, integrity workflows |
| **Supporting explanatory/governance content** | Rationale and durable acceptance state | `docs/SYSTEM_RATIONALE.md`, Part 1 Authority Decision |

Lower layers cannot override higher Canonical authority.

## Current accepted release

The current repository representation of accepted Part 1 is based on:

- canonical source finalization: `main@2e144d21535f8bf838f9a6c064ebd967f8b491ce`;
- release status: `HUMAN_OWNER_ACCEPTED`;
- distribution revision: `4`;
- current distribution contents: `174` artifacts;
- Proof A–O: complete, including clean-room adoption, independent whole-system review, and Human Owner acceptance.

The historical release ID/version retain their candidate-era labels. Current acceptance is established by the release manifest plus the durable Human Owner Authority Decision record.

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

## Repository organization note

The live revision-4 representation organizes Canonical, adoption, reference, tooling, and explanatory material into dedicated directories. Historical revision 3 preserves the accepted flat-path representation and exact payload hash. The reorganization changes navigation/path representation only; it does not redefine Canonical architecture or Part 1 semantics.

## Repository governance follow-on

The repository has nine machine-verifiable integrity suites. GitHub issue **#12** remains open until actual branch/ruleset enforcement is configured and an intentionally failing applicable check is proven to block merge. Until then, the checks should not be described as repository-enforced merge gates.

---

For authoritative release state, start with **[canonical_ae_release_manifest.json](canonical_ae_release_manifest.json)**. For a human introduction, start with **[START_HERE.md](START_HERE.md)**.