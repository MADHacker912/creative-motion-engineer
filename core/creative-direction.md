# Creative Direction: Styles, Moodboards, and Storyboards

## 1. Establishing Art Direction

Before generating assets or code, anchor the project in one of these recognized creative styles:

### 1.1 High-End Luxury & Editorial
- **Visual Markers**: Serif display typography (e.g., Ogg, Editorial New, Playfair), vast negative space, thin hairline borders, muted palettes.
- **Motion Dialect**: Slow cinematic easing (`cubic-bezier(0.25, 1, 0.5, 1)`), smooth image parallax, subtle opacity fades, zero elastic bounce.

### 1.2 Cyber-Brutalist & Technical Precision
- **Visual Markers**: Monospace typography, exposed grid coordinates, technical metadata, high-contrast borders, wireframe overlays.
- **Motion Dialect**: Instant or razor-sharp cubic transitions (`cubic-bezier(0.16, 1, 0.3, 1)`), step-based ticker reveals, radar sweeps, CRT scanlines.

### 1.3 Fluid Organic & Atmospheric
- **Visual Markers**: Soft lighting, volumetric shadows, fluid 3D shapes, smooth gradients, frosted layers.
- **Motion Dialect**: Spring-based inertia, liquid morphing transitions, noise-driven displacement, continuous gentle drift.

---

## 2. Storyboarding & Frame-by-Frame Planning

A storyboard ensures that motion sequences have narrative rhythm:

```
┌─────────────────────┬─────────────────────┬─────────────────────┐
│ Frame 01: [0.0s]    │ Frame 02: [1.2s]    │ Frame 03: [2.5s]    │
│                     │                     │                     │
│  [Hero Text Masked] │  [Mask lifts up]    │  [3D Model enters]  │
│  Dark background    │  Hairline rules     │  Camera dollies in  │
│  Ambient light pulse│  fade in            │  CTA uncurls        │
└─────────────────────┴─────────────────────┴─────────────────────┘
```

For every shot, define:
- **Duration**: Total time in seconds or frames.
- **Camera Action**: Static, dolly-in, pan, orbital tilt.
- **Focal Object**: The element carrying the primary animation.
- **Audio Cue**: Transients, risers, impacts, or musical beat drop.
