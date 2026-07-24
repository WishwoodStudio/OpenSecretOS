# Director Package Comparison — v1 vs v2 (Luxury Destruction)

**Status:** Production validation exercise. Not an architecture document,
not an ADR. Answers the six required questions below using only what was
actually found in the now-available Canonical Layer.

**What was read:** `Decision_Log_v2 (1).md`, `Visual_Identity_System_v2
(1).md`, `Mechanism_Ladder_v1.md`, `Content_Constitution_v4_DRAFT.md.docx`,
`Production_Playbook_v1.docx`. The two `.docx` files were unzipped and
their raw text extracted directly (no `pandoc`/Python available in this
environment) — this is noted for reproducibility, not as an engineering
concern.

**Critical finding, up front:** `Content_Constitution_v4_DRAFT.md.docx`
contains no actual content. Its entire extracted text is one sentence:
*"See content in downloaded file — Content_Constitution_v4_DRAFT.md"* —
a placeholder pointing to a `.md` file that does not exist anywhere in
this repository. Everywhere this report says "Constitution v4 could not
be verified," this is why.

---

## 1. Which parts changed?

Every file in `director-package-v2/` differs from `director-package-v1/`
in the same way: explicit canonical citations replace v1's repeated "none
available" notes. The underlying creative content — shot structure,
camera language, colors, typography, negative constraints — is
**substantively the same** in both versions. Specific differences:

- Every shot-list entry, prompt file, and the asset manifest now cites a
  real canonical rule where one applies, instead of stating no citation
  was available.
- A new, prominent runtime-compliance flag was added to the top of
  `shot-list.md` — this did not exist in v1 because v1 had no canonical
  runtime target to check against.
- `asset-manifest.md` gained a new note about the AI video generation
  stack naming mismatch (Runway/Kling vs. this repository's
  `higgsfield/` folder) — v1 couldn't surface this without Decision Log
  v2.
- `director-package.meta.json` version bumped to 2, status notes rewritten
  to record what was verified and what wasn't, and an explicit
  `supersedes` field added.
- Beat 8a/8b in the shot list gained an explicit caveat that their
  structural basis (source-claimed Constitution v4 §13 Rule 9) is
  unverifiable.

Nothing in the shot durations, VO breakdown, block assignments, or
prompt scene descriptions was changed.

## 2. Which changes were directly caused by canonical knowledge?

- The Purple Rule citation on Beat 6 (`Visual Identity System v2` §3 /
  `Decision Log v2`) — confirms, rather than assumes, that the source's
  single-purple-use design is canonically correct.
- The Hook Rule citation on Beat 1 (§5) — confirms the VO's ~2.6s landing
  time satisfies the canonical 3-second requirement.
- The "Real Artifacts First" citation on Beats 2–3 and in the asset
  manifest (§2) — confirms the two real-document choices over
  reconstructions are canonically preferred, not just a stylistic choice.
- Motion-principle citations throughout (push-in ranges, hard-cut
  default, 200ms cross-dissolve max, build-in timing, no-looping rule) —
  all §6.
- Color and typography citations (§3, §4) — every hex value and font
  choice in the source material matches the canonical table exactly.
- **The runtime-compliance flag** — this is the one change that
  materially affects production, not just documentation. It exists only
  because canonical knowledge was checked.

## 3. Which canonical documents influenced the output?

- **`Visual Identity System v2`** — heavily. Colors, typography, motion
  principles, hook patterns, the Purple Rule, Real Artifacts First, and
  the Publishing Technical Standards (including the runtime target) all
  came from this document.
- **`Decision Log v2`** — heavily. Independently confirms the Purple
  Rule, Hook Rule, Publishing Target (runtime), and color system; also
  the source of the AI-video-stack naming finding (Runway/Kling).
- **`Production Playbook v1`** — moderately. Confirms the 15-second block
  workflow and independently restates the 58–59s runtime target in its
  Publishing QA checklist — a third, independent confirmation of the
  same number.

## 4. Which canonical documents were not used?

- **`Mechanism Ladder v1`** — read in full, not used. It governs episode
  *selection* (which causal layer becomes Episode 1, mini-series
  planning) — a decision that already happened before this Production
  Package existed. Nothing in it applies to Direction-stage shot-list or
  prompt generation. This is a scope confirmation, not a gap.
- **`Content Constitution v4`** — intended to be used (the source package
  cites it by section number three times: §13 Rule 9, §8, §10) but
  **could not be used** — the file present in `canonical/` is an empty
  placeholder, not the actual document.

## 5. Did any contradictions between canonical documents become visible?

**Among the three documents that could actually be read, no
contradictions were found.** Decision Log v2, Visual Identity System v2,
and Production Playbook v1 agree with each other on every point checked
— runtime target, Purple Rule, Hook Rule, colors, typography, motion
principles. All consistent.

**The real contradiction is between the source Production Package's
claimed canonical basis and the actual canonical text.** The source
document states, in its own §11 preamble: *"The v1 package was built to
a runtime target ('58–59s hard') that Decision Log v2 has since
superseded with the Duration Philosophy (no fixed target — every second
earns its place, ≤3 min Shorts ceiling)."*

The actual `Decision_Log_v2 (1).md`, read directly, contains no concept
called "Duration Philosophy" anywhere. Its Publishing Target entry reads,
verbatim: *"1080×1920, 58–59 seconds, no Content ID" — Status: ACTIVE —
CANONICAL.* `Visual Identity System v2` §8 is even more explicit: *"58–59
seconds is a hard target. Videos over 60 seconds do not qualify as
YouTube Shorts... this eliminates Shorts discovery entirely."*

The source package used this unverifiable claim to justify growing the
episode from a 58s v1 to a ~76s v2. That growth is not supported by any
canonical document actually present in this repository. Whether a real
"Duration Philosophy" decision exists somewhere in the business's actual
records (outside this repository) is unknown from here — this report
only states what is and isn't verifiable against what's in `canonical/`.

## 6. Is the current Canonical Layer sufficient for Director Worker, or are additional canonical documents required?

**Not sufficient, for two distinct reasons:**

1. **Missing content.** Content Constitution v4 — the document the
   source material leans on most heavily for its structural requirements
   (Personal Consequence gate, Rolling Payoff Rule, Named Mechanism
   Requirement) — is present only as an empty placeholder. Director
   Worker cannot validate against rules it doesn't have.
2. **Unverifiable claims in upstream artifacts.** Even where canonical
   documents ARE present, this episode's own source material asserted a
   canonical change ("Duration Philosophy") that the real documents don't
   contain. If Director Worker trusts an upstream artifact's self-reported
   canonical basis instead of checking the actual canonical documents, it
   will silently produce non-compliant output — exactly what happened
   here until this comparison was run by hand.

`Mechanism Ladder v1` is not a gap — it's simply out of scope for this
pipeline stage, and its presence or absence doesn't affect Director
Worker's sufficiency one way or the other.

---

## What this report does not do

It does not resolve the runtime contradiction, does not fetch the real
Content Constitution v4, does not rename any Engine folder, and does not
propose an ADR or architecture change. Per this exercise's framing, these
are findings for review, not decisions made here.
