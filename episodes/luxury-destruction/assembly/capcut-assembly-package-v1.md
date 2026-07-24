# CapCut Assembly Package v1 — Luxury Destruction

**Artifact ID:** `capcut-assembly-package-luxury-destruction-v1`
**Episode ID:** luxury-destruction
**Status:** Generated
**Basis:** assembled exclusively from already-locked upstream artifacts.
No timing, pacing, or creative decision is made in this document — every
number and every line of text below traces to one of:
- `script/script-package-v3.md` (locked, immutable — VO text)
- `director-package-v3/shot-list.md` (beat boundaries, camera language,
  transitions, canonical citations)
- `director-package-v3/asset-manifest.md` (diagram, typography basis,
  logo, asset list)
- `voice/voice-package-v1.md` (pause/emphasis guidance)
- `source/OS_Production_Package_LuxuryDestruction_v2.md` §8–10 (diagram
  build mechanics, typography design language, music cue rule) — reused
  for its *design*, retimed to v3's locked beat boundaries. No design
  choice here is new; each is the same rule v2 already established,
  reapplied to the new timing.
- The 5 generated video files in `assets/Generated/block-*/`

Where a sub-beat timing had to be derived (e.g., where within a 15-second
beat a typography card should change), it is computed by the same
word-count-proportional method already used throughout this project's
planning artifacts — not a new pacing judgment.

---

## 1. Timeline order and exact placement of Blocks A–E

| Beat | Time | Block | Asset file | Transition in |
|---|---|---|---|---|
| 1 | 0:00–0:05 | A | `assets/Generated/block-A/block-a_v1_seedance2mini.mp4` | Cold open |
| 2 | 0:05–0:10 | — (real artifact 1, see §7) | *(pending — see Blockers)* | Hard cut |
| 3 | 0:10–0:17 | — (real artifact 2, see §7) | *(pending — see Blockers)* | Hard cut |
| 4 | 0:17–0:22 | B | `assets/Generated/block-B/block-b_v1_seedance2mini.mp4` | Hard cut |
| 5 | 0:22–0:29 | B (continued) | same file, continued — no new import | Hard cut, internal to Block B |
| 6 | 0:29–0:40 | C + diagram overlay | `assets/Generated/block-C/block-c_v1_seedance2mini.mp4` | Hard cut |
| 7 | 0:40–0:43 | D | `assets/Generated/block-D/block-d_v1_seedance2mini.mp4` | Hard cut |
| 8 | 0:43–0:58 | E | `assets/Generated/block-E/block-e_v1_seedance2mini.mp4` | Hard cut |
| — | 0:58–0:58.2 | Logo card | *(pending — see Blockers)* | 200ms cross-dissolve |

All beat boundaries and block assignments are unchanged from
`shot-list.md` — reproduced here only for placement against the actual
archived files. Beats 2 and 3 use no generated video block; per
`asset-manifest.md`'s "Real Artifacts First" priority, they use the two
licensed real documents, not AI footage.

Every generated block was rendered at 15s reference length (per
`asset-manifest.md`'s convention); each is trimmed in-edit to its beat's
actual duration:

| Block | Rendered length | Used duration | Trim needed |
|---|---|---|---|
| A | 15s | 5s | Trim to lead-in only |
| B | 15s | 12s (beats 4+5 combined) | Trim to lead-in; internal cut at 0:22 is a VO/typography change only, not a new import |
| C | 15s | 11s | Trim to lead-in |
| D | 15s | 3s | Trim to the calmest 3-second span — flagged in `shot-list.md` Production Issue and restated in §9 below |
| E | 15s | 15s | Full rendered length used |

---

## 2. VO synchronization points

One continuous take, per `voice-package-v1.md`. Sync points below are
each beat's VO start time; word-level timestamps from the actual
ElevenLabs render (not yet generated — see Blockers) are the final
authority once they exist.

| Beat | VO start | VO text |
|---|---|---|
| 1 | 0:00 | "Burberry burned £28.6 million of its own clothes." |
| 2 | 0:05 | "Every year: 'finished goods physically destroyed.' Ninety million pounds, over five years." |
| 3 | 0:10 | "Burberry wasn't alone. Cartier's parent company, Richemont, spent 481 million euros buying back its own unsold watches — then took them apart." |
| 4 | 0:17 | "Two different companies. Same decision: zero dollars, on purpose, instead of a discount. Why?" |
| 5 | 0:22 | "Because a marked-down coat isn't one lost sale. It's a public price tag — visible to every full-price customer — for the entire collection." |
| 6 | 0:29 | "So it's never 'destroy it' versus 'sell it for something.' It's 'destroy it' versus 'quietly discount everything else, too.' Count it that way, and zero is the cheaper number. This is the markdown tax." |
| 7 | 0:40 | "Burberry stopped in 2018; France banned it in 2022." |
| 8 | 0:43 | "So the next time a brand protects its scarcity — a waitlist, a restock kept deliberately tiny — there's a different way to read it. It's not exclusivity built for you. It's the markdown tax, paid in a different currency: your attention, your patience, the appeal of being let in. Is that exclusivity? Or is it the markdown tax?" |

Two pauses, per `voice-package-v1.md`: after the Beat 1 line (let it
land before the 0:05 cut), and after "This is the markdown tax." in Beat
6 (let the name register before Beat 7).

---

## 3. Typography timing

Design language (fonts, sizes, colors, hierarchy) is unchanged from the
source material's Typography Package (§9) — only text and timing are
updated to match the locked script and retimed beats. Every card's text
is copied verbatim from the locked script; none is newly written.

| # | Beat | Card text | Timing | Color |
|---|---|---|---|---|
| 1a | 1 | "£28.6 MILLION" | 0:00–0:02 | Primary `#EDEAE2` |
| 1b | 1 | "Of its own clothes. Burned." | 0:02–0:05 | Primary `#EDEAE2` |
| 2 | 2 | "5 years. £90,000,000." | 0:07–0:10 | Amber `#E8A838` |
| 3 | 3 | "€481,000,000" | 0:14–0:17 | Amber `#E8A838` |
| 4 | 4 | "Same decision. Why?" | 0:17–0:22 | Primary `#EDEAE2` |
| 5a | 5 | "A marked-down coat isn't one lost sale." | 0:22–0:25 | Primary `#EDEAE2` |
| 5b | 5 | "It's a price tag for everything." | 0:25–0:29 | Primary `#EDEAE2` |
| 6 | 6 | "THE MARKDOWN TAX" | 0:37–0:40 | **Purple `#A855F7`** — sole use, per Purple Rule |
| 7a | 7 | "2018 — Burberry stops." | 0:40–0:41.5 | Gray `#6B7280` |
| 7b | 7 | "2022 — France bans it." | 0:41.5–0:43 | Gray `#6B7280` |
| 8a | 8 | "There's a different way to read it." | 0:43–0:49 | Primary `#EDEAE2` |
| 8b | 8 | "The markdown tax — paid in a different currency." | 0:49–0:56 | Primary `#EDEAE2` |
| 8c | 8 | "Exclusivity? Or the markdown tax?" | 0:56–0:58 | Primary `#EDEAE2`, held to the cut |

Cards 5a/5b, 7a/7b, and 8a/8b/8c did not exist as separate locked
entries in any v3 artifact — their sub-beat split and timing are derived
here (word-count-proportional, same method as every prior timing
estimate in this episode's planning) because a single beat merging
multiple clauses needs card boundaries to be assemblable at all. Flagged
individually in §9.

Subtitle track (separate from the display-number/statement cards above):
Inter Medium, max 8 words/line, throughout — unchanged convention.

---

## 4. Diagram timing

Unchanged design, retimed only. Beat 6 is the same 11-second duration as
v2 (0:33–0:44 → 0:29–0:40), so every internal offset carries over
unchanged, shifted 4 seconds earlier:

- **0:29** — diagram build starts. Left side: "Discount it" → small amber
  flow → wide red "signal" bar expands (0.6s).
- **0:30** (build +1s) — hold left side alone, 1s.
- **0:31.6** — right side builds: "Destroy it" → small red bar only, no
  expansion (0.4s).
- **0:32** — both sides held side by side, 1.5s.
- **0:37** — purple caption fades in, "THE MARKDOWN TAX" (0.4s fade),
  holds to 0:40.
- **0:40** — hard cut to Beat 7.

Colors, node labels, and flow structure: unchanged from
`asset-manifest.md` §Diagram — Amber `#E8A838` (recovered cash), Red
`#E05555` (signal cost + destruction cost), Gray `#6B7280` (structural
labels), Purple `#A855F7` (sole reveal use).

---

## 5. Transitions

Unchanged rule, applied beat by beat: **hard cut is the canonical
default** between every beat above except:
- Beat 4→5: internal to Block B, no new import (continuation, not a
  cut).
- End of Beat 8 → Logo: **one 200ms cross-dissolve**, the canonical
  maximum — the only cross-dissolve in the episode.

No other transition type appears anywhere in the locked Director
Package.

---

## 6. Music entry/exit points

Same rule as the source material's music cue (single continuous
ambient/analytical bed, no Content ID risk), retimed to the locked beat
boundaries using the same anchor logic — intensity lift at the reveal
build, settle at the start of the closing beat, fade under the logo:

- **0:00** — bed starts, continuous under the full edit.
- **0:29** — subtle intensity lift begins (was 0:33 in v2; anchored to
  Beat 6's start, which is now 0:29).
- **0:43** — settles back down into the closing register (was 0:52 in
  v2; anchored to the closing beat's start, which is now Beat 8 at
  0:43).
- **0:58** — fades out under the logo cross-dissolve.

---

## 7. Overlays required by the Director Package

- **Real artifact 1** (Beat 2, 0:05–0:10): Burberry Annual Report
  2017/18, cropped to the disclosure line ("the cost of finished goods
  physically destroyed in the year was £28.6m"). Push-in to the
  disclosure line per `shot-list.md`.
- **Real artifact 2** (Beat 3, 0:10–0:17): Richemont 2018 earnings
  report, page 3, cropped to the buyback figure. Push-in mirroring
  Beat 2's grammar.
- **Diagram** (Beat 6, 0:29–0:40): "The Markdown Tax," per §4 above.
- **Logo** (0:58, outro): Open Secret logo, A1 variant, 200ms
  cross-dissolve.

None of these four overlay assets exist as files in this repository yet
— see §9.

---

## 8. Asset reference (what actually exists right now)

| Asset | Status | Location |
|---|---|---|
| Block A video | ✅ Exists | `assets/Generated/block-A/block-a_v1_seedance2mini.mp4` |
| Block B video | ✅ Exists | `assets/Generated/block-B/block-b_v1_seedance2mini.mp4` |
| Block C video | ✅ Exists | `assets/Generated/block-C/block-c_v1_seedance2mini.mp4` |
| Block D video | ✅ Exists | `assets/Generated/block-D/block-d_v1_seedance2mini.mp4` |
| Block E video | ✅ Exists | `assets/Generated/block-E/block-e_v1_seedance2mini.mp4` |
| VO audio | ❌ Does not exist | `voice-package-v1.md` is a submission-ready spec; never submitted to ElevenLabs (confirmed in `production-log.md`) |
| Real artifact 1 (Burberry report crop) | ❌ Does not exist | Not sourced anywhere in this repository |
| Real artifact 2 (Richemont report crop) | ❌ Does not exist | Not sourced anywhere in this repository |
| Diagram ("The Markdown Tax") | ❌ Does not exist | Design specified in `asset-manifest.md`; no rendered graphic file |
| Music bed | ❌ Does not exist | Rule specified ("YouTube Audio Library / licensed, no Content ID risk"); no specific track selected or sourced |
| Logo (A1 variant) | ❌ Not confirmed | Referenced throughout; not verified present in this repository |

---

## 9. Production blockers discovered during assembly preparation

1. **This package cannot be executed end-to-end yet.** Of the 11 assets
   a first assembly needs (5 video blocks, VO audio, 2 real-artifact
   crops, 1 diagram, 1 music bed, 1 logo), only the 5 video blocks
   exist. Milestone 4's framing lists "Generated video assets (Blocks
   A–E)" and "Voice Package v1" as complete upstream artifacts; that's
   accurate for the video blocks, but Voice Package v1 is a text
   specification, not audio — no VO has been generated. This is stated
   plainly because the assembly package itself is genuinely ready
   (timeline, sync points, typography, transitions, music cue all
   derived and placed); what's missing is the raw material, not the
   plan.
2. **Beat 7's 3-second window is now confirmed tight at the
   typography-card level, not just the shot level.** `shot-list.md`
   already flagged the compressed VO; preparing actual card timing for
   this package makes the specific consequence concrete: two sequential
   cards ("2018 — Burberry stops." / "2022 — France bans it.") now get
   1.5 seconds each. That's readable but leaves no slack — worth a
   first-look check once real VO timing exists, before assuming it
   holds.
3. **Beat 8's three sub-cards and Beats 5/7's split cards are this
   package's own derived timing, not something locked upstream.** No
   v3 artifact specifies where inside a merged or multi-clause beat a
   typography card should change — §3's sub-beat splits were computed
   here by the same proportional method used throughout this project,
   not copied from an existing decision. Flagged so a human reviewer
   treats those specific rows as newly derived, not as pre-approved.
4. **All timing in this package is still a planning estimate.** No
   change from the standing caveat already carried through every prior
   artifact: real assembly must re-anchor every timestamp above against
   actual ElevenLabs word-level timestamps once VO exists, per the
   verification protocol already defined in `voice-package-v1.md`.
