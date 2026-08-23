# ADR-008 — Machine-readable standards/health protocol and integrity check

**Status:** Accepted  
**Date:** 2026-08-22

## Context

L1-J adds machine-testable semantics for standards applicability/effectivity and Engineering Health Finding/remediation behavior. The repository already uses the staged ADR-002–007 pattern: Human semantic artifacts remain normative; JSON/Python/GitHub Actions provide a conforming executable/reference layer.

## Decision

Use:

- `standards_health_protocol.json` as the Stage-1 machine-readable L1-J representation;
- `standards_health_scenarios.json` for semantic valid/invalid fixtures;
- `standards_health_portability_fixtures.json` for materially different implementation equivalence;
- `validate_standards_health.py` as the repository reference validator;
- `.github/workflows/standards-health-integrity.yml` as the distinct repository CI job `standards-health-integrity`.

The validator cross-checks inherited lifecycle, capability, authority, context, Planning/Execution, and Validation machine models rather than creating shadow local semantics.

Human L1-J semantic artifacts remain normative for meaning. JSON, Python, and GitHub Actions are repository/reference implementation choices, not Canonical AE technologies.

## Required executable properties

The check must falsify, among other cases:

- mandatory requirements disguised as advisory/proportional omission;
- collapsed applicability/waiver/nonconformance states;
- unproven exceptions;
- latest-version silent rebase;
- Product silent weakening;
- checklist/tool-score shadow truth;
- framework-name health findings;
- Capability Gap/health confusion;
- destructive finding-history rewrite;
- self-validation of remediation;
- context/summary becoming source authority;
- new convenience entity inflation;
- central standards/health service assumptions.

## Consequences

The repository gains meaningful executable L1-J proof and portability fixtures. It does not gain a production compliance platform, standards database, maturity model, or health-scoring product.

Issue #12 should track `standards-health-integrity` but remain open until branch/ruleset enforcement is actually configured and demonstrated.