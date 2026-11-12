# Checklist: Web Animation Quality
- [ ] Zero animating layout properties (`top`, `left`, `width`, `height`, `margin`).
- [ ] Strictly animating `transform` and `opacity`.
- [ ] Cleaned up GSAP timelines via `context.revert()` or `useGSAP`.
- [ ] Capped canvas pixel ratio at `min(devicePixelRatio, 2)`.
- [ ] Tested responsive breakpoints via `ScrollTrigger.matchMedia()`.
