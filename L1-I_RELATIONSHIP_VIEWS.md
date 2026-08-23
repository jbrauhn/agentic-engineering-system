# L1-I — Validation Relationship Views

## Core judgment chain

```text
Contract revision
   └─ contains ─> Proof Criterion(s)
                    │
                    ▼
             Validation Requirement [B]
                    │
          requires / evaluates
                    │
                    ▼
Evidence Record(s) [A2] ── references ──> provider Evidence [C]
                    │
                    ▼
       independent Validator path
                    │
                    ▼
          Validation Record [A2]
                    │
          judgment + provenance
                    │
                    ▼
         R1 lifecycle route
 ACCEPT / RETRY / REPLAN / CONTRACT CHANGE / ESCALATE
```

The judgment and route are related but not the same semantic object.

## Verification versus Validation

```text
Contract Proof
     │
     ▼
Plan Verification/Test Strategy
     │
     ▼
Execution / Verification
     │
     ├─> Evidence Record(s) / provider Evidence
     │
     ▼
Independent Validation
     │
     ▼
G4 acceptance only if exact requirement + sufficiency + independence are satisfied
```

The work-producing path may produce Evidence but may not issue its own acceptance.

## Increment and final Contract Validation

```text
Increment A Validation ─┐
Increment B Validation ─┼─> final reconciliation
Increment C Validation ─┘         │
                                  ├─ reused valid Evidence/Validation
                                  ├─ cross-Increment interactions
                                  ├─ final state/integration
                                  ├─ current-reliance checks
                                  ├─ full final Contract Proof coverage
                                  ▼
                       Final Contract Validation Record
                                  │
                                  ▼
                              G4 / ACCEPT
```

Increment acceptance does not automatically imply final Contract acceptance.

## Evidence invalidation without history mutation

```text
Evidence E@issued ──used_by──> Validation V@issued
      │                            │
      │ later finding             │ historical judgment retained
      ▼                            │
Current reliance: UNRELIABLE      │
      │                            │
      └────> revalidation / escalation / later Validation
```

The historical Evidence and Validation records remain immutable.

## Provider / actor separation

```text
Validation Requirement
       │
       ▼
Validator actor/path ── independent resolve ──> Evidence/source state
       │
       ├─ may call ─> Validation Capability provider
       ├─ may consume ─> CI/test/security/eval/observability providers
       └─ issues ─> Validation Record
```

Provider identity does not automatically equal Validator identity.

## Policy strengthening

```text
Canonical minimum: judgment-path independence
              │
              ▼
OEB/Product/risk policy
              │
              ├─ Human participation?
              ├─ provider/model diversity?
              ├─ environment separation?
              ├─ negative testing?
              ├─ reproducibility?
              └─ stronger Evidence/currentness?
              │
              ▼
Effective Validation Requirement
```

Stronger dimensions are scoped/policy-sensitive, not universal Canonical Core requirements.

## Scope specialization

```text
one core Validation protocol
   ├─ engineering Increment
   ├─ final Contract
   ├─ installation/adoption
   └─ Capability Binding/readiness
```

Specialize requirement/scope, not Validation entity type.
