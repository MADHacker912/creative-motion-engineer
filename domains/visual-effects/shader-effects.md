# Shader Effects: Film Grain, Vignette, and Scanlines

## 1. Procedural Film Grain Shader
```glsl
float pseudoNoise(vec2 co) {
    return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
}

void applyFilmGrain(inout vec3 color, vec2 uv, float time, float intensity) {
    float grain = pseudoNoise(uv * time) * intensity;
    color += grain - (intensity * 0.5);
}
```
