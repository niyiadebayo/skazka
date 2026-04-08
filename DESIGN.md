# Skazka Tours — Visual Storytelling System

## Direction

The site is now structured as a visual narrative instead of a standard landing page.
Each locale follows the same arc:

1. **Opening hook** — emotional invitation and visual promise
2. **Story setup** — how the trip is shaped around feeling and pace
3. **Journey movement** — a day-in-the-life rhythm section
4. **Audience fit** — different traveler archetypes
5. **Planning arc** — how the process unfolds
6. **Practical clarity** — cost, scope, flexibility, safety
7. **Closing chapter** — direct contact CTA

## Core Files

- `assets/site.css` — shared visual system for all locales
- `assets/site.js` — reveal-on-scroll behavior with reduced-motion fallback
- `index.html` — English page
- `ru/index.html` — Russian page
- `de/index.html` — German page
- `fr/index.html` — French page
- `404.html` — branded error page

## Palette

| Token | Value | Purpose |
|---|---|---|
| `--forest-950` | `#0f2017` | deep contrast, dark panels |
| `--forest-900` | `#173223` | hero accents, theme color |
| `--forest-700` | `#2f6247` | emphasis inside display type |
| `--sand-50` | `#fffaf2` | base page tone |
| `--sand-100` | `#f8efdf` | warm surfaces and gradients |
| `--gold-300` | `#dfb885` | warm highlights |
| `--gold-400` | `#cf9a63` | CTA gradient top |
| `--gold-500` | `#b97847` | CTA gradient base, eyebrow text |
| `--ink-950` | `#221c16` | primary text |
| `--ink-700` | `#5f5448` | secondary narrative text |
| `--surface` | `rgba(255, 250, 242, 0.76)` | translucent cards |
| `--line` | `rgba(34, 28, 22, 0.12)` | borders and separators |

## Typography

- **Hero / chapter titles:** `Playfair Display`
- **Card and note titles:** `Cormorant Garamond`
- **Body / UI copy:** `Manrope`

The type system is intentionally mixed:

- `Playfair Display` carries drama and cinematic scale
- `Cormorant Garamond` adds softness to sub-narrative moments
- `Manrope` keeps practical information readable and contemporary

## Layout Principles

- Max content width: `1180px`
- Hero is a two-column cinematic split on desktop, stacked on mobile
- Most chapters use a header row plus a card/grid layout
- Journey chapter shifts into a dark immersive band for contrast and pacing
- Closing CTA mirrors the hero with a final high-emotion panel

## Motion

- Reveal-on-scroll is powered by `IntersectionObserver` in `assets/site.js`
- `.reveal` elements animate upward into place
- `prefers-reduced-motion: reduce` disables transitions and reveals

## Accessibility

- Skip link included on all pages
- Semantic landmarks preserved: `nav`, `main`, `header`, `section`, `footer`
- All CTA states have visible focus outlines
- All imagery uses descriptive `alt` text
- Motion is reduced automatically for users who request it

## Content Posture

Until verified business details are available, the site stays intentionally conservative:

- email-first contact
- no fabricated phone numbers
- no placeholder license claims
- no fake review counts or dead social links

## Imagery

Current images are still served from Unsplash CDN and should be replaced with real brand photography for production. The visual pattern assumes:

- one emotional hero image
- one journey image
- one lifestyle / lodge image
- one closing landscape image

## Notes For Future Iteration

- Reintroduce WhatsApp only when real contact details are available
- Replace stock images with original photography for stronger brand trust
- Add real credentials, social proof, and business metadata once verified
- If the site grows beyond four static locales, move this structure into a template system
