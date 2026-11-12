# Technology: Remotion (Programmatic Video in React)

## 1. Overview & Mental Model
Remotion turns React components into video frames. Time is measured in **frames**, not milliseconds:
- `useCurrentFrame()`: The current frame index.
- `useVideoConfig()`: Video metadata (`fps`, `durationInFrames`, `width`, `height`).
- `interpolate()`: Linear and clamped property transitions.
- `spring()`: Newtonian physics-based animations.

## 2. Production Composition Example
```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export const TitleCard: React.FC<{ title: string }> = ({ title }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({ frame, fps, config: { damping: 14, stiffness: 120 } });
  const opacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", background: "#050811" }}>
      <h1 style={{ transform: `scale(${scale})`, opacity, color: "#FFFFFF", fontFamily: "sans-serif", fontSize: 80 }}>
        {title}
      </h1>
    </AbsoluteFill>
  );
};
```
