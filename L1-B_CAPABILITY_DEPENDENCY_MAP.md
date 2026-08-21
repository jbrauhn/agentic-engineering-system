# L1-B — Capability Dependency Map

**Status:** Approved L1-B baseline  
**Scope:** Why the seven canonical logical responsibilities depend on the ten canonical AE capabilities. This is input to later Capability Contract operation/entitlement design, not the final operation matrix.

## 1. Mapping rule

A dependency exists when a canonical logical responsibility needs behavior that an Organization-specific AE Implementation may obtain through one of the ten canonical Capability Contracts.

The map captures **why** the dependency exists. It does not imply:

- one provider per capability;
- one component per responsibility;
- that the provider is always physically external to the organization;
- that every responsibility directly invokes every provider;
- that a checkmark alone proves the capability is usable.

Later capability design must work backwards from these reasons to define required operations, agent accessibility, entitlement/scoping, Block/Constrain/Degrade implications, policy/enforcement, and implementation Proof.

## 2. Capability types

1. Source Control
2. CI/CD
3. Models
4. Runtime / Execution
5. Identity & Access
6. Governed Tool Access
7. Observability
8. Knowledge / Memory
9. Work Management
10. Validation

## 3. Responsibility dependencies

### R1 — Lifecycle State & Transition Governance

| Capability | Why R1 may require it |
|---|---|
| **Work Management** | Persist or represent work/Loop state, relationships, and transitions; expose lifecycle-relevant status without human clerical mediation. |
| **Knowledge / Memory** | Retrieve durable lifecycle/Contract/Plan/decision context needed to evaluate current state and valid routes. |
| **Identity & Access** | Establish actor identity where transition eligibility or gate satisfaction depends on who acted/approved. |
| **Validation** | Consume authoritative Validation outcome that drives Accept, Retry, Replan, Contract-change, or Escalation routing. |
| **Source Control** | Where versioned Contract/Plan/decision artifacts are authoritative, determine approved/current artifact state referenced by lifecycle transitions. |

**Later operation questions:** read current lifecycle-related state; read approved artifact/version; record transition; query relationships; consume gate/Validation outcome; preserve transition provenance.

---

### R2 — Durable Engineering State, Identity & Traceability

| Capability | Why R2 may require it |
|---|---|
| **Source Control** | Authoritative versioning/provenance for Contracts, Plans, ADRs, architecture-as-code, schemas, or other versioned engineering artifacts. |
| **Work Management** | Authoritative operational state for work items, relationships, dependencies, and selected lifecycle properties. |
| **Knowledge / Memory** | Durable knowledge, handoff, explanatory/context state, or indexed relationships that remain system-owned and reconstructable. |
| **Observability** | Preserve references/provenance to operational events or evidence sources when those events participate in traceability. |
| **Identity & Access** | Associate material changes/provenance with authenticated actors and control access to authoritative state. |

**Architecture Model Stewardship dependencies:** Source Control and/or Knowledge / Memory may persist architecture representations; Work Management may relate architecture-significant work; all remain implementation bindings rather than required stores.

**Later operation questions:** create/read/version/reference durable artifacts; resolve stable IDs; retrieve authoritative version; link relationships; inspect provenance; identify writer/actor; resolve system of record.

---

### R3 — Context & Knowledge Coordination

| Capability | Why R3 may require it |
|---|---|
| **Knowledge / Memory** | Retrieve durable knowledge, prior handoffs, indexed representations, and context material without depending on conversation history. |
| **Source Control** | Retrieve authoritative code, architecture, Contracts, Plans, decisions, standards/profile artifacts, or other versioned state for context assembly. |
| **Work Management** | Retrieve current work, dependencies, status, discussion/evidence links, and task scope. |
| **Models** | Models may help select, summarize, reason over, or package bounded context; this does not make one model/context strategy canonical. |
| **Identity & Access** | Apply actor/resource access boundaries during retrieval and context construction. |
| **Governed Tool Access** | Access organization knowledge/tools through governed interfaces where retrieval itself is a protected operation. |

**Later operation questions:** query/retrieve by task and stable identity; read authorized state; preserve source/provenance; construct handoff; continue/resume with bounded context.

---

### R4 — Authority, Policy & Decision Coordination

| Capability | Why R4 may require it |
|---|---|
| **Identity & Access** | Establish authenticated actor identity and relevant entitlements/attributes used in OA/DA or policy decisions. |
| **Governed Tool Access** | Obtain or carry policy/authority context for protected tool operations and integration boundaries. |
| **Work Management** | Surface/record decisions, approvals, proposals, rationale, or gates through organization workflow when selected as the implementation mechanism. |
| **Knowledge / Memory** | Preserve durable rationale, decision context, approval records, and policy references where not held elsewhere. |
| **Source Control** | Support source-controlled decision/approval artifacts or versioned policy/profile references when selected. |

**Later operation questions:** resolve authenticated actor; query authority/policy; submit decision request; record approval/rejection; preserve rationale/provenance; expose decision outcome to R1/R5.

---

### R5 — Capability Binding & Governed Invocation

R5 is the primary cross-capability integration responsibility.

| Capability | Why R5 may require it |
|---|---|
| **Source Control** | Bind and invoke canonical source-control operations such as read/change/commit/branch/PR operations where required by lifecycle work. |
| **CI/CD** | Bind and invoke build/test/pipeline/evidence operations. |
| **Models** | Bind model inference/reasoning operations to approved providers/models subject to organization controls. |
| **Runtime / Execution** | Bind execution/sandbox/environment operations used by agents or engineering work. |
| **Identity & Access** | Establish/use scoped identity and entitlements needed for provider operations. |
| **Governed Tool Access** | Bind tool interfaces and authorization/enforcement mechanisms used for protected external operations. |
| **Observability** | Bind telemetry/query/event interfaces used to observe AE and target-system behavior. |
| **Knowledge / Memory** | Bind retrieval/write operations used for durable knowledge and context. |
| **Work Management** | Bind the canonical agent-operable create/read/query/update/relationship/state/comment/evidence/close operations. |
| **Validation** | Bind validation/evaluation operations or provider interfaces used by R6. |

**Later operation questions:** resolve provider binding for canonical operation; determine supported interface; convey task/resource scope; invoke under least privilege; handle denial/failure; retain operation/result provenance; prove agent accessibility.

**Important:** R5 dependency on all capabilities does not imply that every invocation traverses one Capability Gateway.

---

### R6 — Evidence & Validation Coordination

| Capability | Why R6 may require it |
|---|---|
| **Validation** | Obtain or execute independent evaluation behavior appropriate to Proof and risk. |
| **CI/CD** | Consume build, test, scan, and automated verification evidence. |
| **Source Control** | Identify exact code/artifact/version under Validation and retrieve versioned evidence/changes. |
| **Observability** | Consume runtime/operational evidence where Proof concerns behavior, performance, reliability, security, or other observed outcomes. |
| **Work Management** | Relate Validation/evidence to work items and route resulting work/retry/replan actions. |
| **Knowledge / Memory** | Retrieve durable evidence context and preserve Validation rationale/records where selected. |
| **Identity & Access** | Establish Validator identity/role and protect Validation/evidence resources. |
| **Models** | A model may perform part/all of a Validator role where policy/risk permits; model use does not by itself establish independence. |

**Later operation questions:** retrieve immutable/identified evidence; bind evidence to Proof; establish Validator identity/path; record independent result; route outcome; preserve rationale/provenance.

---

### R7 — Observability, Metrics & Learning

| Capability | Why R7 may require it |
|---|---|
| **Observability** | Collect/query operational telemetry and events needed to measure AE Loops, provider operations, and outcomes. |
| **Knowledge / Memory** | Preserve experiment definitions/results, conclusions, learning, and references into future context. |
| **Work Management** | Relate learning/findings to work, experiments, remediation, and follow-on actions. |
| **CI/CD** | Provide pipeline/verification timing and outcome data used in diagnostics and experiments. |
| **Models** | Models may assist analysis/synthesis of observations and experiments while evidence remains the basis for conclusions. |
| **Source Control** | Preserve versioned experiment/system-decision artifacts or correlate outcomes with exact implementation changes. |

**Later operation questions:** emit/query relevant events; correlate event to Loop/artifact/provider operation; retrieve measures; persist experiment result/conclusion; create durable learning/reference.

## 4. Cross-cutting observations for later Capability Contract design

### Work Management is used in two materially different ways

- **R1/R2/R4/R6/R7** may use Work Management as an authoritative or relationship-bearing workflow/state system.
- **R5** must be able to invoke the canonical agent-operable work-item operations directly when authorized.

This distinction is why “we have Jira/Plane/Azure DevOps” does not by itself satisfy the Work Management capability. Agent operability and scoped entitlement must also be demonstrated.

### Identity & Access does not equal Decision Authority

Identity & Access provides identity/authentication/entitlement mechanisms. R4 applies canonical OA/DA and policy semantics. An identity provider does not decide the meaning of Human Decision Authority for AE.

### Observability capability does not equal R7

The provider can collect/store telemetry. R7 establishes what AE measurements/events mean, how they relate to Loops/outcomes, and how learning becomes durable state.

### Validation capability does not equal R6

A Validation provider can provide evaluation operations/evidence. R6 preserves Proof/evidence relationships, independence semantics, Validation state/provenance, and lifecycle routing.

### Knowledge / Memory capability does not equal R2 or R3

The provider stores/retrieves information. R2 governs authoritative state meaning/relationships; R3 governs task-relevant context construction and continuation.

## 5. Input to downstream capability design

For every dependency above, later capability design shall determine at least:

- required provider operation(s);
- whether the operation must be directly agent-accessible;
- minimum entitlement/scoping semantics;
- required OA/policy context;
- where PEP enforcement occurs;
- what missing/denied operation does to Loop operability and AE conformance;
- what evidence demonstrates that the binding is actually usable.

This artifact intentionally does not yet define those complete operation contracts.