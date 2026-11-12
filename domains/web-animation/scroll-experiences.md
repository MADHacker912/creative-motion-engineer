# Scroll Experiences: Pinning, Scrubbing, and Choreography

## 1. The Scroll-Scrub Architecture
In a scrubbed narrative, the user's scroll position acts as the playhead of a master timeline.
- **Pinning**: Keep the stage fixed in the viewport while the timeline progress advances from `0.0` to `1.0`.
- **Anticipate Pin**: Set `anticipatePin: 1` in GSAP ScrollTrigger to prevent visual micro-stutter when the section locks.
- **Lenis Smooth Scroll**: Normalize scroll velocity across platforms to avoid jerky mechanical mouse-wheel steps.

```typescript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

export function createPinnedStory(triggerEl: HTMLElement, cardEl: HTMLElement) {
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: triggerEl,
      start: "top top",
      end: "+=200%",
      pin: true,
      scrub: 1, // 1-second lag smoothing
      anticipatePin: 1
    }
  });

  tl.fromTo(cardEl, { scale: 0.8, opacity: 0 }, { scale: 1, opacity: 1, duration: 1 })
    .to(cardEl, { y: -100, rotateX: 10, duration: 1 });
}
```
