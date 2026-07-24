"""
Builds the single continuous 14-second replacement insert for the
16-30s section (was 3 separate 5s black placeholders spanning 16-31s;
this brief explicitly asked for 14s spanning 16-30s -- see the
production notes for that 1-second discrepancy, not silently absorbed).

"WEALTH" is not baked into the AI-generated pie footage -- consistent
with this project's established rule that AI video footage carries no
legible text (Visual Identity System v2 SS2), since these models render
text unreliably. Added here as a text overlay in the same style as
every other typography in this episode.
"""

import os
import subprocess

FFMPEG = r"C:\Users\Eugene\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
ROOT = r"C:\Projects\OpenSecretOS\episodes\episode-004"
GEN = os.path.join(ROOT, "assets", "Generated")
PREP = os.path.join(ROOT, "assembly", "insert_prepared")
os.makedirs(PREP, exist_ok=True)

PRIMARY = "0xEDEAE2"


def label(text, fontsize=40, y="80", color=PRIMARY):
    esc = text.replace("'", "\\'")
    return (f"drawtext=text='{esc}':fontcolor={color}:fontsize={fontsize}:"
            f"fontfile='{FONT}':x=(w-text_w)/2:y={y}:box=1:boxcolor=0x0D1117@0.55:boxborderw=14")


# (id, source, trim_start, trim_dur, extra_vf_or_None)
SEGMENTS = [
    ("1a", os.path.join(GEN, "insert-1a-printing-press", "insert-1a_v1_seedance2mini.mp4"), 0, 1.33, None),
    ("1b", os.path.join(GEN, "insert-1b-empty-site", "insert-1b_v1_seedance2mini.mp4"), 0, 1.33, None),
    ("1c", os.path.join(GEN, "insert-1c-farmland", "insert-1c_v1_seedance2mini.mp4"), 0, 1.34, None),
    ("2", os.path.join(GEN, "insert-2-people-running", "insert-2_v1_seedance2mini.mp4"), 0, 5.00, None),
    ("3", os.path.join(GEN, "insert-3-pie-slicing", "insert-3_v1_seedance2mini.mp4"), 0, 5.00, label("WEALTH", fontsize=48, y="120")),
]

prepared = []
for seg_id, src, start, dur, extra in SEGMENTS:
    assert os.path.exists(src), f"Missing: {src}"
    out = os.path.join(PREP, f"seg_{seg_id}.mp4")
    vf = "fps=30,setsar=1,setpts=PTS-STARTPTS"
    if extra:
        vf += "," + extra
    cmd = [FFMPEG, "-y", "-i", src, "-ss", str(start), "-t", str(dur),
           "-vf", vf, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED", seg_id, r.stderr[-2000:])
        raise SystemExit(1)
    prepared.append(out)
    print("prepared", seg_id)

inputs = []
filt = []
for i, f in enumerate(prepared):
    inputs += ["-i", f]
    filt.append(f"[{i}:v]")
filt_str = "".join(filt) + f"concat=n={len(prepared)}:v=1:a=0[outv]"

final_out = os.path.join(ROOT, "assembly", "episode-004_insert-16-30s_v1.mp4")
cmd = [FFMPEG, "-y"] + inputs + ["-filter_complex", filt_str, "-map", "[outv]",
                                   "-c:v", "libx264", "-pix_fmt", "yuv420p", final_out]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("CONCAT FAILED", r.stderr[-3000:])
    raise SystemExit(1)
print("FINAL:", final_out)
