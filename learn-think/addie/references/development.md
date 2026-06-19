# Development — Build the Deliverables

> Source: Pastore, R. (2020). *The Instructional Design and Development Process: A 'How To' Guide for Practitioners*. KDP. ISBN 9798651489978.

The phase non-IDs assume is the whole job. Pastore: "Some people believe this development phase is all an ID does. They assume we just develop eLearning. As you can see this is only one part…" (p. 12).

The discipline of this phase: **storyboard before you build, style-guide before you scale, multimedia-principles before you author, alpha/beta-test before you ship.**

## 1. Common Deliverables (§6.0, pp. 71–75)

| Deliverable | What it is | Notes |
|---|---|---|
| **Instructor Guide** | "Cookbook for delivery" — slides + notes + ice breaker + step-by-step | The trainer follows this |
| **Learner Guide** | Slimmed-down instructor guide without the notes | What the learner takes home |
| **Presentations** | Slides — but learn beyond PowerPoint | Keynote, Google Slides, etc. |
| **Computer-Based Training** | Executable + dev files, narration, images, video | Deliver via cloud or LMS |
| **Video** | Recorded lectures, demos, scenarios | Hire pro for narration |
| **Narration** | Voice-over | Text-to-speech still robotic — hire a person |
| **Job Aids** | Quick-reference performance support | Used post-training on the job |
| **Images** | Photos, diagrams, icons | Subscribe to a stock library |

Deliverable matrix by training type (Table 11.0, p. 75) — match deliverables to whether the training is face-to-face, blended, or fully online.

## 2. Storyboarding (§6.1, pp. 76–80)

> "A sample of what our product is going to look like." (p. 76)

**When:** between or during design, just before development.

**Required for:** computer-based training.
**Optional for:** face-to-face only.

### Storyboard as quality checkpoint (p. 77)

> "Think of storyboard as a quality checkpoint."

Get **client sign-off** on storyboards before building anything. This is where you catch design problems while changes are still cheap.

### Paper prototyping (pp. 77–78)

Hand-drawn sketches to brainstorm with the client. Pastore: "you can produce options in 5 minutes." Cheaper than mockups; faster iteration; easier to throw away.

### Storyboard fields (Figure 4.0, p. 79)

| Field | Purpose |
|---|---|
| Title / Name / # | Identifier |
| Files | Asset list (images, audio, video) |
| Mockup of screen | Visual layout |
| Notes for developer | Implementation hints |
| Text / Narration | Exact words on screen + voice-over |
| Navigation and Interactivity | What buttons do, where they go |

### Big tip: storyboard inside your dev tool (p. 80)

> "I do my storyboard in the software I am developing in (this is a big tip)."

When you're both designer and developer, building storyboards in Captivate / Articulate / PowerPoint saves time — the storyboard and the build start to converge.

## 3. Style Guide (§6.2, pp. 81–83)

**Always create one. Even solo.** (p. 82)

> "It is very quick and easy to do." (p. 83)

### Contents

- Fonts (which family, which sizes, which weights)
- Colors (3–5 color family — defined hex/RGB)
- Screen resolution
- Buttons (style, hover state, click state)
- Spacing (margins, padding, line-height)
- Formatting (APA? Chicago?)
- SCORM / metadata standards
- Code comments (if shipping editable source)

### Why solo IDs need this too

Six months later you'll need to edit the course and won't remember what color the headers were. The style guide is the only artifact that survives that gap.

## 4. Software IDs Use (§6.3, Table 12.0, p. 85)

### Authoring

| Tool | Platform | Notes |
|---|---|---|
| **Articulate** | Windows only | Pastore's repeated emphasis: "Articulate and Captivate. Articulate and Captivate. Articulate and Captivate. Articulate and Captivate." |
| **Captivate** | Mac + PC | Cross-platform |
| **PowerPoint** | Mac + PC | Underrated; rapid prototyping |
| **Lectora** | Windows | Enterprise option |

### Video (p. 86)

- **Camtasia** — screen recording + editing
- **Adobe Premiere** — pro editing
- **Final Cut** — Mac pro editing
- **OBS** — free streaming + recording

### Audio (pp. 86–87)

- **Audacity** — preferred (free)
- **Adobe Audition** — pro

### Document (p. 86)

- InDesign, Acrobat, MS Word

### Images (p. 87)

- Photoshop, Illustrator

### LMS (p. 87)

- Moodle, Blackboard, Canvas, plus proprietary
- Pastore: "learn one and the rest are pretty much the same"

### Programming (pp. 87–88)

- HTML, CSS, JavaScript — dabble only; you're not a full-stack dev

## 5. Multimedia Theories (§6.4, pp. 89–91)

### Multimedia (Mayer 2014, p. 89)

> Multimedia = combination of verbal (words/audio) + nonverbal (images, graphs, charts, icons).

**Multimedia principle:** words + images > words alone (Mayer 2014, p. 89).

### Working memory limit (p. 90)

~5 units. (Originally 7 per Miller 1956 — Pastore's update is "~5".)

**Glass-of-water analogy** for cognitive overload (p. 90): keep pouring water into a full glass and the water spills. Pour information into full working memory and the information is lost.

### Pastore's own meta-analysis (p. 92)

(Pastore, Briskin, and Asino, 2016)

~12% improvement in **both** recall AND problem-solving when multimedia is used vs. text alone.

> "This is what IDs are paid to do!" (p. 91)

## 6. Multimedia Development — Mayer's principles (§6.5, Table 13.0, p. 93)

(Adapted from Mayer 2014.)

| Principle | Apply by... |
|---|---|
| **Multimedia** | Combine words + relevant images |
| **Split Attention** | Don't separate text and the image it describes |
| **Modality** | Use narration with on-screen images, not on-screen text |
| **Redundancy** | Don't read on-screen text aloud verbatim |
| **Coherence** | Cut decorative content that doesn't serve learning |
| **Spatial Contiguity** | Place text near the image it describes |
| **Temporal Contiguity** | Sync narration with the visual it describes |
| **Signaling** | Highlight what matters (arrows, color, emphasis) |
| **Interactivity** | Build in clicks, drags, choices |

### Caveat from Pastore (p. 92)

> "Take these with a grain of salt."

Most of Mayer's research was in controlled K-12 / university lab settings. They generally work in real-world IDs but treat them as defaults, not laws.

## 7. Usability Guidelines (§6.6, pp. 95–96)

- Simple, natural dialogue; speak the user's language
- Minimize cognitive load
- Apply multimedia principles
- No busy backgrounds
- Buttons correct size (Fitts' Law — bigger = easier to hit)
- Be consistent
- 2–4 colors max
- Legible fonts
- Organized layout
- Provide feedback (e.g., "page 2 of 20", progress bar)
- Marked exits (clear "back" / "exit" buttons)
- Positive error handling (don't blame the user)
- Develop for the users' actual tech (not your dev machine)
- Rule of thirds for image placement
- Always provide help documentation

## 8. Pilot Testing (§6.7, pp. 97–98)

| Phase | When | What you're catching | Who tests |
|---|---|---|---|
| **Alpha** | Start before signing the contract | Big problems, hardware/LMS compatibility | You + dev team on **client's actual stack** |
| **Beta** | Near completion | Small glitches, broken links, spelling, flow | Real users in small groups; observe them |

### Alpha test priority

Stress-test on the **client's** hardware and LMS, not yours. Pastore's hard rule: do this before signing.

### Beta test priority

Observe users — don't just collect survey data. Watch what they do, where they pause, what they click first.

## 9. Common mistakes

| Mistake | Page | Consequence |
|---|---|---|
| Skipping storyboard sign-off | 77 | Scope creep, full redevelopment |
| Skipping style guide because solo | 82–83 | Can't reverse-engineer your own work in 6 months |
| Text-to-speech for full narration | 73–74 | Sounds robotic; learners disengage |
| Not stress-testing on client hardware | 97 | Course breaks on production LMS |
| Treating "development" as the whole ID job | 12 | Skipping analysis and design |
| Over-using interactivity for its own sake | 96 | Cognitive overload; learners frustrated |
| Decorative content / busy backgrounds | 95 | Violates coherence + signaling principles |
| Reading on-screen text aloud verbatim | 93 | Violates redundancy principle |

## Copy patterns

> "I do my storyboard in the software I am developing in (this is a big tip)." (p. 80)

> "Articulate and Captivate. Articulate and Captivate. Articulate and Captivate. Articulate and Captivate." (p. 85)

> "Think of storyboard as a quality checkpoint." (p. 77)

> "This is what IDs are paid to do!" (p. 91)
