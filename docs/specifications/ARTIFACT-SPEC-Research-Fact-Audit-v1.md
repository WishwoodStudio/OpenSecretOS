# ARTIFACT-SPEC: Research Fact Audit (v1)

**Status:** Artifact design only. Not registered as a Contract in
`engine/contracts/`, not added to `SPEC-001`'s Contract list, not
assigned to any Worker. This document defines the artifact a future Fact
Audit Worker would produce — it does not define that Worker, any
automation, or any Runtime behavior. `SPEC-001` is unmodified.

**Trigger for this design:** the Editorial Gate for "The Giant Is The
Hostage" found that its central statistic (45% of Microsoft's future
cloud revenue depending on OpenAI) had no cited primary source anywhere
in the available research material — see
`episodes/the-giant-is-the-hostage/research-gap-report-45-percent-claim.md`.
That investigation was performed by hand, once, for one claim. This
artifact is the durable, reusable form of that same check, so it doesn't
have to be redone by hand, once per claim, forever.

---

## 1. Purpose

Given a completed Research Package, record the verification status of
every factual claim expected to appear in the episode, so that every
downstream Worker (Editorial, Director, Voice, QA) can know which facts
are safe to build on **without re-deriving that judgment itself**. A
Fact Audit does not perform new research — it evaluates research that
already exists, claim by claim, against whatever primary sources can
actually be found for it.

## 2. Inputs

- **Research Package** — the Contract this audits (`SPEC-001` §10; one of
  OS-013's nine Initial Contracts).
- **Source Log / primary source inventory** — per `OS-016`, Research
  Worker's own outputs already include a "Primary source inventory" and
  "Confidence assessment" alongside the Research Package itself. A Fact
  Audit's natural first move is to check whether each claim in the
  Research Package is actually backed by an entry in that inventory, not
  just asserted alongside it.
- **Any primary sources** the Research Package or Source Log references
  by name (filings, transcripts, direct statements, prior Board
  exercises, etc.), to the extent they're actually available to check
  against.

## 3. Outputs

One Research Fact Audit document per Research Package version. Consumed
by:
- **Editorial Worker** — before committing a claim to the Script
  Package's actual dialogue.
- **Director Worker** — per `SPEC-Director-Worker-v1` §11, every prompt
  must already cite a Visual Identity rule or note none applied; the same
  discipline applies to factual claims a shot's on-screen text or VO
  states plainly.
- **QA Worker** — at Final QA, to confirm no Unsupported claim made it
  into the finished cut without being caught.

## 4. Required sections

1. **Header** — audit-level metadata (see §5).
2. **Claim Inventory** — every factual claim in the Research Package that
   is expected to appear in the episode, each assigned a stable Claim ID.
3. **Per-claim verification record** — one entry per claim (see §5 for
   fields).
4. **Summary rollup** — counts by status (Verified / Partially Supported
   / Unsupported / Editorial Interpretation), so a reader can assess the
   episode's overall evidentiary strength at a glance without reading
   every entry.
5. **Outstanding gaps** — claims that are Unsupported or Partially
   Supported, listed together, with what specifically would resolve each
   one (mirroring the "exact missing link" discipline already used in
   `research-gap-report-45-percent-claim.md`).
6. **Sign-off** — who performed the audit and when; this document's own
   Approval State (per OS-014's artifact lifecycle — Draft through
   Archived).

## 5. Required fields

**Document-level (once per audit), following OS-014's Artifact
Specification exactly:**

`Artifact ID` · `Episode ID` · `Version` · `Status` · `Owner Worker`
(placeholder until a Fact Audit Worker exists — not designed here) ·
`Input Dependencies` (the specific Research Package version audited) ·
`Output Consumers` · `Last Updated` · `Approval State`.

**Per-claim (repeated for every entry in the Claim Inventory):**

| Field | Purpose |
|---|---|
| `Claim ID` | Stable identifier downstream artifacts cite instead of restating the claim |
| `Claim text` | The claim as it appears (or will appear) in production material, stated precisely enough to be checked |
| `Origin` | Where in the Research Package this claim comes from |
| `Status` | One of the four values defined in §6 |
| `Primary source(s)` | Named source(s) if any were found, or explicitly "none found" |
| `Missing link` | Required whenever Status is not Verified — states precisely what evidence would be needed, not just that evidence is absent |
| `Expected usage` | Which part of the episode the claim is expected to support, once known (may be populated after the audit, by whichever downstream artifact uses the claim — see §7) |
| `Auditor reasoning` | Why this status was assigned, in enough detail that a second auditor could check the reasoning without redoing the search |

## 6. Validation status definitions

- **Verified** — a named primary source explicitly and directly supports
  the claim as stated, with no interpretive leap required. *Example
  (already in production): "Burberry burned £28.6 million of its own
  clothes," sourced directly to Burberry's Annual Report 2017/18
  disclosure line.*
- **Partially Supported** — a primary source supports part of the claim,
  a related metric, a different time period, or requires a real but
  defensible interpretive step to connect the source to the claim as
  stated. *Example (hypothetical): a source confirming "OpenAI is
  Microsoft's largest single cloud customer" without confirming the
  specific 45% figure — directionally supported, magnitude unverified.*
- **Unsupported** — no primary source was found; the claim is asserted
  without evidentiary basis. *Example (real, from this repository): the
  45% claim itself — see §8.*
- **Editorial Interpretation** — not a factual claim at all; a framing,
  metaphor, or narrative choice, explicitly labeled as such so it is
  never mistaken for something requiring a source. *Examples: "the giant
  is the hostage," "the markdown tax" — both coined frames, not
  checkable facts.*

A claim that cannot be cleanly sorted into one of the first three
categories, and is not clearly a framing device either, should be marked
**Unsupported** by default — this artifact's job is to make evidentiary
weakness visible, not to give an ambiguous claim the benefit of the
doubt.

## 7. Traceability requirements

- Every claim entry must carry a `Claim ID` stable enough that a Script
  Package or Director Package line can cite it directly (e.g., "supports
  Claim RFA-GIANT-001") instead of re-describing or re-justifying the
  claim.
- Every claim must trace to exactly one place in the source Research
  Package (`Origin`) — no claim should appear in an audit without a
  known point of origin.
- Every non-Verified claim must name what's missing, not just that
  something is missing — matching the standard already set in
  `research-gap-report-45-percent-claim.md` §3, which named the specific
  absent document rather than saying "more research needed."
- This artifact does not itself enforce that downstream artifacts cite
  Claim IDs back — that would require Runtime/validation behavior, which
  is explicitly out of scope here. The traceability requirement is a
  property the artifact's *design* must support; enforcing it is a
  future concern for whichever Worker and validation logic eventually
  consumes this artifact.

## 8. Example: the Microsoft/OpenAI 45% claim

```
Claim ID: RFA-GIANT-001
Episode ID: the-giant-is-the-hostage
Claim text: "Approximately 45% of Microsoft's future cloud revenue
  depends on OpenAI."
Origin: episodes/OS_Research_MSFT_OpenAI_EditorialBoard_ConceptCompare_v1.md,
  Concept B hook specification and Reveal section
Status: Unsupported
Primary source(s): none found
Missing link: The source document's own footnote references a separate,
  prior "primary-source-only fact audit" Board exercise that would be
  expected to contain this claim's sourcing. That document does not
  exist anywhere in this repository (confirmed by name, topic, and
  content search).
Expected usage: Hook (00:00–00:15), Mechanism Reveal (00:15–00:30) —
  both already produced and pending this claim's resolution
Auditor reasoning: see episodes/the-giant-is-the-hostage/
  research-gap-report-45-percent-claim.md for the full investigation;
  this entry is that report's finding, restated in this artifact's
  required shape.
```

## Open questions this design surfaces, not resolved here

- `OS-016` already lists "Confidence assessment" as one of Research
  Worker's own outputs. Whether a Fact Audit *is* that confidence
  assessment, formalized, or is a distinct second pass performed later
  by a different Worker, is not decided by this document — flagged for
  whoever designs the actual Fact Audit Worker.
- The source material available for "The Giant Is The Hostage" is an
  Editorial Board comparison document, not a Research Package in
  `OS-013`'s formal sense. This artifact's Input (§2) assumes a proper
  Research Package exists; applying it to the material actually on hand
  for this episode would itself require a judgment call this design
  doesn't make.
- No file path convention is mandated here, but `episodes/<episode-id>/research/`
  (an already-required Episode Workspace component per `OS-005`) is the
  natural home, consistent with where Research Package itself belongs —
  noted as a suggestion, not a Runtime or Engine decision.
