# Surface-Level Improvements

Reference for chapters 2–6 of *The Art of Readable Code*. These are the line-by-line moves that pay off on every read.

---

## Naming: Pack Information In (Ch. 2)

A name is a tiny comment. Use it to communicate everything a reader would otherwise need to read the implementation to find out.

### 1. Choose specific words

Generic verbs are a tax. Replace them with one that survives reading aloud.

| Generic | More specific |
|---|---|
| `Get()` | `Fetch()`, `Download()`, `Lookup()`, `LoadFromCache()` |
| `Size()` | `Height()`, `NumNodes()`, `MemoryBytes()` |
| `Stop()` | `Kill()` (irreversible), `Pause()` (resumable) |
| `make`/`do` | `create`, `build`, `set up`, `generate`, `compose` |
| `send` | `deliver`, `dispatch`, `announce`, `route`, `forward` |
| `find` | `search`, `extract`, `locate`, `recover` |

The thesaurus is a real tool. Reach for it.

### 2. Avoid generic names — unless their generic-ness *is* the meaning

`tmp`, `retval`, `foo`, `data`, `info`, `it`, `bar` carry no signal. They survive only when the variable's *only* role is "a thing being momentarily swapped/returned." If `tmp` lives more than a few lines or holds anything specific, rename it.

Smell:
```
tmp = user.name();
tmp += " <" + user.email() + ">";
log(tmp);
```
Fix: `user_info = ...`.

`retval` is the canonical anti-pattern — at minimum encode what's being returned: `sum_squares`.

### 3. Concrete over abstract

`ServerCanStart()` is abstract — start when? where? `CanListenOnPort()` is concrete.

`--run_locally` is vague — a `--debug_mode` for what? `--extra_logging` or `--use_local_database` say exactly which behavior they toggle.

### 4. Attach extra information with suffix/prefix

When a variable's *units* or *state* matter, append them.

| Without | With |
|---|---|
| `delay` | `delay_secs` |
| `size` | `size_mb` |
| `limit` | `max_kbps` |
| `angle` | `degrees_cw` |
| `password` | `plaintext_password` / `unsafe_password` |
| `comment` | `unescaped_comment` / `html_utf8` |
| `id` | `hex_id` |

If a value has been escaped, normalized, validated, or transformed, encode that.

### 5. Length should match scope

A 3-line loop counter is fine as `i`. A class field used across hundreds of lines is `client_index`. Long names cost nothing in IDEs but cost the reader nothing extra to parse — pay the cost where the lifespan justifies it.

### 6. Use formatting to convey meaning

`ClassName`, `methodName()`, `CONSTANT_NAME`, `_private`, `kStaticConstant`. Adopt a project convention and stick to it; mixed conventions are worse than any single one.

---

## Names That Can't Be Misconstrued (Ch. 3)

After naming, scrutinize: *what other meanings could this name carry?* If a name has more than one plausible reading, change it.

### Patterns

| Pattern | Use |
|---|---|
| Inclusive limit | `max_items = 10`, `min_kbps` |
| Inclusive range | `first` / `last` (both endpoints included) |
| Inclusive/exclusive | `begin` / `end` (end is excluded — `for (i = begin; i < end; i++)`) |
| Boolean | prefix with `is_`, `has_`, `can_`, `should_` |
| Avoid `filter()` | use `select()` ("keep") or `exclude()` ("drop") |
| Avoid negations | `use_ssl = true` beats `disable_ssl = false` |

### Match user expectations

Names carry implicit contracts. Break them at your peril.

- `get*()` should be **cheap** — callers expect O(1). If yours iterates, rename `compute*()`.
- `size()` on a collection should be **O(1)**. If you have to count, call it `countAll()`.
- `is*()` should have **no side effects**.

### Evaluate multiple candidates

Brainstorm three names. Mentally read each one in context — at the call site, in a stack trace, in a code review comment. The best one needs no explanation.

---

## Aesthetics (Ch. 4)

Code is read by skimming first, then drilling in. Make the skim work.

### Three principles

1. **Consistent layout** — once the reader learns your pattern, every later file reads faster.
2. **Similar code looks similar** — parallel structure reveals parallel meaning.
3. **Group related lines into paragraphs** — blank lines are a free unit of structure.

### Tactics

**Extract repeated irregularity into a helper.** If three call sites have the same 6-line setup, that's a function. The reader skims three calls instead of three blocks.

**Use column alignment when it helps.**
```
CheckFullName("Doug Adams"     , "Mr. Douglas Adams"     , "");
CheckFullName(" Jake  Brown "  , "Mr. Jake Brown III"    , "");
CheckFullName("No Such Guy"    , ""                       , "no match found");
CheckFullName("John"           , ""                       , "more than one result");
```
…but don't force it. If alignment requires reformatting on every edit, drop it.

**Pick a meaningful order — importance, matches the HTML form, alphabetical — and use it everywhere.** Declarations, error handling, switch cases, init lists. Inconsistency makes the reader hunt.

**Declare in blocks.** Don't interleave unrelated declarations. Group by role:
```
// authentication
string email;
string token;
DateTime token_expiry;

// preferences
bool dark_mode;
string locale;
```

**Break code into paragraphs.** Blank lines between logical steps tell the reader "this chunk is one idea."

### Personal vs. project consistency

A weird convention everyone follows beats a clean convention only half the team uses. When in doubt, match the file.

---

## Comments — Knowing What to Write (Ch. 5)

> The purpose of a comment is to help the reader know what the writer knew.

When you write code you carry a head full of context. The code captures the *what*. Comments are the only place to capture the *why*, the *what-was-considered-and-rejected*, the *what-will-bite-you*.

### Don't comment

- **What the code already says.** `// constructor`, `// loop over items`. The reader has eyes.
- **A bad name.** A comment explaining a name is a sign the name should change. Fix the name, delete the comment.
- **Filler to satisfy style guides.** A bad comment is worse than no comment — it forces a read that returns nothing.

### Do comment

- **Why** a non-obvious choice was made. (`// using binary search because list is presorted and dataset is >100k`)
- **Flaws and limits.** Standard markers help future readers grep:
  - `// TODO:` polish
  - `// FIXME:` known broken
  - `// HACK:` ugly workaround
  - `// XXX:` danger / proceed carefully
- **The reasoning for constants.** `// 0.72 = best empirical ratio from A/B test #218`. Constants without rationale are landmines.
- **Likely pitfalls** the caller might not expect. `// may take 60s on inputs > 1M rows`. `// not thread-safe — callers must hold the index lock`.
- **Big-picture commentary** at file/class top. *Why* does this exist? *Where* does it fit?
- **Section labels inside long functions.** `// --- step 2: normalize ---` is a free table of contents.

### Anticipate confusion (the readers' shoes)

Walk through your code as a stranger. The places you'd stop and ask "wait, why?" are exactly where to put a comment. Common spots:

- A subtle invariant the code depends on.
- An optimization that looks like a bug.
- A workaround for a bug in a library you can't change.
- A piece of business logic that wouldn't be obvious from code alone.

### "Director's commentary"

Comment on the *design* decision, not the implementation. `// favored a linked list here because we delete from the middle 10x more than we iterate.` That's the kind of note the next maintainer needs.

---

## Comments — Precise and Compact (Ch. 6)

If you're going to spend the reader's screen real estate, spend it well.

### High information-to-space ratio

```
// The int is the CategoryType.
// The first float is the 'score', the second is the 'weight'.
typedef hash_map<int, pair<float, float>> ScoreMap;
```
becomes:
```
// CategoryType -> (score, weight)
typedef hash_map<int, pair<float, float>> ScoreMap;
```

### Avoid ambiguous pronouns

"This" and "it" point at whichever noun the reader guesses. Spell out the noun:

> *Insert the data into the cache, but check if it's too big first.*  (it = data or cache?)

> *Insert the data into the cache, but check if **the data** is too big first.* ✓

### Use input/output examples

One example beats a paragraph of description:

```
// Strip 'chars' from both ends of 'src'.
// Example: Strip("ab", "abbacaa") returns "c"
string Strip(string chars, string src);
```

### Describe behavior precisely

Vague:
```
// Return the number of lines in this file.
int CountLines(string filename);
```

What counts as a line? Empty file → 0 or 1? Trailing newline? Files of just `\n`?

Better:
```
// Count how many newline bytes ('\n') are in the file.
int CountLines(string filename);
```

### State intent, not mechanism

```
// fast version of std::hash — tested empirically against our key distribution
```
beats
```
// computes hash by xor-ing 8-byte chunks
```

### "Named parameter" comments at call sites

When booleans or magic numbers obscure intent at the call site, comment the argument inline:

```
Connect(/* timeout_ms = */ 10, /* use_encryption = */ false);
```

Even better: rename the parameter so callers can use a keyword-arg style.

### Information-dense words

Use vocabulary that compresses meaning: *heuristic*, *brute-force*, *canonical form*, *snapshot*, *raw*, *normalized*, *idempotent*, *amortized*, *fail-open*, *fail-closed*. One precise word can replace a sentence.
