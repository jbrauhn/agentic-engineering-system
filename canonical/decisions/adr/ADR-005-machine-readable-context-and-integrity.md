# ADR-005 — Machine-readable context semantics and context-integrity

**Status:** Accepted  
**Scope:** Canonical AE repository reference/executable layer for L1-G

## Context

L1-G introduces context/reconstruction semantics that are precise enough to test mechanically, but Canonical AE must remain neutral to retrieval, memory, RAG, vector, agent-framework, and interface technologies.

## Decision

Continue the staged machine-authority pattern established by ADR-002/003/004:

- Human L1-G semantic artifacts are normative for meaning.
- `context_protocol.json`, scenarios, and portability fixtures are conforming machine representations.
- `validate_context.py` is a repository/reference validator.
- GitHub Actions job `context-integrity` is repository CI.

The machine model proves semantic invariants; it is not a production context service, RAG stack, policy engine, or memory database.

The validator cross-checks existing lifecycle, capability, and authority machine artifacts where useful so context semantics cannot drift into a separate universe.

## Consequences

- Context Requirement, authority/currentness, promotion, Handoff, reconstruction, security, and portability become executable design claims.
- JSON/Python/GitHub Actions remain replaceable repository implementation choices.
- If `context-integrity` is introduced, issue #12 must track it but remain open until repository rules actually require applicable checks.
