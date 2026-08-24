# L1-H — Worker Context, Result, Promotion, and Recovery Model

## 1. Worker context

A delegated worker/subagent receives bounded task-specific context through L1-G semantics rather than an accidental full transcript dump.

Worker context makes resolvable, as applicable:

- exact/effective Contract;
- exact reviewed Plan revision and scope;
- L2/L3 work scope;
- relevant Product/System Baseline and architecture neighborhood;
- dependencies/barriers/shared-resource constraints;
- applicable authority/capability requirements;
- adaptation boundary;
- Verification/evidence expectations;
- relevant Handoff/continuation state.

Fresh workers are allowed but not mandatory. Continuing workers are allowed when material state is not session-only.

## 2. Worker result

A worker result is subordinate execution semantics, not a new A1/A2 entity by default. It preserves/references, as applicable:

- outcome/result;
- evidence/provenance;
- blockers/failures;
- discovered dependency/resource conflict;
- material architecture issue;
- Plan-deficiency signal;
- Contract-deficiency signal;
- material information requiring promotion;
- next/reconciliation needs.

Small worker results do not require a Handoff Record merely because responsibility briefly crossed a model invocation boundary.

## 3. Semantic promotion

Material discoveries do not become durable truth by remaining in worker/session state.

Route them to the correct semantic owner, such as:

- Plan revision;
- Contract Change Proposal;
- Architecture Model / ADR;
- Evidence Record;
- Learning Record;
- Work state;
- Authority state;
- Handoff Record where continuation semantics require it.

L4 micro-plans remain ephemeral by default. Before an L4 micro-plan/session is intentionally discarded, material information that would otherwise be lost must already exist in the proper durable owner or continuation state.

## 4. Recovery

A conforming implementation can reconstruct material Planning/Execution state after orchestrator/session loss from authoritative durable state and references.

The orchestrator may hold queues, caches, projections, temporary dependency graphs, or worker-local state, but these cannot be the only copies of material Plan/work/dependency/authority/evidence decisions.

## 5. Human collaboration boundary

Human participation may provide judgment, expertise, tradeoff reasoning, Human-reserved DA, or organization-reserved approvals.

A Human required only to copy, click, translate, upload, or trigger an already-determined agent action is mechanical middleware when the required canonical operation should be agent-operable.

> **Human judgment is a feature. Human transcription is usually a defect.**
