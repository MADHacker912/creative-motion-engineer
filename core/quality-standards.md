# Quality Standards: The 6 Quality Gates for Production

Every motion engineering output must pass through these 6 Quality Gates before it is considered production-ready.

---

## Gate 1: Aesthetic Distinctiveness (Zero-Slop Rule)
- [ ] No generic AI template patterns (unmotivated floating blobs, generic purple neon gradients).
- [ ] Typography has clear typographic hierarchy, consistent line-heights, and zero unmotivated tracking jumps.
- [ ] Visual hierarchy directs eye movement intentionally through scale, value, and motion contrast.

## Gate 2: Frame Pacing & Smoothness (60 FPS Target)
- [ ] Animations strictly target GPU-accelerated CSS properties (`transform`, `opacity`).
- [ ] Zero layout thrashing: no animating `width`, `height`, `top`, `left`, `margin`, or `padding`.
- [ ] `will-change` is applied judiciously and cleaned up after animation completes.
- [ ] Canvas rendering pixel ratio is capped at `min(window.devicePixelRatio, 2)`.

## Gate 3: Semantic Accessibility (WCAG 2.1 AA)
- [ ] Strict adherence to `@media (prefers-reduced-motion: reduce)`.
- [ ] All critical content and interactive elements are 100% visible and functional when motion is disabled.
- [ ] Zero flashing content exceeding 3 flashes per second (seizure prevention).
- [ ] Keyboard focus rings remain visible and un-obscured during and after transitions.

## Gate 4: Architecture & Memory Hygiene
- [ ] Every GSAP timeline instantiated in React uses `useGSAP` or cleans up with `ctx.revert()`.
- [ ] Every Three.js scene disposes geometries, materials, textures, and render targets on unmount.
- [ ] Event listeners (`scroll`, `mousemove`, `resize`) are debounced, throttled, or managed via `requestAnimationFrame`.
- [ ] Zero runaway render loops when the canvas is scrolled out of the viewport.

## Gate 5: Responsive & Cross-Device Resilience
- [ ] Mobile viewports do not experience horizontal scroll leaks from entering animated objects.
- [ ] Heavy 3D effects scale down or degrade gracefully on mobile GPUs (reduced particles, lowered shadow map resolution).
- [ ] Touch gestures replace mouse-hover dependencies on touchscreen devices.

## Gate 6: Code Elegance & Maintainability
- [ ] Code follows the Ponytail standard: shortest working diff, standard APIs, zero unneeded dependencies.
- [ ] Motion parameters are extracted into semantic tokens or config objects rather than hardcoded magic numbers.
- [ ] TypeScript types are strictly declared (no `any` shortcuts).
