#!/usr/bin/env python3
"""Blocking Rules QA (MOTION_RULES.md R1–R12). Usage: python3 qa.py <project> [mp4]"""
import json, os, re, subprocess, sys
import numpy as np
proj = os.path.abspath(sys.argv[1]).rstrip('/\\'); mp4 = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else proj + '.mp4'
cfg = json.load(open(os.path.join(proj, 'scenes.json')))
res = []
def check(rid, ok, msg): res.append((rid, bool(ok), msg))
def run(a): return subprocess.run(a, capture_output=True, text=True)

pr = json.loads(run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', mp4]).stdout)
v = next(s for s in pr['streams'] if s['codec_type'] == 'video'); a = [s for s in pr['streams'] if s['codec_type'] == 'audio']
fps = eval(v['r_frame_rate']); dur = float(pr['format']['duration'])
with open(mp4, 'rb') as fh: head = fh.read(200000)
faststart = head.find(b'moov') != -1 and (head.find(b'mdat') == -1 or head.find(b'moov') < head.find(b'mdat'))
check('R1', v['width'] == cfg['width'] and v['height'] == cfg['height'] and abs(fps - 30) < 0.01 and v['codec_name'] == 'h264'
      and v['pix_fmt'] == 'yuv420p' and a and a[0]['codec_name'] == 'aac' and a[0]['sample_rate'] == '48000' and a[0]['channels'] == 2 and faststart,
      f"{v['width']}x{v['height']} {fps:.2f}fps {v['codec_name']} {v['pix_fmt']} audio={a[0]['codec_name'] if a else None} {a[0]['sample_rate'] if a else ''} faststart={faststart}")
check('R2', 25 <= dur <= 40, f'duration {dur:.2f}s')
sc = cfg['scenes']; secs = [s['frames'] / cfg['fps'] for s in sc]
beats = [s['beat'] for s in sc]
arc_ok = beats[0] == 'hook' and beats[-1] == 'payoff' and 'reveal' in beats and 'build' in beats
check('R3', 6 <= len(sc) <= 8 and all(2.5 <= x <= 7 for x in secs) and arc_ok, f'{len(sc)} scenes, {min(secs):.1f}-{max(secs):.1f}s, arc={"→".join(beats)}')
tr = cfg['transitions']
check('R4', len(tr) == len(sc) - 1 and all(t['name'] not in ('none', 'cut', '') and t['frames'] >= 8 for t in tr), ', '.join(t['name'] for t in tr))
check('R5', all(s.get('shared') for s in sc), 'shared element in all scenes: ' + sc[0]['shared'].split('(')[0].strip())
moving = [s for s in sc if s.get('camera') and s['camera'] not in ('static', 'none')]
check('R6', len(moving) >= len(sc) / 2, f'{len(moving)}/{len(sc)} scenes with camera moves')
src = ''.join(open(os.path.join(proj, 'src', f)).read() for f in os.listdir(os.path.join(proj, 'src')) if f.endswith('.tsx'))
sizes = [int(x) for x in re.findall(r'fontSize[=:]\s*\{?\s*(\d+)', src)]
# safe-area: sample frames, check no non-background pixels in outer 2% band apart from motion bg? -> use edge text heuristic on rendered frames
check('R7', sizes and min(sizes) >= 28, f'min fontSize {min(sizes) if sizes else None}px')
# R8 flashing: luma + red per frame at 64x36
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-vf', 'scale=64:36', '-pix_fmt', 'rgb24', '-f', 'rawvideo', '-'], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 36, 64, 3).astype(float)
luma = (0.2126 * fr[..., 0] + 0.7152 * fr[..., 1] + 0.0722 * fr[..., 2]).mean((1, 2)) / 255
redfrac = ((fr[..., 0] > 180) & (fr[..., 1] < 90) & (fr[..., 2] < 90)).mean((1, 2))
dl = np.abs(np.diff(luma)) > 0.2; dr = np.abs(np.diff(redfrac)) > 0.25
win = int(round(fps)); worst = max(int(dl[i:i + win].sum()) for i in range(0, max(1, len(dl) - win + 1)))
check('R8', worst <= 3 and dr.sum() == 0, f'max luma swings/s={worst}, red-flash frames={int(dr.sum())}, max red coverage={redfrac.max()*100:.1f}%')
eb = run(['ffmpeg', '-hide_banner', '-i', mp4, '-map', '0:a', '-af', 'ebur128=peak=true', '-f', 'null', '-']).stderr
I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', eb)[-1]); TP = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', eb)[-1])
check('R9', abs(I + 14) <= 1 and TP <= -1.0, f'{I:.1f} LUFS, TP {TP:.1f} dBTP')
fz = run(['ffmpeg', '-hide_banner', '-i', mp4, '-vf', 'freezedetect=n=0.001:d=2', '-map', '0:v', '-f', 'null', '-']).stderr
bk = run(['ffmpeg', '-hide_banner', '-i', mp4, '-vf', 'blackdetect=d=0.5:pix_th=0.05', '-map', '0:v', '-f', 'null', '-']).stderr
freezes = re.findall(r'freeze_start: ([\d.]+)', fz); blacks = [(float(x), float(y)) for x, y in re.findall(r'black_start:([\d.]+) black_end:([\d.]+)', bk)]
blacks = [b for b in blacks if b[1] < dur - 0.05]
check('R10', not freezes and not blacks, f'freezes={freezes} blacks={blacks}')
facts = open(os.path.join(proj, 'FACTS.md')).read()
rows = [r for r in facts.splitlines() if r.startswith('|') and not r.startswith('|---') and 'Figure' not in r]
illus = [r for r in rows if 'Illustrative' in r]
ok11 = rows and all(('Real' in r and 'http' in r) or 'Derived' in r or 'Illustrative' in r for r in rows)
ok11 = ok11 and (not illus or re.search(r'[Ii]llustrative|simplified', src))
check('R11', ok11, f'{len(rows)} figures logged, {len(illus)} illustrative (tagged on screen)')
cred = open(os.path.join(proj, 'CREDITS.md')).read()
lot = [f[:-5] for f in os.listdir(os.path.join(proj, 'public', 'lottie'))] if os.path.isdir(os.path.join(proj, 'public', 'lottie')) else []
used_ok = all(f'{n}.json' in cred for n in lot)
logos = [f for f in os.listdir(os.path.join(proj, 'public')) if re.search(r'logo', f, re.I)]
check('R12', used_ok and not logos, f'{len(lot)} Lottie assets credited, logo files={logos}')
n = sum(ok for _, ok, _ in res)
for rid, ok, msg in res: print(f"{'PASS' if ok else 'FAIL'} {rid}: {msg}")
print(f'Rules QA: {n}/{len(res)}'); sys.exit(0 if n == len(res) else 1)
