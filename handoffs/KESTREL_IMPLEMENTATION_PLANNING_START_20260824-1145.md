# Handoff: Kestrel — First Organization-Specific AE Implementation Planning Start

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**Coordination only — do not merge this branch into `main`.**

---

## Human Owner direction

Part 1 of the Canonical Agentic Engineering System is closed, independently verified, and Human Owner accepted. Do **not** reopen Part 1, invent an L1-M domain, or change Canonical Core semantics merely because implementation work is beginning.

The Human Owner has now authorized the next scope:

> **Plan the first real organization-specific AE implementation on Kestrel, the Human Owner's home lab.**

Kestrel is the first implementation target, not a Canonical AE dependency.

This receiving session is a **Planning session only** until the Human Owner approves the Kestrel implementation Contract and implementation Plan. Do not make changes to Kestrel from this ChatGPT planning session.

---

## Inputs the Human Owner will supply in the new session

The Human Owner will upload directly after this handoff:

- `Kestrel_Baseline.md`
- the corresponding Kestrel baseline `.zip`

Treat those uploaded baseline materials as the authoritative supplied organization/system baseline for this planning exercise unless their own contents identify subordinate or superseded sources.

Also use the accepted Canonical AE System distribution/repository as the source of AE semantics. The repository may receive non-semantic human-readability/navigation improvements from an independent reviewer; independently verify the current release manifest and accepted semantic basis and distinguish navigation/organization changes from Canonical semantic changes.

Do **not** derive AE semantics from prior design conversations when the Canonical repository/distribution supplies the authoritative answer.

---

## Known Kestrel implementation-team context

The actual implementation team for this first installation will itself be an AI agent.

Primary implementation actor:

- **Claude CLI**, already running on Kestrel;
- has **root technical access** to Kestrel;
- may use as many fresh CLI sessions as needed.

Secondary tooling available:

- Codex CLI is also installed/available, but the Human Owner cannot access it as conveniently when remote;
- Claude CLI is therefore the preferred first implementation actor unless Planning establishes a reason to use something else.

Critical Canonical distinction:

> **Root access is technical capability/entitlement; it does not by itself establish Operational Authority or Decision Authority.**

The Kestrel implementation Plan must explicitly define what the implementation agent is authorized to inspect/change and what remains Human-reserved.

The Human Owner is comfortable with broad agent Operational Authority in the home lab if it is explicitly scoped and governed.

---

## Experimental intent

Kestrel is not only an installation target. It is the first real operational experiment of the accepted AE System.

We want to learn:

- whether an implementation agent can understand and use the accepted distribution without hidden design-history coaching;
- how much of implementation is configuration/binding versus new software;
- whether the ten Canonical Capability Contracts are sufficient in a real environment;
- whether fresh Claude sessions can reconstruct and continue work from durable state;
- where human-readability/discoverability of the repository affects agents or Humans;
- whether authority semantics are useful or cumbersome in a single-owner lab;
- what Human mechanical intervention remains and why;
- what implementation friction suggests for a future AE Portal/product surface;
- total time, Human time, agent sessions, retries, replans, failed validations and cost where practical;
- what instructions an implementation team wishes it had.

Preserve a practical **implementation friction log** as learning/evidence. Do not make the friction log Canonical truth merely because it is useful.

---

## Implementation-method hypothesis to test

Part 1 already defines the semantic adoption process. Kestrel should test and operationalize it rather than invent a separate implementation methodology.

Expected high-level path:

1. verify accepted Canonical AE release/distribution;
2. comprehend and version the supplied Kestrel baseline;
3. establish/derive the applicable OEB + Product/System Profile/Baseline inputs;
4. create a Candidate `AE Implementation Profile [A1]`;
5. map all ten Canonical Capability categories and required operations to Kestrel providers/access paths;
6. identify Capability gaps separately from Engineering Health Findings;
7. establish identity, entitlements, OA, DA, policy, PEP and exception semantics;
8. establish architecture anchors, durable state, bootstrap/context, knowledge and handoff/reconstruction;
9. establish Work Management and normal lifecycle interfaces;
10. derive the normal Kestrel implementation `Plan [A1]` with L2/L3 work, dependencies, parallelism, adaptation boundaries, Verification/Evidence and Validation strategy;
11. independently review the exact Plan;
12. only after Human Owner approval, give the implementation actor the accepted distribution + supplied baseline + approved Contract + approved Plan and let it execute through normal AE semantics;
13. independently Validate the exact Kestrel implementation before any Conforming projection.

There is no special "Adoption Plan" or "Installation Record" entity unless Canonical semantics later require one.

---

## Human implementation path vs agent implementation path

The Human Owner wants reusable implementation guidance for both future cases.

The Canonical requirements should remain the same. The execution interface differs.

### Human implementation team path

A Human team needs:

- explanatory sequence and rationale;
- checklists and decision points;
- provider/access-path examples;
- commands/configuration guidance as applicable;
- Evidence collection guidance;
- troubleshooting and recovery guidance;
- explicit points where Human judgment/DA is required.

### Agent implementation team path

An agent implementation team needs:

- machine-readable/discoverable accepted distribution;
- exact supplied baseline;
- explicit approved Contract and Plan;
- authorized access paths and scope;
- durable task/state/evidence locations;
- bootstrap/reconstruction instructions for fresh sessions;
- bounded adaptation/retry/replan/escalation rules;
- independent Validation path.

Use Kestrel to discover the practical differences. After real implementation evidence exists, propose a reusable **AE Implementation Guide** with Human and Agent paths rather than writing it entirely from theory now.

---

## Required first-session work after baseline upload

After reading the full `Kestrel_Baseline.md` and `.zip`, do **not** immediately produce shell commands or an installation script.

First produce a grounded Planning assessment containing:

1. **Baseline comprehension**
   - what Kestrel is;
   - current architecture/topology;
   - existing engineering/tooling environment;
   - authoritative baseline/version facts;
   - material constraints and risks.

2. **Input sufficiency assessment**
   - determine whether the supplied baseline already constitutes or can support the OEB, Product/System Profile and Product/System Baseline needs;
   - identify only material missing information;
   - do not issue a giant questionnaire;
   - infer where the source clearly supports an answer and ask the Human Owner only for genuinely unresolved blockers/decisions.

3. **Canonical applicability map**
   - identify the accepted Canonical release/effectivity;
   - map all ten Capability categories and required Kestrel operations;
   - identify already-satisfied, binding/configuration, and genuine gap work.

4. **Authority model proposal**
   - technical access;
   - identity and entitlements;
   - proposed broad Claude Operational Authority;
   - Human-reserved Decision Authority;
   - policy/PEP/exception/revocation needs;
   - safety/rollback constraints for root-level operations.

5. **Capability gaps vs Engineering Health gaps**
   - keep them explicitly separate;
   - classify material impact as BLOCK / CONSTRAIN / DEGRADE / NONE as applicable.

6. **Architecture/context/bootstrap proposal**
   - authoritative durable state locations;
   - bootstrap entry points for Human and agent actors;
   - fresh-session reconstruction path;
   - interface parity from normal Kestrel working environments.

7. **Proposed Kestrel Implementation Contract**
   - Goal;
   - Spec;
   - Proof;
   - Non-goals;
   - Human-reserved decisions.

8. **Architecture-aware Kestrel Implementation Plan**
   - exact Contract/baseline references;
   - affected architecture;
   - L2/L3 work;
   - dependencies/barriers/parallelizable work;
   - Planning Depth/Method;
   - capability bindings and access paths;
   - authority/policy needs;
   - context/bootstrap work;
   - standards/applicability;
   - health remediation;
   - Verification/Evidence strategy;
   - independent adoption Validation strategy;
   - adaptation boundaries;
   - rollback/recovery considerations;
   - agent session/handoff strategy.

9. **Implementation-team package design**
   - what the Claude implementation agent will receive;
   - what it must discover itself;
   - what prior conversation/design history must be excluded;
   - how fresh sessions resume;
   - what outputs/evidence each session must leave behind.

10. **Experiment/measurement plan**
    - elapsed time;
    - Human hours/interventions;
    - agent sessions;
    - retries/replans/escalations;
    - Validation failures;
    - software installed vs existing systems bound/configured;
    - capability/health findings;
    - friction and possible future Portal needs;
    - cost where observable.

---

## Planning guardrails

- **Planning mode first.** No Kestrel implementation changes before Human Owner review/approval of Contract + Plan.
- Treat the accepted Canonical AE System as authoritative; do not redesign the Core to suit Kestrel.
- Kestrel-specific choices belong in OEB/Profile/Binding/Plan/architecture/implementation artifacts unless a genuine Canonical contradiction is discovered.
- Do not assume a Portal, one CLI, one IDE, one orchestrator, one model provider, one database or one runtime.
- Do not equate root access with OA/DA.
- Do not insert the Human as routine mechanical middleware where a governed agent-accessible operation should exist.
- Preserve exact revision/source traceability.
- Preserve fresh-session reconstructability.
- Use normal Evidence and independent Validation; executor success is not adoption acceptance.
- Surface ambiguity or contradiction rather than inventing hidden Kestrel facts.

---

## Clean implementation-agent boundary

The ChatGPT planning session may use this handoff and the supplied Kestrel baseline to produce the Contract/Plan.

The later Claude implementation actor should ideally **not** receive the historical AE design conversations. Give it the minimum sufficient governed implementation package:

- accepted Canonical AE distribution;
- supplied/effective Kestrel baseline;
- approved Kestrel implementation Contract;
- approved exact Plan and execution scope;
- capability/authority/bootstrap access information necessary to execute;
- durable state/evidence/handoff locations.

This makes the Kestrel installation itself a meaningful test of whether the system works without hidden conversational memory.

---

## Known parallel follow-on

Canonical repository issue #12 — required integrity-check enforcement on `main` — remains a separate accepted non-blocking repository-governance follow-on. Do not conflate it with Kestrel's organization-specific implementation unless explicitly authorized.

---

## Immediate receiving-session instruction

1. Read this handoff fully.
2. Read `handoffs/README.md` on `ae-session-relay`.
3. Wait for / inspect the Human Owner's uploaded `Kestrel_Baseline.md` and `.zip`.
4. Independently verify current accepted Canonical release state, accounting for any non-semantic repository readability/navigation changes since Part 1 closure.
5. Produce the baseline comprehension + input-sufficiency assessment first.
6. Tell the Human Owner whether anything material is still needed.
7. Continue into Contract/Plan design only from grounded baseline facts.
8. Do not implement on Kestrel until Human Owner approval.
