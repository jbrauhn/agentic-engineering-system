# L1-C — Entity Classification & R1–R7 Ownership Matrix

**Status:** Approved L1-C semantic baseline  
**Scope:** Classification, governing responsibility, durability, authoritative-source semantics, and key relationships for canonical L1-C objects.

## 1. Reading the matrix

- **Primary responsibility** means the R1–R7 responsibility that governs the object's canonical semantics. It does not imply a storage component.
- **Collaborators** identify other responsibilities that materially participate.
- **Authority/source** follows DR-107 federated authoritative state; physical storage may remain distributed.
- **Exact revision at governance boundary** indicates that authority/review/Validation references must identify exact revisions where state-dependent meaning matters.

## 2. A1 — First-class durable entities

| A1 entity | Why independent identity is required | Primary | Collaborators | Authoritative-source semantics | Mutability | Provider state participates? | Exact revision at governance boundaries? |
|---|---|---|---|---|---|---|---|
| Organization Engineering Baseline | Evolves independently; reused across products/Loops; adoption claims need exact baseline | R2 | R4, R5, R7 | Declared authoritative revision/source for OEB; may reference external policy/standard/provider facts | Versioned governed | Yes, by references/config sources | Yes |
| Product/System Profile | Durable representation of external target reused across Loops | R2 | R3, R7 | AE-governed profile revision; may reference external system sources | Versioned governed | Yes | Yes when Planning/Validation depends on state |
| AE Implementation Profile | Durable representation of declared implementation scope/configuration/claim | R2 | R4, R5, R6 | Profile is authoritative for declared configuration/scope; conformance is supported by Validation, not editable truth | Versioned governed | Yes | Yes for adoption/conformance evaluation |
| Capability Binding | Independently changing mapping from canonical operation to provider mechanism | R5 | R2, R4 | Binding revision/source authoritative for declared provider mapping/scope | Versioned governed | Yes, centrally relevant | Yes for governed invocation/Proof |
| Product/System Baseline — L1 | Persistent baselined system state that Plans plan against across Loops | R2 | R3, R7 | Baseline revision identifies authoritative revisions of constituent persistent state; Baseline Manifest is representation | Versioned governed | Yes via referenced constituent sources | Yes |
| AE Loop | Durable correlation for one bounded lifecycle execution | R1 | R2, R3, R4, R5, R6, R7 | R1 governs Loop state/transition meaning; persistence may be distributed | Operational stateful | Yes | Yes for referenced Contract/Plan/Baseline at gates |
| Contract | Goal+Spec+Proof; exact approved revision controls work/Validation | R2 | R1, R4, R6 | Declared Contract source; approved revision immutable | Versioned governed | May be stored externally | Yes — mandatory |
| Contract Change Proposal | Independent proposal/rationale/diff/disposition target | R2 | R4, R1 | Proposal source authoritative for submitted revision; disposition via Authority Decision | Versioned until submission; issued proposal revision frozen | May reference external evidence/work | Yes |
| Plan | Governed route from Contract to Proof; independently reviewed/revised | R2 | R1, R3, R4, R5, R6 | Canonical Plan revision independent of its representations | Versioned governed | May have external representations | Yes — mandatory for Plan Review/execution gates |
| Execution Increment — L2 | Bounded delivery unit with durable decomposition/dependencies/outcome | R2 | R1, R5, R6 | AE canonical increment state; operational properties may reference provider state | Operational stateful / versioned as needed | Yes | Yes when review/evidence meaning depends on revision |
| Executable Task — L3 | Portable task semantics independent of Work Management object | R2 | R1, R5, R6 | AE owns minimal canonical Task semantics; provider may own selected operational fields | Operational stateful | Yes — via External Resource Reference | Yes when evidence/authority depends on task state |
| Architecture Model | First-class structural system representation across Loops | R2 — Architecture Model Stewardship | R3, R6, R7 | Declared current/baselined Architecture Model revision; representation source may vary | Versioned governed | Yes, external modeling source possible | Yes for Planning/ADR/Validation where architecture state matters |
| Experiment | Formal experiment has lifecycle from question through conclusion | R7 | R2, R6 | Experiment record/source plus referenced provider measurements/evidence | Operational stateful then concluded/frozen | Yes | Yes for concluded results/decisions |

## 3. A2 — First-class durable records

| A2 record | Why independent identity is required | Primary | Collaborators | Authoritative-source semantics | Mutability | Provider state participates? | Exact target revision required? |
|---|---|---|---|---|---|---|---|
| Decision Record / ADR | Consequential rationale persists/references independently across Loops | R2 | R3, R7 | Issued DR/ADR record is authoritative for what was decided; later change uses supersession/new record | Issued immutable | May cite provider evidence | Yes when decision targets revisioned state |
| Authority Decision | Proves eligible authority approved/rejected exact target | R4 | R1, R2, R5 | Issued authenticated decision record; may integrate external approval provider | Issued immutable | Yes | Yes — mandatory when target is revisioned |
| Plan Review Record | Independent review of exact Plan revision is durable gate evidence | R2 | R1, R6 | Issued review record/source | Issued immutable | Possible external reviewer/work system | Yes — mandatory |
| Evidence Record | Material evidence provenance/reference survives even when bytes remain external | R6 | R2, R5, R7 | Issued Evidence Record records source/context at issuance; external evidence source may remain authoritative for bytes/data | Issued immutable; later assessment separate | Yes — expected | Exact related revisions as needed |
| Validation Record | Independent outcome judgment must be reconstructable exactly | R6 | R1, R2, R3, R4 | Issued Validation record authoritative for that judgment/outcome; evidence remains separately sourced | Issued immutable | Yes | Yes — Contract/Proof and other state as applicable |
| Handoff Record | Durable continuation boundary across actor/session replacement | R3 | R2, R1 | Issued handoff references authoritative state; does not replace it | Issued immutable/correct by supersession | May reference provider work/context | Yes where continuation depends on exact revision |
| Learning Record | Durable conclusion can influence future work independently of source Loop/Experiment | R7 | R2, R3 | Issued learning record with evidence/source provenance; later correction/supersession separate | Issued immutable | May reference telemetry/evidence | Exact source revision where material |

## 4. B — Canonical subordinate/value concepts

| B concept | Parent/scope | Primary | Persistence expectation | Notes |
|---|---|---|---|---|
| Goal | Contract revision | R2 | Durable within Contract | No global identity needed |
| Spec / Spec Statement | Contract revision | R2 | Durable within Contract | Statements can have stable scoped IDs |
| Non-goal | Contract revision | R2 | Durable within Contract | Scope boundary |
| Proof / Proof Criterion | Contract revision | R6/R2 | Durable within Contract | Proof Criterion must be stably addressable within exact Contract revision |
| Loop Context | AE Loop | R1/R3 | Durable Loop state as required | Classification/context semantics, not separate global entity |
| Loop Transition Event | AE Loop | R1 | Append-only/reconstructable | Scoped event identity sufficient |
| Planning Depth / Method | Plan revision | R2 | Durable within Plan | Preserves inherited Planning model |
| Verification/Test Strategy | Plan revision | R6/R2 | Durable within Plan | Derived from Proof; does not move Proof into Plan |
| Architecture Element | Architecture Model | R2 | Durable/addressable within model | Stable element identity scoped to logical model/target |
| Architecture Relationship | Architecture Model | R2 | Durable/addressable within model | Typed subordinate relationship |
| Plan Review Finding | Plan Review Record | R2 | Durable within issued review | No separate global identity unless later lifecycle justifies promotion |
| Evidence Set | Validation context | R6 | Durable as part of Validation/reference selection | Individual Evidence Records remain A2 |
| Standards Applicability State | OEB/Product/Baseline scope | R2 | Durable hook | L1-E decides whether promotion to A2 is needed |
| Conformance projection/status | AE Implementation Profile | R6/R2 | Derived from authoritative Validation | Must never be editable independent truth |

## 5. C / D / E / F ownership summary

### C — External Resource Reference

- **Primary:** R5 for provider binding/operation context; R2 for durable identity/traceability relationships.
- **Authority:** provider remains authoritative for declared external properties.
- **Durability:** reference persists whenever a canonical relationship depends on the external resource.

### D — Derived views/projections/context products

- **Context Package:** R3; disposable/reconstructable; consequential provenance hook required.
- **Dashboards/summaries/indexes/vectors/IGs/generated architecture visualizations:** owning semantic source depends on underlying state; derived object is not authoritative by default.
- **Conformance projection:** R6→AE Implementation Profile; authoritative basis is installation/adoption Validation.

### E — Ephemeral operating state

- **L4 agent micro-plan:** executing actor/runtime; no durability requirement by default.
- Material information must be promoted to the appropriate A1/A2/B object.

### F — Normative definitions/release objects

- **Primary:** Canonical Distribution governance rather than one operational R1–R7 runtime responsibility.
- Organization implementations reference exact normative release/type/capability definitions and may not mutate them.

## 6. Key relationship expectations by entity

Every A1/A2 object shall eventually support the relationships necessary to reconstruct its place in AE without relying on filenames or document nesting.

Examples:

- OEB → used_by → AE Implementation Profile;
- Product/System Profile → included_in/referenced_by → Product/System Baseline revision;
- Product/System Baseline revision → plans_against ← Plan revision;
- AE Loop → uses → exact Contract and Plan revisions;
- Plan → decomposes_to → L2 Increment;
- L2 → decomposes_to → L3 Task;
- L3 Task → realized_by → External Work Resource Reference;
- Evidence Record → supports → Proof Criterion;
- Validation Record → evaluates → exact Contract revision and uses → Evidence Records;
- Decision Record/ADR → affects → Architecture Element / Plan / capability or other target;
- Learning Record → informs → Decision/Planning/guidance.

## 7. Engineering Team Interface / Working Environment hook

Open issue **#6** is intentionally not represented as a new A1 entity.

Potential future references/configuration hooks may attach to:

- AE Implementation Profile;
- Capability Binding;
- OEB;
- Product/System Profile/Baseline;
- Context/Handoff mechanisms;
- authority/policy configuration.

L1-C keeps those objects extensible without assuming Dev Containers, one IDE, one CLI, one Portal, one local daemon, or one agent host.