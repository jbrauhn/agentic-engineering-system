# L1-J — Standards Source, Applicability, Effectivity, and Exception Model

**Status:** Human Owner-approved L1-J semantic baseline  
**Semantic authority:** Human-readable Canonical AE specification  
**Scope:** Standards/practices applicability without making AE a standards repository or universal checklist

## 1. Core invariant

Canonical AE references authoritative standards, policies, practices, principles, and guidance; it does not become their universal repository.

An indexed, cached, summarized, copied, embedded, or retrieved representation does **not** acquire authority merely because AE can access it. DR-107 federated authoritative-state semantics remain controlling.

## 2. Standards source/reference semantics

A standards/practice reference can identify, as applicable:

- authoritative source/resource reference;
- source authority and provenance;
- exact version/revision/edition;
- effective basis, time, and scope;
- organization/Product-System scope/default applicability rule;
- requirement character;
- applicability trigger/condition;
- expected application/Evidence semantics;
- exception/waiver semantics when allowed;
- currentness/reassessment information.

External source text may remain external. Canonical AE requires reliable identity, provenance, effectivity, and retrievability—not wholesale copying.

No central Standards Service or standards provider is canonical.

## 3. Requirement character

Canonical applicability reasoning supports at least:

- **MANDATORY** — governing constraint when applicable;
- **CONDITIONAL** — mandatory when its declared trigger/condition is met;
- **ADVISORY** — selected practice/guidance whose proportional use is determined by context;
- **REFERENCE** — informational technique/source with no independent compliance obligation.

A mandatory requirement cannot be downgraded to advisory merely because compliance is inconvenient or process-heavy.

## 4. Applicability [B]

Standards applicability remains subordinate **[B]** semantics associated with the applicable versioned Standards Profile/OEB/Product specialization/work scope and authoritative references. L1-J does **not** create a first-class Standards Applicability Determination entity.

Applicability answers only whether a requirement/practice governs the declared scope. Minimum states are:

- **APPLIES**;
- **DOES_NOT_APPLY**;
- **CONDITIONAL_PENDING** — a declared condition/trigger is material but not yet resolved/effective;
- **UNRESOLVED_REQUIRES_DECISION** — governing facts cannot yet be established or a reserved decision is required.

A mandatory or conditional requirement with unresolved applicability does not silently become optional.

## 5. Application/disposition is a separate question

Applicability and application/compliance are not one status. Once applicability is established, a separate subordinate disposition can be:

- **SATISFIED** — appropriate application/compliance demonstrated;
- **NOT_DEMONSTRATED_OR_NONCONFORMING** — required application is absent or not yet evidenced;
- **AUTHORIZED_EXCEPTION_WAIVER** — requirement applies, but eligible authority explicitly permits deviation for the exact scope/version/effectivity window;
- **PROPORTIONATELY_NOT_USED** — an advisory practice is intentionally omitted because proportional engineering judgment shows it is unnecessary/disproportionate;
- **UNRESOLVED** — application/compliance cannot yet be established.

These meanings must never collapse:

`DOES_NOT_APPLY` ≠ `PROPORTIONATELY_NOT_USED` ≠ `AUTHORIZED_EXCEPTION_WAIVER` ≠ `NOT_DEMONSTRATED_OR_NONCONFORMING` ≠ `UNRESOLVED`.

A mandatory requirement cannot use `PROPORTIONATELY_NOT_USED` as an undocumented waiver.

## 6. Exceptions and waivers

Where deviation is allowed, an exception/waiver must resolve to existing authority semantics sufficient to prove, as applicable:

- eligible authority/Decision Authority;
- exact requirement/source version;
- exact organization/Product/System/work/resource scope;
- conditions and validity/effectivity;
- rationale/provenance;
- resulting Evidence/Validation expectations.

Reuse existing Authority Decision / Decision Record semantics where sufficient. L1-J introduces no waiver entity.

Applicability reasoning itself is not automatically Decision Authority. Human or other DA is required only when higher canonical/organization policy reserves the decision or exception.

## 7. Exact version and effectivity

The correct/effective requirement version for the declared scope governs—not the newest version merely because it exists.

A newer standard version does **not** silently rebase active or historical work.

For material use, the implementation must be able to reconstruct:

- the exact source/version considered;
- why it governed or did not govern the scope;
- the effectivity basis/time/scope;
- the previous effective basis when relevant;
- whether the new version requires reassessment;
- the governed response when active work is affected.

If a newly effective mandatory requirement invalidates reviewed assumptions, continuation must be explicitly evaluated. Route according to inherited semantics:

- inside reviewed adaptation boundaries → **LOCAL_ADAPTATION** where valid;
- material reviewed-route change with Contract still valid → **REPLAN**;
- Contract/Proof semantics are deficient → **PROPOSE_CONTRACT_CHANGE** / G5;
- authority/risk/policy cannot be established → **ESCALATE**.

Historical applicability remains reconstructable.

## 8. Relationship to Contract Proof, Planning, and Validation

Applicable standards/practices may contribute:

- Planning constraints;
- architecture/security/engineering expectations;
- Verification/Test Strategy requirements;
- Evidence expectations;
- Validation Requirement inputs;
- adaptation boundaries;
- authority/exception references;
- Context Requirements.

They do not become a second Contract and do not silently rewrite Contract Proof.

> **Contract Proof defines the required evidence for Contract success; applicable standards may constrain the work and contribute additional Evidence/Validation expectations when governing Contract/OEB/Product/policy semantics make them material.**

Checklist completion, provider pass labels, or applicability status alone is not Evidence.

## 9. OEB / Product-System specialization

OEB may reference organization standards sources, default applicability rules, requirement character, Evidence/Verification/Validation expectations, exception authority/process references, and engineering-practice expectations.

Product/System Profile may tighten, narrow, specialize, or add product-specific requirements. It may not silently weaken mandatory Canonical or organization constraints.

Authorized exceptions remain explicit, scoped, provenance-backed, and effectivity-aware.

The resolved effective standards view is derived **[D]**, not a competing authoritative standards store.

## 10. Agent-useful context

Through L1-G Context Requirements, an actor should be able to resolve, as applicable:

- what governs the current scope;
- exact authoritative source/version/effectivity;
- requirement character;
- why applicability was determined;
- expected Evidence/application requirements;
- applicable exception/waiver/decision;
- unresolved conflicts/unknowns;
- resulting route/adaptation constraints.

Context Package, retrieval index, summary, or cache never becomes standards authority.

## 11. Guardrails

Canonical AE does not require:

- one standards repository/provider;
- universal checklist compliance;
- one compliance platform;
- universal Human approval for applicability;
- one policy engine;
- latest-version-wins semantics;
- copying full standards into AE;
- heavier process as evidence of greater maturity.

Choose the simplest useful engineering pattern that satisfies the effective requirement and produces sufficient Evidence.