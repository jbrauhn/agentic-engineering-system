# DR-117 — Effective OA/DA semantics and Authority Assignment

**Status:** Adopted — Human Owner L1-F approval

## Decision

Canonical AE distinguishes entitlement, Operational Authority, Decision Authority, and Authority Decision.

Operational Authority is the effective scoped authority of an actor to perform/request operational canonical AE actions under applicable context/conditions. Decision Authority is the effective scoped authority to make/approve governed decisions of a specified class.

Effective authority may be explicitly assigned, externally authoritative, or dynamically derived.

Introduce **Authority Assignment [A2]** when authority is explicitly issued, assigned, or delegated as independently meaningful governed state. The semantic type does not require AE-owned shadow copies of externally authoritative IAM assignments.

Canonical Human-reserved Decision Authority is limited to decision classes already established by Contract/adopted decisions; L1-F does not silently add new universal Human reservations.

## Consequences

- entitlement does not imply OA;
- OA does not imply DA;
- Authority Decision records an exercise of DA rather than becoming DA;
- explicit assignment/delegation can be durably represented without forcing all authority into grants;
- external/dynamic authority models remain conforming when their basis is reconstructable.

## Supersession

Future change to the core meanings of OA/DA or the admission of Authority Assignment should supersede this decision rather than silently altering L1-F artifacts.
