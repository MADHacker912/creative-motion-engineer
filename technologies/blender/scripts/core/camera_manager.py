"""
Camera Manager Module (CME 2.0 Core)
Builds professional 2-node camera rigs with target tracking and depth-of-field.
"""

try:
    import bpy
    import math
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def create_tracked_camera(
    location=(2.5, -3.2, 1.8),
    target_location=(0.0, 0.0, 0.6),
    focal_length=85.0,
    f_stop=2.8,
    name="CinematicCamera"
):
    """
    Creates a commercial 2-node camera rig:
    - Target Empty at target_location
    - Perspective camera constrained with TRACK_TO
    - Depth of Field enabled and linked to the target empty
    """
    if not IN_BLENDER:
        return None, None

    # 1. Target Empty
    target = bpy.data.objects.new(name + "_Target", None)
    target.empty_display_type = 'SPHERE'
    target.empty_display_size = 0.15
    target.location = target_location
    bpy.context.collection.objects.link(target)

    # 2. Camera
    cam_data = bpy.data.cameras.new(name + "_Data")
    cam_data.lens = focal_length
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = target
    cam_data.dof.aperture_fstop = f_stop

    cam_obj = bpy.data.objects.new(name, cam_data)
    cam_obj.location = location
    bpy.context.collection.objects.link(cam_obj)

    # 3. Track To Constraint
    track = cam_obj.constraints.new(type='TRACK_TO')
    track.target = target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'

    bpy.context.scene.camera = cam_obj
    return cam_obj, target
