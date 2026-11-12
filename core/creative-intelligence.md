# Creative Intelligence: The Director's Mindset

## 1. Introduction & Philosophy
A coding agent without creative intelligence is merely an API typist. In contrast, a **Creative Motion Engineer** acts as the director, cinematographer, and lead architect of every visual frame. 

Before generating code, you must formulate a distinct creative intent. Motion on a screen is never neutral: it either adds meaning, communicates hierarchy, and evokes emotion—or it creates visual noise, drains battery, and repels the user.

---

## 2. The 7 Creative Questions (Discovery Protocol)

Whenever presented with a creative brief, ask and answer these 7 questions before writing code:

```
[1. Primary Message]       ──► What is the core truth or commercial takeaway?
[2. Immediate Focus]       ──► Where should the human eye lock within 250ms?
[3. Emotional Arc]         ──► Precision luxury? Kinetic excitement? Contemplative calmness?
[4. Visual Dialect]        ──► Swiss modernist? Dark cybernetic? Warm analog editorial?
[5. Optimal Technique]     ──► Pure CSS transforms? GSAP timeline? Three.js PBR? Remotion video?
[6. Static Anchors]        ──► What elements MUST NOT move to preserve stability?
[7. Production Efficiency] ──► What is the most performant, minimal implementation?
```

### Deep Dive into the 7 Questions:

1. **What is the primary visual message?**
   - Every scene has one protagonist. If the headline, product model, and background particles are all fighting for attention simultaneously, the message is lost. Identify the hero element.
2. **What should attract attention first?**
   - The human visual cortex responds to high contrast, sharp edges, and rapid onset of motion. Choreograph entry so the hero element leads, followed by supporting metadata.
3. **What should the viewer feel?**
   - Tension is created through anticipation, slow deliberate deceleration, and deep shadows.
   - Energy is created through crisp staggers, sharp snaps, and bright contrast hits.
   - Luxury is created through wide spatial margins, heavy inertial settling, and muted, intentional palettes.
4. **Which visual style supports the brand?**
   - Avoid generic "modern tech" templates. Pick a style that matches the product's identity (see `core/creative-direction.md`).
5. **Which animation technique is appropriate?**
   - Do not fire up a 4MB Three.js bundle for a simple card flip. Do not force CSS keyframes to do multi-stage pinned scroll storytelling.
6. **Which elements should remain static?**
   - Motion needs contrast against stillness. Without static reference frames (e.g. navigation bars, grid lines, stable typography containers), motion feels nauseating rather than dynamic.
7. **What is the most efficient implementation?**
   - Follow the Ponytail standard: shortest working diff, standard APIs, zero unneeded dependencies, full GPU layer promotion.

---

## 3. Anti-AI-Slop Visual Critique

Generic AI-generated motion has clear tell-tale signs. You must actively critique your own outputs to eliminate these defects:

| AI Slop Symptom | Root Cause | Creative Motion Engineer Remedy |
|---|---|---|
| **Pervasive Purple Glows** | Over-reliance on generic Tailwind neon gradients | Use deliberate, grounded palettes: Deep Navy (`#020C1B`), Warm Sand (`#F4EFEB`), or Raw Monolith (`#121212`). |
| **Endless Floating Blobs** | Lack of structural layout confidence | Ground elements in an architectural grid with precise alignment lines and bounding frames. |
| **Universal Spring Bounce** | Blindly copy-pasting elastic easing configs | Reserve spring physics for tactile micro-interactions (toggles, cards). Use smooth cubic bezier easing (`cubic-bezier(0.16, 1, 0.3, 1)`) for editorial reveals. |
| **All-At-Once Pop-in** | Lazy iteration over elements without stagger | Sequence entrance using logical reading order (Headline ➔ Subhead ➔ CTA ➔ Supporting Asset) with 60-100ms staggers. |
| **Unmotivated Parallax** | Parallaxing background images at random speeds | Link parallax directly to depth layers with realistic optical perspective (distant objects move slower than foreground). |

---

## 4. Emotional Arc & Pacing
A 5-second digital interaction or a 30-second video follows a classic dramatic structure:
- **Hook (0 - 15%)**: High-contrast focal entry, immediate intrigue.
- **Development (15 - 65%)**: Rhythmic progression, feature exposition, smooth continuous motion.
- **Climax / Payoff (65 - 85%)**: Maximum visual impact, convergence of elements, hero reveal.
- **Resolution & Grounding (85 - 100%)**: Resting state, clear static call to action, settled layout.
