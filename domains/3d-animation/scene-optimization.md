# Scene Optimization: Draw Calls, VRAM & Battery Life

## 1. Optimization Rules
- **Cap Pixel Ratio**: `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`. Never render at 3x or 4x on mobile Retina screens.
- **Draw Call Budget**: Keep total draw calls below **50** for mobile and below **120** for desktop. Use `THREE.InstancedMesh` for repeated objects.
- **Disposal Pattern**: Always dispose geometries, materials, and textures when removing objects:
```typescript
export function disposeHierarchy(node: THREE.Object3D) {
  node.traverse((child) => {
    if (child instanceof THREE.Mesh) {
      child.geometry.dispose();
      if (Array.isArray(child.material)) {
        child.material.forEach((m) => m.dispose());
      } else {
        child.material.dispose();
      }
    }
  });
}
```
