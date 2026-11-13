# Cinematography & Studio Lighting: Visual Direction & Optics

## 1. Camera Language & Focal Length Selection
The camera lens choices dictate the viewer's psychological relationship with the subject:

| Focal Length | Visual Characteristics | Best Used For |
|---|---|---|
| **24mm – 35mm** | Wide field of view, exaggerated depth perspective, dynamic angles. | Monumental architecture, environmental storytelling, dramatic establishing shots. |
| **50mm** | Neutral human perspective, minimal optical distortion. | Natural editorial portraits, lifestyle scenes. |
| **85mm – 105mm** | Slight telephoto compression, true-to-life geometric proportions. | **Gold standard for luxury product visualization**, jewelry, and watches. |
| **135mm – 200mm** | Extreme compression, background stacks directly behind subject. | Graphic poster compositions, abstract silhouette isolation. |

---

## 2. Professional Camera Rigs in Blender

### 2.1 The Two-Node Orbit & Track Camera Rig
Never animate camera location and rotation independently. Use a targeted rig where the camera is constrained to look at an explicit Empty tracking focus point:

```python
import bpy

def setup_cinematic_camera_rig(target_location=(0, 0, 0.8), focal_length=85.0, f_stop=2.8):
    """Builds a professional 2-node camera rig with automatic focus tracking."""
    # 1. Focus Target Empty
    target = bpy.data.objects.new("Camera_Focus_Target", None)
    target.empty_display_type = 'SPHERE'
    target.empty_display_size = 0.2
    target.location = target_location
    bpy.context.collection.objects.link(target)

    # 2. Camera Object
    cam_data = bpy.data.cameras.new("CinematicCamera_Data")
    cam_data.lens = focal_length
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = target
    cam_data.dof.aperture_fstop = f_stop

    cam_obj = bpy.data.objects.new("CinematicCamera", cam_data)
    cam_obj.location = (2.2, -3.2, 2.0)
    bpy.context.collection.objects.link(cam_obj)

    # 3. Track To Constraint
    track = cam_obj.constraints.new(type='TRACK_TO')
    track.target = target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'

    bpy.context.scene.camera = cam_obj
    return cam_obj, target
```

---

## 3. Studio Lighting Systems & Reflection Management

Lighting creates form through shadow. If every angle is evenly illuminated, the subject becomes visually flat and lifeless.

### 3.1 The 4 Core Commercial Light Configurations
1. **Large Overhead Diffuser (Softbox)**:
   - Area light (`2.5m x 2.5m`) placed directly above the subject.
   - Provides smooth, gradual gradients across curved surfaces and illuminates internal mechanisms.
2. **Vertical Strip Rim Lights**:
   - Long, narrow area light (`0.2m x 3.0m`) placed behind and to the side of the subject.
   - Creates a continuous razor-sharp specular streak that outlines the silhouette from the background.
3. **Contrast Key Light**:
   - Positioned at 45° horizontal and 45° vertical relative to camera line of sight.
   - Dictates the primary shadow direction and volume.
4. **Negative Fill (Black Flags)**:
   - In physical studio photography, black velvet boards are placed opposite the key light to absorb bounce and prevent washed-out shadows. In Blender, simulate this by keeping fill light intensity low or placing non-reflective cards.

```python
import bpy

def create_commercial_studio_lights():
    """Sets up a commercial product lighting rig with key, strip rim, and overhead softbox."""
    # 1. Overhead Softbox
    top_data = bpy.data.lights.new("Overhead_Softbox", 'AREA')
    top_data.energy = 180.0
    top_data.size = 2.0
    top_data.size_y = 2.0
    top = bpy.data.objects.new("Overhead_Softbox", top_data)
    top.location = (0, 0, 3.5)
    bpy.context.collection.objects.link(top)

    # 2. Key Area Light
    key_data = bpy.data.lights.new("Key_Light", 'AREA')
    key_data.energy = 220.0
    key_data.size = 1.2
    key = bpy.data.objects.new("Key_Light", key_data)
    key.location = (2.5, -2.5, 2.0)
    key.rotation_euler = (0.785, 0.35, 0.785)
    bpy.context.collection.objects.link(key)

    # 3. Specular Strip Rim Light
    rim_data = bpy.data.lights.new("Strip_Rim", 'AREA')
    rim_data.energy = 350.0
    rim_data.size = 0.15
    rim_data.size_y = 2.5
    rim = bpy.data.objects.new("Strip_Rim", rim_data)
    rim.location = (-2.8, 1.8, 1.2)
    rim.rotation_euler = (1.57, 0.2, -2.35)
    bpy.context.collection.objects.link(rim)
```
