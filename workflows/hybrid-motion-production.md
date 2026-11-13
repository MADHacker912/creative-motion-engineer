# Workflow: Hybrid Motion Production Pipeline (Blender + Remotion + FFmpeg)

## 1. Multi-Tool Production Architecture
Modern commercial videos and landing pages rarely rely on a single software package. The highest-converting creative work combines the strengths of 3 specialized engines:

```
┌────────────────────────────────────────────────────────┐
│ 1. 3D ASSET & CAMERAWORK (Blender)                     │
│    └─► PBR product rendering, turntable & alpha frames │
├────────────────────────────────────────────────────────┤
│ 2. COMPOSITION & KINETIC TYPOGRAPHY (Remotion)         │
│    └─► React component timelines, audio sync, springs  │
├────────────────────────────────────────────────────────┤
│ 3. ENCODING & STREAMING MASTERING (FFmpeg)             │
│    └─► Fast-start two-pass MP4, VP9 WebM with alpha   │
└────────────────────────────────────────────────────────┘
```

---

## 2. End-to-End Production Steps

### Step 1: Render 3D Alpha Pass in Blender
Render the product animation with transparent background enabled:
```python
import bpy

scene = bpy.context.scene
scene.render.film_transparent = True
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGBA'
scene.render.filepath = "/tmp/render_frames/frame_"
bpy.ops.render.render(animation=True)
```

### Step 2: Assemble Video in Remotion (React)
Bring the rendered 3D frames into a Remotion `Composition`, layer kinetic typography over it, and synchronize hit points with audio stems:

```tsx
import { AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame } from "remotion";

export const HybridShowcase: React.FC = () => {
  const frame = useCurrentFrame();
  const padIndex = String(frame + 1).padStart(4, "0");

  return (
    <AbsoluteFill style={{ backgroundColor: "#020C1B" }}>
      {/* 3D Rendered Sequence Layer */}
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <Img src={staticFile(`frames/frame_${padIndex}.png`)} style={{ height: "80%" }} />
      </AbsoluteFill>

      {/* Kinetic Typography & Brand Overlay */}
      <Sequence from={30} durationInFrames={90}>
        <h1 style={{ position: "absolute", bottom: 80, left: 100, color: "#64FFDA", fontSize: 64 }}>
          ENGINEERED PERFECTION
        </h1>
      </Sequence>
    </AbsoluteFill>
  );
};
```

### Step 3: Master Encoding with FFmpeg
Encode the final video into high-profile web streaming format:
```bash
ffmpeg -y -i remotion_output.mp4 -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 192k master_delivery.mp4
```
