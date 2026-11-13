# CME 2.0 BENCHMARK VALIDATION SUITE

This suite provides three complete, production-grade 3D projects demonstrating the full capabilities of **Creative Motion Engineer 2.0**. Each project contains automated generation scripts, saved `.blend` project files, and rendered visual outputs adhering to CME 2.0 Quality Gates.

---

## Benchmark A: Luxury Product Visualization — "AURA-01" Luxury Audio Dial

- **Path**: `benchmarks/benchmark_a_luxury_product/`
- **Script**: `build_benchmark_a.py`
- **Output Project**: `benchmark_a_aura01.blend`
- **Preview Render**: `preview_render_a.png` (960×540, 16 samples)
- **Final Master Render**: `final_render_a.png` (1920×1080, 64 samples)

### Creative Direction:
- **Style Dialect**: High-End Luxury Industrial Design (Bang & Olufsen / Leica aesthetic).
- **Geometry**:
  - Precision knurled outer bezel (48-division cylinder with 3-segment bevel & weighted normal modifier).
  - Chamfered step-down indicator ring with micro-gap clearance.
  - Optical glass lens cap (convex curvature, 1.52 IOR, subtle transmission roughness).
  - Curved infinity studio cove (smooth cyclorama beveling, zero sharp creases).
- **Materials**:
  - `Brushed_Titanium`: 0.82 Base, 1.0 Metallic, 0.22 Roughness with subtle micro-bump.
  - `Luxury_Ceramic`: 0.03 Base, 0.05 Roughness, deep obsidian gloss.
  - `Optical_Glass`: 1.52 IOR, 1.0 Transmission, 0.02 Roughness.
- **Cinematography & Lighting**:
  - **Camera**: 85mm Telephoto lens with shallow Depth of Field (f/2.4) focused precisely on the indicator index.
  - **Lighting Rig**: Overhead 180W softbox diffusion, 240W 45° Key Area, and 380W razor-thin grazing Rim Strip.

---

## Benchmark B: Atmospheric Cinematic 3D Scene — "KAIROS MONOLITH"

- **Path**: `benchmarks/benchmark_b_cinematic_scene/`
- **Script**: `build_benchmark_b.py`
- **Output Project**: `benchmark_b_kairos.blend`
- **Preview Render**: `preview_render_b.png` (960×540, 20 samples)
- **Final Master Render**: `final_render_b.png` (1920×1080, 48 samples)

### Creative Direction:
- **Style Dialect**: Monumental Brutalism & Atmospheric Sci-Fi (Dune / Blade Runner 2049).
- **Geometry**:
  - Tapered monolithic obelisk with bevel edge highlights and weighted normals.
  - Embedded vertical emissive rune channel sliced directly into the stone body.
  - Stepped circular pedestal with chamfered rim.
  - Expansive reflective obsidian ground plane (30m span).
- **Materials**:
  - `MAT_DarkBasalt`: Dark basalt with procedural noise roughness variation and micro-bump.
  - `MAT_CyanGlyphEmissive`: High-intensity electric cyan core (18.0 emission strength).
  - `MAT_ObsidianGround`: High-gloss dark stone with Fresnel falloff.
- **Cinematography & Lighting**:
  - **Camera**: 35mm Wide-Angle lens set low to the ground with dramatic upward tilt for monumental presence.
  - **Lighting Rig**: Chiaroscuro high-contrast lighting with an atmospheric cyan grazing strip.

---

## Benchmark C: Animated 3D Brand Reveal — "NEXUS IDENTITY"

- **Path**: `benchmarks/benchmark_c_brand_reveal/`
- **Script**: `build_benchmark_c.py`
- **Output Project**: `benchmark_c_nexus.blend`
- **Preview Render**: `preview_render_c.png` (960×540, 20 samples)
- **Final Master Render**: `final_render_c.png` (1920×1080, 48 samples)

### Creative Direction:
- **Style Dialect**: Futuristic Kinetic Identity & Tech Brand Packaging.
- **Geometry**:
  - Interlocking dual-axis torus rings (outer gold brush, inner chrome mirror).
  - Floating suspended luminescent core orb.
  - Dark matte studio floor.
- **Animation & Motion**:
  - Multi-axis counter-rotation across 90 frames (24 fps).
  - Custom Bezier F-Curve easing (`AUTO_CLAMPED` handles for zero robotic linear stops).
  - Core scale anticipation pop and settle.
  - Camera dolly-in track from wide overview (-5.5m) to hero framing (-3.6m).
- **Materials**:
  - `MAT_NexusChrome`: Pure mirror chrome (1.0 metallic, 0.08 roughness).
  - `MAT_NexusGold`: Luxury brushed warm gold (1.0 metallic, 0.18 roughness).
  - `MAT_NexusCoreEmissive`: Luminous violet core (14.0 emission).

---

## Hardware Compliance & Execution Record

- **Test Machine**: Lenovo ThinkPad T420 (Intel Core i3-2310M @ 2.10GHz, 2 cores / 4 threads, 11GB RAM, Intel HD Graphics 3000).
- **Engine**: Blender EEVEE CPU software rasterization (Mesa/SwiftShader fallback).
- **Polycount Budget**: Under 80,000 faces per scene.
- **Render Times**:
  - 960×540 Preview: ~12–20s
  - 1080p Final Master: ~40–60s
