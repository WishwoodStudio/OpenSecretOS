# Asset Manifest v2 — Luxury Destruction

**Director Package artifact, regenerated against the now-available
Canonical Layer.**

## AI-generated video (5 blocks, ~15s reference length each)

**Canonical basis for the 15-second block approach:** `Production
Playbook v1`, Lessons from Episodes — *"15-second blocks outperform one
long generation."* This is production evidence (not a hard rule), cited
here because it directly matches the block structure the source package
already used.

| Block | Used in | Description |
|---|---|---|
| A | Beat 1 | Boutique interior, warm ambient light — opens the episode |
| B | Beats 4–5 | Quiet stockroom, unglamorous/procedural — contrast to Block A |
| C | Beat 6 | Abstract diagram-stage, low-key — backdrop for the reveal diagram |
| D | Beat 7 | Storefront exterior, dusk — register shift toward the conclusion |
| E | Beats 8a–9 | Quiet interior wide, closing — must visually rhyme with Block A |

Full generation prompts for each block are in `prompts/higgsfield/`.

**Canonical note on the generation tool itself:** `Decision Log v2`,
Section 5, names **Runway / Kling** as the canonical AI video generation
stack — not Higgsfield, which is what this repository's Engine
architecture (`SPEC-001` §17, sourced from `OS-009`) names as the video
integration. This Director Package uses the folder name
`prompts/higgsfield/` because that's the Engine's existing, already-built
convention — changing it would be an Engine architecture change, which
this exercise is not authorized to make. The prompts themselves are
written platform-agnostically (per the source material's own convention)
and are not Higgsfield-specific, so this naming mismatch doesn't affect
their content. Flagged as a finding, not resolved.

## Real documentary artifacts (2, both required)

**Canonical basis:** `Visual Identity System v2`, §2, "Real Artifacts
First" — licensed real artifact is priority 1, ahead of reconstruction or
synthetic graphics. Both assets below satisfy that priority directly.

| Asset | Type | Why required |
|---|---|---|
| Burberry Annual Report 2017/18 — disclosure line | Filing | Primary source for the episode's core claim |
| Richemont 2018 earnings report, page 3 — buyback figure | Filing | Second independent primary source |

## Diagram (1)

**Name:** The Markdown Tax (comparison diagram)
**Appears:** Beat 6, 0:33–0:44

- **Colors, with canonical citation** (`Visual Identity System v2`, §3 —
  Color System table):
  - Amber `#E8A838` — canonical semantic meaning "Money flow... amber for
    money moving only." Used here for recovered cash, which is a money
    quantity — consistent use.
  - Red `#E05555` — canonical semantic meaning "Cost / loss." Used for
    both the discount's signal damage and destruction's sunk cost —
    consistent, both are loss quantities.
  - Gray `#6B7280` — canonical "Neutral / secondary," used for structural
    labels — consistent.
  - Purple `#A855F7` — canonical "Mechanism reveal... once per episode
    maximum" — used exactly once, at this diagram's closing caption. See
    Beat 6's compliance note in `shot-list.md`.
- **Build order:** matches the canonical build-in rule exactly (`Visual
  Identity System v2`, §6: opacity 0→100, upward translate 4–8px,
  200–300ms) and the "no looping" rule (diagrams build, hold, and clear).

## Typography (episode-wide)

**Canonical basis:** `Visual Identity System v2`, §4 (Typography table).
Space Grotesk ExtraBold for numbers/headlines, Inter Medium for
labels/body — matches exactly what the source material already
specifies. Subtitle rule (Inter Medium, max 8 words/line) also matches
§4's size rules exactly.

## Logo

Open Secret logo (A1 variant) — outro only, cross-dissolved in at 200ms
(the canonical maximum, `Visual Identity System v2` §6).

## Total unique hard assets

5 AI video blocks + 2 real artifacts + 1 diagram = 8.
