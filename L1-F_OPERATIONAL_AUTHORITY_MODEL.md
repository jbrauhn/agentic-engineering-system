# L1-F — Operational Authority Model

**Status:** Human Owner-approved L1-F semantic baseline

## 1. Definition

> **Operational Authority is the effective scoped authority of an actor to perform or request one or more operational canonical AE actions against specified resources/context under applicable conditions.**

OA is effective semantic authority, not one persistence mechanism.

## 2. Authority basis

A conforming implementation may establish OA through:

- Authority Assignment [A2] when explicitly issued/assigned/delegated;
- authoritative external assignment/reference;
- dynamic policy derivation;
- role, attribute, relationship, task, resource, or environment policy;
- another reconstructable authoritative mechanism.

Equivalent OA meaning is required even when organization mechanisms differ.

## 3. Minimum scope semantics

OA must be capable of expressing/reconstructing, where applicable:

- subject/actor/identity;
- canonical operation(s) or operation class;
- target resource(s) / resource scope;
- organization / Product-System;
- Loop / Increment / Task;
- Contract/Plan context when authority depends on them;
- environment/classification;
- conditions/obligations;
- valid-from / valid-until;
- authoritative source;
- delegation basis;
- provenance;
- revocation/supersession/condition state.

Not every implementation must persist every dimension in one object.

## 4. Least privilege

> **Authority and technical entitlement should use the smallest enforceable scope sufficient to perform the authorized work reliably and safely.**

Meaningfully narrower enforceable authority should be preferred over broad standing administrator access. Canonical AE does not require impractical one-call/one-token granularity.

## 5. Independent lifetimes

`credential lifetime ≠ entitlement lifetime ≠ OA lifetime ≠ DA lifetime`.

OA semantics support, as applicable:

- not-yet-valid;
- active;
- expired;
- revoked;
- superseded;
- invalidated by condition change.

A technically valid credential does not extend expired/revoked OA. Credential refresh does not silently renew OA.

## 6. Historical integrity

Later revocation changes future effective authority and does not destructively rewrite prior authorization history.

If prior authority is later discovered invalid/fraudulent, preserve the historical event and create explicit corrective finding/provenance rather than rewriting the earlier record.
