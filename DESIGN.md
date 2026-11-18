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

Since November 2026 the colours come from the **"Adeniyi Adebayo" design system** (claude.ai design system artifact). Its rules apply: one accent, no gradients, glows, drop shadows or textures, text at 4.5:1 or better.

| Token | Value | Role on Skazka |
|---|---|---|
| `white` | `#FFFFFF` | Default ground |
| `stone` | `#F4F3EC` | Alternate bands; text on dark grounds |
| `stone-paper` | `#E5E3D9` | Quiet panels |
| `ink` | `#22322E` | Headlines and body text |
| `ink-muted` | `#5A615C` | Secondary text, labels |
| `rule-soft` | `#B9BCB2` | Hairlines |
| `field` | `#33700A` | **The one accent**: eyebrows, italic headline words, buttons, selected chips, links |
| `field-tint` | `#A3D67F` | The accent on tobacco |
| `tobacco` | `#5C4126` | Dark grounds: hero, nav over hero, A day in the field |
| `on-yard-muted` | `#B8B4AC` | Secondary text on tobacco |
| `dawn` | `#E0935C` | The 06:00 moment in A day in the field |
| `granite` | `#1E1C1A` | Before-dawn and night moments |
| `soil-deep` | `#93421B` | Warnings only |

Ultramarine is not used: the system allows field or ultramarine on a page, never both. The hero keeps a dark scrim behind its headline for legibility over the video; that is the only gradient left.

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

## Added November 2026 (inspired by human-md.ai)

- **A day in the field** (`#day`): the safari day as seven sky-coloured moments. A live East Africa Time clock marks the current moment and moves a sun along a track. Without JS, every moment is still visible; only the "now" marker is missing.
- **House rules / SKAZKA.md** (`#house-rules`): a manifesto styled as a markdown file, built only from promises made elsewhere on the page. The same text is served raw at `/skazka.md`; `/llms.txt` summarises the site for AI assistants. Keep all three in sync.
- **Enquiry letter**: the four-step form writes a plain-English note to Kimani as it is filled in, and that note leads the email body. Clicking a sample-journey card adds it as the starting point.
- **Motion rule**: nothing may start hidden and animate in (see the April 2026 removal of scroll reveals). Motion is decorative only and switched off under `prefers-reduced-motion`.
