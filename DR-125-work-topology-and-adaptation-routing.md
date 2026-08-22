# DR-125 — Work Topology and Adaptation Routing

**Status:** Adopted  
**Date:** 2026-08-22

## Decision

Canonical AE defines provider-neutral work-topology semantics for dependencies, barriers, independent branches, shared-resource conflicts, reconciliation points, scope-specific authority/capability/context boundaries, and evidence aggregation. It does not require a DAG engine, scheduler, queue, swarm, branch strategy, or central orchestrator.

Independent ready scopes may execute concurrently. Blocking propagates only through meaningful declared dependencies/barriers/conflicts or another condition making continuation invalid or unsafe.

Execution routing uses the following semantic distinction:

- adjustment inside reviewed Plan boundaries → local adaptation;
- execution failure while reviewed route remains valid → Retry;
- material reviewed-route change with Contract still valid → Replan;
- Goal/Spec/Proof or other Contract-level change → Contract Change Proposal;
- unresolved authority/risk/decision issue → Escalate.

## Rationale

This allows high-concurrency agentic work without losing review boundaries or turning AE into a workflow engine.

## Consequences

- local adaptation is not a hidden Plan edit;
- Replan creates a new Plan revision and applicable review;
- Contract change still uses G5/Human Decision Authority;
- a blocked branch does not freeze unrelated valid work;
- shared dependency/resource conflicts can prevent unsafe parallel continuation;
- workers may signal deficiencies but may not rewrite Plan/Contract authority.
