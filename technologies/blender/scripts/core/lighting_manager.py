"""
Lighting Manager Module (CME 2.0 Core)
Commercial product and cinematic studio lighting configurations.
"""

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def setup_commercial_product_rig(overhead_energy=180.0, key_energy=240.0, rim_energy=380.0):
    """
    Sets up a commercial 3-light product studio:
    - Overhead Softbox for smooth global fill & internal highlights
    - Key Area light at 45° for form definition
    - High-intensity narrow Strip Rim light for silhouette separation
    """
    if not IN_BLENDER:
        return {}

    lights = {}

    # 1. Overhead Softbox
    top_data = bpy.data.lights.new("LGT_OverheadSoftbox", 'AREA')
    top_data.energy = overhead_energy
    top_data.size = 2.5
    top_data.size_y = 2.5
    top_data.color = (0.98, 0.99, 1.0)
    top = bpy.data.objects.new("LGT_OverheadSoftbox", top_data)
    top.location = (0, 0, 3.2)
    bpy.context.collection.objects.link(top)
    lights["overhead"] = top

    # 2. Key Light (45° angle)
    key_data = bpy.data.lights.new("LGT_KeyArea", 'AREA')
    key_data.energy = key_energy
    key_data.size = 1.2
    key_data.color = (1.0, 0.98, 0.95)
    key = bpy.data.objects.new("LGT_KeyArea", key_data)
    key.location = (2.2, -2.4, 2.0)
    key.rotation_euler = (0.785, 0.35, 0.785)
    bpy.context.collection.objects.link(key)
    lights["key"] = key

    # 3. Narrow Specular Strip Rim Light
    rim_data = bpy.data.lights.new("LGT_StripRim", 'AREA')
    rim_data.energy = rim_energy
    rim_data.size = 0.12
    rim_data.size_y = 2.8
    rim_data.color = (0.92, 0.96, 1.0)
    rim = bpy.data.objects.new("LGT_StripRim", rim_data)
    rim.location = (-2.6, 2.0, 1.5)
    rim.rotation_euler = (1.57, 0.2, -2.35)
    bpy.context.collection.objects.link(rim)
    lights["rim"] = rim

    return lights

def setup_cinematic_chiaroscuro_rig(key_energy=320.0, rim_energy=200.0):
    """Sets up high-contrast dramatic cinematic lighting with deep shadows."""
    if not IN_BLENDER:
        return {}

    lights = {}
    key_data = bpy.data.lights.new("LGT_CinematicKey", 'SPOT')
    key_data.energy = key_energy
    key_data.spot_size = 0.785  # 45 deg
    key_data.spot_blend = 0.4
    key = bpy.data.objects.new("LGT_CinematicKey", key_data)
    key.location = (-3.0, -2.5, 3.0)
    key.rotation_euler = (0.7, -0.4, -0.6)
    bpy.context.collection.objects.link(key)
    lights["key"] = key

    rim_data = bpy.data.lights.new("LGT_AtmosphericRim", 'AREA')
    rim_data.energy = rim_energy
    rim_data.size = 0.5
    rim = bpy.data.objects.new("LGT_AtmosphericRim", rim_data)
    rim.location = (2.5, 2.5, 1.0)
    rim.rotation_euler = (1.5, 0.0, 2.3)
    bpy.context.collection.objects.link(rim)
    lights["rim"] = rim

    return lights
