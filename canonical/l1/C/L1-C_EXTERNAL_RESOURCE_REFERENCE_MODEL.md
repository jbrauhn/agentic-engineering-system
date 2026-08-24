# L1-C — External Resource Reference Model

**Status:** Approved L1-C semantic baseline  
**Authority:** DR-107 federated authoritative state; R5 Capability Binding & Governed Invocation; Human Owner L1-C decision  
**Scope:** Provider-neutral reference semantics for externally authoritative/provider-owned objects.

## 1. Purpose

AE must reference provider-owned resources without either:

- reducing the reference to an untyped URL/locator; or
- copying the provider object into AE and silently taking ownership of provider state.

The canonical pattern is:

> **generic canonical reference core + capability-specific extensions**

## 2. External Resource Reference — C category

An External Resource Reference is not a copy of the external resource.

It is a canonical AE reference sufficient to identify the resource, its provider/binding context, its role in AE, and relevant source-of-truth/integrity semantics.

The generic semantic core must be able to express, as applicable:

- canonical Capability category;
- Capability Binding identity/revision;
- provider resource identity;
- locator/access mechanism where applicable;
- canonical role/relationship in AE;
- relevant provider-authoritative properties when the declaration belongs with the relationship/reference;
- provider revision/version/integrity information where relevant;
- provenance/reference creation context.

Exact field shape is deferred to schema design.

## 3. Strong provider identity over locator

> **A locator is not automatically a durable identity.**

Where a provider exposes stronger immutable/stable resource identity, the External Resource Reference should preserve that identity rather than relying only on a URL/path that may change.

A locator may remain useful for access/navigation but need not be authoritative identity.

## 4. Capability-specific extensions

The generic core may be extended with capability-specific semantics without creating bespoke provider coupling in every domain object.

Examples:

### Work Management reference

May include semantics equivalent to:

- project/workspace context;
- provider work-item identity;
- provider workflow-state authority declaration;
- dependency-link authority where relevant.

### Source Control reference

May include:

- repository identity;
- commit/PR/branch/tag identity;
- immutable commit/integrity information where relevant.

### CI/CD / Validation evidence reference

May include:

- run/job/test-result identity;
- artifact identity;
- execution revision/commit correlation;
- retention/integrity context.

### Observability reference

May include:

- trace/log/metric resource identity/query scope;
- time range;
- backend binding;
- retention/integrity limitations.

### Identity/Policy reference

May include:

- external principal/group/policy identity;
- relevant source authority;
- provider version/effective state where material.

## 5. Canonical Task versus Work Management object

The canonical L3 **Executable Task** remains distinct from a provider Work Item.

Example conceptually:

```text
Executable Task AE-TASK-147
    canonical:
      identity
      intended engineering work
      parent Execution Increment
      AE-required dependencies
      Contract/Plan traceability
      evidence/authority relationships

    realized_by:
      External Resource Reference
        capability: Work Management
        binding: org-work-management-binding
        provider resource identity: ENG-491
```

Provider-authoritative properties may include workflow status, assignment, provider-specific dependency fields, comments, timestamps, or other declared operational properties.

Anti-duplication rule:

> **AE shall not duplicate provider-owned properties unless AE has a semantic reason to own another authoritative property.**

## 6. Evidence reference

An **Evidence Record** is canonical A2. Evidence bytes/data may remain in an external provider.

The Evidence Record may point through an External Resource Reference to:

- CI run/report;
- source-control object;
- test artifact;
- observability trace;
- artifact store resource;
- other provider evidence.

The external reference preserves source/integrity/locator semantics while the Evidence Record preserves AE-specific provenance and relationship to Proof.

## 7. Architecture references

An externally hosted architecture source/model/representation may be referenced using this abstraction when the organization provider remains authoritative for selected representation properties.

This does not change the canonical **Architecture Model** entity or turn the external provider object into the model ontology.

## 8. Authority and governed invocation

External Resource Reference does not grant authority.

R4/R5 and applicable PEPs determine whether an actor may use the referenced provider resource for a canonical operation.

A resource being addressable is not evidence that an agent is entitled to read/write it.

## 9. Revision and stale-resource semantics

When interpretation depends on an exact external revision/version/integrity state, the reference must preserve enough provider semantics to resolve or verify that exact state.

Where a provider resource is mutable and no immutable revision exists, the Evidence/Validation/relationship semantics must preserve enough time/version/integrity context to avoid falsely implying exact historical reproducibility.

## 10. Provider replacement portability

Because canonical domain entities reference resources through Capability Binding + External Resource Reference semantics:

- Work Management may move from one provider to another without redefining Executable Task;
- source-control provider can change without redefining Contract/Plan/ADR semantics;
- CI/observability providers can change without redefining Evidence Record;
- canonical relationships remain stable while provider references/bindings evolve.

## 11. Working-environment hook

Open issue **#6** may later require environment/interface references to capability endpoints or bindings.

This model intentionally provides provider-neutral binding/resource identity hooks without creating a canonical IDE, Dev Container, CLI, local daemon, Portal, or agent-host requirement.