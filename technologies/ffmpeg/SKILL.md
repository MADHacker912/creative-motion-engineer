# Technology: FFmpeg Video & Audio Mastering

## 1. Essential Production Commands

### Two-pass High Quality MP4:
```bash
ffmpeg -y -i input.mov -c:v libx264 -b:v 3000k -pass 1 -an -f null /dev/null && ffmpeg -y -i input.mov -c:v libx264 -b:v 3000k -pass 2 -c:a aac -b:a 192k output.mp4
```

### Image Sequence to 60fps MP4:
```bash
ffmpeg -y -framerate 60 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p video.mp4
```

### Audio Loudness Normalization (EBU R128):
```bash
ffmpeg -y -i input_audio.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 normalized.mp3
```
