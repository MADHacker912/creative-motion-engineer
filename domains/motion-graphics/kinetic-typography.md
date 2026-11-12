# Kinetic Typography & Dynamic Letterforms

## 1. Principles of Type in Motion
Typography is visual voice. When animating text, readability must remain the primary constraint. 

### Core Rules:
1. **Reading Speed Budget**: The average adult reads 200–250 words per minute (~4 words per second). Never dismiss or wipe text before the reading threshold has elapsed:
   $$\text{Minimum Display Time} = \max\left(1.2\text{s}, \; \frac{\text{Word Count}}{3.5} + 0.5\text{s}\right)$$
2. **Masked Reveals**: The cleanest modern type entrance uses an overflow-hidden wrapper where characters or lines slide up from below the baseline (`translateY(110%)` to `translateY(0%)`).
3. **Stagger Intervals**:
   - Character staggers: `20ms` to `35ms` per character.
   - Word staggers: `60ms` to `90ms` per word.
   - Line staggers: `120ms` to `180ms` per line.

---

## 2. Kinetic Techniques & Implementations

### 2.1 Staggered Word Reveal (GSAP & SplitText Alternative)
```typescript
import { gsap } from "gsap";

export function animateHeadline(container: HTMLElement) {
  // Wrap words in overflow-hidden spans
  const words = container.querySelectorAll(".word-inner");

  gsap.fromTo(
    words,
    { y: "115%", rotateZ: 3, opacity: 0 },
    {
      y: "0%",
      rotateZ: 0,
      opacity: 1,
      duration: 1.0,
      ease: "power4.out",
      stagger: 0.08,
      clearProps: "transform,opacity"
    }
  );
}
```

### 2.2 Variable Font Interpolation
```css
@keyframes expandWeight {
  0% {
    font-variation-settings: 'wght' 300, 'wdth' 100;
    letter-spacing: -0.02em;
  }
  100% {
    font-variation-settings: 'wght' 800, 'wdth' 120;
    letter-spacing: 0.05em;
  }
}

.hero-variable-type {
  animation: expandWeight 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```
