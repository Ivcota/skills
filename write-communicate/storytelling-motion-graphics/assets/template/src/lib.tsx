import React, {useEffect, useState} from 'react';
import {AbsoluteFill, interpolate, Easing, useCurrentFrame, useVideoConfig, staticFile, delayRender, continueRender} from 'remotion';
import {Lottie} from '@remotion/lottie';
import {fade} from '@remotion/transitions/fade';
import {slide} from '@remotion/transitions/slide';
import {wipe} from '@remotion/transitions/wipe';
import {flip} from '@remotion/transitions/flip';
import {iris} from '@remotion/transitions/iris';
import {clockWipe} from '@remotion/transitions/clock-wipe';
import {pushCut} from '@remotion/transitions/push-cut';

export const ease = Easing.bezier(0.22, 1, 0.36, 1);
export const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);

/** Global start frame of each scene given TransitionSeries overlap. */
export const sceneStarts = (cfg: any) => {
  const starts: number[] = []; let t = 0;
  cfg.scenes.forEach((s: any, i: number) => { starts.push(t); t += s.frames - (cfg.transitions[i]?.frames ?? 0); });
  return starts;
};

/** Named transitions (CSS-only, no flashes). */
export const presentation = (name: string, w = 1920, h = 1080): any => {
  switch (name) {
    case 'slide-left': return slide({direction: 'from-right'});
    case 'slide-up': return slide({direction: 'from-bottom'});
    case 'wipe': return wipe({direction: 'from-left'});
    case 'wipe-diag': return wipe({direction: 'from-top-left'});
    case 'flip': return flip({direction: 'from-right'} as any);
    case 'iris': return iris({width: w, height: h});
    case 'clock-wipe': return clockWipe({width: w, height: h});
    case 'push-zoom': return pushCut({flashOpacity: 0, outgoingScale: 1.25, incomingStartScale: 0.85});
    default: return fade();
  }
};

/** Camera: interpolates scale/translate over the local sequence. */
export const Camera: React.FC<{from: [number, number, number]; to: [number, number, number]; children: React.ReactNode; origin?: string}> = ({from, to, children, origin = '50% 50%'}) => {
  const f = useCurrentFrame(); const {durationInFrames} = useVideoConfig();
  const p = interpolate(f, [0, durationInFrames], [0, 1], {extrapolateRight: 'clamp', easing: easeInOut});
  const s = from[0] + (to[0] - from[0]) * p, x = from[1] + (to[1] - from[1]) * p, y = from[2] + (to[2] - from[2]) * p;
  return <AbsoluteFill style={{transform: `translate(${x}px, ${y}px) scale(${s})`, transformOrigin: origin}}>{children}</AbsoluteFill>;
};

export const counterValue = (f: number, start: number, dur: number, a: number, b: number) =>
  interpolate(f, [start, start + dur], [a, b], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});

export const fmt = (v: number, d = 2) => v.toLocaleString('en-US', {minimumFractionDigits: d, maximumFractionDigits: d});

/** Appear: fade + rise, returns style. */
export const appear = (f: number, start: number, dur = 14, dy = 40): React.CSSProperties => {
  const p = interpolate(f, [start, start + dur], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});
  return {opacity: p, transform: `translateY(${(1 - p) * dy}px)`};
};

/** Lottie from public/lottie/<name>.json */
export const LottieIcon: React.FC<{name: string; size: number; loop?: boolean; speed?: number; style?: React.CSSProperties}> = ({name, size, loop = true, speed = 1, style}) => {
  const [data, setData] = useState<any>(null);
  const [handle] = useState(() => delayRender('lottie ' + name));
  useEffect(() => {
    fetch(staticFile(`lottie/${name}.json`)).then(r => r.json()).then(j => { setData(j); continueRender(handle); });
  }, [handle, name]);
  if (!data) return null;
  return <div style={{width: size, height: size, ...style}}><Lottie animationData={data} loop={loop} playbackRate={speed} style={{width: size, height: size}} /></div>;
};
