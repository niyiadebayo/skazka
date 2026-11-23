# Content for the Skazka site. build.py turns this into pages and structured data.
# Text may contain HTML entities and  (rendered without italics).

FAQ = [('How is Skazka different from a regular safari operator?',
  "Most operators sell fixed packages and hand you off between a dozen vendors. We run one team &mdash; twenty-five people I've trained personally &mdash; and "
  'the same guide stays with you for the whole trip. There is no package. Every journey is written for the specific guests coming.'),
 ('Who actually leads the trip day-to-day?',
  "I do, for most trips &mdash; and when I can't, it is one of three senior guides I've worked with for six years or more. You will always know who it is "
  'before you arrive, and speak with them directly during planning.'),
 ("What does 'engineer's approach' actually mean in practice?",
  "Three things. One &mdash; camp logistics are thought through the way I'd design a system: redundancy on vehicles, power, and water; honest risk margins. "
  "Two &mdash; I weave Kenya's engineering history into the guiding, because you can't understand a migration route without understanding the railway that cut "
  'through it. Three &mdash; if a storm cuts a road, we route around it rather than cancelling a day.'),
 ('Group size and privacy?',
  'We only take small parties &mdash; couples, families, and close-friend groups up to six. One vehicle, one guide, one chef. We do not pool strangers. Ever.'),
 ('What is included in the price?',
  'Everything after you land: all camps and lodging, all meals, all transfers including charter flights where relevant, park and conservancy fees, the guide '
  'and crew, and the concierge throughout. International flights and visas are yours.'),
 ('Can plans change mid-trip?',
  "Yes &mdash; that is the point. If the leopard cubs have come back and you want another night, we stay. If you've had enough bush and want Lamu two days "
  'early, we move. Flexibility is the product.'),
 ('When should I book?',
  'Six to twelve months before travel is comfortable. For July&ndash;October (Mara migration peak) we are often full a year out. We hold small windows for '
  'last-minute guests &mdash; ask.'),
 ('What about children?',
  'Welcome. I have taken guests as young as five. For children under ten we adjust pace, driving hours, and walking &mdash; the trip becomes calmer, not less '
  'interesting.'),
 ('How much does a private Kenya safari cost?',
  'Our sample journeys start from $6,800 per person for five days, $12,600 for ten days and $16,200 for fourteen days, based on sharing. That covers '
  'everything after you land: camps, meals, transfers, park and conservancy fees, your guide and crew. International flights and visas are yours. Your own '
  'trip is priced in one clear document, with the reason for every choice.'),
 ('Do you have Russian-speaking guides?',
  'Yes. I speak English, Swahili and Russian, and I studied in Kazan. Our manager Elena is Russian-speaking, and the rest of the team is multilingual.'),
 ('When is the best time to go on safari in Kenya?',
  'It depends on the region. The Maasai Mara is at its best from July to October, during the migration; I also like late June, before the crowds. Laikipia is '
  'good all year. Samburu runs from June to March, Amboseli from June to October and again in January and February, Tsavo from June to October, and Lamu and '
  'the coast are best from November to March.')]

JOURNEYS = [{'key': 'Mara Classic, our way',
  'title': 'Mara Classic, our way',
  'desc': 'The Mara without the crowds. Private conservancies, night drives, and a rivercamp only reached by foot across a hippo bridge.',
  'days': 10,
  'price': '$12,600',
  'img': 'https://images.unsplash.com/photo-1518709594023-6eab9bab7b23?w=1400&q=80',
  'alt': 'Zebras in tall golden grass under a blue sky',
  'w': 1400,
  'h': 933,
  'stops': ['Private conservancies', 'The river camp']},
 {'key': 'Coast, craft &amp; bush',
  'title': 'Coast, craft, &amp; bush',
  'desc': 'A full sweep &mdash; bush camps in Tsavo, dhow sailing in Lamu, a tailor in Malindi. Built for couples who want the land and the ocean.',
  'days': 14,
  'price': '$16,200',
  'img': '/assets/lamu-sunset.jpg',
  'alt': 'Sunset over the Lamu archipelago',
  'w': 1400,
  'h': 1050,
  'stops': ['Tsavo', 'Lamu', 'Malindi']},
 {'key': 'The short sabbatical',
  'title': 'The short sabbatical',
  'desc': 'For guests with little time. A private conservancy in Laikipia, three guided walks, one hot-air balloon at dawn. Nothing more.',
  'days': 5,
  'price': '$6,800',
  'img': 'https://images.unsplash.com/photo-1519659528534-7fd733a832a0?w=1400&q=80',
  'alt': 'A hot-air balloon above the plains, with wildebeest below',
  'w': 1400,
  'h': 933,
  'stops': ['Laikipia']}]

U = 'https://images.unsplash.com/photo-'
REGIONS = [
 dict(slug='maasai-mara', name='Maasai Mara', sub='Southwest &middot; 1,510 km&sup2;', season='Jul&ndash;Oct best',
      desc='The great northern extension of the Serengeti. We work only in the private conservancies that ring the reserve &mdash; Olare Motorogi, Mara North, Naboisho &mdash; where vehicles are limited and off-road is permitted.',
      img=U+'1535082623926-b39352a03fb7?w=1400&q=80', alt='Wildebeest and a safari vehicle on the open plains', w=1400, h=933,
      stats=[('Drive time', '5h'), ('Elevation', '1,650m'), ('Best for', 'Big cats')]),
 dict(slug='laikipia', name='Laikipia', sub='Central highlands &middot; 9,500 km&sup2;', season='Year-round',
      desc='A plateau of private conservancies north of Mt. Kenya, stitched together from former cattle ranches. Rhinos, wild dogs, walking safaris, fly camps under the stars. My favorite place in Kenya.',
      img=U+'1535338454770-8be927b5a00b?w=1400&q=80', alt='A rhino and her calf in dry grass', w=1400, h=933,
      stats=[('Drive time', '3.5h'), ('Elevation', '1,800m'), ('Best for', 'Walking')]),
 dict(slug='samburu', name='Samburu', sub='Northern &middot; Ewaso Nyiro basin', season='Jun&ndash;Mar',
      desc="Dry, red country. Home to the 'Samburu Special Five' &mdash; reticulated giraffe, Grevy's zebra, gerenuk, beisa oryx, Somali ostrich &mdash; and no one else's itinerary. We fly in, then drive doubletracks.",
      img=U+'1523805009345-7448845a9e53?w=1400&q=80', alt='A giraffe behind a thorn tree in warm evening light', w=1400, h=933,
      stats=[('Flight', '1h 15m'), ('Elevation', '900m'), ('Best for', 'Rare species')]),
 dict(slug='amboseli', name='Amboseli', sub='South &middot; 392 km&sup2;', season='Jun&ndash;Oct, Jan&ndash;Feb',
      desc='The elephant country. Kilimanjaro rises across the border in Tanzania and makes the photographs. Our camp is on a private concession outside the park &mdash; quieter mornings, fewer vehicles.',
      img='/assets/amboseli-elephants.jpg', alt='A family of elephants on the grass plain, Amboseli', w=1400, h=1050,
      stats=[('Drive time', '4h'), ('Elevation', '1,140m'), ('Best for', 'Elephants')]),
 dict(slug='lamu', name='Lamu &amp; the coast', sub='Northeast &middot; Indian Ocean', season='Nov&ndash;Mar best',
      desc='A Swahili island with no cars, a donkey sanctuary, and tailors who have been cutting linen for four generations. We finish many safaris here &mdash; three days of doing very little.',
      img='/assets/lamu-sunset.jpg', alt='Sunset over the Lamu archipelago, Indian Ocean coast', w=1400, h=1050,
      stats=[('Flight', '2h'), ('Humidity', 'High'), ('Best for', 'Rest')]),
 dict(slug='tsavo', name='Tsavo', sub='South-central &middot; 22,000 km&sup2;', season='Jun&ndash;Oct',
      desc='Red-dust elephants and the hardest-earned sightings in Kenya. For guests who have been on safari before and want space, solitude, and distance from the circuit.',
      img=U+'1547471080-7cc2caa01a7e?w=1400&q=80', alt='A lone acacia over red earth at sunset', w=1400, h=933,
      stats=[('Drive time', '5h'), ('Elevation', '500m'), ('Best for', 'Solitude')]),
]

# Guides and languages. placeholder=True marks a profile that is not yet a real person:
# the card says so, and these languages are kept out of the structured data and llms.txt until it is.
GUIDES = [
 dict(face='English &middot; Kiswahili &middot; &#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;', lang='en', role='Founder and lead guide', name='Kimani Kennedy Muna',
      text='KPSGA silver-licensed guide and former electrical engineer. Leads most trips himself.', placeholder=False),
 dict(face='&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;', lang='ru', role='Manager', name='Elena',
      text='Our Russian-speaking manager, part of the team that runs every trip.', placeholder=False),
 dict(face='&#26085;&#26412;&#35486;', lang='ja', role='Guide', name='Japanese-speaking guide',
      text='A guide for Japanese-speaking guests. Name, licence and story to follow.', placeholder=True),
 dict(face='&#54620;&#44397;&#50612;', lang='ko', role='Guide', name='Korean-speaking guide',
      text='A guide for Korean-speaking guests. Name, licence and story to follow.', placeholder=True),
 dict(face='Espa&ntilde;ol', lang='es', role='Guide', name='Spanish-speaking guide',
      text='A guide for Spanish-speaking guests. Name, licence and story to follow.', placeholder=True),
]
LANGS_SHORT = 'EN &middot; SW &middot; RU &middot; JA &middot; KO &middot; ES'
LANGS_LONG = 'English, Swahili, Russian, Japanese, Korean and Spanish'
