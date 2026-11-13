#!/usr/bin/env python3
"""
Live Blender Interactive Demonstration Script
Tests connection to live Blender (or automatic headless fallback),
spawns a procedural glowing torus ring, and exports to WebGL GLB.
"""

import sys
import os
from pathlib import Path

# Add technologies/blender/scripts to python path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "technologies" / "blender" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import blender_client

def main():
    print("=" * 60)
    print("CREATIVE MOTION ENGINEER: LIVE BLENDER DEMO")
    print("=" * 60)

    # 1. Check status
    online, data = blender_client.is_live_bridge_online()
    if online:
        print(f"[✓] Connected to LIVE Blender GUI Session (v{data.get('blender_version')})")
    else:
        print("[*] Live bridge offline — running via automated Headless CLI mode.")

    # 2. Execute procedural script
    gem_script = Path(__file__).parent / "procedural_gem.py"
    with open(gem_script, "r", encoding="utf-8") as f:
        code = f.read()

    print("[*] Generating Procedural Emerald Gem in Blender...")
    if online:
        res = blender_client.send_live_request("/api/exec", {"code": code})
    else:
        res = blender_client.execute_headless_script(code)

    if res.get("success"):
        print("[✓] Mesh, Material, and Turntable Keyframes created successfully!")
        if res.get("stdout"):
            print(res["stdout"].strip())
    else:
        print(f"[!] Error: {res.get('error')}")
        sys.exit(1)

    # 3. Export to WebGL GLB
    output_glb = "/tmp/procedural_emerald.glb"
    print(f"[*] Exporting WebGL GLTF (Draco compressed) to {output_glb}...")
    if online:
        exp_res = blender_client.send_live_request("/api/export_gltf", {"filepath": output_glb, "draco": True})
    else:
        exp_code = f"""
import bpy
bpy.ops.export_scene.gltf(
    filepath="{output_glb}",
    export_format='GLB',
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=7
)
print("Export complete!")
"""
        exp_res = blender_client.execute_headless_script(exp_code)

    if exp_res.get("success") and os.path.exists(output_glb):
        size_kb = os.path.getsize(output_glb) / 1024
        print(f"[✓] SUCCESS! Exported GLB Model ({size_kb:.1f} KB): {output_glb}")
    else:
        print(f"[!] Export failed: {exp_res.get('error')}")

if __name__ == "__main__":
    main()
