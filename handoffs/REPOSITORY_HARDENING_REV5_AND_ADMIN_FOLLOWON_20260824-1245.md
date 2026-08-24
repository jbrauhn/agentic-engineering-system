# Repository Hardening Revision 5 and Remaining Admin Follow-on

## Scope

Independent repository audit and hardening after Human Owner requested a critical review of whether the Canonical AE repository itself meets the engineering standards defined by AE.

## Current canonical repo state

Repo: `jbrauhn/agentic-engineering-system`
Current `main`: `f8affb51c8f6f9e5c1fdd160445e1b91370b2fc0`
Canonical release status: `HUMAN_OWNER_ACCEPTED`
Current distribution representation: revision `5`
Human-accepted basis remains unchanged:
- source commit `6c2424d5aea415819b276dfc6988aa9f964c6e62`
- distribution revision `2`
- transport SHA-256 `24131b15f6e960afa5463418bbf99c321c68eae01606aadd44e5dbb9df46887e`

No Contract/L1/DR/ADR semantic change was made by repository hardening.

## Audit findings

### Material governance finding

`main` is still unprotected. GitHub branch API after all hardening merges reports:
- `protected: false`
- protection disabled
- required status checks enforcement off.

Issue #12 remains OPEN and is the required enforcement follow-on.

### Branch audit

Before cleanup there are 25 branches total:
- `main`
- intentionally divergent `ae-session-relay`
- 23 stale/completed/temp branches.

Every completed normal development branch audited has `ahead_by = 0` against `main`; no consequential implementation commits were stranded.

Temporary packaging branches have only intentionally unmerged package-workflow commits. `noop-probe` has no unique commits. Branch problem is lifecycle hygiene, not lost integration.

### Traceability finding

Issue #2 was stale and contradictory after Part 1 acceptance. Audit found accepted L1-K references DR-102/103/104 as open experiments while those records are absent from the repo, and no consolidated Decision Register / Experiments Results Ledger is present.

Issue #2 was reclassified and remains OPEN as post-Part-1 evolution/discoverability/traceability debt. Missing records must not be fabricated from memory.

### Product-boundary finding

Portal issue #1 was active in the Canonical AE repo despite Portal being a separate future product. Issue #1 was closed as `not planned` in this repository while explicitly preserving the product idea for a future Portal product/repo.

## PR #29 — repository hardening

Title: `Harden repository governance and release representation`
Merged: YES
Merge commit: `4a7996030830fb13ec4a87c88baff341ea6fd509`
Exact reviewed PR head: `260d8f2afeca49fdd482fd070378c2653d31b01f`

Changes:
- all nine integrity workflows now appear on every PR to `main`;
- all nine are configured to rerun on every push to `main`;
- removed Observability/Learning and Adoption path filters;
- added missing push behavior for Standards/Health;
- explicit job names support stable required-check configuration;
- distribution revision `4 → 5` because integrity workflows are manifest-selected executable/reference artifacts;
- README/START_HERE/System Rationale/Repository Map updated for exact accepted lineage and rev5;
- added `.github/CONTRIBUTING.md`;
- added `.github/pull_request_template.md`.

Exact PR head passed all nine suites:
- lifecycle
- capability
- authority
- context
- planning/execution
- validation
- standards/health
- observability/learning
- adoption

Adoption integrity passed against rev5.

Issue #12 received a status update. Its remaining closure condition is actual GitHub enforcement + intentional failing-check merge-block proof.

## PR #30 — durable release publishing workflow

Title: `Add durable accepted-release publishing workflow`
Merged: YES
Merge commit: `f8affb51c8f6f9e5c1fdd160445e1b91370b2fc0`
Exact reviewed PR head: `bb5ab175b674e4bd3ba21203163d6bdcf9ed1ce7`

Adds `.github/workflows/publish-release-package.yml`.
This file is not selected by `.github/workflows/*-integrity.yml`, so distribution revision remains 5.

On manual workflow dispatch it:
1. assembles manifest-selected distribution;
2. requires accepted rev5 state + unchanged rev2 accepted basis;
3. verifies exactly 174 selected artifacts and every inventory SHA-256;
4. verifies clean-room baseline and handoff exclusion;
5. creates deterministic `Canonical_AE_Part1_Accepted_rev5.tar.gz`;
6. creates `SHA256SUMS.txt`, manifest, inventory, acceptance Authority Decision, and release metadata;
7. uploads Actions artifact copy;
8. creates GitHub Release/tag.

Exact PR head passed all nine integrity suites.

## Human Owner admin actions still required

Current connector cannot perform these GitHub admin operations:

1. Create an ACTIVE branch ruleset for `main` requiring PR + all nine checks, blocking force-pushes/deletion, and preventing normal bypass.
2. Prove enforcement with an intentionally failing integrity check; issue #12 must remain open until merge is visibly blocked.
3. Enable automatic deletion of merged head branches.
4. Delete 23 stale branches; keep `main` and temporarily keep `ae-session-relay` until relay migration.
5. Fill public repo description/topics and optionally disable Wiki as a parallel source-of-truth surface.
6. Run `Actions → Publish Canonical AE Release Package → Run workflow` with defaults to publish durable rev5 GitHub Release/tag.
7. Create a separate private coordination/relay repository. After it exists, migrate current `handoffs/` state there, verify migration, then delete `ae-session-relay` from the Canonical repo.

## Anti-drift

Do not call issue #12 closed before enforcement is demonstrated.
Do not invent DR-102/103/104 content.
Do not move Portal backlog back into Canonical AE repo.
Do not merge `ae-session-relay` to main.
Do not treat rev5 as a new Canonical semantic release; it is non-semantic executable/reference repository hardening over the accepted Part 1 basis.
