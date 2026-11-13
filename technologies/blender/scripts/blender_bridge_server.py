#!/usr/bin/env python3
"""
Live Blender Bridge Server (HTTP & JSON-RPC)
Runs inside Blender to expose a live control API for AI agents and external tools.
Allows real-time scene inspection, procedural object creation, shader tuning,
rendering, and GLTF export directly in an active Blender session.
"""

import sys
import os
import json
import io
import queue
import threading
import traceback
from http.server import HTTPServer, BaseHTTPRequestHandler
from contextlib import redirect_stdout, redirect_stderr

try:
    import bpy
    import mathutils
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8198

task_queue = queue.Queue()
response_queue = queue.Queue()
_server_instance = None

def redraw_all_viewports():
    """Forces all 3D viewports in Blender to immediately refresh on screen."""
    if not IN_BLENDER:
        return
    try:
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()
    except Exception:
        pass

def execute_on_main_thread(action_type, payload):
    """Executes a task inside Blender's main thread with full context access."""
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    res_data = None
    success = True
    err_msg = None

    try:
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            if action_type == "exec":
                code = payload.get("code", "")
                globals_dict = {"bpy": bpy, "mathutils": mathutils, "__name__": "__main__"}
                exec(code, globals_dict, globals_dict)
                res_data = {k: str(v) for k, v in globals_dict.items() if not k.startswith("_") and k not in ("bpy", "mathutils")}
                redraw_all_viewports()

            elif action_type == "eval":
                code = payload.get("code", "")
                val = eval(code, {"bpy": bpy, "mathutils": mathutils})
                res_data = str(val)

            elif action_type == "scene_info":
                objs = []
                for obj in bpy.data.objects:
                    mat_names = [m.name for m in obj.data.materials] if hasattr(obj.data, "materials") else []
                    objs.append({
                        "name": obj.name,
                        "type": obj.type,
                        "location": [round(c, 3) for c in obj.location],
                        "rotation_euler": [round(c, 3) for c in obj.rotation_euler],
                        "scale": [round(c, 3) for c in obj.scale],
                        "visible": obj.visible_get(),
                        "materials": mat_names
                    })
                
                active_cam = bpy.context.scene.camera.name if bpy.context.scene.camera else None
                res_data = {
                    "scene_name": bpy.context.scene.name,
                    "frame_current": bpy.context.scene.frame_current,
                    "frame_start": bpy.context.scene.frame_start,
                    "frame_end": bpy.context.scene.frame_end,
                    "active_camera": active_cam,
                    "render_engine": bpy.context.scene.render.engine,
                    "objects": objs
                }

            elif action_type == "clear_scene":
                keep_camera_and_light = payload.get("keep_camera_and_light", True)
                for obj in list(bpy.data.objects):
                    if keep_camera_and_light and obj.type in {'CAMERA', 'LIGHT'}:
                        continue
                    bpy.data.objects.remove(obj, do_unlink=True)
                for block in bpy.data.meshes:
                    if block.users == 0:
                        bpy.data.meshes.remove(block)
                for block in bpy.data.materials:
                    if block.users == 0:
                        bpy.data.materials.remove(block)
                redraw_all_viewports()
                res_data = {"cleared": True}

            elif action_type == "export_gltf":
                filepath = payload.get("filepath", "/tmp/blender_export.glb")
                os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
                draco = payload.get("draco", True)
                selected = payload.get("selected_only", False)
                bpy.ops.export_scene.gltf(
                    filepath=filepath,
                    export_format='GLB',
                    use_selection=selected,
                    export_draco_mesh_compression_enable=draco,
                    export_draco_mesh_compression_level=7
                )
                res_data = {"exported_path": os.path.abspath(filepath), "size": os.path.getsize(filepath)}

            elif action_type == "render_frame":
                filepath = payload.get("filepath", "/tmp/blender_render.png")
                os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
                bpy.context.scene.render.filepath = filepath
                frame = payload.get("frame", None)
                if frame is not None:
                    bpy.context.scene.frame_set(int(frame))
                bpy.ops.render.render(write_still=True)
                res_data = {"rendered_path": os.path.abspath(filepath), "size": os.path.getsize(filepath)}

            else:
                success = False
                err_msg = f"Unknown action: {action_type}"

    except Exception as e:
        success = False
        err_msg = f"{type(e).__name__}: {str(e)}\n{traceback.format_exc()}"

    return {
        "success": success,
        "result": res_data,
        "error": err_msg,
        "stdout": stdout_buf.getvalue(),
        "stderr": stderr_buf.getvalue()
    }

def process_queue_tick():
    """Processes pending agent commands on Blender's main thread."""
    try:
        while not task_queue.empty():
            req_id, action_type, payload = task_queue.get_nowait()
            result = execute_on_main_thread(action_type, payload)
            response_queue.put((req_id, result))
    except Exception as e:
        print(f"[Blender Bridge Error] {e}")
    return 0.02  # Run every 20ms in GUI mode

class BridgeHTTPHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_OPTIONS(self):
        self._send_json({"status": "ok"})

    def do_GET(self):
        if self.path in ("/", "/status", "/api/status"):
            file_path = None
            objs_count = 0
            if IN_BLENDER:
                try:
                    file_path = bpy.data.filepath
                except Exception:
                    file_path = None
                try:
                    objs_count = len(bpy.data.objects)
                except Exception:
                    objs_count = 0

            info = {
                "status": "online",
                "blender_version": getattr(bpy.app, "version_string", "UNKNOWN") if IN_BLENDER else "NOT_IN_BLENDER",
                "binary_path": getattr(bpy.app, "binary_path", None) if IN_BLENDER else None,
                "current_file": file_path,
                "objects_count": objs_count,
            }
            self._send_json({"success": True, "data": info})
        elif self.path in ("/api/scene", "/scene"):
            res = self._dispatch_to_blender("scene_info", {})
            self._send_json(res)
        else:
            self._send_json({"success": False, "error": f"Endpoint not found: {self.path}"}, 404)

    def do_POST(self):
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = {}

        if self.path == "/api/exec":
            res = self._dispatch_to_blender("exec", payload)
            self._send_json(res)
        elif self.path == "/api/eval":
            res = self._dispatch_to_blender("eval", payload)
            self._send_json(res)
        elif self.path == "/api/clear":
            res = self._dispatch_to_blender("clear_scene", payload)
            self._send_json(res)
        elif self.path == "/api/export_gltf":
            res = self._dispatch_to_blender("export_gltf", payload)
            self._send_json(res)
        elif self.path == "/api/render":
            res = self._dispatch_to_blender("render_frame", payload)
            self._send_json(res)
        else:
            self._send_json({"success": False, "error": f"Unknown POST endpoint: {self.path}"}, 404)

    def _dispatch_to_blender(self, action_type, payload):
        req_id = id(payload)
        task_queue.put((req_id, action_type, payload))
        while True:
            r_id, result = response_queue.get()
            if r_id == req_id:
                return result
            response_queue.put((r_id, result))

    def log_message(self, format, *args):
        return

def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT, keep_alive=False):
    global _server_instance
    if not IN_BLENDER:
        print("[!] ERROR: Run inside Blender: blender -P blender_bridge_server.py")
        sys.exit(1)

    if _server_instance is not None:
        return

    try:
        _server_instance = HTTPServer((host, port), BridgeHTTPHandler)
    except OSError as e:
        print(f"[*] Port {port} in use or bridge already running: {e}")
        return

    server_thread = threading.Thread(target=_server_instance.serve_forever, daemon=True)
    server_thread.start()

    print(f"[✓] Live Blender Bridge Server listening on http://{host}:{port}")
    print(f"[✓] Ready for autonomous agent commands. Blender Version: {bpy.app.version_string}")

    if not bpy.app.background:
        # GUI mode: Register timer with Blender window manager
        if not bpy.app.timers.is_registered(process_queue_tick):
            bpy.app.timers.register(process_queue_tick, persistent=True)
    elif keep_alive:
        # Background dedicated server mode: Keep main thread running
        import time
        try:
            while True:
                time.sleep(0.02)
                process_queue_tick()
        except KeyboardInterrupt:
            print("[*] Blender Bridge Server stopped.")

if __name__ == "__main__":
    start_server(keep_alive=bpy.app.background)
