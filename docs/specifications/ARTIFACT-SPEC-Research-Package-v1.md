# ARTIFACT-SPEC: Research Package (v1, minimum viable)

**Status:** Artifact design only. Not registered as a Contract in
`engine/contracts/`, not added to `SPEC-001`'s Contract list, no Worker
designed. This is the first production version of the artifact, derived
entirely from one real failure — it is not a general-purpose Research
Package Contract, and later versions may need more than this once new
failures are observed. Nothing here should be read as final.

**Method:** every section below exists because a specific, already-observed
production failure traces to its absence. Sections that would be
reasonable in a general-purpose Research Package but aren't demonstrated
as necessary by this specific failure are listed at the end, explicitly
excluded, with the reasoning for excluding them — not silently omitted.

---

## Root cause, restated precisely

The Research Fact Audit for "The Giant Is The Hostage" found 10 of 13
claims Unsupported. The upstream material — an Editorial Board
comparison document — was never a Research Package: it asserted facts
with no citation apparatus at all, let one concept's unsourced facts
(Concept A) get silently reused inside the chosen concept (Concept B)
without their own sourcing ever being checked, and left room for two
more claims to be invented outright during script drafting with no
paper trail back to any prior document. A minimum viable Research
Package needs to close exactly these gaps — not be comprehensive.

## Section 1: Header

**Purpose:** give the Research Package a stable, citable identity.

**What production failure does this prevent?** Without one, nothing
downstream — the Fact Audit's own `Input Dependencies` field, or a
future Editorial Board comparison — has anything specific to cite as its
source. The Fact Audit artifact already assumes a "specific Research
Package version audited" exists to reference (`ARTIFACT-SPEC-Research-Fact-Audit-v1.md`
§5); for this episode, that reference didn't exist, and the audit had to
note the gap explicitly instead of citing anything. This section exists
so that never has to happen again.

**Required contents:** Artifact ID, Episode ID (or Topic ID, if produced
before an episode is assigned), Version, Date.

**Downstream artifact(s) that consume it:** Research Fact Audit (cites
this as its audited input); any Editorial Board comparison exercise
(cites this as the material it's comparing concepts *from*, not
restating facts independently of it).

## Section 2: Claim Inventory

**Purpose:** record every factual claim found during research, each
paired with either its actual primary source or an explicit statement
that none was found.

**What production failure does this prevent?** This is the section that
would have caught the actual failure directly. The 45% figure, and nine
other claims, were used across two full concept write-ups and two
produced script segments with zero citation anywhere — not weak
citation, none. A required field that must be filled with either a real
citation or the literal words "No primary source found" makes that gap
visible to whoever is about to build a concept on top of it, instead of
visible only after an audit run days or weeks later, once creative work
already depends on it.

**Required contents**, per claim:

| Field | Requirement |
|---|---|
| Claim ID | Stable, assigned here — not by whatever concept-comparison or Fact Audit consumes it later. This is what lets "Concept A's fact" and "Concept B's fact" be the same cited claim instead of two independently-asserted copies, which is exactly how an unsourced Concept A claim ended up silently inside the produced Concept B episode. |
| Claim text | Stated precisely enough to be checked — matching the discipline already established in the Fact Audit's own claim entries. |
| Primary source | The actual citation (document, filing, transcript, named source), **or** the literal statement "No primary source found." Never blank. Never asserted without one or the other. |

**Explicit rule, not a separate section:** a claim with no source is
still recorded, in full, exactly like a sourced one — it is not omitted,
softened, or hedged into vagueness to avoid an empty field. The
Editorial Board document's actual failure mode was treating "no research
performed" as a blanket disclaimer covering everything, rather than
marking each claim individually. This artifact does not allow that —
every claim carries its own answer.

**Downstream artifact(s) that consume it:** Research Fact Audit (checks
each cited source and assigns Verified / Partially Supported /
Unsupported — a judgment this section does not make itself); Editorial
Board comparison exercises (must cite Claim IDs from here rather than
asserting facts inline, so that whichever concept is chosen inherits
this section's sourcing state, not a fresh, unchecked restatement of it);
eventually, Editorial Worker and Director Worker, once a concept is
selected and a script is drafted, so that a script line can trace back
to a Claim ID instead of being written from memory of the concept
document.

---

## Explicitly excluded, and why

Each of these would be reasonable in a general-purpose Research Package.
None is included here because none is demonstrated necessary by the
actual failure — including them would be optimizing for completeness,
which this task explicitly rules out.

- **Research methodology / search process log** (what was searched, when,
  how). The failure wasn't "we don't know how the research was
  conducted" — it was "no source was attached to specific claims at
  all." A per-claim source field solves that; a full methodology trail
  doesn't add anything the evidence calls for.
- **Open Questions / Gaps section.** This is the Fact Audit's own job
  (`ARTIFACT-SPEC-Research-Fact-Audit-v1.md` §4, "Outstanding gaps").
  Duplicating it here, before any audit has actually happened, would
  blur the boundary between "what research found" and "what an
  independent audit judged," which this whole two-artifact split exists
  to keep separate.
- **Summary rollup / claim counts.** Considered and rejected: a count of
  sourced vs. unsourced claims might be a convenient at-a-glance signal,
  but the failure wasn't caused by nobody counting — it was caused by
  nothing being marked in the first place. A complete, honestly-marked
  Claim Inventory already makes the gap visible to anyone who reads it;
  a summary count is a nice-to-have, not a failure-preventing mechanism,
  and this task said not to add those.
- **Topic overview / background narrative.** Nothing in the observed
  failure traces to a missing summary of the topic — it traces to
  missing sourcing on specific claims. Not included.
- **Verification status per claim (Verified/Partial/Unsupported).** This
  is deliberately left to the Fact Audit, not duplicated here. The
  Research Package records what was found; the Fact Audit judges whether
  what was found actually supports the claim. Collapsing these into one
  step is closer to what already failed — the Editorial Board document
  asserted claims with an implicit, unexamined confidence level, rather
  than separating "what I found" from "whether it holds up."

## One limit this artifact does not solve, stated plainly

RFA-GIANT-009 and RFA-GIANT-010 (in the actual audit) were not carried
over from any prior document at all — they were invented during script
drafting itself. A well-built Research Package prevents claims from
entering *without* a source; it cannot, by itself, stop a later drafting
step from inventing a new claim and never checking it against this
document in the first place. That's a downstream consumption-discipline
problem, not a gap in this artifact's design — enforcing it would mean
designing Runtime or Worker validation behavior, which this task
explicitly excludes.
