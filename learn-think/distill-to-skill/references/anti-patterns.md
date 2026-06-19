# Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Letting the model fill gaps from training data | Produces plausible-but-ungrounded skills; erodes trust in the output | Hard rule: no citation, no content |
| Single monolithic extraction pass | Misses structure; synthesis and extraction fight each other | Separate extract → synthesize phases |
| Auto-generating the description without user input | Triggers are the single most important field; hardest to guess | Always run the description interview |
| Inventing numeric values in application tables | Faking values the source never stated is deceptive | Only include values the source states; otherwise leave qualitative |
| Forcing a fixed section count | Some sources have 4 pillars, others 8 — padding to a target invents content | Match the source's actual structure |
| Skipping the staging dir | Bad output pollutes the live skills dir and starts firing on triggers | Stage, review, then move |
| SKILL.md over 100 lines | Future agents load it on every invocation; bloat costs tokens and obscures the spine | Push framework section detail into `references/<section>.md`; SKILL.md is a navigator |
| Putting full framework sections inside SKILL.md | Each section's tables + insights blow past the 100-line cap | One-line-per-section index in SKILL.md, full section in `references/<slug>.md` |
