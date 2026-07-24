# Production Log — Episode 004

## 2026-07-18 — First full production pass

**Source:** `Episode_004_Approved_Script.md` (canonical narration, provided
and archived to `script/`), plus a detailed storyboard supplied in the
same request (shot direction, subtitles, black-placeholder beats,
generation instructions).

**Output:** `assembly/episode-004_v1_picture-lock.mp4` — 37.000s exactly,
720×1280, H.264. Picture-locked; no audio track (see Gap #1 below).

### What was generated

9 live-action shots via Seedance 2.0 Mini (Higgsfield), each at the
model's 4-second minimum duration, matching the storyboard's own
"one visual every 3-5 seconds" retention direction:

| Shot | Beat | Subject |
|---|---|---|
| shot-01 | 1 | Banknotes close-up |
| shot-02a/b/c | 2 | Government meeting / tax paperwork / budget cuts (montage) |
| shot-04a/b/c | 4 | Builder / farmer / worker (montage) |
| shot-08 | 8 | Hand taking a pie slice |
| shot-09 | 9 | Pull-back reveal, pie + civic building |

**Budget note:** cost scales linearly with duration (confirmed: 10
credits per 4s clip vs. the 37.5 credits/15s clip rate used throughout
Luxury Destruction — same 2.5 credits/second rate both times). Total
spend: 90 credits against a 92.5 balance — 9 generations fit with only
2.5 credits to spare. No retries were needed beyond two free
preset-matcher interceptions (declined, resubmitted literally, no
charge — same pattern observed during Luxury Destruction).

### What was built without cost (ffmpeg only)

- 3 pure-black full-frame placeholders (beats 5, 6, 7), exact durations
  (5s each) per the script's explicit instruction not to generate
  motion graphics for these.
- 1 text-reveal card (beat 3, "MONEY ≠ WEALTH"), styled per the
  existing Visual Identity System Purple Rule — this episode's single
  purple use, at its mechanism-reframing moment, same rule Luxury
  Destruction's diagram reveal used.

### Assembly

All 13 segments (9 shots, 3 placeholders, 1 reveal card) trimmed to
their exact beat duration, subtitled per the storyboard's exact given
text, and concatenated via `ffmpeg` `filter_complex concat` (not the
concat demuxer — that approach produced frame-duplication artifacts on
mismatched-fps inputs during Luxury Destruction's pacing-review build;
avoided here from the start). Script: `assembly/build_episode.py`.

### Known gaps, stated plainly

1. **No narration audio.** The script is the canonical narration text,
   but no ElevenLabs generation was requested or authorized for this
   episode (no voice selected — the same open item Luxury Destruction's
   Voice Package flagged and never resolved). This render is picture +
   burned-in text only. Not silently treated as final — flagged here.
2. **The 37-second target is unvalidated against real speech, same as
   Luxury Destruction's 58s estimate was.** That estimate ran long by
   ~8% once real narration existed (62.589s actual). This script's word
   count (~109 words over 37s ≈ 2.95 words/sec) sits in the same
   optimistic range Luxury Destruction's original estimate did before
   real narration corrected it. Recorded as a real risk, not a
   prediction of failure — resolve the same way: get real narration,
   compare, adjust assembly-level timing if needed, don't touch this
   picture lock preemptively.
3. **Beat 8's shot doesn't show "many thin slices"** as the generation
   prompt intended — the rendered pie reads as a single lattice-top pie
   with one slice being lifted, not a pie already cut into many pieces.
   Still serves the beat's narration adequately as a "taking a slice"
   metaphor; noted for anyone reviewing before this is called final.

### Placeholder timeline (for CapCut replacement)

See `assembly/PLACEHOLDER-NOTES.md` for exact timestamps, intended
motion graphic per placeholder, and replacement instructions.

## 2026-07-18 — Placeholders replaced; final master assembled

**No CapCut project existed for this episode to edit directly** — unlike
Luxury Destruction, this picture-lock was built via `ffmpeg` from the
start, so there was no draft to open. Assembled the replacement via the
explicitly authorized `ffmpeg` fallback instead
(`assembly/build_final_master.py`). No generation calls made in this
pass — editing only, reusing already-generated footage.

**Discrepancy resolved, not silently absorbed:** the delivered insert
was 14s; the placeholder span was 15s (0:16–0:31, three 5s slots). To
"preserve the overall runtime (~37 seconds)" without any speed change or
new generation, the Scene 1 montage (printing press / empty site /
farmland) was extended from ~1.33s to ~1.67s per clip using footage
already present in the original 4s-per-clip generations but not used in
the previously-delivered insert file — real, already-rendered frames,
not a stretch. Scenes 2 and 3 fill their 5s slots exactly as generated.

**Subtitles restored:** the delivered insert file was clean (no
captions, by design for that request). Re-added the original placeholder
subtitles ("PRINT ≠ BUILD," "MORE MONEY / SAME STUFF," "PIE → MORE
SLICES") onto the replacement footage so they carry over from the
placeholders they replace, per "preserve subtitles."

**Result:** `assembly/episode-004_v2_final-master.mp4` — 37.000s
exactly, verified by direct inspection. QA frames checked at both seams
(entry/exit of the replaced region) and mid-shot — clean cuts, correct
subtitle positioning, "WEALTH" (on-pie label) and "PIE → MORE SLICES"
(caption) render together without overlap.
