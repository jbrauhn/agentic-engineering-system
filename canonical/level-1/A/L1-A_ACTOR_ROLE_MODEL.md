# L1-A — Actor & Role Model

**Status:** Approved L1-A baseline  
**Scope:** Logical participation model only. Detailed Operational Authority (OA), Decision Authority (DA), entitlements, risk controls, and Validation independence rules are designed downstream.

## 1. Core distinction

AE shall not equate the following concepts:

> **role ≠ actor ≠ model ≠ agent instance ≠ authority**

### Role

A logical set of responsibilities within the AE lifecycle.

### Actor

A concrete human, organizational participant, software participant, or governed identity that fulfills one or more roles in a specific context.

### AI agent instance

A concrete running agent/session/process that may fulfill one or more logical roles subject to context, identity, policy, and authority.

### Model

A model capability used by an agent or other system component. A model is not itself a role, agent identity, or authority grant.

### Authority

The scoped right to perform an operation or make a decision in a particular context. Authority attaches to an actor/identity under policy; it is not inherent in a role label or technical access.

## 2. Logical roles

| Logical role | Primary responsibility | Typical possible actors | Later authority attachment |
|---|---|---|---|
| **Human Owner** | Owns consequential intent, Contract approval/change, material risk acceptance, and reserved decisions | Human | Human Decision Authority and applicable Operational Authority |
| **Engineering Practitioner** | Performs and evaluates engineering work through AE; collaborates with agents | Human engineer, architect, product/technical practitioner | Task/resource-scoped OA; DA where assigned |
| **AI Agent** | Reasons and executes governed work through capability bindings | Agent instance using one or more models/tools | Explicit scoped OA; DA only where canonical/organizational policy permits |
| **Independent Validator** | Evaluates evidence against Proof with required independence | Human, fresh AI agent, another agentic system, mixed Human–AI review | Validation authority appropriate to risk/policy; independence constraints designed later |
| **Implementation Team / Implementation Agent** | Instantiates the Canonical AE System Distribution for an organization | Human team, AI agent(s), mixed team | Installation/configuration OA and implementation decision authority as assigned |
| **Organization Governance / Policy Authority** | Supplies organization policy, risk posture, authority boundaries, classifications/constraints, and governance expectations | Human governance body, designated authority, policy system with human authority behind it | Policy/DA source; enforcement mechanics designed later |

## 3. Actor-role multiplicity

A single actor may fulfill multiple roles when allowed by policy and independence requirements.

Examples:

- one human may be both Engineering Practitioner and Human Owner for a low-risk personal project;
- one AI agent may plan and execute bounded work when permitted;
- the Independent Validator role may require a different agent instance or human than the executing actor when independence is required;
- an Implementation Agent may later operate as an Engineering Agent after installation, but authority must be re-evaluated for the new context.

A role does not imply a dedicated persona or permanently allocated agent.

## 4. Independent Validator is a role, not a persona

The Independent Validator role may be fulfilled by:

- a human;
- a fresh AI agent;
- another agentic system;
- mixed Human–AI review;
- another appropriately independent actor.

The correct fulfillment depends on risk, required independence, evidence type, organization policy, and authority. L1-A deliberately does not mandate a dedicated validator agent.

## 5. External relationships

### External Capability Providers

Capability Providers are systems/services, not lifecycle roles. Human and agent actors use them through governed bindings.

### Target Product/System

The Target Product/System is the external engineered subject. It is not an actor role. Humans/agents interact with it through governed operations and capability providers.

### Future AE Portal

The Portal is an optional client/system interaction surface, not a required actor and not a substitute for Human Owner, agent, or Validator roles.

## 6. Inputs to later OA/DA design

L1-F / authority design must be able to attach or evaluate at least:

- actor/identity;
- role being performed;
- operation;
- resource;
- task/Contract context;
- condition/time/environment;
- Operational Authority;
- Decision Authority;
- policy decision and enforcement state.

The existence of a role must never be treated as sufficient proof of authority.

## 7. Implementation-team use

An adopter uses this artifact to avoid hard-coding organizational job titles or agent personas into canonical AE semantics. It provides the logical responsibilities to map onto the organization's real people, agent instances, governance bodies, and technical identities.
