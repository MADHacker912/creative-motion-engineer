# Workflow: Custom VFX and Shader Development

## Overview
1. **Mathematics & Noise**: Prototype vertex displacement or UV manipulation formulas.
2. **Shader Compilation**: Write `.vert` and `.frag` shaders using Three.js `ShaderMaterial`.
3. **Uniform Binding**: Expose `uTime`, `uMouse`, and `uResolution` uniforms.
4. **Performance Profiling**: Check fill rate and shader complexity on low-end mobile GPUs.
