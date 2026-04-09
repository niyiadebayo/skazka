const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const reveals = document.querySelectorAll(".reveal");

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "none";
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.01, rootMargin: "0px 0px -20px 0px" }
  );

  for (const item of reveals) {
    item.style.opacity = "0";
    item.style.transform = "translateY(28px)";
    item.style.transition = "opacity 0.7s ease, transform 0.7s ease";
    observer.observe(item);
  }
}
