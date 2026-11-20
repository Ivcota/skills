#!/usr/bin/env bash
# Usage: preview.sh <project-dir> -> out/preview.mp4 (half-res) + out/contact.png (1 fps) + cut strips
set -euo pipefail
proj="$(cd "$1" && pwd)"
cd "$proj"
npx remotion render src/index.ts Story out/preview.mp4 --scale 0.5 --muted --log error
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 out/preview.mp4)
n=$(python3 -c "import math;print(math.ceil($dur))")
cols=6; rows=$(( (n + cols - 1) / cols ))
ffmpeg -y -v error -i out/preview.mp4 -vf "fps=1,scale=480:-1,drawtext=text='%{pts\:hms}':x=8:y=8:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6,tile=${cols}x${rows}:padding=6:margin=6" -frames:v 1 out/contact.png
python3 - << 'PY'
import json, subprocess
cfg = json.load(open('scenes.json'))
fps = cfg['fps']
t = 0
for i, tr in enumerate(cfg.get('transitions', [])):
    t += cfg['scenes'][i]['frames'] - tr['frames']
    start_s = max(0.0, t / fps - 0.5)
    out = f"out/cut{i+1}.png"
    subprocess.run([
        'ffmpeg', '-y', '-v', 'error', '-ss', f'{start_s:.2f}', '-t', '1.4', '-i', 'out/preview.mp4',
        '-vf', 'fps=10,scale=320:-1,tile=7x2:padding=4:margin=4', '-frames:v', '1', out
    ], check=True)
PY
echo "preview: $proj/out/preview.mp4  contact: $proj/out/contact.png  (${dur}s)"
