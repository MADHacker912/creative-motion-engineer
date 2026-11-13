#!/usr/bin/env python3
"""
Benchmark A: Premium Product Visualization — "AURA-01" Luxury Audio Controller
Builds multi-material precision geometry (Brushed Titanium, Smoked Glass, Chrome),
curved infinity cove studio, 3-point lighting rig, 85mm telephoto camera,
executes Preview & Final renders, and saves the .blend file.
"""

import sys
import os
import math
from pathlib import Path

try:
    import bpy
    import bmesh
except ImportError:
    print("[!] Execute inside Blender: blender -b -P build_benchmark_a.py")
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
import studio_product
import scene_audit

BENCHMARK_DIR = Path(__file__).resolve().parent
BLEND_PATH = BENCHMARK_DIR / "benchmark_a_aura01.blend"
PREVIEW_IMG = BENCHMARK_DIR / "preview_render_a.png"
FINAL_IMG = BENCHMARK_DIR / "final_render_a.png"

def build():
    print("[*] Initializing Benchmark A: AURA-01 Luxury Audio Dial...")
    scene_manager.init_clean_scene()
    scene_manager.set_world_environment(color=(0.015, 0.018, 0.025), strength=0.3)
    
    # 1. Infinity Studio Backdrop
    studio_product.build_infinity_backdrop(width=12.0, depth=10.0, height=6.0, bevel_radius=2.5)

    # 2. Outer Knurled Bezel (Precision Cylinder with Bevel & Weighted Normal)
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=1.6, depth=0.55, location=(0, 0, 0.275))
    bezel = bpy.context.active_object
    bezel.name = "AURA01_Bezel"
    bezel.data.use_auto_smooth = True
    bezel.data.auto_smooth_angle = math.radians(35)
    
    bev = bezel.modifiers.new("Bevel", 'BEVEL')
    bev.width = 0.04
    bev.segments = 2
    bev.limit_method = 'ANGLE'
    bev.angle_limit = math.radians(30)
    bev.harden_normals = True
    
    wn = bezel.modifiers.new("WeightedNormals", 'WEIGHTED_NORMAL')
    wn.mode = 'FACE_AREA_WITH_ANGLE'
    
    mat_titanium = material_manager.create_brushed_metal("Black_Titanium", color=(0.12, 0.13, 0.15, 1.0), roughness=0.22)
    material_manager.assign_material(bezel, mat_titanium)

    # 3. Inner Step Ring (Polished Chrome)
    bpy.ops.mesh.primitive_cylinder_add(vertices=36, radius=1.35, depth=0.2, location=(0, 0, 0.6))
    step_ring = bpy.context.active_object
    step_ring.name = "AURA01_StepRing"
    step_ring.data.use_auto_smooth = True
    bev2 = step_ring.modifiers.new("Bevel", 'BEVEL')
    bev2.width = 0.02
    bev2.segments = 2
    mat_chrome = material_manager.create_pbr_material("Polished_Chrome", base_color=(0.95, 0.95, 0.95, 1.0), metallic=1.0, roughness=0.04)
    material_manager.assign_material(step_ring, mat_chrome)

    # 4. Central Convex Cap (High-Gloss Smoked Glass Dial)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=1.1, location=(0, 0, 0.55))
    glass_cap = bpy.context.active_object
    glass_cap.name = "AURA01_GlassCap"
    glass_cap.scale = (1.0, 1.0, 0.35)
    bpy.ops.object.transform_apply(scale=True)
    glass_cap.data.use_auto_smooth = True
    
    mat_glass = material_manager.create_optical_glass("Smoked_Optical_Glass", ior=1.54, tint=(0.08, 0.1, 0.12, 1.0))
    material_manager.assign_material(glass_cap, mat_glass)

    # 5. Studio Lighting Setup
    lighting_manager.setup_commercial_product_rig(overhead_energy=220.0, key_energy=280.0, rim_energy=450.0)

    # 6. Cinematography: 85mm Telephoto Camera with Depth of Field
    cam_obj, target_empty = camera_manager.create_tracked_camera(
        location=(2.8, -3.4, 2.2),
        target_location=(0, 0, 0.55),
        focal_length=85.0,
        f_stop=3.2
    )

    # 7. Audit Scene
    print("[*] Running Scene Diagnostic Audit...")
    report = scene_audit.audit_scene()
    print("Audit status passed:", report["passed"])
    if report["errors"]:
        print("Audit errors:", report["errors"])
    if report["warnings"]:
        print("Audit warnings:", report["warnings"])

    # 8. Save .blend file
    bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_PATH))
    print(f"[✓] Saved project: {BLEND_PATH}")

    # 9. Fast Preview Render (qHD 960x540)
    print(f"[*] Rendering Preview Mode to {PREVIEW_IMG}...")
    render_manager.configure_render_mode(mode='PREVIEW', engine='BLENDER_EEVEE')
    render_manager.render_to_file(str(PREVIEW_IMG))
    print(f"[✓] Preview render complete: {PREVIEW_IMG} ({os.path.getsize(PREVIEW_IMG):,} bytes)")

    # 10. Final Master Render (1080p Full HD)
    print(f"[*] Rendering Final Master Mode to {FINAL_IMG}...")
    render_manager.configure_render_mode(mode='FINAL', engine='BLENDER_EEVEE')
    render_manager.render_to_file(str(FINAL_IMG))
    print(f"[✓] Final master render complete: {FINAL_IMG} ({os.path.getsize(FINAL_IMG):,} bytes)")

if __name__ == "__main__":
    build()
