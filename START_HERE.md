# START HERE — Canonical Agentic Engineering System

The **Agentic Engineering System (AE)** is a portable, governed socio-technical engineering system for Human–AI engineering. It defines how intent moves through Contract, architecture-aware Planning, bounded Execution, Evidence, independent Validation, and Learning while preserving Human Decision Authority and engineering discipline.

## 1. Confirm the release

Start with the **[Canonical AE Release Manifest](canonical_ae_release_manifest.json)**. It identifies the exact Part 1 release representation, distribution revision, authority layers, and distribution selectors.

Part 1 has been accepted by the Human Owner. The durable decision is **[Part 1 Acceptance Authority Decision](canonical/governance/part1_acceptance_authority_decision_20260824.json)**. The historical release ID/version retain their candidate-era labels; the manifest's current `release_status` plus the Authority Decision establish the accepted state.

The current repository representation is **distribution revision 4**. Revision 4 reorganizes repository paths for human/agent navigation; it does not redefine Canonical Core semantics or replace the exact Human-accepted revision-2 basis.

## 2. Understand what is authoritative

Read these in order:

1. **[Contract](canonical/CONTRACT.md)** — governing Goal / Spec / Proof and Part 1 acceptance boundary.
2. **[Level 1 Canonical domains](canonical/level-1/)** — human-readable Canonical semantics, organized as L1-A through L1-L.
3. **[Decision Records](canonical/decisions/dr/)** — durable Canonical design decisions and rationale within their scope.
4. **[Architecture Decision Records](canonical/decisions/adr/)** — machine-readable/reference architecture decisions; selected technologies do not become Canonical merely because an ADR uses them.

The letters **A–L are Level 1 semantic design domains**, not Contract clause numbers and not sequential runtime stages. For a topic-by-topic map, use the **[Repository Map](docs/REPOSITORY_MAP.md)**.

For explanatory context, read **[System Rationale](docs/SYSTEM_RATIONALE.md)**. It is useful orientation, but it is not a substitute for Canonical authority.

## 3. If you are adopting AE in an organization

Use the **[Adoption Starter Pack](adoption/ADOPTION_STARTER_PACK.md)** to establish organization/product inputs and derive a normal organization-specific `Plan [A1]`.

The most useful Canonical areas during adoption are:

- **[L1-E — Capabilities and OEB](canonical/level-1/E/)** — Canonical capability contracts, bindings, readiness, gaps, and organization engineering baseline semantics.
- **[Ten Canonical Capability Contracts](canonical/level-1/E/L1-E_TEN_CANONICAL_CAPABILITY_CONTRACTS.md)** — the ten capability families every implementation must account for.
- **[L1-F — Authority, Policy, and Enforcement](canonical/level-1/F/)** — identity, entitlement, Operational Authority, Decision Authority, policy evaluation, and enforcement.
- **[L1-G — Knowledge, Context, Memory, and Bootstrap](canonical/level-1/G/)** — context reconstruction, durable state, handoff, and environment-independent bootstrap.
- **[L1-H — Planning and Execution Coordination](canonical/level-1/H/)** — Plan semantics, progressive elaboration, readiness, work topology, and execution coordination.
- **[L1-I — Evidence and Validation](canonical/level-1/I/)** — evidence sufficiency and independent Validation.
- **[L1-J — Standards and Engineering Health](canonical/level-1/J/)** — standards applicability and Engineering Health Findings, kept distinct from Capability gaps.
- **[L1-L — Adoption, Distribution, and Conformance](canonical/level-1/L/)** — adoption, interface parity, bootstrap, release distribution, and Validation-backed conformance.

At minimum, an adopter must be able to resolve the exact OEB revision, Product/System Profile and Baseline where applicable, capability/provider environment, identity/entitlement/authority/policy context, standards context, architecture expectations, context/knowledge sources, Evidence/Validation expectations, and material constraints or known engineering conditions.

## 4. Reference implementation and executable proof

Reference artifacts demonstrate one conforming implementation approach; they do **not** override the Canonical Core.

- **[Protocols](reference/protocols/)** — machine-readable protocol/reference models.
- **[Canonical Capability Contracts — machine-readable reference](reference/protocols/capability_contracts.json)**.
- **[Scenarios](reference/scenarios/)** — positive and negative semantic fixtures.
- **[Fixtures](reference/fixtures/)** — portability, synthetic organization, and clean-room inputs used by the reference layer.
- **[Reference loops](reference/loops/reference_ae_loops.json)** — integrated happy-path, backward-route, and remediation examples.
- **[Validators](reference/validators/)** — machine-verifiable integrity checks.
- **[Integrity workflows](.github/workflows/)** — CI execution of the integrity domains.
- **[Distribution assembler](tools/assemble_distribution.py)** — assembles the versioned distribution selected by the manifest.
- **[Clean-room adoption harness](tools/clean-room/run_clean_room_adoption.py)** — reference clean-room adoption execution.

The reference layer is replaceable. GitHub, Python, JSON, and these specific workflow mechanisms are not required Canonical AE technologies.

## 5. How adoption/conformance is proven

An organization-specific AE implementation begins **Candidate**. It becomes Conforming only when independent adoption Validation evaluates the exact Canonical release, declared scope, exact governing revisions, implemented capability bindings, authority/policy/enforcement, and sufficient Evidence.

Provider installation success, a green CI job, or a manually asserted `conforming=true` value is not conformance.

## 6. First actions

1. **[Verify the release manifest](canonical_ae_release_manifest.json)** and the inventory produced by the **[distribution assembler](tools/assemble_distribution.py)**.
2. Read the **[Contract](canonical/CONTRACT.md)** and browse the **[Level 1 domains](canonical/level-1/)**.
3. Use the **[Adoption Starter Pack](adoption/ADOPTION_STARTER_PACK.md)** against the organization's exact OEB/Product baseline.
4. Map all **[ten Canonical capability families](canonical/level-1/E/L1-E_TEN_CANONICAL_CAPABILITY_CONTRACTS.md)** to real providers, agent-accessible operations, entitlements, authority, and enforcement.
5. Resolve bootstrap/context using **[L1-G](canonical/level-1/G/)** and interface/adoption requirements using **[L1-L](canonical/level-1/L/)**.
6. Derive and independently review the normal implementation Plan using **[L1-H](canonical/level-1/H/)** and define Evidence/Validation using **[L1-I](canonical/level-1/I/)**.
7. Keep **Capability gaps** and **Engineering Health Findings** separate using **[L1-E](canonical/level-1/E/)** and **[L1-J](canonical/level-1/J/)**.
8. Use the **[reference layer](reference/)** and **[integrity workflows](.github/workflows/)** as executable proof/examples, then obtain independent installation/adoption Validation for the organization-specific implementation.

If you are unsure where a topic lives, use the **[Repository Map](docs/REPOSITORY_MAP.md)**.