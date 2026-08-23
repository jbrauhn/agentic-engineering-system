# L1-I — Validator Context, Provider, Policy, and Adoption Model

## Purpose

Define how Validator actors consume governed context and external Validation mechanisms while keeping R6 responsibility, authority, policy, and provider implementation distinct.

## Validator context

Validation consumes L1-G Context Requirement semantics. A Validator may use a bounded Context Package for navigation and reasoning, but the Context Package is derived and non-authoritative.

For material judgment the Validator must independently resolve the authoritative Evidence/source state required by the Validation Requirement.

The Validation context should make resolvable, as applicable:

- exact Contract revision and Proof criteria;
- declared Validation scope;
- applicable Plan/Baseline/Architecture references;
- material Evidence Records and provider-owned Evidence sources;
- relevant prior Validation/finding/limitation state;
- authority/policy constraints;
- required independence dimensions;
- currentness/effectivity expectations;
- final-reconciliation relationships where applicable.

If authoritative state is stale, inaccessible, contradictory, or otherwise indeterminate in a way material to acceptance, the Validator may not rely on a summary to hide the deficiency.

## Context Assembly Receipt

A Context Assembly Receipt remains subordinate [B]. It is retained for Validation only when consequential-use or policy requires it and the assembled context materially influenced the judgment beyond directly referenced canonical inputs.

No universal prompt logging, hidden-reasoning logging, or chain-of-thought retention is required.

## R6 versus Validation Capability/provider

Preserve these distinctions:

- **R6 Evidence & Validation Coordination** — canonical semantic responsibility for Evidence relationships, independent judgment, Validation provenance, and judgment-to-route relationship;
- **External Validation Provider** — capability/provider mechanism that may run tests/evals/reviews or support judgment;
- **Validator actor/path** — identified Human/AI/mixed/other path issuing the independent Validation judgment;
- **provider result** — Evidence/provider output unless canonical Validation judgment semantics are satisfied.

No central Validator service is canonical.

A conforming implementation may compose:

- Humans;
- AI Validators;
- CI/test systems;
- security/static-analysis systems;
- evaluation services;
- observability/telemetry;
- inspection/review mechanisms;
- other Evidence sources/providers.

## Risk/policy strengthening

Canonical AE defines dimensions/hooks, not one mandatory assurance-level scale.

OEB/Product/System policy may explicitly require stronger rigor for a scope, such as:

- stronger judgment-path separation;
- Human participation;
- model/provider diversity;
- environment/toolchain separation;
- reproducibility;
- negative testing;
- Evidence breadth/depth;
- approval/DA requirements;
- stronger currentness/provenance expectations.

The effective requirement must be explicit, policy-backed, scoped, and reconstructable. Risk sensitivity cannot be used to self-declare weak Validation sufficient.

## Authority boundary

Validation judgment is not automatically Human DA. Where a protected Validation operation requires OA/entitlement/PEP, L1-F applies. Where a separate Human/organization approval is required by Contract/OEB/Product policy, that authority decision remains distinct from the R6 judgment.

A Validation Capability provider may execute under a provider identity different from the identified Validator actor/path. The relationship must remain reconstructable.

## Adoption and installation Validation

Installation/adoption and Capability Binding/readiness Validation reuse the same core Validation protocol with specialized Validation Requirements/scopes.

Conformance claims must therefore remain Evidence/Validation-backed rather than mutable status flags.

## Interface neutrality

Validation mechanisms may be exposed through any conforming Access Path. L1-I does not mandate a Portal, CLI, IDE, Dev Container, local daemon, agent host, runtime, or provider interface.

Preserve:

> AE should require interface parity, not environment uniformity.
