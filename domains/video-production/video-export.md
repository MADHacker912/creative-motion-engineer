# Video Export: Codecs, Bitrates, and Master Delivery

## 1. Master Export Presets

| Target Platform | Resolution | Aspect Ratio | Frame Rate | Codec | Target Bitrate |
|---|---|---|---|---|---|
| **YouTube 4K Master** | 3840x2160 | 16:9 | 60 fps | H.264 / ProRes 422 | 45 - 65 Mbps |
| **Web Hero Background** | 1920x1080 | 16:9 | 30 fps | H.264 (MP4) + VP9 (WebM) | 2.5 - 4.5 Mbps |
| **Transparent Web Video** | 1080x1080 | 1:1 | 30 / 60 fps | VP9 with Alpha (WebM) | 3 - 6 Mbps |
| **Instagram Reel / TikTok** | 1080x1920 | 9:16 | 30 / 60 fps | H.264 High Profile | 12 - 16 Mbps |

---

## 2. Production FFmpeg Commands

### Web-Optimized MP4 (Two-Pass, Fast-Start Streaming):
```bash
ffmpeg -y -i input_master.mov -c:v libx264 -preset slow -b:v 3500k   -maxrate 4500k -bufsize 7000k -pix_fmt yuv420p -movflags +faststart   -c:a aac -b:a 160k output_web.mp4
```

### Transparent WebM (Alpha Channel Preserved):
```bash
ffmpeg -y -i master_with_alpha.mov -c:v libvpx-vp9 -pix_fmt yuva420p   -b:v 2500k -auto-alt-ref 0 output_transparent.webm
```
