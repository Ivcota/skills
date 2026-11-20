# Motion Rules (blocking QA — `python3 qa.py <project>` must pass n/n)

R1  Format: 1920x1080 (16:9) unless the brief says otherwise, 30 fps, H.264 yuv420p, AAC 48 kHz stereo, faststart.
R2  Duration: 25–40 s for a storytelling piece.
R3  Beats: 6–8 scenes, each 2.5–7 s; arc = hook → problem → build → reveal → payoff (scenes.json).
R4  Transitions: every cut between scenes uses a *named* transition (slide/wipe/iris/clockWipe/flip/fade/zoom); no hard cuts listed in scenes.json.
R5  Shared element: one element (chip, line, shape) visibly travels through every scene (scenes.json `shared` lists it per scene).
R6  Camera: at least half the scenes have camera motion (dive/push/pan) — no static slides.
R7  Text: min font 28 px (body ≥ 40 px); all text inside 5% title-safe margin; max ~12 words on screen per beat.
R8  Photosensitivity: no flashing — automated check: no more than 3 large luminance swings (>20% mean luma) per second, and no saturated-red full-frame flashes. Red elements must be steady (lines, labels), never strobing.
R9  Audio: integrated loudness -14 LUFS ±1 LU, true peak ≤ -1.0 dBTP; music bed under whole piece; SFX on cuts.
R10 No frozen video longer than 2.0 s (ffmpeg freezedetect) and no black gaps > 0.5 s except a final fade.
R11 Facts: every number on screen is listed in FACTS.md as Real (with source URL) or Illustrative; illustrative number screens carry an on-screen "Illustrative" tag.
R12 Credits: every third-party asset (Lottie, music, fonts with attribution terms) listed in CREDITS.md; no third-party brand logo files unless clearly licensed — text wordmarks only.
