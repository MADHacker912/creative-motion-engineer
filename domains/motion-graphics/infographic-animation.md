# Infographic Animation & Dynamic Data Visualizations

## 1. Principles of Data in Motion
Animated data must never distort factual truth. Motion should highlight trends, comparisons, and scale differentials:
1. **Synchronized Tickers**: Numerical counter tickers must smoothly decelerate (`easeOutExpo`) into the final value.
2. **Sequential Bar & Arc Stagger**: Multi-series charts should grow in sequence from left-to-right or from baseline up.
3. **Direct Label Grounding**: Keep numerical labels locked to the growing tip of the bar or line to prevent visual detachment.

---

## 2. Implementation: Smooth Easing Number Counter

```typescript
import { gsap } from "gsap";

export function animateCounter(
  element: HTMLElement,
  targetValue: number,
  prefix = "",
  suffix = "",
  decimals = 0
) {
  const proxy = { val: 0 };

  gsap.to(proxy, {
    val: targetValue,
    duration: 1.8,
    ease: "power3.out",
    onUpdate: () => {
      element.textContent = `${prefix}${proxy.val.toFixed(decimals)}${suffix}`;
    }
  });
}
```
