# SVG Animation: Vectors, Paths, and Morphing

## 1. Vector Path Draw-On Technique
Animate the `stroke-dashoffset` property from the path's total length to zero:

```typescript
export function animateSvgPath(path: SVGPathElement, duration = 1.2) {
  const length = path.getTotalLength();
  path.style.strokeDasharray = `${length}`;
  path.style.strokeDashoffset = `${length}`;
  path.getBoundingClientRect(); // Trigger reflow

  path.style.transition = `stroke-dashoffset ${duration}s cubic-bezier(0.16, 1, 0.3, 1)`;
  path.style.strokeDashoffset = "0";
}
```
