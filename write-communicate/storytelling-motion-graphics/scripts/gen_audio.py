#!/usr/bin/env python3
"""Generate an original music bed + SFX for a project from scenes.json (+ optional sfx.json).
Usage: python3 gen_audio.py <project>   -> <project>/public/audio/mix.wav  (-14 LUFS, TP <= -1.5 dBTP)
All audio is synthesized here (no third-party samples), so no music credit is needed."""
import json, sys, os, subprocess, re
import numpy as np
from scipy.signal import lfilter, butter, sosfilt
from scipy.io import wavfile

SR = 48000
proj = sys.argv[1]
cfg = json.load(open(os.path.join(proj, 'scenes.json')))
fps = cfg['fps']
starts, t = [], 0
for i, s in enumerate(cfg['scenes']):
    starts.append(t); t += s['frames'] - (cfg['transitions'][i]['frames'] if i < len(cfg['transitions']) else 0)
total_f = t; T = total_f / fps + 0.6
N = int(T * SR)
S = {s['id']: starts[i] / fps for i, s in enumerate(cfg['scenes'])}
ids = [s['id'] for s in cfg['scenes']]
turn = S.get(cfg.get('music', {}).get('turnScene') or '', None)
end_scene = S[ids[-1]]
bpm = cfg.get('music', {}).get('bpm', 112); beat = 60 / bpm
# optional: drive=True -> tense, driving minor (8th bass, 16th hats); invert=True -> minor BEFORE turnScene, major after (tension resolves)
drive = cfg.get('music', {}).get('drive', False); invert = cfg.get('music', {}).get('invert', False)
rng = np.random.default_rng(7)
mus = np.zeros((N, 2)); sfx = np.zeros((N, 2))

def add(buf, start, sig, pan=0.0, gain=1.0):
    i = int(start * SR)
    if i >= N: return
    sig = sig[: N - i] * gain
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[i:i + len(sig), 0] += sig * l * 1.414; buf[i:i + len(sig), 1] += sig * r * 1.414

def tt(d): return np.arange(int(d * SR)) / SR
def midi(n): return 440 * 2 ** ((n - 69) / 12)
def env(d, a=0.01, rel=0.2):
    x = tt(d); e = np.minimum(1, x / max(a, 1e-4)); e *= np.clip((d - x) / max(rel, 1e-4), 0, 1); return e
def lp(sig, fc, order=2): return sosfilt(butter(order, min(fc, SR / 2.2), 'low', fs=SR, output='sos'), sig)
def hp(sig, fc, order=2): return sosfilt(butter(order, fc, 'high', fs=SR, output='sos'), sig)
def bp(sig, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), sig)
def saw(f, d):
    x = tt(d); return 2 * ((x * f) % 1) - 1

# chord tables (midi roots, quality)
MAJ = [(48, [0, 4, 7, 11]), (43, [0, 4, 7, 14]), (45, [0, 3, 7, 10]), (41, [0, 4, 7, 9])]   # Cmaj7 G Am7 F6
MIN = [(45, [0, 3, 7, 10]), (41, [0, 4, 7, 11]), (38, [0, 3, 7, 10]), (40, [0, 4, 7, 10])]  # Am7 Fmaj7 Dm7 E7
END = [(41, [0, 4, 7, 14]), (43, [0, 4, 7, 14]), (48, [0, 4, 7, 11, 14])]                     # F G C(add9)
bar = 4 * beat
drums_in = S[ids[2]] if len(ids) > 2 else 0
tcur, bi = 0.0, 0
while tcur < T - 0.3:
    if tcur >= end_scene: section, prog = 'end', END
    elif invert and (turn is None or tcur < turn): section, prog = 'minor', MIN
    elif not invert and turn is not None and tcur >= turn: section, prog = 'minor', MIN
    else: section, prog = 'major', MAJ
    root, iv = prog[bi % len(prog)] if section != 'end' else END[min(bi % 99, len(END) - 1)]
    d = min(bar, T - tcur)
    # pad
    cut = 1800 if section == 'major' else 900 if section == 'minor' else 1300
    pad = sum(saw(midi(root + 12 + n) * (1 + det), d + 0.4) for n in iv for det in (-0.004, 0.004))
    pad = lp(pad, cut) * env(d + 0.4, 0.25, 0.5) * 0.045
    add(mus, tcur, pad, pan=-0.2); add(mus, tcur, pad, pan=0.2)
    # bass
    nb = 8 if drive and section != 'end' else 4; bstep = 4 * beat / nb
    for b in range(nb):
        if section == 'minor' and not drive and b % 2: continue
        bd = bstep * (0.9 if (section != 'minor' or drive) else 1.9)
        bs = np.sin(2 * np.pi * midi(root - 12) * tt(bd)) * env(bd, 0.005, 0.08 if drive else 0.15)
        add(mus, tcur + b * bstep, lp(bs + 0.3 * np.sign(bs) * bs ** 2, 600), gain=0.22 if not drive else (0.2 if b % 2 == 0 else 0.13))
    # arp plucks (8ths)
    if section != 'end' or True:
        steps = 8 if (section != 'minor' or drive) else 4
        for k in range(steps):
            n = root + 24 + iv[(k * (1 if section == 'major' else 2)) % len(iv)]
            st = tcur + k * bar / steps
            if st >= T - 0.2: break
            pd = 0.35
            x = tt(pd); pl = (np.sin(2 * np.pi * midi(n) * x) + 0.3 * np.sin(4 * np.pi * midi(n) * x)) * np.exp(-x * (9 if section == 'major' else 5))
            g = 0.10 if section == 'major' else 0.08 if section == 'minor' else 0.06
            add(mus, st, pl * env(pd, 0.002, 0.05), pan=0.35 if k % 2 else -0.35, gain=g)
    # drums
    if tcur + 0.01 >= drums_in and section != 'end':
        for b in range(4):
            st = tcur + b * beat
            if section == 'minor' and not drive and b % 2: continue
            x = tt(0.35); k = np.sin(2 * np.pi * np.cumsum(50 + 110 * np.exp(-x * 30)) / SR) * np.exp(-x * 9)
            add(mus, st, k, gain=0.42)
            if section == 'major' or drive:
                for h in ((0, 0.25, 0.5, 0.75) if drive and section == 'minor' else (0, 0.5)):
                    hn = hp(rng.standard_normal(int(0.05 * SR)), 7000) * np.exp(-tt(0.05) * 70)
                    add(mus, st + h * beat, hn, pan=0.25, gain=(0.07 if h else 0.04) if h in (0, 0.5) else 0.03)
                if b in (1, 3):
                    sn = bp(rng.standard_normal(int(0.18 * SR)), 1200, 6000) * np.exp(-tt(0.18) * 22)
                    add(mus, st, sn, gain=0.12)
    tcur += bar; bi += 1
# fade out tail
fo = int(1.2 * SR); mus[-fo:] *= np.linspace(1, 0, fo)[:, None]

# ---------- SFX ----------
def whoosh(d):
    n = rng.standard_normal(int(d * SR)); x = tt(d)
    out = np.zeros_like(n); seg = 1024
    for i in range(0, len(n), seg):
        p = i / len(n); fc = 300 + 5000 * np.sin(np.pi * p) ** 2
        out[i:i + seg] = lp(n[max(0, i - 2048):i + seg], fc)[-len(n[i:i + seg]):]
    return out * np.sin(np.pi * x / d) ** 2
def bell(d=3.0):
    x = tt(d); f0 = 523
    parts = [(1, 1.0, 1.2), (2.0, 0.6, 1.8), (2.76, 0.45, 2.4), (5.4, 0.25, 4), (8.93, 0.12, 6)]
    return sum(a * np.sin(2 * np.pi * f0 * m * x) * np.exp(-x * dk) for m, a, dk in parts) * np.minimum(1, x / 0.003)
def tick():
    x = tt(0.03); return np.sin(2 * np.pi * 2400 * x) * np.exp(-x * 220)
def sweep(f0, f1, d):
    x = tt(d); f = f0 * (f1 / f0) ** (x / d); return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * x / d)
def thud():
    x = tt(0.6); return np.sin(2 * np.pi * np.cumsum(40 + 80 * np.exp(-x * 18)) / SR) * np.exp(-x * 5)

for i, tr in enumerate(cfg['transitions']):
    st = (starts[i + 1]) / fps; d = tr['frames'] / fps
    add(sfx, st - 0.05, whoosh(d + 0.2), pan=(-0.4 if i % 2 else 0.4), gain=0.22)
custom = os.path.join(proj, 'sfx.json')
cues = json.load(open(custom)) if os.path.exists(custom) else []
for c in cues:
    at = S[c['scene']] + c.get('frame', 0) / fps
    kind = c['type']
    if kind == 'bell': add(sfx, at, bell(), gain=c.get('gain', 0.35))
    elif kind == 'ticks':
        dur = c['frames'] / fps; k = 0
        while k * 0.075 < dur:
            p = k * 0.075 / dur; add(sfx, at + k * 0.075, tick(), gain=c.get('gain', 0.12) * (1 - 0.5 * p)); k += 1
    elif kind == 'ding':
        x = tt(1.2); dg = (np.sin(2 * np.pi * 1568 * x) + 0.5 * np.sin(2 * np.pi * 2349 * x)) * np.exp(-x * 4)
        add(sfx, at, dg, gain=c.get('gain', 0.18))
    elif kind == 'riser':
        d = c['frames'] / fps; r = sweep(200, 1400, d) * 0.5 + lp(rng.standard_normal(int(d * SR)), 3000) * np.linspace(0, 0.6, int(d * SR))
        add(sfx, at, r * np.linspace(0, 1, len(r)), gain=c.get('gain', 0.15))
    elif kind == 'drop':
        add(sfx, at, sweep(700, 70, 1.4), gain=c.get('gain', 0.3)); add(sfx, at, thud(), gain=0.45)
    elif kind == 'thud': add(sfx, at, thud(), gain=c.get('gain', 0.4))
    elif kind == 'chime':
        x = tt(2.5); ch = sum(np.sin(2 * np.pi * midi(n) * x) for n in (72, 76, 79, 83)) * np.exp(-x * 1.6) * np.minimum(1, x / 0.01)
        add(sfx, at, ch, gain=c.get('gain', 0.08))

mix = mus * 0.8 + sfx
mix = np.tanh(mix * 0.9) / 0.9
outdir = os.path.join(proj, 'public', 'audio'); os.makedirs(outdir, exist_ok=True)
raw = os.path.join(outdir, 'raw.wav'); wavfile.write(raw, SR, (mix / max(1e-9, np.abs(mix).max()) * 0.8).astype(np.float32))
# two-pass loudnorm
p1 = subprocess.run(['ffmpeg', '-hide_banner', '-i', raw, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(re.search(r'\{[^{}]*"input_i"[^{}]*\}', p1, re.S).group(0))
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
      f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,alimiter=limit=0.82:level=false")
out = os.path.join(outdir, 'mix.wav')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', raw, '-af', af, '-ar', str(SR), '-c:a', 'pcm_s24le', out], check=True)
print('wrote', out, f'{T:.2f}s')
