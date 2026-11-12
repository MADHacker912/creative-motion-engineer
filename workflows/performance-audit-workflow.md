# Workflow: Motion Performance & Frame Rate Audit

## Overview
Step-by-step diagnostic workflow using Chrome DevTools and Web Vitals:
1. **Rendering Tab**: Enable "Paint Flashing" and "Layout Shift Regions". Ensure animations do not trigger green paint rectangles.
2. **Performance Panel**: Record a 5-second interaction. Verify no long tasks (>50ms) during animations.
3. **Memory Panel**: Take heap snapshots before and after unmounting animated routes. Verify zero detached DOM elements or WebGL textures.
