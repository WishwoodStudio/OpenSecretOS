# PE-004 --- First Published Episode Production Findings

**Status:** Reviewed — partially integrated, partially deferred. Not
archived as-is: see the disposition note under each finding and the
**Review Outcome** section at the end. Original submitted status was
"Proposed production evidence"; this document now also records the
result of that proposal being reviewed.
**Episode:** Luxury Destruction

## 1. Increase visual cadence

A single 15-second AI shot with only a slow camera move feels less
dynamic than desired.

**Rule** - Use 2–3 distinct shots within every ~15-second AI block. -
Prefer scenes with visible activity (people, offices, traffic,
factories, movement). - Camera motion should complement scene changes,
not replace them.

> **Disposition: not promoted — duplicates existing evidence, does not
> add new validation.** This restates a finding that already exists
> twice in this repository, in more carefully hedged form: `docs/production-evidence/visual-language/PE-003_Shot_Duration_vs_Perceived_Dynamics.md`
> (status: "Hypothesis, not yet validated," written before any assembly
> existed) and `docs/production-evidence/PE-003_First_Full_Episode_Visual_Findings.md`
> (PE-003-01, written after the first assembly, still marked "not
> canonical rules... promote only after repeated production
> validation," explicitly requiring review "after 3–5 published
> episodes"). This entry states the same claim as a flat "Rule" without
> that hedging, but doesn't supply evidence beyond what those two
> documents already have. One episode has published. The threshold both
> earlier documents already set for themselves — repeated confirmation
> across multiple episodes — isn't met by restating the same
> observation a third time. `PE-003_First_Full_Episode_Visual_Findings.md`
> has been annotated to note this finding arrived again via PE-004; no
> new document created for it.

------------------------------------------------------------------------

## 2. Diagram ownership

Claude should produce a concise diagram brief describing the mechanism.

ChatGPT should generate the production-ready diagram.

Claude then inserts the finished diagram into the edit.

> **Disposition: not promoted — contradicted by what actually happened
> and worked.** For Luxury Destruction, the diagram
> (`assets/Generated/diagram/markdown-tax-diagram_v1.mp4`) was not
> produced this way. Claude designed and built it end-to-end using the
> `motion-graphics`/HyperFrames workflow — no ChatGPT handoff — and it
> passed the tooling's own lint and WCAG contrast checks plus a direct
> visual QA pass before being placed in the assembly. The workflow this
> finding proposes was not the one used, and the one actually used
> succeeded on the first real attempt. Promoting this finding would
> record a process this project has direct counter-evidence against.
> If a Claude-alone diagram workflow fails on a future episode, that
> would be real evidence worth writing up — this isn't that.

------------------------------------------------------------------------

## 3. Music workflow

A curated library of licensed YouTube Audio tracks already exists.

Remove music sourcing from the standard workflow.

Claude should specify only the desired mood, energy and timing.

> **Disposition: not promoted — untested in this project.** Luxury
> Destruction never actually reached this step: `EXPORT-V1-PREPARATION.md`
> and `episodes/luxury-destruction/production-log.md` both record the
> music bed as unselected and unsourced throughout this episode's
> production. The claim that a curated library exists may well be true,
> but nothing in this project's own evidence confirms a track was ever
> pulled from it and used. This is a claim about resource availability,
> not a production result — kept as evidence only until an actual
> episode exercises it.

------------------------------------------------------------------------

## 4. Supporting document workflow

Claude should produce one consolidated request containing every required
supporting document.

For each document specify: - document name; - page/section (if known); -
exact figure or sentence required; - purpose.

The human captures screenshots.

ChatGPT converts them into polished production-ready evidence graphics.

Claude inserts the finished assets into the edit.

> **Disposition: promoted.** Integrated into
> `docs/specifications/WORKFLOW-SPEC-Documentary-Evidence-Sourcing-v1.md`.
> See that document for the destination reasoning and the real
> production trail (the Burberry/Richemont sourcing blocker and its
> resolution) this finding is grounded in — this is the one finding in
> this set with a complete, already-executed, already-successful
> real-world example behind it, not just a proposal.

------------------------------------------------------------------------

## Promotion recommendation (original)

Do not promote these findings to canonical documents yet.

Validate them over the next 3–5 episodes. If consistently successful,
integrate them into the Production Playbook and Director Package.

## Review outcome (this pass)

The blanket "wait 3–5 episodes for everything" instruction turned out to
treat four findings of different evidentiary strength identically. On
review: one (#4) already has a complete, real, successful production
trail behind it and doesn't need to wait for repetition to be written
down — waiting would just risk it being re-derived from scratch next
time the same blocker recurs. One (#1) is a duplicate of existing,
already-more-carefully-hedged evidence and adds nothing new. One (#2) is
contradicted by what was actually built. One (#3) hasn't been tested at
all yet. None of this reopens or modifies any canonical document —
`WORKFLOW-SPEC-Documentary-Evidence-Sourcing-v1.md` lives in
`docs/specifications/`, the same non-canonical, proposed-and-referenced
location already established for the Opening Typography Package and
Thumbnail Package specs.
