import * as THREE from "three";

export class ProductScene {
  private scene = new THREE.Scene();
  private camera: THREE.PerspectiveCamera;
  private renderer: THREE.WebGLRenderer;
  private mesh: THREE.Mesh;
  private animId = 0;

  constructor(private container: HTMLElement) {
    const w = container.clientWidth;
    const h = container.clientHeight;

    this.camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 50);
    this.camera.position.set(0, 0, 4.5);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    this.renderer.setSize(w, h);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    container.appendChild(this.renderer.domElement);

    // Setup geometry & PBR material
    const geo = new THREE.TorusKnotGeometry(0.8, 0.28, 128, 32);
    const mat = new THREE.MeshPhysicalMaterial({
      color: 0x0A84FF,
      metalness: 0.85,
      roughness: 0.18,
      clearcoat: 1.0,
      clearcoatRoughness: 0.1
    });
    this.mesh = new THREE.Mesh(geo, mat);
    this.scene.add(this.mesh);

    // Studio lights
    const key = new THREE.DirectionalLight(0xffffff, 2.0);
    key.position.set(4, 5, 4);
    this.scene.add(key);

    const rim = new THREE.DirectionalLight(0x00f0ff, 2.5);
    rim.position.set(-4, -2, -4);
    this.scene.add(rim);

    this.scene.add(new THREE.AmbientLight(0x050a1a, 0.5));

    this.animate();
  }

  private animate = () => {
    this.mesh.rotation.x += 0.005;
    this.mesh.rotation.y += 0.008;
    this.renderer.render(this.scene, this.camera);
    this.animId = requestAnimationFrame(this.animate);
  };

  public destroy() {
    cancelAnimationFrame(this.animId);
    this.mesh.geometry.dispose();
    (this.mesh.material as THREE.Material).dispose();
    this.renderer.dispose();
    this.container.removeChild(this.renderer.domElement);
  }
}
