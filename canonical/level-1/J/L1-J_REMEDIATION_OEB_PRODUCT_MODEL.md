# L1-J — Governed Remediation, OEB, and Product/System Specialization Model

**Status:** Human Owner-approved L1-J semantic baseline

## 1. No parallel remediation workflow

Engineering-health findings and standards gaps use the existing AE lifecycle. Canonical AE does not create a separate health-remediation process.

Typical route:

```text
Engineering Health Finding / standards gap
    ↓
triage + scope + priority + authority + disposition
    ↓
existing/new AE Loop / Contract as appropriate
    ↓
Planning / Execution
    ↓
Evidence
    ↓
independent Validation
    ↓
current health disposition / baseline / learning update
```

An imperfect organization may adopt AE while governing material deficiencies. There is no universal remediation-before-adoption requirement.

## 2. Routing discovered standards/health conditions

Use inherited L1-H semantics:

- **LOCAL_ADAPTATION** — condition can be handled inside the reviewed Plan adaptation boundary without materially changing the reviewed route;
- **REPLAN** — reviewed route materially changes while Contract remains valid;
- **PROPOSE_CONTRACT_CHANGE** — Goal/Spec/Proof or another Contract-level semantic is deficient/needs change;
- **ESCALATE** — required authority/risk/policy/decision cannot be resolved in current route;
- **DEFER / ACCEPT RISK** — only when applicable governance permits it and the decision remains explicit/provenanced;
- **REMEDIATION LOOP** — when a separate governed unit of work is appropriate.

A newly discovered mandatory standard that makes Contract Proof semantically deficient routes through Contract Change/G5. It does not silently alter Proof.

## 3. Remediation outcome

The discovering/assessing/implementing path may produce Evidence, but successful remediation is established through normal independent L1-I Validation.

The finding is not erased after remediation. Later Validation/Decision/Evidence changes the **current disposition** while preserving historical observation.

## 4. OEB coordination

OEB may reference/coordinate, as applicable:

- authoritative standards sources;
- organization default applicability rules;
- requirement character;
- Evidence/Verification/Validation expectations;
- architecture/security/engineering practice expectations;
- exception/waiver authority/process references;
- known Engineering Health Findings and derived current-health projections;
- organization-level remediation expectations.

OEB is a versioned coordination baseline. It does not physically own external standards text, policy engines, assessment tools, or every health signal.

## 5. Product/System specialization

Product/System Profile may tighten, narrow, specialize, or add product-specific standards/health requirements.

It may not silently weaken:

- Canonical AE mandatory semantics;
- mandatory organization standards/policy;
- mandatory security/governance constraints;
- applicable required Evidence/Validation semantics.

Explicit exceptions remain scoped, authority-backed, effectivity-aware, and provenanced.

Effective standards/health configuration is a derived **[D]** projection.

## 6. Exact/effective state and no silent rebase

Active and historical work must remain reconstructable against exact OEB/Product/Profile/standard/finding state used at the time.

A newer OEB/Product/standard revision does not silently rebase active work. When a newly effective requirement or materially changed health state affects active assumptions, reassessment/routing is explicit.

## 7. Agent-useful context

L1-G Context Requirements should expose only the bounded material standards/health state needed for the current action, including as applicable:

- exact authoritative standards source/version/effectivity;
- applicability and rationale;
- requirement character;
- Evidence/application expectations;
- exception/waiver decision;
- unresolved applicability conflict;
- material Engineering Health Findings;
- health impact and derived current disposition;
- remediation/route constraints.

Do not dump complete external standards or assessment histories into every Context Package.

Context retrieval/index/summary remains non-authoritative.

## 8. Relationship to learning

Completed remediation may produce Learning Records or inform Experiments, standards profiles, OEB/Product revisions, or future Planning. L1-J provides only this relationship hook; it does not define the full metrics/experiments/learning protocol.

## 9. Adoption meaning

Engineering-health detection is diagnostic, not a prerequisite that the organization already be mature.

Canonical adoption should distinguish:

- Capability Gap: AE cannot adequately perform required canonical operations;
- Engineering Health Finding: target engineering state/practice can materially degrade or amplify agentic work.

An organization can be operationally capable of AE while carrying governed health debt. AE should help convert material debt into controlled engineering improvement work.