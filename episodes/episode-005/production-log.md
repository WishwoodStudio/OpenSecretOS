# Production Log — Episode 005 ("Why Are We Obsessed With Reels?")

## 2026-07-19 — Storyboard gap, cost research, full production

### Storyboard gap (resolved before any generation)

`Episode005_Locked_Storyboard.md` as attached was a pointer file only —
it referenced "the approved 25-scene storyboard exactly as reviewed in
the previous production step" without containing it. No scene content,
timing, or continuity notes were present anywhere in the three attached
files. Flagged this explicitly and stopped rather than inventing scene
content, since the brief's own instructions repeatedly prohibit
storyboard rewrites/redesign. The user then supplied the full 25-scene
storyboard directly in chat, timed against a real silence-gap analysis
of the ElevenLabs narration (confirmed via `ffprobe`: 51.252188s, matching
the 51.25s target almost exactly). Archived as
`script/Episode005_Storyboard_Full_25_Scenes.md`, which supersedes the
pointer file for all production purposes.

### Model selection: Kling 3.0 Turbo over Seedance 2.0 Mini

Original 25-generation plan on Seedance 2.0 Mini (this project's default,
2.5 credits/sec confirmed across Episodes 004/Luxury Destruction) priced
at ~250 credits against a 147.5-credit balance — a 102.5-credit shortfall.
Researched Higgsfield's own in-app pricing widget (not third-party
estimates): Kling 3.0 costs ~5 credits per 5s/720p clip (~1 credit/sec).
Preflighted Kling 3.0 Turbo's actual rate via `generate_video`'s
`get_cost` option before spending anything: confirmed **1.5 credits/second,
exactly linear** (3s=4.5, 4s=6, 8s=12), roughly 40% cheaper than Seedance
per second. Combined with editorial shot-merging (below), this closed the
budget gap without a credit top-up.

Deliberate deviation flagged at the time: this storyboard is built
entirely around a recurring human subject's face and direct eye contact
with the lens, a real departure from the "no legible faces" Documentary
Hybrid convention every prior episode (004, Luxury Destruction) followed.
Treated the locked storyboard's explicit, repeated direction as
authoritative for this episode rather than the prior house-style default.

### Shot count reduction via merging (25 scenes -> 20 generations)

Several storyboard scenes are the same continuous take split across
multiple beats. Merged into single longer generations, then trimmed with
ffmpeg (same technique as Episode 004's `build_final_master.py`):

- Scenes 11+12 (pause -> raises phone): 1 generation, split at t=2.56s
- Scenes 13+14 (thumb hover -> swipe): 1 generation, split at t=2.59s
- Scenes 15+18+19+20 (relaxed -> bored -> swipe-away -> confident): 1
  generation (8s), split at t=1.19/3.71/5.42s
- Scene 16 (graphic-match reach pose): reused Scene 4's foraging-hands
  footage at a different in-point (t=1.50s) rather than a new generation

Deliberately NOT merged: Scene 1's 3 flash-cut people (the hook needs
"everyone," not one person) and Scene 23's 3 platform inserts (the point
is three different companies, not one). Collapsing either would have
undercut the script's own argument.

Final count: 20 generations, 75s of total source footage, 112.5 credits
spent (balance 147.5 -> 35 before QC re-generations, -> 21.5 after).
Exactly matched the projected rate with no surprises.

### Scene 21 (per brief, NOT generated)

Per the Production Brief's explicit instruction, Scene 21 is a black
card labelled "CHATGPT STATIC GRAPHIC PLACEHOLDER" rather than generated
footage — the storyboard's rich description of that scene (graphic-match
reveal, purple typography) is reference material for whoever builds the
actual graphic later, not a generation task for this pass.

### QC pass — two real problems found and fixed, one found and NOT fixed

1. **Scene 21 placeholder text overflow (FIXED).** First build's label
   ran off both edges of the 720px frame at fontsize 40 on one line.
   Rebuilt as two centered lines at fontsize 42. Verified by frame-grab
   after rebuild — fully legible now.

2. **Scene 23 platform inserts didn't match spec (FIXED via re-generation).**
   All three initial platform-insert clips (g17/g18/g19) rendered as
   photo-gallery / messaging-app screens with garbled illegible pseudo-text,
   not the "short-video feed, screen-recording style" the storyboard called
   for. Regenerated all three with more explicit prompts (full-bleed video,
   right-side action-icon rail, explicit exclusion of chat/photo-gallery
   UI). All three retries passed visual QC and were swapped into the
   final assembly. Cost: 3 x 4.5 = 13.5 credits (balance 35 -> 21.5).

3. **Actor continuity break, Scenes 11-14 vs 15/18-20 (NOT FIXED — documented).**
   Confirmed via frame comparison: the "pause -> raises phone" / "thumb
   hover-swipe" generation (scenes 11-14) shows a young man (dark hair,
   gray jacket); the "relaxed -> bored -> swipe-away -> confident" face-arc
   generation (scenes 15/18-20) shows a different person, a young woman.
   The storyboard's "same person" framing across this arc is not honored
   in the delivered footage. Root cause: Kling 3.0 Turbo has no
   cross-generation identity/character lock (confirmed in its schema —
   no reference-image or identity parameters, unlike Seedance 2.0's
   `image_references`/`video_references`). A re-generation might or might
   not fix it (no guarantee of a matching re-roll), would cost 12 of the
   remaining 21.5 credits, and was judged not worth gambling more than
   half the remaining budget on a probabilistic outcome. Documented here
   per the brief's own stated policy ("if something cannot realistically
   be generated, document the issue") rather than silently passed off as
   seamless. **This is the single most visible quality gap in the episode
   and should be the first thing addressed in a follow-up pass**, e.g. by
   generating a longer single continuous take from Scene 11 onward instead
   of separate generations, or via a model with real identity-lock
   (Seedance 2.0's `image_references` role, feeding a still frame from the
   Scene 11/12 generation as a reference for the Scene 15/18-20 generation).

Other scenes spot-checked (forager wide/effort/foraging-hands, laptop
dashboard, thumb macro) passed QC cleanly on first generation.

### Final assembly

`assembly/build_episode.py`: 28 segments (20 generated clips split into
25 scene-trims where merged, plus the Scene 21 placeholder) trimmed to
exact storyboard durations, concatenated via `filter_complex concat`
(fps=30 normalization, per the Episode 004 lesson on mismatched-fps
concat-demuxer artifacts), then muxed with the real ElevenLabs narration
track (`audio/narration.mp3`, 51.252188s).

**Result:** `assembly/episode-005_final-master.mp4` — 51.251995s
(narration: 51.252188s, delta 0.0002s), 720x1280, 30fps, H.264 + AAC.
No subtitles, no background music, per brief. Two typography moments
only: Scene 2's "DOPAMINE" (drawtext + a timed strikethrough drawbox,
a simplified stand-in for full title-animation tooling) and the Scene 21
placeholder label.

### Publish readiness

Ready to publish **with the actor-continuity gap in Scenes 11-20
disclosed** — it's a real, visible seam in the episode's central
emotional arc, not a hidden one. Everything else (timing, placeholder
handling, platform inserts after re-generation, typography, audio sync)
passed QC. No CapCut project exists for this episode (all-ffmpeg build,
consistent with Episode 004's precedent) — "project file" deliverable is
the `assembly/build_episode.py` + `build_scene21_placeholder.py` scripts,
which fully reproduce the master from source clips.

### Deliverables

1. Final vertical video: `assembly/episode-005_final-master.mp4`
2. Project file: `assembly/build_episode.py`, `build_scene21_placeholder.py`
3. All generated clips: `assets/Generated/` (20 original + 3 platform
   re-generations = 23 clips), `assets/Placeholders/` (Scene 21 card)
4. This production report
