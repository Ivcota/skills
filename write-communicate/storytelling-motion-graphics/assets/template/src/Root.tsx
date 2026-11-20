import React from 'react';
import {Composition} from 'remotion';
import {Story} from './Story';
import scenes from '../scenes.json';
export const totalFrames = () =>
  scenes.scenes.reduce((a: number, s: any) => a + s.frames, 0) -
  scenes.transitions.reduce((a: number, t: any) => a + t.frames, 0);
export const Root: React.FC = () => (
  <Composition id="Story" component={Story} durationInFrames={totalFrames()}
    fps={scenes.fps} width={scenes.width} height={scenes.height} />
);
