# Workflow: Premium Animated Website Pipeline

## Overview
An 8-phase systematic pipeline for executing an award-winning motion website from initial brief to production launch.

```
[Phase 1: Discovery]      ──► Brand audit, emotional tone, device constraints, motion budget.
[Phase 2: Art Direction]  ──► Typography pairing, color tokens, layout grid, moodboard.
[Phase 3: Motion Script]  ──► Pacing storyboard, scroll trigger map, static anchor definition.
[Phase 4: Base Layout]    ──► Semantic HTML, CSS variables, static typography hierarchy.
[Phase 5: Choreography]   ──► GSAP timelines, Lenis smooth scroll, entrance staggers.
[Phase 6: Micro-Motion]   ──► Magnetic buttons, cursor interactions, state transitions.
[Phase 7: Optimization]   ──► Layer promotion, DevTools frame profiling, disposal hooks.
[Phase 8: Accessibility]  ──► Reduced-motion testing, keyboard navigation verification.
```

---

## Phase-by-Phase Checklist
1. **Discovery**: Answer the 7 Creative Questions (`core/creative-intelligence.md`).
2. **Motion Script**: Map which elements are pinned, which scrub, and which remain static.
3. **Choreography**: Register `ScrollTrigger.matchMedia()` for responsive behavior.
4. **Audit**: Verify 60fps on mobile viewports and complete `prefers-reduced-motion` compliance.
