# L1-F — OEB / Product-System Authority Specialization

**Status:** Human Owner-approved L1-F semantic baseline

## 1. OEB authority coordination

An exact OEB revision may identify/reference:

- authoritative identity sources;
- entitlement models/sources;
- OA baseline/policy;
- DA assignments/reservations;
- Canonical and organization Human-reserved decision constraints;
- delegation policy;
- validity/revocation expectations;
- policy sources;
- policy precedence/combination semantics;
- protected-operation classes;
- PEP/enforcement mappings;
- provenance/audit expectations;
- governed exception mechanisms.

The OEB coordinates authoritative references. It is not the IAM/policy engine and does not copy every policy/assignment into a shadow configuration store.

## 2. Product/System specialization

Product/System Profile may tighten/narrow organization authority policy by, for example:

- requiring stronger identity assurance;
- narrowing authorized environments/resources;
- reserving additional decision classes to Humans;
- requiring additional approval before selected operations;
- selecting stricter PEP/enforcement expectations;
- narrowing provider/access paths.

It may not silently weaken:

- Canonical Human-reserved authority;
- mandatory organization authority controls;
- mandatory security/governance constraints.

## 3. Exceptions

Where an exception mechanism is permitted, the exception must be explicit, authorized by eligible DA, scoped, versioned/provenanced, and bounded by time/condition where applicable.

## 4. Revision behavior

A newer OEB/Profile revision does not retroactively rewrite prior authority evaluations. Active work uses explicit effectivity/reassessment policy where later authority changes must affect it.

## 5. Working-environment neutrality

Authority semantics apply regardless of supported interaction surface. Access Path remains the L1-E hook.

> **AE should require interface parity, not environment uniformity.**
