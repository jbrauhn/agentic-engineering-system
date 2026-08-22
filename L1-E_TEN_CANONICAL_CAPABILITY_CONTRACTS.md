# L1-E — Ten Canonical Capability Contract Definitions

**Status:** Approved L1-E semantic baseline  
**Rule:** Every required operation exists because a canonical AE lifecycle/responsibility would otherwise fail, become mechanically Human-dependent, or lose required evidence/governance.

## 1. Source Control

Required:
- `source.read`
- `source.resolve_revision`
- `source.write_change`
- `source.compare`

Conditional:
- `source.submit_change_for_review` when the organization's governed change path requires submission/review.

Purpose: exact versioned engineering state, governed change, comparison, and provenance without Human file-moving middleware.

## 2. CI/CD

Required:
- `pipeline.discover`
- `pipeline.run`
- `pipeline.status`
- `pipeline.result.read`
- `pipeline.evidence.read`

Conditional:
- `pipeline.promote_or_deploy` when applicable lifecycle work requires deployment/promotion.

Software deployment is not universal AE behavior.

## 3. Models

Required:
- `model.describe`
- `model.invoke`
- `model.result_metadata.read`

Model metadata must support material provider/configuration provenance without requiring unavailable or irrelevant provider internals.

## 4. Runtime / Execution

Required:
- `execution.start`
- `execution.status`
- `execution.result.read`

Conditional:
- `execution.cancel` when the execution shape is long-running/cancellable or explicit cancellation is needed to preserve bounded governed execution.

Atomic work does not need a meaningless stop method. The invariant is:

> **Bounded execution must remain governable.**

## 5. Identity & Access

Required:
- `identity.authenticate`
- `identity.context.read`
- `credential.establish_scoped_use`

Conditional:
- `entitlement.context.read` where permitted and needed.

`credential.establish_scoped_use` permits mediated/injected credentials. It does not require an agent to possess raw secret material.

> **Using IAM ≠ administering IAM.**

Normal AE operation does not require broad IAM administration.

## 6. Governed Tool Access

Required:
- `tool.discover`
- `tool.describe`
- `tool.invoke`
- `tool.result.read`

Conditional:
- `tool.cancel` for long-running/cancellable governed tool activity.

## 7. Observability

Required:
- `telemetry.emit`
- `telemetry.query`
- `telemetry.read`

Agent-access expectations are operation-specific. Telemetry emission may be automatic/system-mediated rather than explicitly reasoning-agent invoked.

## 8. Knowledge / Memory

Required:
- `knowledge.read`
- `knowledge.query`
- `knowledge.write`
- `knowledge.reference`

Knowledge writes are governed by R2 authoritative-state and immutability semantics. The Knowledge capability provides storage/access; it does not grant authority to rewrite approved Contracts, issued records, or another authoritative source.

Destructive deletion is not a universal minimum.

## 9. Work Management

Required:
- `work.create`
- `work.query`
- `work.read`
- `work.update`
- `work.transition`
- `work.relationship.manage`
- `work.annotation.add`
- `work.reference.associate`
- `work.artifact.associate`
- `work.complete`

Detailed semantics are in the Work Management proving contract.

## 10. Validation

Required:
- `validation.request`
- `validation.status`
- `validation.result.read`
- `validation.evidence.read`

R6 Evidence & Validation Coordination is not one provider. The external capability may combine Human review, AI Validators, CI/test systems, static/security analysis, evaluation services, or other mechanisms.

## Operation-family boundary

These definitions are semantic operation families, not provider API contracts. Provider-specific operations belong in Capability Bindings/adapters.
