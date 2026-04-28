# Skills

Agent skills for Claude Code, organized by domain: **Product** (build the thing), **Craft** (sharpen yourself), **Business** (grow the company).

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
- [Craft](#craft)
  - [Thinking](#thinking)
  - [Learning](#learning)
  - [Voice](#voice)
- [Business](#business)
  - [Strategy & idea selection](#strategy--idea-selection)
  - [Customer](#customer)
  - [Offer & pricing](#offer--pricing)
  - [Demand](#demand)
  - [Operations](#operations)

---

# Product & Engineering

*Translate intent into shipped software.*

## Discovery & scoping

**User Story Mapping** — Apply Jeff Patton's User Story Mapping technique to build shared understanding and slice work into outcome-focused releases. Organizes the backlog as a two-dimensional grid (backbone + prioritized tasks) instead of a flat list, keeping the whole story visible while planning incremental delivery.

```bash
npx skills@latest add Ivcota/skills/user-story-mapping
```

## Modeling

**Domain Storytelling** — Interview-driven DDD that maps stakeholder conversations to a domain model and generates pure domain layer code.

```bash
npx skills@latest add Ivcota/skills/domain-storytelling
```

## Delivery

**FAAS** — Four-phase framework for shipping features: Find → ARCH → Automate → Specify-Test-Refine. Uses Responsibility-Driven Design and the 54321 layered architecture model.

```bash
npx skills@latest add Ivcota/skills/faas
```

---

# Craft

*Cross-cutting skills that apply to product and business work alike.*

## Thinking

**Align Mental Model** — Surface wrong beliefs before you act on them. Prediction-check loop with confidence calibration: you predict, rate your confidence, then see the truth — high-confidence-wrongs (the dangerous ones) get why-traced down to the root assumption. Three modes: codebase (verify against code), learning (verify against an authoritative source), planning (split present-reality from future-bets).

```bash
npx skills@latest add Ivcota/skills/align-mental-model
```

**Feynman** — Deep-understand any concept by explaining it simply until all gaps are exposed and filled.

```bash
npx skills@latest add Ivcota/skills/feynman
```

**The ONE Thing** — Narrow focus to extraordinary results using Gary Keller's Focusing Question, Goal Setting to the Now, and Time Blocking. Covers the Six Lies of success, the Three Commitments (Mastery, E→P, Accountability Cycle), and the Four Thieves of productivity.

```bash
npx skills@latest add Ivcota/skills/the-one-thing
```

## Learning

**Bear Hunter System** — Encode complex material with 80-95% retention by building a causal GRINDE map through AIM → SHOOT → SKIN phases.

```bash
npx skills@latest add Ivcota/skills/bear-hunter-system
```

**Distill to Skill** — Turn a book, method, or framework into a Claude Code skill. Fans out citation-grounded sub-agents to extract frameworks, copy patterns, and case studies, then synthesizes against a strict template.

```bash
npx skills@latest add Ivcota/skills/distill-to-skill
```

## Voice

**Style Profile** — Extract a style profile from writing samples and apply it to new content.

```bash
npx skills@latest add Ivcota/skills/style-profile
```

**Style to Skill** — Package an existing `STYLE_PROFILE.md` into a personal, invokable Claude Code skill (like `write-like-me`) so you can apply your voice anywhere without pointing at the source file.

```bash
npx skills@latest add Ivcota/skills/style-to-skill
```

**Humanizer** — Remove signs of AI-generated writing from text. Detects and rewrites 29 patterns (significance inflation, AI vocabulary, em dash overuse, chatbot artifacts, filler phrases, and more). Supports voice calibration from a writing sample.

```bash
npx skills@latest add Ivcota/skills/humanizer
```

---

# Business

*Customer, offer, pricing, distribution, operations.*

## Strategy & idea selection

**Office Hours** — Two modes for pressure-testing ideas: Startup mode asks hard questions, Builder mode helps you think through the details.

```bash
npx skills@latest add Ivcota/skills/office-hours
```

**Zero to One** — Evaluate startup ideas against Peter Thiel's framework: the Contrarian Question, Monopoly vs Competition, Four Characteristics of Monopoly + Last Mover Advantage, Definite Optimism, the Power Law, Secrets, Foundations, Distribution, and the Seven Questions every business must answer.

```bash
npx skills@latest add Ivcota/skills/zero-to-one
```

**Millionaire Fastlane** — Score business ideas and wealth plans against MJ DeMarco's Fastlane framework: the three Roadmaps (Sidewalk, Slowlane, Fastlane), the CENTS / NECST commandments (Control, Entry, Need, Time, Scale), and the Wealth Equation (Net Profit + Asset Value). Distinguishes "Get Rich Quick" (real, process-driven) from "Get Rich Easy" (guru fantasy) and "Get Rich Slow" (40-year wager).

```bash
npx skills@latest add Ivcota/skills/millionaire-fastlane
```

**Good Strategy / Bad Strategy** — Write, diagnose, and audit strategy using Richard Rumelt's Kernel (diagnosis, guiding policy, coherent action), the Four Hallmarks of Bad Strategy, and the Nine Sources of Power.

```bash
npx skills@latest add Ivcota/skills/good-strategy-bad-strategy
```

## Customer

**Validate ICP** — Mine public communities (Reddit, HN, X, IndieHackers, Trustpilot, Discord, forums) for verbatim first-person pain quotes to prove an ICP exists before committing to interviews. Returns source-linked quotes, a named DM list, a reachability scorecard, and a VALIDATED / WEAK / NOT FOUND verdict.

```bash
npx skills@latest add Ivcota/skills/validate-icp
```

**Buyer Profile** — Create deep buyer psychology profiles that uncover real emotional drivers, fears, desires, and motivations behind purchasing decisions.

```bash
npx skills@latest add Ivcota/skills/buyer-profile
```

**Persona to Product** — Turn a buyer persona into ranked product and service ideas grounded in their real problems, failed solutions, and transformation desires.

```bash
npx skills@latest add Ivcota/skills/persona-to-product
```

## Offer & pricing

**Value Equation** — Apply Hormozi's Value Equation as a thinking tool against any artifact — offers, content, features, or ideas. Two modes: Evaluate scores an existing artifact across the four levers (Dream Outcome, Perceived Likelihood, Time Delay, Effort & Sacrifice), finds the weakest lever, and produces a path to 10/10. Create runs a lever-by-lever design interview that saves a brief to `./value-equation-briefs/<slug>.md`.

```bash
npx skills@latest add Ivcota/skills/value-equation
```

**Grand Slam Offer** — Walk through Hormozi's $100M Offers workflow end-to-end to design an offer from scratch: Dream Outcome → Problems → Solutions → Trim & Stack → Bonuses → Guarantee → Scarcity & Urgency → Pricing → Naming. Produces a complete Offer Card (named, priced, bonus-stacked, guaranteed, with scarcity copy) ready to drop into a sales page.

```bash
npx skills@latest add Ivcota/skills/grand-slam-offer
```

**$100M Money Models** — Design a *sequence* of offers — Attraction → Upsell → Downsell → Continuity — so 30-day gross profit per customer exceeds (CAC + cost-to-serve), turning credit-card float into client-financed acquisition. Where `grand-slam-offer` builds one offer, this skill chains five Attraction Offers (Win Your Money Back, Giveaways, Decoy, Buy X Get Y Free, Pay Less Now or Pay More Later), four Upsells (Classic, Menu, Anchor, Rollover), three Downsells (Payment Plan, Trial With Penalty, Feature), and three Continuity types (Bonus, Discount, Waived Fee) into one Money Model with the explicit CFA breakdown.

```bash
npx skills@latest add Ivcota/skills/hundred-million-money-models
```

## Demand

**$100M Leads** — Build a lead generation engine using the Core Four, lead magnets, and Lead Getters. Covers Rule of 100, Hook-Retain-Reward, and the advertising compounding model.

```bash
npx skills@latest add Ivcota/skills/hundred-million-leads
```

## Operations

**E-Myth Revisited** — Build a small business that works without its owner. Applies Michael E. Gerber's Entrepreneur/Manager/Technician model, the Franchise Prototype, and the seven Business Development strategies (Primary Aim, Strategic Objective, Organizational, Management, People, Marketing, Systems).

```bash
npx skills@latest add Ivcota/skills/e-myth-revisited
```

**Theory of Constraints** — Diagnose system bottlenecks and prescribe interventions using Goldratt's Five Focusing Steps (Identify → Exploit → Subordinate → Elevate → Repeat), throughput accounting (T/I/OE), Drum-Buffer-Rope scheduling, and the four constraint types (physical, policy, market, paradigm). Produces a Constraint Diagnosis one-pager with a sequenced exploit→subordinate→elevate plan. Universal lens — works for software flow, sales pipelines, hiring, manufacturing, personal productivity.

```bash
npx skills@latest add Ivcota/skills/theory-of-constraints
```
