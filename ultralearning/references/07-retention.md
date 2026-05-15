# Retention — Deep Dive

> "Don't Fill a Leaky Bucket." (Ultralearning, ch. X)

## What it is

Retention is the engineering of memory across the lifespan of a project. It is the deliberate act of holding on to what you learn — both while you are still learning it (so the vocabulary from week 1 is alive in week 10) and after the project ends (so the skill survives years of disuse).

Young opens the chapter with Hermann Ebbinghaus's **forgetting curve**: a steep exponential decay in the hours and days after learning, tapering off the longer a memory survives. The bucket leaks most at the top. Whatever you don't actively defend against this curve will quietly drain away, regardless of how hard you worked to put it in.

Retention is treated as one of nine principles, but it interacts with most of the others. Direct practice overlearns the high-frequency core. Retrieval is itself a memory-strengthening act. Drill builds proceduralized sub-skills that decay more slowly. And the wrong retention plan — a theoretically optimal SRS schedule you abandon after two weeks — produces worse outcomes than a crude plan you actually stick to.

## Why it works (the science)

- **Hermann Ebbinghaus** — Memorized nonsense syllables, tracked recall over time, derived the exponential forgetting curve. Most loss happens fast, then decay slows.
- **Three theories of forgetting** Young walks through:
  - **Decay** — memories erode with time. Matches intuition but can't explain why vivid childhood events outlast last Tuesday's breakfast.
  - **Interference** — proactive (old memories block new) and retroactive (new memories overwrite old). Anyone who has learned Spanish and then French knows retroactive interference.
  - **Forgotten cues** — the memory is stored but the retrieval path is severed. Predicts the tip-of-the-tongue feeling and the fact that relearning is faster than first learning.
- **Spacing effect** — Spread study over more sessions and you see lower short-run, much higher long-run retention. Ten one-hour sessions beat one ten-hour cram.
- **Procedural vs. declarative memory** — Procedural skills (riding a bicycle, touch-typing) decay far less than declarative knowledge (the Pythagorean Theorem). Most skills migrate declarative → procedural with enough practice.
- **Overlearning** — Continued practice past the point of first correct performance extends retention. Lab studies typically use rifle assembly and emergency checklists; effects are short-term on their own, but Young argues they compound when paired with spacing.
- **An algebra study Young cites** — Students who later took calculus retained more algebra than those who didn't. Moving up a level overlearns the level below.
- **Daniel Willingham's epigraph** — "Memory is the residue of thought."
- **Joshua Foer's *Moonwalking with Einstein*** — Young recommends it as an introduction to mnemonic technique; mnemonic competitors memorize a shuffled deck in under sixty seconds.

The four mechanisms all retention tactics roll up to: **Spacing, Proceduralization, Overlearning, Mnemonics.**

## The named tactics

### Spaced-Repetition Systems (SRS)

Software (Anki is Young's named example; Pimsleur, Memrise, and Duolingo hide SRS algorithms inside) schedules each review near the forgetting threshold. Best for atomic Q/A material: vocabulary, definitions, equations, anatomical maps. Roger Craig used SRS (built on Piotr Woźniak's algorithm) to dominate Jeopardy!.

Use SRS when the bottleneck is sheer volume of arbitrary facts and the relationship is cleanly cue → response. Avoid it when the knowledge is highly contextual or when the application format varies a lot. SRS is a sharp tool for narrow problems, not a substitute for direct practice.

**Contraindication:** Young warns that SRS optimization can become a fetish. A simple system you actually stick with beats a theoretically optimal one you abandon. Don't let perfect become the enemy of good enough.

### Refresher Projects

Semi-regularly redo a small project to reactivate skills that don't fit a daily habit. Young used this for the programming skills from the MIT Challenge — half an hour a week isn't enough to keep coding alive, but a small project every few months is. The schedule deviates from optimal spacing, but a little relearning per refresh is cheaper than starting from zero.

Use refresher projects when the skill is too elaborate to drip-feed (large software projects, finished drawings, full essays in a foreign language).

### Semi-Regular Practice Schedule

Young's post-language-project maintenance plan: 30 minutes of conversation per week on italki for one year, then 30 minutes per month for two more years. The decaying schedule mirrors the fact that forgetting itself decays — the bucket leaks more slowly the longer you've held the water.

He explicitly notes this isn't optimal, but it was sustainable, and sustainable beat optimal in his case. The point isn't the exact numbers; it's that the maintenance frequency can taper.

### Core Practice

Overlearn the small kernel of high-frequency moves — the opening phrases of a conversation, the standard library functions you reach for first, the fundamental algorithms — so they become procedural and effectively permanent. Young observed that the "starting points of conversations" from his Year Without English are nearly impossible to forget, because they got hammered constantly. The classic "move on from beginner material" pattern in school sidesteps this benefit by spreading practice evenly.

### Advanced Practice

Push to a higher-level skill whose use incidentally overlearns the lower-level prerequisite. The cited algebra study: students who later took calculus retained more algebra than those who didn't. Same pattern: writers who keep writing don't forget grammar; coders who tackle harder languages overlearn the basics of their first.

When you can't keep practicing the original level directly, levelling up the difficulty is a sneaky form of retention.

### The Keyword Method

A specific mnemonic, mostly for vocabulary. Three steps:

1. Take the foreign word and find a phrase in your native language that **sounds like** it. (French *chavirer* — "to capsize" — sounds like "shave an ear.")
2. Construct a **vivid, bizarre image** that combines the sounds-like and the meaning. (A giant ear shaving a long beard while sitting in a capsizing boat.)
3. To recall the word, summon the image, which surfaces the sounds-like phrase, which surfaces the word.

Each conversion takes roughly fifteen to twenty seconds with practice.

**Contraindications.** Young is candid: mnemonics are powerful but brittle. Recall via mnemonic is slower than direct recall — fast enough to remember a word, too slow to speak fluently. Treat keyword-method recall as a bridge, not a final destination. The biggest mnemonic feats (memorizing pi to thousands of digits) require an up-front investment that pays back only on tasks that paper and computers already solve for us.

## Anchor story

**Nigel Richards.** A New Zealand engineer with a long beard and aviator sunglasses, who won the French World Scrabble Championship in 2015 without speaking French. After his win he needed a translator to thank the audience. His prior credentials in English Scrabble made him a legend; the French win — a dictionary nearly double the size of English — made him a mystery.

His method, as best Young could reconstruct from his laconic interviews, was almost embarrassingly simple. He reads lists of words from the dictionary, ignoring meaning, tense, and plurals — just letter combinations. Then he gets on his bike, cycles for hours, and rehearses the lists mentally. He had eight weeks of preparation before the French championship. He is also famously obsessive — once cycling 200 miles overnight to a tournament, winning, and cycling back the same way before Monday morning.

Young's read: spacing plus active recall plus obsessive volume. No exotic system. The lesson isn't to copy the cycling — it's to notice that a simple, sustainable mechanism, applied with intensity, beat every speaker of French in the world.

## Worksheets / templates

### Decaying-maintenance schedule (modeled on Young's italki plan)

After your ultralearning project ends, pick a frequency that's just slightly more than "nothing" and let it decay:

| Period | Frequency | Format | Example (Young, languages) |
|---|---|---|---|
| Year 1 post-project | Weekly | One short focused session | 30 min italki conversation |
| Year 2–3 post-project | Monthly | One slightly longer session | 30 min italki conversation |
| Year 4+ | Quarterly or trigger-based | Either scheduled or "next time it comes up" | Speak when you meet a native speaker |

Fill in your version:

- Skill: ___________
- Year 1 cadence: ______ × per week, ______ minutes, in what format: ___________
- Year 2 cadence: ______ × per month, ______ minutes
- Trigger event that resets the schedule (a trip, a project, a job change): ___________
- Where this lives on the calendar so it actually happens: ___________

### Anki / SRS deck design rules

Drawing on the chapter's caveats about narrow SRS use, plus the retrieval-practice principles from ch. VIII:

1. **One fact per card.** If the answer contains "and" or a list, split it.
2. **No compound questions.** "When was the Magna Carta signed and what did it establish?" → two cards.
3. **Cue → response is unambiguous.** If the cue could plausibly trigger several correct answers, narrow it.
4. **Cards are atomic, not paragraphs.** Definitions, formulas, vocabulary — yes. Concepts that require integration — use a different tool.
5. **Add cards as you encounter the gap.** Don't bulk-import an SRS deck someone else built; the discriminations you need are personal.
6. **Maintenance, not creation.** Once you're doing more than ~20 minutes/day of SRS review, either your scope is too wide or your cards are too compound.
7. **Mnemonics live in the card itself.** If you used the keyword method to learn *chavirer*, write the image on the back so reviews refresh both layers.

### Four-mechanism audit for any topic

For a given subject, identify which of the four retention mechanisms you are using:

- **Spacing** — Where in the next 8 weeks is the next exposure already scheduled?
- **Proceduralization** — Which sub-skills have I practiced enough that they no longer require deliberate thought?
- **Overlearning** — Have I continued past the first correct performance on the high-frequency core?
- **Mnemonics** — For the dense / arbitrary / format-specific corner, is there a mnemonic bridge in place?

If any of the four is empty for an important sub-skill, that's the retention gap to fix.

## Anti-patterns specific to this principle

- **Cramming for long-term retention.** Same ten hours in one block lose to ten hours over ten days. Cramming inflates short-term performance and collapses days later.
- **Letting hard-won skills atrophy with no maintenance plan.** Forgetting is the default. The end of a project is not the end of the work.
- **Optimizing SRS schedules you don't stick with.** "Don't let perfect become the enemy of good enough." A 15-card-per-day routine you actually do beats an optimal schedule you abandon in week three.
- **Using mnemonics as the foundation of fluency.** They are a bridge for difficult-to-remember information, not a substitute for the direct retrieval that fluency requires.
- **Spreading practice evenly across an entire curriculum.** This is the standard schooling pattern and it leaves no overlearned core. Identify the high-frequency kernel and overlearn it.
- **Practicing the whole skill at a low frequency and assuming all sub-skills decay at the same rate.** Procedural sub-skills decay slowly; declarative sub-skills (vocabulary, regulations, formulas) decay fast and need their own mechanism.

## When to push this principle vs. when to relax it

**Push retention hard when:**

- The domain is memory-heavy by definition: medicine, law, languages, trivia, anatomy.
- The skill will sit unused for stretches and then need to be available on demand.
- Volume of arbitrary material is the bottleneck (Roger Craig's Jeopardy! prep, Nigel Richards's Scrabble lists).
- The cost of forgetting is high: a doctor who has forgotten a drug interaction; a lawyer who has forgotten a precedent.

**Relax retention when:**

- The information is freely lookup-able and the skill is "knowing *that* a domain exists" rather than "knowing every detail." Young explicitly endorses controlled decay in this case — relearning is faster than first-time learning.
- You are still in the early phase of a project and the right action is to add new material, not lock down what you have.
- The maintenance plan is starting to crowd out new learning. Maintenance is a tax; pay only enough to keep what you actually use.

**Choose explicitly between maintenance, relearning, and mastery** at project end (Young's Step 5). The wrong choice isn't "I picked the wrong one" — it's "I never decided, and the skill decayed by default."

## Cross-links

- See [SKILL.md](../SKILL.md) for retention in the context of the nine-principle workflow.
- Related principles:
  - **Retrieval** (ch. VIII) — every retrieval attempt is also a retention event; the testing effect and the forward-testing effect bleed into this chapter.
  - **Drill** (ch. VII) — the rate-determining-step framing applies to retention bottlenecks too; if a particular sub-skill is decaying faster than the rest, drill it on its own retention cycle.
  - **Directness** (ch. VI) — direct use of a skill produces overlearning of the high-frequency core almost for free.
  - **Intuition** (ch. XI) — the chess-chunks finding (~50,000 stored patterns) is, in part, a retention story: pattern libraries are durable only because they are constantly retrieved in real games.
