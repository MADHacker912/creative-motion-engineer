"""
Render Manager Module (CME 2.0 Core)
Configures rendering engines, resolution, and sampling profiles.
Specifically tuned for low-hardware awareness (e.g. ThinkPad T420 / Intel Core i3).
"""

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def configure_render_mode(mode='PREVIEW', engine='BLENDER_EEVEE'):
    """
    Sets up hardware-conscious rendering settings.
    mode: 'PREVIEW' (Fast, low-res, low-sample) or 'FINAL' (1080p, refined)
    engine: 'BLENDER_EEVEE' (Default, fast) or 'CYCLES' (Photoreal raytracing)
    """
    if not IN_BLENDER:
        return False

    scene = bpy.context.scene
    scene.render.engine = engine

    if mode == 'PREVIEW':
        # Fast iteration profile (< 10s on low-spec hardware)
        scene.render.resolution_x = 960
        scene.render.resolution_y = 540
        scene.render.resolution_percentage = 100

        if engine == 'BLENDER_EEVEE':
            scene.eevee.taa_render_samples = 16
            scene.eevee.use_gtao = True
            scene.eevee.use_bloom = True
            scene.eevee.use_ssr = True  # Screen Space Reflections
            scene.eevee.use_ssr_refraction = True
        elif engine == 'CYCLES':
            scene.cycles.device = 'CPU'
            scene.cycles.samples = 24
            scene.cycles.preview_samples = 12
            scene.cycles.use_denoising = True

    elif mode == 'FINAL':
        # High quality production profile (1080p Full HD)
        scene.render.resolution_x = 1920
        scene.render.resolution_y = 1080
        scene.render.resolution_percentage = 100

        if engine == 'BLENDER_EEVEE':
            scene.eevee.taa_render_samples = 64
            scene.eevee.use_gtao = True
            scene.eevee.use_bloom = True
            scene.eevee.use_ssr = True
            scene.eevee.use_ssr_refraction = True
            scene.eevee.shadow_cube_size = '1024'
            scene.eevee.shadow_cascade_size = '1024'
        elif engine == 'CYCLES':
            scene.cycles.device = 'CPU'
            scene.cycles.samples = 64
            scene.cycles.use_denoising = True

    return True

def render_to_file(filepath, frame=None):
    """Executes render and saves still to disk."""
    if not IN_BLENDER:
        return False
    scene = bpy.context.scene
    scene.render.filepath = filepath
    if frame is not None:
        scene.frame_set(int(frame))
    bpy.ops.render.render(write_still=True)
    return True
