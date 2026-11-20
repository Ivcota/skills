# Workflow

0. Facts: research; fill `FACTS.md` (`Real` + URL, or `Illustrative`). Never present invented figures as real.
1. Scaffold project: `<skill_dir>/scripts/new.sh <project_dir>`; edit `src/Story.tsx` + `scenes.json` (beats, durations, transition names, shared element).
2. Assets: `node <skill_dir>/scripts/fetch_lottie.js <project_dir> noto:1f514:bell ua:trendingUp:#22c55e:up` (credits auto-appended to `CREDITS.md`).
3. Audio: `python3 <skill_dir>/scripts/gen_audio.py <project_dir>` (reads `scenes.json` -> `public/audio/mix.wav`, mastered `-14 LUFS` / `-1.5 dBTP`).
4. Preview: `<skill_dir>/scripts/preview.sh <project_dir>` -> low-res `out/preview.mp4` + `out/contact.png` (1 frame/s) + `out/cut-*.png` (0.1 s cut close-ups). Review the sheets: text clipping, overlap, empty frames, pacing. Fix and repeat.
5. Final: `<skill_dir>/scripts/render.sh <project_dir>` -> `<project_dir>.mp4`
6. QA (blocking): `python3 <skill_dir>/scripts/qa.py <project_dir>` — must be `12/12` PASS before delivery.
