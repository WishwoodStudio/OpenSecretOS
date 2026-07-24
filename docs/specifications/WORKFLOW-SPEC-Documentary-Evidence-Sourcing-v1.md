# WORKFLOW-SPEC: Documentary Evidence Sourcing v1

**Status:** Proposed — not yet ratified, not added to `canonical/`, not
added to `SPEC-001` or `SPEC-Director-Worker-v1`. Written the same way
as the other artifact/workflow specs discovered through real production
(`ARTIFACT-SPEC-Research-Fact-Audit-v1.md`,
`ARTIFACT-SPEC-Research-Package-v1.md`,
`ARTIFACT-SPEC-Opening-Typography-Package-v1.md`,
`ARTIFACT-SPEC-Thumbnail-Package-v1.md`). Unlike those, this one
documents a **process**, not a design deliverable — hence "WORKFLOW-SPEC"
rather than "ARTIFACT-SPEC."

**Promoted from PE-004, Finding 4** ("Supporting document workflow"),
following a knowledge integration review of that document. Promoted
because, unlike the other three findings in PE-004, this one has a
complete, already-executed, already-successful production trail behind
it — not just a proposal.

---

## 1. The problem this documents

Every episode using the "Real Artifacts First" priority (`Visual
Identity System v2` §2) needs real documentary evidence — screenshots
of primary source material — as overlays. Claude cannot reliably fetch
these itself.

**Real evidence, from Luxury Destruction:** Claude attempted to source
the Burberry Annual Report 2017/18 disclosure crop and a Richemont
buyback-figure crop directly. It located the real, correct source (a
`web.archive.org` snapshot of the actual Burberry annual report PDF,
after the live `burberryplc.com` URL returned HTTP 403). Every download
path then failed for concrete, structural reasons, not effort: `curl`,
`WebFetch`, and PowerShell `Invoke-WebRequest` all truncated the file at
exactly 1,048,576 bytes (a hard ~1MB outbound transfer limit in the
working environment), confirmed corrupt via direct PDF parsing (0
readable pages). A real browser reached the live document (no 403) but
triggered a native OS save dialog with no way to complete it
programmatically. This was documented at the time as a genuine,
reproducible blocker, not a one-off failure — logged in
`episodes/luxury-destruction/production-log.md`.

**What actually resolved it:** Eugene supplied two pre-processed
images (`burberry-evidence-v1.png`, `richemont-evidence-v1.png`) —
visibly styled screenshots (bordered card, drop shadow, highlighted
quote, source attribution footer), not raw captures — which Claude
placed directly into the episode's assets and the CapCut draft. That
integration was verified structurally (correct track, correct timing,
no gaps or overlaps introduced) in the same session.

This is the complete loop the workflow below formalizes: a real,
reproducible Claude limitation, and a real, already-proven fix.

## 2. The workflow

1. **Claude produces one consolidated request**, not a series of
   separate asks, listing every supporting document needed for the
   episode. For each: document name, page/section if known, the exact
   figure or sentence required (verbatim, not paraphrased), and why
   it's needed. This is not new practice — it's what Claude already had
   to work out precisely in order to search for the Burberry/Richemont
   material in the first place; this step just means writing it down as
   one deliverable instead of re-deriving it mid-investigation.
2. **The human captures the actual screenshots** — solves the fetch
   problem directly, since a human isn't subject to the same download
   restrictions Claude hit.
3. **An external tool converts raw screenshots into polished,
   production-ready evidence graphics** (the styling seen in the
   Luxury Destruction assets — bordered card, highlighted quote, source
   footer — is the working example of what this step produces).
4. **Claude inserts the finished assets into the edit** at the
   already-locked timing the Director Package or Assembly Package
   specifies — this step is unchanged from what already happened
   successfully.

## 3. What this replaces

Not a new requirement — a formalization of what step 2 of Luxury
Destruction's own real production already did once, reactively, after
Claude's own sourcing attempt failed. This makes it the first step
instead of the fallback, since the underlying constraint (Claude cannot
reliably download primary-source documents in this environment) is
structural and will recur for every future episode that needs real
documentary evidence, not specific to Burberry or Richemont.

## 4. Relationship to the Director Package

Referenced, not owned — same relationship as Voice Package, the CapCut
Assembly Package, the Opening Typography Package, and the Thumbnail
Package already have to Director Package.
`director-package-v*/asset-manifest.md` should cite the supporting
documents needed as a dependency on this workflow, rather than each
episode re-discovering the sourcing problem independently.

## 5. Repository location

This document: `docs/specifications/`, same location as the other
workflow/artifact specs. No per-episode instance folder is needed the
way Voice Package or the Thumbnail Package have one — this document
describes a *process* future episodes follow, not a deliverable with
its own versioned output; the deliverables it produces (the evidence
images themselves) already have a home
(`episodes/<episode-id>/assets/Supporting/`, established during Luxury
Destruction's own production).

**Not recommended:** `canonical/`, or merging into `Visual Identity
System v2` or `SPEC-Director-Worker-v1` directly — same standard as
every other proposed artifact/workflow spec in this repository.
