# L1-F — Authority Source-of-Truth & Provenance Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Federated authoritative authority state

Canonical AE does not require a central authority database.

Apply DR-107: for every material authority fact, the implementation can determine the authoritative source for the relevant scope/time.

Potential facts/sources include:

- authenticated identity → Identity Provider / authoritative identity mechanism;
- provider entitlement → provider IAM/entitlement source;
- OA → Authority Assignment, external assignment, policy/relationship/task derivation;
- DA → authority assignment/policy;
- Contract approval/change → Authority Decision;
- organization/Product policy → authoritative policy source;
- revocation/supersession → authority source;
- PEP configuration → provider/runtime/broker enforcement configuration.

## 2. Caches and projections

Authorization caches/context products are derived.

They must not silently become co-authoritative. They carry enough source/freshness semantics to determine whether they are acceptable for a protected evaluation.

If required authority freshness cannot be established within policy:

`INDETERMINATE → BLOCKED`.

An authoritative revocation overrides a stale cached permit.

## 3. Authorization evaluation provenance [B]

Runtime authorization evaluation remains subordinate B semantics, not a new A2 record for every request.

Retention is risk/operation/policy-sensitive.

The implementation defines which authorization events need durable provenance based on:

- protected-operation class;
- governance significance;
- risk;
- policy;
- audit/evidence requirements.

Where durable reconstruction is required, provenance supports as applicable:

- requester/actor;
- authenticated identity;
- canonical operation;
- target/resource;
- Loop/task scope;
- relevant Contract/Plan/OEB revisions;
- entitlement source;
- OA basis/source;
- DA/Authority Decision basis;
- policy sources/revisions;
- effective policy decision;
- conditions/obligations;
- PEP/enforcement point;
- runtime result;
- provider effect reference;
- Evidence/provenance references.

Do not retain credential secrets merely to support provenance.

## 4. Historical integrity

Later revocation, policy change, or discovery of invalid authority does not destructively rewrite historical events. Corrections/findings are appended or related while the historical record remains reconstructable.
