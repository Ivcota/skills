# Intake

## Input detection

Accepts one or more of:
- **File** — PDF, epub, markdown, txt (any path the Read tool can open; PDFs ≤20 pages per call, chunk longer books)
- **URL** — article, blog post, transcript, publisher page
- **Title + author** — triggers web research (WebSearch → WebFetch)
- **Pasted text** — inline method description

If only a title is given, confirm with the user before spending tokens on research: "I'll search for {title} by {author} — anything specific to prioritize (chapters, concepts)?"

## Modes

- **strict** (default) — paraphrase closely; cite aggressively; drop un-citable content
- **liberal** — rewrite in template voice; still cite but allow synthesis (tables, copy patterns) inferred from quoted material

Ask the user which mode only if ambiguous.

## Output location

Detect which skill directories exist on the user's system and offer them as targets. Common locations:
- `~/.claude/skills/<slug>/` — Claude Code user-scoped skills
- `~/.agents/skills/<slug>/` — generic agent skills (any compatible harness)
- `./skills-draft/<slug>/` — local staging dir (review before installing)
- A project-local `.claude/skills/` or `.agents/skills/` if one exists in the cwd

Ask before writing: "Write to {detected-paths} or stage at `./skills-draft/<slug>/` first?" Slug = kebab-case of 3-5 significant words from the book/method title.

## Phase 1 checklist

1. Detect input type. If only title: propose a research plan and confirm.
2. Ask the 2–3 [description-interview](description-interview.md) questions — audience, trigger phrases, primary use case. These drive the frontmatter `description:` (the only thing future agents see).
3. Pick mode (strict / liberal). Pick output location.
4. Derive slug. Create staging dir.

**Exit gate:** slug chosen, mode chosen, output location chosen, description brief written.
