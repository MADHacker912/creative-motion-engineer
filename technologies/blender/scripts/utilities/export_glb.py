"""
GLB Export Utility (CME 2.0 Utilities)
Exports clean, Draco-compressed GLB models for WebGL, Three.js, and R3F.
"""

import sys
import os
import argparse
from pathlib import Path

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def export_webgl_glb(filepath, draco=True, selected_only=False):
    """Exports production-ready GLB asset with Draco compression."""
    if not IN_BLENDER:
        print("[!] Must be executed inside Blender: blender -b scene.blend -P export_glb.py -- -o model.glb")
        return False

    out_path = os.path.abspath(filepath)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Apply unapplied transforms to selected/all meshes before export
    bpy.ops.object.select_all(action='SELECT')
    try:
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    except Exception:
        pass

    bpy.ops.export_scene.gltf(
        filepath=out_path,
        export_format='GLB',
        use_selection=selected_only,
        export_draco_mesh_compression_enable=draco,
        export_draco_mesh_compression_level=7
    )
    size_kb = os.path.getsize(out_path) / 1024
    print(f"[✓] GLB Export successful: {out_path} ({size_kb:.1f} KB)")
    return True

def main():
    parser = argparse.ArgumentParser(description="Export GLB Utility")
    parser.add_argument("--output", "-o", default="/tmp/model.glb", help="Output .glb filepath")
    parser.add_argument("--no-draco", action="store_true", help="Disable Draco compression")
    parser.add_argument("--selected", action="store_true", help="Export selected objects only")

    args_list = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    args = parser.parse_args(args_list)

    export_webgl_glb(args.output, draco=not args.no_draco, selected_only=args.selected)

if __name__ == "__main__":
    main()
