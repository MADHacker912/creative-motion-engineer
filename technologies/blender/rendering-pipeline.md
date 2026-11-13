# Professional Rendering Pipeline: Color Science, Engines & Low-Hardware Profiles

## 1. Color Science & Tonemapping (AgX vs Filmic)
Never render with default standard sRGB clamping. Standard clipping crushes highlights into harsh, saturated borders (the dreaded "digital clip").

### 1.1 The AgX & Filmic Tonemapping Workflow
- **AgX (Blender 4.0+) / Filmic (Blender 3.6 LTS)**: Emulates real analog photographic film emulsions. Extremely bright specular highlights desaturate naturally to white before clipping, retaining subtle hue gradients.
- **Look Contrast**: Set `Look = 'Medium High Contrast'` or `'High Contrast'` to prevent the flat, washed-out appearance of un-graded filmic curves.

```python
import bpy

def setup_color_science(scene=None):
    """Configures professional photographic color management."""
    if not scene:
        scene = bpy.context.scene
    scene.display_settings.display_device = 'sRGB'
    available = [item.identifier for item in scene.view_settings.bl_rna.properties['view_transform'].enum_items]
    if 'AgX' in available:
        scene.view_settings.view_transform = 'AgX'
    elif 'Filmic' in available:
        scene.view_settings.view_transform = 'Filmic'
    scene.view_settings.look = 'High Contrast'
```

---

## 2. Low-Hardware Architecture (ThinkPad T420 / Intel Core i3 Profile)

When operating on limited hardware (such as a dual-core Intel Core i3-2310M @ 2.10GHz without a dedicated GPU), rendering parameters must be strictly calibrated between **Fast Preview** and **Final Master**.

### 2.1 Dual-Profile Rendering Strategy

| Parameter | PREVIEW MODE (Fast Iteration) | FINAL MASTER MODE (Production) |
|---|---|---|
| **Render Engine** | `BLENDER_EEVEE` | `BLENDER_EEVEE` or `CYCLES` (CPU) |
| **Resolution** | `960 x 540` (qHD) | `1920 x 1080` (Full HD) |
| **EEVEE Samples** | `16 samples` | `64 samples` |
| **Cycles Samples** | `24 samples` (CPU) | `64 samples` + OpenImageDenoise |
| **Shadow Map Size** | `512px` | `1024px` |
| **Target Render Time** | **< 12 seconds per frame** | **< 2.5 minutes per frame** |

---

## 3. Render Passes & Compositing for Post-Processing
For commercial workflows requiring compositing in Remotion or web post-processing:
- **Transparent Background**: Enable `scene.render.film_transparent = True` for alpha PNG / WebM exports.
- **Denoising**: Enable `scene.cycles.use_denoising = True` with `denoiser = 'OPENIMAGEDENOISE'` for clean CPU grain reduction.
- **Render Passes**: Enable `Z-Depth`, `Normal`, and `Mist` passes when transferring 3D depth to 2D post-compositing engines.
