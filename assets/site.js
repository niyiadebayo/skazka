const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const reveals = document.querySelectorAll(".reveal");

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0.01, rootMargin: "0px 0px -20px 0px" }
  );

  for (const item of reveals) observer.observe(item);
  document.documentElement.classList.add("js-enhanced");
} else {
  for (const item of reveals) item.classList.add("is-visible");
}
