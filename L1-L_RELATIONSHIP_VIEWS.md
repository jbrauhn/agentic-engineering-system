# L1-L — Adoption / Distribution Relationship Views

## Distribution authority

```text
Canonical AE Release Manifest [F]
 ├─ identifies → Canonical Core [normative]
 ├─ identifies → Adoption Starter Pack [conforming aid]
 ├─ identifies → Executable / Reference Layer [conforming demonstration]
 └─ records → release provenance / integrity / supersession
```

## Adoption

```text
Canonical AE Release
        ↓
OEB + Product/System Profile/Baseline
        ↓
AE Implementation Profile [Candidate]
        ↓
Capability Bindings + authority/policy + standards + context/bootstrap
        ↓
Capability gaps [D] + Engineering Health Findings [A2]/health-gap view [D]
        ↓
normal Plan [A1]
        ↓
normal AE Loop(s)
        ↓
Evidence [A2]
        ↓
independent adoption Validation [A2]
        ↓
Conformance projection [D]
```

## Bootstrap/interface parity

```text
Environment A: Dev Container → CLI/agent runtime ─┐
                                                  ├→ Bootstrap Descriptor [B]
Environment B: Remote workspace → IDE/broker ────┘
                                                       ↓
                      same effective Release/OEB/Profile/Loop/Contract/Plan
                                                       ↓
                      same canonical Capability operations + governed authority
```

## Drift

```text
Historical Validation against exact Release/Profile/Bindings
        │ remains immutable
        ▼
material later change
        ↓
current reliance assessment
        ├─ unaffected → reuse proportionally
        └─ affected → NEEDS_REASSESSMENT → new Evidence/Validation
```
