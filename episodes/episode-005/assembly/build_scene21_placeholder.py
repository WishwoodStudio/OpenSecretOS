"""
Scene 21 (36.81-41.88s, 5.07s) is explicitly NOT generated per the
Production Brief: "Insert a black placeholder card for Scene 21 labelled:
CHATGPT STATIC GRAPHIC PLACEHOLDER." Pure black card, labelled, ffmpeg only.
"""

import os
import subprocess

FFMPEG = r"C:\Users\Eugene\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
ROOT = r"C:\Projects\OpenSecretOS\episodes\episode-005"
OUT = os.path.join(ROOT, "assets", "Placeholders", "scene21_chatgpt_graphic_placeholder.mp4")

DURATION = "5.07"

LINE1 = "CHATGPT STATIC"
LINE2 = "GRAPHIC PLACEHOLDER"

vf = (
    f"drawtext=text='{LINE1}':fontcolor=0xEDEAE2:fontsize=42:"
    f"fontfile='{FONT}':x=(w-text_w)/2:y=(h/2)-50,"
    f"drawtext=text='{LINE2}':fontcolor=0xEDEAE2:fontsize=42:"
    f"fontfile='{FONT}':x=(w-text_w)/2:y=(h/2)+8"
)

cmd = [
    FFMPEG, "-y",
    "-f", "lavfi", "-i", f"color=c=black:s=720x1280:d={DURATION}:r=30",
    "-vf", vf,
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    OUT,
]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("FAILED", r.stderr[-2000:])
    raise SystemExit(1)
print("PLACEHOLDER BUILT:", OUT)
