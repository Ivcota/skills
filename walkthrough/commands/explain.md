---
name: explain
description: Retrieve rationale chunks from prior /walkthrough output. Invoke as /explain <file>[:<line>] to surface why a piece of code was written the way it was.
argument-hint: <file>[:<line>]
---

# `/explain <file>[:<line>]`

Retrieve the rationale Claude recorded for a piece of code in a prior session.

## Behavior

1. **Parse the argument.** Accept `<file>` or `<file>:<line>`. Normalize `<file>` to repo-relative (strip leading `./` or absolute prefix that matches the repo root).

2. **Scan `.claude/rationale/*.md`.** For each file, walk chunk headers matching the regex:

   ```
   ^## Chunk \d+ — (.+?):(\d+)-(\d+)( \(deleted\))?$
   ```

   A chunk matches the query when:
   - Captured path equals the queried `<file>`, AND
   - If `<line>` was provided, `start ≤ line ≤ end`. Otherwise any line range counts.

3. **Collect matching chunks.** For each match, capture the chunk body up to the next `## Chunk` or end-of-file. Also capture the parent doc's frontmatter `created:` date and `task:` line.

4. **Sort by recency.** Newest rationale doc first (by frontmatter `created`).

5. **Render.** For each matching chunk:

   ```
   ## <task> — <created date>
   Source: .claude/rationale/<filename>

   <full chunk body, including What / Why / Alternatives / Assumptions / Breakage test>

   ---
   ```

6. **If no match:** say so and suggest the user run `/walkthrough` retroactively against the current diff to document the area.

## Examples

- `/explain src/webhook/handler.ts` — every chunk in every rationale doc that touches `handler.ts`.
- `/explain src/webhook/handler.ts:50` — only chunks whose line range covers line 50.

## Implementation notes

- The header format is the API. If a rationale doc deviates from `## Chunk N — <path>:<start>-<end>`, its chunks are unretrievable. The `/walkthrough` skill enforces the format.
- Don't paraphrase or summarize the chunk body. Return it verbatim so the user can see exactly what was recorded at decision time.
- Don't invent rationale when none exists. If `/explain` finds nothing, say so.
