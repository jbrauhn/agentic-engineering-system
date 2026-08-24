# L1-E — Organization Engineering Baseline Operational Model

**Status:** Approved L1-E semantic baseline  
**Domain object:** Organization Engineering Baseline [A1]

## Definition

> **The Organization Engineering Baseline is the durable, versioned organization-level AE engineering operating baseline that establishes organization defaults, constraints, capability-realization references, governance references, and engineering expectations against which Product/System-specific AE implementations are specialized.**

> **The OEB coordinates authoritative organization state; it does not own all of it.**

## Minimum OEB semantics

An exact OEB revision identifies/references, as applicable:

- organization scope;
- Canonical AE Release;
- organization Capability Bindings;
- capability-readiness Validation/Evidence;
- identity/authority/policy baseline references;
- standards/engineering-practice references;
- architecture expectations;
- evidence/Validation expectations;
- risk/classification/security constraints;
- infrastructure/runtime/engineering constraints;
- declared supported working-context constraints where relevant;
- organization engineering-health references;
- governed exception/limitation references;
- provenance.

The OEB shall not become a giant shadow configuration document copying every authoritative organization fact.

## Exact revision behavior

DR-109 applies.

Plans/Loops/adoption assessments that materially depend on OEB state must be able to identify the exact OEB revision used.

> **A new OEB revision does not silently rebase active work.**

Historical work remains reconstructable against the OEB revision it used.

L1-E establishes a hook for policy-driven reassessment/effectivity when a later OEB revision must affect active work, but it does not copy the Contract revision-effectivity protocol or define detailed security/standards policy here.

## Capability relationship

The OEB coordinates the organization-level declared capability environment:

Canonical Capability Contract → Capability Binding → readiness Validation/Evidence → organization defaults/constraints.

A Product/System Profile may select/tighten bindings and constraints for a specific target.
