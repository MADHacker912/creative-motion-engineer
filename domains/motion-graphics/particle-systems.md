# Particle Systems: 2D & 3D Emitters

## 1. Particle System Architecture
A robust particle system consists of:
1. **Emitter**: Spawn origin (point, line, surface, or volumetric box), spawn rate, initial velocity vector.
2. **Forces**: Gravity, drag / air resistance, wind, turbulence (Simplex / Curl noise), attractors / repulsors.
3. **Particle Lifecycle**: `birth` ➔ `update(dt)` ➔ `render()` ➔ `death / recycling`.

---

## 2. Canvas 2D Ambient Floating Dust (High Performance)

```typescript
interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  size: number;
  alpha: number;
  maxAlpha: number;
  life: number;
  decay: number;
}

export class AmbientParticles {
  private particles: Particle[] = [];
  private ctx: CanvasRenderingContext2D;
  private width = 0;
  private height = 0;

  constructor(private canvas: HTMLCanvasElement, private count = 60) {
    this.ctx = canvas.getContext("2d")!;
    this.resize();
    this.init();
  }

  public resize() {
    this.width = this.canvas.width = window.innerWidth;
    this.height = this.canvas.height = window.innerHeight;
  }

  private init() {
    for (let i = 0; i < this.count; i++) {
      this.particles.push(this.createParticle());
    }
  }

  private createParticle(): Particle {
    return {
      x: Math.random() * this.width,
      y: Math.random() * this.height,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4 - 0.1,
      size: Math.random() * 2 + 1,
      alpha: 0,
      maxAlpha: Math.random() * 0.4 + 0.1,
      life: 0,
      decay: Math.random() * 0.005 + 0.002
    };
  }

  public render() {
    this.ctx.clearRect(0, 0, this.width, this.height);
    for (const p of this.particles) {
      p.x += p.vx;
      p.y += p.vy;
      p.life += p.decay;

      // Smooth alpha envelope (fade in, fade out)
      p.alpha = Math.sin(p.life * Math.PI) * p.maxAlpha;

      if (p.life >= 1 || p.x < 0 || p.x > this.width || p.y < 0 || p.y > this.height) {
        Object.assign(p, this.createParticle());
      }

      this.ctx.fillStyle = `rgba(180, 210, 255, ${Math.max(0, p.alpha)})`;
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      this.ctx.fill();
    }
  }
}
```
