# L1-G — Context Requirement & Context Package Model

**Status:** Human Owner-approved L1-G semantic baseline  
**Domain:** Context Requirement [B]; Context Package [D]

## 1. Context Requirement [B]

A Context Requirement answers:

> **What information must be resolvable for this actor/action/task before governed work can proceed correctly?**

It is subordinate semantic state, not a new A1/A2 entity and not an orchestration or retrieval algorithm.

### 1.1 Semantics supported as applicable

- purpose / lifecycle action / canonical operation;
- required governing anchors;
- required authority/source quality;
- exact-revision or scope-effectivity relationship;
- currentness/freshness relationship;
- security/access requirement;
- optional/supporting context categories;
- failure disposition when required context cannot be established;
- assembly bounds/constraints where the use requires them.

### 1.2 Requirement classes

A context source may be classified by the requirement as:

- **REQUIRED_GOVERNING** — must resolve correctly before the protected/governed action can proceed;
- **REQUIRED_OPERATIONAL** — must satisfy currentness/operability requirements at use time;
- **SUPPORTING** — useful for reasoning but not itself a gating governing anchor.

These classes describe use semantics, not trust scores.

### 1.3 Example: begin Execution for Increment A

Required governing anchors can include:

- AE Loop;
- Execution Increment;
- governing Contract exact/effective revision;
- reviewed Plan exact revision + declared review scope;
- Product/System Baseline;
- applicable Architecture neighborhood;
- relevant authority requirements;
- Capability Binding / Access Path information.

Supporting context can include related historical decisions, findings, Learning, or other relevant references.

## 2. Context Package [D]

A Context Package is a bounded derived view assembled for a current purpose.

> **Context Package is not authoritative truth merely because an actor consumes it.**

### 2.1 Minimum semantics supported as applicable

- package-instance identity/reference;
- purpose / context intent;
- intended actor/consumer/runtime context;
- Organization-specific AE Implementation;
- Product/System scope;
- Loop / Increment / Task scope;
- Context Requirement reference;
- assembly time;
- source references;
- exact revisions/digests where material;
- source-authority relationship;
- currentness/effectivity result;
- access/security constraints;
- selected material/references;
- unresolved conflict/unavailable-source indications;
- assembly bounds/constraints;
- Assembly Receipt / Source Manifest reference where retained.

### 2.2 Permitted content

A Context Package may contain excerpts, structured facts, summaries, references, links, retrieval affordances, and other bounded derived material.

It need not copy every authoritative byte into a model context.

> **Bounded context can preserve exactness through resolvable references rather than loading every authoritative byte simultaneously.**

### 2.3 Anti-shadow rule

A Context Package cannot become a shadow Contract, Plan, Architecture Model, Decision Register, Evidence store, policy store, Work Management store, or authority database.

If an actor discovers a difference between the package and an authoritative source, the authoritative source governs according to the applicable Context Requirement and DR-107.

## 3. Package invalidation/reassembly

A Context Package describes what was assembled at a point in time. When governing state changes or required currentness expires, do not mutate the old package to pretend it was always current.

Create/reconstruct a new package or explicitly mark the prior package invalid/stale for the new use.

> **Context invalidation is not authoritative source-state mutation.**
