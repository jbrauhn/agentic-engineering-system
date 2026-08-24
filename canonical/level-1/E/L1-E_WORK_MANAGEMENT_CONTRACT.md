# L1-E — Work Management Detailed Capability Contract

**Status:** Approved L1-E proving capability  
**Contract basis:** Contract v1.0 §7

## Purpose

Work Management must provide governed agent-readable and agent-writable interfaces sufficient for authorized agents to administer routine AE work without a Human mechanical proxy.

## Required operations

### `work.create`
Create a durable provider work object needed by AE.

### `work.query`
Locate relevant work by canonical/provider criteria.

### `work.read`
Retrieve current relevant provider work state/content.

### `work.update`
Modify authorized work content/metadata.

### `work.transition`
Request/change provider workflow state when authorized.

Provider workflow state remains provider-owned and does not become AE Validation state.

### `work.relationship.manage`
Create/update/remove dependencies and other required work relationships.

### `work.annotation.add`
Add comments/annotations needed by AE.

### `work.reference.associate`
Associate Evidence Records, external references, canonical resource references, or other related resources.

### `work.artifact.associate`
Associate a relevant artifact with the work object.

This does **not** require binary attachment/upload semantics. A provider may satisfy it through an attachment, link, comment, structured relationship, native artifact relation, or another mechanism that preserves the canonical association.

### `work.complete`
Complete/close provider work when authorized.

## Agent-operability invariant

Every required operation must have a governed machine-accessible path usable by or on behalf of an appropriately authorized agent.

> **An implementation requiring a Human intermediary for routine Work Management administration does not fully satisfy the canonical Work Management capability.**

## Mechanical-intermediary diagnostic

1. Is the Human exercising judgment/Decision Authority? If yes, legitimate Human participation.
2. Is the Human only translating/clicking/copying/uploading/triggering after substantive intent is known?
3. Is the operation required to be agent-operable?
4. Could an appropriately authorized agent perform it through a least-privilege governed path?

Failure modes:
- no machine path → capability/interface gap;
- machine path exists but only broad admin authority can use it → entitlement-model gap;
- machine path and scoped entitlement exist, but current actor OA denies → correct runtime denial, not a binding defect;
- appropriately entitled/authorized agent succeeds → no mechanical-intermediary deficiency.

> **Human judgment is a feature. Human transcription is usually a defect.**

## Proof

The proving contract must demonstrate:

- two materially different provider shapes map to the same canonical operations;
- required mappings exist;
- declared supported contexts have deterministic access paths;
- authorized agent operation succeeds;
- unauthorized operation is denied;
- missing operation fails;
- UI-only required agent operation fails;
- broad-admin-only entitleability fails;
- provider Done does not imply AE Validation acceptance;
- artifact association does not require one physical attachment mechanism.
