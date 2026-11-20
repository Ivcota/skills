---
name: storytelling-motion-graphics
description: 'Make story-driven motion graphics as code with Remotion/React, animated Lottie icons, procedural audio/SFX mastered to -14 LUFS, and automated 12-rule QA checks. Use when asked to create an explainer video, motion graphic, product animation, or code-driven video from scratch or alongside blog-post-to-linkedin-video.'
license: MIT
---

# Storytelling Motion Graphics

Make story-driven motion graphics in code (Remotion/React), render frame by frame in headless Chromium, and master audio with `ffmpeg`. Never make a single animated card—every piece is a multi-scene short film with a clear narrative arc.

Before writing code, read the bundled reference docs:
- [references/MOTION_RULES.md](references/MOTION_RULES.md) — 12 blocking QA standards (timing, easing, reading time, safe zones, contrast, transitions, camera, sound sync, flash limits, factual sourcing, asset credits).
- [references/STORYTELLING.md](references/STORYTELLING.md) — beat playbook, camera motion, Lottie and music arc patterns.
- [references/WORKFLOW.md](references/WORKFLOW.md) — end-to-end command sequence using `scripts/` and `assets/template/`.

## Non-negotiable defaults

- Something is on screen from frame 0. The hook shows by 1.5 s, and the brand/promise by 3 s.
- One idea and one focal point per beat.
- Text holds for at least `0.3 s per word + 0.5 s` (minimum `1.2 s`), max `42` characters per line, min `28 px` (`>= 40 px` body).
- Use the shared easing tokens in `src/lib.tsx`. Exits take about `60–70%` of entrance time.
- Every cut uses a named transition in `scenes.json`. Never stack two camera moves at once.
- Contrast `>= 4.5:1` (`3:1` large text); respect `5%` platform safe zones.
- Max `3` large luminance swings (`> 20%`) per second; zero red flashing.
- Master audio to `-14 LUFS` (± 1 LU), true peak `<= -1.0 dBTP`. Land SFX `0–2 frames` before their visual cue.

## 1. Brief

Confirm the message, audience, target platform, duration (`25–40 s` default), aspect ratio (`1920x1080` 16:9, `1080x1080` square, or `1080x1350` / `1080x1920` portrait), and end-frame CTA.

## 2. Script and Storyboard (before code)

Write `SCRIPT.md` and `FACTS.md` inside the project directory:
- 6–8 beats (`hook -> problem -> build -> reveal -> payoff`), each `2.5–7 s`, holding the closing frame `>= 3 s`.
- Track one shared visual motif across every scene so the piece reads as one continuous film.
- Log every on-screen number in `FACTS.md` as `Real` (with source URL), `Derived`, or `Illustrative` (and tag illustrative numbers on screen).

## 3. Scaffold Project

```bash
bash scripts/new.sh ./my-video
```

This copies `assets/template/` (including `src/lib.tsx` with `Camera`, `appear`, `counterValue`, `LottieIcon`, `presentation` transitions, and `sceneStarts`), links dependencies, and initializes `FACTS.md` and `CREDITS.md`.

## 4. Lottie Icons

Fetch MIT line icons (`useAnimations`) or Google Noto animated emoji (`CC BY 4.0`) with automatic credit logging:

```bash
node scripts/fetch_lottie.js ./my-video ua:trendingUp:#22c55e:up noto:1f514:bell
```

- Only recolor line icons (`ua:...`), never emoji.
- Any `noto:` asset requires `"Emoji animations: Animated Noto Emoji by Google, CC BY 4.0"` on delivery.
- Never bundle unauthorized third-party brand logo files—use text wordmarks or clean geometric CSS/SVG marks.

## 5. Audio Synthesis & Mastering

Generate an arc-matched music bed + cut/cue SFX synced to `scenes.json` (and optional `sfx.json`) and mastered to `-14 LUFS` / `-1.5 dBTP`:

```bash
python3 scripts/gen_audio.py ./my-video
```

## 6. Preview, Cut Close-Ups & Fix

```bash
cd ./my-video && npx tsc --noEmit
bash <skill_dir>/scripts/preview.sh ./my-video
```

Inspect `out/contact.png` (1 fps) AND `out/cut*.png` (`0.1 s` strips around every cut). Fix overlapping shared motifs, empty bars waiting for numbers, ghosted text during crossfades, clipped copy, or frozen spans before final render.

## 7. Final Render & Blocking QA

```bash
bash <skill_dir>/scripts/render.sh ./my-video ./my-video.mp4
python3 <skill_dir>/scripts/qa.py ./my-video ./my-video.mp4
```

All 12 checks (`R1`–`R12`) must print `PASS` before delivering the MP4.
