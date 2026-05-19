# walkthrough

Claude Code bundle that forces a persisted, structured rationale for every non-trivial diff Claude writes. Lives as a markdown file in the repo, retrievable later via `/explain <file>:<line>`.

## Install

One-liner (works in any repo, no clone needed):

```bash
# This repo only (recommended for first try)
curl -fsSL https://raw.githubusercontent.com/Ivcota/skills/main/walkthrough/install.sh | bash -s -- --project

# Globally for every Claude session on this machine
curl -fsSL https://raw.githubusercontent.com/Ivcota/skills/main/walkthrough/install.sh | bash

# Remove (preserves rationale docs)
curl -fsSL https://raw.githubusercontent.com/Ivcota/skills/main/walkthrough/install.sh | bash -s -- --uninstall
```

Or, if you've cloned this repo:

```bash
bash walkthrough/install.sh --project    # this repo only
bash walkthrough/install.sh              # globally
bash walkthrough/install.sh --uninstall  # remove
```

Requires `jq` (and `curl` for the one-liner).

## What gets installed

Into `~/.claude/` (or `<repo>/.claude/` with `--project`):
- `skills/walkthrough/SKILL.md` — the `/walkthrough` slash command
- `skills/walkthrough/references/format.md` + `chunking.md` — output spec
- `skills/walkthrough/hooks/post-edit-track.sh` — PostToolUse session tracker
- `skills/walkthrough/hooks/stop-walkthrough-gate.sh` — Stop hook gate
- `commands/explain.md` — the `/explain` slash command
- Two entries merged into `settings.json` under `hooks.PostToolUse` (matcher `Edit|Write|NotebookEdit`) and `hooks.Stop`

Into the current repo:
- `.claude/rationale/` — committed; one markdown doc per session
- `.claude/session-state/` — gitignored; ephemeral
- `.claude/walkthrough.config.json` — thresholds and skip paths
- `CLAUDE.md` fragment appended once (paragraph telling Claude to keep a rationale ledger as it works)

## How it works

1. **PostToolUse hook** updates `.claude/session-state/<session_id>.json` after every Edit/Write/NotebookEdit — tracks files touched, lines changed, new/deleted file counts.
2. **Stop hook** fires when Claude tries to end the turn. It loads the state, applies the trivial-change rule (default: ≤2 files AND ≤50 lines AND no new files AND no deletions), and if the diff is non-trivial and no rationale exists for this session, exits with code 2 and a block message instructing Claude to produce a walkthrough following `references/format.md`.
3. **`/walkthrough` skill** runs against the session diff, writes `.claude/rationale/<date>-<slug>.md`, lists chunks as checkboxes, and waits for per-chunk acknowledgment.
4. **`/explain <file>[:<line>]`** greps all rationale docs for chunk headers matching the query and returns the bodies sorted newest-first.

## Configuration

Edit `.claude/walkthrough.config.json` in the repo:

```json
{
  "trivial_threshold": { "files": 2, "lines": 50 },
  "skip_paths": ["**/*.md", "**/*.lock", "**/package-lock.json"]
}
```

Files matching `skip_paths` are excluded from the trivial-rule counts.

## Non-goals

- Not a code-quality review.
- Not source-code comments.
- No telemetry, no network calls.

## Acceptance test

After install, manual test (cannot be automated — needs a live Claude session):

1. Make a 3-file change in a Claude session. Confirm Stop hook blocks and Claude produces a conforming rationale doc.
2. `/explain <file>:<line>` returns the matching chunk.
3. Make a 1-file, 5-line change. Confirm Stop hook does NOT block.
4. `bash install.sh --uninstall`. Confirm hooks removed, rationale docs preserved.
