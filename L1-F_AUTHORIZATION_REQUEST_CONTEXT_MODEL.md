# L1-F — Authorization Request & Requirement Context Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Modular request context

Use subordinate **Authorization Request Context [B]** semantics.

Do not require one giant universally populated authorization object.

> **Common authorization semantics; operation-specific required context.**

## 2. Common core

A protected request must be able to identify as applicable:

- request/correlation identity;
- actor;
- authenticated identity;
- canonical operation;
- target resource / External Resource Reference where relevant;
- organization / Product-System scope;
- request/evaluation time;
- Capability Binding / binding plan;
- Access Path.

## 3. Governed-work facts

When relevant, request evaluation may require:

- AE Loop;
- L2 Execution Increment;
- L3 Executable Task;
- exact Contract revision;
- exact Plan revision and reviewed scope;
- Product/System Baseline revision;
- exact OEB revision;
- exact Product/System Profile revision.

## 4. Authority/security facts

When relevant, request evaluation may require:

- provider entitlement context;
- OA source/basis;
- DA source/basis;
- Authority Assignment reference;
- Authority Decision / approval reference;
- effective policy source references;
- classification;
- environment;
- risk;
- conditions/obligations;
- validity/time facts;
- delegation chain;
- revocation/supersession state.

## 5. Authority Requirement [B]

Each protected canonical operation or governed decision may declare a subordinate **Authority Requirement [B]** describing which facts are required for that operation/scope.

Typical requirement fields:

- protected operation or decision class;
- identity required?;
- provider entitlement required?;
- OA required?;
- DA required?;
- Human DA required?;
- approval / exact Authority Decision required?;
- exact Contract/Plan/OEB revision context required?;
- applicable policy evaluation required?;
- PEP/enforcement required?;
- obligation/condition support required?;
- provenance retention class.

Authority Requirement is semantic configuration, not a production authorization token.

## 6. Fail-closed evaluation

If a required authoritative fact cannot be established reliably within applicable freshness/policy constraints, the authority evaluation is INDETERMINATE and protected runtime behavior is BLOCKED.

If policy deterministically establishes that no qualifying authority exists, the result is DENY / DENIED instead.
