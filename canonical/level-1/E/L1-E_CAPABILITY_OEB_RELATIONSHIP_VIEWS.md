# L1-E — Capability / Binding / OEB Relationship Views

**Status:** Approved L1-E semantic baseline

## 1. Lifecycle action to provider result

```text
Canonical lifecycle/responsibility need
        ↓
Canonical Capability Operation
        ↓
deterministic Binding Resolution / binding plan
        ↓
Capability Binding(s)
        ↓
Access Path Descriptor
        ↓
runtime identity + current entitlement + OA/DA/policy
        ↓
applicable PEP
        ↓
provider-specific operation
        ↓
result + evidence/provenance
        ↓
Capability/adoption Validation
```

## 2. Readiness vs runtime

```text
Installation / Binding readiness
SUPPORTED
BOUND
DISCOVERABLE
REACHABLE
ENTITLEABLE
ENFORCEABLE
PROVEN
        │
        │ does not grant current authority
        ▼
Runtime request
identity → entitlement → OA/DA/policy → PEP
        │
   ┌────┼────┐
   ▼    ▼    ▼
ALLOWED DENIED BLOCKED
```

## 3. Organization baseline

```text
Canonical AE Release
        ↓
Organization Engineering Baseline revision
  ├─ capability binding refs
  ├─ readiness Validation refs
  ├─ policy/authority refs
  ├─ standards/architecture/evidence refs
  └─ engineering constraints
        ↓ specializes
Product/System Profile revision
        ↓
Derived effective configuration
        ↓
AE Loop / Plan / governed work
```

## 4. Interface parity

```text
Canonical operation
       ↓
same semantic Binding
  ┌─────────────┬────────────────┬────────────────┐
  ▼             ▼                ▼
MCP path     governed API      broker path
context A     context B         context C
```

The access mechanisms may differ. The canonical operation, scope, identity/authority semantics, result, and evidence requirements remain recognizable and equivalent.
