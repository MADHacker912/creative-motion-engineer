# Page Transitions: Continuity and Layout Morphing

## 1. Architecture of Seamless Page Shifts
A great page transition eliminates the jarring white flash of browser navigation:
1. **Outro Phase**: Exit current page elements (staggered fade/translate, duration 300ms).
2. **Curtain / Mask Phase**: Wipe transition overlay across screen.
3. **DOM Swap / Hydration**: Fetch new route markup and mount new view.
4. **Intro Phase**: Reveal new page elements along their natural reading order.
