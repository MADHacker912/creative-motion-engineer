varying vec2 vUv;
varying vec3 vNormal;
uniform float uTime;

void main() {
    vUv = uv;
    vNormal = normal;
    vec3 pos = position;
    // Gentle sine displacement
    pos.z += sin(pos.x * 3.0 + uTime) * 0.1;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
}
