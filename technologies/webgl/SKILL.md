# Technology: WebGL (Bare Metal Rendering)

## 1. Core WebGL Pipeline
- Compile Vertex and Fragment Shaders via `gl.compileShader()`.
- Link into `gl.createProgram()`.
- Bind Vertex Buffer Objects (VBO) and define attribute pointers (`gl.vertexAttribPointer`).
- Bind Uniforms (`gl.uniform1f`, `gl.uniformMatrix4fv`).
- Draw arrays (`gl.drawArrays(gl.TRIANGLES, 0, count)`).
