# Export V1 Preparation — Luxury Destruction

**Source of truth:** `assembly/capcut_drafts/luxury-destruction-v1/`
(the validated CapCut draft — 2 tracks, 5 video segments, 13 typography
segments, 58.0s computed duration). Every item below traces to an
already-locked artifact; nothing here reopens or edits Script Package
v3, Director Package v3, or Voice Package v1 — only what those already
specify is being located, produced, or imported.

---

## 1. Manual Assembly Checklist (in order)

**Phase 1 — Unblock narration (do first; several later steps depend on real timing)**
1. Select a narrator voice (`voice_id`) against the criteria already on
   record in `voice/voice-package-v1.md` (documentary/analytical
   register, flat hook delivery + genuine-question inflection). A
   production decision, not a script edit.
2. Submit `voice/elevenlabs-generation-package-v1.md`'s exact text and
   settings to ElevenLabs with that voice, requesting word-level
   timestamps.
3. Download and archive the resulting audio file (same
   `assets/Generated/` convention already used for Blocks A–E).
4. Compare real per-beat timestamps against the planned boundaries in
   `shot-list.md` / `capcut-assembly-package-v1.md`. Watch Beat 7
   especially (planned 3s for two typography cards, 1.5s each — already
   flagged as the tightest point in the episode). If real timing lands
   within 58–59s and beats don't drift materially, proceed. If not: log
   it as production evidence in `production-log.md`, per the
   verification protocol `voice-package-v1.md` already defines. Do not
   edit the script.

**Phase 2 — Produce the remaining static assets (can run in parallel with Phase 1)**
5. Locate and crop the Burberry Annual Report 2017/18 disclosure line.
6. Locate and crop the Richemont 2018 earnings report, page 3, buyback
   figure.
7. Build "The Markdown Tax" diagram exactly per `asset-manifest.md`'s
   node/color/build-order spec.
8. Select or license a single continuous ambient/analytical music bed
   satisfying the "no Content ID risk" rule.
9. Locate the existing Open Secret logo file (A1 variant).

**Phase 3 — Import into the validated draft**
10. Import VO audio to a new audio track; sync to real timestamps (not
    the planning estimates currently in the draft).
11. If Phase 1 step 4 found drift, re-anchor the video and typography
    segment timings in the draft to match.
12. Insert the Burberry crop into Beat 2's gap (currently empty on the
    video track).
13. Insert the Richemont crop into Beat 3's gap (currently empty).
14. Insert the diagram as an overlay on top of Block C during Beat 6,
    matching the build-in timing already specified.
15. Add a subtitle track (Inter Medium, max 8 words/line) synced to real
    VO timestamps — this is separate from the 13 typography cards
    already in the draft and can't be produced until step 3 is done.
16. Import the music bed to its own audio track; apply the entry/lift/
    settle/fade points already specified in the Assembly Package.
17. Import the logo; apply the 200ms cross-dissolve at the true
    end-of-VO timestamp.
18. Review Block D's 3-second segment: the draft currently uses the
    first 3 seconds of the clip as a placeholder. Confirm it or trim to
    the actual calmest 3-second span — already flagged as an open visual
    check in `shot-list.md`, not a new decision.
19. Sanity-check the three sub-card timings inside Beat 8 (already
    flagged in the Assembly Package as this package's own derived
    timing, not something locked upstream) against real VO.

**Phase 4 — QA and export**
20. Run the mechanical/editorial QA checklist already defined in
    `source/OS_Production_Package_LuxuryDestruction_v2.md` §13 (Purple
    Rule — purple appears exactly once; both real artifacts legible at
    mobile scale; no Content ID risk; first frame is the hook visual;
    subtitles present; Rolling Payoff Rule holds against the actual
    cut). Cited, not rewritten.
21. Resolve the resolution question in §5 below before export.
22. Export.

---

## 2–3. Missing assets — placement, defining artifact, specification status

| Asset | Timeline placement | Defined by | Status |
|---|---|---|---|
| Narration audio | Continuous, 0:00–end | `voice/voice-package-v1.md`, `voice/elevenlabs-generation-package-v1.md` | Text and settings fully specified. **One open, bounded decision remains: which voice.** No creative rewrite needed once chosen. |
| Music | 0:00 in, lift at Beat 6 start, settle at Beat 8 start, fade at end | `assembly/capcut-assembly-package-v1.md` §6 | Entry/exit rule and timing fully specified. **Actual track not selected** — a bounded licensing/curatorial pick within an already-fixed rule, not open pacing work. |
| Burberry annual report crop | Beat 2, 0:05–0:10 (real timestamps once VO exists) | `director-package-v3/shot-list.md`, `source/OS_Production_Package_LuxuryDestruction_v2.md` §7 | **Fully specified** (exact document, exact disclosure line quoted). Needs sourcing + cropping — production work, not creative work. |
| Richemont earnings report crop | Beat 3, 0:10–0:17 | Same as above | **Fully specified** (exact document, page, figure). Needs sourcing + cropping only. |
| "The Markdown Tax" diagram | Beat 6, 0:29–0:40, overlaid on Block C | `director-package-v3/asset-manifest.md` §Diagram | **Fully specified** — nodes, colors, flows, labels, build order all locked. Needs production (building the graphic), zero open creative decisions. |
| Logo | 0:58, outro, 200ms cross-dissolve | `director-package-v3/asset-manifest.md` §Logo | Referenced as an existing brand asset (A1 variant). **Not found anywhere in this repository** — needs locating, not designing. |
| Subtitles | Continuous, throughout | `source/...v2.md` §9 Typography Package (Inter Medium, max 8 words/line) | Rule fully specified. Cannot be produced until real VO timestamps exist (Phase 1) — a dependency, not missing creative work. |

No item above requires reopening Script Package, Director Package, or
Voice Package — each is either sourcing a real document, producing a
fully-specified graphic, or a bounded pick within an already-fixed rule.

---

## 4. Remaining manual actions inside CapCut

Everything in Phase 3 and Phase 4 above is manual CapCut work: importing
6 new assets (VO, music, 2 crops, diagram, logo) onto tracks the
generated draft doesn't yet have; adding a subtitle track; re-anchoring
timing if VO drifts; the Block D trim review; the Beat 8 sub-card timing
check; and running the existing QA checklist. Nothing in the video or
typography tracks already in the draft needs manual rework — those were
generated correctly and validated (§ prior session).

---

## 5. Can Export V1 be completed without modifying any upstream artifact?

**Yes, realistically — with one compliance gap to flag, not fix.**

Every remaining task above is asset production, sourcing, or mechanical
CapCut assembly. None of it requires reopening Script Package, Director
Package, or Voice Package. The one built-in risk (VO timing drift) already
has a defined non-upstream-modifying resolution: log it as production
evidence, same as the original 58s/76s conflict, rather than edit the
script.

**One real, previously undocumented gap found while preparing this
checklist:** the validated draft's canvas and all 5 generated video
blocks are natively **720×1280** (Seedance 2.0 Mini's resolution
ceiling — it does not support 1080p). The canonical Publishing Target
(`Decision Log v2`; `Visual Identity System v2` §8) specifies
**1080×1920**. This doesn't force reopening any upstream artifact — it's
resolvable at export time (CapCut can upscale to 1080×1920, with some
softness) or by shipping at 720×1280 — but it is a real compliance
question nobody has decided yet, stated here as evidence, not solved
here.
