# CapCut Assembly Automation — Evaluation and Implementation

**Scope:** whether first-assembly of a CapCut project can be automated,
evaluated and implemented against Luxury Destruction's real, locked
artifacts. No future architecture proposed. No engine/pipeline redesign.
Every claim below is either a cited source or something actually run in
this repository — nothing is asserted from memory alone.

---

## 1. What CapCut project formats/import mechanisms actually exist

- **No official public API or SDK.** CapCut does not offer a public API
  for automated video rendering or project generation; its "Open
  Platform" is for building in-app plugins, not for external automated
  production ([samautomation.work](https://samautomation.work/capcut-api/)).
- **CapCut has no single project file.** A project is a folder
  (`com.lveditor.draft\<project-name>\`) containing `draft_content.json`
  (the actual timeline: tracks, segments, materials) plus
  `draft_meta_info.json` and asset subfolders. This format is
  undocumented by CapCut and known entirely through community
  reverse-engineering ([schema cheat sheet](https://gist.github.com/renezander030/80823f1d47081c312d2c1f9edd20dc22)).
  The schema is flat: segments carry a `material_id` pointing into
  `materials.<category>[]` arrays, with a companion
  `extra_material_refs[]` for transitions/fades/animations.
- **No neutral interchange format (EDL/FCPXML/OTIO) is documented as
  CapCut-importable.** Nothing in this research surfaced an official
  EDL or XML import path — only the JSON draft format above.
- **A real, maintained, pip-installable library exists for generating
  this format:** [`pycapcut`](https://github.com/GuanYixuan/pyCapCut)
  (`pip install pycapcut`), from the same author as the more established
  `pyJianYingDraft`. It generates a real draft folder — tracks,
  video/audio/text segments, transitions, keyframes, effects — without
  needing CapCut installed. Its own docs are explicit that **CapCut
  itself is not required to generate a draft, only to open/export it**,
  and that export is Windows-only; generation works on Windows,
  macOS, and Linux.
- Several other unofficial tools exist (CapCutAPI, VectCutAPI) offering
  similar capability via HTTP/MCP wrappers around the same underlying
  reverse-engineered format; `pycapcut` was used here as the most
  directly Python-scriptable, actively maintained option matching what
  this task needs.

## 2. Can Claude Code generate CapCut projects directly?

**Yes — via `pycapcut`, not via any official mechanism.** This was
verified by actually installing and running it in this repository (see
§4), not inferred from documentation alone. There is no way to generate
a *guaranteed*-correct CapCut project, because the format itself is
unofficial and the library's own docs note edge cases (e.g. composite
animation timing not always refreshing on material replacement). But
direct, real project-file generation is achievable today, not merely
theoretical.

## 3. Highest practical automation level

**Full timeline + typography assembly, for the assets that exist.** Not
"full project generation," because most of what a first CapCut assembly
needs doesn't exist yet as a real file — this is an asset gap, not a
tooling gap:

| Track | Automatable today? | Why |
|---|---|---|
| Video (Blocks A–E, placed/trimmed at locked beat boundaries) | **Yes** | Real files exist (`assets/Generated/block-*/`); timing is fully locked in `shot-list.md` / `capcut-assembly-package-v1.md` |
| Typography (13 cards, text/timing/color) | **Yes** | Fully locked, text-only — no external file dependency |
| VO audio | No | `voice-package-v1.md` is a spec; no ElevenLabs submission has happened |
| Real-artifact crops (Burberry/Richemont) | No | Not sourced anywhere in this repository |
| Diagram ("The Markdown Tax") | No | Specified, not rendered |
| Music bed | No | Rule specified, no track selected |
| Logo | No | Referenced, not confirmed present |

So: two of the seven required tracks are automatable *today*, and both
were actually implemented, not just judged possible. The other five
become automatable the moment their source files exist — the
`pycapcut` script below would only need those file paths added, not a
redesign.

## 4. Implementation — what was actually run

**Environment facts, checked directly, not assumed:** this machine had
no working Python (`Python.Python.3.12` installed via `winget` for this
task) and does not have CapCut installed at all
(`%LOCALAPPDATA%\CapCut` does not exist). Both are stated plainly
because they bound what "tested" can honestly mean here — see the
caveat at the end of this section.

**Script:** `assembly/generate_capcut_draft.py`. Reads only already-
locked data (block placement/trim table and typography card text/timing
copied verbatim from `capcut-assembly-package-v1.md`) and the five real
video files in `assets/Generated/`. Builds a draft via `pycapcut`:
one video track (5 segments, placed and trimmed at the exact locked
timecodes) and one text track (13 typography cards, exact text and
hex colors converted to RGB float tuples).

**Run result:** executed successfully, no errors.
```
DRAFT_SAVED: assembly/capcut_drafts/luxury-destruction-v1
VIDEO_SEGMENTS: 5
TEXT_SEGMENTS: 13
```

**Output validated by direct inspection of the generated
`draft_content.json`** (not just trusting the run log):
- 2 tracks: video (5 segments), text (13 segments) — matches intent
  exactly.
- All 5 video materials resolve to the real local block files.
- 13 text materials present.
- **Computed project duration: exactly 58.0 seconds** — derived by the
  library from the segment placements, independently confirming this
  matches the locked 58–59s canonical target rather than me asserting
  it does.

**What this does *not* prove, stated plainly:** this machine has no
CapCut installation, so the generated draft has not been opened in real
CapCut and its on-screen correctness (does it actually play, do the
typography cards render as intended, does CapCut accept the file without
complaint) is unverified. What's verified is that a real, community-used
library produced a structurally valid, correctly-timed draft from the
real locked data with zero errors — the honest next step is copying
`assembly/capcut_drafts/luxury-destruction-v1/` into a real CapCut
`Projects` folder (on whichever machine has CapCut installed) and
opening it there.

**One known placeholder, not a creative decision:** Block D's 3-second
segment uses the first 3 seconds of the 15-second rendered clip.
`shot-list.md` already flags that the *actual* calmest 3-second span
should be chosen visually — this script picks the start of the clip only
as a mechanical default, explicitly not a substitute for that review.

---

## Conclusion

Full CapCut project generation for this episode is not possible today —
not because the tooling can't do it, but because 5 of the 7 required
tracks have no source file yet. For the 2 tracks that do have real
source material, automation is fully implemented and produces a
structurally valid, correctly-timed draft on the first real run. The
same script is the mechanism for the rest: once VO audio, the two
real-artifact crops, the diagram, the music bed, and the logo exist as
files, extending this script to place them is additive, not a redesign.

Sources:
- [CapCut API: Official Docs & Video Automation](https://samautomation.work/capcut-api/)
- [CapCut / JianYing draft_content.json schema cheat sheet](https://gist.github.com/renezander030/80823f1d47081c312d2c1f9edd20dc22)
- [pyCapCut (GuanYixuan)](https://github.com/GuanYixuan/pyCapCut)
- [pyJianYingDraft (GuanYixuan)](https://github.com/GuanYixuan/pyJianYingDraft)
