# L1-D — Lifecycle State Ownership Matrix

**Status:** Approved L1-D semantic baseline  
**Scope:** Clarifies where canonical lifecycle truth lives and where provider state may participate without becoming canonical AE truth.

| Scope / object | Canonical lifecycle/state semantics | Primary responsibility | Authoritative-source expectation | Provider participation |
|---|---|---|---|---|
| **AE Loop** | OPEN / SUSPENDED / CLOSED + terminal disposition ACCEPTED / CANCELLED / SUPERSEDED | R1 | Conforming implementation must be able to establish current Loop control state and reconstruct transition history | Work Management or another provider may store/project state, but provider status alone is not canonical truth |
| **Contract revision** | draft/proposed/approved/superseded semantics inherited from Contract decisions; immutable approved revisions | R2 + R4 + R1 | Exact approved revision and approval provenance must be determinable | Source Control/artifact system may remain authoritative for content; authority record may live elsewhere |
| **Plan revision** | draft/reviewed/superseded semantics plus exact Plan Review coverage | R2 + R1 | Review validity resolves to exact Plan Review Record + exact Plan revision + review scope | Work Management/source control can represent plan state; editable provider status does not replace review record |
| **Product/System Baseline revision** | exact baselined revision used by governed Planning/Execution scope | R2 | Exact revision must remain determinable at governance boundaries | May be represented by Baseline Manifest and references to provider-owned state |
| **Execution Increment — L2** | active position PLANNING / READY / EXECUTING / VALIDATING; terminal disposition ACCEPTED / CANCELLED / SUPERSEDED; orthogonal blocking | R1 + R2 + R6 | Canonical scope state and governing exact Contract/Plan/Baseline revisions must be reconstructable | Work Management can project or assist, but canonical meaning survives provider replacement |
| **Executable Task — L3** | NOT_STARTED / ACTIVE / COMPLETE + orthogonal blocking where needed | R1 + R2 + R5 | Only AE-required portable execution state is canonical | Provider Work Item may remain authoritative for rich workflow status, assignment, comments, timestamps, provider dependencies, etc. |
| **L4 micro-plan** | ephemeral operating state | executing actor | No durability requirement unless material information is promoted to the correct durable entity/record | Local agent/runtime state only |
| **Plan Review Record** | issued immutable A2 governance record | R2/R1 | Exact review record is authoritative for what Plan revision/scope was reviewed and dispositioned | May be stored in source control, work management, review system, etc. |
| **Authority Decision** | issued immutable A2 governance record | R4 | Exact decision is authoritative for approval/rejection/authority disposition | Identity/policy/work systems may participate |
| **Evidence Record** | issued immutable A2 provenance/reference | R6/R2 | Record preserves what evidence existed and where; bytes may remain external | CI/CD, test, observability, artifact providers may remain authoritative for evidence data |
| **Validation Record** | issued immutable A2 independent judgment | R6 | Exact Validation Record is authoritative for acceptance/rejection of a declared scope against exact Contract/Proof/evidence | Validation provider may execute checks, but provider status does not substitute for AE judgment semantics |
| **Gate projection** | SATISFIED / UNSATISFIED / UNKNOWN | R1 with relevant responsibility | Must resolve to authoritative records/revisions/evidence; is not independently editable truth | Cached/displayed anywhere |
| **Blocking condition** | scope-aware condition preventing protected transition | R1/R4/R5 depending cause | Must be reconstructable with reason, scope, and prerequisite/decision needed | Provider `Blocked` may map to it only where semantics align |
| **Provider workflow status** | provider-owned operational state | provider + R5 binding | Provider may remain authoritative for declared provider properties | Never automatically equals canonical AE lifecycle/Validation state |

## 1. Anti-shadow rule

AE does not replicate provider workflows merely to make lifecycle state convenient to query.

Examples:

`Plane Done` may map to `Task COMPLETE` when the Capability Binding establishes that mapping.

It does **not** imply:

- Increment ACCEPTED;
- Validation accepted;
- Loop CLOSED / ACCEPTED.

Those require their own canonical semantics and authoritative records.

## 2. Scope and revision ownership

Every governed active L2 Execution/Validation scope must expose or resolve:

- governing exact Contract revision;
- governing exact Plan revision where applicable;
- exact Product/System Baseline revision where applicable;
- applicable gate records;
- blocking/effectivity conditions.

The Loop may therefore correlate multiple active scopes using different exact Plan revisions and, during an explicitly governed Contract revision transition, different exact Contract revisions.

## 3. Derived phase summary

A Human-facing statement such as:

`Loop active: Planning + Execution + Validation in progress`

is a D/derived projection from the scoped facts above. It is not a separate source of lifecycle truth.
