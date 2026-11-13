# Advanced 3D Animation Systems: Choreography, Curves & Physics

## 1. Professional Animation Principles in 3D
Inserting two keyframes and leaving default linear or auto-bezier interpolation results in stiff, amateur animation. 

Professional 3D motion requires:
1. **Anticipation & Settling**: Objects compress or pull back slightly before dynamic translation, and settle with micro-damped oscillations upon stopping.
2. **Arc Trajectories**: Rigid linear paths look mechanical. Curved trajectories simulate natural organic mechanics and gravitational momentum.
3. **Staggered Hierarchical Timing**: Sub-components never move simultaneously. Main chassis moves first (frame 0), followed by sub-assemblies (frame 8), followed by delicate dials/accents (frame 16).

---

## 2. Programmatic F-Curve & Easing Manipulation

To give animations intentional, stylized acceleration curves:

```python
import bpy

def set_fcurve_custom_bezier(fcurve, handle_type='AUTO_CLAMPED'):
    """Configures smooth, overshoot-free Bezier handles on an F-Curve."""
    for kp in fcurve.keyframe_points:
        kp.interpolation = 'BEZIER'
        kp.handle_left_type = handle_type
        kp.handle_right_type = handle_type

def animate_exploded_view_part(obj, start_frame, duration, target_offset_z=0.8):
    """Animates a component separating along its local axis with smooth deceleration."""
    end_frame = start_frame + duration
    obj.animation_data_create()
    
    # Initial position
    obj.keyframe_insert(data_path="location", index=2, frame=start_frame)
    
    # Target separated position
    obj.location.z += target_offset_z
    obj.keyframe_insert(data_path="location", index=2, frame=end_frame)
    
    # Adjust F-Curve easing
    action = obj.animation_data.action
    for fc in action.fcurves:
        if fc.data_path == "location" and fc.array_index == 2:
            set_fcurve_custom_bezier(fc, handle_type='AUTO_CLAMPED')
```

---

## 3. Constraint-Driven Camera Choreography

Animate camera motion along an authored 3D curve path while maintaining lock-on focus to the subject:

```python
import bpy

def setup_camera_path_flight(camera_obj, path_curve, target_empty, total_frames=180):
    """Binds camera to a 3D bezier rail while tracking target empty."""
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = total_frames

    # Follow Path constraint
    c_path = camera_obj.constraints.new(type='FOLLOW_PATH')
    c_path.target = path_curve
    c_path.use_curve_follow = True
    c_path.forward_axis = 'FORWARD_Z'
    c_path.up_axis = 'UP_Y'

    # Animate path offset from 0 to 100
    c_path.offset = 0
    c_path.keyframe_insert(data_path="offset", frame=1)
    c_path.offset = -100
    c_path.keyframe_insert(data_path="offset", frame=total_frames)

    # Track target
    c_track = camera_obj.constraints.new(type='TRACK_TO')
    c_track.target = target_empty
    c_track.track_axis = 'TRACK_NEGATIVE_Z'
    c_track.up_axis = 'UP_Y'
```
