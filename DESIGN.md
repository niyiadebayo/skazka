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

## Direction: quiet luxury (November 2026)

Researched against Aman (near-monochrome warm neutrals, colour only from photographs, an editorial serif with a quiet sans, square corners, generous space) and Gentle Monster (gallery presentation, extreme negative space, thin rules). This replaces the short-lived adoption of the "Adeniyi Adebayo" design system palette and type.

**Principles**
- **Space is material (ma).** Sections breathe: 120–224px of padding, 64–112px under each headline.
- **Colour comes from the photographs.** The interface stays in warm linen to charcoal; the one accent is a deep dry-grass brown.
- **Light, not weight.** Headlines in a light serif; emphasis by italic and tone, never by bold or colour blocks.
- **Hairlines and square corners.** Borders at 14–32% charcoal; no radii except the round mark.
- **Gradients as light, not decoration.** Two close stops only: section washes (sand to linen), the day chapter (night to dusk), the day moments.
- **Slow and sparse motion.** 0.6s eased transitions, a 1.8s image drift on hover, the hero video fading in over the poster. Nothing starts hidden.

## Palette

| Token | Value | Use |
|---|---|---|
| linen `--bg` | `#F5F1EA` | Page ground |
| sand `--bg-2` | `#ECE5DA` | Washed bands (method, house rules, FAQ), footer |
| paper `--surface` | `#FBF9F5` | Cards, the form, the SKAZKA.md file |
| charcoal `--ink` | `#2A2622` | Text (13.3:1 on linen); primary buttons |
| taupe `--ink-dim` | `#6B6358` | Secondary text, labels, italic accents (4.7:1 on sand) |
| dry grass `--accent` | `#6A5B42` | The one quiet accent (5.3:1 on sand) |
| night | `#24201C` | Hero and day chapter grounds |
| bone | `#EFE9DF` | Text on night (13.4:1) |
| mist | `#C9BFB1` | Secondary text on night (8.9:1) |
| pale grass | `#D8C8A8` | Accent on night |

## Typography

- **Newsreader** (Google Fonts, optical sizes): headlines at weight 300, card heads at 400, quotes and the enquiry note. Closest free match to Aman's Lyon.
- **Hanken Grotesk**: body at 16/1.75, and labels as small capitals (11.5px, 500, 0.2em tracking). Closest free match to Aman's Whitney.
- Headline sizes: hero 46–92px, section titles 34–54px, card heads 22–28px.

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
