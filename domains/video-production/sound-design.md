# Sound Design: Stems, Transients, and Audio-Visual Synchronization

## 1. The 5 Audio Stems of Commercial Video
A professional soundtrack is composed of 5 distinct layers:
1. **Music Bed (Harmonic Core)**: The driving rhythm and melodic emotion.
2. **Voiceover / Narration**: Crisp, centered vocal track (EQ rolled off below 80Hz, gentle compression).
3. **Impacts & Downbeats**: Sub-heavy hits synchronized with primary title reveals or logo appearances.
4. **Whooshes & Risers**: White noise / filtered sweeps that build anticipation leading into cuts or camera dollies.
5. **Foley & UI Clicks**: Delicate high-frequency sounds (1kHz–6kHz) corresponding to button clicks, cursor snaps, and panel expansions.

---

## 2. Remotion Audio Layering & Ducking

```tsx
import { Audio, staticFile, interpolate, useCurrentFrame } from "remotion";

export const AudioMix: React.FC = () => {
  const frame = useCurrentFrame();

  // Duck music volume when voiceover is speaking (frames 45 to 150)
  const musicVolume = interpolate(
    frame,
    [0, 40, 45, 150, 160],
    [0.8, 0.8, 0.25, 0.25, 0.8],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <>
      <Audio src={staticFile("audio/music-bed.mp3")} volume={musicVolume} />
      <Sequence from={45} durationInFrames={105}>
        <Audio src={staticFile("audio/voiceover.mp3")} volume={1.0} />
      </Sequence>
      <Sequence from={35} durationInFrames={30}>
        <Audio src={staticFile("audio/sfx-whoosh.mp3")} volume={0.6} />
      </Sequence>
    </>
  );
};
```
