# Phase details

Full prose for each phase. SKILL.md keeps the spine; this file holds gates, Workflow inputs, direct-Agent fallbacks, and source-size logic.

## Phase 2: Source ingestion

Build a source manifest before extraction. For each source, record: `{type, location, access_method, coverage_estimate}`.

- Files: read the full text, chunk if needed, keep page/section pointers
- URLs: WebFetch; record URL + retrieval date
- Title-only: WebSearch for author/publisher pages, structured summaries, interviews, official talks/transcripts, and reviews that quote heavily. Prefer primary sources.

**Exit gate:** `./skills-draft/<slug>/sources.md` exists with at least one primary source and citation pointers.

## Phase 3: Parallel extraction

Run exactly three independent jobs:

1. **Structure** — thesis + framework sections + end-to-end process
2. **Application** — copy patterns + case studies
3. **Guardrails** — common mistakes + ethical boundaries

The canonical job prompts and schemas live in [extraction-jobs.md](extraction-jobs.md).

### Preferred: saved Workflow

When the Workflow tool is available and the user authorized workflow/multi-agent orchestration, invoke:

```text
Workflow({
  scriptPath: "${CLAUDE_SKILL_DIR}/workflows/distill.js",
  args: {
    stage: "extract",
    skillDir: "<absolute active skill directory>",
    stagingDir: "<absolute staging directory>",
    estimatedSourceTokens: <number or omit>,
    sourceScope: "full source"
      OR { structure: "...", application: "...", guardrails: "..." }
  }
})
```

The Workflow launches all three workers with `parallel()`. Each writes only its assigned artifact:

- `notes-structure.md`
- `notes-application.md`
- `notes-guardrails.md`

### Portable fallback: direct Agent fan-out

If Workflow is absent or not authorized, launch the three jobs from [extraction-jobs.md](extraction-jobs.md) as Agent calls in one message so they run concurrently. Give each cold-start prompt the staging path, source manifest, exact scope, output filename, citation rules, and token cap.

### Shared source-size gate

Estimate source tokens before launching (rough: words × 1.3).

- ≤100k tokens → each worker may load the full source.
- >100k tokens → the main thread builds a chapter map and passes explicit per-job scopes. Workers may not read outside scope.

Every worker must cap WebSearch at 3 verification reads, return/write ≤10k tokens of structured notes, and omit unsupported claims. Author bio, further reading, and trigger phrases remain main-thread tasks.

**Exit gate:** all three notes files exist, carry ≥1 citation per item, and stay under the 10k-token cap. Run `scripts/check.sh <staging-dir> --phase 3`.

## Phase 4: Synthesis

Assemble SKILL.md in the main thread using [template.md](template.md). Do not delegate synthesis: the main thread owns framework-name reconciliation, source ordering, and cross-section coherence. Pull only from extraction notes. If a section is thin, launch one targeted follow-up worker or drop it.

Ordering check: framework sections follow the author's sequence, not the model's preferred order.

**Exit gate:** SKILL.md exists and is ≤100 lines. Run `scripts/check.sh <staging-dir> --phase 4`.

## Phase 5: References fan-out

First ensure `<staging-dir>/references/` exists. Build the canonical section list from synthesized SKILL.md:

```text
sections: [{ name: "Author's section name", slug: "safe-lowercase-slug" }, ...]
```

### Preferred: saved Workflow

Invoke `workflows/distill.js` with `stage: "expand"`, absolute `skillDir`/`stagingDir`, and `sections`. The Workflow pipelines each framework section, `case-studies.md`, and `checklist.md` through:

1. a focused drafting worker that writes only its assigned file;
2. a verifier that inspects and surgically fixes that same file.

Different items run concurrently; verification for an item begins as soon as its draft finishes.

### Portable fallback: direct Agent fan-out

Launch one Agent per framework section plus one for `case-studies.md` and one for `checklist.md`. Each gets its section notes, `sources.md`, citation rules, review rubric, target path, and permission to WebSearch only for deeper verification. Target roughly 100–300 lines per framework reference. After drafting, verify each file directly or with a focused follow-up Agent.

Both paths must preserve source order and voice, cite every claim/example/pattern, and avoid invented contexts, values, or ethics.

**Exit gate:** every `references/*.md` link in SKILL.md resolves, and `references/case-studies.md` plus `references/checklist.md` exist. Run `scripts/check.sh <staging-dir> --phase 5`.

## Phase 6: Review and surgical revision

### Preferred: saved Workflow

Invoke:

```text
Workflow({
  scriptPath: "${CLAUDE_SKILL_DIR}/workflows/distill.js",
  args: {
    stage: "review",
    skillDir: "<absolute active skill directory>",
    stagingDir: "<absolute staging directory>",
    maxRevisionRounds: 3
  }
})
```

The Workflow uses structured rubric output, groups deficiencies by target file/section, pipelines non-overlapping surgical revisions, and re-scores after each round. It never regenerates the whole skill. Revision rounds are capped at 5; if unresolved targets remain, the Workflow returns them explicitly for main-thread resolution.

### Portable fallback: direct review

Self-score against [review-rubric.md](review-rubric.md). For each category below target, launch a focused revision Agent with the affected files, original extraction instructions, and exact deficiency. Replace only deficient material and re-score only the affected category.

Minimum ship bar:

- [ ] Description includes `Use when...` with specific trigger phrases
- [ ] SKILL.md ≤100 lines
- [ ] Every framework reference has all sourced required elements
- [ ] Every claim traces to `sources.md`
- [ ] No invented numbers, statistics, contexts, or outcomes
- [ ] Application and common-mistakes tables meet sourced depth targets
- [ ] Further reading and author bio are grounded
- [ ] `case-studies.md` and `checklist.md` exist

**Exit gate:** every rubric category meets its target; hard rules score 10.

## Phase 7: Emit

Move from staging to the confirmed install location, such as `~/.claude/skills/<slug>/`, `~/.agents/skills/<slug>/`, or a project-local skills directory. Print:

- slug + path
- sources used
- section count + reference count
- rubric score
