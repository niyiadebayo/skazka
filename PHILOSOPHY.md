# Skazka: design philosophy

Begun November 2026. A first draft, meant to be argued with and rewritten.

`DESIGN.md` says how the site is built. This file says why it looks and behaves the way it does, so that the next decision can be made without asking anyone.

Lines marked **(open)** are proposals that Kimani has not yet confirmed.

## 1. The idea

Skazka means fairy tale. The company's own line is "Kenya, carried by hand."

Put together: a story told by one person, to one small party, by hand. Everything we design should feel like being hosted by someone who knows the land, and never like being sold a package.

The test for any page, picture or sentence: would a good host do this?

## 2. Who we are designing for

A family, a couple or a few close friends, two to six people, planning one of the larger trips of their lives. One of them is doing the research late in the evening, on a phone, and will send a link to the others.

They are not short of money. They are short of trust and of time. They want to know three things quickly: what will it feel like, who will look after us, and what does it cost.

## 3. What we believe

1. **Looked after, not looked at.** Much of luxury design is about being seen. Ours is about being cared for. We show the gesture of service (tea brought to the tent, a route redrawn around a storm) before we show the trophy.
2. **Legibility is hospitality.** A guest should never have to squint. Text contrast, type size and plain words come before atmosphere. The floors are in section 9.
3. **One thought at a time.** A screen carries one idea. Journeys are shown one by one. A statement gets a field to itself.
4. **Say what is true, and no more.** Every number, promise and photograph on the site must be something Skazka can stand behind. Placeholders are labelled as placeholders. Hidden data repeats the visible page.
5. **The land sets the clock.** The site knows what time it is in Kenya and behaves accordingly. The day follows the light, and so do we.
6. **Quiet confidence.** No superlatives, no urgency, no pleading. We describe what we do and let the guest decide.

## 4. The signature

Four things make a page recognisably Skazka. Use them consistently and sparingly.

### The arc

A horizon, the sun's path over it, and the sun. It comes from the day chapter ("The day keeps the sun's hours") and from the fact that near the equator the sun sets at almost the same time all year.

- It is the mark: in the menu, the browser tab, the chat and the footer.
- Full size, it is the clock in "A day in the field", where the sun sits where it really is over Kenya.
- The sun is the only part that takes a colour: brass on dark grounds, laterite on light.

### The field

One colour used whole: laterite, the red earth of Tsavo and Samburu.

- A field holds one thought set large (the statement on the home page) or closes a page (the card beside a photograph).
- One field, one colour for type and mark: ivory on laterite, nothing else.
- At most one statement per page. If everything is a statement, nothing is.

### The lit index

Every page is named large in the footer. The page you are on is lit; the rest are dimmed. It is navigation and signature at once, and it ends every page the same way: the dusk scene, then the index.

### Numerals large, labels small

Figures (a price, a number of days, a step) are set large in the serif. Their captions are small, in the sans, in sentence case. We never use tracked capitals for labels: they shout, and they are harder to read.

### Supporting cast

These are part of the family but not the signature. Do not add more.

- Animal tracks beside chapter labels.
- The small vehicle that drives along the menu bar and along each journey's route.
- The dusk scene of silhouettes that closes each page.
- The running head: a thin line of labels that opens a page or a field (where you are, whose house this is).

## 4a. The grid

Two edges, on every page. If something sits anywhere else, it needs a reason.

- **The page edge.** The menu, every section, and the footer start on the same line.
- **The content column.** One third in, where section titles begin. Introductions, notes and narrow reading blocks (the house rules, the guest letter, the regions list) sit in it, under the title.
- **Wide objects span both.** Grids, spreads, the day strip, the closing card.
- **A field is the exception.** A statement is centred, because it stands alone.
- On a phone there is one edge.

Every page opens the same way: a running head, then the title at full size, on linen. The first section stays on linen; after that, linen and sand alternate. No hairlines between sections; the change of ground is the divider.

**Lines.** Space divides; lines do not. A line is kept only where it does a job:
- rows in a list (questions, regions, house rules, what is included),
- form fields, buttons and tags,
- link underlines,
- the horizon in the day chapter and the drawn routes.

No frames around blocks, no rules above or below a block, no accent bars down the side of a note. One frame remains, around the enquiry form, because paper on linen is too faint to show where the form ends.

## 5. Colour

Colour comes from the photographs. The interface stays out of their way.

| Name | Value | Use |
|---|---|---|
| Linen | `#F6F2EB` | The page |
| Sand | `#EDE6DB` | Alternate bands |
| Paper | `#FFFDF9` | Cards, the form |
| Ink | `#1F1B17` | All copy; night grounds |
| Ink, quiet | `#4A4238` | Labels and captions |
| Ivory | `#FBF7F0` | Type on dark and on the field |
| Laterite | `#6E2B16` | The field; small marks on light grounds |
| Brass | `#D4B272` | Marks and numerals on dark grounds only |

Rules:
- Copy is ink or ivory. Laterite and brass are never used for sentences.
- Brass does not appear on light grounds (it fails contrast there).
- Gradients are light, not decoration: two close stops, as in the day cards and the dusk sky.

## 6. Type

- **Newsreader** for anything said: headlines, statements, names, figures, quotes. Regular weight, tight, large.
- **Hanken Grotesk** for anything explained: paragraphs, labels, buttons.
- No italics anywhere. No bold headlines. No capitals for emphasis.
- Emphasis comes from size and from space, in that order.

## 7. Photography (open)

Today most photographs are stock stand-ins, and each was looked at before it was used. The aim is to replace all of them with Skazka's own.

A direction to shoot towards:
- **The gesture of service.** Hands, not poses: the tea tray, the map on the bonnet, the door held, the bridge crossed on foot.
- **People as hosts.** Kimani and the team at work, named. Guests only with consent, and never as trophies.
- **The light of the hour.** Dawn, the long afternoon, dusk. Avoid the flat light of midday.
- **Room around the subject.** Wide frames that can carry a headline on one side.
- **True captions.** A caption says what is in the picture. It does not claim a place unless we were there.

## 8. Motion

- Motion explains or welcomes. It never decorates and never hides content.
- Nothing starts invisible. If the script fails, the page is still complete.
- Slow and eased: about 0.6 seconds for interface, longer for pictures.
- Everything stops for visitors who ask for reduced motion.

## 9. Floors

These are measured on the rendered page, not assumed.

- Copy: 13:1 contrast or better. Labels: 8:1 or better.
- Nothing smaller than 14px for labels, 16px for copy.
- No font weight under 400.
- Text over a photograph: 7:1 against the actual pixels behind it, or it moves off the photograph.
- Exception, accepted: the dimmed entries in the lit index are 6.3:1. They are 36px or larger.
- No sideways scrolling on a phone. Every control works from the keyboard.

## 10. Voice

Kimani speaks in the first person, plainly, with specifics.

- "I read every enquiry myself" over "Our team is dedicated to you".
- A number or a place in every claim: "three full rest days", "the conservancies that ring the reserve".
- Short sentences, said plainly: "You won't have a typical day. However, this is the rhythm most of them follow, set by the light and the weather of the day."
- No "X, not Y" constructions and no neat reversals ("set by the light, not the clock"). They read as machine-written. Say what the thing is.
- Never: bespoke, curated, unforgettable, once in a lifetime, world-class.

## 11. What we refuse

- Fixed packages presented as products with a "book now" button.
- Countdown timers, "only two places left", pop-ups, newsletter gates.
- Invented reviews, invented guides, invented awards.
- Italics, tracked capitals, drop shadows, glows, grain.
- Decorative lines: frames, dividers between blocks, side bars on notes.
- More than one accent colour on a page.
- Any effect that makes text harder to read.

## 12. Borrowed, and left behind

In November 2026 the structure of this system was sharpened against a brand platform for a premium chauffeur service, shared by the owner as a reference.

Borrowed, because it is structure and not identity:
- very large serif statements with a small running head,
- a stacked index in which the current item is lit and the rest dimmed,
- large numerals with small captions, and numbered pillars,
- one signature colour field, with one colour for type and mark,
- a photograph on one side and a colour panel on the other.

Left behind, because it belongs to that brand:
- its name, logo, palette and typefaces,
- its rounded corners,
- its register. That brand is about arrival and being noticed. Skazka is about being looked after, and about plans that bend.

## 13. Open questions

1. Is laterite the right signature colour, or does Kimani see Skazka in another (the Maasai red, the green of the highlands)?
2. Is the arc the right mark? It replaced a plain "S" without a brief.
3. Which line deserves the statement on the home page? It is currently house rule 03, "The itinerary is a hypothesis."
4. When will first-party photographs replace the stock stand-ins?
5. The animal tracks are stylised. Should a guide redraw them accurately, or should they go?
