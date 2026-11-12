# Three.js Scene Architecture & Lifecycle Management

## 1. Clean Scene Boilerplate with Resize and Disposal
```typescript
import * as THREE from "three";

export class SceneManager {
  public scene = new THREE.Scene();
  public camera: THREE.PerspectiveCamera;
  public renderer: THREE.WebGLRenderer;
  private animId = 0;

  constructor(private container: HTMLElement) {
    const { clientWidth: w, clientHeight: h } = container;
    this.camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
    this.camera.position.set(0, 0, 5);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
    this.renderer.setSize(w, h);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.0;
    container.appendChild(this.renderer.domElement);

    window.addEventListener("resize", this.onResize);
    this.start();
  }

  private onResize = () => {
    const w = this.container.clientWidth;
    const h = this.container.clientHeight;
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(w, h);
  };

  private start() {
    const loop = () => {
      this.renderer.render(this.scene, this.camera);
      this.animId = requestAnimationFrame(loop);
    };
    loop();
  }

  public destroy() {
    cancelAnimationFrame(this.animId);
    window.removeEventListener("resize", this.onResize);
    this.renderer.dispose();
    this.container.removeChild(this.renderer.domElement);
  }
}
```
