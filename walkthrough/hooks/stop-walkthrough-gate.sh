#!/usr/bin/env bash
# Stop hook — blocks the session from ending if a non-trivial diff exists
# but no rationale has been recorded. Emits a block message that points
# Claude at the format spec and the rationale output path.
#
# Wired by install.sh into settings.json under: hooks.Stop
#
# stdin: JSON with session_id, cwd, transcript_path, hook_event_name.
# stdout: when blocking, JSON {"decision":"block","reason":"..."} per Claude Code hook API.
# exit:   2 to block, 0 to allow.

set -u

if ! command -v jq >/dev/null 2>&1; then
  exit 0
fi

input="$(cat)"

session_id="$(printf '%s' "$input" | jq -r '.session_id // empty')"
cwd="$(printf '%s' "$input" | jq -r '.cwd // empty')"

if [ -z "$session_id" ]; then
  exit 0
fi

# Resolve project .claude/ dir.
project_claude=""
dir="${cwd:-$PWD}"
while [ -n "$dir" ] && [ "$dir" != "/" ]; do
  if [ -d "$dir/.claude" ]; then
    project_claude="$dir/.claude"
    break
  fi
  dir="$(dirname "$dir")"
done

# Without a project .claude/, this gate doesn't apply (e.g. ad-hoc sessions).
if [ -z "$project_claude" ]; then
  exit 0
fi

state_file="$project_claude/session-state/$session_id.json"
config_file="$project_claude/walkthrough.config.json"
rationale_dir="$project_claude/rationale"

# No state means no edits happened this session.
if [ ! -f "$state_file" ]; then
  exit 0
fi

# Load config with defaults.
trivial_files_default=2
trivial_lines_default=50
default_skip='["**/*.md","**/*.lock","**/package-lock.json"]'

if [ -f "$config_file" ]; then
  trivial_files="$(jq -r --argjson d "$trivial_files_default" '.trivial_threshold.files // $d' "$config_file" 2>/dev/null || echo "$trivial_files_default")"
  trivial_lines="$(jq -r --argjson d "$trivial_lines_default" '.trivial_threshold.lines // $d' "$config_file" 2>/dev/null || echo "$trivial_lines_default")"
  skip_paths_json="$(jq -c --argjson d "$default_skip" '.skip_paths // $d' "$config_file" 2>/dev/null || echo "$default_skip")"
else
  trivial_files=$trivial_files_default
  trivial_lines=$trivial_lines_default
  skip_paths_json="$default_skip"
fi

# Filter files_touched against skip_paths (glob match via case statement).
# Use newline-delimited strings instead of arrays for macOS bash 3.2 compat.
skip_patterns="$(printf '%s' "$skip_paths_json" | jq -r '.[]?')"
touched="$(jq -r '.files_touched[]?' "$state_file")"

files_count=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  skip=0
  while IFS= read -r pat; do
    [ -z "$pat" ] && continue
    # shellcheck disable=SC2254
    case "$f" in
      $pat) skip=1; break ;;
    esac
    base="${f##*/}"
    # shellcheck disable=SC2254
    case "$base" in
      ${pat##**/}) skip=1; break ;;
    esac
  done <<EOF
$skip_patterns
EOF
  [ $skip -eq 0 ] && files_count=$((files_count + 1))
done <<EOF
$touched
EOF
lines_changed="$(jq -r '.lines_changed // 0' "$state_file")"
new_files_count="$(jq -r '.new_files | length // 0' "$state_file")"
deleted_files_count="$(jq -r '.deleted_files | length // 0' "$state_file")"

# Trivial-change rule: all four must hold to skip.
trivial=1
[ "$files_count" -gt "$trivial_files" ] && trivial=0
[ "$lines_changed" -gt "$trivial_lines" ] && trivial=0
[ "$new_files_count" -gt 0 ] && trivial=0
[ "$deleted_files_count" -gt 0 ] && trivial=0

if [ $trivial -eq 1 ]; then
  exit 0
fi

# Non-trivial. Check whether a rationale already exists for this session.
if [ -d "$rationale_dir" ]; then
  if grep -l -F "session_id: $session_id" "$rationale_dir"/*.md >/dev/null 2>&1; then
    exit 0
  fi
fi

# Block. Emit the JSON instruction for Claude.
date_str="$(date -u +%Y-%m-%d)"
reason="Before stopping, produce a walkthrough for this session's diff.

Follow the format in skills/walkthrough/references/format.md exactly. Group edits per skills/walkthrough/references/chunking.md.

Write it to: .claude/rationale/${date_str}-<slug>.md

The frontmatter MUST include 'session_id: ${session_id}' so /explain can find it.

After writing, list each chunk to the user with a markdown checkbox and ask them to mark each reviewed. Do not report done until the user has acknowledged all chunks.

Diff size for this session: ${files_count} files, ${lines_changed} lines, ${new_files_count} new, ${deleted_files_count} deleted."

jq -n --arg r "$reason" '{decision: "block", reason: $r}'
exit 2
