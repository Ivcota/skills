# Analysis — Front-End, Needs, and Task Analysis

> Source: Pastore, R. (2020). *The Instructional Design and Development Process: A 'How To' Guide for Practitioners*. KDP. ISBN 9798651489978.

The single most leverage-bearing phase. "70% of projects fail and poor analysis and management are usually the cause" (p. 106). Skip or rush this and the rest of ADDIE is wasted.

## Two distinct activities

| Activity | Question it answers | Output |
|---|---|---|
| **Front-End Analysis (FEA)** / Performance Analysis | Is training actually the right intervention? | Recommended solution (training or other) |
| **Needs Analysis** | Given training is the answer, what kind? | Learner + context + gap analysis |
| **Task Analysis** | What tasks must learners be able to do? | Hierarchical task list, signed off by SME/client |

Pastore: "The point of performance/front-end analysis is to determine if training is really the problem and the point of an instructional analysis is to determine what training solution is best" (p. 26). In practice these are usually run together (pp. 25, 28).

## 1. Front-End Analysis — the 4-step model

(Figure 2.0, p. 17)

1. **Determine the problem, cause, and solution.** Who/what/where/when/why. Gap analysis. End goal: a recommended solution.
2. **Design and develop.** If training is the solution, begin the ID analysis. Otherwise solve via other means.
3. **Implement the solution.** Rollout, change management.
4. **Evaluate effectiveness.** Did you solve the problem? ROI? Select an evaluation model.

### How to gather information (p. 18)

- Interviews
- Meetings
- Observations
- Surveys
- Document analysis

Usually starts with 1–2 meetings with the manager + SME. Realistically, you may have **only one phone call** to do FEA — "knowing what information you need and knowing what questions you need to ask is vital to project success" (p. 16).

### Root-cause: the "Why" exercise

(Olivier, 2017 — cited p. 18)

Keep asking "why" until you reach the underlying cause. Don't stop at the first plausible reason. Example: "employees are entering bad data" → why → "they don't know the new fields" → why → "the field names changed in the new release and no one was told" → root cause is communication, not training.

### Gap Analysis (Table 1.0, p. 20)

Three columns:

| Current State | Desired State | Recommended Solution |
|---|---|---|
| What is happening now | What the client wants | Concrete intervention(s) with ROI/budget/timeline |

**Watch out for the "dream desired state."** Clients often describe an unrealistic future. Present **multiple solutions** at different price points / timelines so the client can choose with eyes open (pp. 19–20, 32–33).

### When training is NOT the answer (p. 15)

- Communication problem
- Computer/system glitch
- Motivation problem
- Multiple problems (training is one piece)

Solve via other means: fix the system, communicate the message, change incentives.

## 2. Training Charter — start day 1

(pp. 26–27)

Analogous to a PM project charter. Contents:

- Client
- Problem
- Cause
- Intervention
- Stakeholders
- Managers
- SMEs
- ROI
- Budget
- Schedule

Maintain it from kickoff through delivery. It's the artifact stakeholders ratify when scope arguments arise.

## 3. Needs Analysis = Learner + Context + Gap

### Learner Analysis (p. 29)

Profile the actual learners:

- Education level
- Computer / smartphone literacy
- Age
- Motivations
- Work conditions
- Preferences (video / online / classroom / CBT)

**Pastore on learning styles (p. 30):**
> "There is no learning style. We might examine if the learners prefer and are used to learning via video, online learning, computer-based training, classroom, etc."

Preferences are real and design-relevant. "Learning styles" (visual/auditory/kinesthetic learners) are a myth — don't burn design budget on them.

### Context Analysis (pp. 30–31)

The conditions where the new skill will be used:

- Physical environment
- Available technology
- LMS in use (if any — many clients don't know what theirs is)
- Budget for new technology

**Common trap:** "We have an LMS" → which one? → "I don't know." Pin this down before building anything.

### Content Walkthrough (pp. 33–34)

A short SME session to get a realistic estimate of how much content there really is.

> "The client will tell you it's a 30-minute course. Then you walk through the content and it's 2 hours."

Without this, your budget and schedule are fiction.

### Goals (p. 34)

Two kinds:

- **Project goals** — PM-style ("complete by Q3, under $X")
- **Instructional goals** — general ("Train users to fly a plane")

**Goal vs Objective:** a goal is general; an objective is specific and measurable (p. 35). Goals come from analysis; objectives come in design (§Design).

## 4. Task Analysis (§4.1)

Done after client sign-off on goals. Decompose the goal into the specific tasks/skills/knowledge a learner must master (p. 36).

### Procedure

1. Break the high-level goal into tasks.
2. Prioritize each task on a 1–10 scale across (Table 3.0, p. 38):
   - **Importance** — how critical to the goal
   - **Difficulty** — how hard to learn
   - **Length** — how long to teach
   - **Cost** — to develop
3. Recursively decompose each task into sub-tasks until **prior knowledge takes over** (i.e., further decomposition would teach things the learner already knows).
4. Pick a format:
   - **List** — hierarchical numbering (1.0 → 1.1 → 1.1.1)
   - **Tree** — graphic decomposition (Figure 3.0, p. 42)

### Sign-off

Get the SME/client to sign off on the task analysis **before writing learning objectives** (p. 36). This is the single biggest scope-creep prevention move in the whole framework.

### Pro tip

Start template development during task analysis (p. 36) — you'll know enough by then to pick fonts/format/style.

## 5. Analysis Document — what to deliver

(pp. 43–44)

Sample structure:

1. Training Charter summary
2. Front-End Analysis results
3. Learner + Context Analysis results
4. Project solution + goals
5. High-level prioritized task list
6. Full task analysis (list or tree)

Client signs this off before design begins.

## Common mistakes in analysis

| Mistake | Page | Consequence |
|---|---|---|
| Trusting client's stated problem | 15, 108 | Wrong solution to wrong problem |
| Skipping FEA when client says "I just need a course" | 16 | Training fails; performance gap remains |
| Skipping content walkthrough | 33–34 | Budget blow-up |
| Not pinning down LMS/tech upfront | 31 | Alpha test reveals incompatible stack |
| Recommending model before hearing problem | 23 | Wrong tool for the job |
| Confusing learning preferences with learning styles | 30 | Wasted design effort |
| Skipping task analysis sign-off | 38, 43 | Scope creep, redevelopment |
| One-shot meeting → write proposal next day | 16 | Missing information surfaces mid-build |

## Worked example (synthesized from Pastore's framing, pp. 18–20)

**Client request:** "We need a 30-minute course on the new ticketing system."

**FEA via "Why":**
- Why training? → Tickets are being mis-routed.
- Why mis-routed? → Wrong category selected on the form.
- Why? → Categories were renamed in v2.
- Why? → Release notes weren't sent to support staff.

**Root cause:** communication, not training.

**Recommended solutions** (gap analysis):
1. Send release notes + 5-min Loom walkthrough (cheap, fast)
2. 30-min refresher CBT (medium)
3. Full 2-hour ticketing certification course (expensive)

Present all three with ROI/budget/timeline; let the client choose.

## Copy patterns

> "Training is not always the answer." (p. 15)

> "You always need to go in knowing that you need to find the problem and cause then worry about the solution." (p. 16)

> "Good analysis helps ensure quality; bad analysis ensures poor quality." (p. 28)

> "70% of projects fail and poor analysis and management are usually the cause." (p. 106)

> "There is no learning style." (p. 30)
