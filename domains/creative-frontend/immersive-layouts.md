# Immersive Layouts: Split Screens, Pinned Canvases, and Modals

## 1. Pinned Background Canvas Architecture
```html
<div class="webgl-canvas-container fixed inset-0 -z-10 pointer-events-none">
  <canvas id="hero-webgl"></canvas>
</div>
<main class="relative z-10">
  <!-- Content flows cleanly over the 3D scene -->
</main>
```
