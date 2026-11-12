# Parallax: Optical Depth and Layered Movement

## 1. Golden Rules of Parallax
- **Foreground Fast, Background Slow**: Foreground elements move faster than the scroll velocity; distant horizons move slower.
- **Never Parallax Body Text**: Only apply parallax to images, decorative geometries, and background cards. Parallaxing readable text causes reading frustration.
- **Transform Only**: Always use `transform: translate3d(0, y, 0)` to keep rendering on the GPU compositor thread.
