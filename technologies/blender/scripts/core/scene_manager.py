"""
Scene Manager Module (CME 2.0 Core)
Handles clean scene initialization, unit scale setup, world backgrounds,
and memory/orphan cleanup in Blender.
"""

import sys
try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def init_clean_scene(keep_camera=False, keep_lights=False):
    """Purges default cube and unused data blocks to start from a clean canvas."""
    if not IN_BLENDER:
        return False
    
    # Remove objects
    for obj in list(bpy.data.objects):
        if keep_camera and obj.type == 'CAMERA':
            continue
        if keep_lights and obj.type == 'LIGHT':
            continue
        bpy.data.objects.remove(obj, do_unlink=True)

    # Purge orphan data
    for block in list(bpy.data.meshes):
        if block.users == 0:
            bpy.data.meshes.remove(block)
    for block in list(bpy.data.materials):
        if block.users == 0:
            bpy.data.materials.remove(block)
            
    # Set units to Metric
    scene = bpy.context.scene
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1.0
    scene.unit_settings.length_unit = 'METERS'
    
    # Configure Color Management for modern cinematic look
    if hasattr(scene.view_settings, "view_transform"):
        # Use Filmic or AgX if available
        available_views = [item.identifier for item in scene.view_settings.bl_rna.properties['view_transform'].enum_items]
        if 'AgX' in available_views:
            scene.view_settings.view_transform = 'AgX'
        elif 'Filmic' in available_views:
            scene.view_settings.view_transform = 'Filmic'
    
    scene.view_settings.look = 'High Contrast'
    return True

def set_world_environment(color=(0.02, 0.02, 0.03), strength=0.4):
    """Sets background world ambient color and strength."""
    if not IN_BLENDER:
        return
    world = bpy.context.scene.world
    if not world:
        world = bpy.data.worlds.new("CME_World")
        bpy.context.scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get("Background")
    if bg_node:
        bg_node.inputs["Color"].default_value = (*color, 1.0)
        bg_node.inputs["Strength"].default_value = strength
