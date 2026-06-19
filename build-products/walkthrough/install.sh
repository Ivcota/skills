#!/usr/bin/env bash
# /walkthrough installer.
#
# Modes:
#   install.sh             — install globally into ~/.claude/
#   install.sh --project   — install into <cwd>/.claude/
#   install.sh --uninstall — remove hooks and skill files (preserves rationale docs)
#
# One-liner (after the repo is pushed to GitHub):
#   curl -fsSL https://raw.githubusercontent.com/Ivcota/skills/main/build-products/walkthrough/install.sh | bash -s -- --project
#
# Idempotent: re-running installs once, doesn't duplicate entries.

set -euo pipefail

# Resolve where bundle files live. When run locally, that's the dir next to
# this script. When run via `curl | bash`, BASH_SOURCE points at /dev/fd/...
# and the bundle files don't exist on disk — fetch them from GitHub instead.
WALKTHROUGH_REPO="${WALKTHROUGH_REPO:-Ivcota/skills}"
WALKTHROUGH_REF="${WALKTHROUGH_REF:-main}"
WALKTHROUGH_PATH="${WALKTHROUGH_PATH:-build-products/walkthrough}"
RAW_BASE="https://raw.githubusercontent.com/${WALKTHROUGH_REPO}/${WALKTHROUGH_REF}/${WALKTHROUGH_PATH}"

if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]:-}" ]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  STANDALONE=0
else
  SCRIPT_DIR="$(mktemp -d -t walkthrough-bootstrap.XXXXXX)"
  STANDALONE=1
  trap 'rm -rf "$SCRIPT_DIR"' EXIT
fi

fetch_bundle() {
  if ! command -v curl >/dev/null 2>&1; then
    echo "Error: curl is required for remote install." >&2
    exit 1
  fi
  echo "Fetching walkthrough bundle from ${RAW_BASE}"
  mkdir -p "$SCRIPT_DIR/references" "$SCRIPT_DIR/hooks" "$SCRIPT_DIR/commands"
  local files=(
    "SKILL.md"
    "CLAUDE-fragment.md"
    "walkthrough.config.example.json"
    "references/format.md"
    "references/chunking.md"
    "hooks/post-edit-track.sh"
    "hooks/stop-walkthrough-gate.sh"
    "commands/explain.md"
  )
  for f in "${files[@]}"; do
    curl -fsSL "$RAW_BASE/$f" -o "$SCRIPT_DIR/$f" || {
      echo "Error: failed to fetch $f from $RAW_BASE" >&2
      exit 1
    }
  done
  chmod +x "$SCRIPT_DIR/hooks/"*.sh
}

if [ "$STANDALONE" = "1" ]; then
  fetch_bundle
fi

MODE="install"
SCOPE="user"
for arg in "$@"; do
  case "$arg" in
    --project) SCOPE="project" ;;
    --uninstall) MODE="uninstall" ;;
    -h|--help)
      cat <<EOF
Usage: install.sh [--project] [--uninstall]

  (no flags)     Install into ~/.claude/ (global, all repos)
  --project      Install into <cwd>/.claude/ (just this repo)
  --uninstall    Remove hooks and skill files. Rationale docs preserved.
EOF
      exit 0
      ;;
    *) echo "Unknown arg: $arg" >&2; exit 1 ;;
  esac
done

if ! command -v jq >/dev/null 2>&1; then
  echo "Error: jq is required. Install with: brew install jq  (or apt-get install jq)" >&2
  exit 1
fi

# Resolve target dirs.
if [ "$SCOPE" = "project" ]; then
  TARGET_CLAUDE="$PWD/.claude"
  PROJECT_REPO="$PWD"
else
  TARGET_CLAUDE="$HOME/.claude"
  PROJECT_REPO="$PWD"
fi

SETTINGS_FILE="$TARGET_CLAUDE/settings.json"
SKILL_DIR="$TARGET_CLAUDE/skills/walkthrough"
COMMANDS_DIR="$TARGET_CLAUDE/commands"

# --- helpers -----------------------------------------------------------------

settings_init() {
  mkdir -p "$TARGET_CLAUDE"
  if [ ! -f "$SETTINGS_FILE" ]; then
    echo '{}' > "$SETTINGS_FILE"
  fi
}

merge_hook_entry() {
  # Args: event_name, matcher_or_empty, command_path
  local event="$1" matcher="$2" cmd="$3"
  local tmp="$SETTINGS_FILE.tmp.$$"

  jq \
    --arg event "$event" \
    --arg matcher "$matcher" \
    --arg cmd "$cmd" \
    '
    .hooks //= {} |
    .hooks[$event] //= [] |
    # remove any prior managed entry for this command
    .hooks[$event] = [
      .hooks[$event][] |
      select(
        (._walkthrough_managed != true) or
        (.hooks // [] | map(.command) | index($cmd) | not)
      )
    ] |
    .hooks[$event] += [
      (if $matcher == "" then
        { _walkthrough_managed: true,
          hooks: [{ type: "command", command: $cmd }] }
      else
        { _walkthrough_managed: true,
          matcher: $matcher,
          hooks: [{ type: "command", command: $cmd }] }
      end)
    ]
    ' "$SETTINGS_FILE" > "$tmp" && mv "$tmp" "$SETTINGS_FILE"
}

remove_managed_hooks() {
  local tmp="$SETTINGS_FILE.tmp.$$"
  jq '
    if .hooks then
      .hooks = (
        .hooks
        | to_entries
        | map(.value = [ .value[] | select(._walkthrough_managed != true) ])
        | map(select(.value | length > 0))
        | from_entries
      )
    else . end
  ' "$SETTINGS_FILE" > "$tmp" && mv "$tmp" "$SETTINGS_FILE"
}

append_claude_md_fragment() {
  local target_md="$PROJECT_REPO/CLAUDE.md"
  local fragment_file="$SCRIPT_DIR/CLAUDE-fragment.md"
  [ -f "$fragment_file" ] || return 0
  if [ -f "$target_md" ] && grep -q "walkthrough-fragment:start" "$target_md"; then
    return 0  # already installed
  fi
  {
    [ -f "$target_md" ] && echo ""
    cat "$fragment_file"
  } >> "$target_md"
}

remove_claude_md_fragment() {
  local target_md="$PROJECT_REPO/CLAUDE.md"
  [ -f "$target_md" ] || return 0
  grep -q "walkthrough-fragment:start" "$target_md" || return 0
  local tmp="$target_md.tmp.$$"
  awk '
    /<!-- walkthrough-fragment:start -->/ { skip=1 }
    skip != 1 { print }
    /<!-- walkthrough-fragment:end -->/ { skip=0; next }
  ' "$target_md" > "$tmp" && mv "$tmp" "$target_md"
}

ensure_gitignore_entry() {
  local gi="$PROJECT_REPO/.gitignore"
  local entry=".claude/session-state/"
  [ -f "$gi" ] || touch "$gi"
  if ! grep -qxF "$entry" "$gi"; then
    echo "$entry" >> "$gi"
  fi
}

# --- install ------------------------------------------------------------------

do_install() {
  echo "Installing /walkthrough → $TARGET_CLAUDE"

  mkdir -p "$SKILL_DIR/references" "$SKILL_DIR/hooks" "$COMMANDS_DIR"
  cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"
  cp "$SCRIPT_DIR/references/format.md" "$SKILL_DIR/references/format.md"
  cp "$SCRIPT_DIR/references/chunking.md" "$SKILL_DIR/references/chunking.md"
  cp "$SCRIPT_DIR/hooks/post-edit-track.sh" "$SKILL_DIR/hooks/post-edit-track.sh"
  cp "$SCRIPT_DIR/hooks/stop-walkthrough-gate.sh" "$SKILL_DIR/hooks/stop-walkthrough-gate.sh"
  chmod +x "$SKILL_DIR/hooks/"*.sh
  cp "$SCRIPT_DIR/commands/explain.md" "$COMMANDS_DIR/explain.md"

  settings_init
  merge_hook_entry "PostToolUse" "Edit|Write|NotebookEdit" "$SKILL_DIR/hooks/post-edit-track.sh"
  merge_hook_entry "Stop" "" "$SKILL_DIR/hooks/stop-walkthrough-gate.sh"

  # Per-repo data dirs (regardless of scope — these belong to the project).
  mkdir -p "$PROJECT_REPO/.claude/rationale" "$PROJECT_REPO/.claude/session-state"
  touch "$PROJECT_REPO/.claude/rationale/.gitkeep"
  if [ ! -f "$PROJECT_REPO/.claude/walkthrough.config.json" ]; then
    cp "$SCRIPT_DIR/walkthrough.config.example.json" "$PROJECT_REPO/.claude/walkthrough.config.json"
  fi

  ensure_gitignore_entry
  append_claude_md_fragment

  cat <<EOF

Installed:
  Skill:    $SKILL_DIR/
  Command:  $COMMANDS_DIR/explain.md
  Settings: $SETTINGS_FILE (hooks merged)

In this repo:
  Created:  $PROJECT_REPO/.claude/rationale/   (commit this)
  Created:  $PROJECT_REPO/.claude/session-state/ (gitignored)
  Config:   $PROJECT_REPO/.claude/walkthrough.config.json
  CLAUDE.md fragment appended (if CLAUDE.md exists)

Try it: make a non-trivial change in a Claude session. The Stop hook will
block until you produce a walkthrough.
EOF
}

# --- uninstall ----------------------------------------------------------------

do_uninstall() {
  echo "Uninstalling /walkthrough from $TARGET_CLAUDE"
  if [ -f "$SETTINGS_FILE" ]; then
    remove_managed_hooks
  fi
  rm -rf "$SKILL_DIR"
  rm -f "$COMMANDS_DIR/explain.md"
  remove_claude_md_fragment
  cat <<EOF

Removed:
  Hooks from $SETTINGS_FILE
  $SKILL_DIR/
  $COMMANDS_DIR/explain.md
  CLAUDE.md fragment

Preserved (your data):
  $PROJECT_REPO/.claude/rationale/
  $PROJECT_REPO/.claude/walkthrough.config.json
EOF
}

case "$MODE" in
  install)   do_install ;;
  uninstall) do_uninstall ;;
esac
