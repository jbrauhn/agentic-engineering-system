# L1-F — Authority / Capability / Lifecycle Relationship Views

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Protected operation path

```text
Canonical lifecycle need
        │
        ▼
Canonical Capability Operation
        │
        ▼
Capability Binding / Access Path
        │
        ▼
Authorization Request Context
        │
        ├─ identity
        ├─ provider entitlement
        ├─ OA
        ├─ DA / Authority Decision if required
        ├─ exact governed-work context
        └─ effective policy sources
        │
        ▼
Policy / authority evaluation
 PERMIT | DENY | INDETERMINATE
        │
        ▼
Applicable distributed PEP
        │
        ▼
R5 provider invocation when ALLOWED
        │
        ▼
Provider effect + Evidence/provenance
```

## 2. Runtime outcome mapping

```text
PERMIT + entitlement + enforceable PEP + provider available
    → ALLOWED

DENY
    → DENIED

INDETERMINATE
    → BLOCKED

PERMIT + missing technical entitlement
    → BLOCKED
```

## 3. Contract Change Human-DA path

```text
Contract Change Proposal exact revision
        │
        ▼
eligible Human DA?
        │
        ▼
Authority Decision [A2]
        │
        ▼
G5 Contract Change Gate
        │
        ▼
new Contract revision approved
        │
        ▼
L1-D effectivity evaluation
```

## 4. Explicit versus derived OA

```text
Authority Assignment [A2] ─┐
External Assignment [C] ────┼─► Effective OA
Dynamic Policy Derivation ──┘
                             │
                             ▼
                    Policy evaluation
```

No implementation must materialize every authority basis as an AE-owned assignment.

## 5. Enforcement/bypass view

```text
PERMIT
  │
  ├─► preferred Access Path ─► PEP ─► provider
  │
  └─► bypass assessment for identities/credentials/paths
       available to governed actor/runtime in declared scope

Equivalent ungoverned path available?
  yes → enforcement Proof fails
  no  → continue Proof
```
