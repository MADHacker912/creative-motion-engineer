"""
Material Manager Module (CME 2.0 Core)
Procedural PBR materials for luxury products, optics, metals, and ceramics.
"""

try:
    import bpy
    IN_BLENDER = True
except ImportError:
    IN_BLENDER = False

def create_pbr_material(name="PBR_Material", base_color=(0.8, 0.8, 0.8, 1.0), metallic=0.0, roughness=0.3):
    """Creates a basic clean Principled BSDF material."""
    if not IN_BLENDER:
        return None
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base_color
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
    return mat

def create_brushed_metal(name="Brushed_Titanium", color=(0.82, 0.83, 0.85, 1.0), roughness=0.22):
    """Creates an anisotropic brushed metal with micro-bump."""
    if not IN_BLENDER:
        return None
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    out = nodes.new("ShaderNodeOutputMaterial")
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    out.location = (400, 0)
    bsdf.location = (0, 0)

    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Metallic"].default_value = 1.0
    bsdf.inputs["Roughness"].default_value = roughness
    if "Anisotropic" in bsdf.inputs:
        bsdf.inputs["Anisotropic"].default_value = 0.85
        bsdf.inputs["Anisotropic Rotation"].default_value = 0.25

    # Subtle noise bump
    tex_noise = nodes.new("ShaderNodeTexNoise")
    tex_noise.location = (-400, -150)
    tex_noise.inputs["Scale"].default_value = 180.0
    tex_noise.inputs["Detail"].default_value = 6.0

    bump = nodes.new("ShaderNodeBump")
    bump.location = (-150, -150)
    bump.inputs["Strength"].default_value = 0.02
    bump.inputs["Distance"].default_value = 0.01

    links.new(tex_noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat

def create_luxury_ceramic(name="Luxury_Ceramic", color=(0.03, 0.04, 0.05, 1.0)):
    """Creates a high-gloss ceramic with clearcoat layer."""
    if not IN_BLENDER:
        return None
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Metallic"].default_value = 0.0
        bsdf.inputs["Roughness"].default_value = 0.07
        if "Clearcoat" in bsdf.inputs:
            bsdf.inputs["Clearcoat"].default_value = 1.0
            bsdf.inputs["Clearcoat Roughness"].default_value = 0.03
        elif "Coat Weight" in bsdf.inputs:
            bsdf.inputs["Coat Weight"].default_value = 1.0
            bsdf.inputs["Coat Roughness"].default_value = 0.03
    return mat

def create_optical_glass(name="Optical_Glass", ior=1.52, tint=(0.95, 0.98, 1.0, 1.0)):
    """Creates refractive optical glass with smooth surface."""
    if not IN_BLENDER:
        return None
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = tint
        bsdf.inputs["Metallic"].default_value = 0.0
        bsdf.inputs["Roughness"].default_value = 0.04
        if "Transmission" in bsdf.inputs:
            bsdf.inputs["Transmission"].default_value = 0.96
        elif "Transmission Weight" in bsdf.inputs:
            bsdf.inputs["Transmission Weight"].default_value = 0.96
        bsdf.inputs["IOR"].default_value = ior
    return mat

def assign_material(obj, mat):
    """Assigns or replaces the primary material of an object."""
    if not IN_BLENDER or not obj or not mat:
        return
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
