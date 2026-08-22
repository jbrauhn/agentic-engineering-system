# L1-G — Knowledge / Context / Memory Relationship Views

**Status:** Human Owner-approved L1-G semantic baseline  
**Purpose:** architecture-neutral semantic views; these boxes are not deployment components.

## 1. R2/R3 relationship

```text
Authoritative durable state (R2)
  Contract / Plan / Baseline / Architecture / Decisions
  Evidence / Validation / Authority / provider-owned properties
            │
            │ exact references + provenance + authority
            ▼
R3 Context & Knowledge Coordination
  Context Requirement [B]
  bootstrap/discovery
  retrieval / source resolution
  currentness/effectivity checks
  bounded assembly
            │
            ▼
Context Package [D]
            │
            ├── current actor use
            └── conditional Context Assembly Receipt [B]
```

R3 does not absorb the R2 objects it retrieves.

## 2. Continuation view

```text
Actor/session A
   │ material work/state
   ├── promoted to canonical owner (R2)
   └── Handoff Record [A2] when continuation state requires it
                │ exact reconstruction anchors
                ▼
        replacement/continuing actor
                │ resolve current/effective sources
                ▼
        new Context Package [D]
```

Old Handoff prose is not current source truth.

## 3. Bootstrap through heterogeneous Access Paths

```text
Supported Access Path A ─┐
Supported Access Path B ─┼─► Bootstrap / discovery semantics
Supported Access Path C ─┘        │
                                  ▼
                         implementation / release
                         OEB / Product Profile
                         actor / authority
                         work scope / Loop
                         Contract / Plan / Baseline / Architecture
                         Capability Bindings / Access Paths
                         Handoff / Context Requirement
                                  │
                                  ▼
                          bounded Context Package
```

No Portal/CLI/IDE/runtime is canonical.

## 4. Knowledge write versus semantic promotion

```text
reference information
  └─ knowledge.write ─► Knowledge provider/reference resource
                       (authority independently determined)

material canonical discovery
  └─ identify semantic owner
     └─ governed update/change process
        └─ canonical owner + provenance
           └─ derived retrieval/index/context refresh
```

## 5. Consequential judgment provenance

```text
Authoritative inputs ──────────────┐
Evidence Records ──────────────────┤
Context Assembly Receipt [B] ──────┤ when assembled context materially matters
                                   ▼
                        durable governed judgment
                        Validation / Review / Authority Decision / DR
```

The receipt supplements provenance; it does not become Evidence or source authority by itself.
