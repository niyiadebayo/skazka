# Skazka Tours — Design Tokens

## Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--green` | `#1a3a2a` | Headers, hero background, footer |
| `--green-deep` | `#0f2218` | Hero fallback, deep accents |
| `--green-light` | `#2d5a3f` | Card borders, hover states |
| `--ochre` | `#c4956a` | CTAs, accents, step numbers, gold lines |
| `--ochre-light` | `#d4a87a` | Hover states for ochre elements |
| `--gold` | `#b8963e` | Decorative quote marks |
| `--ivory` | `#FFFBF5` | Page background |
| `--ivory-warm` | `#f5efe6` | FAQ section background tint |
| `--text` | `#2C2C2C` | Body text |
| `--text-light` | `#5a5247` | Secondary text |
| `--text-muted` | `#8a8278` | Muted/tertiary text |
| `--border` | `#e0d8cc` | Dividers, borders |
| `--wa-green` | `#25D366` | Primary contact CTA |

## Typography

- **Headings (h1, h2):** Playfair Display, 400-500 weight, serif
- **Subheadings (h3):** Cormorant Garamond, serif
- **Body:** Cormorant Garamond, 17px base, line-height 1.7
- **UI elements:** -apple-system, BlinkMacSystemFont, sans-serif
- **Section labels:** System sans, 0.65-0.7rem, letter-spacing 0.3-0.5em, uppercase

## Imagery

All images via Unsplash CDN. Replace with real trip photography for production.

| Section | Image | Unsplash ID |
|---------|-------|-------------|
| Hero | Giraffes at golden hour | `photo-1547471080-7cc2caa01a7e` |
| Photo break 1 | Elephants crossing savanna | `photo-1535338454528-1b22dc78db53` |
| Photo break 2 | Leopard in sunlight | `photo-1549366021-9f761d450615` |
| How it works bg | Safari lodge | `photo-1516426122078-c23e76319801` |
| Photo break 3 | Kilimanjaro | `photo-1611241893603-3c228ee0ae6f` |
| Footer bg | Savanna sunset | `photo-1523805009345-7448845a9e53` |

## Effects

- **Glassmorphism:** `backdrop-filter: blur(12px)` with `rgba(255,251,245,0.08)` background
- **Parallax:** `background-attachment: fixed` on photo break sections
- **Gold line accents:** 60px `--ochre` underline on section headings
- **Card treatment:** `rgba(255,251,245,0.06)` background, 1px border `rgba(255,251,245,0.1)`
- **Hover shadows:** `box-shadow: 0 20px 50px rgba(0,0,0,0.3)` on card hover

## Layout

- **Max content width:** 800px (text sections), 900px (step cards grid)
- **Section padding:** 5rem 2rem (desktop), 4rem 1.5rem (mobile)
- **Breakpoint:** 768px (mobile/desktop split)
- **Testimonial grid:** 2x2 on desktop, stacked on mobile
- **Step cards:** 3-column grid on desktop, stacked on mobile

## Dark Mode

Automatic via `prefers-color-scheme: dark`. Overrides `--ivory`, `--text`, `--text-light`, `--text-muted`, `--border`.

## Accessibility

- WCAG 2.1 AA color contrast
- `prefers-reduced-motion: reduce` disables parallax and transitions
- All images have descriptive alt text
- Keyboard navigable
- Semantic HTML landmarks
