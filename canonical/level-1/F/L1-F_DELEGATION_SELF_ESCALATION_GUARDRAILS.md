# L1-F — Delegation and Self-Escalation Guardrails

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Delegation is optional

An organization may prohibit delegation and remain conforming.

When delegation exists:

- delegation is explicit;
- the delegator is authorized to delegate;
- delegated authority cannot exceed the delegator's delegable scope;
- operation/decision class/resource/time/conditions remain bounded;
- provenance is retained;
- onward delegation is prohibited unless explicitly allowed;
- Canonical Human-reserved DA cannot be delegated to AI.

L1-F does not define a delegation DSL or universal depth algorithm.

## 2. Self-escalation invariant

> **An actor may not use the effect of an authority-changing operation to authorize that same authority-changing operation.**

Authority-changing mutations are evaluated using authoritative **pre-change state**.

This applies as relevant to changes in:

- OA assignments;
- DA assignments;
- provider entitlement;
- authority-relevant identity/group/role state;
- policy;
- Capability Bindings;
- OEB/Profile authority configuration;
- Authority Decision/approval state;
- PEP configuration.

A mutation succeeds only when the actor already has independently established authority for that mutation.

## 3. No approval by document appearance

An actor cannot gain authority by fabricating an approval-shaped artifact.

Authority Decision validity requires authoritative identity, applicable DA, correct exact target/scope/revision, authoritative source, and provenance.

## 4. Circular authorization prohibition

A proposed new authority state may be the target of an authorized mutation, but it cannot serve as the authority basis for authorizing its own creation.

This rule also applies to automated policy/configuration changes made by agents.
