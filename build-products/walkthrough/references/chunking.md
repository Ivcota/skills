# Trivial-change & chunking rules

Used by the Stop hook gate and by the `/walkthrough` skill when grouping edits.

## Trivial-change rule

The Stop hook skips the walkthrough gate **only if all four** are true:

- Files touched ≤ `trivial_threshold.files` (default 2)
- Lines changed ≤ `trivial_threshold.lines` (default 50)
- No new files created
- No deletions of existing files

Thresholds are overridable per-repo via `.claude/walkthrough.config.json`:

```json
{
  "trivial_threshold": { "files": 2, "lines": 50 },
  "skip_paths": ["**/*.md", "**/*.lock", "**/package-lock.json"]
}
```

`skip_paths` are excluded from both the file count and the line count before applying the trivial rule. Patterns are glob-style, matched against the repo-relative path.

If the config file is missing or malformed, defaults apply and the hook logs a warning to stderr but does not block.

## Chunking rules

How `/walkthrough` groups edits into chunks in the rationale doc:

1. **Each new file = one chunk.** Even if the file is small.
2. **Contiguous edits within a single hunk** (≤10 lines apart in the same file) = one chunk.
3. **Edits separated by >10 lines** OR by a different function/class boundary = separate chunks.
4. **Conceptual grouping overrides mechanical rules.** If two edits sit far apart but implement the same idea (e.g., adding a flag at the top of the file and reading it 200 lines later), chunk them together and use the line-range header `<min>-<max>`.

## Line-range header

The header `## Chunk N — <path>:<start>-<end>` uses post-edit line numbers in the file as it sits after the change. For deletions-only chunks where the post-edit lines don't exist, use the line numbers from the **pre-edit** file and add `(deleted)` after the path: `## Chunk N — src/old.ts:42-58 (deleted)`.

## File path normalization

- Always repo-relative, no leading `./` or `/`.
- Forward slashes on all platforms.
- Lowercase as written in the filesystem (don't normalize case).
