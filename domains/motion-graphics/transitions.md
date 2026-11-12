# Transitions: Spatial Continuity and Scene Shifts

## 1. Taxonomy of Creative Transitions
Transitions bridge narrative beats. Avoid generic cross-fades; choose a transition that reflects the physics of the scene:

| Transition Type | Physical Metaphor | Ideal Application |
|---|---|---|
| **Whip Pan / Snap Push** | Rapid camera repositioning with motion blur. | Fast-paced product promos, feature leaps. |
| **Mask / Matte Wipe** | An architectural shape or element wipes across the screen. | Clean UI section shifts, editorial showcases. |
| **Match Cut** | Visual alignment of geometry between scene A and scene B. | Evolution stories, before-and-after reveals. |
| **Iris / Portal Zoom** | A focal circle expands outwards to reveal the next world. | Immersive 3D introductions, logo payoffs. |

---

## 2. Implementation: Hardware-Accelerated Mask Wipe

```css
.transition-curtain {
  position: fixed;
  inset: 0;
  background: var(--bg-surface-primary);
  transform-origin: bottom center;
  transform: scaleY(0);
  pointer-events: none;
  z-index: 9999;
}
```

```typescript
import { gsap } from "gsap";

export function executeSceneTransition(curtain: HTMLElement, onHalfway: () => void) {
  const tl = gsap.timeline();

  tl.to(curtain, {
    scaleY: 1,
    duration: 0.5,
    ease: "power4.inOut",
    onComplete: onHalfway
  })
  .set(curtain, { transformOrigin: "top center" })
  .to(curtain, {
    scaleY: 0,
    duration: 0.5,
    ease: "power4.inOut"
  });
}
```
