# Citation rules

The single rule that makes this skill useful: **no claim ships without a source.** If you can't point to where it came from, it doesn't go in the output.

## What counts as a source

Ranked, highest trust first:

1. **Primary text** — the book / paper / original post, quoted with page or section number.
2. **Author-authored secondary** — author's own talks, interviews, blog posts, course pages (still the author's words).
3. **High-fidelity summaries** — Blinkist, Shortform, Farnam Street, Derek Sivers notes, published book reviews that quote the text. Treat as pointers back to primary, not as the source of record.
4. **Community summaries** — Wikipedia, HN threads, Reddit discussions. Only usable to triangulate, never as the sole source for a claim.

Model memory ("I recall the book says…") is **not** a source. If that's all you have, search before you write.

## Citation format

Inline in extraction notes:

```
- Claim: {one-line restatement of the author's claim}
  Source: {Book Title}, Ch. "{Chapter Name}", p. {page}
  Quote: "{verbatim sentence from the source}"
```

For URLs, include retrieval date:

```
- Claim: Cold email open rates have dropped below X% post-2024
  Source: https://example.com/report (retrieved 2026-04-16)
  Quote: "..."
```

Citations don't need to appear in the final SKILL.md text — they live in `sources.md` and the extraction notes. But every bullet in the final skill should be traceable back to one.

## When the source isn't in front of you

Order of operations:

1. Ask: "Do you have a PDF / link / excerpt I should work from?"
2. If no: WebSearch for the specific concept + author name. Prefer quoted passages.
3. WebFetch the top 2–3 pages. Record URL + date.
4. If web doesn't confirm after reasonable effort (~3 queries): **drop the claim.** Do not fill from memory.

## Tables and copy patterns

Product-application tables and copy-pattern lists are the highest risk for invention because they feel like "just examples." Rules:

- **Application rows** — each row must come from a case study, example, or passage in the source. If the source doesn't cover SaaS, the SaaS row is omitted (or marked as "inferred, unverified" and left for user review).
- **Copy patterns** — must be sentence templates the author actually uses. You can generalize (`[Avatar]`, `[Outcome]`) but the underlying structure must appear in the text.
- **Dollar values** — only include if the source states them. Never invent "$X value" for a bonus.

## Statistics and outcomes

Any numeric claim (conversion rates, response rates, growth percentages, timelines) needs a direct quote in the note. If the source says "most of our clients," the skill says "most clients" — not "87% of clients."

## Author bio and further reading

Same rule. Pull the bio from the author's own about page, publisher bio, or book jacket — not model memory. Verify the ISBN and Amazon link by WebFetch before including.

## When strict mode disagrees with liberal mode

In liberal mode, you may *synthesize* new phrasing in the template voice, but the underlying claim must still be sourced. Liberal means "rewrite," not "invent."

## Red flags during review

If you notice any of these while writing, stop and re-check:

- A bullet you can't match to a citation
- A table row that "sounds right" but you don't remember where it came from
- A copy pattern that's generic marketing advice, not specific to the author
- A statistic with no quote backing it
- An ethical-boundary paragraph that sounds like generic ethics, not the author's own guardrails
