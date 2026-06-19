# `/walkthrough` — Build Requirements

Hand this whole doc to the build agent. It's self-contained.

---

## 1. Overview

`/walkthrough` is a Claude Code extension bundle (skill + hooks + slash commands) that makes Claude produce a persisted, structured rationale for every non-trivial diff it writes. The rationale survives the session as a file in the repo, can be auto-posted as a PR comment, and is retrievable later via `claude explain <file>:<line>`.

It exists because stock Claude explains itself in chat, chat dies with the session, and engineers can't defend in PR review or debug at 2am three months later. `/walkthrough` fixes the persistence and retrievability gap.

## 2. User & job

Primary user: senior software engineer using Claude Code on production code that will be reviewed by humans.

Job-to-be-done: *"When I accept a non-trivial diff from Claude, I want a rationale I can defend in PR review today and recover when the code breaks months from now."*

The user must be able to:
- Trust that the rationale exists and is honest, without remembering to invoke a command
- Review the rationale per-chunk, not as a wall of text
- Surface chunks they don't yet understand and drill in
- Retrieve the rationale months later, scoped to a file/line

## 3. Goals (measurable)

| Goal | Target |
|---|---|
| Every non-trivial Claude session produces a rationale doc | 100% (forced by hook) |
| Rationale captures alternatives considered | Required for every non-trivial chunk |
| Engineer marks each chunk reviewed before "done" | Forcing function via Stop hook |
| Rationale persists in repo | File written to `.claude/rationale/` |
| Retrievable later by file/line | `claude explain <file>:<line>` returns rationale |
| Installation in a new repo | One command, idempotent |
| Trivial changes skip the ceremony | Auto-skip below threshold |

## 4. Non-goals

- **No source-code comments.** Rationale lives in separate files, joined by file/line. Diff stays clean.
- **No code quality review.** This captures *why* the diff exists, not *whether* it's good.
- **No new model capability required.** Built entirely on existing Claude Code extension paths.
- **No platform-level changes.** Cannot modify Claude Code's defaults for users who don't install this bundle.
- **No replacement for thinking.** Surfaces decisions; doesn't make them.
- **No telemetry, no network calls beyond optional PR-comment posting.**

## 5. Architecture

Five components, all using approved Claude Code extension paths:

```
┌─────────────────────────────────────────────────────────┐
│  Claude session                                          │
│  ┌─────────────┐   edit/write   ┌──────────────────┐    │
│  │ Claude      │ ─────────────► │ PostToolUse hook │    │
│  │ (planning + │                │ updates session  │    │
│  │  executing) │                │ state            │    │
│  └─────────────┘                └──────────────────┘    │
│         │                                ▼              │
│         │ Stop                  .claude/session-state/   │
│         ▼                                                │
│  ┌─────────────────┐                                    │
│  │ Stop hook       │ ── if non-trivial & no walkthrough ─►│
│  │ walkthrough     │      block; ask Claude to produce   │
│  │ gate            │      walkthrough per format spec    │
│  └─────────────────┘                                    │
│                                                          │
│  /walkthrough skill ─── manual invoke / format spec     │
│  /explain command   ─── retrieval                        │
│  CLAUDE.md fragment ─── plan-time rationale capture     │
└─────────────────────────────────────────────────────────┘
```

## 6. Component requirements

### 6.1 `/walkthrough` skill (manual invoke + format spec)

**Location:** `skills/walkthrough/SKILL.md`

**Frontmatter:**
```yaml
---
name: walkthrough
description: Produce a chunk-by-chunk rationale for the current session's diff and persist it to .claude/rationale/. Use after a non-trivial change, or invoked automatically by the Stop hook.
---
```

**Behavior when invoked:**
1. Identify all edits in the current session (read from session state, or `git diff` if session state unavailable).
2. Group edits into logical chunks (see §6.6 for chunking rules).
3. For each chunk, produce a rationale entry per the format in §7.1.
4. Write the full walkthrough to `.claude/rationale/<YYYY-MM-DD>-<slug>.md`.
5. Print a chunk list to the user with checkboxes (markdown-style) and offer "explain more" per chunk.
6. Wait for user to acknowledge each chunk before reporting done.

**Manual invocation:** `/walkthrough` — runs against current uncommitted diff if no session state exists.

### 6.2 Stop hook — walkthrough gate

**Location:** `skills/walkthrough/hooks/stop-walkthrough-gate.sh`

**Wired into:** `~/.claude/settings.json` under `hooks.Stop`.

**Input:** JSON via stdin from Claude Code with session metadata (session_id, transcript path).

**Behavior:**
1. Read session state from `.claude/session-state/<session_id>.json`.
2. If session is **trivial** (see §6.6 trivial-change rule), exit 0. No walkthrough needed.
3. If non-trivial AND `.claude/rationale/<task>.md` exists for this session, exit 0.
4. If non-trivial AND no rationale exists yet, exit with non-zero code and JSON output instructing Claude:
   > "Before stopping, produce a walkthrough using the format in `skills/walkthrough/references/format.md`. Write it to `.claude/rationale/<date>-<slug>.md`. Then list each chunk to the user with a checkbox and ask them to mark each reviewed. Do not report done until the user has acknowledged all chunks."
5. Hook must be idempotent and side-effect-free except for reading state.

**Exit codes & output:** Conform to Claude Code's hook API — non-zero exit + structured stderr JSON to feed feedback back to Claude. (Verify exact format against current Claude Code hook docs at build time.)

### 6.3 PostToolUse hook — session state tracker

**Location:** `skills/walkthrough/hooks/post-edit-track.sh`

**Wired into:** `~/.claude/settings.json` under `hooks.PostToolUse` matching `Edit|Write|NotebookEdit`.

**Input:** JSON via stdin including session_id and the tool call details.

**Behavior:**
1. Read or create `.claude/session-state/<session_id>.json`.
2. Append the affected file path to a `files_touched` set.
3. Update `lines_changed` counter (best-effort line count from the tool input).
4. Exit 0 always — this hook never blocks.

**State file shape:**
```json
{
  "session_id": "...",
  "started_at": "2026-05-19T10:14:00Z",
  "files_touched": ["src/webhook/handler.ts", "..."],
  "lines_changed": 184,
  "rationale_path": null
}
```

### 6.4 `/explain` slash command

**Location:** `skills/walkthrough/SKILL.md` references it, or separate `skills/explain/SKILL.md`.

**Invocation:** `/explain <file>:<line>` or `/explain <file>` (returns all rationale touching the file).

**Behavior:**
1. Grep all files in `.claude/rationale/*.md` for chunks whose file/line range covers the query.
2. Return the matching chunk(s) — full rationale body, including alternatives and assumptions.
3. If no match, say so and suggest the user run `/walkthrough` retroactively.
4. Sort results by recency (newest rationale first) if multiple match.

### 6.5 CLAUDE.md fragment

**Location:** `skills/walkthrough/CLAUDE-fragment.md`

**Content:** A paragraph to be appended to project CLAUDE.md by the installer:

> When planning a non-trivial change (≥3 files OR ≥50 lines), maintain a rationale ledger as you go. For each logical chunk you intend to write, record: what the chunk does, why this approach, what alternatives you considered and rejected (with reasons), and what assumptions the chunk depends on. Capture rationale at decision time, not reconstructed at the end. This ledger becomes the source for `/walkthrough` when the session completes.

### 6.6 Chunking & trivial-change rules

**Trivial-change rule** (Stop hook skips walkthrough if all true):
- Files touched ≤ 2 AND
- Lines changed ≤ 50 AND
- No new files created AND
- No deletions of existing files

Configurable via `.claude/walkthrough.config.json`:
```json
{
  "trivial_threshold": { "files": 2, "lines": 50 },
  "skip_paths": ["**/*.md", "**/*.lock", "**/package-lock.json"]
}
```

**Chunking rules** (how Claude groups edits into walkthrough chunks):
- Each new file = one chunk
- Contiguous edits within a single hunk (≤10 lines apart) = one chunk
- Edits separated by >10 lines or by a different function/class boundary = separate chunks
- Logical groupings can override mechanical rules — Claude should chunk by *what changed conceptually*, not by hunk geometry, when the two diverge

## 7. File formats

### 7.1 Rationale doc — `.claude/rationale/<date>-<slug>.md`

```markdown
---
task: <one-line task description>
session_id: <session uuid>
created: 2026-05-19T10:42:00Z
files:
  - src/webhook/handler.ts
  - src/middleware/idempotency.ts
  - migrations/20260519_stripe_event_log.sql
  - tests/webhook.test.ts
chunks: 6
---

# <Task one-liner>

<2-3 sentence summary of what the change does and why.>

## Chunk 1 — src/webhook/handler.ts:42-58

**What:** <plain-language description of the change>

**Why this approach:** <reasoning — specific, not generic>

**Alternatives considered:**
- <alternative>: rejected because <reason>
- <alternative>: rejected because <reason>

**Assumptions:** <what must remain true for this code to be correct>

**Breakage test:** <path:line of a test that fails if the assumption breaks, or "none — add one">

---

## Chunk 2 — ...
```

Rules for chunk entries:
- Every section is required except "Alternatives considered" which may be empty if no real alternatives existed (must say "none — only one reasonable approach" explicitly).
- "Why" must be **specific to this code, not generic.** "Improves performance" is rejected; "avoids N+1 by batching the user lookups in the loop at user-service.ts:42" is acceptable.
- "Assumptions" must name things that could change (Stripe API behavior, library version, schema invariants), not tautologies.
- Maximum chunk body: ~200 words. If longer, split into sub-chunks.

### 7.2 Session state — `.claude/session-state/<session_id>.json`

See §6.3.

### 7.3 Config — `.claude/walkthrough.config.json`

See §6.6.

## 8. Installation

**Entry point:** `build-products/walkthrough/install.sh`

**Idempotent. Must:**
1. Copy `skills/walkthrough/` into `~/.claude/skills/walkthrough/` (or honor a `--project` flag to install into `<repo>/.claude/skills/`).
2. Merge hook entries into `~/.claude/settings.json` (or `<repo>/.claude/settings.json` with `--project`) without clobbering existing hooks. Use a JSON-aware merge, not text concatenation.
3. Create `.claude/rationale/` and `.claude/session-state/` in the target repo. Add both to `.gitignore` exclusions if needed — actually, `.claude/rationale/` **should be committed**; `.claude/session-state/` should not.
4. Append the CLAUDE.md fragment to the project's `CLAUDE.md` if not already present (detect by a marker comment).
5. Print a one-screen confirmation of what was installed and what was modified.

**Uninstall:** `install.sh --uninstall` removes the hook entries from settings.json and the skill files. Leaves rationale docs (user's data).

## 9. Acceptance criteria

The build is done when this end-to-end demo works:

1. Fresh repo with no prior installation. Run `bash install.sh --project`. Confirm settings.json, CLAUDE.md, and `.claude/` directories are updated correctly.
2. Start a Claude session. Ask Claude to make a non-trivial change (touch ≥3 files). Observe:
   - PostToolUse hook updates session state on each edit
   - When Claude tries to report done, Stop hook blocks
   - Claude produces a walkthrough conforming to §7.1
   - Walkthrough is written to `.claude/rationale/<date>-<slug>.md`
   - Claude lists chunks and asks user to acknowledge each
3. After acceptance, run `/explain src/webhook/handler.ts:50`. Confirm the relevant chunk rationale is returned.
4. Start a new Claude session in the same repo and make a trivial change (1 file, 5 lines). Confirm Stop hook does NOT block and no walkthrough is produced.
5. Run `bash install.sh --uninstall`. Confirm hooks are removed and skills cleaned up. Confirm rationale docs are preserved.

## 10. Constraints & assumptions about Claude Code

The build agent must verify these against current Claude Code docs before relying on them:

- Hook events available: `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, `UserPromptSubmit` — confirm the Stop hook is the right event for "before reporting done."
- Hook input format: JSON via stdin, session_id included.
- Hook block mechanism: non-zero exit + stderr JSON message gets fed to Claude as instruction.
- Skills live in `~/.claude/skills/<name>/SKILL.md` with YAML frontmatter.
- Settings file: `~/.claude/settings.json` (global) or `<repo>/.claude/settings.json` (project).
- Tool names for edit detection: `Edit`, `Write`, `NotebookEdit` — confirm at build time.

If any of these don't match current Claude Code behavior, prefer the actual API over what's written here.

## 11. Out of scope (future versions)

- Reviewer subagent that quality-gates the walkthrough before acceptance
- GitHub MCP integration to auto-post walkthroughs as PR comments
- Cross-session rationale search index
- Walkthrough diffing (when the same code is edited twice, show how rationale evolved)
- Integration with editor UIs to show rationale inline on hover

## 12. Tone & style for output Claude produces

When Claude writes walkthroughs:
- Peer-engineer voice. No marketing language, no "I've carefully considered..."
- Specific over general. Cite line numbers, library names, doc URLs when relevant.
- Honest about uncertainty. If the rationale is "I picked this because the other options also work and this seemed clean," say that — don't fabricate trade-offs.
- Match project's existing technical voice if CLAUDE.md establishes one.

---

## 13. Suggested build order

1. **Format spec + manual `/walkthrough` skill** (no hooks yet). Test by manually invoking on a real diff. Iterate on the format until rationale quality is good.
2. **PostToolUse session-state hook.** Test that it accurately tracks files/lines.
3. **Stop hook with trivial-change gate.** Test that it blocks correctly and that Claude obeys the feedback message.
4. **`/explain` retrieval command.** Test on accumulated rationale docs.
5. **CLAUDE.md fragment.** Test that plan-time rationale capture improves walkthrough quality.
6. **`install.sh`.** Last — once everything works manually, automate the wiring.
7. **End-to-end acceptance test** per §9.

Ship the bundle after step 7 passes. Defer §11 items to V2.
