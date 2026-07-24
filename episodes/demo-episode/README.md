# episodes/demo-episode/

## Purpose
Not a real Open Secret episode. This workspace exists solely to prove
that Open Secret Engine can execute one complete production cycle
end-to-end — Production Package → Context Loader → Director Worker →
Director Package — per `docs/implementation/SPRINT-001.md`'s Sprint Goal.

## Ownership
Created and owned by SPRINT-001. Not part of the show's real production
slate; nothing here is meant to outlive the sprint that created it.

## What belongs here
- `fixtures/` — non-ratified stand-ins for canonical context (Visual
  Identity, Production Playbook), scoped to this workspace only. Not real
  canonical documents; see `canonical/README.md` for why they can't live
  in `canonical/`, and `docs/implementation/SPRINT-001.md` Task A1 for the
  reasoning behind this location.
- `script/` — a deliberately minimal, synthetic Script Package (Task C2),
  invented for this sprint. Does not resemble real Open Secret material.
- `director-package/` — the Director Package produced by running the
  pipeline against the above.

## What must never be stored here
- Real episode content — this is a test fixture workspace, not a
  production episode.
- Anything meant to be reused by other episodes (belongs in `assets/` at
  the repository root) or ratified canonical content (belongs in
  `canonical/`).

## Note on completeness

This workspace intentionally omits several components `SPEC-001` §16
requires for a real episode workspace (Research, Sources, Reveal Brief,
Voice Package, Assets, QA, Output, Postmortem) — see SPRINT-001 Task C1.
Full compliance with that structure is deferred to whichever sprint first
runs a real episode.
