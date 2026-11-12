# GSAP Advanced Patterns: FLIP, CustomEase, and React useGSAP

## 1. React useGSAP Hook Pattern
```tsx
import { useRef } from "react";
import { gsap } from "gsap";
import { useGSAP } from "@gsap/react";

export function AnimatedCard() {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    gsap.from(".card-item", {
      opacity: 0,
      y: 20,
      stagger: 0.05,
      ease: "power2.out"
    });
  }, { scope: container });

  return (
    <div ref={container} className="grid">
      <div className="card-item">Alpha</div>
      <div className="card-item">Beta</div>
    </div>
  );
}
```
