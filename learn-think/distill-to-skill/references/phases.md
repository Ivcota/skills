# Phase details

Full prose for each phase. SKILL.md keeps the spine; this file holds gates, the one-run Workflow contract, direct-Agent fallback, and source-size logic.

## Phase 2: Source ingestion

Build a source manifest before extraction. For each source, record: `{type, location, access_method, coverage_estimate}`.

- Files: read the full text, chunk if needed, keep page/section pointers
- URLs: WebFetch; record URL + retrieval date
- Title-only: WebSearch for author/publisher pages, structured summaries, interviews, official talks/transcripts, and reviews that quote heavily. Prefer primary sources.
- Author grounding: add the author's official site, publisher page, or book jacket as a manifest entry for the bio and further-reading section. Do this even when the main source is a local PDF.

**Exit gate:** `./skills-draft/<slug>/sources.md` exists with at least one primary framework source, citation pointers, and an author/publisher source for biographical claims.

## One saved Workflow for Phases 3–6

After Intake and Ingest pass, invoke the saved Workflow once:

```text
Workflow({
  scriptPath: "${CLAUDE_SKILL_DIR}/workflows/distill.js",
  args: {
    skillDir: "<absolute active skill directory>",
    stagingDir: "<absolute staging directory>",
    estimatedSourceTokens: <number or omit>,
    sourceScope: "full source"
      OR { structure: "...", application: "...", guardrails: "..." },
    maxRevisionRounds: 3
  }
})
```

Do not pass `stage` or `sections`. The Workflow advances through Extract → Synthesize → Expand → Review/Revise in one run. It derives the canonical section list from synthesis and returns:

- `ready` — every phase completed, every rubric category passes, and the internal mechanical validation Agent confirmed the staged artifacts
- `blocked` — a prerequisite, worker, result contract, path, or rubric response failed; later phases did not run
- `needs-revision` — review is valid, but deficiencies remain after the revision cap

The result includes sections, generated files, counts, per-phase summaries, and blockers or unresolved targets. The main session remains responsible for interactive Intake/Ingest, re-running the final mechanical check independently, and emission.

If Workflow is unavailable or the user did not authorize multi-agent orchestration, use the direct-Agent fallback described under each phase. Both paths must produce identical artifacts and obey identical gates.

## Phase 3: Parallel extraction

Run exactly three independent jobs:

1. **Structure** — thesis + framework sections + end-to-end process
2. **Application** — copy patterns + case studies
3. **Guardrails** — common mistakes + ethical boundaries

The canonical job prompts and schemas live in [extraction-jobs.md](extraction-jobs.md).

### Saved Workflow behavior

The Workflow launches all three workers with `parallel()`. Each writes only its assigned artifact:

- `notes-structure.md`
- `notes-application.md`
- `notes-guardrails.md`

Null, malformed, wrong-path, or explicitly blocked results become first-class blockers. The Workflow does not synthesize from an incomplete extraction set.

### Portable fallback: direct Agent fan-out

Launch the three jobs from [extraction-jobs.md](extraction-jobs.md) as Agent calls in one message so they run concurrently. Give each cold-start prompt the staging path, source manifest, exact scope, output filename, citation rules, and token cap. Do not continue unless all three assigned files exist and are grounded.

### Shared source-size gate

Estimate source tokens before launching (rough: words × 1.3).

- ≤100k tokens → each worker may load the full source.
- >100k tokens → build a chapter map and pass explicit per-job scopes. Workers may not read outside scope.

Every worker must cap WebSearch at 3 verification reads, return/write ≤10k tokens of structured notes, and omit unsupported claims. Author bio, further reading, and trigger phrases belong to the single synthesis owner.

**Exit gate:** all three notes files exist, carry ≥1 citation per item, and stay under the 10k-token cap. Run `scripts/check.sh <staging-dir> --phase 3` when checking manually.

## Phase 4: Synthesis

### Saved Workflow behavior

One dedicated synthesis Agent owns the complete `SKILL.md`. It reads `description-brief.md`, `sources.md`, all three extraction files, [template.md](template.md), citation rules, and the rubric.

The synthesis Agent must:

- reconcile framework names using Structure as canonical;
- preserve the author's section order and actual section count;
- use the interviewed description rather than generating a replacement;
- keep SKILL.md at or below 100 lines;
- link every framework section plus `case-studies.md` and `checklist.md`;
- return the canonical ordered `[{name, slug}]` list.

The coordinator derives `references/<slug>.md` itself. It rejects duplicate names/slugs, non-kebab-case slugs, and collisions with `case-studies` or `checklist` before expansion starts.

### Portable fallback: main-session synthesis

Assemble SKILL.md in the main session using [template.md](template.md). Do not split this file across workers: one coherence owner must reconcile framework names, source ordering, frontmatter, and cross-section links. Read `description-brief.md`, `sources.md`, and all three extraction notes; use the manifest's author/publisher entry for the bio and further reading. If a section is thin, launch one targeted follow-up worker or drop it.

Ordering check: framework sections follow the author's sequence, not the model's preferred order.

**Exit gate:** SKILL.md exists, is ≤100 lines, and yields a safe unique section list. Run `scripts/check.sh <staging-dir> --phase 4` when checking manually.

## Phase 5: References fan-out

### Saved Workflow behavior

The Workflow internally builds this item list:

1. every validated framework section from synthesis;
2. `references/case-studies.md`;
3. `references/checklist.md`.

It runs each item through a two-stage `pipeline()`:

1. a focused drafting worker writes only its assigned file;
2. a verifier inspects and surgically fixes that same file.

Different items run concurrently; verification for one item begins as soon as its draft succeeds. A null, malformed, blocked, or wrong-path draft skips its verifier and blocks review. A failed verifier also blocks review.

### Portable fallback: direct Agent pipelines

Launch one Agent per framework section plus one for case studies and one for checklist. Each gets its section notes, `sources.md`, citation rules, review rubric, target path, and permission to WebSearch only for deeper verification. Target roughly 100–300 lines per framework reference. After each draft succeeds, verify that same file directly or with a focused follow-up Agent; never verify a missing draft.

Both paths must preserve source order and voice, cite every claim/example/pattern, and avoid invented contexts, values, or ethics.

**Exit gate:** every `references/*.md` link in SKILL.md resolves, and `references/case-studies.md` plus `references/checklist.md` exist. Run `scripts/check.sh <staging-dir> --phase 5` when checking manually.

## Phase 6: Review and surgical revision

### Saved Workflow behavior

The Workflow scores every canonical category exactly once. Category keys and targets are coordinator-owned; the reviewer does not decide `ship` or invent target values. Missing, duplicate, unknown, or malformed categories block the run instead of crashing or shipping.

For below-target categories, revision targets may include only final generated artifacts:

- `SKILL.md`
- validated `references/<section-slug>.md` files
- `references/case-studies.md`
- `references/checklist.md`

The coordinator rejects traversal, absolute paths outside staging, notes/source edits, and any file outside that allowlist. Targets sharing a file are merged so concurrent revision workers always have disjoint write scopes. After successful surgical revisions, the Workflow runs a fresh review. Revision rounds default to 3 and are capped at 5.

If every category passes, status is `ready`. If the cap is reached with valid unresolved deficiencies, status is `needs-revision`. Null or malformed reviews/revisions return `blocked`.

### Portable fallback: direct review

Self-score against [review-rubric.md](review-rubric.md). For each category below target, group issues by final output file, merge overlapping scopes, and launch focused revision Agents only for disjoint targets. Replace only deficient material and re-score after each round. Never modify source manifests or extraction notes to make the score appear better.

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

## Final mechanical validation

Before returning `ready`, the Workflow launches a read-only validation Agent that executes `scripts/check.sh <staging-dir>` and independently confirms that SKILL.md, every linked section reference, `case-studies.md`, and `checklist.md` exist. It must inspect the command result rather than trusting prior worker reports. A missing result, non-zero command, or absent required file returns `blocked` at the Validate phase.

The main session re-runs the same checker before emission so the final outward-facing move does not rely solely on a sub-agent's report.

## Phase 7: Emit

After the Workflow returns `ready`, run `scripts/check.sh <staging-dir>`. Then move from staging to the confirmed install location, such as `~/.claude/skills/<slug>/`, `~/.agents/skills/<slug>/`, or a project-local skills directory. Print:

- slug + path
- sources used
- section count + reference count
- rubric score

Do not emit on `blocked`. On `needs-revision`, resolve or explicitly surface the remaining targets before asking whether to emit.
