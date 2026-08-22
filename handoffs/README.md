# AE Session Relay — Simple Handoff Protocol

This branch is coordination state only. Do not merge it into `main`.

For every cross-session handoff:

1. The sending session writes the complete handoff payload verbatim to a uniquely named file under `handoffs/` on branch `ae-session-relay`.
2. The receiving session must fetch and read the entire designated file before acting. Do not rely on a summary or partial excerpt.
3. Repository claims in a handoff remain claims to verify independently where the receiving role requires review/verification.
4. When the receiving session completes its work, it writes the complete next handoff payload verbatim to a new uniquely named file under `handoffs/` on this branch.
5. The session then gives the Human Owner only:
   - a very short human-readable summary; and
   - a very short copy/paste block containing the next handoff title, repository, branch, and exact file path.
6. Do not overwrite prior handoff files. Preserve history.
7. If the designated handoff cannot be retrieved completely, stop rather than guessing or continuing from a summary.

The Human Owner remains the transport trigger between sessions for now; the branch carries the full payload.