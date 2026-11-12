# Technology: React Three Fiber (R3F) & Drei

## 1. Componentized 3D in React
R3F translates Three.js objects into a declarative React component tree:
```tsx
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Float, ContactShadows, Environment } from "@react-three/drei";
import { useRef } from "react";
import * as THREE from "three";

function FloatingProduct() {
  const meshRef = useRef<THREE.Mesh>(null!);

  useFrame((_, delta) => {
    meshRef.current.rotation.y += delta * 0.4;
  });

  return (
    <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
      <mesh ref={meshRef}>
        <boxGeometry args={[1.5, 1.5, 1.5]} />
        <meshStandardMaterial color="#0A84FF" roughness={0.2} metalness={0.8} />
      </mesh>
    </Float>
  );
}

export function ProductCanvas() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 45 }} dpr={[1, 2]}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 10, 5]} intensity={1.5} />
      <FloatingProduct />
      <ContactShadows position={[0, -1.8, 0]} opacity={0.4} scale={5} blur={2} />
      <Environment preset="city" />
    </Canvas>
  );
}
```
