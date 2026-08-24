# Repository ruleset enforcement proven; issue #12 closed

**Repository:** `jbrauhn/agentic-engineering-system`  
**Coordination branch:** `ae-session-relay`  
**Date:** 2026-08-24

## Human Owner action

Human Owner created and activated the GitHub branch ruleset `Protect main` targeting the default branch with the agreed controls, including:

- Active enforcement;
- empty bypass list;
- default branch target;
- restrict deletions;
- require pull request before merging;
- 0 required human approvals for current solo-maintainer operation;
- require conversation resolution;
- Merge-only integration;
- require status checks to pass;
- require branches to be up to date before merging;
- block force pushes;
- nine AE integrity jobs configured as required checks:
  - `lifecycle-integrity`
  - `capability-integrity`
  - `authority-integrity`
  - `context-integrity`
  - `planning-execution-integrity`
  - `validation-integrity`
  - `standards-health-integrity`
  - `observability-learning-integrity`
  - `adoption-integrity`

GitHub branch API changed from prior `protected:false` to `protected:true`, confirming an active rule now targets `main`.

## Negative enforcement Proof

A dedicated negative-test branch and PR were created:

- branch: `ruleset-enforcement-negative-test-20260824`
- PR: `#31` — `NEGATIVE TEST — prove required integrity check blocks merge`
- exact head: `3506b1d591764079a8c0f6a2491c7debd4e58381`

The branch changed only `.github/workflows/lifecycle-integrity.yml` by adding an intentional `exit 1` step.

Exact-head CI result:

- 8 integrity suites: `success`
- `lifecycle-integrity`: `failure` as intentionally designed

An explicit GitHub API merge attempt was then made using:

- merge method: `merge`
- expected exact head SHA: `3506b1d591764079a8c0f6a2491c7debd4e58381`

GitHub rejected the merge with HTTP 405:

> Repository rule violations found  
> Required status check "lifecycle-integrity" is failing.

PR #31 was then closed unmerged.

This proves the repository enforcement path blocks a merge when a required AE integrity check fails, including for the repository owner/admin actor with no bypass configured.

## Issue #12

Issue `#12` — `Repository governance — require applicable integrity checks before main merge` — now satisfies its closure condition and was closed as `completed`.

Closure evidence was recorded in the issue discussion before closure.

## Merge method disposition

The repository ruleset uses **Merge only**.

This is a repository implementation choice, not a Canonical AE semantic requirement. It is preferred here because the accepted AE system places strong value on non-destructive history, exact revisions, reconstructability, and provenance. Merge commits preserve the branch commit graph and make the PR integration event an explicit two-parent commit. Squash merging remains a potentially valid conforming choice in other repositories if durable provenance/evidence requirements are still satisfied.

## Remaining repository-hygiene follow-ons

Still Human-admin/manual unless separately completed:

1. enable automatic deletion of merged head branches;
2. delete stale completed/temporary branches, including the negative-test branch;
3. publish the durable rev5 GitHub Release using the merged `Publish Canonical AE Release Package` workflow;
4. fill repository description/topics/homepage metadata;
5. disable unused Wiki if not intentionally maintained;
6. move `ae-session-relay` coordination state to a separate private repository, then delete the relay branch from the Canonical repository after migration is independently verified;
7. issue #2 remains OPEN as evolution/discoverability/traceability debt for the historical Decision Register and Experiment results ledger.

No Canonical Core semantic change was made by the ruleset or negative enforcement test.