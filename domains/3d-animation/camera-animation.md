# Camera Animation & Cinematic Rigs

## 1. Pointer Parallax with Spring Damping
To create a high-end interactive feeling without turning the website into a clunky CAD viewer, use subtle mouse parallax damping:

```typescript
import * as THREE from "three";

export class DampedCameraRig {
  private target = new THREE.Vector2(0, 0);
  private current = new THREE.Vector2(0, 0);

  constructor(private camera: THREE.PerspectiveCamera, private factor = 0.05) {
    window.addEventListener("pointermove", (e) => {
      this.target.x = (e.clientX / window.innerWidth - 0.5) * 2;
      this.target.y = -(e.clientY / window.innerHeight - 0.5) * 2;
    });
  }

  public update() {
    // Lerp towards target
    this.current.x += (this.target.x - this.current.x) * this.factor;
    this.current.y += (this.target.y - this.current.y) * this.factor;

    this.camera.position.x = this.current.x * 0.8;
    this.camera.position.y = this.current.y * 0.5 + 1.2;
    this.camera.lookAt(0, 0.5, 0);
  }
}
```
