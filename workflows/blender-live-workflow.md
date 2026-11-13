# Workflow: Live Blender Production & Asset Pipeline

## Overview
A complete, 7-step production workflow for autonomous AI agents to build, texture, animate, and export 3D assets using an active or headless Blender session.

```
[1. Environment Detection] ──► Query port 8198 or check system Blender executable.
[2. Bridge Connection]    ──► Connect to Live GUI session or arm CLI headless runner.
[3. Scene Initialization] ──► Clear default primitives; configure metric scale & EEVEE render engine.
[4. Procedural Modeling]  ──► Execute bmesh generation; apply bevels and subdivision surface.
[5. PBR Shader Crafting]  ──► Build Principled BSDF node trees (Metallic, Roughness, Transmission).
[6. Camera & Lighting]    ──► Set up 3-point studio lighting and turntable keyframes.
[7. Draco GLB Export]     ──► Export optimized WebGL assets for Three.js / R3F runtime.
```

---

## Step-by-Step Execution Protocol

### Step 1: Detect Blender Availability
Run `blender_client.py status` to determine whether a live Blender GUI session is active:
```bash
python3 technologies/blender/scripts/blender_client.py status
```
- If **Online**: All commands execute interactively in the open Blender window. The user can watch the 3D viewport update live.
- If **Offline**: Commands automatically route to `/home/obito/.local/bin/blender --background`.

### Step 2: Initialize Scene
Reset unnecessary objects while preserving studio cameras and lights:
```python
import bpy

# Clear mesh objects
for obj in list(bpy.data.objects):
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj, do_unlink=True)
```

### Step 3: Procedural Geometry Generation
Generate the required parametric mesh using `bmesh` or modifier stacks. Ensure quad topology and avoid non-manifold geometry.

### Step 4: Shader & Material Assignment
Construct PBR materials. Dielectrics (`metalness = 0.0`) or conductors (`metalness = 1.0`). Use realistic roughness values (`0.1` to `0.4`).

### Step 5: Optimization & WebGL Export
Export directly to the project's public asset directory:
```bash
python3 technologies/blender/scripts/blender_client.py export-gltf ./public/models/hero_asset.glb
```
