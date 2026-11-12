export function drawSvgOutline(path: SVGPathElement) {
  const length = path.getTotalLength();
  path.style.strokeDasharray = `${length}`;
  path.style.strokeDashoffset = `${length}`;
  path.getBoundingClientRect(); // force reflow

  path.style.transition = "stroke-dashoffset 1.4s cubic-bezier(0.22, 1, 0.36, 1)";
  path.style.strokeDashoffset = "0";
}
