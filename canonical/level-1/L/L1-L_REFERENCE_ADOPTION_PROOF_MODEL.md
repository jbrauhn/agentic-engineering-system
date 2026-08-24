# L1-L — Reference Adoption Proof Model

## 1. Synthetic imperfect organization

The reference layer uses a deliberately imperfect generic organization fixture. It is small enough to understand and intentionally contains:

- plausible but heterogeneous provider bindings;
- authority/policy and standards context;
- architecture/evidence/Validation expectations;
- one true Capability gap;
- one Engineering Health Finding;
- one capability that is technically available but not sufficiently agent-operable/entitleable;
- one allowed direct-agent Work Management operation;
- one denied out-of-scope Work Management operation;
- governed health remediation with Evidence and independent Validation.

The fixture is reference/test material, not Canonical Core and not a product design.

## 2. Integrated happy path

The reference loop composes existing L1 semantics:

```text
Loop Context
→ exact Contract
→ architecture-aware Plan
→ exact-scope Plan Review
→ capability/context/authority readiness
→ bounded Execution
→ Verification + Evidence
→ independent Validation
→ Accept
→ learning disposition
```

No demo bypass is permitted for authority, review, Evidence, Validation, or history.

## 3. Controlled backward path

The reference layer includes a failed Validation that routes to `REPLAN`, preserves the failed Validation and old Plan review history, creates a new exact Plan revision/review, and then re-enters bounded Execution/Validation.

The same canonical lifecycle could use Retry Execution or Contract Change/G5; L1-L does not add a new route.

## 4. Governed health remediation

An Engineering Health Finding becomes normal governed work. The remediation:

- traces to the Finding and applicable baseline;
- uses a normal Plan/Increment/Task;
- executes under capability/authority boundaries;
- produces Evidence;
- receives independent Validation;
- records current disposition through later authoritative state rather than rewriting the original Finding.

## 5. Clean-room adoption proof

The reference harness assembles a distribution, including an exact release manifest and per-artifact SHA-256 inventory. A clean-room planning actor receives only:

1. that assembled distribution; and
2. a supplied OEB/Product baseline distinct from the bundled reference fixture.

It derives a normal `Plan [A1]`. An independent evaluator checks the existing Contract rubric:

1. semantic fidelity;
2. baseline comprehension;
3. capability binding completeness;
4. agent-access/entitlement correctness;
5. gap reasoning;
6. implementation credibility;
7. Evidence/Validation design;
8. traceability.

This reference harness proves the input boundary, reconstructability and rubric mechanics. It does not claim that every future model/provider automatically passes the fresh-session adoption test. A final Part 1 evidence package should additionally include a genuinely fresh external Human/agent run using the published release inputs.

## 6. Distribution integrity

The reference packager computes a provider-independent SHA-256 inventory over the exact packaged artifacts. SHA-256 is a reference implementation choice, not a mandatory Canonical technology. A conforming implementation may use another integrity/signing mechanism if exact payload identity and provenance remain verifiable.

## 7. Portability

The portability fixture proves equivalent canonical adoption results across two materially different provider/environment topologies without requiring the same:

- source control;
- CI/CD;
- Work Management;
- IAM/policy model;
- telemetry/knowledge provider;
- developer environment;
- bootstrap UX;
- agent runtime;
- model/provider.
