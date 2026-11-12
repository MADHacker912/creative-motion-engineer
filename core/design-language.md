# Design Language: Systems, Tokens, and Aesthetics

## 1. Motion Tokens Architecture

Treat motion tokens with the same mathematical rigor as typography scales and spacing grids.

### 1.1 Duration Scale
- `duration-instant`: `100ms` — Tooltips, micro-toggles, active state feedback.
- `duration-fast`: `200ms` — Button hovers, small dropdown expansions.
- `duration-normal`: `350ms` — Modal entrances, card reveals, drawer slides.
- `duration-deliberate`: `600ms` — Section transitions, hero graphic reveals.
- `duration-cinematic`: `1000ms+` — Full-screen page wipe, slow atmosphere drift.

### 1.2 Stagger Scale
- `stagger-tight`: `40ms` — Character-by-character kinetic type.
- `stagger-normal`: `75ms` — List items, navigation links, grid cards.
- `stagger-loose`: `120ms` — Feature sections, sequential imagery.

---

## 2. Approved Color Dynamics & Luxury Palettes

Reject generic AI purple-blue gradients. Adopt intentional, high-contrast palettes:

### Palette A: Royal Dark Navy (High-Tech Enterprise & Luxury SaaS)
- **Base Background**: `#020C1B` (Deep Abyssal Navy)
- **Surface Layer**: `#0A192F` (Muted Steel Slate)
- **Border / Divider**: `rgba(100, 255, 218, 0.1)` (Subtle Cyan Ray)
- **Primary Text**: `#CCD6F6` (Frost Titanium)
- **Accent Signal**: `#64FFDA` (Electric Mint / Cyan Accent)

### Palette B: Warm Editorial Neutral (Publishing, Luxury Goods, Architecture)
- **Base Background**: `#F7F5F0` (Alabaster Paper)
- **Surface Layer**: `#FFFFFF` (Crisp Linen)
- **Border / Divider**: `rgba(34, 34, 34, 0.08)` (Soft Charcoal Rule)
- **Primary Text**: `#1A1A1A` (Cast Iron Black)
- **Accent Signal**: `#C2593F` (Terracotta Brick)

### Palette C: Monolith Cyber-Brutalist (Developer Tools, Terminals, Web3)
- **Base Background**: `#0D0E11` (Obsidian Core)
- **Surface Layer**: `#16181D` (Carbon Frame)
- **Border / Divider**: `#262930` (Milled Aluminum)
- **Primary Text**: `#E6EDF3` (Pure White Mono)
- **Accent Signal**: `#00F0FF` (Laser Neon Blue)

---

## 3. Typography Integration with Motion

Motion must honor typographic integrity:
1. **Never Distort Text Aspect Ratio**: Do not animate `scaleX` and `scaleY` unequally on text nodes.
2. **Masking Over Scaling**: Reveal text using parent `overflow: hidden` containers with vertical transforms (`translateY(110%)` to `translateY(0%)`).
3. **Variable Fonts**: Animate font weight (`wght` axis: 300 to 700) or slant (`slnt` axis) for fluid typographical state changes.
