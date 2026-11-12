# Interactive Experiences: Playgrounds & Generative Canvases

## 1. Dynamic Cursor Trails & Canvas Fields
- Keep interactive canvases decoupled from DOM layout.
- Use `requestAnimationFrame` with delta time clamping (`Math.min(dt, 0.1)`) to avoid physics explosion when tabs become inactive.
