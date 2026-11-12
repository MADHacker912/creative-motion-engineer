import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

export function initScrollStory(track: HTMLElement, panels: HTMLElement[], metricCounter: HTMLElement) {
  const ctx = gsap.context(() => {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: track,
        start: "top top",
        end: `+=${panels.length * 100}%`,
        pin: true,
        scrub: 1,
        anticipatePin: 1
      }
    });

    panels.forEach((panel, i) => {
      if (i > 0) {
        tl.fromTo(panel, 
          { opacity: 0, scale: 0.85, y: 50 }, 
          { opacity: 1, scale: 1, y: 0, duration: 1 }
        );
      }
    });

    const metric = { val: 0 };
    tl.to(metric, {
      val: 99.9,
      duration: 2,
      onUpdate: () => {
        metricCounter.textContent = `${metric.val.toFixed(1)}%`;
      }
    }, "<");
  }, track);

  return () => ctx.revert();
}
