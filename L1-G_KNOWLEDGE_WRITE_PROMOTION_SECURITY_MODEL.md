# L1-G — Knowledge Write, Semantic Promotion & Context Security Model

**Status:** Human Owner-approved L1-G semantic baseline

## 1. Knowledge capability does not redefine ownership

L1-E `knowledge.read`, `knowledge.query`, `knowledge.write`, and `knowledge.reference` enable governed storage/access. They do not redefine which domain owns a fact.

> **`knowledge.write` persistence does not make information canonical truth.**

## 2. Reference-knowledge persistence path

```text
information
→ governed Knowledge provider
→ durable external/reference resource
→ provenance
→ External Resource Reference where useful
```

This can support documentation, source material, notes, searchable organizational knowledge, or other reference information. Authority remains independently determined.

## 3. Canonical semantic-promotion path

```text
ephemeral discovery
→ determine materiality
→ identify semantic owner
→ establish source/conflict/evidence
→ authorize/validate as required
→ write/update the correct canonical owner
→ preserve provenance
→ refresh derived indexes/context
```

The destination may be Contract Change Proposal, Plan revision, Architecture Model, Decision/ADR, Evidence Record, Learning Record, Authority state, Work state, or another established canonical owner.

The governing question is:

> **Where does this fact belong canonically?**

not “which memory store should remember it?”

Generic Knowledge write cannot bypass Contract immutability, issued-record immutability, R2 ownership, DR-107 source authority, or L1-F authority/PEP enforcement.

## 4. Context access/security

Preserve:

`source exists ≠ actor may retrieve ≠ source may appear in Context Package ≠ derived summary may reveal it`.

> **A derived Context Package may not grant broader information access than the actor has to the underlying information, absent an explicitly authorized and proven sanitization/declassification transformation.**

Derived summaries do not bypass source restrictions by default.

## 5. Revocation/current authority

Stale authorization does not indefinitely authorize retrieval. Protected actions re-evaluate current authority as required rather than trusting old Context Package state.

If access is later revoked, Canonical AE does not claim already exposed information has been erased. It supports, as applicable:

- no further governed retrieval;
- invalidation of continued protected use;
- blocking protected actions based on revoked authority;
- provider/runtime purge/reset where organization mechanisms require/support it.

## 6. Compaction and material promotion

Before intentional compaction/discard of system-managed context, material state that would otherwise be lost must already exist in its durable semantic owner or an appropriate Handoff.

Summaries may aid compression or retrieval but cannot replace exact Contract, Plan, Architecture, Authority Decision, Evidence, Validation, or authoritative provider state.

## 7. Context and Evidence/Validation

Context Package is not Evidence merely because a Validator saw it.

Validation remains grounded in exact Contract/Proof, Evidence Records, and authoritative state. Where additional assembled context materially influenced the judgment, retain sufficient basis through direct references and/or a Context Assembly Receipt according to the consequential-use rule.
