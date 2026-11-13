# Changelog

## [2.0.0] - 2026-11-13

### Added - CME 2.0 Professional Creative Intelligence & Production Upgrade
- **Professional Creative Intelligence**:
  - `core/professional-art-direction.md`: 10-step pre-production protocol, style dialect matrix (Luxury, Monumental Brutalist, Swiss Editorial, Organic/Bio-Mechanical), reference deconstruction rules, visual anti-patterns ban.
  - `workflows/blender-visual-iteration-workflow.md`: Mandatory 12-stage Render-Inspect-Correct closed feedback loop with visual defect checklist.
  - `checklists/blender-professional-quality.md`: 9 Production Quality Gates (Physical Coherence, Lighting Purity, Silhouettes, Motion Easing, etc.).
- **Advanced Blender Engineering Intelligence**:
  - `technologies/blender/advanced-modeling.md`: Hard-surface modeling, non-destructive modifier stacks (Bevel + Weighted Normal), subdivision surfaces, Bmesh parametric scripting.
  - `technologies/blender/geometry-nodes.md`: Procedural network architectures, radial/circular instancing, Poisson surface distribution, Python node graph generation.
  - `technologies/blender/material-artistry.md`: Physical Principled BSDF workflows, Anisotropic brushed metals, luxury obsidian ceramic, optical glass with chromatic dispersion, procedural micro-imperfections.
  - `technologies/blender/cinematography.md`: Cinematic camera optics (85mm telephoto vs 35mm wide), 2-node tracked camera rigs, commercial studio 3-point softboxes, chiaroscuro lighting, depth-of-field control.
  - `technologies/blender/animation-systems.md`: F-Curve manipulation, Bezier cubic easing handles, multi-axis kinetic choreography, exploded view assembly, follow-path constraints.
  - `technologies/blender/rendering-pipeline.md`: AgX and Filmic high-contrast color science, EEVEE vs Cycles performance tuning, dedicated ThinkPad T420 CPU rendering profile (<80k polycount, software rasterization fallback).
  - `workflows/hybrid-motion-production.md`: Multi-tool production pipeline integrating Blender 3D passes into Remotion React composition and FFmpeg final master encoding.
- **Modular Python Production Toolkit (`technologies/blender/scripts/`)**:
  - `core/scene_manager.py`: Metric unit setup, orphan data purge, AgX color management.
  - `core/render_manager.py`: Dual-mode (PREVIEW vs FINAL) rendering manager with automatic engine/hardware optimization.
  - `core/camera_manager.py`: Tracked 2-node camera rigs with Depth of Field.
  - `core/material_manager.py`: Procedural PBR material generators (titanium, chrome, ceramic, glass).
  - `core/lighting_manager.py`: Commercial softbox 3-point rigs and chiaroscuro studio lighting.
  - `core/blender_client.py`: Multi-mode client supporting live WebSocket/HTTP bridge and headless CLI execution.
  - `quality/scene_audit.py`: Automated scene diagnostic checking cameras, lights, unapplied transforms, materials, and polycounts.
  - `presets/studio_product.py`: Curved infinity cove cyclorama with 3-point studio lighting.
  - `presets/cinematic_scene.py`: Monolithic floor, chiaroscuro lighting, and 35mm wide framing.
  - `utilities/render_preview.py`: Rapid preview rendering utility.
  - `utilities/export_glb.py`: Draco-compressed GLB export utility.
- **Production Validation Benchmarks (`benchmarks/`)**:
  - **Benchmark A (AURA-01 Luxury Audio Dial)**: Full multi-material asset, infinity cove studio, 85mm DOF camera, preview & 1080p master render.
  - **Benchmark B (KAIROS Monolith)**: Brutalist architectural scene, dark obsidian ground, emissive glyph slice, 35mm low-angle camera, preview & 1080p master render.
  - **Benchmark C (NEXUS Identity)**: Animated 3D brand reveal, keyframed dual-axis counter-rotation, cubic Bezier easing, camera dolly-in, preview & 1080p master render.
  - `benchmarks/BENCHMARKS.md`: Complete benchmark specifications, creative directions, and execution logs.

---

## [1.1.0] - 2026-11-13

### Added
- **Live Blender Bridge & Autonomous Integration**:
  - `technologies/blender/scripts/blender_bridge_server.py`: Real-time HTTP & JSON-RPC server running inside Blender's modal event loop (:8198).
  - `technologies/blender/scripts/blender_client.py`: Universal CLI & Python controller with auto-detection of live sessions and headless fallback.
  - `technologies/blender/live-bridge.md`: Full architectural reference for live Blender control, viewport synchronization, and API specs.
  - `technologies/blender/procedural-generation.md`: Advanced Bmesh parametric generators, PBR glass/metal node graphs, and turntable keyframing.
  - `workflows/blender-live-workflow.md`: Standard operating procedure for live interactive 3D asset development.
  - `examples/blender/procedural_gem.py`: Standalone procedural faceted emerald with PBR glass shader and 360-degree turntable.
  - `examples/blender/live_blender_demo.py`: Live interactive demonstration script connecting to Blender and exporting Draco GLBs.
  - `examples/blender/README.md`: Setup and execution guide.
  - Auto-start script installed in `~/.config/blender/3.6/scripts/startup/start_agent_bridge.py`.

All notable changes to the **Creative Motion Engineer** skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-12

### Added
- **Core Intelligence Engine**:
  - `core/creative-intelligence.md`: Creative director mindset, conceptual planning, 7 creative questions.
  - `core/visual-thinking.md`: Principles of composition, framing, negative space, visual tension.
  - `core/motion-principles.md`: 12 Disney animation principles adapted for modern UI, easing math & spring physics.
  - `core/design-language.md`: Cohesive motion tokens, typography integration, color hierarchy.
  - `core/creative-direction.md`: Art direction styles, moodboarding, storyboarding guidelines.
  - `core/quality-standards.md`: The 6 Quality Gates for motion engineering.
- **Production Domains**:
  - `domains/motion-graphics/`: Kinetic typography, logo reveals, transitions, particle systems, infographics.
  - `domains/video-production/`: Cinematic storytelling, Remotion integration, sound design, color grading, multi-platform video export.
  - `domains/3d-animation/`: Real-time WebGL modelling, PBR materials, lighting theory, camera animation, product visualization, scene optimization.
  - `domains/web-animation/`: Scroll storytelling, page transitions, micro-interactions, parallax, SVG stroke manipulation, interactive playgrounds.
  - `domains/visual-effects/`: Compositing, distortion effects, particle simulations, lighting passes, custom GLSL shaders.
  - `domains/creative-frontend/`: Visual hierarchy, fluid responsive design, immersive split-screen layouts, gesture physics.
- **Technology Specializations**:
  - Complete technical manuals for GSAP 3, Three.js, React Three Fiber, Remotion, Blender Python (`bpy`), Rive, Lottie, WebGL, GLSL Shaders, FFmpeg CLI, Motion (Framer), and CSS/SVG.
- **Production Workflows**:
  - 7 standard production pipelines from discovery to delivery.
- **Production-Ready Examples**:
  - GSAP Hero Reveal & Scroll Sequence (TypeScript).
  - Three.js Interactive Floating Mesh Scene with HDRI & Post-Processing (TypeScript).
  - GLSL Vertex Wave & Fragment Chromatic Aberration Shaders.
  - Remotion Video Showcase Component (React/TSX).
  - CSS Hardware-Accelerated Micro-Interactions.
  - SVG Dynamic Path Draw-on and Morphing.
- **Quality Checklists**:
  - Pre-production, web animation quality, video quality, 3D quality, mobile performance, accessibility.
- **Comprehensive Reference Manuals**:
  - Official documentation directory, learning roadmap, and 100+ entry technical terminology index.
