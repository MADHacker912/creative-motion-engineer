# Responsive Design: Fluid Canvases and Device Adaptation

## 1. Responsive Canvas Architecture
Ensure the WebGL canvas dynamically adapts to window resizing without distortion:
```typescript
export function handleCanvasResize(
  renderer: THREE.WebGLRenderer,
  camera: THREE.PerspectiveCamera
) {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
}
```
