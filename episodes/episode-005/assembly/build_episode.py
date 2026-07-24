"""
Episode 005 final assembly. Trims each of the 20 generated Kling 3.0 Turbo
clips (plus the Scene 21 black placeholder) to the exact per-scene
durations from the locked storyboard (timed against the real ElevenLabs
narration waveform, 51.252188s), concatenates all 25 scenes in order via
filter_complex concat (proven reliable over the concat demuxer on
mismatched-fps inputs, per the Episode 004 lesson), then muxes the real
narration track over the picture.

No subtitles anywhere (per brief). Two typography moments only, per the
storyboard: Scene 2's "DOPAMINE" (struck through) and Scene 21, which is
the designated black placeholder rather than generated footage.

Several source clips are reused across more than one scene at different
in-points -- a single continuous take covering multiple beats, split by
this script rather than by separate generations (commuter scroll, thumb
hover+swipe, the 4-scene face arc, pause-to-phone, foraging hands doubling
as the Scene 16 graphic-match source, and the commuter's final look-up).
"""

import os
import subprocess

FFMPEG = r"C:\Users\Eugene\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
ROOT = r"C:\Projects\OpenSecretOS\episodes\episode-005"
GEN = os.path.join(ROOT, "assets", "Generated")
PH = os.path.join(ROOT, "assets", "Placeholders")
PREP = os.path.join(ROOT, "assembly", "prepared")
os.makedirs(PREP, exist_ok=True)

PRIMARY = "0xEDEAE2"


def dopamine_overlay():
    # "DOPAMINE" appears for the whole 2.56s scene; a strikethrough line
    # (drawbox) appears over the back half, echoing "on 'wrong' it's
    # struck through" without full title-animation tooling.
    text = (
        f"drawtext=text='DOPAMINE':fontcolor={PRIMARY}:fontsize=64:"
        f"fontfile='{FONT}':x=(w-text_w)/2:y=(h-text_h)/2:"
        f"box=1:boxcolor=0x0D1117@0.55:boxborderw=18"
    )
    strike = (
        "drawbox=x=(w-340)/2:y=(h/2)-4:w=340:h=8:color=0xEDEAE2@0.95:t=fill:"
        "enable='gte(t,1.3)'"
    )
    return f"{text},{strike}"


# (segment_id, source_path, trim_start_s, trim_dur_s, extra_vf or None)
SEGMENTS = [
    ("01a", os.path.join(GEN, "g01-commuter-scroll", "g01_v1_kling3turbo.mp4"), 0.00, 0.60, None),
    ("01b", os.path.join(GEN, "g02-teen-scroll", "g02_v1_kling3turbo.mp4"), 0.00, 0.60, None),
    ("01c", os.path.join(GEN, "g03-office-scroll", "g03_v1_kling3turbo.mp4"), 0.00, 0.60, None),
    ("02", os.path.join(GEN, "g01-commuter-scroll", "g01_v1_kling3turbo.mp4"), 1.00, 2.56, dopamine_overlay()),
    ("03", os.path.join(GEN, "g04-forager-wide", "g04_v1_kling3turbo.mp4"), 0.00, 3.61, None),
    ("04", os.path.join(GEN, "g05-foraging-hands", "g05_v1_kling3turbo.mp4"), 0.00, 0.77, None),
    ("05", os.path.join(GEN, "g06-shelter-hands", "g06_v1_kling3turbo.mp4"), 0.00, 0.70, None),
    ("06", os.path.join(GEN, "g07-firelight-cave", "g07_v1_kling3turbo.mp4"), 0.00, 0.94, None),
    ("07", os.path.join(GEN, "g08-forager-effort", "g08_v1_kling3turbo.mp4"), 0.00, 2.12, None),
    ("08", os.path.join(GEN, "g09-walk-to-tree", "g09_v1_kling3turbo.mp4"), 0.00, 1.51, None),
    ("09", os.path.join(GEN, "g10-climb-hill", "g10_v1_kling3turbo.mp4"), 0.00, 1.56, None),
    ("10", os.path.join(GEN, "g11-open-book-hands", "g11_v1_kling3turbo.mp4"), 0.00, 1.55, None),
    ("11", os.path.join(GEN, "g12-pause-to-phone", "g12_v1_kling3turbo.mp4"), 0.00, 2.56, None),
    ("12", os.path.join(GEN, "g12-pause-to-phone", "g12_v1_kling3turbo.mp4"), 2.56, 1.81, None),
    ("13", os.path.join(GEN, "g13-thumb-hover-swipe", "g13_v1_kling3turbo.mp4"), 0.00, 2.59, None),
    ("14", os.path.join(GEN, "g13-thumb-hover-swipe", "g13_v1_kling3turbo.mp4"), 2.59, 1.14, None),
    ("15", os.path.join(GEN, "g14-face-arc", "g14_v1_kling3turbo.mp4"), 0.00, 1.19, None),
    ("16", os.path.join(GEN, "g05-foraging-hands", "g05_v1_kling3turbo.mp4"), 1.50, 2.57, None),
    ("17", os.path.join(GEN, "g15-scroll-blur", "g15_v1_kling3turbo.mp4"), 0.00, 1.88, None),
    ("18", os.path.join(GEN, "g14-face-arc", "g14_v1_kling3turbo.mp4"), 1.19, 2.52, None),
    ("19", os.path.join(GEN, "g14-face-arc", "g14_v1_kling3turbo.mp4"), 3.71, 1.71, None),
    ("20", os.path.join(GEN, "g14-face-arc", "g14_v1_kling3turbo.mp4"), 5.42, 1.72, None),
    ("21", os.path.join(PH, "scene21_chatgpt_graphic_placeholder.mp4"), 0.00, 5.07, None),
    ("22", os.path.join(GEN, "g16-laptop-dashboard", "g16_v1_kling3turbo.mp4"), 0.00, 1.29, None),
    ("23a", os.path.join(GEN, "g17b-platform-1-retry", "g17b_v1_kling3turbo.mp4"), 0.00, 1.34, None),
    ("23b", os.path.join(GEN, "g18b-platform-2-retry", "g18b_v1_kling3turbo.mp4"), 0.00, 1.34, None),
    ("23c", os.path.join(GEN, "g19b-platform-3-retry", "g19b_v1_kling3turbo.mp4"), 0.00, 1.33, None),
    ("24", os.path.join(GEN, "g20-commuter-lookup", "g20_v1_kling3turbo.mp4"), 0.00, 2.29, None),
    ("25", os.path.join(GEN, "g20-commuter-lookup", "g20_v1_kling3turbo.mp4"), 2.29, 1.78, None),
]

prepared_files = []
for seg_id, src, start, dur, extra in SEGMENTS:
    assert os.path.exists(src), f"Missing source: {src}"
    out = os.path.join(PREP, f"seg_{seg_id}.mp4")
    vf = "scale=720:1280,fps=30,setsar=1,setpts=PTS-STARTPTS"
    if extra:
        vf += "," + extra
    cmd = [
        FFMPEG, "-y", "-i", src, "-ss", str(start), "-t", str(dur),
        "-vf", vf, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", out,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", seg_id, r.stderr[-2000:])
        raise SystemExit(1)
    prepared_files.append(out)
    print("prepared", seg_id, "->", out)

# Concat picture-only via filter_complex.
inputs = []
filt = []
for i, f in enumerate(prepared_files):
    inputs += ["-i", f]
    filt.append(f"[{i}:v]")
filt_str = "".join(filt) + f"concat=n={len(prepared_files)}:v=1:a=0[outv]"

picture_lock = os.path.join(ROOT, "assembly", "episode-005_picture-lock.mp4")
cmd = [FFMPEG, "-y"] + inputs + ["-filter_complex", filt_str, "-map", "[outv]",
                                   "-c:v", "libx264", "-pix_fmt", "yuv420p", picture_lock]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("CONCAT FAILED:", r.stderr[-3000:])
    raise SystemExit(1)
print("PICTURE LOCK:", picture_lock)

# Mux the real narration track over the picture (video ends first per fps
# rounding on 25 trimmed segments; -shortest keeps output tied to picture).
narration = os.path.join(ROOT, "audio", "narration.mp3")
final_out = os.path.join(ROOT, "assembly", "episode-005_final-master.mp4")
cmd = [
    FFMPEG, "-y", "-i", picture_lock, "-i", narration,
    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-shortest", final_out,
]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("MUX FAILED:", r.stderr[-3000:])
    raise SystemExit(1)
print("FINAL MASTER:", final_out)
