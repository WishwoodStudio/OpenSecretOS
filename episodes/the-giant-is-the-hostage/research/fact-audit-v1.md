# Research Fact Audit — The Giant Is The Hostage (v1)

Produced per `docs/specifications/ARTIFACT-SPEC-Research-Fact-Audit-v1.md`,
exactly as written. First production execution of that artifact — no
changes made to the artifact's structure or field definitions.

## Header

| Field | Value |
|---|---|
| Artifact ID | `fact-audit-the-giant-is-the-hostage-v1` |
| Episode ID | `the-giant-is-the-hostage` |
| Version | 1 |
| Status | Generated |
| Owner Worker | Fact Audit Worker (not yet designed — per the artifact spec, this audit was produced by hand) |
| Input Dependencies | `episodes/OS_Research_MSFT_OpenAI_EditorialBoard_ConceptCompare_v1.md` — **note:** this is an Editorial Board comparison document, not a formal Research Package (`OS-013` Contract). No Research Package exists for this episode. This is the exact gap the artifact spec's own "Open questions" section flagged in advance; it is not resolved here, only encountered as expected. |
| Output Consumers | Editorial Worker, Director Worker, QA Worker (per the artifact spec §3) — none implemented; this audit is available for the human production process in the meantime |
| Last Updated | 2026-07-11 |
| Approval State | Draft |

**Scope note:** per instruction, no research was performed outside the
approved source material. All findings below reflect only what is or
isn't stated in the document above, plus the two already-produced
episode segments (`opening-00-15-version-b-FINAL.md`,
`opening-00-15-30-mechanism-reveal-v1.md`) that this audit checks
claims against. No claim's truth or falsity was assessed against outside
knowledge, and no claim's wording was changed, softened, or strengthened
in the course of this audit.

## Claim Inventory

`RFA-GIANT-001` through `010` — factual claims. `RFA-GIANT-011` through
`013` — editorial interpretations, tracked so they are never later
mistaken for facts requiring a source.

## Per-claim verification records

### RFA-GIANT-001
- **Claim text:** "Approximately 45% of Microsoft's future cloud revenue depends on OpenAI."
- **Origin:** Editorial Board document, Concept B hook specification and Reveal section.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** The document's own footnote references a separate, prior "primary-source-only fact audit" Board exercise that would be expected to contain this claim's sourcing. That document does not exist anywhere in this repository (confirmed by name, topic, and content search).
- **Expected usage:** Hook (00:00–00:05), reprised at Mechanism Reveal (00:12.0).
- **Auditor reasoning:** Full investigation already performed and documented — see `episodes/the-giant-is-the-hostage/research-gap-report-45-percent-claim.md`. This entry restates that finding in the artifact's required shape, per the artifact spec's own worked example.

### RFA-GIANT-002
- **Claim text:** "Microsoft's cloud revenue from this relationship is contracted to be earned for years into the future — a multi-year commitment, not a one-time or short-term arrangement."
- **Origin:** Editorial Board document, Concept B Reveal ("contracted to earn for years to come").
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No contract summary, filing, or analyst report establishing duration or terms is cited anywhere in the source material.
- **Expected usage:** Mechanism Reveal, 00:24.5 ("These aren't handshake deals. They're contracts running years ahead.").
- **Auditor reasoning:** Distinct from RFA-GIANT-001 — even if the 45% magnitude were independently verified, contract duration and formality is a separate assertion requiring its own evidence, and none is present.

### RFA-GIANT-003
- **Claim text:** "Microsoft's own quarterly profit swings by billions of dollars purely on OpenAI's fortunes."
- **Origin:** Editorial Board document, Concept B Reveal.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No earnings report, investor call transcript, or analyst commentary showing quarterly profit variance attributable specifically to OpenAI is cited.
- **Expected usage:** Not used in either segment produced so far. Present in the source's core Reveal text; plausible for a later beat.
- **Auditor reasoning:** This claim is arguably more specific and more falsifiable than RFA-GIANT-001 (it implies a measurable, recurring financial correlation across multiple quarters), yet has no more support in the source than the 45% figure — in fact less elaboration.

### RFA-GIANT-004
- **Claim text:** "ChatGPT has to keep paying [Microsoft] to keep running" — an ongoing, usage-based compute cost.
- **Origin:** Editorial Board document, Concept A Reveal (cross-borrowed into the Mechanism Reveal segment per that segment's own Editorial Reasoning table).
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No cloud-services agreement, billing structure, or technical/financial disclosure is cited.
- **Expected usage:** Underlies Mechanism Reveal 00:15.0 ("running under a contract Microsoft has already locked in to keep earning from for years") even though not quoted verbatim.
- **Auditor reasoning:** This claim's own evidentiary status was not separately assessed when the 00:15.0 line was drafted or revised — only RFA-GIANT-001-equivalent reasoning (the future-revenue link) was checked at that time. This audit is the first time RFA-GIANT-004 itself has been evaluated.

### RFA-GIANT-005
- **Claim text:** "Microsoft owns the machines/infrastructure that OpenAI's services run on."
- **Origin:** Editorial Board document, Concept A Reveal.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No infrastructure agreement, hosting disclosure, or technical documentation is cited.
- **Expected usage:** Mechanism Reveal, 00:15.0, directly — "that's Microsoft's own servers."
- **Auditor reasoning:** This is the single most load-bearing claim in the entire 00:15.0 line, and it has zero citation anywhere in the approved source material.

### RFA-GIANT-006
- **Claim text:** "Microsoft takes a cut of OpenAI's revenue."
- **Origin:** Editorial Board document, Concept A Reveal ("a cut of OpenAI's revenue"); also named as "revenue share" in Concept A's diagram description.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No partnership or investment agreement terms are cited.
- **Expected usage:** Mechanism Reveal, 00:20.0, directly — "Microsoft also takes a cut of OpenAI's revenue."
- **Auditor reasoning:** Directly underlies an already-locked VO line.

### RFA-GIANT-007
- **Claim text:** "Microsoft owns a stake in OpenAI now worth many times its original investment."
- **Origin:** Editorial Board document, Concept A Reveal ("a stake now worth many times the original check"); also "stake value" in Concept A's diagram description.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No valuation figure, funding-round data, or filing is cited for either the original or current stake value.
- **Expected usage:** Mechanism Reveal, 00:22.0 — "And owns a growing stake in the company."
- **Auditor reasoning:** The word "growing" in the produced line is itself a claim about value trajectory over time, not just stake existence — a stronger assertion than the source material's own "now worth many times" (a static comparison, not a trend), and equally unsupported.

### RFA-GIANT-008
- **Claim text:** "Microsoft's original investment in OpenAI was $13,000,000,000."
- **Origin:** Editorial Board document, Concept A hook specification and diagram description.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No filing, press release, or funding announcement is cited for this specific figure.
- **Expected usage:** Not used in either segment produced so far (00:00–00:30). Present in the source material as Concept A's own hook figure and shared factual context for the underlying relationship; plausible for future use if the script needs to establish the relationship's origin.
- **Auditor reasoning:** Included per the artifact's instruction to audit every claim "expected to appear," not only claims already scripted — this figure describes the same real-world relationship Concept B's episode is about, even though Concept A itself wasn't chosen.

### RFA-GIANT-009
- **Claim text:** "These aren't handshake deals. They're contracts running years ahead." — asserts formal, written, multi-year contracts, explicitly contrasted against informal agreements.
- **Origin:** Not present in the Editorial Board document. Added during script drafting (Mechanism Reveal, 00:24.5), extending RFA-GIANT-002.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** Same gap as RFA-GIANT-002, plus the specific "not handshake deals" contrast does not trace to the source material at all — it was added for rhetorical effect during drafting.
- **Expected usage:** Mechanism Reveal, 00:24.5 (already locked in the drafted segment).
- **Auditor reasoning:** Weaker evidentiary standing than RFA-GIANT-002 — part of this line's specific content isn't even an unsourced restatement of something the Board asserted; it's new content introduced during production.

### RFA-GIANT-010
- **Claim text:** "Walk away, and Microsoft breaks its own growth promise [to investors]."
- **Origin:** Not present in the Editorial Board document at all. Added during script drafting (Mechanism Reveal, 00:27.5) as an inference about how public companies communicate forward guidance.
- **Status:** Unsupported
- **Primary source(s):** None found.
- **Missing link:** No investor communication, earnings guidance, or analyst report establishing a specific Microsoft growth commitment tied to OpenAI is cited — because none is referenced in the source material at all.
- **Expected usage:** Mechanism Reveal, 00:27.5 (already locked in the drafted segment; already flagged NEEDS REVISION under that segment's own "Trust" self-review criterion).
- **Auditor reasoning:** The weakest claim in this entire inventory. Unlike RFA-GIANT-001 through 009, which at least appear as assertions in the approved source material (unsupported there, but present), this claim doesn't appear in the source material in any form. It is a production-judgement inference on top of an already-unsupported claim (RFA-GIANT-002), not even an unsourced restatement of something the Board itself asserted.

### RFA-GIANT-011 — Editorial Interpretation
- **Claim text:** "The Giant Is The Hostage" (episode title / framing metaphor).
- **Status:** Editorial Interpretation.
- **Reasoning:** Not a checkable factual claim — a narrative frame selected through the Editorial Board's own comparative process. Tracked here only so it is never later mistaken for a claim requiring a source.

### RFA-GIANT-012 — Editorial Interpretation
- **Claim text:** "Where is your 45%?" (personal consequence question).
- **Status:** Editorial Interpretation.
- **Reasoning:** A rhetorical device, not a claim requiring its own citation. Flagged dependency: its persuasive force rests entirely on RFA-GIANT-001, which is currently Unsupported — worth downstream Workers knowing even though this line itself isn't a fact to verify.

### RFA-GIANT-013 — Editorial Interpretation
- **Claim text:** "The bigger a single relationship becomes to you, the more it secretly controls you. Size isn't power — concentration is exposure." (transfer lens thesis).
- **Status:** Editorial Interpretation.
- **Reasoning:** A general principle/thesis statement, not a specific factual claim about Microsoft or OpenAI.

## Summary rollup

| Status | Count | Claim IDs |
|---|---|---|
| Verified | 0 | — |
| Partially Supported | 0 | — |
| Unsupported | 10 | RFA-GIANT-001 through RFA-GIANT-010 |
| Editorial Interpretation | 3 | RFA-GIANT-011 through RFA-GIANT-013 |

**Every factual claim currently expected to appear in this episode is
Unsupported.** This is not a partial gap concentrated in one figure — it
is the complete state of this episode's evidentiary base, given the
source material available. The Editorial Board document explicitly
disclaims research ("No research performed") for all of Concept A and
Concept B alike, and this audit confirms that disclaimer holds for every
individual claim checked, not just in general.

## Outstanding gaps

Grouped by root cause, not repeated individually:

1. **The referenced "primary-source-only fact audit" is absent.** Affects RFA-GIANT-001 and RFA-GIANT-002 directly (both are Concept B claims the footnote's convergence language most plausibly relates to). Resolving this means locating that document or reconstructing an equivalent one.
2. **No sourcing exists anywhere for Concept A's factual claims** (hosting, revenue share, equity stake, the $13B figure), despite three of them (RFA-GIANT-004, 005, 006, 007) now underlying already-locked lines in the Mechanism Reveal segment, cross-borrowed from a concept that wasn't even selected. Resolving this means sourcing Microsoft/OpenAI's actual infrastructure, revenue-share, and equity relationship independently — this was never in scope for the Board's editorial-comparison exercise to begin with.
3. **Two claims (RFA-GIANT-009, RFA-GIANT-010) were introduced during script drafting itself**, not carried over from the source material at all. These cannot be resolved by locating a missing Board document — they would need original sourcing from scratch, or removal/rewording if no source can be found.

## Sign-off

Audited by: Claude, per user instruction, as the first production
execution of `ARTIFACT-SPEC-Research-Fact-Audit-v1.md`. No claim was
weakened or strengthened in the course of this audit — every claim's
wording above matches its source (the Editorial Board document or the
already-drafted episode segments) exactly. No additional research was
performed outside the approved source material. This document does not
modify the artifact specification, the episode's locked or drafted
segments, or `SPEC-001`.
