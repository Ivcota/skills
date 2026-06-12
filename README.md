# Skills

Type `/grand-slam-offer`. Claude becomes Hormozi. Type `/zero-to-one`. Claude becomes Thiel. Every framework elite builders rely on — encoded as a single command, ready the moment you need it.

Organized by domain: **Product** (build the thing), **Craft** (sharpen yourself), **Business** (grow the company).

## Install

Every skill installs the same way:

```bash
npx skills@latest add Ivcota/skills/<skill-name>
```

## Index

- [Product & Engineering](#product--engineering)
  - [Discovery & scoping](#discovery--scoping)
  - [Modeling](#modeling)
  - [Delivery](#delivery)
  - [Code quality](#code-quality)
- [Craft](#craft)
  - [Thinking](#thinking)
  - [Habits](#habits)
  - [Learning](#learning)
  - [Workflow](#workflow)
  - [Voice](#voice)
- [Business](#business)
  - [Strategy & idea selection](#strategy--idea-selection)
  - [Customer](#customer)
  - [Offer & pricing](#offer--pricing)
  - [Demand](#demand)
  - [Authority](#authority)
  - [Operations](#operations)

---

# Product & Engineering

*Ship the right thing the first time.*

## Discovery & scoping

**User Story Mapping** — Stop shipping features that don't connect to outcomes. Builds a 2D grid — backbone + tasks — so the whole team sees the story before committing to a sprint.

```bash
npx skills@latest add Ivcota/skills/user-story-mapping
```

**Outcome-Driven Innovation** — Stop guessing what customers want. Captures Jobs, Outcomes, and Constraints, ranks opportunities with Ulwick's Opportunity Algorithm, and scores concepts before you build.

```bash
npx skills@latest add Ivcota/skills/outcome-driven-innovation
```

## Modeling

**Domain Storytelling** — Build a domain model the business actually recognizes. Interview-driven DDD that maps stakeholder conversations directly to code — no translation layer, no guesswork.

```bash
npx skills@latest add Ivcota/skills/domain-storytelling
```

**Solutions Architect's Handbook** — Design and review solution architectures across business goals, NFRs, architecture views, quality pillars, operations, cost, and SAD documentation.

```bash
npx skills@latest add Ivcota/skills/solutions-architects-handbook
```

## Delivery

**FAAS** — Ship features without the mess. Four phases — Find → ARCH → Automate → Specify-Test-Refine — so every feature lands clean, tested, and maintainable.

```bash
npx skills@latest add Ivcota/skills/faas
```

## Code quality

**Readable Code** — Write code that's fast to understand, not just short. Applies Boswell & Foucher's line-level tactics — naming, control flow, expressions, decomposition — to minimize time-till-understanding on every PR, function, and variable.

```bash
npx skills@latest add Ivcota/skills/readable-code
```

**Walkthrough** — Preserve the why behind non-trivial code changes. Chunks the current diff, writes rationale to `.claude/rationale/`, and gives future `/explain` calls something durable to recover.

```bash
npx skills@latest add Ivcota/skills/walkthrough
```

---

# Craft

*Think sharper than your tools.*

## Thinking

**Align Mental Model** — Catch wrong beliefs before they cost you. Runs a prediction-check loop — predict, rate confidence, see the truth. High-confidence-wrongs get traced to the root assumption. Three modes: codebase, learning, planning.

```bash
npx skills@latest add Ivcota/skills/align-mental-model
```

**Feynman** — Find out what you actually understand. Explain any concept simply until every gap surfaces — then fill them.

```bash
npx skills@latest add Ivcota/skills/feynman
```

**Grill Me** — Stress-test a plan or design until every branch of the decision tree is explicit. Asks one hard question at a time, gives a recommended answer, and stops before implementation.

```bash
npx skills@latest add Ivcota/skills/grill-me
```

**Grill with Docs** — Challenge a plan against the project's own language. Uses `CONTEXT.md` and ADRs to sharpen terms, catch contradictions, and record decisions only when they matter.

```bash
npx skills@latest add Ivcota/skills/grill-with-docs
```

**The ONE Thing** — Stop splitting attention, start making real progress. Runs Keller's Focusing Question and Goal Setting to the Now to isolate the one move that makes everything else easier or unnecessary.

```bash
npx skills@latest add Ivcota/skills/the-one-thing
```

**Essentialism** — Stop overcommitting and choose the vital few. Runs McKeown's Essence → Explore → Eliminate → Execute framework with the 90 Percent Rule, graceful no scripts, buffers, and routines.

```bash
npx skills@latest add Ivcota/skills/essentialism-disciplined-pursuit
```

## Habits

**Atomic Habits** — Turn goals into identity-based systems that survive real life. Applies James Clear's habit loop, Four Laws, environment design, habit stacking, tracking, and failure recovery.

```bash
npx skills@latest add Ivcota/skills/atomic-habits
```

**My Habits** — Surface the right active habit cards from your vault at the right time. Finds cue -> action cards by status, schedule, priority, weekday, date, and query.

```bash
npx skills@latest add Ivcota/skills/my-habits
```

## Learning

**Deep Learner** — Actually understand what you study, not just recognize it. Runs a 7-step Socratic framework — Anchor → Connect → Translate → Dissect → Stress Test → Evaluate → Build — so every concept gets pulled out of you, not poured in.

```bash
npx skills@latest add Ivcota/skills/deep-learner
```

**Four Pillars Learning Coach** — Learn through Dehaene's four pillars: focused attention, active attempt, diagnostic error feedback, and consolidation. Runs source-grounded tutoring one question at a time.

```bash
npx skills@latest add Ivcota/skills/four-pillars-learning-coach
```

**Bear Hunter System** — Actually remember what you learn. Builds a causal GRINDE map through AIM → SHOOT → SKIN so complex material sticks at 80–95% retention.

```bash
npx skills@latest add Ivcota/skills/bear-hunter-system
```

**ADDIE** — Design training that solves the real performance problem. Runs Pastore's ADDIE framework — Analysis, Design, Development, Implementation, Evaluation — with objectives, assessments, multimedia principles, and evaluation baked in.

```bash
npx skills@latest add Ivcota/skills/addie
```

**Ultralearning** — Build an aggressive self-directed learning project. Applies Scott Young's nine principles — Metalearning, Focus, Directness, Drill, Retrieval, Feedback, Retention, Intuition, Experimentation — to compress skill acquisition.

```bash
npx skills@latest add Ivcota/skills/ultralearning
```

**Ultralearning Draft** — Draft version of the Ultralearning skill with extended framework notes and project process detail.

```bash
npx skills@latest add Ivcota/skills/skills-draft/ultralearning
```

**Teach** — Turn this workspace into a stateful teaching environment. Builds lessons, references, resources, and learning records around the user's mission.

```bash
npx skills@latest add Ivcota/skills/teach
```

**Distill to Skill** — Turn any book into a Claude skill. Fans out citation-grounded agents to extract the frameworks, patterns, and cases — then synthesizes them into an installable skill.

```bash
npx skills@latest add Ivcota/skills/distill-to-skill
```

## Workflow

**Now** — Route the day without thinking. Inspects time, daily-note state, and user intent, then hands off to `/intentional`, `/go`, or `/wrap-up`.

```bash
npx skills@latest add Ivcota/skills/now
```

**Intentional** — Build a complete daily note before execution. Creates Shaped Goals, Rolling Timeblocks, and calendar-aware plans for today or tomorrow.

```bash
npx skills@latest add Ivcota/skills/intentional
```

**Go** — Sync progress and commit the next rolling timeblock. Use repeatedly during the day to stay locked in and keep the calendar aligned with reality.

```bash
npx skills@latest add Ivcota/skills/go
```

**Wrap Up** — Close the day cleanly. Summarizes completed and open work, captures missing logs, reflects, and hands off to `/intentional` for tomorrow.

```bash
npx skills@latest add Ivcota/skills/wrap-up
```

**One-Month Day** — Plan a single day built for a month's worth of output. Stacks flow blocks, clears load, builds a flow fortress, and locks tomorrow's deep-work schedule.

```bash
npx skills@latest add Ivcota/skills/one-month-day
```

## Voice

**Style Profile** — Write in your voice, not Claude's. Extracts a style profile from your samples and applies it to any new content.

```bash
npx skills@latest add Ivcota/skills/style-profile
```

**Style to Skill** — Make your voice a reusable command. Packages your style profile into a personal skill so you can invoke it anywhere — no source file needed.

```bash
npx skills@latest add Ivcota/skills/style-to-skill
```

**Humanizer** — Make AI-written text read like you wrote it. Detects and rewrites 29 AI patterns — significance inflation, em dash overuse, chatbot artifacts — with optional voice calibration from your own samples.

```bash
npx skills@latest add Ivcota/skills/humanizer
```

---

# Business

*Build the machine that grows.*

## Strategy & idea selection

**Office Hours** — Find the holes in your idea before the market does. Two modes: Startup (hard questions that expose fatal flaws) and Builder (think through the details).

```bash
npx skills@latest add Ivcota/skills/office-hours
```

**Zero to One** — Find out if your startup is genuinely different or just a copy. Runs Thiel's full framework — Contrarian Question, Monopoly vs Competition, Seven Questions — and gives you a verdict.

```bash
npx skills@latest add Ivcota/skills/zero-to-one
```

**Million Dollar Weekend** — Validate a business in 48 hours before you build. Runs Noah Kagan's process to find a problem, create a one-minute business model, and get three paying customers.

```bash
npx skills@latest add Ivcota/skills/million-dollar-weekend
```

**Millionaire Fastlane** — Score your wealth plan before it costs you a decade. Runs DeMarco's CENTS commandments and Wealth Equation to tell you if you're on the Sidewalk, Slowlane, or Fastlane.

```bash
npx skills@latest add Ivcota/skills/millionaire-fastlane
```

**Good Strategy / Bad Strategy** — Stop mistaking goals for strategy. Runs Rumelt's Kernel — diagnosis, guiding policy, coherent action — and flags the four hallmarks of bad strategy before you commit to a direction.

```bash
npx skills@latest add Ivcota/skills/good-strategy-bad-strategy
```

## Customer

**Validate ICP** — Prove the market exists before you build. Mines Reddit, HN, X, and forums for verbatim pain quotes — then returns a VALIDATED / WEAK / NOT FOUND verdict with source links and a DM list.

```bash
npx skills@latest add Ivcota/skills/validate-icp
```

**Buyer Profile** — Stop guessing why people buy. Builds a deep psychology profile — real emotional drivers, fears, and desires — so your copy and offer speak to the actual decision.

```bash
npx skills@latest add Ivcota/skills/buyer-profile
```

**Persona to Product** — Turn a buyer profile into ranked product ideas. Grounds each in real problems, failed solutions, and transformation desires — so you build what they'll actually pay for.

```bash
npx skills@latest add Ivcota/skills/persona-to-product
```

## Offer & pricing

**Value Equation** — Find the lever killing your conversions. Scores any offer, feature, or content across Hormozi's four levers — Dream Outcome, Perceived Likelihood, Time Delay, Effort — and gives you a path to 10/10.

```bash
npx skills@latest add Ivcota/skills/value-equation
```

**Grand Slam Offer** — Design an offer so good people feel stupid saying no. Runs Hormozi's full workflow — Dream Outcome through Pricing — and hands you a complete Offer Card ready for a sales page.

```bash
npx skills@latest add Ivcota/skills/grand-slam-offer
```

**$100M Money Models** — Make acquisition self-funding. Chains Attraction → Upsell → Downsell → Continuity offers so 30-day gross profit exceeds CAC — turning credit-card float into client-financed growth.

```bash
npx skills@latest add Ivcota/skills/hundred-million-money-models
```

## Demand

**$100M Leads** — Stop hoping leads find you. Builds a lead engine using the Core Four, lead magnets, and Lead Getters — with the Rule of 100 and advertising compounding model built in.

```bash
npx skills@latest add Ivcota/skills/hundred-million-leads
```

**Breakthrough Advertising** — Write copy that doesn't try to create desire — it channels desire that already exists. Runs Schwartz's full diagnostic (mass desire × awareness state × sophistication stage) before a single word is written.

```bash
npx skills@latest add Ivcota/skills/breakthrough-advertising
```

**Hook Point** — Win the first three seconds. Applies Brendan Kane's framework to sharpen social posts, video openers, subject lines, headlines, ads, and above-the-fold copy.

```bash
npx skills@latest add Ivcota/skills/hook-point
```

**Epiphany Bridge** — Turn an origin story into a conversion story. Walks through Brunson's Backstory → Journey/Conflict → New Opportunity → Framework → Transformation arc and outputs full and 30-second versions.

```bash
npx skills@latest add Ivcota/skills/epiphany-bridge
```

## Authority

**Key Person of Influence** — Become the recognized authority in your industry in twelve months. Runs Priestley & Harrington's five-step sequence — Pitch → Publish → Product → Profile → Partnership — scoring each out of 10 so you fix the foundation before scaling.

```bash
npx skills@latest add Ivcota/skills/key-person-of-influence
```

**Win Friends & Influence People** — Handle people without creating resentment. Applies Dale Carnegie's 30 principles to difficult messages, criticism, feedback, persuasion, networking, and leadership moments.

```bash
npx skills@latest add Ivcota/skills/win-friends-influence-people
```

## Operations

**E-Myth Revisited** — Stop being the bottleneck in your own business. Applies Gerber's Franchise Prototype and seven Business Development strategies to build a system that runs without you.

```bash
npx skills@latest add Ivcota/skills/e-myth-revisited
```

**Theory of Constraints** — Stop optimizing the wrong thing. Runs Goldratt's Five Focusing Steps to find the one constraint limiting your entire system — then prescribes the exact intervention to break it.

```bash
npx skills@latest add Ivcota/skills/theory-of-constraints
```
