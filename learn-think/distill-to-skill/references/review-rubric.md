# Review rubric

Self-score the generated skill on each category 0–10. Any category <8 triggers a revision pass. Minimum ship bar: every category ≥8, hard-rule categories = 10.

## Hard rules (must be 10 or do not ship)

### Citation coverage
- 10: every bullet, table row, and copy pattern traces to an entry in `sources.md`
- <10: anything unsourced. Fix: drop or re-extract.

### No invention of numbers
- 10: every dollar value, percentage, timeline, and statistic is a direct quote
- <10: any invented number. Fix: strip or replace with qualitative language.

### Author bio grounded
- 10: bio cites the author's own site, publisher page, or book jacket
- <10: any biographical detail not confirmed by a source. Fix: re-fetch.

## Graded categories

### Description quality (target 9+)
- Audience is specific
- 3+ direct trigger phrases from the user interview
- 2+ problem phrases
- 1+ artifact/context phrase
- Under 1024 chars
- Third person, no time-sensitive language

### Structural fidelity (target 9+)
- Frontmatter matches template exactly
- Core Principle present
- Scoring section present if source has one, absent if not
- Section count matches source's actual structure
- Every framework section has all 6 required sub-elements (Core concept, Why it works, Key insights, Applications, Copy patterns, Ethical boundary *if sourced*, Reference link)
- Process, Common Mistakes, Quick Diagnostic, Reference Files, Further Reading, About the Author all present

### Depth of framework sections (target 8+)
- 5-7 key insights per section
- Application table has 3+ rows drawn from sourced contexts
- 4-6 copy patterns per section

### Reference-file completeness (target 8+)
- Every framework section has a matching `references/<slug>.md`
- `references/case-studies.md` exists with examples from source
- `references/checklist.md` exists with actionable steps
- Reference files are 100-300 lines each

### Common mistakes & diagnostic (target 8+)
- ≥5 rows in common mistakes, each sourced
- Diagnostic questions map 1:1 to framework sections where possible
- Fixes are actionable, not vague

### Voice match (target 8+)
- Tone matches the source — if the author is blunt, the skill is blunt
- No generic marketing-speak unless the author uses it
- Author's distinctive phrases preserved

### Ethical boundaries (target 8+, or exempt)
- Where the source has explicit guardrails, they appear in the relevant section
- No invented or generic ethics paragraphs
- Exempt if the source has zero ethical framing (rare)

## Revision protocol

The one-run Workflow owns review after extraction, synthesis, and expansion. It scores these canonical keys exactly once: `citation_coverage`, `no_invented_numbers`, `author_bio_grounded`, `description_quality`, `structural_fidelity`, `framework_depth`, `reference_completeness`, `mistakes_and_diagnostic`, `voice_match`, and `ethical_boundaries`. Targets come from the coordinator, not the reviewer, and the coordinator computes ship readiness.

When a category scores <target:

1. Identify which final output file(s) or section(s) pulled the score down.
2. Group all deficiencies that touch the same target so parallel workers never edit the same file.
3. Allow revisions only in `SKILL.md` and the generated `references/*.md` files; never revise sources or extraction notes to improve the score.
4. In direct-Agent fallback mode, spawn a targeted Agent with the canonical extraction prompt plus the specific deficiency ("the copy patterns don't match the source's voice — re-extract with tighter quoting").
5. Replace only the deficient material, then run a fresh score pass.

Do not regenerate the whole skill. Workflow and fallback paths both use surgical fixes.

## Review output

After scoring, print to the user:

```
Review for {slug}:
  Citation coverage: 10/10 ✓
  No invention of numbers: 10/10 ✓
  Author bio grounded: 10/10 ✓
  Description quality: 9/10
  Structural fidelity: 10/10
  Depth of sections: 8/10
  Reference files: 9/10
  Common mistakes & diagnostic: 8/10
  Voice match: 9/10
  Ethical boundaries: 8/10

  Status: ready to ship
  Path: {chosen install dir}/{slug}/
  Sources used: {count}
  Sections: {count}
  References: {count}
```
