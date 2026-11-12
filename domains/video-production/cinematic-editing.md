# Cinematic Editing: Rhythm, Cuts, and Visual Momentum

## 1. The Grammar of Editing
- **Hard Cut**: Instant transition between shots. Best for rapid dialogue or sudden changes in perspective.
- **J-Cut**: The audio of the upcoming shot precedes the visual transition by 8–15 frames. Creates natural, subconscious continuity.
- **L-Cut**: The visual changes to the new shot while the audio of the previous shot continues underneath. Excellent for reflective closures.
- **Cutting on Action**: Performing the cut during an active movement (e.g., an arm swinging, a window sliding). The eye tracks the motion and fails to notice the cut boundary.

---

## 2. Remotion Frame-Accurate Sequencing

```tsx
import { Sequence, useCurrentFrame, interpolate } from "remotion";

export const MultiShotScene: React.FC = () => {
  return (
    <>
      {/* Shot 1: Frames 0 to 60 (2.0s @ 30fps) */}
      <Sequence from={0} durationInFrames={60}>
        <IntroTitle />
      </Sequence>

      {/* Shot 2: Frames 60 to 180 (4.0s @ 30fps) */}
      <Sequence from={60} durationInFrames={120}>
        <ProductShowcase />
      </Sequence>

      {/* Shot 3: Frames 180 to 240 (2.0s @ 30fps) */}
      <Sequence from={180} durationInFrames={60}>
        <OutroFinale />
      </Sequence>
    </>
  );
};
```
