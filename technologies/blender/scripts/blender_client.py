#!/usr/bin/env python3
"""
Universal Blender Client & Bridge CLI
Communicates with a live Blender session via HTTP bridge or automatically falls back
to headless CLI execution when Blender is not actively running.
"""

import sys
import os
import json
import urllib.request
import urllib.error
import subprocess
import argparse
import tempfile
from pathlib import Path

DEFAULT_PORT = 8198
DEFAULT_URL = f"http://127.0.0.1:{DEFAULT_PORT}"
BLENDER_BIN = os.environ.get("BLENDER_BIN") or "/home/obito/.local/bin/blender"

if not os.path.exists(BLENDER_BIN):
    which_bin = subprocess.run(["which", "blender"], capture_output=True, text=True).stdout.strip()
    if which_bin:
        BLENDER_BIN = which_bin

def is_live_bridge_online(base_url=DEFAULT_URL, timeout=1.0):
    """Pings the live Blender bridge server."""
    try:
        req = urllib.request.Request(f"{base_url}/api/status", headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("success", False), data.get("data", {})
    except Exception:
        return False, {}

def send_live_request(endpoint, payload=None, base_url=DEFAULT_URL, timeout=60):
    """Sends a request to the live Blender HTTP server."""
    url = f"{base_url}{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return {"success": False, "error": f"Failed to connect to live Blender bridge: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Error: {str(e)}"}

def execute_headless_script(py_code, extra_args=None):
    """Executes a Python script in Blender headless mode when live server is offline."""
    if not os.path.exists(BLENDER_BIN):
        return {"success": False, "error": f"Blender executable not found at {BLENDER_BIN}."}

    # Inject JSON wrapper to format return value
    wrapped_code = f"""
import sys, json, io, traceback
from contextlib import redirect_stdout, redirect_stderr

stdout_buf = io.StringIO()
stderr_buf = io.StringIO()
success = True
err_msg = None
res_data = None

try:
    with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
        import bpy, mathutils
        globals_dict = {{"bpy": bpy, "mathutils": mathutils, "__name__": "__main__"}}
        locals_dict = {{}}
        exec({json.dumps(py_code)}, globals_dict, globals_dict)
        res_data = {{k: str(v) for k, v in locals_dict.items() if not k.startswith("_")}}
except Exception as e:
    success = False
    err_msg = f"{{type(e).__name__}}: {{str(e)}}\\n{{traceback.format_exc()}}"

out = {{
    "success": success,
    "result": res_data,
    "error": err_msg,
    "stdout": stdout_buf.getvalue(),
    "stderr": stderr_buf.getvalue()
}}
print("___JSON_RESULT_START___")
print(json.dumps(out))
print("___JSON_RESULT_END___")
"""

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(wrapped_code)
        temp_path = f.name

    cmd = [BLENDER_BIN, "--background", "--python", temp_path]
    if extra_args:
        cmd.extend(extra_args)

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        os.remove(temp_path)
        output = proc.stdout
        
        if "___JSON_RESULT_START___" in output and "___JSON_RESULT_END___" in output:
            json_str = output.split("___JSON_RESULT_START___")[1].split("___JSON_RESULT_END___")[0].strip()
            return json.loads(json_str)
        else:
            return {
                "success": proc.returncode == 0,
                "error": proc.stderr if proc.returncode != 0 else None,
                "stdout": proc.stdout
            }
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return {"success": False, "error": f"Headless execution error: {str(e)}"}

# ----------------- CLI ACTIONS -----------------

def cmd_status(args):
    online, data = is_live_bridge_online()
    if online:
        print(f"[✓] Live Blender Bridge is ONLINE at {DEFAULT_URL}")
        print(f"    Blender Version : {data.get('blender_version')}")
        print(f"    Current File    : {data.get('current_file') or 'Unsaved / New'}")
        print(f"    Objects in Scene: {data.get('objects_count')}")
    else:
        print(f"[-] Live Blender Bridge is OFFLINE (Port {DEFAULT_PORT})")
        print(f"    Blender Binary  : {BLENDER_BIN} ({'Found' if os.path.exists(BLENDER_BIN) else 'NOT FOUND'})")
        print("    Autonomous fallback: CLI Headless execution is enabled.")

def cmd_exec(args):
    code = args.code
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            code = f.read()
    if not code:
        print("[!] Error: No code provided. Use -c 'code' or -f file.py")
        sys.exit(1)

    online, _ = is_live_bridge_online()
    if online and not args.force_headless:
        print(f"[*] Executing via LIVE Blender Bridge (Session is interactive)...")
        res = send_live_request("/api/exec", {"code": code})
    else:
        print(f"[*] Executing via Blender HEADLESS CLI...")
        res = execute_headless_script(code)

    if res.get("success"):
        print("[✓] Execution successful!")
        if res.get("stdout"):
            print(f"--- Output ---\n{res['stdout'].strip()}")
        if res.get("result"):
            print(f"--- Result Variables ---\n{json.dumps(res['result'], indent=2)}")
    else:
        print("[!] Execution failed!")
        if res.get("error"):
            print(f"Error: {res['error']}")
        if res.get("stderr"):
            print(f"Stderr: {res['stderr']}")
        sys.exit(1)

def cmd_scene_info(args):
    online, _ = is_live_bridge_online()
    if online:
        res = send_live_request("/api/scene")
    else:
        code = """
objs = []
for obj in bpy.data.objects:
    mat_names = [m.name for m in obj.data.materials] if hasattr(obj.data, "materials") else []
    objs.append({
        "name": obj.name,
        "type": obj.type,
        "location": [round(c, 3) for c in obj.location],
        "materials": mat_names
    })
active_cam = bpy.context.scene.camera.name if bpy.context.scene.camera else None
scene_data = {
    "scene_name": bpy.context.scene.name,
    "active_camera": active_cam,
    "render_engine": bpy.context.scene.render.engine,
    "objects": objs
}
print(json.dumps(scene_data))
"""
        raw = execute_headless_script(code)
        if raw.get("stdout"):
            try:
                res = {"success": True, "result": json.loads(raw["stdout"].strip())}
            except Exception:
                res = raw
        else:
            res = raw

    print(json.dumps(res, indent=2))

def cmd_create_primitive(args):
    code = f"""
import bpy
# Clear existing mesh if requested
prim_type = "{args.type}"
name = "{args.name or 'Object'}"

if prim_type == "cube":
    bpy.ops.mesh.primitive_cube_add(size={args.size}, location=({args.x}, {args.y}, {args.z}))
elif prim_type == "sphere":
    bpy.ops.mesh.primitive_uv_sphere_add(radius={args.size/2}, location=({args.x}, {args.y}, {args.z}))
elif prim_type == "cylinder":
    bpy.ops.mesh.primitive_cylinder_add(radius={args.size/2}, depth={args.size}, location=({args.x}, {args.y}, {args.z}))
elif prim_type == "torus":
    bpy.ops.mesh.primitive_torus_add(major_radius={args.size/2}, minor_radius={args.size/6}, location=({args.x}, {args.y}, {args.z}))

obj = bpy.context.active_object
obj.name = name

# Apply PBR material
mat = bpy.data.materials.new(name=name + "_Material")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")
if bsdf:
    # Color hex conversion
    hex_col = "{args.color}".lstrip("#")
    r, g, b = tuple(int(hex_col[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
    bsdf.inputs["Metallic"].default_value = {args.metallic}
    bsdf.inputs["Roughness"].default_value = {args.roughness}

if obj.data.materials:
    obj.data.materials[0] = mat
else:
    obj.data.materials.append(mat)

print(f"Created {{obj.name}} at {{obj.location}} with PBR material")
"""
    online, _ = is_live_bridge_online()
    if online:
        res = send_live_request("/api/exec", {"code": code})
    else:
        res = execute_headless_script(code)
    print(json.dumps(res, indent=2))

def cmd_export_gltf(args):
    filepath = os.path.abspath(args.output)
    online, _ = is_live_bridge_online()
    if online:
        res = send_live_request("/api/export_gltf", {
            "filepath": filepath,
            "draco": not args.no_draco,
            "selected_only": args.selected
        })
    else:
        code = f"""
import bpy
bpy.ops.export_scene.gltf(
    filepath="{filepath}",
    export_format='GLB',
    use_selection={args.selected},
    export_draco_mesh_compression_enable={not args.no_draco},
    export_draco_mesh_compression_level=7
)
print("Exported GLB to {filepath}")
"""
        res = execute_headless_script(code)
    print(json.dumps(res, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Universal Blender Bridge CLI")
    subparsers = parser.add_subparsers(dest="command")

    # status
    subparsers.add_parser("status", help="Check bridge status")

    # exec
    p_exec = subparsers.add_parser("exec", help="Execute Python code in Blender")
    p_exec.add_argument("-c", "--code", help="Python code string")
    p_exec.add_argument("-f", "--file", help="Python script file")
    p_exec.add_argument("--force-headless", action="store_true", help="Force headless execution even if live is running")

    # scene-info
    subparsers.add_parser("scene-info", help="Get scene metadata and object list")

    # create-primitive
    p_prim = subparsers.add_parser("create-primitive", help="Spawn geometry with PBR material")
    p_prim.add_argument("--type", choices=["cube", "sphere", "cylinder", "torus"], default="cube")
    p_prim.add_argument("--name", default="Geometry")
    p_prim.add_argument("--size", type=float, default=2.0)
    p_prim.add_argument("-x", type=float, default=0.0)
    p_prim.add_argument("-y", type=float, default=0.0)
    p_prim.add_argument("-z", type=float, default=0.0)
    p_prim.add_argument("--color", default="#00F0FF")
    p_prim.add_argument("--metallic", type=float, default=0.9)
    p_prim.add_argument("--roughness", type=float, default=0.15)

    # export-gltf
    p_exp = subparsers.add_parser("export-gltf", help="Export scene to GLB")
    p_exp.add_argument("output", help="Output .glb filepath")
    p_exp.add_argument("--no-draco", action="store_true", help="Disable Draco compression")
    p_exp.add_argument("--selected", action="store_true", help="Export selected objects only")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "status":
        cmd_status(args)
    elif args.command == "exec":
        cmd_exec(args)
    elif args.command == "scene-info":
        cmd_scene_info(args)
    elif args.command == "create-primitive":
        cmd_create_primitive(args)
    elif args.command == "export-gltf":
        cmd_export_gltf(args)

if __name__ == "__main__":
    main()
