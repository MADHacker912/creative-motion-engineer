# Technology: GSAP (GreenSock Animation Platform)

## 1. Overview & Best Practices
GSAP is the industry standard for high-performance scripted web animation. 

### Core Rules:
1. **Always Use gsap.context() in Frameworks**: Prevent React 18+ strict-mode double-invocations and memory leaks.
2. **Batch Transforms**: GSAP optimizes `x`, `y`, `scale`, `rotation`, `skew` into a single `transform: matrix3d()`.
3. **Avoid Overlapping Tweens**: Use timelines rather than uncoordinated standalone `gsap.to()` calls.
