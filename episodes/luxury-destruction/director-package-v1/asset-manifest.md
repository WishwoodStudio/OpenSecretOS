# Asset Manifest — Luxury Destruction

**Director Package artifact.** Combines the source Production Package's
Production Asset List (§4), Documentary Asset Package (§7), and Diagram
Package (§8). Every asset here is referenced by at least one shot in
`shot-list.md`.

## AI-generated video (5 blocks, ~15s reference length each)

| Block | Used in | Description |
|---|---|---|
| A | Beat 1 | Boutique interior, warm ambient light — opens the episode |
| B | Beats 4–5 | Quiet stockroom, unglamorous/procedural — contrast to Block A |
| C | Beat 6 | Abstract diagram-stage, low-key — backdrop for the reveal diagram, must not compete with it |
| D | Beat 7 | Storefront exterior, dusk — register shift toward the episode's conclusion |
| E | Beats 8a–9 | Quiet interior wide, closing — must visually rhyme with Block A (bookend) |

Full generation prompts for each block are in `prompts/higgsfield/`.

## Real documentary artifacts (2, both required)

| Asset | Type | Why required |
|---|---|---|
| Burberry Annual Report 2017/18 — disclosure line ("the cost of finished goods physically destroyed in the year was £28.6m") | Filing | Primary source for the episode's core claim — the company's own words |
| Richemont 2018 earnings report, page 3 — buyback figure (€481m over two years) | Filing | Second independent primary source — this is what earns "pattern" rather than "isolated case" |

**Deliberately not sourced:** a news-headline screenshot for the
"Burberry stopped / France banned" beat, and product photography of
either brand — cut to minimize asset count. The regulatory facts are
carried by typography instead; AI atmosphere covers the emotional
register without a licensing dependency or trademark-legibility risk.

## Diagram (1)

**Name:** The Markdown Tax (comparison diagram)
**Appears:** Beat 6, 0:33–0:44

- **Nodes:** "Discount it" → "$490 recovered" → "Rest of the line now
  looks discounted too" (widening, red) on one side; "Destroy it" →
  "$0 recovered" → "No signal sent" (small, contained) on the other.
- **Colors:** amber (`#E8A838`) for recovered cash only; red (`#E05555`)
  for both the discount's signal damage and destruction's sunk cost —
  same color, different scale, which is the point; gray (`#6B7280`) for
  structural labels; purple (`#A855F7`) reserved for the single closing
  caption, matching the shot list's Beat 6 purple-moment note.
- **Build order:** left side builds first (discount → signal expansion),
  hold, then right side builds (destroy → no expansion), hold both, then
  the purple mechanism-name caption fades in last.

## Typography (episode-wide)

Hook number card, scale card, question card, signal-reframe card, reveal
caption (the sole purple use), consequence cards, personal-stake cards
(8a/8b), closing question card. Subtitle font: Inter Medium, max 8
words/line throughout, independent of the display-number cards.

## Logo

Open Secret logo (A1 variant) — outro only, cross-dissolved in at the
close of Beat 9.

## Total unique hard assets

5 AI video blocks + 2 real artifacts + 1 diagram = 8.
