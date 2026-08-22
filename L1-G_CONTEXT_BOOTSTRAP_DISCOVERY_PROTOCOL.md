# L1-G — Context Bootstrap / Discovery Protocol

**Status:** Human Owner-approved L1-G semantic baseline  
**Scope:** canonical discovery semantics; no prescribed interface technology

## 1. Purpose

A Human or agent entering through a supported Access Path must be able to discover enough authoritative AE identity, scope, capability, authority, and continuation state to assemble governed current context without relying on trial-and-error or hidden prior conversation.

## 2. Canonical discovery questions

The bootstrap protocol must be able to resolve, as applicable:

1. Which Organization-specific AE Implementation is this?
2. Which Canonical AE release applies?
3. Which exact OEB revision applies?
4. Which exact Product/System Profile applies?
5. Who is the actor and what authority context matters?
6. Which Product/System/work scope is being entered?
7. Which Loop / Increment / Task applies?
8. Which exact/effective Contract, Plan/review scope, Baseline, Architecture, Decisions, and Validation state apply?
9. Which Capability Bindings and Access Paths apply?
10. Is there applicable Handoff/continuation state?
11. Which Context Requirement applies?
12. Assemble bounded current context.

## 3. Bootstrap Descriptor [B]

A subordinate Bootstrap Descriptor or semantically equivalent discovery metadata may represent enough information to find the items above.

It is not an Engineering Environment Profile and is not a new A1/A2 entity.

## 4. Interface neutrality

Bootstrap/discovery may be provided through injected configuration, local machine-readable metadata, runtime service, API, MCP, source-controlled files, Work Management, a future Portal, or another conforming Access Path.

Canonical AE does not require one Portal, CLI, IDE, bootstrap filename, daemon, agent host, REST endpoint, or runtime.

> **AE should require interface parity, not environment uniformity.**

## 5. Issue #6 relationship

L1-E Access Path + L1-G Bootstrap/Context semantics provide the semantic hook needed for later developer/agent working-environment design.

Issue #6 remains open because L1-G does not define the complete Human/agent interaction experience or environment bootstrap mechanism.
