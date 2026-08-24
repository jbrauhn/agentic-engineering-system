# L1-I — Validation Requirement and Independence Model

## Purpose

Define the minimum canonical semantics needed for independent Validation without canonizing a Validator product, model/provider, physical separation pattern, Human review rule, or universal risk formula.

## Validation Requirement [B]

A **Validation Requirement** is a subordinate canonical structure that declares what must be independently judged for a governed Validation scope. It is not a new A1/A2 entity and does not replace the existing Validation Record [A2].

A Validation Requirement supports, as applicable:

- validation purpose/type;
- exact Contract revision;
- applicable Contract Proof criteria;
- declared Validation scope;
- applicable Plan, Product/System Baseline, and Architecture references;
- required Evidence classes/relationships;
- required independence characteristics;
- risk/policy constraints;
- required currentness/effectivity;
- unresolved findings/known limitations that must be considered;
- authority/approval requirements where applicable;
- expected judgment/routing semantics.

Operation/scope-specific requirements are preferred over one giant mandatory form.

## Universal independence invariant

Canonical AE requires **judgment-path independence**.

Minimum universal semantics:

1. the work-producing execution path may not issue its own Validation acceptance;
2. the Validator must be able to independently resolve the material Evidence and authoritative state required by the Validation Requirement;
3. the Validation judgment is attributable to an identified Validator actor/path with reconstructable provenance;
4. provider/test/CI success, executor summary, executor-created Evidence, or a `Validator` role label alone does not establish G4 acceptance.

The doer shall not become its own judge.

## Stronger independence is policy-sensitive

OEB/Product/System/risk policy may strengthen independence requirements, including as applicable:

- fresh invocation/agent;
- separate actor or identity;
- Human participation;
- model/provider diversity;
- environment/toolchain separation;
- organizational review separation;
- reproducibility;
- negative testing;
- stronger Evidence breadth/depth;
- additional authority/approval requirements.

These dimensions are **not universal Canonical AE requirements** unless higher authority explicitly makes them so.

The same underlying model/provider may conform for a scope when the judgment path is genuinely independent and the effective Validation Requirement permits it.

## Validator identity and authority

Preserve:

> role ≠ identity ≠ entitlement ≠ OA ≠ DA ≠ Validation judgment.

A Validation Record should make reconstructable, as applicable:

- Validator actor/identity;
- Validator type (Human, AI, other agentic system, mixed) where useful;
- exact Validation Requirement/scope;
- independence basis/provenance;
- material Evidence/source references;
- applicable authority/policy context;
- judgment/result/rationale;
- lifecycle-route relationship;
- issued time/version.

A `Validator` role label alone is insufficient.

A Validation judgment is an R6 judgment semantic, not automatically Human Decision Authority. Where Contract/OEB/Product policy requires Human DA or another approval in addition to Validation, that authority requirement remains separate.

The Validation Capability provider identity and Validator actor identity may differ.

## Independence assessment

The implementation must be able to establish, for the declared scope, that the judgment path is not controlled by the work-producing path. Merely relabeling the same work-producing action or workflow step as `validation` does not satisfy the invariant.

The independence basis may be explicit actor/path separation, technical enforcement, role/identity boundaries, policy-governed invocation separation, or another mechanism that provides equivalent semantic independence and provenance.

## Fail-closed rule

If required independence, identity, authoritative Evidence access, currentness, or required authority cannot be established for a protected acceptance decision, G4 acceptance must not occur.

## Non-goals

L1-I does not require:

- one Validator service;
- a fresh model/provider for every Validation;
- a Human Validator for every Validation;
- one testing or quality framework;
- one risk-tier scale;
- physical environment separation for every Validation;
- universal prompt or chain-of-thought logging.
