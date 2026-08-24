# L1-G — Bounded Context Selection, Currentness & Source Authority Model

**Status:** Human Owner-approved L1-G semantic baseline

## 1. Anchor-first, relevance-expanding assembly

Canonical semantic ordering is:

1. required governing anchors;
2. current work objects/dependencies;
3. relevant Architecture neighborhood;
4. material Decisions / Evidence / Handoff;
5. supporting knowledge by relevance;
6. stop when bounded-context constraints are reached.

This is not a retrieval algorithm. Implementations may use search, graphs, direct reads, vector retrieval, keyword indexing, or other methods.

Mandatory governing anchors must not lose a popularity/relevance contest to semantically similar supporting text.

## 2. Selection factors

Assembly considers as applicable:

- Context Requirement;
- authority/source quality;
- scope;
- exact revision/effectivity;
- currentness;
- dependency relationships;
- Architecture proximity;
- information-access policy;
- materiality;
- runtime/model/resource bounds.

Token count, context-window size, top-k, embedding model, chunk size, and reranking algorithm are not canonical requirements.

## 3. Requirement-relative currentness

> **Correct/effective revision beats newest revision.**

### EXACT_REVISION

That exact revision is required. A newer revision does not invalidate an intentionally requested historical/exact revision.

### EFFECTIVE_FOR_SCOPE

The implementation must identify the exact revision that governs the declared work scope. This must honor L1-D Contract effectivity and rolling-wave semantics.

### CURRENT_AT_USE

The source must be current enough at protected use time under applicable policy. Authority/revocation and operational provider facts commonly use this mode.

### BEST_AVAILABLE / SUPPORTING

Useful context may assist reasoning without being a gating authoritative anchor. Missing/stale supporting context may DEGRADE or CONSTRAIN instead of BLOCK.

## 4. Dispositions

- required governing source known stale/wrong revision → **REFRESH / REASSEMBLE**;
- required protected-use state freshness/authority UNKNOWN → **BLOCKED** until resolved;
- optional/supporting source unavailable/stale → **DEGRADE / CONSTRAIN** as applicable;
- intentionally requested historical source → valid when the exact historical revision resolves.

Old Context Packages are not silently mutated to claim currentness.

## 5. Source authority relationships

Reuse DR-107. Do not create a context-specific truth model.

Source metadata may distinguish orthogonally:

- authority relationship: `AUTHORITATIVE / NON_AUTHORITATIVE / UNKNOWN`;
- derivation relationship: issued/source vs derived/indexed/summarized/cached;
- currentness relationship: satisfies requirement / stale / unknown / intentionally historical.

Avoid one generic trust score.

## 6. Conflicts

If the authoritative source is known, it governs the property/scope/version. Conflicting cache/index/summary copies are identified as non-authoritative/stale/conflicting.

If two sources claim authority for the same material property/scope/version, context assembly may not silently choose the easiest or highest-ranked source.

- protected use + unresolved authority conflict → required state cannot be established → **BLOCKED**;
- exploratory reasoning may expose the conflict explicitly as unresolved context.

If an authoritative source is unavailable, a cache/vector/summary result is not promoted to authority. Authority/currentness becomes unknown according to the Context Requirement.
