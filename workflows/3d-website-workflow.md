# Workflow: Interactive 3D Website Pipeline

## Overview
The end-to-end process for deploying interactive 3D assets to the web without degrading performance.

```
[1. Asset Pipeline]       ──► Blender modeling, retopology (<50k tris), normal bake, Draco GLB.
[2. Scene Setup]          ──► Three.js / R3F Canvas, HDRI environment lighting, camera rig.
[3. Interaction]          ──► Damped pointer parallax, raycaster model picking, scroll scrub.
[4. Post-Processing]      ──► Selective bloom, chromatic aberration, tone mapping.
[5. Optimization]         ──► Pixel ratio clamping, texture disposal, fallback image creation.
```
