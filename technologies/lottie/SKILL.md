# Technology: Lottie & dotLottie Vector Playback

## 1. High Performance Lottie Guidelines
- Prefer `.lottie` (dotLottie) container over `.json` (typically 70% smaller).
- Avoid complex vector effects like Drop Shadows or Trim Paths on complex groups, which cause canvas CPU spikes.
