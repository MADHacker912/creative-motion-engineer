"""
Studio Product Preset (CME 2.0 Presets)
Instantiates an infinity cove backdrop, commercial lighting, and tracked camera.
"""

import math
try:
    import bpy
    import bmesh
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

import sys
from pathlib import Path

# Add core to sys.path
CORE_DIR = Path(__file__).resolve().parent.parent / "core"
sys.path.insert(0, str(CORE_DIR))

import scene_manager
import lighting_manager
import camera_manager
import render_manager

def build_infinity_backdrop(width=10.0, depth=8.0, height=5.0, bevel_radius=2.0):
    """Builds a seamless curved studio cyclorama / infinity cove."""
    mesh = bpy.data.meshes.new("InfinityBackdrop_Mesh")
    bm = bmesh.new()

    # Create L-shape profile vertices
    v0 = bm.verts.new((-width/2, -depth/2, 0))
    v1 = bm.verts.new((width/2, -depth/2, 0))
    v2 = bm.verts.new((width/2, depth/2, 0))
    v3 = bm.verts.new((-width/2, depth/2, 0))
    v4 = bm.verts.new((width/2, depth/2, height))
    v5 = bm.verts.new((-width/2, depth/2, height))

    # Faces for floor and wall
    bm.faces.new((v0, v1, v2, v3))
    bm.faces.new((v3, v2, v4, v5))

    bm.to_mesh(mesh)
    bm.free()

    cove = bpy.data.objects.new("InfinityBackdrop", mesh)
    bpy.context.collection.objects.link(cove)

    # Add Bevel modifier to curve the back corner
    cove.data.use_auto_smooth = True
    cove.data.auto_smooth_angle = 1.0
    bev = cove.modifiers.new("BackdropCurve", 'BEVEL')
    bev.width = bevel_radius
    bev.segments = 12
    bev.limit_method = 'ANGLE'
    bev.angle_limit = 0.5

    # Satin studio backdrop material
    mat = bpy.data.materials.new(name="StudioBackdrop_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (0.04, 0.045, 0.055, 1.0)
        bsdf.inputs["Roughness"].default_value = 0.45
        bsdf.inputs["Metallic"].default_value = 0.0
    cove.data.materials.append(mat)
    return cove

def setup_studio_product_scene(target_location=(0, 0, 0.6), camera_dist=3.5):
    """Complete one-call studio setup for commercial product rendering."""
    if not IN_BLENDER:
        return False

    scene_manager.init_clean_scene()
    scene_manager.set_world_environment(color=(0.01, 0.01, 0.02), strength=0.2)
    render_manager.configure_render_mode(mode='PREVIEW')

    # Backdrop
    build_infinity_backdrop()

    # Lighting
    lighting_manager.setup_commercial_product_rig()

    # Camera
    cam_x = target_location[0] + camera_dist * 0.7
    cam_y = target_location[1] - camera_dist * 0.9
    cam_z = target_location[2] + camera_dist * 0.45
    camera_manager.create_tracked_camera(
        location=(cam_x, cam_y, cam_z),
        target_location=target_location,
        focal_length=85.0,
        f_stop=2.8
    )
    return True

if __name__ == "__main__":
    setup_studio_product_scene()
    print("[✓] Studio Product scene setup successfully!")
