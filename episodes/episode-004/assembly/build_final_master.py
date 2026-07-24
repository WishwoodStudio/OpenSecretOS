"""
Editorial-only assembly of the 37-second master. No generation calls.
Reuses:
 - the untouched beat segments already prepared for the picture-lock
   (assembly/prepared/seg_01..seg_04c.mp4, seg_08.mp4, seg_09.mp4)
 - the original per-shot generated insert footage
   (assets/Generated/insert-*), re-trimmed with different in/out points
   than the previously-delivered insert file used, to recover the 1
   extra second needed to fill the 15s placeholder span from 14s of
   distinct content -- using more of the already-generated Scene 1
   footage (unused headroom in already-generated clips), not a speed
   change and not new material.

No CapCut project exists for Episode 004 to edit directly -- unlike
Luxury Destruction, this episode's picture-lock was built directly via
ffmpeg from the start (see production-log.md), so there is no draft to
open. Proceeding via the explicitly authorized ffmpeg fallback.
"""

import os
import subprocess

FFMPEG = r"C:\Users\Eugene\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
ROOT = r"C:\Projects\OpenSecretOS\episodes\episode-004"
GEN = os.path.join(ROOT, "assets", "Generated")
PREPARED = os.path.join(ROOT, "assembly", "prepared")
REPLACE_DIR = os.path.join(ROOT, "assembly", "replacement_prepared")
os.makedirs(REPLACE_DIR, exist_ok=True)

PRIMARY = "0xEDEAE2"


def sub_lines(lines, fontsize=44, y_from_bottom=300, color=PRIMARY):
    filters = []
    n = len(lines)
    for i, line in enumerate(lines):
        y = f"h-{y_from_bottom + (n - 1 - i) * (fontsize + 16)}"
        esc = line.replace("'", "\\'")
        filters.append(
            f"drawtext=text='{esc}':fontcolor={color}:fontsize={fontsize}:"
            f"fontfile='{FONT}':x=(w-text_w)/2:y={y}:box=1:boxcolor=0x0D1117@0.55:boxborderw=14"
        )
    return ",".join(filters)


def label_top(text, fontsize=48, y="120", color=PRIMARY):
    esc = text.replace("'", "\\'")
    return (f"drawtext=text='{esc}':fontcolor={color}:fontsize={fontsize}:"
            f"fontfile='{FONT}':x=(w-text_w)/2:y={y}:box=1:boxcolor=0x0D1117@0.55:boxborderw=14")


# Replacement segments for placeholders 1, 2, 3 (0:16-0:21, 0:21-0:26, 0:26-0:31)
REPLACEMENTS = [
    # (id, source, trim_start, trim_dur, extra_vf)
    ("ph1a", os.path.join(GEN, "insert-1a-printing-press", "insert-1a_v1_seedance2mini.mp4"), 0, 1.67, None),
    ("ph1b", os.path.join(GEN, "insert-1b-empty-site", "insert-1b_v1_seedance2mini.mp4"), 0, 1.67, None),
    ("ph1c", os.path.join(GEN, "insert-1c-farmland", "insert-1c_v1_seedance2mini.mp4"), 0, 1.66,
     sub_lines(["PRINT ≠ BUILD"])),  # subtitle appears once, on the last sub-shot of the montage
    ("ph2", os.path.join(GEN, "insert-2-people-running", "insert-2_v1_seedance2mini.mp4"), 0, 5.00,
     sub_lines(["MORE MONEY", "SAME STUFF"])),
    ("ph3", os.path.join(GEN, "insert-3-pie-slicing", "insert-3_v1_seedance2mini.mp4"), 0, 5.00,
     label_top("WEALTH") + "," + sub_lines(["PIE → MORE SLICES"])),
]

prepared_replacements = []
for seg_id, src, start, dur, extra in REPLACEMENTS:
    assert os.path.exists(src), f"Missing: {src}"
    out = os.path.join(REPLACE_DIR, f"seg_{seg_id}.mp4")
    vf = "fps=30,setsar=1,setpts=PTS-STARTPTS"
    if extra:
        vf += "," + extra
    cmd = [FFMPEG, "-y", "-i", src, "-ss", str(start), "-t", str(dur),
           "-vf", vf, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED", seg_id, r.stderr[-2000:])
        raise SystemExit(1)
    prepared_replacements.append(out)
    print("prepared replacement", seg_id)

# Full 37s order: untouched beats 1-4, new placeholder replacement (15s), untouched beats 8-9.
UNTOUCHED_BEFORE = ["seg_01.mp4", "seg_02a.mp4", "seg_02b.mp4", "seg_02c.mp4",
                     "seg_03.mp4", "seg_04a.mp4", "seg_04b.mp4", "seg_04c.mp4"]
UNTOUCHED_AFTER = ["seg_08.mp4", "seg_09.mp4"]

full_order = [os.path.join(PREPARED, f) for f in UNTOUCHED_BEFORE] + \
             prepared_replacements + \
             [os.path.join(PREPARED, f) for f in UNTOUCHED_AFTER]

for f in full_order:
    assert os.path.exists(f), f"Missing segment: {f}"

inputs = []
filt = []
for i, f in enumerate(full_order):
    inputs += ["-i", f]
    filt.append(f"[{i}:v]")
filt_str = "".join(filt) + f"concat=n={len(full_order)}:v=1:a=0[outv]"

final_out = os.path.join(ROOT, "assembly", "episode-004_v2_final-master.mp4")
cmd = [FFMPEG, "-y"] + inputs + ["-filter_complex", filt_str, "-map", "[outv]",
                                   "-c:v", "libx264", "-pix_fmt", "yuv420p", final_out]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("CONCAT FAILED", r.stderr[-3000:])
    raise SystemExit(1)
print("FINAL MASTER:", final_out)
