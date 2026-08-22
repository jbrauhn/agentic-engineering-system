# ADR-006 — Machine-readable Planning / Execution Protocol and Integrity Check

**Status:** Adopted  
**Date:** 2026-08-22

## Context

L1-H now defines enough structural Planning/Execution semantics to test rolling-wave review, readiness, dependencies/barriers, adaptation routing, evidence boundaries, worker promotion, and recovery without requiring a production orchestrator.

## Decision

For this repository's Stage-1 executable/reference layer:

- Human L1-H semantic artifacts remain normative for meaning;
- `planning_execution_protocol.json` is a conforming machine-readable structural representation;
- `planning_execution_scenarios.json` provides valid/invalid semantic fixtures;
- `planning_execution_portability_fixtures.json` compares materially different Planning/Execution architectures;
- `validate_planning_execution.py` is a repository/reference validator;
- `.github/workflows/planning-execution-integrity.yml` runs the `planning-execution-integrity` job on PR/push to `main`.

The validator cross-checks existing L1-D lifecycle, L1-E capability, L1-F authority, and L1-G context machine definitions rather than redefining those semantics locally.

JSON, Python, and GitHub Actions are repository implementation choices, not Canonical AE technology requirements.

## Consequences

The executable layer can prove semantic portability and detect stale review inheritance, unsafe parallelism, invalid adaptation routing, self-Validation, hidden orchestrator state, and other L1-H failures. It does not become a canonical planner, workflow engine, scheduler, or orchestration runtime.

Repository issue #12 tracks whether this and other integrity jobs become actually required by branch protection/rulesets; a successful run alone is not enforcement.
