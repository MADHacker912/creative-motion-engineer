# 3D Modelling & Topology for Real-Time WebGL

## 1. Polygon Budgets for WebGL
In real-time web applications, poly-count directly affects vertex shader processing and download weight:

| Scene Complexity | Mobile Target | Desktop Target |
|---|---|---|
| **Simple Hero Object** | 10k - 25k triangles | 40k - 80k triangles |
| **Complex Product (Watch / Car)** | 35k - 60k triangles | 100k - 200k triangles |
| **Full Architectural Scene** | 80k - 150k triangles | 300k - 600k triangles |

---

## 2. Hard-Surface Topology & Beveling
- **Never sharp 90-degree edges**: In reality, no surface has an infinitely sharp edge. Always model a subtle chamfer or micro-bevel (1-2 segments) to capture specular light glints.
- **Normal Map Baking**: High-frequency surface detail (screws, vents, engraved text) should be baked from a high-poly sculpt into a 16-bit tangent normal map rather than modeled in raw geometry.
