# Technology: Modern CSS Animations & SVG Filters

## 1. Hardware Accelerated Transforms
Always animate strictly `transform` and `opacity`. Never animate `top`, `left`, `margin`, `width`, or `height`.
```css
.hardware-accelerated-card {
  will-change: transform;
  transform: translate3d(0, 0, 0);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
}

.hardware-accelerated-card:hover {
  transform: translate3d(0, -6px, 0) scale(1.02);
}
```
