# DR-126 — Execution Evidence, Worker Results, Recovery, and Federated State

**Status:** Adopted  
**Date:** 2026-08-22

## Decision

Contract Proof defines required evidence; Planning derives the Verification/Test Strategy; Execution creates or references Evidence; independent Validation judges the result. Execution/test/CI success does not create Validation acceptance.

Worker/subagent context is bounded through L1-G Context Requirements and exact governing anchors. Worker returns remain subordinate execution/result semantics by default and preserve result, evidence/provenance, blockers, dependency/resource conflicts, architecture issues, Plan/Contract deficiency signals, and material promotion needs.

No new Execution Attempt, Worker Result, Execution Topology, Adaptation Record, or Verification Result A1/A2 type is introduced without a future DR-108 admission decision.

Material Planning/Execution state is federated under DR-107 and must survive orchestrator/session loss. Queues, scheduler graphs, Context Packages, worker sessions, and provider workflow projections cannot be the only source of material state.

## Rationale

This preserves the maker/checker boundary, prevents execution-local shadow truth, and permits fresh or continuing workers and materially different orchestration architectures.

## Consequences

- L4 micro-plans remain ephemeral; material discoveries are promoted to proper durable owners;
- parallel evidence is reconciled for Validation readiness;
- architecture-impacting discoveries route to ADR/Replan/Contract Change as applicable;
- Product/System Baseline is not silently mutated mid-execution;
- Human judgment remains valid collaboration while clerical Human proxying reveals capability/access-path deficiency;
- recovery from orchestration/session loss is a conformance property.
