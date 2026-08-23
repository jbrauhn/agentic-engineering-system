# Handoff: L1-L Closure and Part 1 Acceptance Readiness / Fresh-Session Adoption / Independent System Review Prompt

**Repository:** `jbrauhn/agentic-engineering-system`  
**Relay branch:** `ae-session-relay`  
**This branch is coordination-only. Do not merge it into `main`.**

Receiving session: read this file completely before acting, then read `handoffs/README.md`. Verify repository claims independently before relying on them.

This handoff closes the L1 semantic/design sequence through **L1-L — Adoption, Conformance, Distribution & Implementation Readiness** and moves Part 1 into **acceptance-evidence coordination**. Do **not** invent an L1-M merely to continue the letter sequence. If acceptance review reveals a genuine missing Canonical semantic domain or Contract contradiction, surface it to the Human Owner rather than silently adding semantics.

---

# 1. Critical clean-room rule for the receiving session

**You are NOT the fresh-session adoption-test actor.**

By reading this relay you receive prior-system/design knowledge. Therefore your own implementation Plan cannot count as Contract Proof M's fresh-session adoption result.

Your role is **Part 1 acceptance coordinator / independent system reviewer**:

1. verify the candidate distribution and merged system;
2. prepare an exact blind-test package and minimal blind-test instructions;
3. have the Human Owner launch a genuinely fresh Human/agent session that receives only the candidate distribution + supplied OEB/Product baseline;
4. evaluate the blind result against the existing Contract rubric;
5. perform/coordinate independent Part 1 system review from the Contract Proof N perspectives;
6. assemble the Part 1 Proof matrix and unresolved findings;
7. bring the final Proof O acceptance decision to the Human Owner.

Do not contaminate the fresh actor with this relay, prior chat summaries, Kestrel, unpublished design explanation, or repository files outside the assembled distribution and separately supplied baseline.

---

# 2. L1-L closure — authoritative repository state

## PR / merge

- PR: **#20 — Establish L1-L adoption conformance distribution and implementation readiness**
- exact independently reviewed/tested PR head: **`eabd5746c6da08493bc3a57c6e45b177f8eb1afd`**
- merged: **YES**
- merge commit on `main`: **`0ec9d294960cd591296df955baceb6d2229e61ce`**
- base before L1-L: `f18aa538bb76134aa8a045a074dae7f02ed7c48e`

Verify `main` before starting acceptance work.

## L1-L semantic / adoption artifacts merged

- `L1-L_ADOPTION_DISTRIBUTION_CONFORMANCE_MODEL.md`
- `L1-L_STARTER_PACK_BOOTSTRAP_INTERFACE_MODEL.md`
- `L1-L_REFERENCE_ADOPTION_PROOF_MODEL.md`
- `L1-L_RELATIONSHIP_VIEWS.md`
- `START_HERE.md`
- `ADOPTION_STARTER_PACK.md`
- `SYSTEM_RATIONALE.md`

## Decisions merged

- `DR-136-release-authority-starter-pack-and-interface-parity.md`
- `DR-137-validation-backed-scoped-conformance-and-proportional-reassessment.md`
- `DR-138-integrated-synthetic-adoption-and-clean-room-reference-proof.md`
- `ADR-010-machine-readable-adoption-distribution-and-integrity.md`

## Machine / reference integration artifacts merged

- `canonical_ae_release_manifest.json`
- `adoption_distribution_protocol.json`
- `adoption_scenarios.json`
- `adoption_portability_fixtures.json`
- `synthetic_organization_fixture.json`
- `clean_room_adoption_baseline.json` — supplied test input; explicitly excluded from assembled distribution
- `reference_ae_loops.json`
- `assemble_distribution.py`
- `run_clean_room_adoption.py`
- `validate_adoption.py`
- `.github/workflows/adoption-integrity.yml`

A small repository-CI integration change also updates `.github/workflows/observability-learning-integrity.yml` so L1-L/adoption-protocol changes trigger that inherited regression suite.

---

# 3. Final L1-L semantics

## Release/distribution authority

The existing **Canonical AE Release Manifest `[F]`** is the release authority object. Current candidate manifest on `main`:

- `release_id`: **`CAE-P1-CANDIDATE-2026-08-23`**
- `release_version`: **`part1-candidate-2026.08.23`**
- status: **`CANDIDATE_PENDING_HUMAN_OWNER_PART1_ACCEPTANCE`**

Three Contract semantic layers remain distinct:

1. **CANONICAL_CORE** — normative, subject to artifact status/decision precedence;
2. **ADOPTION_STARTER_PACK** — conforming implementation aid;
3. **EXECUTABLE_REFERENCE_LAYER** — conforming/reference behavior, non-normative and technology-replaceable.

`SYSTEM_RATIONALE.md` is packaged separately as **canonical explanatory/non-normative supporting content**. It is not detailed decision authority.

The Field Guide remains explanatory only and is not Canonical authority.

### Reference integrity

`assemble_distribution.py` builds an exact packaged payload and writes `RELEASE_INVENTORY.json` with per-artifact **SHA-256** digests.

SHA-256, Git/GitHub, JSON, Python, repository paths, package layout, and signing technology are reference implementation choices, not Canonical AE requirements. Canonical requirement is verifiable exact payload identity/provenance.

The candidate package explicitly excludes:

- `clean_room_adoption_baseline.json`;
- prior conversation;
- unpublished design context;
- previous session memory;
- relay handoff state.

## Starter Pack

`START_HERE.md` lets a fresh adopter discover:

- what AE is;
- exact release;
- what is authoritative;
- what is Starter/template guidance;
- what is reference/example only;
- required supplied baseline inputs;
- how to derive a normal implementation Plan;
- how adoption/conformance is proven;
- where rationale/decisions/experiments/learning live.

`ADOPTION_STARTER_PACK.md` guides establishment/use of existing canonical identities:

- OEB;
- Product/System Profile + Baseline;
- AE Implementation Profile;
- Capability Bindings/readiness/gaps;
- identity/entitlement/OA/DA/policy/enforcement;
- standards/practices applicability;
- architecture anchors;
- Context Requirements / Bootstrap Descriptor / durable knowledge;
- Evidence/Validation expectations;
- Engineering Health Findings;
- derived capability/health/bootstrap/readiness views;
- normal `Plan [A1]`;
- installation/adoption Proof.

No `Adoption Project`, `Adoption Plan`, `Installation Record`, `Conformance Claim`, `Environment Profile`, `Interface Profile`, `Capability Gap Record`, `Health Assessment`, or special adoption Validation identity was added.

## Candidate → Conforming

Organization-specific AE Implementation:

- starts **Candidate**;
- becomes **Conforming** only through applicable independent existing `Validation Record [A2]` semantics;
- Validation must target exact declared scope and exact relevant Release/OEB/Profile/Baseline/AE Implementation Profile/Binding/governance revisions;
- conformance status is derived `[D]` projection, not an editable authoritative boolean;
- provider install success, CI green, deployment success, dashboard state, tool availability, or Human clerical confirmation do not create conformance;
- scoped/partial conformance requires explicit scope, exclusions and limitations;
- conformance is not external certification unless a separate certification regime actually proves that claim.

Historical conformance/Validation remains immutable. Later material release/baseline/binding/policy/interface/standards/Evidence change may move current reliance to `NEEDS_REASSESSMENT` but does not rewrite history. Reassessment is proportional.

## Bootstrap / interface parity

L1-L reuses the existing L1-G `Bootstrap Descriptor [B]` and Context Requirements.

Canonical principle now established:

> **Equivalent Canonical operations and governed state must be reachable; identical environment implementation is not required.**

For each declared supported actor/runtime environment class, required agent-accessible operations need a governed, deterministic, discoverable, proven Access Path.

A missing interface/access path is represented through existing capability/readiness/gap semantics as `BLOCK`, `CONSTRAIN`, or `DEGRADE` for the affected scope. It is not normally repaired with a Human clerical proxy.

No mandatory Portal, CLI, IDE, MCP topology, Dev Container, daemon, agent host, local runtime, or Environment Profile was introduced.

---

# 4. Issue #6 is CLOSED

Issue **#6 — Engineering Team Interface / Working Environment — interface parity across heterogeneous development environments** is now **CLOSED / completed**.

Reason:

- exact PR head `eabd574…` passed all nine suites;
- `adoption-integrity` proved two materially different developer/agent environment/access topologies:
  - containerized terminal + CLI/agent runtime;
  - remote cloud workspace + IDE/broker/API;
- the implementations also differ materially in SCM, CI, Work Management, IAM/policy, observability and knowledge topology;
- they resolve equivalent Canonical Release/OEB/Profile/Baseline/work scope/operations/authority/Validation semantics;
- missing interfaces correctly become Capability/readiness gaps;
- no environment uniformity or Human mechanical intermediary was needed.

A resolution comment was added to issue #6 before closing it. Future Portal/CLI/IDE/UX/bootstrap-product improvements are implementation/product work, not the now-closed broad Canonical semantic question.

---

# 5. Issue #12 remains OPEN

Issue **#12 — Repository governance — require applicable integrity checks before main merge** remains **OPEN**.

It now tracks **nine** meaningful integrity jobs:

1. lifecycle-integrity
2. capability-integrity
3. authority-integrity
4. context-integrity
5. planning-execution-integrity
6. validation-integrity
7. standards-health-integrity
8. observability-learning-integrity
9. adoption-integrity

All nine passed on the exact reviewed L1-L PR head.

However `main` branch protection/ruleset enforcement is still **OFF / unproven**. Therefore successful checks are evidence but are not repository-enforced merge gates.

Issue #12 closure condition remains:

1. configure repository rules so applicable integrity checks are required before main merge; and
2. prove enforcement with an intentionally failing applicable check that the repository actually prevents from merging.

This is repository governance, not a Canonical requirement to use GitHub Actions or GitHub branch protection.

Acceptance review must decide whether issue #12 is:

- a blocker that should be remediated before final Part 1 acceptance; or
- a material repository-governance finding that the Human Owner explicitly accepts/routes to future governed work.

Do not silently ignore it.

---

# 6. L1-L executable evidence

## Exact reviewed head

`eabd5746c6da08493bc3a57c6e45b177f8eb1afd`

## All nine workflows succeeded

On that exact head:

- Lifecycle Integrity — success
- Capability Integrity — success
- Authority Integrity — success
- Context Integrity — success
- Planning Execution Integrity — success
- Validation Integrity — success
- Standards Health Integrity — success
- Observability Learning Integrity — success
- Adoption Integrity — success

## Adoption Integrity

Exact PR-head run/job:

- workflow run: **32640348301**
- job: **97196370553**

Evidence from the log:

- assembled **172 artifacts** into the exact candidate distribution;
- created a SHA-256 inventory;
- copied the supplied clean-room baseline outside the repository;
- executed `/tmp/ae-distribution/run_clean_room_adoption.py` from `/tmp/clean-room-run`;
- derived `PLAN-CLEANROOM-BETA@1` from distribution + supplied baseline only;
- passed **67 semantic scenarios**;
- passed **4 portability cases**;
- passed distribution integrity;
- passed integrated happy-path AE loop;
- passed controlled Replan/backward path with non-destructive history;
- passed governed Engineering Health remediation;
- passed direct-agent Work Management allow/deny requirements;
- passed bootstrap/interface parity;
- passed clean-room rubric mechanics.

## Synthetic organization

`SYNTH-ORG-ALPHA` is deliberately imperfect and Kestrel-free.

It contains:

- healthy Source Control / CI/CD / Work Management / Knowledge / Validation examples;
- Work Management allowed in-scope agent operation and denied out-of-scope operation;
- Observability technically available but agent query access missing → `CONSTRAIN`;
- Models technically available but only broad administrator credential / no appropriate scoped entitlement → `BLOCK`;
- Engineering Health Finding `EHF-SYNTH-1`: high change amplification + incomplete architecture decision history → `DEGRADE`;
- Human Owner DA for Contract/material risk;
- two supported environment classes.

## Reference loops

1. Happy path:
   Loop Context → Contract → architecture-aware Plan → Plan Review → readiness/authority → bounded Execution → Verification/Evidence → independent Validation → Accept → learning disposition.

2. Controlled backward path:
   failed Validation → `REPLAN`; old Validation/Plan/review preserved; new Plan revision + review + Execution/Validation → Accept.

3. Health remediation:
   Engineering Health Finding → normal Plan/Increment/Task → Evidence → independent Validation → later current disposition `REMEDIATED`; original Finding remains immutable.

---

# 7. Independent L1-L review findings corrected

The independent PR review recorded these material corrections before merge:

### Finding 1 — System Rationale authority over-classified

Initial manifest placed `SYSTEM_RATIONALE.md` under a uniformly normative Core selector even though the file correctly says it is explanatory navigation.

Correction:
- remove it from normative Core selector;
- package as `SUPPORTING_SYSTEM_RATIONALE` with canonical explanatory/non-normative authority;
- Core remains normative subject to artifact status/precedence.

### Finding 2 — relay state leaked through provenance reference

Initial manifest pointed to the Human Owner relay handoff as packaged provenance.

Correction:
- remove the coordination-only relay pointer;
- package provenance now references DR-136/137/138 + ADR-010;
- clean-room distribution does not depend on relay/session state.

### Finding 3 — clean-room working-directory isolation under-proved

Initial deterministic actor read only explicit inputs but executed from the repository working directory.

Correction:
- assemble distribution to `/tmp/ae-distribution`;
- copy supplied baseline to `/tmp/clean-room-input`;
- execute actor from `/tmp/clean-room-run` using only those explicit paths.

### Finding 4 — no explicit leak assertion

Correction:
- validator now fails if `clean_room_adoption_baseline.json` exists inside the assembled distribution;
- validator fails if any `handoffs/` path appears in the packaged inventory.

### Finding 5 — inherited observability suite path-filtered out

The first L1-L PR head ran eight suites; Observability Learning did not run because its PR path filter did not match L1-L-only changes.

Correction:
- no meaningless semantic edit was made;
- `.github/workflows/observability-learning-integrity.yml` now treats `L1-L_*` and `adoption_distribution_protocol.json` as cross-domain triggers;
- exact final head reran and passed **all nine** suites.

No Contract contradiction emerged. No new A1/A2 identity was warranted.

---

# 8. Clean-room honesty boundary — still important

The deterministic L1-L clean-room harness proves:

- exact candidate distribution assembly;
- baseline exclusion from the package;
- isolated distribution+baseline-only execution boundary;
- exact-reference reconstruction;
- Capability vs Engineering Health gap reasoning;
- normal Plan derivation;
- Evidence/Validation design;
- Contract Proof M rubric mechanics.

It does **not** prove that a genuinely fresh external Human/model/provider, ignorant of the system, can independently discover and use the distribution correctly.

Contract Proof M specifically requires a **fresh implementation/planning session** receiving only:

1. the published Canonical AE distribution; and
2. supplied OEB + Product/System Profile/baseline.

Therefore final acceptance evidence still needs a genuinely fresh external run.

---

# 9. Remaining Part 1 work — acceptance evidence, not L1-M

The semantic system is now materially covered by L1-A through L1-L.

The next phase is:

## **Part 1 Acceptance Readiness**

Primary unresolved Contract Proof areas:

### Proof A — versioned published distribution

The candidate manifest and assembly mechanism exist and are merged.

Acceptance coordinator should produce/identify a concrete exact candidate payload for blind testing (for example an assembled ZIP + SHA-256 inventory generated from merge commit `0ec9d294…`). Do not require GitHub as a Canonical mechanism.

### Proof B — completeness/coherence

L1-A–L and all nine suites strongly support this, but final independent system review should check cross-domain completeness/coherence rather than assume it.

### Proof C — machine-verifiable integrity

Nine jobs exist and function. Repository enforcement is still issue #12.

### Proof D–L — reference behavior

L1-L integrated reference evidence now materially covers:

- D happy path;
- E backward path;
- F synthetic imperfect organization;
- G capability-operation/entitlement assessment;
- H Work Management direct-agent allow/deny;
- I portability;
- J Capability-gap detection;
- K Engineering-health detection;
- L governed agent-assisted remediation.

Acceptance reviewer should verify the evidence is sufficient against the exact Contract wording, not merely trust this relay.

### Proof M — reproducible fresh-session adoption test

**Still needs a genuinely fresh external Human/agent run.**

### Proof N — independent system review

Still needs explicit Part 1 review from relevant perspectives including:

- adopting organization;
- architecture;
- Planning;
- Execution;
- Validation;
- governance/security;
- portability;
- implementation-team usability;
- future product/client use.

Material findings must be resolved, accepted by appropriate authority, or converted into governed future work.

### Proof O — Human Owner acceptance

Not yet granted.

Final Part 1 acceptance remains a Human Owner Decision Authority action after assembled Proof A–N.

---

# 10. Recommended next-session sequence

## Phase A — verify candidate state

1. Verify `main == 0ec9d294960cd591296df955baceb6d2229e61ce` or understand any later changes.
2. Verify PR #20 and exact reviewed head evidence.
3. Verify issue #6 is closed/completed.
4. Verify issue #12 remains open and branch protection status.
5. Read Contract Proof A–O directly.

## Phase B — create exact blind-test package

Create an exact candidate distribution from the merged L1-L state using `assemble_distribution.py`.

Prefer producing a single transportable package such as:

- `Canonical_AE_Part1_Candidate_2026-08-23.zip`
- containing the assembled distribution + `RELEASE_INVENTORY.json`;
- **NOT containing** `clean_room_adoption_baseline.json`.

Record the ZIP/payload SHA-256 in acceptance Evidence.

Separately package/export the supplied blind-test baseline (`clean_room_adoption_baseline.json`) as the second input.

Do not place this relay or hidden acceptance instructions inside the clean-room distribution.

## Phase C — prepare minimal blind-test instruction

The blind actor should receive only:

1. assembled candidate distribution;
2. supplied OEB/Product baseline;
3. a minimal task instruction equivalent to:

> Using only the supplied Canonical AE distribution and supplied organization/product baseline, derive a credible organization-specific AE implementation Plan. Do not use prior knowledge or external unstated AE semantics. Identify required capability bindings, agent-access/entitlement/authority needs, Capability gaps vs Engineering Health gaps, implementation work, Evidence/Validation strategy, and traceability. State any ambiguity or missing information rather than inventing hidden semantics.

Do **not** send the blind actor this relay, prior conversation, historical summaries, Kestrel, or an answer key.

The Human Owner should launch this in a genuinely fresh independent session/model context.

## Phase D — evaluate Proof M

After the Human Owner returns the blind actor's Plan/output, independently score it against the existing eight dimensions:

1. Canonical semantic fidelity;
2. baseline comprehension;
3. Capability Binding completeness;
4. agent-access/entitlement correctness;
5. gap reasoning;
6. implementation credibility;
7. Evidence/Validation design;
8. traceability.

Do not grade for stylistic conformity. Grade semantic/implementation correctness.

A failure in any rubric dimension requires correction/Replan/disposition; it is not silently passed because the deterministic harness succeeded.

Store/record:

- exact distribution identity/hash;
- exact baseline identity/hash;
- blind actor/session/model identity where appropriate;
- minimal prompt;
- raw Plan/output or durable reference;
- independent rubric evaluation;
- findings/disposition.

## Phase E — Proof N independent system review

Perform or coordinate explicit independent review of the assembled Part 1 System from every required perspective.

Recommended output is one consolidated review matrix with:

- perspective;
- Contract/semantic scope reviewed;
- strengths/evidence;
- material finding;
- severity/impact;
- required disposition;
- responsible authority;
- evidence of resolution/acceptance/future-work routing.

Important review tests:

- Can an adopting organization actually start without hidden knowledge?
- Is the architecture coherent across R1–R7 and L1-A–L?
- Do Planning/Execution remain usable rather than over-process-heavy?
- Is Validation truly independent where required?
- Can governance/security fail closed without making routine work unusable?
- Does portability survive materially different providers/environments/models?
- Is Starter Pack usable by an implementation team without inventing core method?
- Could a future Portal/client use these semantics without becoming a hidden mandatory runtime?
- Are the nine integrity domains coherent, or are there cross-domain contradictions?
- Does issue #12 materially undermine the candidate release or represent an acceptable repository-level future governance item?

## Phase F — assemble Part 1 Proof matrix

Create durable acceptance evidence mapping every Contract Proof item A–O to:

- status: PROVEN / PARTIAL / OPEN / ACCEPTED_RISK / NOT_APPLICABLE if legitimate;
- exact Evidence/ref;
- independent review result;
- unresolved finding;
- required Human decision.

Do not create a new Canonical A1/A2 merely for this acceptance matrix unless DR-108 genuinely requires it. It can be repository release/review Evidence/reference material.

## Phase G — Human Owner gate

When A–N are adequately proven/dispositioned, present the Human Owner a concise acceptance package:

1. exact release candidate identity/hash;
2. Proof A–O summary;
3. fresh-session adoption result;
4. independent system review findings/dispositions;
5. issue #12 decision;
6. any remaining accepted risks/future work;
7. one explicit decision:
   - **ACCEPT Part 1**, or
   - **DO NOT ACCEPT / require stated corrections**.

Do not self-approve Proof O.

---

# 11. Issue #12 decision is a real acceptance-review question

The repository currently permits merge without enforced required checks even though nine semantic integrity workflows exist.

Leading acceptance-review options:

### Option A — fix before Part 1 acceptance

Configure main protection/ruleset and prove a deliberately failing applicable integrity check is blocked from merge.

Advantage: repository governance matches the engineering discipline demonstrated by the Canonical System.

Potential constraint: current connector may still not expose branch protection/ruleset mutation. If tooling cannot configure it, do not fabricate enforcement.

### Option B — Human Owner explicitly accepts/routes as repository-level follow-on

Contract C requires machine-verifiable checks to exist and function; it does not explicitly require GitHub branch protection. If all checks are proven functional, the Human Owner may decide issue #12 is a repository-governance improvement rather than a Canonical Part 1 blocker.

If so, record that decision explicitly. Do not close issue #12 unless its own closure condition is actually met.

The receiving acceptance coordinator should recommend, not silently decide, this tradeoff.

---

# 12. Entity discipline during acceptance

Do not create:

- Part1AcceptanceProject `[A1]`;
- AcceptanceTest `[A1/A2]`;
- AcceptanceClaim `[A2]`;
- FreshSessionTest entity;
- ReviewPerspective entity;
- ProofMatrix entity;
- ReleasePackage entity merely for convenience.

Use existing Evidence/Validation/Decision semantics where canonical identity matters and ordinary repository/release/review artifacts where a derived/documentary representation is sufficient.

Final Human Owner Part 1 acceptance should be recorded through existing Human Decision / Decision Record semantics if/when approved.

---

# 13. Do not reopen these settled L1-L semantics absent a contradiction

- Release Manifest `[F]` is existing release authority object.
- Three semantic layers remain Core / Starter / Reference.
- System Rationale is explanatory/non-normative navigation.
- Starter Pack does not redefine Core.
- Candidate → Conforming is existing independent Validation semantics.
- Conformance projection is derived, scoped and exact-revision-backed.
- No silent rebase; historical Validation immutable; reassessment proportional.
- Bootstrap Descriptor `[B]` is reused.
- Interface parity, not environment uniformity.
- Issue #6 broad Canonical question is closed.
- Capability gaps distinct from Engineering Health Findings.
- Normal Plan `[A1]` used for adoption implementation.
- No special adoption lifecycle or Validation ontology.
- No new L1-L A1/A2.
- No Kestrel in generic Part 1.
- Final Part 1 acceptance belongs to Human Owner.

---

# 14. Current known repository concerns

- **Issue #6:** CLOSED / completed after L1-L interface-parity Proof.
- **Issue #12:** OPEN; nine checks are operational but not branch-protection-required.
- `main` was still unprotected at L1-L merge time.
- No L1-M branch/PR existed at closure.
- Candidate Release status remains `CANDIDATE_PENDING_HUMAN_OWNER_PART1_ACCEPTANCE`.

Do not change candidate status to final/accepted until Human Owner Proof O approval.

---

# 15. Next genuine Human Owner decision gates

The next meaningful Human Owner decisions are not new L1 semantics.

They are:

1. **How to disposition issue #12 for Part 1 acceptance:** fix before acceptance vs explicitly accept/route as repository-level follow-on.
2. **Whether the genuinely fresh external adoption result passes Contract Proof M.**
3. **Disposition of any material Proof N independent-review findings.**
4. **Final Proof O: accept or reject Part 1.**

Package those decisions concisely when they are ready. Do not require the Human Owner to re-read the entire design history.

---

# 16. Relay close-out rule

When this acceptance-readiness session completes its work:

- write the complete next handoff to a NEW unique file under `handoffs/` on `ae-session-relay`;
- do not overwrite this file;
- do not merge `ae-session-relay` to main;
- Human-facing response should be only a short status summary + exact handoff block.

If the next step requires the Human Owner to launch the blind fresh-session agent manually, the next handoff should contain the acceptance coordinator state, and the Human-facing message should additionally provide the **minimal blind-test copy/paste instruction and exact files/package to supply**, while preserving the rule that the blind agent must not receive this relay.