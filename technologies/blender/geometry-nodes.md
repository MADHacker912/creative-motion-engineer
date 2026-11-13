# Geometry Nodes: Procedural Modeling & Generative Systems

## 1. Architectural Philosophy
Geometry Nodes transforms Blender from a static polygon modeler into a parametric, non-destructive procedural engine. 

Instead of generating one-off static meshes, Geometry Nodes allows agents to create **reusable, data-driven procedural assets** whose density, distribution, curvature, and scale remain dynamically adjustable via modifier parameters.

---

## 2. Core Node Graph Mechanics in Blender 3.6+

Every Geometry Node system operates on fields and geometry flows:
- **Geometry Input / Output**: The foundational stream of vertices, edges, faces, and point clouds.
- **Fields (Diamond Sockets)**: Functions evaluated per-element (per-vertex, per-instance, or per-face).
- **Constants (Circle Sockets)**: Single uniform values passed globally across the entire graph.

---

## 3. Programmatic Geometry Nodes Creation via Python

You can assemble, wire, and expose parameters of Geometry Node systems completely from Python scripts:

```python
import bpy

def create_procedural_array_system(target_obj, instance_mesh, count=10, radius=2.5):
    """Creates a procedural circular instancing Geometry Node tree via Python."""
    # Add Geometry Nodes modifier
    modifier = target_obj.modifiers.new(name="CircularArray", type='NODES')
    node_group = bpy.data.node_groups.new("CircularArray_Tree", 'GeometryNodeTree')
    modifier.node_group = node_group

    nodes = node_group.nodes
    links = node_group.links
    nodes.clear()

    # 1. Group Input & Output
    group_in = nodes.new("NodeGroupInput")
    group_in.location = (-400, 0)
    group_out = nodes.new("NodeGroupOutput")
    group_out.location = (600, 0)

    # 2. Curve Circle (Path for points)
    curve_circle = nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.location = (-200, 150)
    curve_circle.inputs["Radius"].default_value = radius

    # 3. Resample Curve (Define exact count of points)
    resample = nodes.new("GeometryNodeResampleCurve")
    resample.location = (0, 150)
    resample.inputs["Count"].default_value = count

    # 4. Instance on Points
    instance_node = nodes.new("GeometryNodeInstanceOnPoints")
    instance_node.location = (250, 0)

    # 5. Object Info (Reference the instance mesh)
    obj_info = nodes.new("GeometryNodeObjectInfo")
    obj_info.location = (0, -150)
    obj_info.inputs["Object"].default_value = instance_mesh
    obj_info.transform_space = 'RELATIVE'

    # Wire up the network
    links.new(curve_circle.outputs["Curve"], resample.inputs["Curve"])
    links.new(resample.outputs["Curve"], instance_node.inputs["Points"])
    links.new(obj_info.outputs["Geometry"], instance_node.inputs["Instance"])
    links.new(instance_node.outputs["Instances"], group_out.inputs["Geometry"])

    return modifier
```

---

## 4. Standard Procedural Patterns

### 4.1 Poisson Disk Surface Scattering
For natural pebble, foliage, or screw distribution across a surface, use `Distribute Points on Faces` in `POISSON` mode. The `Distance Min` parameter prevents unnatural instance overlapping.

### 4.2 Curve to Mesh Extrusions
Turn 3D curves into architectural moldings, neon light tubes, or frame borders dynamically using `Curve to Mesh` paired with a `Curve Circle` profile.
