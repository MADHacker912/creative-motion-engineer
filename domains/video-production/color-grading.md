# Color Grading: Look Development and Cinematic Spaces

## 1. Principles of Color Grading
Color grading establishes atmospheric tone and visual authority.
- **Lift (Shadows)**: Controls black levels. Crushing shadows (`<0.02`) adds digital contrast; slightly lifting shadows (`0.04-0.08`) creates an analog film or matte aesthetic.
- **Gamma (Midtones)**: Controls the balance of human skin tones and general exposure.
- **Gain (Highlights)**: Controls specular peaks and sky brightness.

---

## 2. CSS & WebGL Color Grading Matrix (Film LUT Simulation)

```css
/* Cinematic Contrast and Tonal Push */
.cinematic-grade {
  filter: contrast(1.12) brightness(0.96) saturate(0.92);
}

/* Luxury Warm Film Tonal Look */
.luxury-film-grade {
  filter: sepia(0.08) contrast(1.08) brightness(1.02) hue-rotate(-5deg);
}
```

For WebGL and GLSL post-processing, use a 3D LUT texture sample or an ACES Filmic Tone Mapping curve (see `technologies/glsl-shaders/SKILL.md`).
