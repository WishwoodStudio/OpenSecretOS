# Asset Manifest v3 — Luxury Destruction

**Director Package artifact, regenerated from the locked
`script/script-package-v3.md`.** Asset list is unchanged from v2 — the
compression pass that produced the locked script removed only words, not
beats' visual assignments. Only beat/timing references below are
updated.

## AI-generated video (5 blocks, ~15s reference length each)

**Canonical basis for the 15-second block approach:** `Production
Playbook v1`, Lessons from Episodes — *"15-second blocks outperform one
long generation."* Production evidence, not a hard rule.

| Block | Used in | Description |
|---|---|---|
| A | Beat 1 (0:00–0:05) | Boutique interior, warm ambient light — opens the episode |
| B | Beats 4–5 (0:17–0:29) | Quiet stockroom, unglamorous/procedural — contrast to Block A |
| C | Beat 6 (0:29–0:40) | Abstract diagram-stage, low-key — backdrop for the reveal diagram |
| D | Beat 7 (0:40–0:43) | Storefront exterior, dusk — register shift toward the conclusion |
| E | Beat 8 (0:43–0:58) | Quiet interior wide, closing — must visually rhyme with Block A |

Full generation prompts for each block are in `prompts/higgsfield/`.
Block E's usage note changed from "Beats 8a–9" (v2) to "Beat 8" (v3) —
same block, same continuous shot, reflecting the script's beat merge; see
`shot-list.md` Production Issue #1 for the one open question that merge
created (where inside the beat the push-in starts).

**Canonical note on the generation tool itself (unresolved, carried
forward from v2):** `Decision Log v2`, Section 5, names Runway/Kling as
the canonical AI video generation stack — not Higgsfield, which is what
this repository's Engine architecture (`SPEC-001` §17, sourced from
`OS-009`) names as the video integration. This Director Package still
uses the folder name `prompts/higgsfield/` because that's the Engine's
existing, already-built convention — changing it would be an Engine
architecture change, which this regeneration is not authorized to make.
The prompts are written platform-agnostically and are not
Higgsfield-specific, so the naming mismatch doesn't affect their content.

## Real documentary artifacts (2, both required)

**Canonical basis:** `Visual Identity System v2`, §2, "Real Artifacts
First." Unchanged from v2.

| Asset | Type | Why required |
|---|---|---|
| Burberry Annual Report 2017/18 — disclosure line | Filing | Primary source for the episode's core claim |
| Richemont 2018 earnings report, page 3 — buyback figure | Filing | Second independent primary source |

## Diagram (1)

**Name:** The Markdown Tax (comparison diagram)
**Appears:** Beat 6, 0:29–0:40 (timing shifted earlier from v2's
0:33–0:44; same 11-second duration, same content, unchanged)

- **Colors, with canonical citation** (`Visual Identity System v2`, §3):
  - Amber `#E8A838` — money flow (recovered cash).
  - Red `#E05555` — cost/loss (both the discount's signal damage and
    destruction's sunk cost).
  - Gray `#6B7280` — neutral/secondary, structural labels.
  - Purple `#A855F7` — mechanism reveal, once per episode maximum — used
    exactly once, at this diagram's closing caption. See Beat 6's
    compliance note in `shot-list.md`.
- **Build order:** matches the canonical build-in rule (opacity 0→100,
  upward translate 4–8px, 200–300ms) and the no-looping rule. Unchanged
  from v2.

## Typography (episode-wide)

**Canonical basis:** `Visual Identity System v2`, §4. Space Grotesk
ExtraBold for numbers/headlines, Inter Medium for labels/body; subtitle
rule Inter Medium, max 8 words/line. Unchanged from v2. Individual
typography card timings should be re-derived from `shot-list.md`'s new
beat boundaries before shooting — not re-derived here, since typography
card content is unaffected by the word-level cuts (no typography card
quoted any of the removed VO segments verbatim).

## Logo

Open Secret logo (A1 variant) — outro only, cross-dissolved in at 200ms
(canonical maximum). Unchanged from v2.

## Total unique hard assets

5 AI video blocks + 2 real artifacts + 1 diagram = 8. **Unchanged from
v2** — the script compression that produced v3 removed words and merged
beat labels, not visual assets or blocks.
