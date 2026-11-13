# Workflow: Blender Visual Iteration & Defect Correction Loop

## 1. The Core Philosophy: Execution ≠ Excellence
An autonomous agent must **never** conclude that a 3D scene is finished simply because a Python script executed with `returncode == 0`. 

A script can execute with zero errors while producing:
- A completely pitch-black scene (missing or occluded lights).
- An empty frame (camera pointing into infinity).
- Blown-out clipped white highlights.
- Distorted, plastic-looking materials.
- Floating, detached, or intersecting geometry.

The **Render-Inspect-Correct Visual Feedback Loop** is mandatory for all 3D production.

---

## 2. The 12-Stage Visual Iteration Loop

```
┌────────────────────────────────────────────────────────┐
│ 1. BRIEF & ART DIRECTION                               │
│    └─► Define thesis, materials, lighting & camera     │
├────────────────────────────────────────────────────────┤
│ 2. BLOCKOUT & COMPOSITION                              │
│    └─► Establish primary forms & 2-node camera rig     │
├────────────────────────────────────────────────────────┤
│ 3. FIRST PREVIEW RENDER (Fast Mode: 960x540, 16s)      │
│    └─► Generate rapid visual proof                     │
├────────────────────────────────────────────────────────┤
│ 4. VISUAL INSPECTION (Defect Checklist)               │
│    └─► Evaluate framing, shadow penumbra & contrast    │
├────────────────────────────────────────────────────────┤
│ 5. TARGETED CORRECTIONS                                │
│    └─► Tweak light energies, roughness & bevels        │
├────────────────────────────────────────────────────────┤
│ 6. SECOND PREVIEW & FINAL POLISH                       │
│    └─► Verify fixes; add micro-surface detail          │
├────────────────────────────────────────────────────────┤
│ 7. FINAL MASTER RENDER (1080p / 4K + Denoising)       │
│    └─► Full resolution with color management (AgX)     │
├────────────────────────────────────────────────────────┤
│ 8. QUALITY GATE 1-9 VERIFICATION & DELIVERY            │
└────────────────────────────────────────────────────────┘
```

---

## 3. Visual Defect Detection Checklist

During the inspection step, systematically evaluate:

| Category | Defect Symptom | Technical Remedy |
|---|---|---|
| **Lighting** | Subject appears flat or washed out | Increase contrast ratio; reduce ambient fill; reposition Key light to 45° angle. |
| **Lighting** | Blown-out specular glare destroying surface detail | Increase area light size to soften penumbra; lower specular energy. |
| **Material** | Surface looks cheap, toy-like or plastic | Ensure metalness is strictly `0.0` or `1.0`; add roughness variation via noise/musgrave map. |
| **Material** | Reflections too sharp or mirrored | Increase Principled BSDF roughness from `0.0` to `0.15`–`0.25`. |
| **Geometry** | Visible polygonal faceting or hard polygon edges | Apply smooth shading (`use_auto_smooth = True`) and add a micro-bevel modifier. |
| **Camera** | Extreme distortion on product edges | Increase lens focal length from default 50mm to `85mm` or `100mm`. |
| **Composition**| Subject drifting awkwardly toward edge | Adjust camera tracking Empty location to re-center subject on 1/3 grid intersection. |
| **Scale** | Ground plane floating or objects intersecting | Snap bottom-most bounding box Z-coordinate to `Z = 0.0`. |
