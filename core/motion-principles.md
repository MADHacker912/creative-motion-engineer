# Motion Principles, Easing Math, and Physics

## 1. The 12 Disney Principles Adapted for Digital Interfaces

Originally codified by Ollie Johnston and Frank Thomas, these principles are essential for modern interactive UI and 3D motion:

| Classic Principle | Digital & UI Interpretation | Implementation Rule |
|---|---|---|
| **1. Squash & Stretch** | Visual distortion under acceleration or impact. | Subtle scale changes on press (`scale(0.96, 1.04)`); never distort readable text. |
| **2. Anticipation** | A subtle counter-movement before a major action. | A card pulls back slightly (`-4px`) before snapping forward across the screen. |
| **3. Staging** | Clear presentation of an idea without distraction. | One primary element animates while secondary elements pause or dim. |
| **4. Straight Ahead vs Pose to Pose** | Procedural physics vs structured keyframe choreography. | Use physics/springs for continuous interaction; use keyframe timelines for scripted narrative reveals. |
| **5. Follow Through & Overlapping Action** | Elements do not stop simultaneously; parts lag behind. | Stagger child items by 50-80ms; give text a slight lag behind its container. |
| **6. Slow In and Slow Out (Easing)** | Acceleration and deceleration curves. | Never use `linear` for physical objects; use custom cubic-bezier or springs. |
| **7. Arcs** | Natural motion travels along curved paths. | Animate X and Y coordinates with differing easing or along SVG bezier paths. |
| **8. Secondary Action** | Supplementary motion enhancing the main action. | As a card expands, its internal badge fades in and subtle shadow depth deepens. |
| **9. Timing & Spacing** | Number of frames between actions determines perceived weight. | Light elements move quickly (150-250ms); heavy architectural panels move deliberately (500-800ms). |
| **10. Exaggeration** | Amplifying motion to convey intent. | Slightly Overshooting values (`1.05` scale) before settling at `1.0`. |
| **11. Solid Drawing / Geometry** | Maintaining volume, perspective, and balance. | Consistent lighting vectors and 3D perspective across all rendered surfaces. |
| **12. Appeal** | Charisma, cohesion, and craftsmanship. | A unified motion language where all elements feel governed by the same physical laws. |

---

## 2. Easing Curves Math and Bezier Curves

A Cubic Bezier easing function is defined by two control points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ where $x \in [0, 1]$ represents time and $y$ represents progress:

$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3 \quad 	ext{for } t \in [0, 1]$$

### Production Bezier Presets:

```css
/* 1. Fast Out, Slow In (Quintic Out - Universal Entrance) */
--ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);

/* 2. Sharp Snappy Reveal (Expo Out) */
--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);

/* 3. Smooth Cinematic Deceleration (Power4 Out) */
--ease-cinematic: cubic-bezier(0.25, 1, 0.5, 1);

/* 4. Balanced Symmetrical Transition (Quad In-Out) */
--ease-in-out-quad: cubic-bezier(0.45, 0, 0.55, 1);
```

---

## 3. Spring Physics Mechanics

Unlike duration-based easing, springs model true Newtonian physics. A damped harmonic oscillator is governed by:

$$m rac{d^2x}{dt^2} + c rac{dx}{dt} + k x = 0$$

Where:
- $m$ = mass (inertia of the element)
- $k$ = stiffness (restoring force toward target)
- $c$ = damping coefficient (resistance / friction)

### Key Parameters:
- **Damping Ratio ($\zeta = rac{c}{2\sqrt{km}}$)**:
  - $\zeta < 1.0$: Under-damped (overshoots and oscillates).
  - $\zeta = 1.0$: Critically damped (fastest return to equilibrium with zero overshoot).
  - $\zeta > 1.0$: Over-damped (sluggish return, zero bounce).

### Recommended Spring Configurations:

| Interaction Type | Stiffness ($k$) | Damping ($c$) | Mass ($m$) | Perceived Feel |
|---|---|---|---|---|
| **Snappy Button / Toggle** | 400 | 28 | 1 | Crisp, tactile, zero wobble |
| **Card Dismissal / Modal** | 260 | 26 | 1 | Smooth, confident settling |
| **Playful Floating Badge** | 180 | 12 | 1 | Gentle organic oscillation |
