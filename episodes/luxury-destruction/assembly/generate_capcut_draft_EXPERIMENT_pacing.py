"""
EXPERIMENT ONLY -- does not touch the locked draft
(capcut_drafts/luxury-destruction-v1/) and does not modify Script
Package, Voice Package, Director Package, or Assembly Package.

Question being tested: how much of the 62.589s real-narration overrun
(vs. the locked 58.0s visual timeline) can be absorbed by extending
existing shots' hold time, without reordering shots, without exceeding
60s, and touching typography only where the extension would otherwise
leave a shot's closing line ending before its (now longer) shot does.

Shot order and content are identical to generate_capcut_draft.py.
Only each shot's DURATION changes (four shots get +0.5s each); every
downstream shot's START time cascades forward as a pure mechanical
consequence, exactly as it would in any sequential edit. Typography
cards keep their original offset from their own shot's start unchanged
-- i.e. the same relative design -- except the one closing card that was
explicitly designed to "hold to the cut," which is extended to match its
shot's new end so it doesn't finish 0.5s before the shot does.

Output: a separate draft, "luxury-destruction-v1-EXPERIMENT-pacing", in
the same capcut_drafts/ folder. The locked draft is never opened by this
script.
"""

import os
import pycapcut as cc
from pycapcut import trange

REPO_ROOT = r"C:\Projects\OpenSecretOS"
EPISODE_DIR = os.path.join(REPO_ROOT, "episodes", "luxury-destruction")
ASSETS_DIR = os.path.join(EPISODE_DIR, "assets", "Generated")
SUPPORTING_DIR = os.path.join(EPISODE_DIR, "assets", "Supporting")
DRAFT_OUTPUT_DIR = os.path.join(EPISODE_DIR, "assembly", "capcut_drafts")

BLOCK_FILES = {
    "A": os.path.join(ASSETS_DIR, "block-A", "block-a_v1_seedance2mini.mp4"),
    "B": os.path.join(ASSETS_DIR, "block-B", "block-b_v1_seedance2mini.mp4"),
    "C": os.path.join(ASSETS_DIR, "block-C", "block-c_v1_seedance2mini.mp4"),
    "D": os.path.join(ASSETS_DIR, "block-D", "block-d_v1_seedance2mini.mp4"),
    "E": os.path.join(ASSETS_DIR, "block-E", "block-e_v1_seedance2mini.mp4"),
}
EVIDENCE_FILES = {
    "burberry": os.path.join(SUPPORTING_DIR, "burberry-evidence-v1.png"),
    "richemont": os.path.join(SUPPORTING_DIR, "richemont-evidence-v1.png"),
}
NARRATION_FILE = os.path.join(ASSETS_DIR, "voice", "narration_v1.mp3")
DIAGRAM_FILE = os.path.join(ASSETS_DIR, "diagram", "markdown-tax-diagram_v1.mp4")
for path in list(BLOCK_FILES.values()) + list(EVIDENCE_FILES.values()) + [NARRATION_FILE, DIAGRAM_FILE]:
    assert os.path.exists(path), f"Missing asset: {path}"

# --- Experimental shot durations -------------------------------------
# (shot_id, file, original_duration_s, added_s)
# Order unchanged from the locked draft. Only "added_s" is new.
SHOTS = [
    ("A",         BLOCK_FILES["A"],          5.0,  0.0),  # hook -- excluded, see report
    ("burberry",  EVIDENCE_FILES["burberry"], 5.0,  0.5),
    ("richemont", EVIDENCE_FILES["richemont"],7.0,  0.5),
    ("B",         BLOCK_FILES["B"],          12.0,  0.5),
    ("C",         BLOCK_FILES["C"],          11.0,  0.5),
    ("D",         BLOCK_FILES["D"],           3.0,  0.0),  # tightest shot -- excluded, see report
    # E excluded: source clip is only 15.042s and Block E already uses
    # the full 15.0s of it -- 0.042s of real slack, not enough for a
    # meaningful extension via simple trim. See report.
    ("E",         BLOCK_FILES["E"],          15.0,  0.0),
]

TYPOGRAPHY_CARDS = [
    # (content, original_start_s, original_duration_s, hex_color)
    ("£28.6 MILLION", 0, 2, "#EDEAE2"),
    ("Of its own clothes. Burned.", 2, 3, "#EDEAE2"),
    ("5 years. £90,000,000.", 7, 3, "#E8A838"),
    ("€481,000,000", 14, 3, "#E8A838"),
    ("Same decision. Why?", 17, 5, "#EDEAE2"),
    ("A marked-down coat isn't one lost sale.", 22, 3, "#EDEAE2"),
    ("It's a price tag for everything.", 25, 4, "#EDEAE2"),
    ("THE MARKDOWN TAX", 37, 3, "#A855F7"),
    ("2018 — Burberry stops.", 40, 1.5, "#6B7280"),
    ("2022 — France bans it.", 41.5, 1.5, "#6B7280"),
    ("There's a different way to read it.", 43, 6, "#EDEAE2"),
    ("The markdown tax — paid in a different currency.", 49, 7, "#EDEAE2"),
    ("Exclusivity? Or the markdown tax?", 56, 2, "#EDEAE2"),
]
# The one typography change made: this closing card originally held to
# its shot's cut (56-58s, Block E's original end). Block E's end moves;
# extending only this card keeps that "holds to the cut" design intact
# instead of ending 0.5s before the shot does.
HOLD_TO_CUT_CARDS = {"Exclusivity? Or the markdown tax?"}


def hex_to_rgb01(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return (round(r / 255, 3), round(g / 255, 3), round(b / 255, 3))


def main():
    # Compute new shot starts by walking the fixed order forward.
    shot_new = {}
    cursor = 0.0
    for shot_id, _file, orig_dur, added in SHOTS:
        new_dur = orig_dur + added
        shot_new[shot_id] = {"start": cursor, "orig_start": None, "orig_dur": orig_dur,
                               "new_dur": new_dur, "added": added}
        cursor += new_dur
    total = cursor

    # Recover each shot's ORIGINAL start (for offset math) by walking the
    # original durations forward the same way.
    orig_cursor = 0.0
    for shot_id, _file, orig_dur, _added in SHOTS:
        shot_new[shot_id]["orig_start"] = orig_cursor
        orig_cursor += orig_dur

    draft_folder = cc.DraftFolder(DRAFT_OUTPUT_DIR)
    script = draft_folder.create_draft(
        "luxury-destruction-v1-EXPERIMENT-pacing", 720, 1280, allow_replace=True
    )
    script.add_track(cc.TrackType.audio, "narration")
    script.add_track(cc.TrackType.video, "base_video")
    script.add_track(cc.TrackType.video, "diagram_overlay")
    script.add_track(cc.TrackType.text, "typography")

    narration_material = cc.AudioMaterial(NARRATION_FILE)
    script.add_segment(
        cc.AudioSegment(narration_material, trange("0s", narration_material.duration)),
        track_name="narration",
    )

    for shot_id, file_path, orig_dur, added in SHOTS:
        s = shot_new[shot_id]
        script.add_segment(
            cc.VideoSegment(file_path, trange(f"{s['start']}s", f"{s['new_dur']}s")),
            track_name="base_video",
        )

    # Diagram overlay: fixed 11s pre-rendered animation, NOT stretched.
    # Repositioned to Block C's new start; plays in full, then Block C's
    # backdrop alone covers the added 0.5s before the cut to D.
    c_start = shot_new["C"]["start"]
    script.add_segment(
        cc.VideoSegment(DIAGRAM_FILE, trange(f"{c_start}s", "11s")),
        track_name="diagram_overlay",
    )

    # Typography: cascade each card by its own shot's start delta, i.e.
    # keep the same offset-from-shot-start (unchanged relative design).
    # One exception: the "holds to the cut" closing card is stretched to
    # match its shot's new end instead of its old one.
    # Map each card to the shot it visually belongs to by original time.
    def shot_for_time(t):
        for shot_id, _file, orig_dur, _added in SHOTS:
            os_ = shot_new[shot_id]["orig_start"]
            if os_ <= t < os_ + orig_dur + 1e-6:
                return shot_id
        return SHOTS[-1][0]

    for content, orig_start, orig_dur, hex_color in TYPOGRAPHY_CARDS:
        shot_id = shot_for_time(orig_start)
        s = shot_new[shot_id]
        offset = orig_start - s["orig_start"]
        new_start = s["start"] + offset
        if content in HOLD_TO_CUT_CARDS:
            new_dur = (s["start"] + s["new_dur"]) - new_start
        else:
            new_dur = orig_dur
        script.add_segment(
            cc.TextSegment(
                content, trange(f"{new_start}s", f"{new_dur}s"),
                style=cc.TextStyle(color=hex_to_rgb01(hex_color), align=1),
            ),
            track_name="typography",
        )

    script.save()

    print("EXPERIMENTAL_DRAFT_SAVED:", os.path.join(DRAFT_OUTPUT_DIR, "luxury-destruction-v1-EXPERIMENT-pacing"))
    print("TOTAL_RUNTIME_S:", round(total, 3))
    print("NARRATION_S:", round(narration_material.duration / 1_000_000, 3))
    print()
    print("Shot".ljust(12), "orig".rjust(6), "added".rjust(7), "new".rjust(6), "new_start".rjust(10), "new_end".rjust(9))
    for shot_id, _file, orig_dur, added in SHOTS:
        s = shot_new[shot_id]
        print(shot_id.ljust(12), f"{orig_dur:.1f}s".rjust(6), f"+{added:.1f}s".rjust(7),
              f"{s['new_dur']:.1f}s".rjust(6), f"{s['start']:.1f}s".rjust(10),
              f"{s['start']+s['new_dur']:.1f}s".rjust(9))


if __name__ == "__main__":
    main()
