# Contributing to the Canonical AE System Repository

This document governs the **GitHub repository implementation process** for this repository. It does not redefine Canonical Agentic Engineering semantics. The Contract, release manifest, Canonical artifacts, and decision precedence remain authoritative for system meaning.

## Normal change path

1. Start from current `main`.
2. Create one bounded working branch for the change.
3. Make the smallest coherent change that satisfies the approved scope.
4. Open a pull request to `main`.
5. State the semantic impact explicitly:
   - Canonical semantic change;
   - executable/reference change;
   - adoption/supporting-content change;
   - repository-only/representation change.
6. Identify exact affected Contract/L1/DR/ADR/release references where applicable.
7. Run and pass all nine integrity suites on the exact PR head.
8. Review Evidence and any independent-review findings before merge.
9. Merge only the reviewed exact head.
10. Delete the completed working branch after merge.

Do not use direct pushes to `main` for normal work.

## Required integrity checks

The repository contains these nine check jobs:

- `lifecycle-integrity`
- `capability-integrity`
- `authority-integrity`
- `context-integrity`
- `planning-execution-integrity`
- `validation-integrity`
- `standards-health-integrity`
- `observability-learning-integrity`
- `adoption-integrity`

All nine are configured to appear on every pull request and to rerun on every push to `main`.

GitHub issue #12 tracks repository-level enforcement. Until a `main` ruleset/branch-protection rule requires these checks and a failing-check block test has been demonstrated, this document describes the intended process but must not be misrepresented as technically enforced.

## Canonical changes

A repository edit is not allowed to silently change Contract meaning.

For changes that affect Canonical semantics:

- identify the exact governing Contract and Level 1 scope;
- preserve immutable approved/historical revisions;
- use Decision Records / ADRs where the Canonical model requires them;
- route material Contract changes through the governed Contract Change process and Human Owner Decision Authority;
- update executable/reference models and Evidence proportionally;
- perform independent Validation appropriate to the change.

Repository reorganization, tooling, GitHub Actions, Python, JSON, branch rules, and provider-specific mechanics are repository implementation choices unless an authoritative Canonical artifact explicitly says otherwise.

## Distribution representation changes

If a change modifies an artifact selected by `canonical_ae_release_manifest.json`, assess whether the distributed payload changes.

When it does:

- advance the distribution representation revision when required;
- preserve the exact Human-accepted basis and historical revisions;
- update manifest purpose/compatibility information without silently rebasing acceptance;
- assemble the distribution and verify its inventory/hashes;
- rerun adoption integrity.

## Temporary branches and packaging work

Temporary test/package branches must be clearly marked, must not be merged when their purpose is export/test only, and must be deleted after their evidence/artifacts are preserved.

Do not keep completed feature branches merely as history. Git commits, merged pull requests, release artifacts, Decision Records, Validation/Evidence records, and issue history provide durable provenance.

## Session relay branch

`ae-session-relay` is a coordination mechanism, not Canonical product source and not a branch to merge into `main`.

Until it is moved to a separate coordination repository, treat it as intentionally divergent and exclude it from release/distribution claims. Never use its contents as hidden adoption input.

## Product-boundary discipline

The Canonical AE repository is for the AE System and its conforming reference/adoption material.

Separate products—such as a future AE Portal—must not use this repository as their product backlog or implementation repository merely because they consume or may be engineered through AE.

## Pull-request closure

Before declaring a change complete, verify:

- exact intended scope is present in `main`;
- no consequential commits remain stranded on the working branch;
- applicable Evidence/Validation is preserved;
- issues/findings are closed, updated, or explicitly carried forward;
- temporary scaffolding is removed;
- branch cleanup is complete.
