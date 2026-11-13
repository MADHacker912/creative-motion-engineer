# Technology: Blender (Headless Scripting & Live Bridge)

## 1. Overview & Operational Philosophy
Blender is the primary 3D modeling, asset generation, and rendering engine in the Creative Motion Engineer pipeline. 

This skill supports two execution modes:
1. **Live Interactive Bridge (`127.0.0.1:8198`)**: Connects directly to an open Blender GUI session via HTTP/JSON-RPC. Allows the agent to inspect the active scene, spawn geometry, tune shaders, and update the 3D viewport live in front of the user!
2. **Autonomous Headless CLI (`blender -b -P`)**: Automatically executed when Blender is not actively open. Operates headlessly to generate procedural models, bake textures, render stills, and export Draco-compressed GLB files.

---

## 2. Directory Structure & Sub-Modules
- `live-bridge.md`: Architectural specifications for the live HTTP bridge and real-time execution.
- `procedural-generation.md`: Advanced Python recipes for parametric meshes, PBR node graphs, and camera keyframes.
- `scripts/blender_bridge_server.py`: The live server that runs inside Blender's modal timer loop.
- `scripts/blender_client.py`: The unified CLI client used by agents and scripts to communicate with Blender.

---

## 3. Quick Start: Controlling Blender

### Check Connection:
```bash
python3 technologies/blender/scripts/blender_client.py status
```

### Run Python in Blender (Live or Headless):
```bash
python3 technologies/blender/scripts/blender_client.py exec -c "import bpy; print(len(bpy.data.objects))"
```

### Inspect Scene Hierarchy:
```bash
python3 technologies/blender/scripts/blender_client.py scene-info
```

### Export Scene to WebGL GLB:
```bash
python3 technologies/blender/scripts/blender_client.py export-gltf output.glb
```

---

## 4. WebGL Export Standards
When preparing assets for Three.js or React Three Fiber:
- **Format**: `.glb` (Binary glTF).
- **Compression**: Enable Draco mesh compression (`export_draco_mesh_compression_enable=True`).
- **Materials**: Strictly use Principled BSDF with PBR metal/roughness workflow.
- **Transforms**: Apply all scale and rotation transforms (`bpy.ops.object.transform_apply()`) prior to export.
