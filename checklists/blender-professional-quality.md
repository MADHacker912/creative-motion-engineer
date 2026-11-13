# Quality Checklist: Blender Professional Production Gates (CME 2.0)

A project cannot be signed off simply because the Python script ran without exceptions. Every 3D scene must pass all 9 production quality gates:

---

## Gate 1: Creative Direction & Concept
- [ ] Visual thesis directly aligns with client brief and emotional anchor.
- [ ] Art direction is distinct (Luxury, Monolithic, Swiss Minimal, or Organic), not generic template.
- [ ] Composition follows rule of thirds, golden ratio, or monumental monolith alignment.

## Gate 2: Modeling & Topology
- [ ] Silhouettes and proportions are visually believable.
- [ ] Micro-bevels applied to all hard edges; zero infinitely sharp 90° computer edges.
- [ ] Auto Smooth enabled with Weighted Normal modifier to eliminate flat face shading artifacts.
- [ ] Unapplied transforms cleared (`scale == (1,1,1)` and `rotation == (0,0,0)`).

## Gate 3: Material Artistry
- [ ] Zero flat single-color plastic materials.
- [ ] Metalness parameter is strictly `0.0` (dielectrics) or `1.0` (conductors).
- [ ] Roughness variation is present (subtle noise map breaking specular highlights).
- [ ] Glass and transparent materials feature correct Index of Refraction (IOR).

## Gate 4: Lighting & Shadows
- [ ] Subject is visually dominant and clearly separated from background.
- [ ] Specular highlights are controlled and not clipping into harsh pure white blobs.
- [ ] Narrow strip rim light provides crisp edge separation against dark backgrounds.
- [ ] Ambient fill does not wash out form-defining shadows.

## Gate 5: Cinematography & Optics
- [ ] Focal length is matched to subject (85mm–105mm for luxury products; 35mm for cinematic environments).
- [ ] 2-node camera rig with target tracking Empty is active.
- [ ] Depth of Field (DoF) is enabled with realistic f-stop (`f/2.8` to `f/4.0`).

## Gate 6: Animation Polish
- [ ] Motion timing incorporates anticipation, acceleration, and micro-settling.
- [ ] F-Curves are configured with custom Bezier tangent handles (no stiff linear starts).
- [ ] Sub-assemblies animate with staggered offsets (hierarchical motion).

## Gate 7: Rendering & Color Management
- [ ] Filmic or AgX tonemapping enabled with High Contrast look (no standard sRGB clipping).
- [ ] Hardware-appropriate profile selected (Preview mode on limited CPU, Final for delivery).
- [ ] Denoising active on Cycles/CPU rendering.

## Gate 8: Technical Integrity
- [ ] Scene opens cleanly without missing textures or broken external links.
- [ ] Orphan data blocks and unused meshes purged via `bpy.data.orphans_purge()`.
- [ ] Exported GLB verified with Draco compression and clean WebGL vertex colors.

## Gate 9: Delivery Verification
- [ ] Preview render visually inspected by the agent for lighting, framing, and contrast defects.
- [ ] Final 1080p render exported and verified on disk.
- [ ] Complete project files and audit logs organized in project directory.
