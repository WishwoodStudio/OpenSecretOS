"""
Generates a real CapCut draft for Luxury Destruction from already-locked
production artifacts (script-package-v3.md, shot-list.md,
asset-manifest.md, capcut-assembly-package-v1.md). No new creative or
timing decisions are made here -- every timestamp, every typography
card's text, and every color below is copied from those locked
documents, unless noted otherwise in the dated updates below.

2026-07-12 update: the two documentary evidence images (Burberry annual
report crop, Richemont/Guardian evidence crop) were approved and placed
on the base video track, filling the gap left for them.

2026-07-13 update (narration + diagram): the real ElevenLabs narration
MP3 and the rendered Markdown Tax diagram MP4 were added -- narration on
its own audio track (full real length, unmodified), diagram on its own
overlay track above Block C at the originally-locked Beat 6 timing.
Real narration measured 62.589s, longer than the 58s visual timeline at
the time.

2026-07-13 update (visual pacing decision): following review, the
58-59s target was explicitly retired in favor of the real narration as
the reference timeline -- the script is locked, the narration is
approved, and the objective is now the best-paced finished edit against
that real 62.589s length, not preserving the old estimate. Shot ORDER
is unchanged. Shot DURATIONS are extended, distributed across five
shots rather than concentrated in one, using two techniques:
  (a) simple hold extension, using real spare footage each block's own
      15.042s source clip already contains beyond what was previously
      used (Burberry/Richemont holds, Block B, Block C, Block D), and
  (b) a small, quantified speed reduction on Block E only, because its
      full 15.042s of source was already in use and no further hold
      extension was possible without it (see BLOCK_E_SPEED below).
Block A (the hook) and the diagram's own internal animation are
deliberately untouched -- seem inline comments below for why each shot
was or wasn't extended. Typography keeps each card's original offset
from its own shot's start (unchanged relative design); the two
exceptions -- Block D's pair of cards re-split evenly across its new,
longer duration, and the final "holds to the cut" closing card extended
to match the true new end -- are called out explicitly below.
"""

import os
import pycapcut as cc
from pycapcut import trange

REPO_ROOT = r"C:\Projects\OpenSecretOS"
EPISODE_DIR = os.path.join(REPO_ROOT, "episodes", "luxury-destruction")
ASSETS_DIR = os.path.join(EPISODE_DIR, "assets", "Generated")
DRAFT_OUTPUT_DIR = os.path.join(EPISODE_DIR, "assembly", "capcut_drafts")

os.makedirs(DRAFT_OUTPUT_DIR, exist_ok=True)

BLOCK_FILES = {
    "A": os.path.join(ASSETS_DIR, "block-A", "block-a_v1_seedance2mini.mp4"),
    "B": os.path.join(ASSETS_DIR, "block-B", "block-b_v1_seedance2mini.mp4"),
    "C": os.path.join(ASSETS_DIR, "block-C", "block-c_v1_seedance2mini.mp4"),
    "D": os.path.join(ASSETS_DIR, "block-D", "block-d_v1_seedance2mini.mp4"),
    "E": os.path.join(ASSETS_DIR, "block-E", "block-e_v1_seedance2mini.mp4"),
}
for letter, path in BLOCK_FILES.items():
    assert os.path.exists(path), f"Block {letter} asset missing: {path}"

SUPPORTING_DIR = os.path.join(EPISODE_DIR, "assets", "Supporting")
EVIDENCE_FILES = {
    "burberry": os.path.join(SUPPORTING_DIR, "burberry-evidence-v1.png"),
    "richemont": os.path.join(SUPPORTING_DIR, "richemont-evidence-v1.png"),
}
for name, path in EVIDENCE_FILES.items():
    assert os.path.exists(path), f"Evidence asset missing: {path}"

NARRATION_FILE = os.path.join(ASSETS_DIR, "voice", "narration_v1.mp3")
assert os.path.exists(NARRATION_FILE), f"Narration asset missing: {NARRATION_FILE}"

DIAGRAM_FILE = os.path.join(ASSETS_DIR, "diagram", "markdown-tax-diagram_v1.mp4")
assert os.path.exists(DIAGRAM_FILE), f"Diagram asset missing: {DIAGRAM_FILE}"

# Shot order, unchanged. Each entry: (shot_id, file, original_duration_s,
# added_s, reason). Order of this list IS the shot order -- untouched.
SHOTS = [
    ("A", BLOCK_FILES["A"], 5.0, 0.0,
     "hook -- untouched on purpose; Hook Rule requires landing within 3s, "
     "extending it works against its own design regardless of overall runtime"),
    ("burberry", EVIDENCE_FILES["burberry"], 5.0, 0.5,
     "static document hold with slow push-in; real spare screen time exists, "
     "a longer hold on a still image is the least perceptible extension available"),
    ("richemont", EVIDENCE_FILES["richemont"], 7.0, 0.5,
     "same reasoning as burberry"),
    ("B", BLOCK_FILES["B"], 12.0, 0.5,
     "3.042s of real unused footage in the 15.042s source clip; small hold extension"),
    ("C", BLOCK_FILES["C"], 11.0, 0.5,
     "4.042s of real unused footage; extension is backdrop-only, added AFTER the "
     "diagram's own fixed 11s animation finishes, so the diagram itself is untouched"),
    ("D", BLOCK_FILES["D"], 3.0, 2.0,
     "the one shot this pass deliberately fixes rather than merely absorbs time into: "
     "this beat held 8s for the same two facts before the now-retired 58s ceiling forced "
     "it down to 3s (1.5s/card); the ceiling is gone, so this restores real breathing room "
     "for two dates the audience needs to actually read, not just re-derives padding"),
    ("E", BLOCK_FILES["E"], 15.0, None,
     "handled separately -- see BLOCK_E_SPEED below; its 15.042s source clip was already "
     "fully used, so a hold extension isn't available and a small speed reduction is used instead"),
]

# Block E: source is fully used (15.0s of a 15.042s clip) with no hold
# extension available. The remaining time needed (whatever's left after
# the other five shots' extensions) is added via a small, quantified
# speed reduction instead -- an already-slow "static hold, then 2%
# push-in" shot is exactly where a few-percent slowdown is least likely
# to be noticed. Computed, not guessed: narration length minus the sum
# of every other shot's new duration.
NARRATION_FILE_DURATION_PLACEHOLDER = None  # resolved at runtime from the real file

# Diagram placement: composited above Block C, at Block C's (new) start,
# playing its own fixed 11s animation unstretched -- repositioned, never
# re-timed.
DIAGRAM_NATIVE_DURATION_S = 11.0

# Typography cards, from the CapCut Assembly Package, unless noted.
# (content, original_start_s, original_duration_s, hex_color)
TYPOGRAPHY_CARDS = [
    ("£28.6 MILLION", 0, 2, "#EDEAE2"),
    ("Of its own clothes. Burned.", 2, 3, "#EDEAE2"),
    ("5 years. £90,000,000.", 7, 3, "#E8A838"),
    ("€481,000,000", 14, 3, "#E8A838"),
    ("Same decision. Why?", 17, 5, "#EDEAE2"),
    ("A marked-down coat isn't one lost sale.", 22, 3, "#EDEAE2"),
    ("It's a price tag for everything.", 25, 4, "#EDEAE2"),
    ("THE MARKDOWN TAX", 37, 3, "#A855F7"),  # sole purple use, Purple Rule
    ("2018 — Burberry stops.", 40, 1.5, "#6B7280"),      # re-split, see D_CARDS below
    ("2022 — France bans it.", 41.5, 1.5, "#6B7280"),    # re-split, see D_CARDS below
    ("There's a different way to read it.", 43, 6, "#EDEAE2"),
    ("The markdown tax — paid in a different currency.", 49, 7, "#EDEAE2"),
    ("Exclusivity? Or the markdown tax?", 56, 2, "#EDEAE2"),  # holds to cut, extended below
]
D_CARDS = {"2018 — Burberry stops.", "2022 — France bans it."}  # re-split 50/50 across D's new duration
HOLD_TO_CUT_CARDS = {"Exclusivity? Or the markdown tax?"}       # extended to match shot's true new end


def hex_to_rgb01(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return (round(r / 255, 3), round(g / 255, 3), round(b / 255, 3))


def main():
    narration_material = cc.AudioMaterial(NARRATION_FILE)
    narration_s = narration_material.duration / 1_000_000

    # Resolve every shot's new duration, leaving Block E for last (it
    # absorbs whatever's left after the other five explicit extensions).
    fixed_total = sum(orig + (added or 0) for _sid, _f, orig, added, _r in SHOTS if added is not None)
    e_orig = next(orig for sid, _f, orig, _a, _r in SHOTS if sid == "E")
    e_new_dur = narration_s - fixed_total
    e_added = e_new_dur - e_orig
    e_speed = e_orig / e_new_dur  # < 1.0 = slight slow motion

    shot_new = {}
    cursor = 0.0
    orig_cursor = 0.0
    for shot_id, _file, orig_dur, added, _reason in SHOTS:
        new_dur = e_new_dur if shot_id == "E" else orig_dur + added
        shot_new[shot_id] = {"start": cursor, "orig_start": orig_cursor,
                              "orig_dur": orig_dur, "new_dur": new_dur}
        cursor += new_dur
        orig_cursor += orig_dur
    total = cursor

    draft_folder = cc.DraftFolder(DRAFT_OUTPUT_DIR)
    script = draft_folder.create_draft("luxury-destruction-v1", 720, 1280, allow_replace=True)
    script.add_track(cc.TrackType.audio, "narration")
    script.add_track(cc.TrackType.video, "base_video")
    script.add_track(cc.TrackType.video, "diagram_overlay")
    script.add_track(cc.TrackType.text, "typography")

    script.add_segment(
        cc.AudioSegment(narration_material, trange("0s", narration_material.duration)),
        track_name="narration",
    )

    file_lookup = {sid: f for sid, f, *_ in SHOTS}
    for shot_id, _file, orig_dur, added, _reason in SHOTS:
        s = shot_new[shot_id]
        if shot_id == "E":
            seg = cc.VideoSegment(
                file_lookup["E"],
                trange(f"{s['start']}s", f"{s['new_dur']}s"),
                speed=e_speed,
            )
        else:
            seg = cc.VideoSegment(file_lookup[shot_id], trange(f"{s['start']}s", f"{s['new_dur']}s"))
        script.add_segment(seg, track_name="base_video")

    c_start = shot_new["C"]["start"]
    script.add_segment(
        cc.VideoSegment(DIAGRAM_FILE, trange(f"{c_start}s", f"{DIAGRAM_NATIVE_DURATION_S}s")),
        track_name="diagram_overlay",
    )

    def shot_for_time(t):
        # Strict half-open interval match [start, start+dur) -- a card
        # starting exactly on a shot boundary belongs to the NEXT shot,
        # not the one ending there. No epsilon: every value here is an
        # exact literal, not an accumulated float.
        for shot_id, _file, orig_dur, _added, _reason in SHOTS:
            os_ = shot_new[shot_id]["orig_start"]
            if os_ <= t < os_ + orig_dur:
                return shot_id
        return SHOTS[-1][0]

    d_start = shot_new["D"]["start"]
    d_new_dur = shot_new["D"]["new_dur"]

    for content, orig_start, orig_dur, hex_color in TYPOGRAPHY_CARDS:
        if content in D_CARDS:
            half = d_new_dur / 2
            is_first = content == "2018 — Burberry stops."
            new_start = d_start if is_first else d_start + half
            new_dur = half
        else:
            shot_id = shot_for_time(orig_start)
            s = shot_new[shot_id]
            offset = orig_start - s["orig_start"]
            new_start = s["start"] + offset
            if content in HOLD_TO_CUT_CARDS:
                new_dur = (s["start"] + s["new_dur"]) - new_start
            else:
                new_dur = orig_dur
        script.add_segment(
            cc.TextSegment(content, trange(f"{new_start}s", f"{new_dur}s"),
                            style=cc.TextStyle(color=hex_to_rgb01(hex_color), align=1)),
            track_name="typography",
        )

    script.save()

    draft_path = os.path.join(DRAFT_OUTPUT_DIR, "luxury-destruction-v1")
    print("DRAFT_SAVED:", draft_path)
    print("TOTAL_RUNTIME_S:", round(total, 3))
    print("NARRATION_S:", round(narration_s, 3))
    print("BLOCK_E_SPEED:", round(e_speed, 5), "| BLOCK_E_ADDED_S:", round(e_added, 3))
    print()
    print("Shot".ljust(12), "orig".rjust(7), "added".rjust(8), "new".rjust(8), "start".rjust(9), "end".rjust(9))
    for shot_id, _file, orig_dur, added, _reason in SHOTS:
        s = shot_new[shot_id]
        added_s = s["new_dur"] - orig_dur
        print(shot_id.ljust(12), f"{orig_dur:.2f}s".rjust(7), f"+{added_s:.2f}s".rjust(8),
              f"{s['new_dur']:.2f}s".rjust(8), f"{s['start']:.2f}s".rjust(9), f"{s['start']+s['new_dur']:.2f}s".rjust(9))


if __name__ == "__main__":
    main()
