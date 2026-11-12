# Three.js Materials & Lighting

## 1. Physically Based Materials
- Use `THREE.MeshStandardMaterial` for standard matte or metallic surfaces.
- Use `THREE.MeshPhysicalMaterial` when requiring clearcoat, transmission (glass), or iridescence.
- Always configure an `Environment` map (HDR) for realistic ambient specular reflections.
