I reviewed the L1-F proposal and approve the overall authority architecture.

Proceed with D1–D20 as the L1-F Human Owner decision baseline, subject to the refinements below.

You are now authorized to implement L1-F after incorporating these refinements.

# Human Owner Decision — L1-F

APPROVED WITH REFINEMENTS.

The central principle is approved:

> **Canonical AE defines an authorization protocol over authoritative facts, not a canonical authorization product.**

Preserve portability across:

- explicit authority assignments;
- role-based policy;
- attribute-based policy;
- relationship policy;
- dynamic policy;
- provider IAM;
- external PDPs;
- runtime authorization;
- distributed enforcement;
- combinations of these mechanisms.

Do not make one IAM provider, policy language, RBAC/ABAC paradigm, PDP topology, gateway, or centralized authorization service canonical AE architecture.

# D1 — Core authority definitions

APPROVED.

Use the proposed distinctions:

## Entitlement

A technically enforceable permission/capability available to an authenticated identity within a provider/system.

Entitlement is a technical prerequisite.

It is NOT proof of AE authority.

## Operational Authority — OA

Use:

> **Operational Authority is the effective scoped authority of an actor to perform or request one or more operational canonical AE actions against specified resources/context under applicable conditions.**

OA answers:

> **May this actor perform this operation in this governed work context?**

OA may be established by:

- explicit Authority Assignment;
- authoritative external assignment/reference;
- dynamic policy derivation;
- relationship/task/resource policy;
- another conforming authoritative mechanism.

Do NOT define OA as synonymous with a stored grant.

## Decision Authority — DA

Use:

> **Decision Authority is the effective scoped authority of an actor to make or approve a governed decision of a specified decision class.**

DA answers:

> **May this actor decide this question?**

DA does not itself grant provider execution permission.

## Authority Decision [A2]

Approved as:

> an immutable durable governance record showing that an actor with applicable DA exercised that authority against an exact target/scope/revision.

Authority Decision is an **exercise of DA**.

It is not the DA itself.

## Policy decision

Use:

- PERMIT
- DENY
- INDETERMINATE

Subordinate policy sources may use NOT_APPLICABLE where useful.

## Policy Enforcement Point — PEP

Use:

> **A mechanism at or near a protected boundary that prevents the protected effect from occurring unless applicable authorization requirements are satisfied and that enforces required authorization conditions.**

Preserve:

policy decision
≠
PEP enforcement.

# D2 — Authorization Request Context

APPROVED.

Use a subordinate modular Authorization Request Context [B].

Do NOT create one universally mandatory giant authorization object.

Common core should support as applicable:

- request/correlation identity;
- actor;
- authenticated identity;
- canonical operation;
- target resource/reference;
- organization/Product-System scope;
- evaluation/request time;
- Capability Binding/binding plan;
- applicable Access Path.

Governed-work facts may include when required:

- AE Loop;
- L2 Increment;
- L3 Task;
- Contract exact revision;
- Plan exact revision/review scope;
- Product/System Baseline;
- OEB exact revision;
- Product/System Profile exact revision.

Authority/security facts may include when required:

- provider entitlement;
- OA source/facts;
- DA source/facts;
- Authority Assignment;
- Authority Decision/approval;
- effective policy sources;
- classification;
- environment;
- risk;
- conditions;
- validity;
- delegation;
- revocation.

Preserve:

> **Common authorization semantics; operation-specific required context.**

Approve the subordinate **Authority Requirement [B]** concept so protected operations can declare which authority facts are required without forcing irrelevant facts onto every request.

# D3 / D4 — Effective OA

APPROVED.

OA is effective semantic authority.

It may be:

- explicitly assigned;
- externally authoritative;
- dynamically derived.

Canonical AE requires equivalent meaning and reconstructable authority basis.

It does not require one persistence mechanism.

# D5 — Authority Assignment [A2]

APPROVED WITH A SCOPE REFINEMENT.

Introduce:

**Authority Assignment [A2]**

for cases where authority is explicitly issued, assigned, or delegated as independently meaningful governed authority state.

It may represent:

- Operational Authority Assignment;
- Decision Authority Assignment;
- Delegated Authority Assignment.

The proposed admission reasoning is accepted:

> confusing two assignments can create material authorization, delegation, provenance, and security errors.

Minimum semantics should support as applicable:

- assignment ID;
- authority kind;
- subject/holder;
- issuer/authoritative source;
- operation(s) or decision class(es);
- resource/scope;
- organization/Product-System;
- Loop/task scope;
- conditions;
- valid-from;
- valid-until;
- delegation semantics;
- source assignment when delegated;
- provenance.

Issued assignment history is non-destructive.

Expiration/revocation/supersession does not rewrite what was originally issued.

## Important federation refinement

Do NOT require an AE-owned shadow Authority Assignment record when the authoritative assignment already exists in an external IAM/policy/authority system.

Apply DR-107.

Canonical AE must preserve:

- semantic identity;
- authoritative-source determination;
- exact assignment/reference where required;
- scope;
- validity;
- provenance;
- relationships.

Physical storage may remain external.

An external authoritative assignment may therefore participate through the established External Resource Reference/federated-state mechanisms.

The existence of the canonical Authority Assignment semantic type does not mandate copying every external IAM grant into an AE database.

# D6 — Decision Authority

APPROVED.

Keep DA separate from:

- provider entitlement;
- OA;
- provider write access.

DA supports:

- decision class;
- subject/holder;
- scope;
- limits/conditions;
- effective validity where relevant;
- delegation rules;
- provenance.

# D7 — Canonical Human-reserved versus organization-reserved decisions

APPROVED WITH AN IMPORTANT CONTRACT-FIDELITY GUARDRAIL.

Do NOT silently expand the set of universally Human-reserved decisions beyond the approved Contract / adopted Decision Register.

L1-F must inventory the decisions already explicitly reserved to Human authority by adopted AE semantics.

At minimum this includes the Human authority already established around approved Contract/Contract-change semantics and other explicit Human Owner gates present in the approved Contract/DRs.

If concepts such as:

- material risk acceptance;
- consequential tradeoffs;
- architecture decisions;
- production actions;

are NOT already universally Human-reserved by adopted canonical semantics, do NOT make them universally Human-reserved merely because they sound consequential.

Instead distinguish:

## Canonical Human-reserved Decision Authority

Only decision classes already established by Canonical AE authority.

These cannot be weakened by organization policy.

## Organization-reserved Human Decision Authority

Additional decision classes the organization chooses to reserve based on:

- regulation;
- classification;
- risk;
- safety;
- product criticality;
- architecture governance;
- production impact;
- business policy;
- other context.

This avoids silently changing Contract v1.0.

Precedence remains:

Canonical AE authority constraints
→ Organization authority baseline
→ Product/System specialization
→ Loop/task context.

No silent weakening.

# D8 / D9 — Policy decision versus runtime outcome

APPROVED.

Use policy/authority evaluation:

- PERMIT
- DENY
- INDETERMINATE

Reuse runtime request outcomes:

- ALLOWED
- DENIED
- BLOCKED.

Preserve the semantic distinction:

```text
policy PERMIT
+ required technical prerequisites
+ applicable entitlement
+ applicable enforcement
+ provider operability
→ ALLOWED
```

```text
policy DENY
→ DENIED
```

```text
policy INDETERMINATE
→ BLOCKED
```

Also:

```text
policy PERMIT
+ missing required technical entitlement
→ BLOCKED
```

## Important nuance

Absence of an explicit grant is not automatically INDETERMINATE.

If the authoritative policy model deterministically defines:

`no applicable grant = DENY`

then the result is DENY.

INDETERMINATE is for cases where the required authoritative state cannot be reliably established or resolved.

For protected operations:

> **INDETERMINATE is never permission.**

# Policy obligations / conditions

A PERMIT result may carry enforceable conditions/obligations where needed.

Examples may include:

- restricted environment;
- approval reference;
- time boundary;
- evidence/audit obligation;
- scoped resource constraint.

Do not design a universal obligation DSL.

But ensure the semantic model can carry required conditions from decision to enforcement.

# D10 / D11 — Policy precedence and conflict handling

APPROVED.

Do NOT canonize one universal policy-engine combining algorithm such as global deny-overrides.

Canonical requirements are:

1. Canonical authority constraints cannot be weakened downstream.
2. Organization/Product policy precedence or combination must be deterministic.
3. Product/System specialization may tighten/narrow but not silently weaken mandatory organization controls.
4. Exceptions, where permitted, must be explicit, authorized, scoped, versioned/provenanced, and time/condition bounded where applicable.
5. No unresolved applicable policy conflict may produce PERMIT for a protected operation.

Therefore:

unresolved applicable conflict
→ INDETERMINATE
→ BLOCKED.

# D12 — Least privilege

APPROVED with the proposed refinement:

> **Authority and technical entitlement should use the smallest enforceable scope sufficient to perform the authorized work reliably and safely.**

Scope may include as applicable:

- operation;
- resource;
- Product/System;
- Loop/task;
- environment;
- time;
- conditions.

Do not require absurd one-call/one-token granularity universally.

But broad standing administrator access must not be accepted merely for convenience when meaningfully narrower enforceable authority is available.

# D13 — Validity / expiry / revocation

APPROVED.

Explicitly preserve:

credential lifetime
≠
entitlement lifetime
≠
OA lifetime
≠
DA lifetime.

Authority semantics must support as applicable:

- not-yet-valid;
- active;
- expired;
- revoked;
- superseded;
- invalidated by condition change.

A technically valid credential cannot extend expired/revoked authority.

Credential refresh does not silently extend OA/DA.

Later revocation affects future effective authority.

It does not destructively rewrite historical authorization state.

# D14 — Delegation

APPROVED.

Delegation is optional.

An organization can prohibit delegation and remain conforming.

If delegation exists:

- delegation is explicit;
- delegator is authorized to delegate;
- delegated scope cannot exceed delegable authority;
- operation/decision class/resource/time/conditions remain bounded;
- provenance is retained;
- onward delegation is not allowed unless explicitly permitted;
- Canonical Human-reserved DA cannot be delegated to AI where Canonical AE reserves the decision to Human authority.

Do not build a full delegation language in L1-F.

# D15 — Self-escalation

APPROVED.

Preserve the invariant:

> **An actor may not use the effect of an authority-changing operation to authorize that same authority-changing operation.**

Evaluate the authority-changing mutation using authoritative **pre-change state**.

This applies to attempts to modify as relevant:

- OA assignments;
- DA assignments;
- provider entitlement;
- authority-relevant identity/group/role state;
- policy;
- Capability Bindings;
- OEB/Profile authority configuration;
- Authority Decision/approval state;
- PEP configuration.

A mutation may succeed only when the actor already possesses independently established authority for that mutation.

Likewise:

document appearance
≠
authoritative approval.

An agent-created artifact saying “Human approved” is not an Authority Decision without valid identity, DA, target, source, and provenance.

# D16 — Federated authority state

APPROVED.

Do NOT create a canonical central AE authorization database.

Apply DR-107.

For every material authority fact, the implementation must know its authoritative source.

Examples include:

- authenticated identity;
- provider entitlement;
- OA;
- DA;
- Authority Assignment;
- Authority Decision;
- organization policy;
- Product/System policy;
- revocation state;
- approval state;
- PEP configuration.

Caches/context projections remain derived.

They may not silently become co-authoritative.

When required authority freshness cannot be established within applicable policy:

INDETERMINATE
→ BLOCKED.

# D17 — Authorization evaluation provenance

APPROVED as subordinate B semantics for now.

Do NOT make every runtime authorization evaluation a new A2 record.

However, add this refinement:

> **Authorization provenance retention is risk/operation/policy-sensitive.**

Canonical AE requires enough provenance to reconstruct material protected operations and satisfy applicable Proof/audit needs.

It does NOT require permanent canonical retention of every low-risk authorization check merely because it occurred.

The implementation must define which authorization events require durable provenance based on:

- protected-operation class;
- governance significance;
- risk;
- policy;
- audit/evidence requirements.

Where durable reconstruction is required, the provenance should support as applicable:

- requester/actor;
- authenticated identity;
- canonical operation;
- target/resource;
- Loop/task scope;
- relevant Contract/Plan/OEB revisions;
- entitlement source;
- OA basis/source;
- DA/Authority Decision basis;
- applicable policy sources/revisions;
- effective policy decision;
- required conditions;
- PEP/enforcement point;
- runtime result;
- provider effect reference;
- evidence/provenance.

Never store secret credential material merely for provenance.

# D18 — Distributed enforcement / PEP / bypass path

APPROVED WITH A SCOPE REFINEMENT.

PEPs may be distributed across:

- provider;
- agent/runtime;
- broker;
- gateway;
- SCM;
- CI/CD;
- deployment boundary;
- data/service boundary;
- other protected resources.

No centralized PEP is canonical.

Preserve:

R4
= authority/policy/decision coordination.

R5
= binding/invocation.

PEP
= enforcement.

## Bypass-path invariant

Adopt:

> **Protected-operation Proof must account for materially equivalent bypass paths available to the governed actor through the identities, credentials, Access Paths, and runtime/working context in the declared protected scope.**

If:

```text
governed integration denies operation
```

but:

```text
the same governed actor/runtime can exercise materially equivalent authority through an ungoverned raw credential/interface
```

then enforcement Proof fails unless that alternate path is equivalently governed.

## Important boundary

Do NOT interpret this as requiring proof that:

- no enterprise administrator exists;
- the same Human owns no separate administrator identity;
- no unrelated operational staff can access the resource.

The scope is the **governed actor and the effective identities/credential/access paths available to that actor in the declared execution context**.

This makes the test implementable and avoids accidentally treating legitimate break-glass/admin identities outside the agent's operating context as bypasses.

If an actor can actually switch to another identity within its governed runtime and bypass enforcement, that identity IS relevant to the test.

# Enforcement Proof

For each protected canonical operation/binding, implementation Proof should be able to identify:

- enforcement boundary;
- PEP/mechanism;
- authority/identity facts consumed;
- required obligations/conditions enforced;
- unauthorized-use denial evidence;
- fail-closed behavior when required authority cannot be established;
- materially equivalent bypass-path assessment for the governed actor/scope.

# D19 — OEB / Product-System authority specialization

APPROVED.

An exact OEB revision may identify/reference:

- authoritative identity sources;
- entitlement model/sources;
- OA baseline/policy;
- DA assignments/reservations;
- Human-reserved decision constraints;
- delegation policy;
- authority validity/revocation expectations;
- policy sources;
- policy precedence/combination semantics;
- protected-operation classes;
- PEP/enforcement mappings;
- provenance/audit expectations;
- governed exception mechanisms.

The OEB coordinates these references.

It does not become the IAM/policy engine.

Product/System Profile may tighten/narrow.

It may not silently weaken:

- Canonical Human-reserved authority;
- mandatory organization authority controls;
- mandatory security/governance constraints.

# Issue #6

Keep issue #6 OPEN.

Nothing in L1-F should assume:

- Dev Container;
- IDE;
- Portal;
- CLI;
- local daemon;
- one agent host;
- one policy client.

The authority protocol applies regardless of supported interaction surface.

Access Path remains the L1-E hook.

Preserve:

> **AE should require interface parity, not environment uniformity.**

# D20 — Machine-readable authority semantics / CI

APPROVED.

Continue the staged authority pattern:

Human L1-F semantic artifacts
= normative for meaning.

Machine-readable authority definitions/scenarios
= conforming executable representation.

Python validator
= repository/reference implementation.

GitHub Actions
= repository CI implementation.

Do NOT create a canonical policy language.

The executable model should test canonical authority semantics, not become a production IAM engine.

Create a distinct:

**authority-integrity**

job.

# Authority-integrity coverage

At minimum mechanically test:

## Entitlement / OA separation

```text
entitlement + no OA
→ DENIED
```

```text
OA + missing provider entitlement
→ BLOCKED
```

## Authority determinacy

```text
required authority INDETERMINATE
→ BLOCKED
```

and where authoritative policy explicitly defines absence as denial:

```text
no qualifying authority
→ DENY
→ DENIED
```

## Expiry / revocation

```text
expired OA + still-valid credential
→ not ALLOWED
```

```text
revoked OA + stale cached permit
→ not ALLOWED
```

## Human DA / G5

Test:

- eligible Human approval succeeds;
- AI self-approval fails;
- wrong Human DA scope fails;
- stale Contract Change Proposal fails;
- forged Authority Decision fails;
- G5 target mismatch fails.

Do NOT expand the Canonical Human-reserved decision catalog beyond adopted Contract/DR semantics while building the fixtures.

## Self-escalation

Reject:

- actor granting itself OA;
- actor granting itself entitlement;
- actor modifying authority policy and using resulting authority circularly;
- actor fabricating approval.

Authority-changing operations must be authorized using pre-change state.

## Policy conflicts

Unresolved applicable policy conflict:

→ INDETERMINATE
→ BLOCKED.

## PEP

PERMIT without required enforceable PEP:

→ protected-operation Proof fails.

## Bypass path

Equivalent ungoverned access available to the governed actor/runtime:

→ enforcement Proof fails.

Do not fail merely because an unrelated administrator exists elsewhere.

## Historical integrity

Later revocation does not rewrite the prior historical authorization result.

## Portability

Use at least two materially different synthetic authority implementations.

Example:

Implementation A:
- role/scoped mapping;
- explicit assignment;
- provider entitlement.

Implementation B:
- attribute/resource/task policy;
- dynamic OA;
- external entitlement source.

Semantically equivalent scenarios must produce equivalent canonical:

PERMIT / DENY / INDETERMINATE

and:

ALLOWED / DENIED / BLOCKED.

Do not canonize RBAC or ABAC.

# Issue #12

If `authority-integrity` is created, update the existing issue #12 to track:

- lifecycle-integrity;
- capability-integrity;
- authority-integrity.

Do not create another repository-governance issue unless there is a genuinely different governance problem.

Keep issue #12 OPEN.

Do not claim these jobs are merge-required until repository protection/rules actually enforce them.

Closure Proof remains:

> an intentionally failing applicable integrity check is prevented from merging.

# Decision records

Use the smallest useful decision set.

I agree the likely grouping is approximately:

1. OA / DA / Authority Assignment semantics.
2. Policy evaluation / precedence / validity / self-escalation semantics.
3. Distributed PEP / bypass / authority provenance / OEB coordination.
4. Machine-readable authority model and `authority-integrity` ADR.

Do not create twenty DRs simply because there are twenty decision questions.

# Independent review additions

In addition to the proposed review, explicitly test:

1. Did L1-F accidentally add new universally Human-reserved decision classes beyond the approved Contract/Decision Register?
2. Does Authority Assignment avoid becoming a shadow copy of external IAM?
3. Can externally authoritative OA/DA still satisfy canonical semantics?
4. Can no-grant deterministically mean DENY when policy says so, while genuinely unavailable/ambiguous authority means INDETERMINATE?
5. Can a PERMIT carry required enforceable conditions without creating a policy DSL?
6. Does provenance retain only what is needed by risk/policy rather than generating an audit-record swamp?
7. Does the bypass test apply to the governed actor/runtime identity context rather than every administrator in the enterprise?
8. Can an alternate identity available inside the governed runtime still be detected as a bypass?
9. Can later revocation leave historical authorization truth intact?
10. Can two materially different policy architectures produce equivalent canonical outcomes?

# Durable L1-F artifacts

Proceed with the proposed package:

1. Canonical Authority Model
2. Authorization Request & Requirement Context Model
3. Operational Authority Model
4. Decision Authority Model
5. Authority Assignment Model
6. Policy Evaluation & Precedence Model
7. Delegation / Self-Escalation Guardrails
8. Distributed Enforcement / PEP / Bypass Model
9. Authority Source-of-Truth & Provenance Model
10. OEB / Product-System Authority Specialization
11. Authority / Capability / Lifecycle Relationship Views
12. machine-readable authority definitions/scenarios
13. synthetic authority implementation A/B fixtures
14. authority validator + valid/invalid scenarios
15. authority-integrity CI
16. minimum necessary DRs/ADRs

Do not introduce Kestrel.

Do not design a canonical IAM product or policy language.

Do not solve the detailed developer experience from issue #6.

Do not solve standards applicability.

Do not steal downstream Validation-risk or Context/Memory design.

# GitHub authorization

You now have Human Owner approval to implement L1-F with these refinements.

Proceed:

branch
→ semantic authority artifacts
→ Authority Assignment semantics
→ machine-readable authority scenarios
→ synthetic portability fixtures
→ authority validator
→ authority-integrity CI
→ minimum DRs/ADR
→ update issue #12 if applicable
→ keep issue #6 open
→ independent review
→ correct material findings
→ PR
→ verify available integrity jobs
→ merge.

# L1-F closure report

After merge, report:

- final definitions of entitlement/OA/DA/Authority Decision/policy decision/PEP;
- whether/how Authority Assignment became A2;
- explicit versus dynamically derived authority treatment;
- final Canonical Human-reserved decision treatment;
- authorization request/context model;
- PERMIT/DENY/INDETERMINATE semantics;
- ALLOWED/DENIED/BLOCKED mapping;
- policy precedence/conflict behavior;
- least-privilege semantics;
- time/expiry/revocation behavior;
- delegation model;
- self-escalation protections;
- distributed PEP model;
- bypass-path scope;
- authority source-of-truth/federation model;
- authorization provenance/retention treatment;
- OEB/Product-System authority specialization;
- machine-readable authority artifacts;
- authority-integrity fixture coverage/results;
- portability test across materially different authority models;
- issue #12 status;
- issue #6 status;
- DRs/ADRs created;
- independent-review findings/dispositions;
- PR and merge commit;
- what the next L1 domain inherits;
- the next genuine Human Owner decision gate.

Then stop before beginning the next domain.
