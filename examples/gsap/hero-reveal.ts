import { gsap } from "gsap";

export interface HeroElements {
  container: HTMLElement;
  badge: HTMLElement;
  titleWords: HTMLElement[];
  description: HTMLElement;
  ctaGroup: HTMLElement;
  heroMedia: HTMLElement;
}

export function initHeroReveal(elements: HeroElements) {
  // Respect reduced motion
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    gsap.set([elements.badge, elements.titleWords, elements.description, elements.ctaGroup, elements.heroMedia], {
      opacity: 1,
      y: 0,
      scale: 1
    });
    return () => {};
  }

  const ctx = gsap.context(() => {
    const tl = gsap.timeline({
      defaults: { ease: "power4.out", duration: 1.1 }
    });

    tl.from(elements.badge, {
      opacity: 0,
      y: -15,
      duration: 0.8
    })
    .from(elements.titleWords, {
      opacity: 0,
      y: "110%",
      rotateZ: 2,
      stagger: 0.05
    }, "-=0.5")
    .from(elements.description, {
      opacity: 0,
      y: 20,
      duration: 0.9
    }, "-=0.7")
    .from(elements.ctaGroup, {
      opacity: 0,
      scale: 0.96,
      duration: 0.8,
      ease: "back.out(1.5)"
    }, "-=0.6")
    .from(elements.heroMedia, {
      opacity: 0,
      scale: 0.92,
      duration: 1.4,
      ease: "power3.out"
    }, "-=1.0");
  }, elements.container);

  return () => ctx.revert();
}
