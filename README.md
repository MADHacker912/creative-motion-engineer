# Creative Motion Engineer (CME) 2.0
> Universal Creative Production Intelligence System for AI Coding Agents.

[![CME Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Blender 3.6+ LTS](https://img.shields.io/badge/Blender-3.6%2B%20LTS-orange.svg)](https://www.blender.org/)
[![Three.js / GSAP](https://img.shields.io/badge/WebGL-Three.js%20%7C%20GSAP-green.svg)](https://threejs.org/)

---

## Overview

**Creative Motion Engineer (CME) 2.0** transforms an autonomous AI coding agent into a multidisciplined creative production engineer combining the mindsets of a **Senior 3D Artist, Creative Director, Motion Designer, Cinematographer, Technical Artist, and Creative Technologist**.

Unlike typical code generators that produce generic primitive placeholders or unmotivated animations, CME 2.0 operates with strict aesthetic taste, physical material modeling, high-contrast AgX color science, closed-loop visual inspection, and deterministic production workflows.

---

## What's New in CME 2.0

### 1. Professional Creative Intelligence
- **10-Step Pre-Production Protocol**: Intentional design dialect selection (*Luxury Industrial, Monumental Brutalist, Swiss Editorial, Organic/Bio-Mechanical*), visual reference deconstruction, and explicit anti-pattern bans.
- **Closed-Loop Visual Iteration**: Mandatory 12-stage Render-Inspect-Correct cycle. Agents render intermediate frames, inspect with diagnostic audits, and refine before presenting deliverables.
- **The 9 Production Quality Gates**: Physical Coherence, Lighting Purity, Silhouette Separation, Motion Easing Rigor, Color Science (AgX), Zero Primitive Slop, Closed Visual Feedback, Hardware Safety, and Deterministic Delivery.

### 2. Professional Blender Intelligence
- **Advanced Modeling (`technologies/blender/advanced-modeling.md`)**: Professional hard-surface topology, non-destructive Bevel + Weighted Normal modifier stacks, subdivision edge flow, and Bmesh parametric generators.
- **Geometry Nodes (`technologies/blender/geometry-nodes.md`)**: Procedural distribution graphs, radial/circular instancing, Poisson scattering, and reusable node network synthesis via Python.
- **Material Artistry (`technologies/blender/material-artistry.md`)**: Photorealistic Principled BSDF node trees (anisotropic brushed titanium, obsidian ceramic, optical glass with dispersion, procedural micro-imperfections).
- **Cinematography & Studio Lighting (`technologies/blender/cinematography.md`)**: Exact focal length selection (85mm telephoto vs 35mm wide), 2-node tracked camera rigs with Depth of Field, commercial softbox studio lighting, and dramatic chiaroscuro.
- **Animation Systems (`technologies/blender/animation-systems.md`)**: F-Curve keyframe choreography, Bezier cubic easing handles, multi-axis kinetic motion, exploded view mechanics, and follow-path constraints.
- **Rendering Pipeline (`technologies/blender/rendering-pipeline.md`)**: AgX/Filmic high-contrast color management, EEVEE vs Cycles performance tuning, and low-hardware CPU rasterization profiling.

### 3. Modular Python Production Toolkit (`technologies/blender/scripts/`)
- `core/scene_manager.py`: Scene purging, metric scaling, world environment, and AgX management.
- `core/render_manager.py`: Dual-mode (PREVIEW vs FINAL) rendering management with hardware awareness.
- `core/camera_manager.py`: Tracked 2-node camera rigs with Depth of Field.
- `core/material_manager.py`: Procedural PBR material generators (titanium, chrome, ceramic, glass).
- `core/lighting_manager.py`: Commercial 3-light studio rigs & chiaroscuro setups.
- `core/blender_client.py`: Multi-mode client supporting live WebSocket/HTTP bridge (:8198) and headless CLI execution.
- `quality/scene_audit.py`: Automated scene diagnostic checking cameras, lights, unapplied transforms, materials, and polycounts.
- `presets/studio_product.py`: Curved infinity cove cyclorama with 3-point studio lighting.
- `presets/cinematic_scene.py`: Monolithic floor, chiaroscuro lighting, and 35mm wide framing.
- `utilities/render_preview.py`: CLI/script preview renderer.
- `utilities/export_glb.py`: Draco-compressed GLB export utility.

### 4. Real-World Production Benchmarks (`benchmarks/`)
Complete verified projects with automated build scripts, saved `.blend` files, and rendered visual outputs:
- **Benchmark A (`benchmarks/benchmark_a_luxury_product/`)**: "AURA-01" Luxury Audio Dial (Brushed titanium, knurled bezel, smoked glass, infinity cyclorama, 85mm DOF).
- **Benchmark B (`benchmarks/benchmark_b_cinematic_scene/`)**: "KAIROS MONOLITH" (Brutalist obelisk, reflective obsidian floor, emissive cyan glyph, chiaroscuro lighting, 35mm wide lens).
- **Benchmark C (`benchmarks/benchmark_c_brand_reveal/`)**: "NEXUS IDENTITY" (Interlocking kinetic emblem, multi-axis counter-rotation, cubic Bezier easing, camera dolly-in).

---

## Directory Architecture

```
creative-motion-engineer/
├── SKILL.md                          # Main Agent Entry Point (CME 2.0 Standard)
├── README.md                         # Architecture Overview & Engineering Guide
├── AGENT-INSTALL.md                  # Multi-Platform Agent Installation Guide
├── CHANGELOG.md                      # Version History & Release Notes
├── manifest.json                     # Skill Manifest & Tool Bindings
├── QUALITY-REPORT.md                 # Validation Audit & Verification Report
├── AUDIT/                            # Audit Reports & Upgrade Blueprints
│   └── CME-2.0-UPGRADE-REPORT.md     # Comprehensive 2.0 Gap Analysis & Roadmap
│
├── core/                             # Creative & Visual Intelligence
│   ├── creative-intelligence.md      # Creative Director Mindset & Conceptualization
│   ├── visual-thinking.md            # Composition, Contrast & Negative Space
│   ├── motion-principles.md          # 12 Principles, Easing Math & Spring Physics
│   ├── design-language.md            # Motion Systems, Spacing & Color Dynamics
│   ├── creative-direction.md         # Art Direction, Storyboarding & Moodboards
│   ├── professional-art-direction.md # 10-Step Pre-Production Protocol & Dialect Matrix
│   └── quality-standards.md          # The 6 Foundational Quality Gates
│
├── benchmarks/                       # Real-World Production Benchmarks
│   ├── BENCHMARKS.md                 # Benchmark Specifications & Verification Log
│   ├── benchmark_a_luxury_product/   # AURA-01 Audio Dial (.blend, preview & 1080p final)
│   ├── benchmark_b_cinematic_scene/  # KAIROS Monolith (.blend, preview & 1080p final)
│   └── benchmark_c_brand_reveal/     # NEXUS Animated Reveal (.blend, preview & 1080p final)
│
├── domains/                          # Creative Production Domains
│   ├── motion-graphics/              # 2D Animation, Kinetic Type, Logo Reveals
│   ├── video-production/             # Cinematic Storytelling, Remotion, Sound, Grading
│   ├── 3d-animation/                 # Real-time WebGL, PBR, Lighting, Asset Optimization
│   ├── web-animation/                # Scroll Storytelling, Pinned Sections, Parallax
│   ├── visual-effects/               # Compositing, Distortion, Particles, Post-Processing
│   └── creative-frontend/            # Fluid Grids, Immersive Typography, Responsive UI
│
├── technologies/                     # Deep Technical Specializations
│   ├── gsap/                         # Timelines, ScrollTrigger, FLIP, Observer
│   ├── threejs/                      # Scenegraph, PBR Shaders, Camera Rigs, Optimization
│   ├── react-three-fiber/            # R3F Canvas, Drei Helpers, Spring Hooks
│   ├── remotion/                     # Programmatic Video, Interpolation, Audio Sync
│   ├── blender/                      # Professional Blender 3D Specialization
│   │   ├── SKILL.md                  # Blender Agent Sub-Skill & Routing Table
│   │   ├── advanced-modeling.md      # Hard-Surface Topology & Modifier Stacks
│   │   ├── geometry-nodes.md         # Procedural Instancing & Node Graphs
│   │   ├── material-artistry.md      # Principled BSDF, Metals, Glass & Imperfections
│   │   ├── cinematography.md         # Focal Lengths, 2-Node Camera Rigs & Studio Lighting
│   │   ├── animation-systems.md      # F-Curve Bezier Easing & Kinetic Rigging
│   │   ├── rendering-pipeline.md     # AgX Color Science, EEVEE vs Cycles & CPU Profiles
│   │   ├── live-bridge.md            # Real-time HTTP/WebSocket Bridge Architecture
│   │   └── scripts/                  # Modular Python Production Toolkit
│   │       ├── core/                 # Scene, Camera, Light, Material & Render Managers
│   │       ├── presets/              # Studio Product & Cinematic Presets
│   │       ├── quality/              # Scene Diagnostic Auditor
│   │       └── utilities/            # Rapid Preview & Draco GLB Exporter
│   ├── rive/                         # State Machines, Vector Runtimes, Interactive Bones
│   ├── lottie/                       # Vector Playback, DotLottie, Web Optimization
│   ├── webgl/                        # Bare-metal WebGL, Buffer Attributes, Uniforms
│   ├── glsl-shaders/                 # Vertex & Fragment Shaders, Noise, Raymarching
│   ├── ffmpeg/                       # Transcoding, Codecs, Bitrates, ProRes, WebM Alpha
│   └── motion/                       # Framer Motion, Shared Layout, Gesture Physics
│
├── workflows/                        # Production Workflows & Feedback Loops
│   ├── blender-visual-iteration-workflow.md # Mandatory 12-Stage Feedback Loop
│   ├── hybrid-motion-production.md   # Multi-Tool Pipeline (Blender ➔ Remotion ➔ Web)
│   └── blender-live-workflow.md      # Live Bridge Interactive Workflow
│
└── checklists/                       # Quality Control & Acceptance Checklists
    └── blender-professional-quality.md # The 9 Production Quality Gates
```

---

## The 9 Production Quality Gates

Every 3D and motion deliverable produced using CME 2.0 must pass:

1. **Gate 1: Physical Coherence & Scale**: Exact real-world metric dimensions and applied scales (`Ctrl+A ➔ All Transforms`).
2. **Gate 2: Lighting Purity & Hierarchy**: Clear primary key light, secondary fill, and grazing rim light. Zero unmotivated flat ambient lighting.
3. **Gate 3: Silhouette & Edge Treatment**: Chamfered/beveled micro-edges on all hard surfaces with weighted normal modifiers to catch light highlights.
4. **Gate 4: Motion Easing Rigor**: Natural cubic Bezier acceleration/deceleration with `AUTO_CLAMPED` handles. Zero robotic linear stops.
5. **Gate 5: Color Science (AgX / Filmic)**: Dynamic range color management set to `AgX` or `Filmic` with `High Contrast` look. Standard sRGB clipping is strictly forbidden.
6. **Gate 6: Zero Primitive Slop**: No unmodeled default cubes, spheres, or cylinders. All assets must possess deliberate form, purpose, and micro-details.
7. **Gate 7: Render-Inspect-Correct Cycle**: Mandatory intermediate render verification and diagnostic auditing (`scene_audit.py`).
8. **Gate 8: Low-Hardware Profiling**: Real-time polygon and sample budget management ensuring clean execution on dual-core CPU machines.
9. **Gate 9: Deterministic Delivery**: Automated reproducibility via clean Python scripts, saved `.blend` files, and rendered assets.

---

## Installation & Setup

### In Antigravity / Gemini CLI:
```bash
# Clone repository into active skills directory
git clone https://github.com/MADHacker912/creative-motion-engineer.git ~/.gemini/config/skills/creative-motion-engineer
```

### In Claude Code:
```bash
# Add as a skill or include in your project
git clone https://github.com/MADHacker912/creative-motion-engineer.git ~/.claude/skills/creative-motion-engineer
```

### In Cursor / Windsurf / Cline / Roo-Code:
Add the path to your rules or `.cursorrules` / `.windsurfrules`:
```markdown
# Creative Motion Engineering
Always consult and follow instructions in:
`~/.gemini/config/skills/creative-motion-engineer/SKILL.md`
```

---

## License

MIT © [MADHacker912](https://github.com/MADHacker912) & Antigravity Creative Team.
