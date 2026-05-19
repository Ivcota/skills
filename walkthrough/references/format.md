# Rationale doc format

This is the exact format every `/walkthrough` output must follow. The Stop hook references this file when it tells Claude to produce a walkthrough.

## File location

`.claude/rationale/<YYYY-MM-DD>-<slug>.md`

- `<YYYY-MM-DD>` — UTC date the rationale was produced
- `<slug>` — kebab-case from the first 4 words of the user's task message; fall back to `manual-<HHMM>` (UTC) if no task is derivable

## Document shape

```markdown
---
task: <one-line task description>
session_id: <session uuid from the hook stdin>
created: <ISO 8601 UTC timestamp>
files:
  - <path>
  - <path>
chunks: <integer>
---

# <Task one-liner>

<2-3 sentence summary of what the change does and why.>

## Chunk 1 — <path>:<start>-<end>

**What:** <plain-language description of the change>

**Why this approach:** <reasoning — specific, not generic>

**Alternatives considered:**
- <alternative>: rejected because <reason>
- <alternative>: rejected because <reason>

**Assumptions:** <what must remain true for this code to be correct>

**Breakage test:** <path:line of a test that fails if the assumption breaks, or "none — add one">

---

## Chunk 2 — <path>:<start>-<end>

...
```

## Frontmatter rules

- `session_id` is required — `/explain` and the Stop hook both key off it to find the rationale for a given session.
- `files` lists every file that has at least one chunk. Order matches first appearance in the walkthrough.
- `chunks` is the integer count of `## Chunk N — ...` headers in the body.

## Chunk header format

Header is exactly: `## Chunk <N> — <path>:<start>-<end>`

- `<N>` is 1-indexed, sequential.
- `<path>` is repo-relative, no leading `./`.
- `<start>-<end>` is the inclusive line range in the **post-edit** file. Single-line changes use `<n>-<n>`.

`/explain` parses these headers with the regex `^## Chunk \d+ — (.+?):(\d+)-(\d+)$`. Deviating from this format will make chunks unretrievable.

## Required sections in each chunk

Every chunk must have **all five** sections in this order:

1. **What** — Plain-language description. State what the code now does, not what it used to do.
2. **Why this approach** — Specific to this code. "Improves performance" is rejected. "Avoids N+1 by batching the user lookups in `user-service.ts:42`" is acceptable.
3. **Alternatives considered** — Bulleted list. If no real alternatives existed, write exactly: `none — only one reasonable approach`. Don't fabricate trade-offs.
4. **Assumptions** — Things that could change and break this code (API behavior, schema invariants, library version, env shape). Tautologies ("the input is valid") don't count.
5. **Breakage test** — `<path>:<line>` of an existing test that fails if an assumption breaks. If none exists, write `none — add one` and consider adding it before merging.

## Length

- Chunk body ≤ 200 words.
- If a chunk needs more, split it into sub-chunks with the same header format (different line ranges).

## Voice

- Peer-engineer voice. No marketing language. No "I've carefully considered..."
- Specific over general. Cite line numbers, library names, doc URLs.
- Honest about uncertainty. "I picked this because the other options also work and this seemed clean" is acceptable — better than fabricating a trade-off.
- If `CLAUDE.md` establishes a project voice, match it.

## After writing

The skill must:

1. List each chunk to the user with a markdown checkbox (`- [ ] Chunk 1 — <path>:<lines>`).
2. Offer "explain more" per chunk.
3. Wait for the user to acknowledge each chunk before reporting the task done.
