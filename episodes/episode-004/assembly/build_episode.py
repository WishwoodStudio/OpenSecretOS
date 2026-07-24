"""
Episode 004 final assembly. Trims each source clip to its exact beat
duration, burns in the storyboard's exact subtitle text, normalizes
fps/SAR (required for clean concat, per the lesson learned building
Luxury Destruction's pacing-review preview), then concatenates all
segments in order via filter_complex concat.

No audio track: no narration was supplied or authorized for this
episode (no voice_id decision made), so this render is picture + burned
-in text only. Documented as a gap in the deliverables writeup, not
silently treated as final-final.
"""

import os
import subprocess

FFMPEG = r"C:\Users\Eugene\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
ROOT = r"C:\Projects\OpenSecretOS\episodes\episode-004"
GEN = os.path.join(ROOT, "assets", "Generated")
PH = os.path.join(ROOT, "assets", "Placeholders")
PREP = os.path.join(ROOT, "assembly", "prepared")
os.makedirs(PREP, exist_ok=True)

PRIMARY = "0xEDEAE2"


def drawtext_lines(lines, fontsize=44, y_from_bottom=300, color=PRIMARY):
    # Stack lines above y_from_bottom, bottom line closest to y_from_bottom.
    filters = []
    n = len(lines)
    for i, line in enumerate(lines):
        y = f"h-{y_from_bottom + (n - 1 - i) * (fontsize + 16)}"
        esc = line.replace("'", "\\'").replace(":", "\\:")
        filters.append(
            f"drawtext=text='{esc}':fontcolor={color}:fontsize={fontsize}:"
            f"fontfile='{FONT}':x=(w-text_w)/2:y={y}:box=1:boxcolor=0x0D1117@0.55:boxborderw=14"
        )
    return ",".join(filters)


# (segment_id, source_path, trim_start_s, trim_dur_s, subtitle_lines or None)
SEGMENTS = [
    ("01", os.path.join(GEN, "shot-01-banknotes", "shot-01_v1_seedance2mini.mp4"), 0, 4.00, ["WHY NOT PRINT MORE?"]),
    ("02a", os.path.join(GEN, "shot-02a-gov-meeting", "shot-02a_v1_seedance2mini.mp4"), 0, 1.33, ["TAXES → CUTS"]),
    ("02b", os.path.join(GEN, "shot-02b-tax-paperwork", "shot-02b_v1_seedance2mini.mp4"), 0, 1.33, ["TAXES → CUTS"]),
    ("02c", os.path.join(GEN, "shot-02c-budget-cuts", "shot-02c_v1_seedance2mini.mp4"), 0, 1.34, ["TAXES → CUTS"]),
    ("03", os.path.join(PH, "beat3_reveal_money_wealth_v2.mp4"), 0, 4.00, None),  # already has its own text baked in
    ("04a", os.path.join(GEN, "shot-04a-builder", "shot-04a_v1_seedance2mini.mp4"), 0, 1.33, ["RECEIPT"]),
    ("04b", os.path.join(GEN, "shot-04b-farmer", "shot-04b_v1_seedance2mini.mp4"), 0, 1.33, ["RECEIPT"]),
    ("04c", os.path.join(GEN, "shot-04c-worker", "shot-04c_v1_seedance2mini.mp4"), 0, 1.34, ["RECEIPT"]),
    ("05", os.path.join(PH, "beat5_black_placeholder.mp4"), 0, 5.00, ["PRINT ≠ BUILD"]),
    ("06", os.path.join(PH, "beat6_black_placeholder.mp4"), 0, 5.00, ["MORE MONEY", "SAME STUFF"]),
    ("07", os.path.join(PH, "beat7_black_placeholder.mp4"), 0, 5.00, ["PIE → MORE SLICES"]),
    ("08", os.path.join(GEN, "shot-08-slice-thinning", "shot-08_v1_seedance2mini.mp4"), 0, 4.00, ["YOUR SLICE", "GETS SMALLER"]),
    ("09", os.path.join(GEN, "shot-09-pullback", "shot-09_v1_seedance2mini.mp4"), 0, 2.00, ["WHOSE SLICE?"]),
]

prepared_files = []
for seg_id, src, start, dur, subs in SEGMENTS:
    assert os.path.exists(src), f"Missing source: {src}"
    out = os.path.join(PREP, f"seg_{seg_id}.mp4")
    vf = "fps=30,setsar=1,setpts=PTS-STARTPTS"
    if subs:
        vf += "," + drawtext_lines(subs)
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

# Concat via filter_complex (proven reliable over the concat demuxer,
# which produced frame-duplication artifacts on mismatched-fps inputs
# during Luxury Destruction's pacing-review build).
inputs = []
filt = []
for i, f in enumerate(prepared_files):
    inputs += ["-i", f]
    filt.append(f"[{i}:v]")
filt_str = "".join(filt) + f"concat=n={len(prepared_files)}:v=1:a=0[outv]"

final_out = os.path.join(ROOT, "assembly", "episode-004_v1_picture-lock.mp4")
cmd = [FFMPEG, "-y"] + inputs + ["-filter_complex", filt_str, "-map", "[outv]",
                                   "-c:v", "libx264", "-pix_fmt", "yuv420p", final_out]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("CONCAT FAILED:", r.stderr[-3000:])
    raise SystemExit(1)

print("FINAL:", final_out)
