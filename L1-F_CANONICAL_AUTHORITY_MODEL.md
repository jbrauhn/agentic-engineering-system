# L1-F — Canonical Authority Model

**Status:** Human Owner-approved L1-F semantic baseline  
**Authority:** Contract v1.0; DR-107–116; Human Owner L1-F approval  
**Scope:** Provider-neutral authority, policy, and enforcement semantics. This artifact does not prescribe an IAM provider, policy language, RBAC/ABAC/ReBAC model, PDP topology, gateway, or centralized authorization service.

## 1. Central principle

> **Canonical AE defines an authorization protocol over authoritative facts, not a canonical authorization product.**

A conforming implementation may realize authority through explicit assignments, role-based policy, attribute/resource/task policy, relationship policy, dynamic policy, provider IAM, external PDPs, runtime authorization, distributed enforcement, or combinations of those mechanisms.

## 2. Canonical distinctions

AE preserves these as semantically distinct:

`technical capability ≠ Capability Binding readiness ≠ identity ≠ provider entitlement ≠ Operational Authority ≠ Decision Authority ≠ approval state ≠ policy decision ≠ Policy Enforcement Point ≠ successful provider execution`.

### Entitlement

> **A technically enforceable permission/capability available to an authenticated identity within a provider/system.**

Entitlement is a technical prerequisite. It is not proof of AE authority.

### Operational Authority — OA

> **Operational Authority is the effective scoped authority of an actor to perform or request one or more operational canonical AE actions against specified resources/context under applicable conditions.**

OA answers: **May this actor perform this operation in this governed work context?**

OA may be established by explicit Authority Assignment, authoritative external assignment/reference, dynamic policy derivation, relationship/task/resource policy, or another conforming authoritative mechanism. OA is not synonymous with a stored grant.

### Decision Authority — DA

> **Decision Authority is the effective scoped authority of an actor to make or approve a governed decision of a specified decision class.**

DA answers: **May this actor decide this question?**

DA does not itself grant provider execution permission.

### Authority Decision [A2]

> **An immutable durable governance record showing that an actor with applicable DA exercised that authority against an exact target/scope/revision.**

Authority Decision is an exercise of DA. It is not the DA itself.

### Policy decision

The final authority/policy evaluation result is:

- **PERMIT**
- **DENY**
- **INDETERMINATE**

Subordinate policy sources may use **NOT_APPLICABLE** where useful.

### Policy Enforcement Point — PEP

> **A mechanism at or near a protected boundary that prevents the protected effect from occurring unless applicable authorization requirements are satisfied and that enforces required authorization conditions.**

Policy decision and enforcement are separate responsibilities.

## 3. Policy result versus runtime outcome

L1-D runtime outcomes remain:

- **ALLOWED**
- **DENIED**
- **BLOCKED**

Typical mapping:

- `PERMIT + required technical prerequisites + applicable entitlement + applicable enforcement + provider operability → ALLOWED`
- `DENY → DENIED`
- `INDETERMINATE → BLOCKED`
- `PERMIT + missing required technical entitlement → BLOCKED`

Absence of an explicit grant is not automatically INDETERMINATE. If authoritative policy deterministically defines no qualifying authority as DENY, the result is DENY.

> **For a protected operation, INDETERMINATE is never permission.**

## 4. Policy obligations / conditions

A PERMIT may carry enforceable conditions/obligations, such as an environment restriction, exact approval reference, time boundary, evidence/audit obligation, or scoped resource constraint.

Canonical AE defines the need to carry required conditions from decision to enforcement. It does not define a universal obligation DSL.

## 5. Canonical Human-reserved authority inventory

L1-F does not add new universally Human-reserved decisions. It reflects the authority already established by Contract v1.0 and adopted decisions.

Contract v1.0 explicitly preserves Human authority over:

- engineering intent;
- material risk acceptance;
- consequential tradeoffs;
- Contract approval;
- Contract change;
- other decisions explicitly assigned to Human Decision Authority by higher canonical authority.

G1 Contract Approval and G5 Contract Change use this Human Decision Authority where applicable.

Organizations may reserve additional decision classes to Humans based on regulation, classification, risk, safety, product criticality, architecture governance, production impact, business policy, or other context. Those organization-reserved classes are not automatically universal Canonical AE Human reservations.

## 6. Authority precedence

`Canonical AE authority constraints → Organization authority baseline → Product/System specialization → Loop/task context`.

Downstream policy may tighten/narrow. It may not silently weaken a higher-authority mandatory constraint.

## 7. Relationship to R4, R5, and PEP

- **R4 Authority, Policy & Decision Coordination** evaluates/co-ordinates authority and policy and preserves decision provenance.
- **R5 Capability Binding & Governed Invocation** resolves provider-neutral canonical operations into provider-specific invocation.
- **PEP(s)** enforce the effective authorization result at/near protected boundaries.

R4 is not a universal execution broker. R5 is not the authority source. A PEP is not the policy decision itself.
