# Critical Chain — TOC for Projects

Manufacturing flow is repetitive; projects are one-shot. Goldratt's *Critical Chain* (1997) adapts TOC to project work — software projects, R&D, construction, anything with a deadline and finite resources.

When the user is planning a one-shot project (vs. running a steady-state flow), prefer Critical Chain framing.

## The three signature ideas

### 1. The constraint is the longest *resource-aware* dependency chain

Traditional project management uses the **Critical Path** — the longest sequence of dependent tasks. Critical Chain adds resource contention: if the same person is on two parallel branches, those branches aren't actually parallel.

The **critical chain** is the longest path through the project *after accounting for shared resources*. It is, by definition, the project's constraint. Every day the critical chain is delayed, the project is delayed.

**Why this matters:** standard PM software calculates the critical *path* and treats parallel tasks as actually parallel. Real projects miss because someone is needed on three "parallel" tracks simultaneously. Critical Chain forces that conflict to surface during planning.

### 2. Strip per-task safety; pool it into a project buffer at the end

The classic project pathology:
- People are asked for estimates and judged on hitting them.
- They pad the estimate (often 2-3x) to protect themselves.
- Then they consume the padding via:
  - **Parkinson's Law** — work expands to fill available time.
  - **Student syndrome** — start at the last possible moment ("I have 2 weeks, no rush").
  - **Multitasking** — get pulled to other work because "this one has slack."
- The padding gets consumed; the task still finishes late or just on time. The padding never aggregates upward; you just get slow projects with no apparent slack.

**The Critical Chain fix:**
1. Estimate aggressively — ~50% probability of finishing on time per task. Half the tasks will run over; that's expected.
2. Strip the safety from each task.
3. Pool the safety into a single **project buffer** at the project's end (typically 50% of the stripped estimates).
4. Manage the buffer, not the per-task deadlines. Per-task overruns are normal; buffer consumption is what triggers escalation.

The buffer absorbs variability *centrally* (which is mathematically far more efficient than per-task buffering — pooling reduces total safety needed by ~50% via the central limit theorem).

Add **feeding buffers** where non-critical-chain tasks merge into the critical chain, so a late feeder doesn't push the critical chain.

### 3. No multitasking on the critical chain

Switching between projects multiplies elapsed time of *all* of them. If a developer splits time across three projects:
- Each project takes ~3x longer in elapsed time vs. focused work.
- Context-switch tax adds further slowdown.
- Total throughput drops vs. sequential project execution.

The project-level utilization fallacy: keeping every developer on multiple projects *feels* productive (no idle time) but slows every project. Critical Chain says: **no multitasking on critical-chain tasks.** When you're on a CC task, you're on it until done.

This is hard culturally. Managers see a developer "free" for an hour and ask them to fix something else; the cost is invisible (everyone's project slips a tiny amount) and the relief is visible (the urgent thing got addressed).

## Buffer management — how to run a Critical Chain project

The project buffer is the management dashboard. As tasks complete, the buffer either remains intact (project ahead) or gets consumed (project behind).

Divide the buffer into thirds:
- **Green** (first third consumed) — watch only.
- **Yellow** (middle third consumed) — make a recovery plan.
- **Red** (final third consumed) — execute the recovery plan.

Plot **buffer consumption vs. critical-chain progress**. If you're 50% through the chain and 60% through the buffer, you're in yellow. If 30% through the chain and 70% through the buffer, you're red and need to act.

This replaces per-task status reporting (which is dishonest theater because of student syndrome).

## Workflow tells — when to reach for Critical Chain

- "We always slip our deadlines."
- "Each task hits its date but the project is late." (Suspicious — usually it's that *some* tasks slip, padding hides it, and feeding buffers don't exist.)
- "Everyone's working on too many things."
- "We can't tell if we're going to make it until the last week."
- A roadmap with explicit dates and parallel "swim lanes" assuming people can be on multiple lanes at once.

## When *not* to use Critical Chain

- Steady-state flow (not project work) — use DBR instead.
- Very short projects (< 2 weeks) — overhead exceeds benefit.
- Projects where the team won't actually strip per-task safety — partial implementation creates the worst of both worlds (no per-task safety AND no project buffer).

## Common Critical Chain failures

- **Adding a project buffer without stripping per-task safety.** Now you have padded estimates *and* a buffer; everything is slow and the buffer is huge.
- **Treating the project buffer as a target deadline.** "We'll deliver by [end of buffer]" — kills the discipline. The buffer is a safety mechanism, not a commitment.
- **Allowing multitasking despite naming the critical chain.** The CC is identified but everyone keeps cross-allocating. The chain is symbolic, not enforced.
- **Computing CP not CC.** Standard PM tools compute the path, ignore resource contention, mislabel the result as the "critical chain."

## Source

*Critical Chain* by Eliyahu M. Goldratt (1997). The novel form makes it readable but the operational rules are scattered — the appendices and Goldratt Institute white papers consolidate the actual procedures.
