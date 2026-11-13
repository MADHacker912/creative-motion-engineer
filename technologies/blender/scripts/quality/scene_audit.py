"""
Scene Audit Module (CME 2.0 Quality Gate)
Systematically diagnoses active Blender scenes for visual, geometric,
and technical defects before rendering or exporting.
"""

import json

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def audit_scene():
    """Runs a complete technical audit and returns a structured findings report."""
    if not IN_BLENDER:
        return {"success": False, "error": "Not running inside Blender"}

    report = {
        "passed": True,
        "warnings": [],
        "errors": [],
        "metrics": {
            "mesh_count": 0,
            "total_faces": 0,
            "light_count": 0,
            "has_camera": False
        }
    }

    # 1. Camera Audit
    cam = bpy.context.scene.camera
    if not cam:
        report["passed"] = False
        report["errors"].append("CRITICAL: No active camera set in scene.")
    else:
        report["metrics"]["has_camera"] = True
        if not cam.data.dof.use_dof:
            report["warnings"].append("Cinematography: Camera Depth of Field is disabled.")

    # 2. Lighting Audit
    lights = [obj for obj in bpy.data.objects if obj.type == 'LIGHT']
    report["metrics"]["light_count"] = len(lights)
    if len(lights) == 0:
        report["passed"] = False
        report["errors"].append("CRITICAL: Zero lights found in scene. Render will be completely black.")
    else:
        for lgt in lights:
            if lgt.data.energy <= 0.0:
                report["warnings"].append(f"Light '{lgt.name}' has 0.0 energy.")

    # 3. Geometry & Mesh Audit
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    report["metrics"]["mesh_count"] = len(meshes)
    total_faces = 0

    for m in meshes:
        f_count = len(m.data.polygons)
        total_faces += f_count

        # Check for unapplied scale
        sx, sy, sz = m.scale
        if abs(sx - 1.0) > 0.001 or abs(sy - 1.0) > 0.001 or abs(sz - 1.0) > 0.001:
            report["warnings"].append(f"Object '{m.name}' has unapplied scale: ({sx:.2f}, {sy:.2f}, {sz:.2f}). Modifiers and bevels may distort.")

        # Check for missing materials
        if len(m.data.materials) == 0:
            report["warnings"].append(f"Object '{m.name}' has no material assigned.")

    report["metrics"]["total_faces"] = total_faces
    if total_faces > 120000:
        report["warnings"].append(f"High polycount ({total_faces:,} faces). May cause slowdown on limited CPU hardware.")

    return report

if __name__ == "__main__":
    result = audit_scene()
    print("--- SCENE AUDIT REPORT ---")
    print(json.dumps(result, indent=2))
