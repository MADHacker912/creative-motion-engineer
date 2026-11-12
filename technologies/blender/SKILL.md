# Technology: Blender Headless Scripting & GLTF Pipelines

## 1. Headless Python Scripting (bpy)
Automate asset optimization and GLTF exports without GUI:
```python
import bpy

# Set all materials to metallic PBR
for mat in bpy.data.materials:
    if mat.use_nodes:
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Roughness"].default_value = 0.2
            bsdf.inputs["Metallic"].default_value = 0.9

# Export to WebGL GLTF with Draco Compression
bpy.ops.export_scene.gltf(
    filepath="export_optimized.glb",
    export_format='GLB',
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=7
)
```
