# L1-A — Design Forces / Quality Attributes

**Status:** Approved L1-A baseline candidate pending repository review/merge  
**Purpose:** Provide architecture evaluation forces for downstream L1 design without silently creating new Contract requirements.

## Classification rule

Each force is classified as one of:

- **Contract-derived requirement** — directly follows from approved Contract v1.0;
- **Adopted design principle** — supported by adopted Decision Records and consistent with Contract, but not elevated into a new Contract invariant;
- **Candidate design decision** — would require explicit review before becoming an adopted architectural constraint.

No L1-A force below creates a new Contract requirement.

## 1. Portability

**Classification:** Contract-derived requirement.  
**Source:** Contract Goal; Spec §4 Portable canonical semantics; §5 Organization Engineering Baseline; §6 Canonical AE Capability Model; §18 Concrete Part 1 Adoption Deliverable; Portability Principle.

**Architectural consequence:**

- separate canonical semantics from provider/organization bindings;
- avoid embedding vendor products or one topology into canonical interfaces;
- make Organization Engineering Baseline and profiles explicit;
- make capability contracts technology-neutral but behaviorally precise.

## 2. Governability

**Classification:** Contract-derived requirement.  
**Source:** Contract Spec §2 Human–AI authority and governed enforcement; §6 Capability Model; §14 Planning and Execution; §15 Validation and evidence.

**Architectural consequence:**

- represent identity, authority, policy, resource/task scope, and enforcement explicitly;
- protected operations cannot rely on documentation-only controls;
- fail closed where required authority cannot be established;
- distinguish technical access, Operational Authority, and Decision Authority.

## 3. Agent-operability

**Classification:** Contract-derived requirement.  
**Source:** Contract Goal; Spec §6 Canonical AE Capability Model; §7 Agent-accessible Work Management; §10 Agent-assisted engineering improvement.

**Architectural consequence:**

- Capability Contracts identify required operations and agent-accessible operations;
- implementations must support scoped entitlements needed by the lifecycle;
- routine mechanical intermediary work must not be shifted to humans merely because a provider lacks agent interfaces;
- least privilege still applies.

## 4. Traceability

**Classification:** Contract-derived requirement.  
**Source:** Contract Spec §11 Architecture and traceability; §12 Durable engineering knowledge and identifiers; §15 Validation and evidence; applicable Proof traceability expectations.

**Architectural consequence:**

- stable identities and relationships across Contract, architecture, Plan, work, evidence, decisions, and Validation;
- provenance and version history where materially useful;
- architecture and lifecycle artifacts must be navigable by humans and agents.

## 5. Resumability

**Classification:** Contract-derived requirement.  
**Source:** Contract Spec §3 The system owns memory; §12 Durable engineering knowledge and identifiers.

**Architectural consequence:**

- durable state must survive one agent/session ending;
- context can be reconstructed from system-owned state;
- handoffs are explicit;
- no single conversational context becomes the authoritative workflow store.

## 6. Verifiability

**Classification:** Contract-derived requirement.  
**Source:** Contract Goal; Spec §6 Implementation Proof; §15 Validation and evidence; Proof C Machine-verifiable integrity; G capability-operation/entitlement assessment; H Work Management Proof; M reproducible fresh-session adoption test.

**Architectural consequence:**

- capabilities define proof of usability, not only configuration claims;
- machine-checkable artifacts use validators/checks where reasonable;
- installation/adoption state must be demonstrable with evidence;
- reference behavior includes both happy and controlled non-happy routes.

## 7. Evolvability

**Classification:** Contract-derived boundary plus adopted design principle.  
**Source:** Contract Spec §4 Portable canonical semantics; Contract Non-Goals; DR-017 Contract change-control boundary and design test.

**Architectural consequence:**

- separate invariants from provider, protocol, notation, context strategy, model-placement, orchestration, and other lower-level choices;
- use DR/ADR/profile/Plan/experiment layers rather than reopening the Contract for replaceable mechanisms;
- design interfaces so lower-level choices can be superseded independently.

## 8. Human comprehensibility

**Classification:** Contract-derived design force reinforced by adopted design principles; not a new Contract invariant.  
**Source:** Contract Spec §2 Human–AI authority; §17 Decision history and System Rationale. Reinforced by adopted DR-091 Human–AI thinking partnership and DR-092 human-native communication.

**Architectural consequence:**

- make lifecycle position, consequential decisions, authority state, evidence, and architecture relationships inspectable by humans;
- preserve rationale rather than presenting only machine state;
- avoid architectures whose governance depends on humans inferring hidden coupling or opaque agent behavior.

## 9. Engineering-quality protection

**Classification:** Contract-derived requirement.  
**Source:** Contract Goal (increase speed, scale, automation without sacrificing—and where evidence supports it, improving—engineering quality); §9 Engineering-health assessment; §15 Validation and evidence; Proof K Engineering-health detection; L governed agent-assisted remediation.

**Architectural consequence:**

- quality must remain observable and evidential;
- engineering-health findings remain distinct from capability gaps;
- faster execution cannot bypass Verification/Validation expectations;
- agents may help remediate weaknesses rather than amplifying them.

## Downstream use

L1-B and later architecture alternatives should explicitly evaluate their consequences against these forces.

If a later architecture discussion produces a genuinely new mandatory quality requirement, it must be surfaced as a new decision question rather than silently inserted into this list.
