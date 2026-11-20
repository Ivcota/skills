#!/usr/bin/env bash
# Usage: render.sh <project-dir> [output-mp4]
set -euo pipefail
proj="$(cd "$1" && pwd)"
out="${2:-${proj%/}.mp4}"
cd "$proj"
npx remotion render src/index.ts Story out/video.mp4 --muted --codec h264 --crf 16 --pixel-format yuv420p --log error
ffmpeg -y -v error -i out/video.mp4 -i public/audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -shortest -movflags +faststart "$out"
echo "final: $out"
