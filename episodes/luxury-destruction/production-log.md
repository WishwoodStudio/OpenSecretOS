# Production Log — Luxury Destruction

Chronological record of obstacles and findings encountered while
processing this episode. Per the current phase's rule: architecture
changes require production evidence, and this log is that evidence.
Nothing below has triggered an architecture change — each entry states
the finding and stops there, pending review.

## 2026-07-11 — Source Production Package received

`OS_Production_Package_LuxuryDestruction_v2.md` was placed directly in
this episode's workspace. It is the first real (non-demo, non-synthetic)
production content this repository has processed. Filed to
`source/`, treated as immutable.

## 2026-07-11 — Finding 1: referenced canonical documents don't exist here

The source document names its canonical basis explicitly: Content
Constitution v4, Decision Log v2, Visual Identity System v2 (§7B
applied), Production Playbook v1, Mechanism Ladder v1, S9 Scorecard v1.
None of these exist in `canonical/` in this repository — confirmed empty
throughout this entire sprint.

**Consequence:** the Director Package produced from this source (see
`director-package/`) extracts the source's own already-made creative
decisions faithfully, but this repository cannot independently verify
those decisions against the real canonical text, because that text isn't
here. `SPEC-Director-Worker-v1` §11's validation rule — "every prompt
must cite a Visual Identity rule" — could not be satisfied against a real
document; each prompt file instead states plainly that no Visual Identity
citation was available.

**Architecture impact: none proposed.** This is a content-availability
gap, not a design flaw — nothing about the Engine's structure prevented
this from working; it simply doesn't have the real documents yet.

## 2026-07-11 — Finding 2: the real Production Package is one monolithic document, not separated Contracts

The source document, in a single file, contains content spanning what
this repository's architecture treats as several distinct Contracts:
the script (Script Package's scope), the shot list/camera
language/prompts/asset manifest (Director Package's entire scope), the
narration and pronunciation notes (Voice Package's scope, §11 of the
source), and metadata/QA-checklist/risk content adjacent to Publishing
and QA. It was not produced as separate documents that later get
combined — it's authored as one continuous package.

**Consequence:** producing a Director Package for this episode required
manually splitting one real document into several artifacts this
repository's architecture expects to be distinct. That split was
mechanical (extraction, not new creative work) but was real, non-trivial
effort, and every extracted artifact now needs to be kept in sync with
the same immutable source by hand, since there's no automated
relationship between them.

**Architecture impact: none proposed.** This is recorded as evidence
about how production actually happens today. Whether the Contract-split
model should change to reflect it is a question for whoever reviews this
log, not a decision this entry makes.

## 2026-07-11 — Finding 3: the AI Generation content doesn't map cleanly onto Higgsfield/HyperFrames

`OS-009`'s integration split is video (Higgsfield) versus image/keyframe
(HyperFrames). This episode's actual AI Generation Package contains: 5
AI **video** blocks (clean Higgsfield fit), 1 animated 2D diagram build
(not clearly video-camera work or static image/keyframe work), and
typography + real-document-screenshot overlays (not AI-generated at
all). `prompts/hyperframes/` was created empty for this episode, with its
own note explaining why, rather than forcing the diagram or typography
into either category to make the folder non-empty.

**Architecture impact: none proposed.** Recorded as evidence that the
two-integration split, as currently scoped, doesn't account for
motion-graphics/diagram work or typography/overlay work — both of which
this real episode needs. Whether that's a gap in `OS-009` or simply work
that doesn't need an "integration" at all (it might be closer to what
`hyperframes-animation`/`motion-graphics`-style tooling, already present
elsewhere on this machine, is for) is a question for review, not decided
here.

## 2026-07-11 — Director Package produced

Despite the three findings above, none of them made production
*impossible* — only incomplete in specific, now-documented ways. A
Director Package was produced:
`episodes/luxury-destruction/director-package/` — `shot-list.md`,
`asset-manifest.md`, five Higgsfield prompt files (one per video block),
an empty (and explained) `hyperframes/` folder, and
`director-package.meta.json` recording status honestly as `Generated`
with validation explicitly marked incomplete, not `Reviewed` or
`Approved`.

**Status:** Open for review. No architecture change has been made or is
being proposed as a result of this episode's processing so far — per
this phase's rule, that decision belongs to whoever reviews these three
findings.

## 2026-07-12 — Editorial Decision Review: 58–59s duration conflict

`director-package-v2`'s runtime (~76s) was found to exceed the 58–59s
hard target stated identically in Decision Log v2, Visual Identity System
v2 §8, and Production Playbook v1. Reviewed against production evidence
only (no speculation): the source document's own text states the core
mechanism is unchanged from v1 (which fit in 58s), and the claimed
"Duration Philosophy" override does not appear in any of the three real
canonical documents read directly. **Recommendation accepted: the 58–59s
rule remains canonical, unchanged.**

## 2026-07-12 — Script v3 produced (canonical-compliant compression)

`script/script-package-v3.md` compresses v2's script from 231 to 177
words (~58s at v2's own established pace) to restore compliance. Only
material v2 itself identified as non-mechanism (a duplicated closing
restatement across three beats, one non-sourced editorial thesis line,
minor descriptive/connective trimming) was cut. The complete mechanism
(beats 4–6), both verified facts (Burberry £28.6M/£90M, Richemont
€481M), the named mechanism, and the personal-stake beat are all
preserved. Full removal log is in that file. Director Package
regeneration from this script was not performed — out of scope for this
pass.

## 2026-07-12 — Final editorial review: one FAIL, resolved

Reviewed script-package-v3 against 5 fixed questions (mechanism loss,
causal completeness, reveal inevitability, personal-stake emergence,
harmful compression). 4/5 PASS. FAIL on "compression that harms
understanding more than it saves runtime": cutting "Cartier's parent
company" from beat 3 saved ~1s but risked weakening the pattern-evidence
beat's credibility (an unrecognized holding-company name doesn't read as
corroborating evidence the way a known-brand reference does).

**Resolved:** "Cartier's parent company" restored in beat 3. Offsetting
cut made in beat 7 ("got caught and" — narrative framing on the
stopped/banned facts, not the facts themselves), chosen as the lowest-
information remaining segment outside the mechanism, reveal, and
personal-stake beats. Net word count unchanged (177 words), estimated
runtime unchanged (~58s). Mechanism, reveal, and personal stake were not
touched. Script Package v3 is ready for Script Lock.

## 2026-07-12 — Script Package v3 locked; Director Package v3 regenerated

`director-package-v3/` produced from the locked `script/script-package-v3.md`,
carrying forward v1/v2's structure and canonical-citation format
unchanged, updating only VO text, beat timings, and beat count (9 → 8,
beats 8a/8b/9 merged into one) to match the locked script.

**Runtime compliance is now met:** total timed runtime is 0:58, inside
the 58–59s canonical target — the first version of this episode's
Director Package to comply. Still a planning (word-count-pace) estimate,
not a confirmed render.

**Two new production issues found during regeneration:**
1. The script's merge of beats 8a/8b/9 removed the beat boundary v2 used
   to time Block E's payoff push-in. This package supplies an
   interpretation (push-in begins at the internal line "It's not
   exclusivity built for you") rather than something the locked script
   states explicitly. Needs review before shooting.
2. Beat 7's VO compression (24 words → 9) shrank its on-screen window
   from 8s to 3s — short for a 15s reference video generation. Flagged in
   `prompts/higgsfield/block-d.md`; will need a trim decision once the
   clip exists.

**Two issues carried forward unresolved from v2 (unrelated to this
regeneration, not fixed here):** Content Constitution v4 is still an
empty placeholder in `canonical/`; `prompts/higgsfield/` still doesn't
match Decision Log v2's named stack (Runway/Kling). No Engine change
made or proposed.

**Status:** Director Package v3, `Generated` / `Draft`. Next blocker
toward the first published episode is unchanged from the Milestone 3
assessment: no Voice Package exists yet for this episode.

## 2026-07-12 — Voice Package v1 produced

`voice/voice-package-v1.md` — narration segmented into the locked
8-beat structure (one continuous ElevenLabs submission, beat boundaries
as a reference map, not eight separate clips), pronunciation notes
carried forward from the source material, pause/emphasis guidance
adapted to the locked wording where the original notes referenced phrases
that no longer exist post-compression, recommended ElevenLabs settings,
and expected per-beat timing (total 58s, planning estimate).

**Open item found while producing this package:** no canonical document
or prior artifact specifies a narrator voice. Flagged in the package
itself as a decision needed before generation, not resolved here.

**Not yet done:** the package has not been submitted to ElevenLabs — no
real audio or confirmed timing exists yet. The package documents the
exact verification protocol to follow once it is: real timing gets
logged here as production evidence; `script-package-v3.md` stays locked
regardless of the result.

## 2026-07-12 — First real media asset generated: Block A

First actual rendered output in this episode's (and this repository's)
production history — everything before this was a plan, prompt, or
script. Submitted via the Higgsfield MCP, per the execution package
prepared in `director-package-v3/prompts/higgsfield/block-a.md`.

- **Model used:** `seedance_2_0_mini` (Seedance 2.0 Mini, Bytedance) —
  this project's default per standing instruction, not Kling 3.0 Turbo
  as originally proposed and rejected.
- **Credits consumed:** 37.5 (confirmed via the Higgsfield MCP's
  transaction ledger; balance after: 242.5, plan: starter).
- **Generation time:** submitted 2026-07-12T05:50:53Z; confirmed
  complete between ~85s and ~175s later (bounded by this session's own
  poll timing — the API returns no separate completion timestamp, so
  this is a bounded estimate, not exact).
- **Result:** **Success.** Status `completed`, output returned at
  `https://d8j0ntlcm91z4.cloudfront.net/user_3G7kcYKrXZeRrvSmreaxmPMgNHP/hf_20260712_055053_b9723905-9e24-43b6-bc09-d82d497ce58d.mp4`
  (job id `b9723905-9e24-43b6-bc09-d82d497ce58d`). Echoed params confirm
  720×1280 (9:16, 720p), 15s duration, no audio — matching every
  explicitly-set parameter exactly.
- **Seedance-specific issues observed:**
  1. While `status` was `in_progress`, `job_display` reported
     `"type":"image"` instead of `"video"` — self-corrected to `"video"`
     once the job completed. Cosmetic/transient, not a failure; noted in
     case it recurs on a future block and looks alarming mid-poll.
  2. The completed job's echoed `params` include several fields never
     submitted and not part of `seedance_2_0_mini`'s documented parameter
     set in `models_explore` (`multi_shots`, `multi_shot_mode`,
     `multi_prompt`, `speedramp`, `reference_elements`,
     `prompt_language`) — appear to be generic backend defaults applied
     across models regardless of relevance, not something specific to
     this request. No effect on the actual output; recorded for
     awareness on future generations.
- **Prompt changes required at execution time:** none beyond what was
  already identified and documented before submission (consolidating the
  Director Package's structured fields into one prompt string; setting
  `aspect_ratio`, `duration`, `resolution`, `generate_audio` explicitly).
  The prompt text itself generated successfully on the first attempt,
  unchanged from what was reviewed.
- **Not yet done:** the output has not been downloaded/archived locally.
  CloudFront-hosted generation URLs from comparable platforms typically
  expire (commonly within 24 hours) — this asset should be pulled down
  before that happens. Not performed here; flagged for the next
  production step.

Per instruction, no regeneration was performed — this attempt succeeded.

## 2026-07-12 — Block B generated

Submitted via the Higgsfield MCP using the prompt already prepared in
`director-package-v3/prompts/higgsfield/block-b.md`, same settings as
Block A (`seedance_2_0_mini`, 9:16, 15s, 720p, no audio).

- **Mechanical adaptation required:** same field-consolidation as Block A
  (structured fields joined into one prompt string, negative constraints
  folded in — no separate field for them). One additional, block-specific
  adaptation: the prepared prompt's "deliberate contrast to Block A's
  warmth" is an internal cross-reference to another document in this
  repository, meaningless to the generation model on its own. Translated
  to a self-contained equivalent — "deliberate contrast to a warmer
  boutique interior" — same descriptive content, no new creative
  material added.
- **API issue:** first submission was intercepted by Higgsfield's preset
  matcher — it recognized the prompt as resembling a preset ("IN THE
  DARK") and returned a recommendation instead of generating literally.
  Declined via `declined_preset_id` and resubmitted; second submission
  generated literally as intended. **Production observation for future
  blocks:** this may recur on other block prompts; the fix is a single
  extra round-trip (decline + resubmit), not a prompt change.
- **Credits consumed:** 37.5 (same as Block A).
- **Generation time:** submitted 2026-07-12T07:08:12Z; completed
  somewhere between ~180s and ~270s later — noticeably longer than Block
  A's ~85–175s. **Production observation:** render time varies block to
  block; don't assume Block A's timing when scheduling future
  generations.
- **Result:** success on the resubmitted (literal) attempt. Output saved
  to `episodes/luxury-destruction/assets/Generated/block-B/block-b_v1_seedance2mini.mp4`
  (same convention as Block A), downloaded from
  `https://d8j0ntlcm91z4.cloudfront.net/user_3G7kcYKrXZeRrvSmreaxmPMgNHP/hf_20260712_070812_f707a984-a9fe-4a0d-91cc-f7b4228bac02.mp4`
  (job id `f707a984-a9fe-4a0d-91cc-f7b4228bac02`).

No regeneration performed beyond the required preset-decline resubmit —
that resubmit was a pre-generation API gate, not a failed generation.
Director Package left unmodified; `block-b.md`'s creative content
untouched.

## 2026-07-12 — Blocks C, D, E generated (remaining video assets)

Submitted via the Higgsfield MCP from the prompts already prepared in
`block-c.md`, `block-d.md`, `block-e.md`, same settings throughout
(`seedance_2_0_mini`, 9:16, 15s, 720p, no audio). All three succeeded;
no regeneration was needed for any of them.

**Mechanical adaptations (same category as Blocks A/B — field
consolidation, negative constraints folded into the single prompt
string; no creative content added or changed):**
- Block C: none beyond the standard consolidation.
- Block D: none beyond the standard consolidation.
- Block E: the prepared prompt's two internal cross-references ("must
  not visually contradict Block A," "consistent color temperature with
  Block A") were translated into a self-contained description (warm
  color temperature matching a warm-lit boutique interior), same
  reasoning as Block B's fix — the model cannot resolve "Block A" as a
  reference to another document.

**API issues:**
- Block D's first submission was intercepted by the same "IN THE DARK"
  preset matcher that hit Block B. Declined and resubmitted literally;
  succeeded. Block C did not trigger it.
- Submitting Block E immediately after C and D (both still rendering)
  hit `429 rate_limit_reached` twice in a row. This is a **concurrency
  limit, not a request-frequency limit** — retrying immediately failed
  again; it only succeeded after C and D had both finished and freed a
  slot. **Production observation for future blocks/episodes:** this
  account's plan (starter) appears to support at most ~2 concurrent
  Seedance 2.0 Mini generations. Submit no more than 2 blocks at once;
  queue the rest to start as slots free up rather than submitting a full
  batch simultaneously.

**Credits consumed:** 37.5 each (112.5 total for C+D+E; 187.5 total
across all five blocks of this episode so far).

**Generation times (bounded estimates, same caveat as Blocks A/B — the
API returns no completion timestamp):**
- Block C: submitted 07:35:27Z, confirmed complete within ~130s.
- Block D: submitted 07:35:41Z, confirmed complete within ~130s (ran
  concurrently with C; both finished by the same check).
- Block E: submitted 07:38:55Z, confirmed complete within ~280s —
  slowest of the five blocks generated in this episode so far.

**Results — all success, all archived:**
- `episodes/luxury-destruction/assets/Generated/block-C/block-c_v1_seedance2mini.mp4` (job `c7bedb3a-47b9-4022-8607-5ff165810117`)
- `episodes/luxury-destruction/assets/Generated/block-D/block-d_v1_seedance2mini.mp4` (job `a766d7fe-1ed5-4476-a427-7fb395017cc5`)
- `episodes/luxury-destruction/assets/Generated/block-E/block-e_v1_seedance2mini.mp4` (job `4ce23322-39d6-4425-8679-291a1060112e`)

**Milestone:** all 5 required video blocks (A–E) for Luxury Destruction
are now generated and archived locally. Director Package v3 left
unmodified throughout — no creative content in any block prompt was
changed, only reformatted for the API and, where a prompt referenced
another block by name, translated into a self-contained description.
Remaining before first assembly: real Voice Package audio (still
unsubmitted, per the 2026-07-12 Voice Package entry above), diagram
asset, and typography — none of which are video-generation tasks.

## 2026-07-12 — CapCut Assembly Package v1 prepared

`assembly/capcut-assembly-package-v1.md` — timeline order, exact Block
A–E placement against the archived asset files, VO sync points,
typography timing (text copied verbatim from the locked script),
diagram timing, transitions, and music entry/exit points. All derived
mechanically from already-locked artifacts (`shot-list.md`,
`asset-manifest.md`, `voice-package-v1.md`, `script-package-v3.md`); no
new creative or pacing decision made.

**Blockers found while preparing it, documented in the package's own
§9:**
- Of the 11 assets a first assembly needs, only the 5 video blocks
  exist. No VO audio (Voice Package v1 is a spec, never submitted to
  ElevenLabs), no real-artifact document crops (Burberry/Richemont),
  no diagram render, no music bed, and the logo file is unconfirmed.
  The assembly plan itself is complete; the raw material mostly isn't.
- Beat 7's already-known 3-second compression is now concretely tight
  at the typography-card level: two cards get 1.5s each.
- Typography sub-card timing for beats 5, 7, and 8 (multi-clause beats)
  had to be derived in this package — it wasn't specified in any
  locked v3 artifact — flagged so it's reviewed as new, not assumed
  pre-approved.

**Status:** assembly package Generated. First real CapCut assembly
cannot begin until VO audio and the three static assets (real-artifact
crops, diagram, music) exist.

## 2026-07-12 — ElevenLabs Generation Package v1 prepared

`voice/elevenlabs-generation-package-v1.md` — the exact single-string
submission text (collapsed from `voice-package-v1.md`'s paragraph
formatting with zero wording/punctuation changes) plus exact generation
settings (`model_id`, `stability`/`similarity_boost`/`style` resolved to
the midpoints of the ranges already recommended, `use_speaker_boost`,
output format), ready for one API/UI submission.

**Blocker restated, now concrete:** `voice_id` is unset — no artifact
has ever selected a narrator voice — so this package is submittable in
every field except that one. Pronunciation is handled as a
post-generation check against the existing respelling notes, not by
altering the submission text; no phoneme dictionary was fabricated.

## 2026-07-12 — CapCut assembly automation evaluated and implemented

`assembly/AUTOMATION-EVALUATION-v1.md` + `assembly/generate_capcut_draft.py`.
Researched CapCut's actual project format (no official API; undocumented
`draft_content.json` folder format, reverse-engineered by the community)
and found a real, maintained, pip-installable library (`pycapcut`) that
generates it without CapCut needing to be installed to do so.

**Installed for this task:** Python 3.12 (via winget — this machine had
none) and `pycapcut`. **Confirmed via direct check:** this machine also
has no CapCut installation at all (`%LOCALAPPDATA%\CapCut` absent) —
stated because it bounds what could actually be tested.

**Implemented and run successfully:** a script that builds a real
CapCut draft from already-locked data only (block placement/trim table
and all 13 typography cards' text/timing/color, copied verbatim from
`capcut-assembly-package-v1.md`) against the 5 real generated video
files. Output: `assembly/capcut_drafts/luxury-destruction-v1/`, a
structurally valid `draft_content.json` — 2 tracks (5 video segments, 13
text segments), all materials resolving to real files, and a
library-computed total duration of exactly 58.0s, independently
confirming it matches the locked canonical target.

**Automation verdict:** 2 of the 7 tracks a full assembly needs (video
blocks, typography) are automatable today and now are. The other 5
(VO audio, 2 real-artifact crops, diagram, music, logo) aren't
automatable yet only because their source files don't exist — not a
tooling limitation. Extending the script once those exist is additive.

**Honest limit:** the generated draft has not been opened in real
CapCut — none is installed on this machine. What's verified is
successful generation of a structurally valid, correctly-timed draft by
a real third-party library; opening it in actual CapCut (on whichever
machine has it installed) is the one remaining unverified step.

## 2026-07-12 — Export V1 preparation

`assembly/EXPORT-V1-PREPARATION.md` — ordered manual assembly checklist,
missing-asset table (placement/defining artifact/specification status),
remaining manual CapCut actions, and export feasibility estimate,
against the validated draft as source of truth. No upstream artifact
modified.

**New finding, not previously documented:** the validated draft's canvas
and all 5 generated video blocks are natively 720×1280 (Seedance 2.0
Mini's resolution ceiling), while the canonical Publishing Target
(`Decision Log v2`; `Visual Identity System v2` §8) specifies 1080×1920.
Not resolved here — flagged as an open export-time decision (upscale vs.
ship at 720×1280).

**Feasibility estimate:** Export V1 can realistically be completed
without reopening Script Package, Director Package, or Voice Package.
Remaining work is asset sourcing/production (narration voice pick +
generation, 2 real-document crops, 1 diagram build, 1 music pick, 1 logo
locate) plus mechanical CapCut import/QA. The one built-in risk (VO
timing drift) already has a non-upstream-modifying fallback: log as
production evidence, per the existing verification protocol.

## 2026-07-12 — Resolution decision: 720p assets vs. regeneration at 1080p

Evaluated whether Seedance 2.0 Mini's 720×1280 output is a real blocker
for Export V1, using only checkable evidence, not assumption.

**Checked directly:**
- All 5 generated blocks confirmed 720×1280, ~15.04s, via local
  metadata inspection (`hachoir`) — not just trusting the generation
  API's echoed params.
- Real credit cost to regenerate at native 1080p: preflighted via
  `seedance_2_0` (full, non-Mini, `mode: std`, `resolution: 1080p`) —
  **135 credits/block**, vs. 37.5/block already spent on Mini. All 5
  blocks: 675 credits, against a remaining balance of ~82.5 — would
  require a new credit purchase.
- CapCut's own upscale behavior, per its documentation and independent
  guides: upscaling "does not magically recreate missing details;
  instead, it enhances the presentation of existing footage" — a real,
  usable mitigation with correct export settings (1080p output, high
  bitrate), not equivalent to native 1080p capture.
- Platform guidance (TikTok, Instagram Reels, YouTube Shorts, 2026):
  consistent real sourcing shows all three platforms compress
  sub-1080p uploads more aggressively, and recommend 1080×1920 sources.
- **No production evidence exists from this project either way** —
  nothing has been published or compared at any resolution yet.

**Decision: A — continue with the current 720p assets for Export V1.**
No production evidence shows regeneration would materially improve this
specific episode's result; the cost of finding out (675 credits, a new
purchase) is real and disproportionate to an unverified benefit. CapCut's
upscale path is a real, if imperfect, mitigation. Consistent with this
project's standing practice: don't spend on a fix ahead of evidence the
fix is needed. Revisit with real evidence after Export V1 publishes.

## 2026-07-12 — Remaining Export V1 assets: results

Worked the 5 tasks from `EXPORT-V1-PREPARATION.md` in order. Two
succeeded, two are blocked on real, documented environment limits (not
invented workarounds), one is correctly stopped rather than faked.

**1. Markdown Tax diagram — done.** Built via the `motion-graphics`
skill (HyperFrames), exactly per `director-package-v3/asset-manifest.md`'s
locked spec: nodes, labels, colors (#E8A838 amber, #E05555 red, #6B7280
gray, #A855F7 purple — sole use), and the 5-step build order from the
source material's Diagram Package (unchanged, since v3's asset-manifest
says "same content, unchanged" from v2 rather than redefining it). 720×1280,
exactly 11.0s (matches Beat 6, 0:29–0:40), verified via local metadata
inspection, not just the render log. Saved to
`assets/Generated/diagram/markdown-tax-diagram_v1.mp4`.
Two production-level (non-creative) fixes were required to pass the
tool's own lint/contrast checks: six overlapping timeline elements moved
to six separate tracks (a rendering-engine requirement, not a design
change), and one bar's text color darkened from a near-white to
`rgb(30,28,28)` to meet WCAG AA contrast against its red background —
the bar's own color stayed exactly `#E05555` as specified; only
unspecified foreground text color was adjusted. Environment note: this
required installing FFmpeg (via winget) — this machine had none.

**2 & 3. Burberry Annual Report crop and Richemont earnings report
crop — blocked, not produced.** Both real documents were correctly
located (via `web.archive.org`'s snapshot of
`burberryplc.com/.../Burberry_AnnualReport_FY17-18.pdf` for the first;
Richemont's 2018 figures confirmed real via press coverage but no direct
report URL found for the second). Direct fetch of the real Burberry
PDF failed identically across three different tools — `curl`, `WebFetch`,
and `PowerShell Invoke-WebRequest` all returned either HTTP 403 (direct
burberryplc.com) or a truncated file at exactly 1,048,576 bytes
(1.0 MB) from the archive.org mirror, confirmed corrupt (0 pages
readable via PyMuPDF). This points to a ~1MB outbound download cap in
this environment, not a source-specific block — the same ceiling would
very likely truncate the Richemont report too, which is why a second
full attempt wasn't made once the pattern was confirmed. A real browser
navigation to the direct Burberry URL did reach the file (no 403) but
triggered a native OS save dialog the browser tool can't complete, and
was explicitly told not to retry. `web.archive.org` itself additionally
requires per-action approval this session doesn't have. **No image was
fabricated or substituted.** This needs either a larger-download-capable
environment or a human manually downloading and cropping the two pages.

**4. Open Secret logo — stopped, not invented, per instruction.**
Checked this repository (all of it, not just the episode folder) and
the separate `Downloads/New documents Open secret...` working directory
— neither contains any image, logo, or brand asset; the second location
holds only the original 18 OS-XXX architecture drafts. A logo is a
brand-identity design decision, not a production task with a locked
spec to execute against (unlike the diagram) — per instruction, this is
reported, not designed.

**5. Remaining typography/overlay assets.** The 13 typography display
cards are already in the validated CapCut draft (prior session) — no
further work needed there. The one remaining overlay,
the subtitle track (Inter Medium, max 8 words/line, per the Typography
Package), is still correctly un-produced: it requires real VO
word-level timestamps, which don't exist yet (Phase 1 of
`EXPORT-V1-PREPARATION.md`, not started). Not a new finding — restated
so this pass doesn't silently look complete.

**Net effect on Export V1 readiness:** 1 of 4 missing visual/graphic
assets is now done and archived (diagram). The two real-document crops
and the logo remain open, for the reasons above — none of them was
worked around or faked.

## 2026-07-12 — Approved documentary evidence assets added to the draft

Eugene supplied two approved evidence images directly (crops of the real
Burberry Annual Report 2017/18 and a Guardian, 18 May 2018 article
reporting Richemont's €500m/€437m two-year buyback figure — note this
second asset is a secondary news source quoting the disclosure, not a
crop of Richemont's own primary filing; recorded precisely as such, not
implied otherwise). Found on disk at
`C:\Users\Eugene\Downloads\Burberry.png` and `Richemont.png`, confirmed
by direct visual comparison against the images Eugene posted before use.

**Saved to the canonical location:**
- `episodes/luxury-destruction/assets/Supporting/burberry-evidence-v1.png`
- `episodes/luxury-destruction/assets/Supporting/richemont-evidence-v1.png`
(new directory, created)

**Draft updated via the existing `generate_capcut_draft.py`** (edited,
not hand-patched, so the whole draft regenerates deterministically from
locked data every time): added two `VideoSegment`s for the new images at
exactly Beat 2 (0:05–0:10) and Beat 3 (0:10–0:17) — the gap that was
already intentionally left there for this exact purpose. No other
segment was touched.

**Verified by direct inspection of the regenerated `draft_content.json`
(not just the run log):**
- Track structure unchanged: still exactly 2 tracks (video, text).
- Text track unchanged: still exactly 13 segments, untouched.
- Video track: 7 segments now (5 blocks + 2 new images), laid out
  continuously with no gap and no overlap: 0–5s (A), 5–10s (Burberry),
  10–17s (Richemont), 17–29s (B), 29–40s (C), 40–43s (D), 43–58s (E).
- Project duration: still exactly 58.0s — unchanged.
- Script Package, Director Package, Voice Package, and Assembly Package
  files: not opened, not modified.

**Manual CapCut action still required, reported rather than worked
around:**
1. This machine still has no CapCut installed — the two images'
   actual on-screen fit/crop/legibility inside the 720×1280 frame
   (CapCut's fit-vs-fill-vs-crop behavior for a placed photo) has not
   been visually confirmed and needs a check once the draft is opened
   in real CapCut.
2. The Markdown Tax diagram (rendered in the prior session, saved to
   `assets/Generated/diagram/markdown-tax-diagram_v1.mp4`) is still not
   inserted into this draft as a segment — out of scope for this task,
   noted so it isn't mistaken for done.
3. Everything else already listed in `EXPORT-V1-PREPARATION.md` is
   unchanged: VO audio, music, logo, subtitles, the Block D trim review,
   and the Beat 8 sub-card timing sanity check.

## 2026-07-13 — Real narration and diagram added to the draft

Eugene supplied the real ElevenLabs narration MP3
(`ElevenLabs_2026-07-12T08_16_32_Adam_pvc_sp115_s45_sb55_se35_b_m2.mp3`)
and the rendered diagram (from the prior session) was already on disk.
Both added via `generate_capcut_draft.py` (edited, not hand-patched):
narration on a new `narration` audio track (full real file, unmodified,
starting at 0s); diagram on a new `diagram_overlay` video track at the
already-locked 0:29–0:40 (Beat 6), composited above the base video
track rather than replacing Block C. No music added, no subtitles
generated, per instruction. Script/Director/Voice/Assembly Package
files: not opened.

**Archived:**
- `assets/Generated/voice/narration_v1.mp3`
- (diagram already at `assets/Generated/diagram/markdown-tax-diagram_v1.mp4`
  from the prior session)

**Verification, against the regenerated `draft_content.json` directly:**

| Check | Result |
|---|---|
| No gaps (base video track) | ✅ Confirmed continuous, 0→5→10→17→29→40→43→58s, identical to before |
| No overlaps (any track) | ✅ Confirmed, all four tracks |
| Video timing unchanged | ✅ All 7 base_video segments byte-identical to the prior draft |
| Typography unchanged | ✅ All 13 cards — text, timing, and color — byte-identical to the prior draft |
| Documentary evidence assets unchanged | ✅ Burberry (5–10s) and Richemont (10–17s) segments untouched |
| **Total duration unchanged** | ❌ **Not unchanged — see below** |

**The one real finding, reported rather than fixed:** the project's
computed total duration is now **62.589s**, not 58.0s. This isn't a
bug in the update — CapCut/pycapcut compute project duration as the
longest track, and the real narration (62.589s) is longer than the
locked 58–59s visual timeline. The base video and typography tracks
still end at 58s; audio continues 4.589s past that with nothing on the
video track to cover it. This is exactly the overage already flagged as
the most likely risk (Beat 7's 3-second window, tightest point in the
episode) — this entry doesn't isolate which beat(s) absorbed it, since
no word-level timestamps came with the file, only the finished mix.

**One more data point worth recording:** the filename encodes the real
settings used — voice "Adam," speed 1.15x (`sp115`), stability 45%
(`s45`), among others — notably faster than natural pace and still 4.6s
over target. At natural (1.0x) pace this narration would run
approximately 72s. Recorded as evidence for calibrating estimates on
the next episode, not acted on here. Also notable: a voice was in fact
selected ("Adam") — `voice-package-v1.md`'s own record still shows this
as an open field, since that file wasn't touched per instruction; the
document and reality are now out of sync until someone updates it.

**Not resolved here, by design:** whether to extend video coverage,
trim the audio, or accept the shortfall is an editorial/production
decision outside this task's scope. Flagged for whoever reviews this
draft next, same as the original 58s/76s conflict was handled.

## 2026-07-13 — Decision: narration is now the reference timeline

Following review, the 58–59s target was explicitly retired for this
episode: narration approved, pace judged natural, script locked. The
production draft (`luxury-destruction-v1`) was regenerated to match the
real 62.589s narration exactly, rather than partially absorbing the gap
under a runtime cap (as the earlier 60s-capped experiment did — that
experiment was correctly not adopted; this is a separate, deliberate
decision, not a reversal of "don't adopt the experiment").

**Shot order unchanged.** Five of seven shots extended, none
concentrated:

| Shot | Added | Method | Why |
|---|---|---|---|
| Burberry evidence | +0.5s | hold extension (real spare footage in the 15.042s source) | static document hold, least perceptible place to add time |
| Richemont evidence | +0.5s | hold extension | same reasoning |
| Block B | +0.5s | hold extension (3.042s of real spare footage available) | — |
| Block C | +0.5s | hold extension, added *after* the diagram's fixed 11s animation finishes | diagram itself untouched — repositioned, not stretched |
| Block D | **+2.0s** | hold extension (12s of real spare footage available) | the one shot this pass actually *fixes*, not just absorbs into: this beat held 8s for the same two facts before the now-retired 58s ceiling forced it to 3s; restores real reading time for two dates, each typography card now gets 2.5s instead of 1.5s |
| Block E | +0.589s | **small speed reduction (0.9622×, ~3.8% slower)**, not a hold extension | its 15.042s source clip was already fully used (15.0s), so no more footage existed to hold on — an already-slow "static hold, then 2% push-in" shot is where a few-percent slowdown is least likely to register |
| Block A (hook) | +0s | untouched, deliberately | Hook Rule requires landing within 3s; extending it works against its own design regardless of overall runtime |

**Resulting total runtime: 62.589s — exact match to the real narration,
zero residual gap**, verified against the regenerated `draft_content.json`
directly: base video track runs 0→5→10.5→18→30.5→42→47→62.589s with no
gaps and no overlaps; the diagram overlay is untouched (still exactly
11s, just repositioned to 30.5–41.5s); narration is the full,
unmodified file, 0–62.589s.

**Typography:** each card keeps its original offset from its own
shot's start (same relative design as before), with two exceptions,
both necessary given the retimed shots: Beat 7's two cards are
re-split evenly across Block D's new 5.0s (2.5s each, was 1.5s each);
the closing "holds to the cut" card is extended to match Block E's true
new end (60.0–62.589s) instead of stopping 0.589s early.

**One real bug found and fixed during this update:** the script's
shot-lookup function used a floating-point tolerance on an exact
boundary check, which silently misfiled two typography cards into the
wrong shot (e.g., "Same decision. Why?" — which starts exactly on the
Richemont/Block B boundary — was being attributed to Richemont's
timing instead of Block B's). Caught immediately by pycapcut's own
overlap validation (`SegmentOverlap` on save), not by manual review —
worth noting as a real case of the generation pipeline's own structural
checks catching a genuine logic error before it reached a draft.

Script Package, Director Package, Voice Package, and Assembly Package:
not opened. `generate_capcut_draft.py` is the only file that changed.

## 2026-07-14 — CapCut Desktop compatibility test: confirmed incompatible

CapCut Desktop (8.9.1.3802) was installed and a real end-to-end test was
run against it. Real project directory located by filesystem search
(`%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\`), draft
copied in unmodified, CapCut launched successfully. Full findings and
conclusion: `docs/production-evidence/PE-003_CapCut_Desktop_Pipeline_Incompatibility.md`.

**Conclusion:** the `pycapcut` pipeline (targets CapCut app_version
6.7.0) is not compatible with the installed 8.9.1.3802 — the generated
draft is missing the `Timelines/` subsystem and several config files
real projects of this version have, and is never registered in the
`root_meta_info.json` index the Projects screen reads from. Per
instruction, investigation stopped here: no modification to
`root_meta_info.json`, no further reverse-engineering of CapCut's
internal format.
