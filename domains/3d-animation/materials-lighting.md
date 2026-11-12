# Materials, Shading & Lighting Theory

## 1. The PBR Metal-Roughness Workflow
Every real-world material in Three.js `MeshPhysicalMaterial` or `MeshStandardMaterial` is governed by:
- **Albedo / Base Color**: Pure diffuse color with zero baked lighting or ambient occlusion.
- **Metalness (`0.0` or `1.0`)**: Dielectrics (plastics, wood, stone) are `0.0`. Conductors (chrome, gold, steel) are `1.0`. Rarely use values in between except for dust/grime layers.
- **Roughness (`0.0` to `1.0`)**: Controls microscopic surface smoothness. Low values produce mirror-like specular highlights; high values produce diffused reflections.
- **Transmission & IOR**: For realistic glass and liquids, set `transmission: 0.95`, `roughness: 0.05`, and `ior: 1.5` (borosilicate glass).

---

## 2. Three-Point Studio Lighting Setup
```typescript
import * as THREE from "three";

export function setupStudioLighting(scene: THREE.Scene) {
  // Key Light (Main form-defining light)
  const keyLight = new THREE.DirectionalLight(0xffffff, 2.5);
  keyLight.position.set(5, 8, 5);
  scene.add(keyLight);

  // Fill Light (Soft shadow-lifting light)
  const fillLight = new THREE.DirectionalLight(0x90b0e0, 1.0);
  fillLight.position.set(-6, 3, -2);
  scene.add(fillLight);

  // Rim / Back Light (Edge silhouette highlight)
  const rimLight = new THREE.DirectionalLight(0xffeedd, 3.0);
  rimLight.position.set(0, 5, -7);
  scene.add(rimLight);

  // Ambient Fill
  const ambient = new THREE.AmbientLight(0x0a1128, 0.4);
  scene.add(ambient);
}
```
