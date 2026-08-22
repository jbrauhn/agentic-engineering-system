# L1-F — Authority Assignment Model

**Status:** Human Owner-approved L1-F semantic baseline  
**Domain type:** Authority Assignment [A2]

## 1. Admission decision

Authority Assignment is a first-class durable record when authority is explicitly issued, assigned, or delegated as independently meaningful governed authority state.

It may represent:

- Operational Authority Assignment;
- Decision Authority Assignment;
- Delegated Authority Assignment.

Independent identity is warranted because confusing assignments can cause material authorization, delegation, provenance, or security errors.

### Relationship to the L1-C domain catalog

DR-117 and this L1-F artifact **extend the canonical A2 record catalog established by L1-C** with `Authority Assignment [A2]`.

The L1-C entity-admission rule is unchanged: independent identity is warranted here because confusing authority assignments can create material governance, authorization, delegation, provenance, and security errors. The original approved L1-C artifact remains the historical L1-C baseline; this later adopted L1-F decision is the authoritative extension rather than a silent rewrite of that baseline.

**Primary logical responsibility:** R4 — Authority, Policy & Decision Coordination.  
**Collaborators:** R2 for durable identity/traceability and R5 where an assignment participates in protected capability use.

## 2. Minimum semantics

An assignment supports as applicable:

- assignment ID;
- authority kind (`OPERATIONAL` or `DECISION`);
- subject/holder;
- issuer / authoritative source;
- operation(s) or decision class(es);
- resource/scope;
- organization/Product-System;
- Loop/task scope;
- conditions;
- valid-from;
- valid-until;
- delegation permitted?;
- onward delegation permitted?;
- source assignment when delegated;
- provenance.

## 3. Issued-history semantics

Issued assignment history is non-destructive.

Expiration, revocation, or supersession does not rewrite what was originally issued. Current effectiveness is evaluated from authoritative validity/revocation state.

## 4. Federation

The canonical semantic type does not require an AE-owned shadow copy of every IAM grant.

Apply DR-107:

- preserve semantic identity;
- determine the authoritative source;
- preserve exact assignment/reference where required;
- preserve scope/validity/provenance/relationships;
- permit physical authoritative storage to remain external.

An externally authoritative assignment may participate through External Resource Reference/federated-state semantics.

## 5. Effective authority remains broader than assignments

An Authority Assignment is one possible authority basis. Effective OA/DA may also be derived dynamically or obtained from another authoritative mechanism. Conformance does not require manufacturing assignments where the organization does not use explicit assignment semantics.
