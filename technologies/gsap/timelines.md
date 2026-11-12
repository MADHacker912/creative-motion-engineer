# GSAP Timelines: Master Sequencing & Labels

## 1. Timeline Sequencing & Positional Syntax
Timelines allow non-linear, frame-accurate choreography:
```typescript
import { gsap } from "gsap";

export function createMasterHeroTimeline() {
  const tl = gsap.timeline({ defaults: { ease: "power3.out", duration: 0.8 } });

  tl.addLabel("start")
    .from(".hero-badge", { y: -20, opacity: 0 })
    .from(".hero-title .word", { y: "100%", stagger: 0.04 }, "start+=0.2")
    .from(".hero-description", { opacity: 0, y: 15 }, "<0.4") // Starts 0.4s into previous tween
    .from(".hero-cta-group", { scale: 0.95, opacity: 0 }, "-=0.2");

  return tl;
}
```
