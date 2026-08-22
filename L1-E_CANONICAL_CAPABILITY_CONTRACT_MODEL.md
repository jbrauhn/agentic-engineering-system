# L1-E — Canonical Capability Contract Model

**Status:** Approved L1-E semantic baseline  
**Authority:** Contract v1.0; DR-106–113; Human Owner L1-E decision  
**Scope:** Provider-neutral capability semantics. This artifact does not prescribe provider APIs, protocols, credentials, topology, or one invocation mechanism.

## 1. Three semantic layers

Canonical AE distinguishes:

1. **Canonical Capability Contract Definition [F]** — defines what a canonical AE capability must make possible.
2. **Organization Capability Binding [A1]** — defines how an Organization-specific AE Implementation realizes the Canonical Capability Contract for a declared scope.
3. **Runtime request authorization/use** — determines whether a particular actor/request may use a bound operation now.

These are not interchangeable.

> **Capability Contract ≠ provider API. Capability Binding ≠ provider. Binding readiness ≠ runtime authorization.**

A healthy binding may deny a particular actor. An actor denial does not by itself make the capability defective. Broad administrator credentials do not prove agent-operability.

## 2. Canonical operation semantics

A canonical operation is provider-neutral. It identifies the semantic engineering action AE requires.

Minimum metadata, where semantically applicable:

- stable canonical `operation_id`;
- capability category;
- purpose;
- requirement class: `REQUIRED` or `CONDITIONAL_REQUIRED`;
- lifecycle / R1–R7 consumers;
- semantic inputs/preconditions;
- semantic result/output;
- side-effect class where relevant;
- actor-access expectation;
- whether agent-operability is required;
- protected-operation status;
- authority/policy/enforcement hooks;
- evidence/provenance expectation;
- failure semantics;
- default operational impact if unavailable;
- implementation Proof expectations.

Provider payloads, REST verbs, MCP tool names, SDK functions, CLI syntax, Jira transitions, GitHub API shapes, token formats, or other provider mechanics are not canonical operation semantics.

## 3. Requirement classes

Canonical Capability Contracts use:

- **REQUIRED** — the capability must provide the operation for the applicable declared scope.
- **CONDITIONAL_REQUIRED** — the operation becomes required when its declared lifecycle/use condition applies.

Optional conveniences remain reference/adoption guidance until evidence justifies promotion into the Canonical Core.

## 4. Agent-operability

`agent_access_required` means:

> **A conforming implementation provides a governed machine-accessible path usable by or on behalf of an appropriately authorized agent for that canonical operation.**

It does not mean the reasoning model directly calls the provider, handles raw credentials, bypasses mediation, or that every agent is entitled.

A direct API, broker, adapter, agent runtime, MCP server, or another governed mechanism may perform the provider interaction.

## 5. Mechanical Human intermediary rule

Human participation is not inherently a deficiency.

A Human exercising Contract approval, risk acceptance, material tradeoff judgment, or another reserved Decision Authority performs legitimate AE work.

A Human who only clicks, copies, uploads, changes provider status, or triggers a known operation because the authorized agent lacks a governed machine path is accidental Human middleware when that operation is required to be agent-operable.

> **Human judgment is a feature. Human transcription is usually a defect.**

## 6. Binding/usability Proof

Configured does not mean proven usable.

For applicable required operations, implementation Proof establishes as relevant:

- semantic operation support;
- correct provider mapping;
- deterministic scope resolution;
- governed access path;
- reachability from declared supported consumer/runtime contexts;
- least-privilege scoped entitleability;
- applicable enforcement;
- authorized success;
- expected unauthorized denial;
- reconstructable result/provenance;
- satisfaction of the canonical semantic result.

Proof may use a sandbox, synthetic resource, lower environment, safe simulation plus integration evidence, or another safe method when that credibly exercises the actual organization binding. API documentation alone is insufficient Proof.

## 7. Runtime authorization

A runtime request evaluates semantics equivalent to:

`identity → current entitlement → OA / applicable DA / policy → PEP → provider execution → result/evidence`

Runtime outcomes reuse L1-D:

- **ALLOWED**
- **DENIED**
- **BLOCKED**

DENIED means established facts forbid the request. BLOCKED means a potentially valid request cannot proceed because a required capability, authority, state, or prerequisite cannot currently be established.

## 8. Downstream boundaries

L1-E exposes hooks but does not fully define:

- OA/DA role-permission matrices;
- policy language or delegation;
- risk-tier authority;
- full Zero Trust evaluation;
- standards applicability;
- context/RAG mechanisms;
- Planning Methods;
- orchestration topology;
- developer-environment taxonomy.
