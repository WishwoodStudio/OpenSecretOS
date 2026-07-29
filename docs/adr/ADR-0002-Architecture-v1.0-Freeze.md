# ADR-0002: Research/Editorial Worker Ownership Boundary, and Architecture v1.0 Freeze

**Status:** Accepted
**Date:** 2026-07-24

This record documents two related decisions made together: a specific
ownership boundary change between Research Worker and Editorial Worker,
and the decision to declare the repository's architecture frozen at
v1.0. Like `ADR-0001`, this is not a changelog of files touched — it is
the reasoning a future maintainer needs to extend this system without
re-litigating settled ground.

---

## Context

Following the initial repository audit, a cleanup pass, and the design of
two new subsystems (a Competitive Intelligence subsystem, not yet
implemented, and the Reveal Brief → Script Package pipeline for Editorial
Worker), the Editorial Worker design surfaced a direct conflict: its own
internal Compliance & Fact-Checker stage needs to read Research Package
for claim-traceability, yet `OS-016_Research_Worker.md` explicitly listed
"reveal framing" under "Never owns," while `OS-017_Editorial_Worker.md`
listed Reveal Brief as something Editorial Worker owns and produces.

Designing Research Worker properly required resolving this before
building it, not after. The repository owner reviewed the proposed
resolution and approved it explicitly, which is the ratification trigger
for everything below — per `OS-004`'s promotion model, ratification has
always required a human decision; this is one.

## Decisions

### 1. Reveal Brief ownership moves from Editorial Worker to Research Worker

Research Worker's remit now runs from a raw topic through an approved
Reveal Brief. Editorial Worker's remit now begins at an approved Reveal
Brief and ends at Script Package.

**Rationale:** Not asserted from first principles — justified by this
repository's own production evidence, per `OS-004`'s own standard for
what's allowed to change an ownership boundary. The one complete,
real reveal-development pipeline this project has actually run
(`unsorted/Research_Dollar_Dominance_DRAFT.md` →
`Research_Dollar_Dominance_Round2_DRAFT.md` →
`Editorial_Review_Dollar_Dominance_DRAFT.md` →
`Editorial_Board_Dollar_Concept_Selection_DRAFT.md` →
`Reveal_Brief_v1.md` → only then `Script_v1.md`) shows reveal-selection
finishing entirely on the research side before any script drafting
starts. `episodes/the-giant-is-the-hostage/`'s own `metadata.md` records
that workspace as being at "Reveal stage," with no script yet — the same
shape in miniature. Reveal-selection has never actually happened inside
the scripting stage in this project's real history.

There is also a direct One Responsibility argument underneath the
evidence: finding the strongest reveal requires holding the full research
corpus — every competing explanation, every piece of counter-evidence —
not a downstream summary of it. Scripting is a different skill (prose,
pacing, retention) applied to an already-decided reveal. Splitting on
"is the reveal decided yet" is a cleaner seam than splitting on "which
document type is being touched."

### 2. Research Package becomes a referenced, non-trigger dependency for Editorial Worker

Editorial Worker's Compliance & Fact-Checker stage still reads Research
Package directly, for claim traceability during script drafting. This
mirrors the relationship Director Package already has to Voice Package
and the Opening Typography Package ("referenced, not owned") — no new
relationship type was invented.

### 3. `OS-016` and `OS-017` are promoted out of `docs/drafts/` into `workers/`

Per `docs/drafts/README.md`'s own existing rule ("anything already
ratified — move it to its proper category instead"), the two drafts were
moved (not copied) to `workers/research-worker.md` and
`workers/editorial-worker.md`, correcting the ownership boundary as part
of the promotion. Their pre-promotion text is preserved via git history,
not duplicated as a second, marked-superseded copy — consistent with how
this repository already treats git as the record of "what a document
used to say," rather than inventing a parallel in-repo archival
convention for file-level promotions specifically. (`canonical/Decision_Log_v2`'s
SUPERSEDED-entries-kept-forever convention is a different mechanism,
for entries within one continuously-updated document — not in tension
with this.)

`workers/` was chosen as the destination, not `docs/specifications/`,
because `workers/README.md` has stated since this repository's first
commit that "this folder holds the *contract* for each worker" — a
promise this promotion is the first thing to actually fulfill.

One incidental resolution came along with this promotion: `OS-016`'s
"Topic or Production Package" input phrasing — already flagged as an
open item in `docs/architecture/Architecture-Gap-Analysis-001.md` §4 Tier
2 and named directly in that document's §6 recommended action 4 ("when
Research Worker's specification is eventually written... resolve
OS-016's 'Production Package' phrase explicitly") — is resolved to
"Topic" alone in `workers/research-worker.md`. This was already decided
in principle by Gap Analysis 001; this promotion is where it was
finally written down.

### 4. `OS-017`'s "S9 evaluation" ownership is explicitly deferred, not resolved

This freeze does not decide where S9 evaluation (the topic-scoring gate
that precedes Episode Selection) now belongs. It is recorded as an open
item in `workers/editorial-worker.md` rather than silently reassigned to
Research Worker or silently left with Editorial Worker. Most plausibly
it becomes part of Research Worker's Question Framer stage or a
distinct, not-yet-specified Episode Selection process — but that is a
future decision, not this one.

### 5. `OS-017`'s "Editorial QA" is resolved

This dangling term (present in `OS-017` with no defined content, flagged
in the original repository audit as appearing nowhere else) is now
satisfied by the approved Editorial Worker pipeline's Compliance &
Fact-Checker and Critical Reviewer stages, recorded as such in
`workers/editorial-worker.md`. It is not a separate artifact.

### 6. The repository's architecture is declared **OpenSecretOS Architecture v1.0 (Frozen)**

No further architectural redesign should be proposed on this repository
unless real implementation experience or production usage demonstrates a
concrete deficiency. Improvements identified in the meantime are backlog
items, not immediate redesigns — the same production-evidence standard
`OS-004` already requires before promoting an idea into `canonical/` is
now applied reflexively to the architecture itself.

This freeze covers the ownership and Contract structure recorded in
`workers/README.md`, `workers/research-worker.md`,
`workers/editorial-worker.md`, `docs/specifications/SPEC-Director-Worker-v1.md`,
and `docs/specifications/SPEC-001_Open_Secret_Engine_v1.md` §9/§10. It
does **not** freeze implementation detail that doesn't exist yet
(`SPEC-Research-Worker-v1.md`, `SPEC-Editorial-Worker-Script-Pipeline-v1.md`,
and both Workers' Skills are still unwritten) — those are expected to be
built next, against this now-stable ownership model, not redesigned as
they're built.

## Consequences

- Implementation of Research Worker and Editorial Worker can now proceed
  against a settled ownership model instead of a contradiction between
  two drafts.
- A repository-wide consistency check was performed alongside this
  decision (files checked, changed, and left alone are enumerated in the
  accompanying Architecture Freeze Report, delivered separately from this
  ADR per this repository's own practice of keeping engineering decision
  records — this file — distinct from audit/status reports).
- Several pre-existing inconsistencies, unrelated to this specific
  ownership change, were identified during that check and were
  deliberately **not** fixed as part of this freeze: `OS-008`'s abandoned
  granular worker taxonomy (Episode Selection Worker, Reveal Worker,
  Script Worker — already contradicted by the real registry before today,
  not made worse by this change), the QA Report/QA Package naming split
  (`OS-008` vs. `OS-007`/`OS-013`/`SPEC-001`), the dangling "Subtitle
  Package" term in `OS-007`, the `Content_Constitution_v4_DRAFT.md.docx`
  stub, the IKEA/Norway provenance question in `canonical/Decision_Log_v2`,
  and several stale population claims in `SPEC-001` §15/§16/§21 and
  `docs/implementation/MILESTONE-001-REVIEW.md` (both describe `canonical/`
  and `episodes/` as emptier than they now are). These remain open,
  tracked as backlog per Decision 6's own standard, not silently
  accepted as permanently unaddressed.
- Future contributors proposing a different Research/Editorial ownership
  split should re-read Decision 1's evidence rather than re-derive the
  question from architecture-level reasoning alone — the standard this
  repository now holds itself to is production evidence, and re-opening
  this without new evidence would be exactly the kind of premature
  redesign Decision 6 exists to prevent.
