# Logo Animation & Animated Brand Identity Systems

## 1. Structural Anatomy of a Logo Reveal
A professional brand sting typically lasts between **1.8s and 3.2s** and consists of 4 distinct phases:

```
[Phase 1: Construction]  ──► Geometric deconstruction, stroke draw-on, wireframe guides (0.0s - 1.0s)
[Phase 2: Convergence]   ──► Shapes snap together, solid fills ignite, mass arrives (1.0s - 1.8s)
[Phase 3: Impact / Glow] ──► Color flash, subtle scale pop, logotype / tagline reveals (1.8s - 2.4s)
[Phase 4: Settling]      ──► Resting lockup, perfect alignment, clean static state (2.4s - 3.0s)
```

---

## 2. Production Techniques

### 2.1 SVG Stroke Dashoffset Write-On
For vector marks, stroke animation simulates precision drafting:
```javascript
import { gsap } from "gsap";

export function revealVectorLogo(svgPath: SVGPathElement, logoFill: SVGElement) {
  const length = svgPath.getTotalLength();

  // Set initial stroke dasharray
  gsap.set(svgPath, {
    strokeDasharray: length,
    strokeDashoffset: length,
    opacity: 1
  });
  gsap.set(logoFill, { opacity: 0 });

  const tl = gsap.timeline({ defaults: { ease: "power3.inOut" } });

  tl.to(svgPath, { strokeDashoffset: 0, duration: 1.4 })
    .to(logoFill, { opacity: 1, duration: 0.6, ease: "power2.out" }, "-=0.3")
    .to(svgPath, { opacity: 0, duration: 0.4 }, "-=0.2");
}
```

### 2.2 Morphing Brand Symbols
When transforming an abstract monogram into a wordmark, ensure:
- Control points count matches between SVG paths, or use GSAP MorphSVGPlugin for automatic spline mapping.
- Anchor points maintain physical centers of mass to avoid awkward shearing.
