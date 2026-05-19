#!/usr/bin/env bash
# PostToolUse hook — appends the file path and a line-count delta to the
# session state file so the Stop hook can apply the trivial-change rule.
#
# Wired by install.sh into settings.json under:
#   hooks.PostToolUse[*].matcher = "Edit|Write|NotebookEdit"
#
# stdin: JSON from Claude Code with session_id, cwd, tool_name, tool_input.
# stdout: ignored.
# exit:   always 0. This hook never blocks.

set -u

if ! command -v jq >/dev/null 2>&1; then
  exit 0
fi

input="$(cat)"

session_id="$(printf '%s' "$input" | jq -r '.session_id // empty')"
cwd="$(printf '%s' "$input" | jq -r '.cwd // empty')"
tool_name="$(printf '%s' "$input" | jq -r '.tool_name // empty')"

if [ -z "$session_id" ] || [ -z "$tool_name" ]; then
  exit 0
fi

# Resolve the project .claude/ dir by walking up from cwd. Fall back to ~/.claude/.
state_dir=""
dir="${cwd:-$PWD}"
while [ -n "$dir" ] && [ "$dir" != "/" ]; do
  if [ -d "$dir/.claude" ]; then
    state_dir="$dir/.claude/session-state"
    break
  fi
  dir="$(dirname "$dir")"
done
if [ -z "$state_dir" ]; then
  state_dir="$HOME/.claude/session-state"
fi
mkdir -p "$state_dir"

state_file="$state_dir/$session_id.json"

# Extract the file path the tool touched.
file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.path // .tool_input.notebook_path // empty')"
if [ -z "$file_path" ]; then
  exit 0
fi

# Best-effort line-delta count.
# Edit: max(1, |new_string lines - old_string lines|)
# Write: lines in content
# NotebookEdit: lines in new_source
case "$tool_name" in
  Edit)
    old_lines="$(printf '%s' "$input" | jq -r '.tool_input.old_string // ""' | awk 'END{print NR}')"
    new_lines="$(printf '%s' "$input" | jq -r '.tool_input.new_string // ""' | awk 'END{print NR}')"
    delta=$(( new_lines - old_lines ))
    [ $delta -lt 0 ] && delta=$(( -delta ))
    [ $delta -lt 1 ] && delta=1
    ;;
  Write)
    delta="$(printf '%s' "$input" | jq -r '.tool_input.content // ""' | awk 'END{print NR}')"
    [ -z "$delta" ] && delta=0
    ;;
  NotebookEdit)
    delta="$(printf '%s' "$input" | jq -r '.tool_input.new_source // ""' | awk 'END{print NR}')"
    [ -z "$delta" ] && delta=1
    ;;
  *)
    delta=1
    ;;
esac

now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Atomic read-modify-write so parallel tool calls don't corrupt state.
tmp="$state_file.tmp.$$"
if [ -f "$state_file" ]; then
  existing="$(cat "$state_file")"
else
  existing="$(jq -n --arg sid "$session_id" --arg now "$now" '{
    session_id: $sid,
    started_at: $now,
    files_touched: [],
    lines_changed: 0,
    new_files: [],
    deleted_files: [],
    rationale_path: null
  }')"
fi

new_file_flag="false"
if [ "$tool_name" = "Write" ] && [ ! -f "$file_path" ]; then
  new_file_flag="true"
fi

printf '%s' "$existing" | jq \
  --arg path "$file_path" \
  --argjson delta "$delta" \
  --argjson is_new "$new_file_flag" \
  '
  .files_touched = ((.files_touched + [$path]) | unique) |
  .lines_changed = (.lines_changed + $delta) |
  (if $is_new then .new_files = ((.new_files + [$path]) | unique) else . end)
  ' > "$tmp" && mv "$tmp" "$state_file"

exit 0
