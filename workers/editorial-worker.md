# Editorial Worker — Contract

**Status:** Ratified. Promoted from `docs/drafts/OS-017_Editorial_Worker.md`
as part of the Architecture v1.0 freeze — see
`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md` for the decision record.
The pre-promotion draft text remains available via this file's git
history (`git log --follow workers/editorial-worker.md`); it is not
duplicated here.

## Mission

Transform an approved Reveal Brief into a production-ready Script
Package.

## Owns

- Script Package
- Editorial QA — satisfied internally by this Worker's own pipeline
  (Compliance & Fact-Checker and Critical Reviewer stages, per the
  approved Editorial Worker architecture), not produced as a separate
  artifact. This resolves what was previously a dangling, single-use term
  in `OS-017` with no defined content.

## Inputs

- Reveal Brief (approved/locked, post-Reveal human gate)
- Canonical documents
- Research Package — **referenced, not a trigger input.** Read by this
  Worker's Compliance & Fact-Checker stage to verify script claims trace
  to already-established evidence; does not initiate or gate this
  Worker's invocation.

## Outputs

- Script Package

## Rules

- Respect Constitution.
- Use Context Loader.
- Never invent facts.
- Never bypass human approval gates.
- Produce artifacts only through Production Contracts.
- Never modify the Reveal Brief it consumes.

## Ownership note

As of the Architecture v1.0 freeze, Reveal Brief moved to Research
Worker's ownership (`workers/research-worker.md`); it is no longer
produced or owned here. This Worker's remit now begins at an approved
Reveal Brief rather than a raw Research Package. See
`docs/adr/ADR-0002-Architecture-v1.0-Freeze.md` for the full reasoning.

**Explicitly deferred, not resolved by this change:** `OS-017`'s original
"Owns" list also included "S9 evaluation." This freeze does not decide
where S9 evaluation now belongs — most plausibly Research Worker's
Question Framer stage or a distinct, not-yet-specified Episode Selection
process, since Research Worker's own design already treats Episode
Selection as a precondition upstream of its own invocation. Recorded here
as an open item rather than silently reassigned or silently left with
this Worker.

## Internal organization

This Worker's internal pipeline (Script Writer, Compliance & Fact-Checker,
General Audience Reviewer, Retention Editor, Critical Reviewer, Lead
Editor — the latter three review stages run as isolated subagents) was
designed and approved separately and is not restated here — this file is
the Contract layer, not the implementation-grade specification. A future
`SPEC-Editorial-Worker-Script-Pipeline-v1.md`, written the same way as
`SPEC-Director-Worker-v1.md`, is the next step before any Skill is built,
and is not yet written.
