# Visual Thinking: Composition, Contrast, and Space

## 1. Composition Systems for Dynamic Canvases

Composition is the deliberate arrangement of visual elements within a frame. In motion design, composition is not static—it evolves across time.

### 1.1 The Rule of Thirds & Golden Ratio
- **Rule of Thirds**: Divide the canvas into 3x3 grid sections. Intersections are natural visual anchor points for focal objects.
- **Golden Ratio ($\Phi pprox 1.618$)**: Use logarithmic spirals and proportional splits (62% hero section, 38% auxiliary panel) to create organic balance.

```
┌─────────────────┬──────────┐
│                 │          │
│   Primary Hero  │  Context │
│   Focus Area    │  Data    │
│   (61.8%)       │  (38.2%) │
│                 │          │
└─────────────────┴──────────┘
```

### 1.2 Dynamic Symmetry & Leading Lines
- Use subtle layout guides, diagonal accents, and directional vectors to funnel the viewer's gaze toward the focal trigger.
- When an object enters the screen, its trajectory forms an invisible vector line. Avoid intersecting trajectory vectors that cause eye fatigue.

---

## 2. Negative Space as an Active Visual Tool

Negative space (whitespace) is not empty area—it is visual breathing room that gives weight to the subject:
- **Tension**: As objects move closer together, negative space compresses, creating visual pressure.
- **Release**: Expanding negative space creates a sense of freedom, luxury, and clarity.
- **Isolation**: Placing a compact typography lockup or 3D object in an expansive sea of deep negative space immediately signals high prestige and enterprise confidence.

---

## 3. Visual Hierarchy & Contrast

Hierarchy dictates the sequence of human cognition:
1. **Scale Contrast**: A headline at `clamp(3rem, 7vw, 6.5rem)` paired with metadata at `0.875rem` establishes an unquestionable hierarchy.
2. **Value Contrast**: Lightness contrast between background and foreground must maintain WCAG AA (minimum 4.5:1 for body, 3:1 for large display text).
3. **Color Accents**: 90% of the visual field should be neutral or deep tonal foundations; 10% should be reserved for high-signal action accents (e.g. International Klein Blue, Electric Emerald, or Safety Amber).
4. **Motion Contrast**: An animated object inside a static container commands 100% of the user's attention. If everything moves, nothing is seen.

---

## 4. Depth and Z-Space Staging

Create believable spatial depth on a 2D screen using 4 optical cues:
- **Atmospheric Haze / Contrast Falloff**: Distant layers have lower contrast and softer edge definition.
- **Scale Perspective**: Foreground elements are larger and move faster across the screen than background elements (parallax differential).
- **Occlusion**: Physical layering where foreground objects partially obscure background elements establishes immediate spatial grounding.
- **Depth of Field (DoF)**: In 3D rendering and camera animation, a subtle bokeh blur on out-of-focus planes directs gaze strictly to the focal plane.
