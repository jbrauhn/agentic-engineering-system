# Canonical AE System — About / System Rationale

## Why this system exists

Agentic Engineering aims to obtain substantial leverage from capable AI agents without turning delegation into abdication. The system therefore joins fast machine execution with explicit Human intent/Decision Authority, durable system-owned knowledge, bounded Operational Authority, architecture-aware Planning, Evidence, and independent Validation.

## Major design ideas

- **Contract = Goal / Spec / Proof.** Intent and success criteria are governed before execution.
- **The doer shall not become its own judge.** Work-producing and acceptance-judgment paths are independent.
- **Access ≠ authority.** Technical entitlement, Operational Authority and Decision Authority remain distinct.
- **Memory belongs to the system, not a conversation.** Fresh/replacement actors reconstruct from durable canonical state.
- **Canonical operations, organization bindings.** Providers are replaceable without redefining AE.
- **Interface parity, not environment uniformity.** Different developer/agent environments can expose equivalent governed semantics.
- **Engineering health is contextual.** Frameworks inform diagnosis; underlying conditions matter more than checklist theater.
- **Measurements are neutral observations.** Experiments and Learning inform governed decisions rather than self-modifying the system.
- **Portability by layering.** Canonical AE → OEB/Product context → organization-specific implementation.

## Current Part 1 state

Part 1 has been accepted by the Human Owner against the exact revision-2 acceptance basis recorded in `canonical/governance/part1_acceptance_authority_decision_20260824.json`.

Later distribution revisions preserve that acceptance history rather than silently rebasing it:

- revision 3 recorded the accepted release-facing state;
- revision 4 reorganized repository/distribution paths for human and agent navigation;
- revision 5 hardens the GitHub executable/reference implementation so all nine integrity workflows are consistently present on pull requests and rerun on pushes to `main`.

Revisions 3–5 do not change Canonical Core semantics or replace the exact Human-accepted revision-2 basis. The historical release ID/version retain their candidate-era labels for continuity. Current release status is determined by the Canonical AE Release Manifest together with the Human Owner Authority Decision record.

## Evolution

The accepted Part 1 system evolved through approved L1 domains:

- L1-A identity/boundaries;
- L1-B logical responsibility architecture;
- L1-C domain/artifact model;
- L1-D lifecycle/state;
- L1-E capabilities/OEB;
- L1-F authority/policy/enforcement;
- L1-G context/memory;
- L1-H Planning/Execution;
- L1-I Validation/Evidence;
- L1-J standards/engineering health;
- L1-K observability/experiments/learning;
- L1-L adoption/distribution/conformance assembly.

The broad Canonical interface-parity question tracked by issue #6 was resolved by L1-L/DR-136 and the reference portability Proof. Older L1-C/L1-D historical text may still describe issue #6 as open because that was true when those baselines were issued; that historical wording is not current status and is not rewritten destructively.

## Detailed authority

This page is a Human-readable rationale/navigation view. `canonical/CONTRACT.md`, Decision Records, ADRs, Human semantic L1 artifacts, and applicable durable Authority Decision records remain the detailed authoritative sources. If this page conflicts with them, this page is wrong.

## Open experiments and follow-ons

Previously recorded experiments such as governed AE vs lighter baselines, model placement, and ASD-STE100 remain experiments rather than predetermined conclusions.

A 2026-08-24 repository audit found that some inherited experiment/decision history is referenced but not yet discoverable in the repository: accepted L1-K material names DR-102, DR-103, and DR-104 as open experiments, while those exact records are absent. Issue #2 now tracks recovery/reconciliation of the historical Decision Register and Experiments / Results Ledger. Missing records must not be reconstructed from memory or inference.

Repository required-check enforcement remains a separate follow-on tracked by issue #12. Revision 5 makes the nine GitHub check jobs consistently available on PRs and `main` pushes, but GitHub branch/ruleset protection must still require them and a failing-check merge-block test must still be demonstrated before enforcement can be claimed.
