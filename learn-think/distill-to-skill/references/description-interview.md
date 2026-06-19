# Description interview

The `description:` frontmatter field is the *only* thing future agents see when deciding whether to load this skill. Auto-generating it from book keywords produces generic triggers that fire on the wrong conversations or miss the right ones. Always ask the user these questions before finalizing.

## The questions (ask one at a time)

### 1. Audience

> "Who is this skill primarily for? Examples: founders pricing their first SaaS, growth marketers designing campaigns, product managers writing specs, engineers reviewing architecture."

Use the answer to shape the first sentence of the description — the subject.

### 2. Trigger phrases

> "What phrases would you say in a conversation that should make this skill fire? Give me 3-5 you'd actually type."

Combine with the `triggers` extraction from Job 9 (direct + problem + artifact phrases). User-supplied triggers take priority — they reflect the user's real vocabulary.

### 3. Primary use case

> "When this skill fires, is the user most often (a) applying the framework to new work, (b) diagnosing existing work, (c) teaching / explaining, or (d) all of the above?"

Shapes the verb at the start of the description:
- **Apply** → "Create / design / build..."
- **Diagnose** → "Audit / review / score..."
- **Teach** → "Explain / map / frame..."
- **All** → "{Verb} and {verb}..."

### 4. (Optional) Cross-references

> "Any existing skills this one should point to as related? E.g., `For X, see other-skill-name.`"

Only ask if the user has other skills in their skills dir (`~/.claude/skills/`, `~/.agents/skills/`, or a project-local equivalent) that overlap.

## Writing the description

After the interview, draft the description in this shape:

```
{One sentence: verb + object + method name + signature concept.}
{Optional second sentence: what distinguishes this from adjacent skills.}
Use when the user mentions {direct phrase 1}, {direct phrase 2}, {direct phrase 3}, or {problem phrase}.
Also trigger when {artifact phrase 1}, {artifact phrase 2}, or {context phrase}.
{Optional: For X, see other-skill. For Y, see other-skill.}
```

## Constraints

- Max 1024 characters
- Third person ("the user mentions", not "you mention")
- First sentence is the *what*, not the *when*
- "Use when..." introduces triggers
- No emojis
- No time-sensitive language ("new framework", "modern approach")

## Review with the user

Show the drafted description and ask:

> "Here's the description — the only thing future agents see when deciding to load this skill. Any phrases missing? Anything here that would cause it to fire when you don't want it to?"

Iterate until the user signs off.
