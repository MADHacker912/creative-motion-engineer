# Material Artistry: Physical Realism, Procedural Shaders & Imperfections

## 1. Physical Believability & The Anti-Plastic Rule
A primary failure mode of beginner 3D work is **flat, plastic-looking materials**. 

Real-world materials possess:
1. **Roughness Variation**: No physical surface has an entirely uniform roughness. Reflections break up due to microscopic scratches, oils, handling marks, and dust.
2. **Fresnel Reflections**: Surfaces reflect more light at grazing angles than when viewed head-on.
3. **Specular Color Discipline**: Dielectrics (glass, plastic, ceramic, wood) have monochromatic white specular reflections. Only metals (gold, copper, brass) tint their specular reflections.

---

## 2. Advanced Material Recipes (Python Node Builders)

### 2.1 Anisotropic Brushed Metal (Luxury Audio Knobs & Watch Bezels)
```python
import bpy

def create_brushed_metal_material(name="BrushedMetal", base_color=(0.85, 0.86, 0.88, 1.0), roughness=0.25, anisotropy=0.85):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    out.location = (400, 0)
    bsdf.location = (0, 0)

    # Metallic PBR parameters
    bsdf.inputs["Base Color"].default_value = base_color
    bsdf.inputs["Metallic"].default_value = 1.0
    bsdf.inputs["Roughness"].default_value = roughness
    if "Anisotropic" in bsdf.inputs:
        bsdf.inputs["Anisotropic"].default_value = anisotropy
        bsdf.inputs["Anisotropic Rotation"].default_value = 0.25

    # Procedural micro-scratch bump
    tex_noise = nodes.new("ShaderNodeTexNoise")
    tex_noise.location = (-400, -200)
    tex_noise.inputs["Scale"].default_value = 150.0
    tex_noise.inputs["Detail"].default_value = 6.0

    bump = nodes.new("ShaderNodeBump")
    bump.location = (-150, -200)
    bump.inputs["Strength"].default_value = 0.03
    bump.inputs["Distance"].default_value = 0.01

    links.new(tex_noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat
```

### 2.2 Luxury Ceramic (Deep Lustre & Glaze)
For camera lenses, luxury electronics, and architectural tiles:
```python
def create_luxury_ceramic_material(name="GlossCeramic", color=(0.04, 0.05, 0.06, 1.0)):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    out.location = (300, 0)
    bsdf.location = (0, 0)

    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["Roughness"].default_value = 0.08
    if "Clearcoat" in bsdf.inputs:
        bsdf.inputs["Clearcoat"].default_value = 1.0
        bsdf.inputs["Clearcoat Roughness"].default_value = 0.03
    elif "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 1.0
        bsdf.inputs["Coat Roughness"].default_value = 0.03

    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat
```

### 2.3 Optical Glass with Dispersion
```python
def create_optical_glass_material(name="OpticalGlass", ior=1.52, roughness=0.02):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    out.location = (300, 0)
    bsdf.location = (0, 0)

    bsdf.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)
    bsdf.inputs["Metallic"].default_value = 0.0
    bsdf.inputs["Roughness"].default_value = roughness
    if "Transmission" in bsdf.inputs:
        bsdf.inputs["Transmission"].default_value = 1.0
    elif "Transmission Weight" in bsdf.inputs:
        bsdf.inputs["Transmission Weight"].default_value = 1.0
    bsdf.inputs["IOR"].default_value = ior

    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat
```

---

## 3. Surface Imperfections Layering
To bring procedural shaders to life:
1. Connect a `Musgrave` or `Noise Texture` node through a `ColorRamp` to remap values into a subtle range (`0.12` to `0.28`).
2. Feed this output into the **Roughness** socket of the Principled BSDF.
3. This creates organic fingerprint smudges, atmospheric condensation, and handling variation that catch dynamic specular glints as lights move.
