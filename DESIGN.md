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

## Direction: quiet luxury, legible (November 2026)

Researched against Aman (warm neutrals, colour only from photographs, an editorial serif with a quiet sans, square corners, generous space) and Gentle Monster (gallery presentation, negative space, thin rules). The first pass was too faint; a rendered-page audit found body copy at 4.7:1, 11.5px labels, and hero text at 2-4:1 over the sky. These floors now apply.

**Legibility floors (measured on the rendered page, not assumed)**
- Copy is `--ink` (13:1 or better on every ground). Labels and captions are `--ink-dim` (8:1 or better).
- Nothing under 12.5px. No font weight under 400.
- Hero and nav text: 6.9:1 or better against the actual video pixels (worst case, brightest 10% behind each line).
- The accent is for marks (dots, rules, the progress line), never for copy.
- Emphasis in headlines is italic only, same colour.

**Principles**
- **Space is material.** Sections carry 112-192px of padding.
- **Colour comes from the photographs.** The interface stays linen to near-black.
- **Hairlines you can see.** Borders at 20-50% ink; square corners.
- **Gradients as light.** Two close stops only (the day moments); the hero scrim darkens the left third and the land, and leaves the sun alone. The scrim must sit above the video (`z-index: 2`).
- **Slow, sparse motion.** 0.6s eased transitions. Nothing starts hidden.

**Hero**
- Desktop: words on the left over a scrim; the four facts are a bottom strip on the dark land.
- Phone: the picture fills the top 56vh, and the words sit beneath it on solid ground.

**Small delights**
- The hero line and the day chapter follow the Kenya clock ("16:00 in Kenya · the afternoon drive is out").
- A 2px reading-progress line at the top (CSS scroll timeline; absent where unsupported).
- Underlines that draw in on links; a tick on chosen chips; the enquiry note brightens briefly when it rewrites itself.

## Palette

| Token | Value | Use |
|---|---|---|
| linen `--bg` | `#F6F2EB` | Page ground |
| sand `--bg-2` | `#EDE6DB` | Alternate bands, footer |
| paper `--surface` | `#FFFDF9` | Cards, the form, the SKAZKA.md file |
| ink `--ink` | `#1F1B17` | All copy and headlines (15.3:1 on linen); primary buttons; night grounds |
| ink-dim `--ink-dim` | `#4A4238` | Labels and captions (8.0:1 on sand) |
| ember `--accent` | `#A0481C` | Marks only |
| bone | `#F3EDE3` | Text on night (14.7:1) |
| mist | `#D5CBBD` | Labels on night (10.7:1) |
| apricot | `#F0BE8E` | Marks on night |

## Typography

- **Newsreader**: headlines at 400, card heads at 500, quotes and the enquiry note at 400.
- **Hanken Grotesk**: body at 17/1.7; labels at 12.5px, 600, 0.14em, uppercase.
- Sizes: hero 48-88px, section titles 36-56px, card heads 23-29px, reading passages 21-22px.

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
