# Live Blender Bridge & Autonomous Agent Integration

## 1. Overview & Architectural Philosophy
The **Live Blender Bridge** connects an AI coding agent directly to an active, interactive Blender session (GUI or headless). 

Unlike traditional static script execution—where Blender boots up, executes, and immediately quits—the Live Bridge allows the agent to:
- **Inspect Live Scenes**: Query existing meshes, materials, collections, cameras, and animation curves in real time.
- **Iterative Procedural Modeling**: Create and modify 3D objects step-by-step while the user observes the 3D viewport update live on screen.
- **Dynamic Shader Construction**: Build and link PBR Principled BSDF node trees interactively.
- **Real-Time Camera Animation**: Tweak camera focal lengths, depths of field, and tracking constraints on the fly.
- **Instant Export**: Trigger GLTF/GLB exports with Draco compression with a single HTTP or CLI call.
- **Autonomous Fallback**: If Blender is not actively open, the client automatically executes tasks via `blender --background` headless mode with identical API semantics.

---

## 2. System Architecture

```
┌─────────────────────────────────┐
│     AI Agent / CLI Client       │
│  (blender_client.py / REST API) │
└────────────────┬────────────────┘
                 │
       [HTTP / JSON-RPC :8198]
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           Live Blender Bridge Server (:8198)            │
│  (scripts/startup/start_agent_bridge.py inside Blender)  │
├─────────────────────────────────────────────────────────┤
│  Thread-Safe Task Queue ──► bpy.app.timers Callback     │
│                                    │                    │
│                                    ▼                    │
│                      [Blender Main UI Thread]           │
│                      - bpy.ops / bpy.data manipulation  │
│                      - Area viewport tag_redraw()       │
│                      - GLTF 2.0 Export / EEVEE Render   │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Communication Endpoints

The bridge server runs by default on `http://127.0.0.1:8198`:

| Method | Endpoint | Description | Payload Example |
|---|---|---|---|
| `GET` | `/status` | Ping server and get Blender version & active file | None |
| `GET` | `/api/scene` | Get comprehensive hierarchy of all objects & materials | None |
| `POST` | `/api/exec` | Execute arbitrary Python code in the live Blender session | `{"code": "bpy.ops.mesh.primitive_cube_add()"}` |
| `POST` | `/api/eval` | Evaluate an expression and return serialized output | `{"code": "len(bpy.data.objects)"}` |
| `POST` | `/api/clear` | Clear mesh objects from the scene | `{"keep_camera_and_light": true}` |
| `POST` | `/api/export_gltf` | Export scene to GLB with Draco compression | `{"filepath": "/path/to/model.glb", "draco": true}` |
| `POST` | `/api/render` | Render the current frame to an image file | `{"filepath": "/path/to/render.png", "frame": 1}` |

---

## 4. Autonomous Client Usage (`blender_client.py`)

The companion client script `technologies/blender/scripts/blender_client.py` auto-detects if the live bridge is reachable. If offline, it seamlessly falls back to headless CLI execution.

### CLI Examples:
```bash
# 1. Check status (detects live session or local binary)
python3 technologies/blender/scripts/blender_client.py status

# 2. Inspect active scene
python3 technologies/blender/scripts/blender_client.py scene-info

# 3. Spawn a metallic primitive with PBR material
python3 technologies/blender/scripts/blender_client.py create-primitive \
  --type torus --name "GlowingRing" --size 2.5 --color "#00F0FF" --metallic 0.95 --roughness 0.1

# 4. Execute a custom Python script
python3 technologies/blender/scripts/blender_client.py exec -f path/to/script.py

# 5. Export scene to WebGL-ready GLB
python3 technologies/blender/scripts/blender_client.py export-gltf ./assets/model.glb
```

---

## 5. Startup Installation in User's Blender

To ensure the bridge server starts automatically whenever the user launches Blender:
```bash
# Copy to Blender startup directory
mkdir -p ~/.config/blender/3.6/scripts/startup/
cp technologies/blender/scripts/blender_bridge_server.py ~/.config/blender/3.6/scripts/startup/start_agent_bridge.py
```
When Blender launches (via GUI or CLI), the message `[✓] Live Blender Bridge Server listening on http://127.0.0.1:8198` will appear in the system console.
