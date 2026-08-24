# L1-G — Context Assembly Receipt / Provenance Model

**Status:** Human Owner-approved L1-G semantic baseline  
**Domain:** Context Assembly Receipt / Source Manifest [B]

## 1. Purpose

Context provenance must be sufficient to reconstruct material context basis where direct canonical references are not enough, without creating a permanent audit record for every routine retrieval.

No new Context Provenance A2 record is introduced.

> **Material context provenance may be durable without context provenance becoming a first-class domain entity.**

## 2. Receipt semantics

A Context Assembly Receipt / Source Manifest supports, as applicable:

- Context Package / purpose / Context Requirement reference;
- assembly time;
- authoritative source references;
- exact revisions/digests where material;
- retrieval/index sources used;
- selection/exclusion outcomes;
- currentness/effectivity checks;
- authorization/access outcomes or references;
- unresolved conflicts;
- assembly mechanism/version when materially relevant;
- optional package integrity digest.

A receipt is subordinate B state. It may be stored with the durable outcome, package, handoff, audit/evidence system, or another conforming mechanism.

## 3. Consequential-use retention trigger

Durable context provenance is required when assembled context materially contributes to a durable consequential outcome whose basis otherwise cannot be adequately reconstructed from direct canonical references.

Depending on policy/risk, this can include:

- Validation judgment;
- Authority Decision;
- Plan Review;
- material architecture/engineering Decision;
- Handoff;
- protected transition;
- another durable governed judgment.

If the durable output already directly references all material authoritative inputs, a separate full receipt may be unnecessary.

Routine low-risk context assembly does not automatically require permanent receipt retention.

## 4. Prohibited retention by default

Do not require a receipt to store:

- private chain-of-thought;
- credential or secret material;
- every prompt;
- complete duplicated source bodies solely for provenance.

Provenance references sources; it does not create a hidden data exfiltration channel or shadow repository.

## 5. Relationship to Evidence and Validation

Context Package is not automatically Evidence.

Where assembled context materially influences Validation beyond direct Evidence/Contract/Proof references, a Validation Record may reference the applicable receipt/source manifest as contextual provenance.

The receipt does not replace Evidence Records or the authoritative sources it references.
