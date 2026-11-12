import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export const PromoVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Entrance spring
  const scale = spring({ frame, fps, config: { damping: 15, stiffness: 120 } });
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  const textY = interpolate(frame, [0, 25], [40, 0], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: "#020C1B", justifyContent: "center", alignItems: "center" }}>
      <div style={{ textAlign: "center", transform: `scale(${scale})`, opacity }}>
        <h1 style={{ color: "#64FFDA", fontFamily: "sans-serif", fontSize: 90, margin: 0, transform: `translateY(${textY}px)` }}>
          CREATIVE MOTION
        </h1>
        <p style={{ color: "#CCD6F6", fontSize: 32, fontFamily: "sans-serif", marginTop: 20 }}>
          High Performance Programmatic Engineering
        </p>
      </div>
    </AbsoluteFill>
  );
};
