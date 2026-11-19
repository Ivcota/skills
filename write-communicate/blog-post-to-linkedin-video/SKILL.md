---
name: blog-post-to-linkedin-video
description: 'Turn a published blog post or article URL into a branded, story-driven 4:5 LinkedIn explainer motion graphic (MP4) and copy-ready LinkedIn caption that points readers back to the article. Use when the user asks to create a LinkedIn video from a blog post, convert articles into social explainer videos, or build a branded motion graphic series from a newsroom or blog.'
license: MIT
---

# Blog Post to LinkedIn Video

Turn any blog post URL into a code-driven, story-first Remotion motion graphic (4:5 portrait, mastered audio, visually QA'd at every cut) plus a LinkedIn post caption that drives traffic back to the article.

## 0. Research the Post & Extract the Brand System

1. Fetch the target blog post URL plus the site root, newsroom or blog index, primary CSS stylesheet, and favicon or Open Graph metadata.
2. Extract:
   - **Content:** core thesis, author byline, publication date, canonical article URL, key comparisons, statistics, timelines, and actionable takeaways.
   - **Brand tokens:** background surface, primary ink, muted ink, primary accent, dark contrast panel color, border color, subtle background grid or motif, display and body fonts, and geometric brand mark or wordmark.
3. Log every claim, figure, date, and source URL in `FACTS.md`.
   - Never invent numbers.
   - Mark estimates (`*2025 is an estimate`) and simplified visual shapes (`path simplified`) directly on screen.
   - Use text wordmarks or clean rebuilt CSS/SVG geometric marks rather than unverified third-party logo files.

## 1. Storyboard a 6–8 Scene Arc (`SCRIPT.md`)

Design a 25–40 s visual narrative built for **muted LinkedIn autoplay**—never a single animated summary card:

1. **Hook (0–5 s):** An immediate concrete stat, tension, or contrast visible within 1.5 s.
2. **Stakes / Noise vs. Signal (4–6 s):** Visual comparison (bars, ratio, split) showing why the topic matters now.
3. **Evidence / Trend (4–6 s):** Animated timeline, chart, or counter driven by verified post numbers.
4. **Why the Old Way Breaks (4–6 s):** Strike-through or contrast on legacy habits (a dark brand panel creates natural mid-film contrast).
5. **The Shift / Mechanism (5–7 s):** The core rule change, technical architecture, or insight from the post.
6. **Actionable Takeaways (5–7 s):** Scannable two-column or card playbook showing what readers can do now.
7. **Payoff & CTA End Frame (5–6 s, >= 3 s hold):** Crisp closing takeaway, author byline, article URL pill (`domain/blog/slug`), publication date, and brand wordmark.

Choose **one shared visual motif** (for example a focus ring, cursor, badge, or connector) that travels through every scene and resolves into the brand mark on the end frame.

## 2. LinkedIn 4:5 Feed Specs & Layout Rules

- **Canvas & encoding:** `1080x1350` (4:5 portrait), `30 fps`, H.264 `yuv420p`, `faststart`, AAC `48 kHz` stereo.
- **Muted-first typography:** Display headlines `60–116 px`, body copy `>= 40 px`, uppercase section labels `>= 28–32 px`, contrast `>= 4.5:1`, max `~12 words` per beat, inside a `5%` safe margin.
- **Motion & camera:** Put subtle continuous camera motion (push, pan, dive-in, pull-back) on at least half the scenes. Animate counters with ease-out and include units and deltas.
- **Icons & fonts:** Prefer MIT-licensed line icons and OFL fonts (such as Google Fonts) to avoid attribution clutter. Log all third-party assets and licenses in `CREDITS.md`, and note any required `CC BY` credit line on delivery.
- **Photosensitivity:** Max 3 large luminance swings (`> 20%`) per second; never flash saturated red (keep negative or alert lines steady).

## 3. Build in Remotion (`TransitionSeries`)

If a local Remotion project already exists, reuse its helper scripts for scaffolding, asset fetch, audio, preview, render, and QA. Otherwise scaffold a Remotion project with `remotion`, `@remotion/transitions`, `@remotion/lottie`, `@remotion/google-fonts`, and `ffmpeg`.

Apply these **cut-polish rules** so transitions feel like one continuous film:

- **Shared motif clearance:** Never let a travelling ring, reticle, or badge hover across incoming headlines, dark bars, or cards during a scene entrance. Either shrink or exit it out of frame before the cut, or fade outgoing text first and glide the motif over open background directly onto its next target.
- **No flat wipes on matching backgrounds:** Avoid horizontal wipes between two scenes with the same surface color (elements shear across static overlays). Prefer directional `slide-up`, `iris`, `clock-wipe`, or clear-first `fade` transitions.
- **Live chart labels:** Animate percentages and labels simultaneously *as* bars grow (for example a live counter inside or beside the bar tip). Never render an empty dark bar waiting 0.5–1 s for its number to appear.
- **Synchronized end frame:** Morph the shared motif into the brand badge while the closing headline enters—never leave a lone badge sitting over an empty frame.

## 4. Audio & Mastering

- Score or generate a music bed matching the emotional arc (for example a tense or minor pulse resolving to major at the solution scene, or a bright editorial groove) plus subtle sound effects `0–2 frames` ahead of cuts and counters.
- Master the muxed MP4 with `ffmpeg` `loudnorm` to **`-14 LUFS` (± 1 LU)** and **true peak `<= -1.0 dBTP`**.

## 5. Preview, Cut Close-Ups & Blocking QA

1. Type-check (`npx tsc --noEmit`) and render a half-scale preview.
2. Generate both:
   - A **1-fps contact sheet** across the whole video (`fps=1`).
   - **`0.1 s` close-up contact strips** around every transition cut (`cut1`, `cut2`, and so on).
3. Inspect the contact sheet and cut strips visually. Fix any motif or text overlap, empty bar frames, crossfade ghosting, clipped copy, or frozen spans longer than `2 s`.
4. Render the final MP4 and run blocking QA checks (`ffprobe` stream format, `ebur128` loudness and true peak, `freezedetect`, black-gap check, luminance flash check, `FACTS.md`, `CREDITS.md`).

## 6. Deliver

1. Provide the final MP4 and a short scene-by-scene breakdown.
2. State QA status, any required attribution lines, and any simplified visuals or estimates.
3. Provide a 2–4 sentence LinkedIn caption grounded strictly in verified facts from the post, with 3 relevant hashtags and the exact link back to the blog article.
