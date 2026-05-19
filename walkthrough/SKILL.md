---
name: walkthrough
description: Produce a chunk-by-chunk rationale for the current session's diff and persist it to .claude/rationale/. Use after a non-trivial change, or invoked automatically by the Stop hook before the session ends. Pair with /explain to retrieve rationale by file/line later.
metadata:
  version: 1.0
---

# `/walkthrough`

Persisted, structured rationale for the diff Claude wrote this session. The rationale survives the session as a file in the repo so it can be defended in PR review today and recovered months from now via `/explain <file>:<line>`.

## When to invoke

- **Automatically** — the Stop hook invokes this skill before the session ends if the diff is non-trivial (>2 files OR >50 lines OR new files OR deletions; configurable in `.claude/walkthrough.config.json`).
- **Manually** — the user runs `/walkthrough` after a change. If no session state is available, fall back to `git diff` against `HEAD` or `git merge-base origin/main HEAD`.

## What to do when invoked

1. **Identify the diff.**
   - First try session state: `.claude/session-state/<session_id>.json` (or `~/.claude/session-state/...` if no project state dir).
   - If no state, run `git diff HEAD` (or against the merge base with the default branch).
   - Resolve repo-relative paths; drop any path matching `skip_paths` from the config.

2. **Group edits into chunks** per `references/chunking.md`. Each new file is its own chunk. Edits >10 lines apart or crossing function/class boundaries split; conceptually-related edits override mechanical splits.

3. **Produce the rationale doc** at `.claude/rationale/<YYYY-MM-DD>-<slug>.md` following `references/format.md` exactly:
   - Frontmatter with `task`, `session_id`, `created`, `files`, `chunks`.
   - 2-3 sentence summary.
   - One section per chunk with **What / Why this approach / Alternatives considered / Assumptions / Breakage test**.
   - Header format `## Chunk N — <path>:<start>-<end>` is load-bearing — `/explain` parses it as a regex.

4. **List chunks to the user with markdown checkboxes** and offer "explain more" per chunk:

   ```
   - [ ] Chunk 1 — src/webhook/handler.ts:42-58
   - [ ] Chunk 2 — src/middleware/idempotency.ts:1-34
   - [ ] Chunk 3 — migrations/20260519_stripe_event_log.sql:1-22
   ```

5. **Wait for per-chunk acknowledgment** before reporting the task done. The user marks each box; if they ask for more on a chunk, expand without rewriting the file.

## Slug rules

- First 4 words of the user's task message, lowercased, kebab-cased, non-alphanumerics stripped.
- Fall back to `manual-<HHMM>` (UTC) if no task message is derivable.
- If the file already exists, append `-2`, `-3`, etc.

## Voice & quality rules

See `references/format.md` — peer-engineer voice, specific over generic, honest about uncertainty. "Improves performance" is rejected; "avoids N+1 by batching user lookups in `user-service.ts:42`" is acceptable. "Alternatives considered" may be empty only if you write exactly `none — only one reasonable approach`. Never fabricate trade-offs.

## Non-goals

- Not a code-quality review. Capture *why* the diff exists, not *whether* it's good.
- Not source-code comments. Rationale lives in `.claude/rationale/`, joined by file/line. The diff stays clean.
- Not a replacement for thinking. This surfaces decisions; it doesn't make them.

## Related

- `/explain <file>[:<line>]` — retrieves chunks from prior walkthroughs for the queried path.
- `references/format.md` — exact output format.
- `references/chunking.md` — trivial-change and chunking rules.
