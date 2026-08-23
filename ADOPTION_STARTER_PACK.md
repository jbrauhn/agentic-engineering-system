# Adoption Starter Pack

**Role:** conforming reusable guidance/template. This file does not redefine Canonical Core.

## 1. Supplied baseline

Record exact references:

- Canonical AE Release: `<release-id>`
- OEB: `<logical-id>@<exact-revision>`
- Product/System Profile: `<id>@<revision>` or N/A
- Product/System Baseline: `<id>@<revision>` or N/A
- target implementation scope: `<scope>`

## 2. AE Implementation Profile [A1]

Declare, without claiming conformance:

- implementation profile ID/revision;
- exact Canonical Release;
- declared organization/product/resource scope;
- exact OEB/Product/Baseline refs;
- selected Capability Bindings/config references;
- authority/policy/standards/context references;
- supported actor/runtime environment classes;
- current state: `Candidate` until applicable Validation proves otherwise.

## 3. Capability Bindings and gaps

For each required canonical operation, resolve:

- Binding revision;
- provider/mechanism;
- declared scope;
- deterministic Access Path(s);
- supported actor/runtime classes;
- SUPPORTED / BOUND / DISCOVERABLE / REACHABLE / ENTITLEABLE / ENFORCEABLE / PROVEN Evidence;
- runtime entitlement/OA/PEP needs;
- deficiency and `BLOCK / CONSTRAIN / DEGRADE / NONE` impact where not ready.

Keep Capability gaps distinct from Engineering Health Findings.

## 4. Authority/policy/enforcement

Reference authoritative identity/entitlement sources, OA/DA sources, applicable Human-reserved decisions, policy sources/precedence, PEPs, least-privilege expectations, revocation/currentness, and exception mechanisms.

## 5. Standards/practices

Determine applicable mandatory/conditional/advisory/reference standards and exact/effective revisions. Record why/where they apply, Evidence expectations, any authorized exception/waiver, and proportional omission reasoning where applicable.

## 6. Architecture

Reference the durable Architecture Model/Baseline and identify required context/boundaries/responsibilities/dependencies/decisions the implementation and normal Plans must use.

## 7. Context/bootstrap/knowledge

Instantiate/reuse Bootstrap Descriptor and Context Requirements so each supported Human/agent environment can resolve the exact Release, baselines, work scope, authority, capabilities, policies, Validation/Evidence interfaces, durable state and Handoff/reconstruction path.

Missing agent interface/access is a capability/readiness gap, not a standing Human clerical step.

## 8. Evidence and Validation

Define adoption Validation Requirements for exact implementation scope and revisions. Identify required Evidence for:

- binding usability/agent access;
- allowed and denied operations;
- authority/PEP behavior;
- context/bootstrap/reconstruction;
- reference loop behavior;
- gap/remediation behavior;
- portability where claimed.

Independent `Validation Record [A2]` establishes adoption/conformance; provider state does not.

## 9. Engineering Health

Assess underlying conditions contextually. Create `Engineering Health Finding [A2]` only for material durable findings. Keep current health/gap reporting derived. Route selected remediation through normal AE work and independently Validate it.

## 10. Derived gap views

Produce reconstructable views of:

- Capability gaps;
- Engineering Health gaps;
- bootstrap/interface gaps;
- outstanding adoption Proof.

Views are not authority and must reference source records.

## 11. Derive the normal implementation Plan [A1]

The Plan should include, as applicable:

- exact Canonical release/baseline refs;
- Capability Bindings/gaps;
- agent access/entitlement/enforcement needs;
- bootstrap/interface readiness;
- authority/policy;
- standards/applicability;
- architecture impacts/anchors;
- context/knowledge integration;
- Evidence/Validation strategy;
- health remediation;
- L2/L3 implementation work, dependencies and parallelism;
- acceptance Proof;
- Planning Depth/Method and allowed adaptation boundaries.

Use normal Plan Review, Execution, Verification/Evidence and Validation semantics. There is no Adoption Plan type.

## 12. Adoption acceptance

After implementation/reference work, issue independent adoption Validation against the exact target. Only applicable accepted Validation supports a Conforming projection. Final Part 1 System acceptance remains a Human Owner decision, separate from one organization installation's conformance.
