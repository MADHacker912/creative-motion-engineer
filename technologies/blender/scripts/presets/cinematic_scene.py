"""
Cinematic Scene Preset (CME 2.0 Presets)
Instantiates an atmospheric monolithic environment with chiaroscuro lighting.
"""

import sys
from pathlib import Path
try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

CORE_DIR = Path(__file__).resolve().parent.parent / "core"
sys.path.insert(0, str(CORE_DIR))

import scene_manager
import lighting_manager
import camera_manager
import render_manager

def setup_cinematic_environment(target_location=(0, 0, 1.0)):
    """Complete cinematic environment setup with dramatic chiaroscuro contrast."""
    if not IN_BLENDER:
        return False

    scene_manager.init_clean_scene()
    scene_manager.set_world_environment(color=(0.005, 0.008, 0.015), strength=0.1)
    render_manager.configure_render_mode(mode='PREVIEW')

    # Monolithic floor plane
    bpy.ops.mesh.primitive_plane_add(size=25.0, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "CinematicFloor"

    mat = bpy.data.materials.new("ObsidianFloor_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (0.015, 0.018, 0.025, 1.0)
        bsdf.inputs["Metallic"].default_value = 0.8
        bsdf.inputs["Roughness"].default_value = 0.25
    floor.data.materials.append(mat)

    # Lighting
    lighting_manager.setup_cinematic_chiaroscuro_rig(key_energy=350.0, rim_energy=220.0)

    # Camera with dramatic low-angle 35mm lens
    camera_manager.create_tracked_camera(
        location=(3.8, -4.5, 1.4),
        target_location=target_location,
        focal_length=35.0,
        f_stop=1.8,
        name="CinematicCamera"
    )
    return True

if __name__ == "__main__":
    setup_cinematic_environment()
    print("[✓] Cinematic Environment setup complete!")
