# START HERE — Canonical Agentic Engineering System

## What is AE?

The **Agentic Engineering System** is a portable, governed socio-technical engineering system for Human–AI engineering. It defines how intent moves through Contract, architecture-aware Planning, bounded Execution, Evidence, independent Validation, and Learning while preserving Human Decision Authority and engineering discipline.

## What release is this?

Read `canonical_ae_release_manifest.json` first. It identifies the exact Part 1 release representation and classifies distribution content by authority.

**Part 1 has been accepted by the Human Owner.** The Human Decision is durably recorded in `part1_acceptance_authority_decision_20260824.json` against the exact accepted source/payload basis. The historical release ID/version retain their candidate-era labels; the manifest's current `release_status` and the Authority Decision record establish the accepted state.

Distribution revision 3 records that accepted state and current release-facing wording without changing Canonical Core semantics. Part 1 acceptance is not external certification, and it does not make any organization-specific implementation automatically Conforming.

## What is authoritative?

Authority flows from:

1. `CONTRACT.md`;
2. approved Decision Records / ADRs within their scope;
3. Human semantic `L1-*.md` artifacts.

Human governance decisions such as Part 1 acceptance are represented by applicable durable Authority Decision records. Starter templates and executable/reference artifacts must conform to Canonical semantics and cannot override them. The Field Guide and generated views are explanatory, not Canonical authority.

## What is Starter/template/guidance?

Use `ADOPTION_STARTER_PACK.md` to establish the organization/product inputs and derive a normal organization-specific `Plan [A1]`.

## What is reference/example only?

JSON protocols, Python validators, GitHub Actions workflows, synthetic fixtures, reference loops, clean-room harnesses and provider examples demonstrate one conforming implementation approach. Their technology choices are replaceable.

## What baseline must I supply?

At minimum, establish or supply enough information to resolve:

- OEB exact revision;
- Product/System Profile and Baseline where applicable;
- organization technology/capability environment;
- identity, entitlement, authority and policy context;
- standards/practices context;
- architecture expectations;
- context/knowledge sources;
- Evidence/Validation expectations;
- material constraints and known engineering conditions.

## How do I derive an implementation Plan?

Use the Starter Pack sections to map Canonical Capability Contracts to organization providers/access paths, identify capability and Engineering Health gaps separately, define authority/interface/context readiness, and produce a normal reviewed `Plan [A1]` with Evidence and adoption Validation strategy.

## How do I prove adoption/conformance?

An organization-specific implementation is **Candidate** until independent adoption Validation evaluates the exact release, declared scope, exact OEB/Product/Profile/Binding revisions and sufficient Evidence. Provider installation success or a manual `conforming=true` flag is not conformance.

## Where are rationale, decisions, experiments and learning?

- `SYSTEM_RATIONALE.md` — concise evolution/rationale navigation and current-state clarification.
- `DR-*.md` / `ADR-*.md` — authoritative detailed decision history.
- `part1_acceptance_authority_decision_20260824.json` — durable Human Owner Part 1 acceptance Authority Decision.
- `L1-K_EXPERIMENT_MODEL.md` / Learning semantics — experiment/learning model.

## Implementation-team first actions

1. Verify the release manifest/inventory.
2. Read the Contract and this START HERE.
3. Instantiate the Starter Pack against your OEB/Product baseline.
4. Resolve bootstrap/interface access from your normal engineering environments.
5. Derive and independently review the normal implementation Plan.
6. Implement bindings/gaps using governed AE work.
7. Run reference/adoption Proof and independent installation Validation.
