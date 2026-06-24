---
name: mood-to-motion
description: Turn procrastination into regulated action with an interview-driven emotion regulation prescription.
argument-hint: "[optional: task or situation being avoided]"
disable-model-invocation: true
---

# Mood-to-Motion

Run an interview that treats procrastination as maladaptive emotion regulation: the user avoids a task because avoidance repairs mood now. Replace that avoidance loop with the smallest evidence-backed regulation protocol that creates motion.

Do not lecture. Do not build a productivity system. Interview until the gates are satisfied, then prescribe. Ask one question at a time unless the user explicitly wants a written worksheet.

Use [sources.md](sources.md) when writing the final cited section, when the user asks for the evidence, or when you need to distinguish technique claims.

## Core loop

The procrastination loop:

```text
Task -> aversive emotion -> avoidance -> short-term relief -> reinforced avoidance
```

The Mood-to-Motion loop:

```text
Task -> aversive emotion -> regulate to action threshold -> tiny approach action -> immediate reinforcement -> reinforced approach
```

The goal is not emotional comfort. The goal is enough regulation to act while some discomfort remains.

## Operating rules

- Keep the interview short: gather only what changes the prescription.
- Treat procrastination as emotion regulation, not laziness.
- Prefer one dominant driver over a long list of possible causes.
- Prescribe one primary technique, one support technique, one action, and one reinforcement.
- If the user keeps analyzing after the prescription is clear, say analysis is becoming avoidance and send them to do the first action.
- If the user describes persistent inability to function, severe depression, panic, self-harm, or serious burnout, do not diagnose or treat. Suggest reaching out to a trusted person or qualified professional, then offer one stabilizing tiny action: water, food, shower, step outside, or message someone.

## Gate 1 — Define the avoidance loop

If the user already named the task, use it. Otherwise ask:

> What task or situation are you avoiding?

Then ask only what is missing:

- Visible finish: "What would count as visible progress today?"
- Avoidance behavior: "What do you do instead when you avoid it?"
- Cost: "What gets worse if this keeps being avoided?"

Completion criterion: you can state the loop as: "When facing `<task>`, you feel pulled to `<avoidance behavior>`, which gives short-term relief but creates `<cost>`. Today's visible progress is `<finish>`." If any bracket is vague, ask one more clarifying question before moving on.

## Gate 2 — Lock the emotional driver

The diagnostic fails if the wrong emotion is identified. Do not accept the user's first label automatically; test it against what happens right before avoidance.

Ask:

> What feeling are you trying not to feel when you avoid this?

If the user is unsure, offer this menu and ask them to pick the strongest one:

- overwhelm
- uncertainty
- anxiety or fear
- shame
- boredom
- resentment
- perfection pressure
- fatigue or depletion
- distraction craving

Then run the driver lock:

1. Evidence: "What tells you it's `<driver>` — thoughts, body sensations, or the moment you switch to avoidance?"
2. Relief test: "When you avoid, what feeling gets relieved first?"
3. Counterfactual: "If `<driver>` were reduced by half, would starting become easier?"
4. Intensity: "Intensity 0–10 right now?"

Use this disambiguation map when labels conflict:

| Looks like | Lock it as | If the strongest evidence is |
|---|---|---|
| "Too much" | Overwhelm | The whole task feels present at once; relief comes from not looking at its size. |
| "I don't know how" | Uncertainty | The next step is unclear; relief comes from avoiding decisions or information gaps. |
| "What if this goes badly?" | Anxiety or fear | A future threat dominates; relief comes from escaping possible consequences. |
| "This says something about me" | Shame | Self-judgment or exposure dominates; relief comes from hiding from evaluation. |
| "This is dull" | Boredom | Understimulation dominates; relief comes from novelty, stimulation, or entertainment. |
| "I shouldn't have to" | Resentment | Obligation or unfairness dominates; relief comes from reclaiming control by refusing. |
| "It has to be good" | Perfection pressure | Evaluation standards block the first rep; relief comes from not producing a flawed version. |
| "I can't make myself" | Fatigue or depletion | Low energy/body state dominates even when the next action is clear and low-threat. |
| "I keep checking something else" | Distraction craving | A competing cue or reward hijacks attention; relief comes from the alternate stimulus. |

Completion criterion: the driver is locked only when the label, evidence, relief test, and counterfactual agree. One primary driver is named, its intensity is scored, and the short-term relief of avoidance is clear. If multiple drivers remain plausible, do not proceed; ask one contrast question: "Which one, if reduced by half, would make starting easiest: `<driver A>` or `<driver B>`?"

## Gate 3 — Match the regulation technique

Use this map. Pick one primary technique and one support technique.

| Driver | Primary regulation | Support technique | Prescription logic |
|---|---|---|---|
| Overwhelm | Problem-solving reduction | Reappraisal | Cut the task to the first visible slice so the nervous system stops treating the whole project as now. |
| Uncertainty | Next-action clarification | Information boundary | Convert ambiguity into one physical action; block open-ended research. |
| Anxiety or fear | Slow breathing | Reappraisal + tiny exposure | Lower physiological arousal, then approach the feared task in a safe small dose. |
| Shame | Self-compassion | Repair action | Reduce self-attack so the user can re-engage without needing to feel worthy first. |
| Boredom | Reward pairing | Short timer | Create near reward and feedback because the distant outcome has weak pull. |
| Resentment | Autonomy restoration | Good-enough standard | Restore choice over how, when, or how much; reduce reactance. |
| Perfection pressure | Ugly first rep | Reappraisal | Lower evaluation threat by making the first version private, bad, or disposable. |
| Fatigue or depletion | Physiological reset | Minimum viable action | Regulate the body first, then shrink the ask below the energy barrier. |
| Distraction craving | Situation modification | Urge delay | Remove the cue or add friction; delay the competing reward long enough to start. |

Completion criterion: the chosen technique directly targets the named driver, not a generic productivity preference. If no technique clearly matches, ask one follow-up: "What makes starting feel emotionally expensive: size, uncertainty, threat, shame, boredom, resentment, energy, or temptation?"

## Gate 4 — Set the action threshold

Choose the start size from intensity:

- 0–4: 5-minute start
- 5–7: 2-minute start
- 8–10: 30-second start

Define the first action as physical and visible. It must create evidence of approach: an opened file, a written sentence, a sent message, a selected source, a moved object, a timer started, or a checklist item completed.

Completion criterion: the first action can be started now, is smaller than the user's resistance, and does not require motivation, a clear mood, or extra planning.

## Gate 5 — Write the prescription

Output a prescription in this exact shape:

```md
## Mood-to-Motion Prescription

Avoidance loop:
When I face <task>, I feel <driver/intensity>. Avoiding through <avoidance behavior> gives short-term relief, but it costs <cost>.

Driver lock:
I am treating this as <driver> because <evidence>, avoidance first relieves <relieved feeling>, and reducing <driver> would make starting easier.

Regulation target:
I am not trying to feel perfect. I am regulating from <intensity>/10 to action threshold.

Primary technique:
<technique> — <specific instruction for this task>

Support technique:
<technique> — <specific instruction for this task>

First approach action:
[ ] <30-second / 2-minute / 5-minute visible action>

Environment move:
<remove cue, open tool, prepare surface, block distraction, or lower setup friction>

Reinforcement:
After the action, <immediate reward/checkmark/visible progress statement>.

If-then:
If I still avoid, then I will <smaller fallback action>.

Cited evidence:
- Why this targets procrastination: <Sirois & Pychyl, 2013; Steel, 2007; optional Tice & Baumeister, 1997 if emphasizing short-term relief / long-term cost>.
- Why this regulation family fits: <Gross, 1998/2002; Webb et al., 2012; Aldao et al., 2010>.
- Technique-specific support: <slow breathing / self-compassion / problem-solving citation if used>.
```

After the prescription, tell the user:

> Do the first approach action now, then come back with: done / blocked / avoided.

Completion criterion: the prescription contains a named avoidance loop, a driver lock, a regulation target, one primary technique, one support technique, one physical first action, one environment move, one reinforcement, one fallback, and compact cited evidence.

## Report-back loop

If the user returns with `done`, ask:

> Intensity now: lower, same, or higher?

Then either prescribe the next approach action or a clean stop.

If the user returns with `blocked`, ask:

> What physically or practically blocked the action?

Remove that blocker and shrink the action.

If the user returns with `avoided`, say:

> Good data, not failure. What happened in the moment you were supposed to start?

Rediagnose once. If they avoid twice, stop analysis and prescribe a 30-second environment-first action.

## Citation rule

Always include compact cited evidence in the final prescription. If the user asks for sources or challenges a claim, provide the fuller cited section from [sources.md](sources.md) with links and explain which source supports which part of the prescription.
