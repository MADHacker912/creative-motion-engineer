#!/usr/bin/env python3
"""
CME 2.0 Benchmark C: Animated 3D Brand Reveal - NEXUS IDENTITY
Demonstrates keyframed animation, F-Curve Bezier easing, camera dolly-in,
metallic anisotropic materials, and kinetic logo choreography.
"""

import sys
import os
import math
from pathlib import Path

try:
    import bpy
except ImportError:
    print("[!] Execute inside Blender: blender -b -P build_benchmark_c.py")
    sys.exit(1)

# Add CME core script modules
MODULES_DIR = Path(__file__).resolve().parent.parent.parent / "technologies" / "blender" / "scripts"
sys.path.insert(0, str(MODULES_DIR / "core"))
sys.path.insert(0, str(MODULES_DIR / "presets"))
sys.path.insert(0, str(MODULES_DIR / "quality"))

import scene_manager
import render_manager
import camera_manager
import lighting_manager
import material_manager
import scene_audit

BENCHMARK_DIR = Path(__file__).resolve().parent
BLEND_PATH = BENCHMARK_DIR / "benchmark_c_nexus.blend"
PREVIEW_IMG = BENCHMARK_DIR / "preview_render_c.png"
FINAL_IMG = BENCHMARK_DIR / "final_render_c.png"


def create_nexus_emblem():
    """Builds an interlocking kinetic brand mark using two rotated torus rings and a floating center orb."""
    # Outer Ring
    bpy.ops.mesh.primitive_torus_add(
        major_radius=1.2,
        minor_radius=0.12,
        major_segments=48,
        minor_segments=24,
        location=(0, 0, 1.5)
    )
    ring_a = bpy.context.active_object
    ring_a.name = "Nexus_Ring_A"
    ring_a.rotation_euler = (math.radians(25), math.radians(45), 0)
    bpy.ops.object.shade_smooth()

    # Inner Ring
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.9,
        minor_radius=0.08,
        major_segments=48,
        minor_segments=24,
        location=(0, 0, 1.5)
    )
    ring_b = bpy.context.active_object
    ring_b.name = "Nexus_Ring_B"
    ring_b.rotation_euler = (math.radians(-35), math.radians(-30), 0)
    bpy.ops.object.shade_smooth()

    # Central Core Orb
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32,
        ring_count=16,
        radius=0.35,
        location=(0, 0, 1.5)
    )
    core = bpy.context.active_object
    core.name = "Nexus_Core_Orb"
    bpy.ops.object.shade_smooth()

    # Dark studio base plate
    bpy.ops.mesh.primitive_plane_add(size=20.0, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Nexus_Floor"

    return ring_a, ring_b, core, floor


def animate_nexus(ring_a, ring_b, core):
    """Applies keyframed rotation and scale easing across frames 1 to 90 (24fps = 3.75s)."""
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 90
    scene.render.fps = 24

    # Ring A: 360 degree spin on Z and wobble on X
    ring_a.rotation_euler = (math.radians(25), math.radians(45), 0)
    ring_a.keyframe_insert(data_path="rotation_euler", frame=1)
    ring_a.rotation_euler = (math.radians(25), math.radians(45), math.radians(360))
    ring_a.keyframe_insert(data_path="rotation_euler", frame=90)

    # Ring B: Counter-rotation
    ring_b.rotation_euler = (math.radians(-35), math.radians(-30), 0)
    ring_b.keyframe_insert(data_path="rotation_euler", frame=1)
    ring_b.rotation_euler = (math.radians(-35), math.radians(-30), math.radians(-360))
    ring_b.keyframe_insert(data_path="rotation_euler", frame=90)

    # Core scale pop & settle
    core.scale = (0.01, 0.01, 0.01)
    core.keyframe_insert(data_path="scale", frame=1)
    core.scale = (1.2, 1.2, 1.2)
    core.keyframe_insert(data_path="scale", frame=45)
    core.scale = (1.0, 1.0, 1.0)
    core.keyframe_insert(data_path="scale", frame=90)

    # Make Bezier handles smooth
    for obj in [ring_a, ring_b, core]:
        if obj.animation_data and obj.animation_data.action:
            for fcurve in obj.animation_data.action.fcurves:
                for kf in fcurve.keyframe_points:
                    kf.interpolation = 'BEZIER'
                    kf.handle_left_type = 'AUTO_CLAMPED'
                    kf.handle_right_type = 'AUTO_CLAMPED'


def animate_camera_dolly(cam):
    """Animates camera moving from wide overview to hero showcase frame."""
    cam.location = (0.0, -5.5, 2.2)
    cam.keyframe_insert(data_path="location", frame=1)

    cam.location = (0.0, -3.6, 1.8)
    cam.keyframe_insert(data_path="location", frame=90)

    if cam.animation_data and cam.animation_data.action:
        for fcurve in cam.animation_data.action.fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'BEZIER'
                kf.handle_left_type = 'AUTO_CLAMPED'
                kf.handle_right_type = 'AUTO_CLAMPED'


def build():
    print("=" * 60)
    print("CME 2.0 BENCHMARK C: NEXUS IDENTITY ANIMATED BRAND REVEAL")
    print("=" * 60)

    # 1. Purge & Init Scene
    scene_manager.init_clean_scene()
    scene_manager.set_world_environment(color=(0.008, 0.008, 0.015), strength=0.2)

    # 2. Build Emblem
    ring_a, ring_b, core, floor = create_nexus_emblem()

    # 3. Materials
    mat_chrome = material_manager.create_pbr_material(name="MAT_NexusChrome", base_color=(0.95, 0.95, 0.95, 1.0), metallic=1.0, roughness=0.08)
    mat_gold = material_manager.create_brushed_metal(name="MAT_NexusGold", color=(1.0, 0.78, 0.35, 1.0), roughness=0.18)
    
    # Emissive Core Material
    mat_core = bpy.data.materials.new(name="MAT_NexusCoreEmissive")
    mat_core.use_nodes = True
    c_nodes = mat_core.node_tree.nodes
    c_links = mat_core.node_tree.links
    c_nodes.clear()
    c_out = c_nodes.new(type='ShaderNodeOutputMaterial')
    c_em = c_nodes.new(type='ShaderNodeEmission')
    c_em.inputs['Color'].default_value = (0.4, 0.1, 1.0, 1.0)
    c_em.inputs['Strength'].default_value = 14.0
    c_links.new(c_em.outputs['Emission'], c_out.inputs['Surface'])

    # Matte dark floor
    mat_floor = bpy.data.materials.new(name="MAT_NexusDarkFloor")
    mat_floor.use_nodes = True
    f_nodes = mat_floor.node_tree.nodes
    f_links = mat_floor.node_tree.links
    f_nodes.clear()
    f_out = f_nodes.new(type='ShaderNodeOutputMaterial')
    f_bsdf = f_nodes.new(type='ShaderNodeBsdfPrincipled')
    f_bsdf.inputs['Base Color'].default_value = (0.012, 0.012, 0.016, 1.0)
    f_bsdf.inputs['Roughness'].default_value = 0.25
    f_links.new(f_bsdf.outputs['BSDF'], f_out.inputs['Surface'])

    ring_a.data.materials.append(mat_chrome)
    ring_b.data.materials.append(mat_gold)
    core.data.materials.append(mat_core)
    floor.data.materials.append(mat_floor)

    # 4. Animate Objects
    animate_nexus(ring_a, ring_b, core)

    # 5. Studio Lighting
    lighting_manager.setup_commercial_product_rig(overhead_energy=200.0, key_energy=300.0, rim_energy=450.0)

    # 6. Camera Rig & Dolly
    cam, target = camera_manager.create_tracked_camera(
        name="Nexus_Camera",
        focal_length=60.0,
        location=(0.0, -5.5, 2.2),
        target_location=(0, 0, 1.5),
        f_stop=2.4
    )
    animate_camera_dolly(cam)

    # Set to frame 65 (climax hero frame)
    bpy.context.scene.frame_set(65)

    # 7. Audit Scene
    audit = scene_audit.audit_scene()
    print("[*] Audit Passed:", audit.get('passed', True))

    # 8. Save Blend File
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    print(f"[✓] Saved Blend file: {BLEND_PATH}")

    # 9. Render Preview & Final
    render_manager.configure_render_mode(mode='PREVIEW')
    render_manager.render_to_file(str(PREVIEW_IMG))
    print(f"[✓] Preview render: {PREVIEW_IMG}")

    render_manager.configure_render_mode(mode='FINAL')
    render_manager.render_to_file(str(FINAL_IMG))
    print(f"[✓] Final render: {FINAL_IMG}")

    print("=" * 60)
    print("BENCHMARK C COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    build()
