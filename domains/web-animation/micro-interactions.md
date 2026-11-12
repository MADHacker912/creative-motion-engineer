# Micro-Interactions: Tactile Feedback & System States

## 1. Magnetic Button Implementation
A magnetic button slightly pulls toward the user's cursor within a defined proximity radius:

```typescript
import { gsap } from "gsap";

export function attachMagneticEffect(button: HTMLElement, radius = 60) {
  const bounds = button.getBoundingClientRect();
  const centerX = bounds.left + bounds.width / 2;
  const centerY = bounds.top + bounds.height / 2;

  function onMouseMove(e: MouseEvent) {
    const dist = Math.hypot(e.clientX - centerX, e.clientY - centerY);
    if (dist < radius) {
      const pullX = (e.clientX - centerX) * 0.35;
      const pullY = (e.clientY - centerY) * 0.35;
      gsap.to(button, { x: pullX, y: pullY, duration: 0.3, ease: "power2.out" });
    } else {
      gsap.to(button, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.4)" });
    }
  }

  window.addEventListener("mousemove", onMouseMove);
  return () => window.removeEventListener("mousemove", onMouseMove);
}
```
