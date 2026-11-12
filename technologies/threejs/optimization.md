# Three.js Optimization: Instancing & Memory

## 1. InstancedMesh for High Counts
When rendering thousands of identical objects (particles, grid markers), use `THREE.InstancedMesh` to render all instances in a **single draw call**.
