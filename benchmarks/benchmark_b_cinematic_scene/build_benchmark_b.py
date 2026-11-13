#!/usr/bin/env python3
"""
CME 2.0 Benchmark B: Cinematic 3D Scene - KAIROS MONOLITH
Demonstrates brutalist architectural geometry, emissive glyph channels,
obsidian floor with roughness maps, chiaroscuro studio lighting, and 35mm cinematic framing.
"""

import sys
import os
import math
from pathlib import Path

try:
    import bpy
except ImportError:
    print("[!] Execute inside Blender: blender -b -P build_benchmark_b.py")
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
BLEND_PATH = BENCHMARK_DIR / "benchmark_b_kairos.blend"
PREVIEW_IMG = BENCHMARK_DIR / "preview_render_b.png"
FINAL_IMG = BENCHMARK_DIR / "final_render_b.png"


def create_monolith_mesh():
    """Builds a tapered, multi-tier brutalist monolith with chamfered edges."""
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.8))
    monolith = bpy.context.active_object
    monolith.name = "Kairos_Monolith_Core"
    monolith.scale = (0.6, 0.4, 1.8)
    bpy.ops.object.transform_apply(scale=True, location=False, rotation=False)

    # Bevel modifier for micro-surface catches
    bev = monolith.modifiers.new(name="Bevel_Micro", type='BEVEL')
    bev.width = 0.025
    bev.segments = 3
    bev.limit_method = 'ANGLE'
    bev.angle_limit = math.radians(30.0)

    # Weighted normal for flat shaded crisp faces
    wn = monolith.modifiers.new(name="WeightedNormal", type='WEIGHTED_NORMAL')
    wn.keep_sharp = True
    monolith.data.use_auto_smooth = True
    monolith.data.auto_smooth_angle = math.radians(60.0)

    # Accent plinth
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.2, depth=0.15, location=(0, 0, 0.075))
    pedestal = bpy.context.active_object
    pedestal.name = "Kairos_Plinth"
    bpy.ops.object.transform_apply(scale=True, location=False, rotation=False)
    
    p_bev = pedestal.modifiers.new(name="Bevel_Plinth", type='BEVEL')
    p_bev.width = 0.015
    p_bev.segments = 2
    pedestal.data.use_auto_smooth = True

    # Emissive Core Slice
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.8))
    blade = bpy.context.active_object
    blade.name = "Kairos_Emissive_Slice"
    blade.scale = (0.02, 0.42, 1.7)
    bpy.ops.object.transform_apply(scale=True, location=False, rotation=False)

    # Reflective Obsidian Ground
    bpy.ops.mesh.primitive_plane_add(size=30.0, location=(0, 0, 0))
    ground = bpy.context.active_object
    ground.name = "Obsidian_Ground"

    return monolith, pedestal, blade, ground


def create_monolith_material():
    """Dark basalt / titanium composite material with subtle roughness noise."""
    mat = bpy.data.materials.new(name="MAT_DarkBasalt")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.03, 0.035, 0.045, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.65
    bsdf.inputs['Roughness'].default_value = 0.35

    tex_noise = nodes.new(type='ShaderNodeTexNoise')
    tex_noise.inputs['Scale'].default_value = 45.0
    tex_noise.inputs['Detail'].default_value = 4.0
    tex_noise.inputs['Roughness'].default_value = 0.6

    cr = nodes.new(type='ShaderNodeValToRGB')
    cr.color_ramp.elements[0].position = 0.3
    cr.color_ramp.elements[0].color = (0.25, 0.25, 0.25, 1.0)
    cr.color_ramp.elements[1].position = 0.7
    cr.color_ramp.elements[1].color = (0.45, 0.45, 0.45, 1.0)

    bump = nodes.new(type='ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.04
    bump.inputs['Distance'].default_value = 0.01

    links.new(tex_noise.outputs['Fac'], cr.inputs['Fac'])
    links.new(cr.outputs['Color'], bsdf.inputs['Roughness'])
    links.new(tex_noise.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])
    links.new(bsdf.outputs['BSDF'], out_node.inputs['Surface'])

    return mat


def create_emissive_glyph_material():
    """High-contrast cyan/teal emissive core material."""
    mat = bpy.data.materials.new(name="MAT_CyanGlyphEmissive")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out_node = nodes.new(type='ShaderNodeOutputMaterial')
    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs['Color'].default_value = (0.0, 0.85, 1.0, 1.0)
    emission.inputs['Strength'].default_value = 18.0

    links.new(emission.outputs['Emission'], out_node.inputs['Surface'])
    return mat


def create_obsidian_ground_material():
    """Mirror-like dark obsidian with gentle falloff reflection."""
    mat = bpy.data.materials.new(name="MAT_ObsidianGround")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.015, 0.018, 0.022, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.2
    bsdf.inputs['Roughness'].default_value = 0.12
    bsdf.inputs['IOR'].default_value = 1.55

    links.new(bsdf.outputs['BSDF'], out_node.inputs['Surface'])
    return mat


def build():
    print("=" * 60)
    print("CME 2.0 BENCHMARK B: KAIROS MONOLITH CINEMATIC PRODUCTION")
    print("=" * 60)

    # 1. Clean Scene & Set World
    scene_manager.init_clean_scene()
    scene_manager.set_world_environment(color=(0.005, 0.007, 0.012), strength=0.25)

    # 2. Build Geometry
    monolith, pedestal, blade, ground = create_monolith_mesh()

    # 3. Materials
    mat_basalt = create_monolith_material()
    mat_emissive = create_emissive_glyph_material()
    mat_obsidian = create_obsidian_ground_material()

    monolith.data.materials.append(mat_basalt)
    pedestal.data.materials.append(mat_basalt)
    blade.data.materials.append(mat_emissive)
    ground.data.materials.append(mat_obsidian)

    # 4. Cinematic Lighting (Chiaroscuro)
    lighting_manager.setup_cinematic_chiaroscuro_rig(key_energy=350.0, rim_energy=280.0)

    # Add extra cyan rim strip for sci-fi atmosphere
    bpy.ops.object.light_add(type='AREA', location=(-2.5, 3.2, 2.4))
    cyan_strip = bpy.context.active_object
    cyan_strip.name = "LGT_Atmospheric_Cyan"
    cyan_strip.data.energy = 220.0
    cyan_strip.data.color = (0.0, 0.7, 1.0)
    cyan_strip.data.size = 0.3
    cyan_strip.data.size_y = 3.5

    # 5. Cinematic 35mm Low-Angle Camera Rig
    cam, target = camera_manager.create_tracked_camera(
        name="Kairos_CinematicCam",
        focal_length=35.0,
        location=(2.8, -4.2, 1.1),
        target_location=(0, 0, 1.8),
        f_stop=2.8
    )

    # 6. Audit Scene Quality
    audit_results = scene_audit.audit_scene()
    print("[*] Audit Passed:", audit_results.get('passed', True))

    # 7. Save Blend File
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    print(f"[✓] Saved Blend file to: {BLEND_PATH}")

    # 8. Render Preview & Final
    render_manager.configure_render_mode(mode='PREVIEW')
    render_manager.render_to_file(str(PREVIEW_IMG))
    print(f"[✓] Preview render: {PREVIEW_IMG}")

    render_manager.configure_render_mode(mode='FINAL')
    render_manager.render_to_file(str(FINAL_IMG))
    print(f"[✓] Final render: {FINAL_IMG}")

    print("=" * 60)
    print("BENCHMARK B COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    build()
