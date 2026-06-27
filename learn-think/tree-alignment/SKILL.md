---
name: tree-alignment
description: Use when the user mentions tree alignment, logic tree, binary branching, or asks to walk down a tree. Guides a vague intent through mutually exclusive, collectively exhaustive binary forks to a concrete leaf/action.
---

# Tree Alignment

Walk a vague intent down a clean binary logic tree until the user reaches a concrete leaf.

## Steps

1. **Name the root.**
   - Convert the user's stated intent into a short root label.
   - Do not explain the method unless the user asks.
   - Completion criterion: the root is short enough to fit in a breadcrumb, e.g. `Meal`, `Career Move`, `Weekend Plan`.

2. **Ask one binary fork.**
   - Ask exactly one question with exactly two branches: `a)` and `b)`.
   - Use this format:

   ```md
   Breadcrumb: <Root → selected path>

   Question <N>: <single binary fork>

   a) <branch>
   b) <branch>

   Recommendation: <No recommendation — preference fork. | Choose a/b because ...>
   ```

   - Include a recommendation only when context makes one branch clearly more useful; otherwise write `No recommendation — preference fork.`
   - Completion criterion: the fork is binary, mutually exclusive, collectively exhaustive, and answerable without seeing later forks.

3. **Advance the path.**
   - If the user answers `a` or `b`, append that branch to the breadcrumb.
   - If the user gives a clear freeform answer, map it to `a` or `b` and continue.
   - If the answer is ambiguous, ask the user to choose `a` or `b`; do not create a third option.
   - Completion criterion: exactly one branch has been selected for the current fork.

4. **Repair bad forks.**
   - If the user rejects both branches, says “neither,” or exposes overlap, treat the fork as invalid.
   - Replace it with a cleaner binary split; do not force the old choice.
   - Completion criterion: the replacement fork makes “neither” impossible or defines the terms tightly enough that the user can choose.

5. **Handle controls.**
   - If the user says `back`, return to the previous fork and remove the last selected branch.
   - If the user says `show the tree` or `tree view`, include a compact mini tree with the next fork; otherwise show only the breadcrumb.
   - Completion criterion: the visible state matches the user's requested mode and current path.

6. **Stop at a leaf.**
   - Stop when the path reaches a concrete action/result, or when another fork would not meaningfully change the answer.
   - Completion criterion: the leaf can be acted on or clearly names the narrowed category.

7. **Produce the Alignment Verdict.**
   - End with this card:

   ```md
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   TREE ALIGNMENT VERDICT
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ROOT
     <root>

   PATH LOCKED
     <indented selected path>

   LEAF
     <final leaf>

   ACTION
     <recommended next action or concrete options>

   ASSUMPTIONS
     ✓ <definitions or thresholds used>
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

   - Completion criterion: the card includes the root, chosen path, final leaf, action, and every definition/threshold used to keep forks clean.

## Compact reference: valid binary forks

Use the cleanest available split:

- **A vs not-A:** `Cook` / `Don’t cook`; `Requires shopping` / `Doesn’t require shopping`.
- **Threshold:** `Under $10` / `$10 or more`; `Under 15 minutes` / `15+ minutes`.
- **Partition:** two defined buckets that cover the space, e.g. `Homemade` / `Purchased`, `Solo` / `Social`.

Avoid fuzzy opposites unless you define the boundary. `Cheap` / `Expensive` needs a threshold; `Hot` / `Cold` needs a definition like `Hot` / `Not hot` if room-temperature would otherwise fall through.

A valid fork makes each option exclusive and makes the pair exhaustive. If “both” or “neither” is plausible, repair the split before continuing.
