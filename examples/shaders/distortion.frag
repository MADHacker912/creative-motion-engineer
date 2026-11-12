precision highp float;
uniform sampler2D tDiffuse;
uniform float uDistortion;
uniform float uTime;
varying vec2 vUv;

void main() {
    vec2 dir = vUv - vec2(0.5);
    float dist = length(dir);
    vec2 offset = dir * dist * uDistortion;

    float r = texture2D(tDiffuse, vUv + offset).r;
    float g = texture2D(tDiffuse, vUv).g;
    float b = texture2D(tDiffuse, vUv - offset).b;

    gl_FragColor = vec4(r, g, b, 1.0);
}
