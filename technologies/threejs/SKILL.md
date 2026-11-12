# Technology: Three.js Real-Time 3D Engine

## 1. Overview & Architecture
Three.js provides an abstraction over WebGL. A production setup requires:
- `THREE.Scene`: The spatial graph containing meshes, lights, and cameras.
- `THREE.PerspectiveCamera`: Projection parameters (FOV, aspect, near, far).
- `THREE.WebGLRenderer`: The rasterization engine with antialiasing and tone mapping.
