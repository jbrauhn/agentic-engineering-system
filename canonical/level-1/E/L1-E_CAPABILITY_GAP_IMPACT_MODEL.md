# L1-E — Capability Gap and Impact Semantics

**Status:** Approved L1-E semantic baseline

## 1. Scope of classification

Classify a **specific deficiency + declared scope**, not a vendor globally.

A finding identifies as applicable:

- capability/operation;
- binding/provider scope;
- missing/deficient semantic;
- relevant Evidence;
- operational impact;
- adoption Proof impact;
- remediation direction.

## 2. Operational impact

- **NONE** — no material operational impact.
- **DEGRADE** — AE remains validly operable, but effectiveness, quality, speed, observability, context quality, or another non-gating property is materially reduced.
- **CONSTRAIN** — AE remains validly operable only through a narrower scope, reduced canonical path, deferred route, or explicitly approved limitation.
- **BLOCK** — a required governed action cannot validly proceed without violating canonical semantics/authority or inserting prohibited mechanical Human mediation.

A Human proxy is not automatically a valid constrained mode when direct agent-operability is canonical.

## 3. Adoption/conformance Proof state

Separate from operational impact:

- **PROVEN**
- **PENDING**
- **FAILED**
- **NOT_APPLICABLE**

Proof state must resolve to Evidence/Validation, not an editable flag.

Therefore:

- a transient provider outage can BLOCK a Loop while installation Proof remains PROVEN;
- a Loop may limp through a manual workaround while an applicable agent-operability Proof remains FAILED.

## 4. Capability Gap vs Engineering-Health Finding

**Capability Gap:** AE operation itself is deficient: missing operation/interface, no machine path, impossible scoped entitlement, unresolved binding, no enforcement, insufficient evidence, or provider cannot satisfy the semantic operation.

**Engineering-Health Finding:** the engineering environment exists but is weak: poor modularity, weak testing, missing architecture knowledge, high coupling, weak observability coverage, technical debt, etc.

Do not classify poor code quality as a Capability Gap. Do not classify missing `work.update` agent access as engineering maturity.

## 5. Capability assessment record semantics

Do not create a new Capability Assessment A2 record.

Use:

- Validation Record [A2];
- Evidence Records [A2];
- subordinate capability findings [B].

Validation scope may identify Capability Contract/release, Binding revision, operation set, organization/product/resource scope, supported consumer/runtime context, evidence, findings, and resulting Proof state.
