# L1-I — Evidence Sufficiency and Current Reliance Model

## Purpose

Define how independent Validation judges whether Evidence is sufficient for an exact Validation Requirement while preserving provider-owned evidence, immutable historical records, and explicit current-reliance changes.

## Evidence sufficiency is subordinate

Evidence sufficiency is a subordinate assessment within the Validation Requirement / Validation judgment. L1-I does **not** introduce an Evidence Set A1/A2 entity.

A conforming sufficiency assessment considers, as applicable:

- Proof-criterion coverage;
- exact scope/revision relationship;
- source authority;
- provenance/integrity;
- currentness/effectivity;
- required independence characteristics;
- completeness;
- contradictory or negative Evidence;
- environmental relevance;
- retrievability/reproducibility where required;
- known gaps/limitations.

The result must be reconstructable from the Validation Record and referenced Evidence Records / external provider resources.

## Evidence may remain external

Evidence Record [A2] is canonical Evidence identity/provenance, not necessarily the bytes themselves. CI/test reports, source-control state, telemetry, evaluation outputs, security results, inspection artifacts, and other Evidence may remain physically authoritative in provider systems when references preserve the required identity, provenance, integrity, scope, and currentness.

Do not copy Evidence merely to make AE appear self-contained if doing so creates a shadow source of truth.

## Executor-produced Evidence

Execution/Verification may produce Evidence. Independent Validation may reuse that Evidence without rerunning every test.

The boundary is:

> Contract Proof defines the required evidence. Planning derives the Verification/Test Strategy. Execution creates or references evidence. Independent Validation judges the result.

Green tests, CI success, provider `Done`, static analysis, security results, or executor summaries do not become Validation acceptance merely because they are favorable.

## Contradictory and negative Evidence

Material contradictory or negative Evidence within the applicable scope may not be silently ignored. The Validator must reconcile, qualify, or explicitly disposition it. Unresolved material contradiction prevents a clean `PROOF_SATISFIED` judgment.

## Currentness and exact revisions

Evidence must satisfy the Validation Requirement's exact/effective revision and currentness semantics. Newest is not automatically correct. Evidence for the wrong Contract, Plan, Baseline, architecture state, resource, environment, or scope cannot satisfy an exact requirement merely because it is recent.

If authoritative Evidence/current state cannot be resolved sufficiently, acceptance must not occur.

## Historical immutability versus current reliance

Evidence Record and Validation Record history is non-destructive.

If Evidence is later discovered to be stale, invalid, incomplete, tampered, superseded, or otherwise unreliable:

1. do not rewrite the historical Evidence Record;
2. do not rewrite the historical Validation Record;
3. preserve what Evidence existed and what judgment was issued at that time;
4. create later finding/Evidence/Validation/decision state as appropriate;
5. update current-reliance semantics explicitly;
6. revalidate or escalate affected current work when required by scope, policy, or risk.

## Current reliance [B]

Current reliance is subordinate state describing whether an Evidence Record or prior Validation judgment is currently usable for a declared scope.

Suggested semantic results:

- `RELIABLE` — currently usable for the declared requirement/scope;
- `QUALIFIED` — usable only with explicit limitations/conditions;
- `UNRELIABLE` — must not be relied upon for the declared requirement/scope;
- `UNKNOWN` — current reliability cannot be established.

Current reliance is scope-sensitive and does not mutate historical issuance.

For protected acceptance, `UNKNOWN` or `UNRELIABLE` material Evidence cannot be treated as sufficient.

## Parallel Evidence aggregation

Parallel work may produce multiple Evidence Records/provider references. Aggregation/reconciliation must preserve:

- originating scope;
- exact revisions;
- producer/source provenance;
- relationship to Proof criteria;
- contradictions/limitations;
- integrity/currentness;
- any applicable independence characteristics.

An aggregate view is subordinate/derived and does not replace underlying authoritative Evidence identities.

## Context Package boundary

A Context Package is not Evidence merely because a Validator consumed it. Material Evidence/source references must remain independently resolvable. A Context Assembly Receipt is retained only when consequential use/policy requires it and assembled context materially influenced the judgment beyond directly referenced canonical inputs.
