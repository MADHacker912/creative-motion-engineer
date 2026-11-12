# GSAP ScrollTrigger: Pinning, Scrubbing, and Responsive Setups

## 1. ScrollTrigger Best Practices
```typescript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// Responsive Media Match
export function setupResponsiveScroll() {
  const mm = gsap.matchMedia();

  mm.add("(min-width: 768px)", () => {
    // Desktop: Pin and scrub multi-panel sequence
    gsap.to(".feature-panels", {
      xPercent: -200,
      ease: "none",
      scrollTrigger: {
        trigger: ".feature-track",
        pin: true,
        scrub: 1,
        end: () => "+=" + window.innerWidth * 2
      }
    });
  });

  mm.add("(max-width: 767px)", () => {
    // Mobile: Simple vertical entrance, zero pinning
    gsap.from(".feature-card", {
      opacity: 0,
      y: 40,
      stagger: 0.1,
      scrollTrigger: {
        trigger: ".feature-track",
        start: "top 80%"
      }
    });
  });

  return () => mm.revert();
}
```
