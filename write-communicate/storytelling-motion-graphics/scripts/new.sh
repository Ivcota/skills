#!/usr/bin/env bash
# Usage: new.sh <project-dir>  -> scaffolds a Remotion project from assets/template
set -euo pipefail
skill_dir="$(cd "$(dirname "$0")/.." && pwd)"
tpl="$skill_dir/assets/template"
proj="${1:?Usage: new.sh <project-dir>}"
[ -e "$proj" ] && { echo "exists: $proj"; exit 1; }
if [ ! -d "$tpl/node_modules" ]; then
  echo "Installing shared Remotion dependencies in $tpl..."
  (cd "$tpl" && npm install)
fi
mkdir -p "$proj"
(cd "$tpl" && tar cf - --exclude=node_modules .) | (cd "$proj" && tar xf -)
ln -s "$tpl/node_modules" "$proj/node_modules"
mkdir -p "$proj/public/lottie" "$proj/public/audio" "$proj/out"
printf '# Third-party asset credits\n\n' > "$proj/CREDITS.md"
printf '# Facts / sources\n\n| Figure | Value | Real or Illustrative | Source |\n|---|---|---|---|\n' > "$proj/FACTS.md"
echo "created $proj"
