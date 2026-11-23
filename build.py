#!/usr/bin/env python3
"""Build the Skazka Tours site.

Edit the files in src/ (content.py for text and data, parts/ and sections/ for markup,
site.css and site.js for look and behaviour), then run:  python3 build.py

Output is written to the repository root and committed, so Cloudflare needs no build step.
The stylesheet and script are written with a content hash in their names, because
everything under /assets/ is cached by browsers for a year.
"""
import hashlib, html, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
sys.path.insert(0, SRC)
import content as C  # noqa: E402

SITE = 'https://skazka.tours'
TODAY = date.today().isoformat()
LINEN, SAND = '#F6F2EB', '#EDE6DB'


def read(*p):
    with open(os.path.join(SRC, *p), encoding='utf-8') as f:
        return f.read()


def text(x):
    """HTML fragment -> plain text, for structured data."""
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()


def slug(x):
    return re.sub(r'[^a-z0-9]+', '-', text(x).lower()).strip('-')


JSLUG = {'Mara Classic, our way': 'mara-classic', 'Coast, craft &amp; bush': 'coast-craft-bush', 'The short sabbatical': 'the-short-sabbatical'}

# ---------------------------------------------------------------- shared pieces

NAV = [('journeys', 'Journeys', '/journeys/'), ('regions', 'Regions', '/regions/'), ('guides', 'Guides', '/guides/'),
       ('method', 'Method', '/method/'), ('questions', 'Questions', '/questions/')]
MENU = [('home', 'Home', '/'), ('journeys', 'Sample journeys', '/journeys/'), ('regions', 'Regions', '/regions/'),
        ('guides', 'Guides and languages', '/guides/'), ('method', 'The method and house rules', '/method/'),
        ('questions', 'Questions', '/questions/')]


def nav(page):
    cur = lambda k: ' aria-current="page"' if k == page['key'] else ''
    links = '\n'.join('      <a href="%s"%s>%s</a>' % (href, cur(k), label) for k, label, href in NAV)
    menu = '\n'.join('          <li><a href="%s"%s>%s</a></li>' % (href, cur(k), label) for k, label, href in MENU)
    solid = page['key'] != 'home'
    return (read('parts', 'nav.html')
            .replace('{{NAV_CLASS}}', ' scrolled' if solid else '').replace('{{NAV_ATTR}}', ' data-solid' if solid else '')
            .replace('{{NAV_LINKS}}', links).replace('{{MENU_LINKS}}', menu).replace('{{CUR_enquire}}', cur('enquire')))


def footer(scene_top):
    f = read('parts', 'footer.html').replace('{{LANGS_SHORT}}', C.LANGS_SHORT)
    assert '<stop offset="0" stop-color="#EDE6DB"/>' in f
    return f.replace('<stop offset="0" stop-color="#EDE6DB"/>', '<stop offset="0" stop-color="%s"/>' % scene_top)


def head_block(track, label, title, level='h2', hid=None):
    return ('''      <div class="section-head">
        <div>
          <div class="eyebrow" data-track="%s">%s</div>
        </div>
        <%s class="display title"%s>
          %s
        </%s>
      </div>
''' % (track, label, level, ' id="%s"' % hid if hid else '', title, level))


def section(cls, sid, inner, labelled=None):
    return '  <section class="%s"%s%s>\n    <div class="container">\n%s    </div>\n  </section>\n\n' % (
        cls, ' id="%s"' % sid if sid else '', ' aria-labelledby="%s"' % labelled if labelled else '', inner)


def page_head(track, label, title, intro, crumb):
    return ('''  <section class="page-head">
    <div class="container">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Skazka</a><span aria-hidden="true">/</span><span>%s</span></nav>
%s      <p class="page-intro">%s</p>
    </div>
  </section>

''' % (crumb, head_block(track, label, title, 'h1'), intro))


def cta(title='Tell me<br/>a little.', line="I personally read every enquiry. No sales team sits between us. Send what you have &mdash; a season, a number of people, a wish &mdash; and I'll write back within two working days."):
    return section('cta-band', 'begin', head_block('zebra', 'Begin', title) + '''      <p>%s</p>
      <div class="ways">
        <a class="btn btn-primary" href="/enquire/">Begin a conversation <span class="arrow">&rarr;</span></a>
        <a class="btn" href="https://wa.me/254722503787">WhatsApp Kimani <span class="arrow">&rarr;</span></a>
      </div>
''' % line)


# ---------------------------------------------------------------- content blocks

def journey_spreads(level='h2'):
    out = '      <div class="journeys">\n'
    for n, j in enumerate(C.JOURNEYS, 1):
        stops = ''.join('<li>%s</li>' % s for s in j['stops'])
        href = '/enquire/?journey=' + re.sub(r'%20', '+', __import__('urllib.parse').parse.quote(text(j['key'])))
        out += '''        <article class="journey" id="%s">
          <div class="journey-media">
            <img src="%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async" />
          </div>
          <div class="journey-body">
            <p class="journey-label"><span>Journey &#8470; %02d</span><span>%d days</span></p>
            <%s class="journey-title">%s</%s>
            <p class="journey-desc">%s</p>
            <div class="route" style="--stops: %d;">
              <svg class="route-jeep" aria-hidden="true"><use href="#i-jeep"/></svg>
              <ol aria-label="Route">%s</ol>
            </div>
            <div class="journey-foot">
              <div class="journey-price">from %s<small>per person, shared</small></div>
              <a class="journey-cta" href="%s">Start from this <span class="arrow" aria-hidden="true">&rarr;</span></a>
            </div>
          </div>
        </article>
''' % (JSLUG[j['key']], j['img'], j['alt'], j['w'], j['h'], n, j['days'], level, j['title'], level, j['desc'],
       len(j['stops']), stops, j['price'], href)
    return out + '      </div>\n'


def journey_plates():
    out = '      <div class="plates">\n'
    for n, j in enumerate(C.JOURNEYS, 1):
        out += '''        <a class="plate" href="/journeys/#%s">
          <div class="plate-media"><img src="%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async" /></div>
          <p class="plate-label"><span>&#8470; %02d</span><span>%d days</span></p>
          <h3 class="plate-title">%s</h3>
          <p class="plate-price">from %s<small>per person, shared</small></p>
        </a>
''' % (JSLUG[j['key']], j['img'], j['alt'], j['w'], j['h'], n, j['days'], j['title'], j['price'])
    return out + '      </div>\n      <a class="more" href="/journeys/">The journeys in full <span aria-hidden="true">&rarr;</span></a>\n'


def region_links():
    out = '      <div class="regions-list is-links">\n'
    for n, r in enumerate(C.REGIONS, 1):
        out += '''        <a class="region-row" href="/regions/#%s">
          <div class="region-num">%02d</div>
          <div class="region-name">%s<small>%s</small></div>
          <div class="region-meta">%s</div>
        </a>
''' % (r['slug'], n, r['name'], r['sub'], r['season'])
    return out + '      </div>\n      <a class="more" href="/regions/">The regions in full <span aria-hidden="true">&rarr;</span></a>\n'


def region_spreads():
    out = '      <div class="journeys">\n'
    for n, r in enumerate(C.REGIONS, 1):
        stats = ''.join('<div><span>%s</span><strong>%s</strong></div>' % kv for kv in r['stats'])
        out += '''        <article class="journey" id="%s">
          <div class="journey-media">
            <img src="%s" alt="%s" width="%d" height="%d" loading="lazy" decoding="async" />
          </div>
          <div class="journey-body">
            <p class="journey-label"><span>Region &#8470; %02d</span><span>%s</span></p>
            <h2 class="journey-title">%s</h2>
            <p class="journey-desc">%s</p>
            <div class="spread-stats">%s</div>
            <div class="journey-foot">
              <div class="journey-price"><small style="margin-top:0">%s</small></div>
              <a class="journey-cta" href="/enquire/">Plan a trip here <span class="arrow" aria-hidden="true">&rarr;</span></a>
            </div>
          </div>
        </article>
''' % (r['slug'], r['img'], r['alt'], r['w'], r['h'], n, r['season'], r['name'], r['desc'], stats, r['sub'])
    return out + '      </div>\n'


def faq_list():
    out = '      <div class="faq-list" id="faq-list">\n'
    for n, (q, a) in enumerate(C.FAQ):
        out += '''        <div class="faq-item%s" data-faq="%d">
          <div class="faq-q" role="button" tabindex="0" aria-expanded="%s">
            <div class="faq-num">%02d</div>
            <h2 class="faq-q-text">%s</h2>
            <div class="faq-toggle">+</div>
          </div>
          <div class="faq-a">
            <div class="faq-a-inner">
              <div class="faq-num"></div>
              <div class="faq-a-text">%s</div>
              <div></div>
            </div>
          </div>
        </div>
''' % (' open' if n == 0 else '', n, 'true' if n == 0 else 'false', n + 1, q, a)
    return out + '      </div>\n'


def guide_cards():
    out = '      <div class="guides">\n'
    for g in C.GUIDES:
        out += '''        <article class="guide%s">
          <div class="guide-face" lang="%s">%s</div>
          <p class="guide-role">%s</p>
          <h3 class="guide-name">%s</h3>
          <p>%s</p>%s
        </article>
''' % (' is-placeholder' if g['placeholder'] else '', g['lang'], g['face'], g['role'], g['name'], g['text'],
       '\n          <span class="guide-tag">Profile to come</span>' if g['placeholder'] else '')
    return out + '      </div>\n'


INCLUDED = '''      <div class="included">
        <div>
          <h3>Included</h3>
          <ul>
            <li>All camps and lodging</li>
            <li>All meals</li>
            <li>All transfers, including charter flights where relevant</li>
            <li>Park and conservancy fees</li>
            <li>Your guide and crew</li>
            <li>The concierge, throughout</li>
          </ul>
        </div>
        <div>
          <h3>Yours to arrange</h3>
          <ul>
            <li>International flights</li>
            <li>Visas</li>
          </ul>
        </div>
      </div>
'''

# ---------------------------------------------------------------- pages

def home():
    founder_quote = re.search(r'<p class="founder-quote">.*?</p>', read('sections', 'founder.html'), flags=re.S).group(0)
    return (read('sections', 'hero.html') + '\n' + read('sections', 'day.html') + '\n'
            + section('journeys-teaser', 'journeys', head_block('zebra', '02 / Sample journeys', 'Starting points,<br/>not destinations.') + journey_plates())
            + section('regions', 'regions', head_block('elephant', '03 / Regions', 'The country,<br/>in six moods.') + region_links())
            + section('founder', 'guides', head_block('antelope', '04 / Who leads your trip', 'One guide,<br/>your whole trip.')
                      + '      <div class="lead-quote">\n        ' + founder_quote + '''
        <div>
          <p class="lead-langs">Guiding in</p>
          <p>%s</p>
          <a class="more" href="/guides/" style="margin-top: 28px;">Meet Kimani and the guides <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
''' % C.LANGS_LONG)
            + section('testimonials', 'testimonials', head_block('elephant', '05 / In their words', 'Notes from<br/>former guests.') + read('sections', 'testimonials.html'))
            + cta())


def journeys():
    return (page_head('zebra', 'Sample journeys', 'Starting points,<br/>not destinations.',
                      "These are real trips we've run &mdash; shown to give you a feel for rhythm and cost. Each is for one small party of two to six. Yours will look different. It should.", 'Journeys')
            + section('journeys-list', 'itineraries', journey_spreads())
            + section('how', 'included', head_block('bird', 'The price', 'Everything after<br/>you land.') + INCLUDED
                      + '      <a class="more" href="/questions/">More on cost, seasons and children <span aria-hidden="true">&rarr;</span></a>\n')
            + cta())


def regions():
    return (page_head('elephant', 'Regions', 'The country,<br/>in six moods.', 'Six regions, each with its own season and its own pace.', 'Regions')
            + section('regions', 'regions', region_spreads()) + cta())


def guides():
    return (page_head('antelope', 'Who leads your trip', 'One guide,<br/>your whole trip.',
                      "I lead most trips myself &mdash; and when I can't, it is one of three senior guides I've worked with for six years or more. You will always know who it is before you arrive, and speak with them directly during planning.", 'Guides')
            + section('founder', 'kimani', head_block('lion', 'The founder', 'I am<br/>Kimani Kennedy Muna.') + read('sections', 'founder.html'))
            + section('how', 'languages', head_block('bird', 'Guides and languages', 'Your language,<br/>in the vehicle.') + guide_cards()
                      + '      <p class="team-note">We are a team of twenty-five &mdash; guides, chefs, mechanics and pilots &mdash; and the same guide stays with you for the whole trip.</p>\n')
            + cta())


def method():
    return (page_head('bird', 'The method', 'Four steps, then<br/>everything else is yours.',
                      'How a trip comes together, from the first call to the last goodbye.', 'Method')
            + section('how', 'how', read('sections', 'how.html'))
            + section('house', 'house-rules', head_block('lion', 'House rules', 'Seven promises,<br/>kept in plain text.', hid='house-title') + read('sections', 'house.html'), labelled='house-title')
            + cta())


def questions():
    return (page_head('antelope', 'Questions', "What we're<br/>often asked.", 'Cost, seasons, children, and how we differ from a regular operator.', 'Questions')
            + section('faq', 'faq', faq_list()) + cta('Something<br/>we missed?', 'Ask me directly. I read every enquiry myself and reply within two working days.'))


def enquire():
    return read('sections', 'enquire.html')


PAGES = [
    dict(key='home', path='', body=home, scene=LINEN, name='Home',
         title='Private Kenya Safaris, Small Parties Only | Skazka Tours',
         desc='Private Kenya safaris for parties of two to six, planned and led from Nairobi since 2015. One guide for your whole trip. English, Swahili and Russian spoken.'),
    dict(key='journeys', path='journeys/', body=journeys, scene=LINEN, name='Journeys',
         title='Sample Kenya Safari Journeys and Prices | Skazka Tours',
         desc='Three private Kenya safaris we have run, with routes and prices: Mara Classic (10 days), Coast, craft and bush (14 days), and 5 days in Laikipia. From $6,800.'),
    dict(key='regions', path='regions/', body=regions, scene=LINEN, name='Regions',
         title='Where We Go: Six Regions of Kenya | Skazka Tours',
         desc='Maasai Mara conservancies, Laikipia, Samburu, Amboseli, Tsavo, and Lamu and the coast: what each region is like, when to go, and how long it takes to reach.'),
    dict(key='guides', path='guides/', body=guides, scene=LINEN, name='Guides',
         title='Your Guide: Kimani Kennedy Muna and Team | Skazka Tours',
         desc='Meet Kimani Kennedy Muna, KPSGA silver-licensed guide and founder of Skazka Tours, and the team of twenty-five behind every private Kenya safari.'),
    dict(key='method', path='method/', body=method, scene=LINEN, name='Method',
         title='How We Plan a Private Kenya Safari | Skazka Tours',
         desc='Four steps: a conversation, a written and clearly priced draft, one guide on the ground with you, and plans that change daily. Plus the seven house rules.'),
    dict(key='questions', path='questions/', body=questions, scene=LINEN, name='Questions',
         title='Kenya Safari Questions: Cost, Seasons, Children | Skazka Tours',
         desc='What a private Kenya safari costs, what is included, the best time to go by region, group size, children, Russian-speaking guides, and when to book.'),
    dict(key='enquire', path='enquire/', body=enquire, scene=SAND, name='Plan a trip',
         title='Plan a Private Kenya Safari | Skazka Tours',
         desc='Tell Kimani when you imagine travelling, who is coming and what you love. Every enquiry is read personally, with a reply within two working days.'),
]


# ---------------------------------------------------------------- structured data (repeats the page, nothing more)

def schema(page):
    base = json.loads(read('schema_base.json'))
    url = SITE + '/' + page['path']
    wp = {"@type": "WebPage", "@id": url + '#webpage', "url": url, "name": page['title'], "description": page['desc'], "inLanguage": "en",
          "isPartOf": {"@id": SITE + '/#website'}, "about": {"@id": SITE + '/#travelagency'}, "dateModified": TODAY}
    graph = []
    if page['key'] == 'home':
        ag = base['TravelAgency']
        ag['description'] = page['desc']
        ag['makesOffer'] = [{"@id": SITE + '/journeys/#journey-' + JSLUG[j['key']]} for j in C.JOURNEYS]
        wp.update({"headline": "Kenya, carried by hand.", "mainEntity": {"@id": SITE + '/#travelagency'},
                   "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + '/assets/og-card.jpg'}})
        graph += [ag, base['WebSite'], wp, base['VideoObject']]
    else:
        graph.append(wp)
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Skazka Tours", "item": SITE + '/'},
            {"@type": "ListItem", "position": 2, "name": page['name'], "item": url}]})
    if page['key'] == 'journeys':
        for j in C.JOURNEYS:
            img = j['img'].replace('&amp;', '&')
            graph.append({"@type": "TouristTrip", "@id": url + '#journey-' + JSLUG[j['key']], "name": text(j['title']), "description": text(j['desc']),
                          "touristType": "Private small party, two to six guests", "image": SITE + img if img.startswith('/') else img,
                          "itinerary": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": text(s)} for i, s in enumerate(j['stops'])]},
                          "provider": {"@id": SITE + '/#travelagency'},
                          "offers": {"@type": "Offer", "priceCurrency": "USD", "price": int(j['price'].replace('$', '').replace(',', '')),
                                     "description": "From price per person, sharing, for %d days. Everything after landing is included; international flights and visas are not." % j['days'],
                                     "url": url + '#' + JSLUG[j['key']], "availability": "https://schema.org/InStock"}})
    if page['key'] == 'questions':
        graph.append({"@type": "FAQPage", "@id": url + '#faq', "mainEntity": [
            {"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}} for q, a in C.FAQ]})
    if page['key'] == 'guides':
        person = dict(base['TravelAgency']['founder'])
        person.update({"@id": url + '#kimani', "worksFor": {"@id": SITE + '/#travelagency'}})
        graph.append(person)
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------- assemble

def hashed(src_name, ext):
    data = read(src_name)
    name = 'site.%s.%s' % (hashlib.sha256(data.encode()).hexdigest()[:10], ext)
    adir = os.path.join(ROOT, 'assets')
    for f in os.listdir(adir):
        if re.fullmatch(r'site\.[0-9a-f]{10}\.%s' % ext, f) and f != name:
            os.remove(os.path.join(adir, f))
    with open(os.path.join(adir, name), 'w', encoding='utf-8') as f:
        f.write(data)
    return '/assets/' + name


def render(page, css, js):
    url = SITE + '/' + page['path']
    home_only = '<link rel="preload" as="image" fetchpriority="high" href="/assets/hero-poster.jpg">\n' if page['key'] == 'home' else ''
    return '''<!DOCTYPE html>
<!-- Generated by build.py from src/. Do not edit this file: edit src/, then run python3 build.py -->
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#F6F2EB">
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/plain" href="https://skazka.tours/llms.txt" title="Skazka Tours: plain-text summary for AI assistants">
<meta property="og:site_name" content="Skazka Tours">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://skazka.tours/assets/og-card.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="African elephants at sunset in Samburu National Reserve, Kenya">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://skazka.tours/assets/og-card.jpg">
<meta name="twitter:image:alt" content="African elephants at sunset in Samburu National Reserve, Kenya">
<link rel="icon" type="image/svg+xml" href="/assets/mark.svg">
<link rel="apple-touch-icon" href="/assets/mark.svg">
<meta name="author" content="Skazka Tours">
<meta name="geo.region" content="KE-110">
<meta name="geo.placename" content="Nairobi">
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
{home_only}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400..500&family=Hanken+Grotesk:wght@400..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">
{schema}
</script>
</head>
<body class="page-{key}">
  <a class="skip-link" href="#main">Skip to the content</a>
{sprite}
{nav}
  <main id="main">
{body}  </main>

{footer}
{concierge}
  <script src="{js}" defer></script>
</body>
</html>
'''.format(title=page['title'], desc=page['desc'], url=url, home_only=home_only, css=css, js=js, schema=schema(page), key=page['key'],
           sprite=read('parts', 'sprite.html'), nav=nav(page), body=page['body'](), footer=footer(page['scene']), concierge=read('parts', 'concierge.html'))


def main():
    css, js = hashed('site.css', 'css'), hashed('site.js', 'js')
    for page in PAGES:
        out = render(page, css, js)
        left = re.findall(r'\{\{[A-Za-z_]+\}\}', out)
        assert not left, (page['key'], left)
        d = os.path.join(ROOT, page['path'])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(out)
        assert len(page['title']) <= 62 and len(page['desc']) <= 160, (page['key'], len(page['title']), len(page['desc']))
        print('%-10s %-22s title %2d  desc %3d  %6.1f KB' % (page['key'], '/' + page['path'], len(page['title']), len(page['desc']), len(out) / 1024))
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
            '  <url>\n    <loc>%s/%s</loc>\n    <lastmod>%s</lastmod>\n    <priority>%s</priority>\n  </url>\n' % (SITE, p['path'], TODAY, '1.0' if p['key'] == 'home' else '0.8')
            for p in PAGES) + '</urlset>\n')
    print('assets:', css, js)


if __name__ == '__main__':
    main()
