#!/usr/bin/env python3
"""Palimpsest Book Studio — template v2 T1 page generator (websites lane, 2026-11-21, t_f3c6dec9).
All copy comes from the verified-facts card body only (primary sources: Creative Loafing Tampa
'More than a store, Ybor City's Palimpsest book studio opens on November 19' (2026-11);
Kress Contemporary arts-organizations partner page, room 200). Unknowns omitted, never guessed.
Output: public/*.html + sitemap.xml + robots.txt. Canonical/OG pinned to the -demo host.
"""
import json, os

ORIGIN = "https://palimpsest-book-studio-demo.up.railway.app"
SITE = "Palimpsest Book Studio"
IG = "https://www.instagram.com/palimpsest.bookstudio/"
MAIL = "palimpsestreads@gmail.com"
GEO_LAT, GEO_LON = 27.960330, -82.441370  # US Census ARC geocode, 1624 E 7th Ave, Tampa FL 33605 (geocoding.geo.census.gov 2026-11-21)
MAPQ = "1624+E+7th+Ave+Tampa+FL+33605"
BUILT = "<!-- BUILT-2026-11-21 -->"

MAP_EMBED = f'<iframe src="https://www.google.com/maps?q={MAPQ}&output=embed" title="Map: {SITE}, Room 200, 1624 E 7th Ave, Ybor City, Tampa, FL 33605"></iframe>'
MAP_LINK = f'https://maps.google.com/maps?q={MAPQ}'

MARK = ('<svg class="mark" viewBox="0 0 100 100" role="img" aria-label="Palimpsest Book Studio emblem: layered pages with an orange bookmark"><rect x="30" y="18" width="46" height="60" rx="6" fill="none" stroke="#d8c49b" stroke-width="3"/><rect x="24" y="24" width="46" height="60" rx="6" fill="none" stroke="#c14e1c" stroke-width="3" opacity=".45"/><rect x="18" y="30" width="46" height="60" rx="6" fill="#f5eddc" stroke="#241c11" stroke-width="4"/><path d="M30 48h22M30 58h22M30 68h13" stroke="#241c11" stroke-width="3.4" stroke-linecap="round" opacity=".55"/><path d="M52 30v22l5-5 5 5V30" fill="#c14e1c"/></svg>')

IC_BOOK = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><path d="M8 10h14a4 4 0 0 1 4 4v26a4 4 0 0 0-4-4H8Z" fill="none" stroke="#241c11" stroke-width="3" stroke-linejoin="round"/><path d="M40 10H26a4 4 0 0 0-4 4v26a4 4 0 0 1 4-4h14Z" fill="none" stroke="#241c11" stroke-width="3" stroke-linejoin="round"/><path d="M26 14v26" stroke="#241c11" stroke-width="3"/><path d="M31 8v12l3.5-3.5L38 20V8" fill="#c14e1c"/></svg>'
IC_ZINE = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><path d="M10 8h20l8 8v24a3 3 0 0 1-3 3H10a3 3 0 0 1-3-3V11a3 3 0 0 1 3-3Z" fill="none" stroke="#241c11" stroke-width="3" stroke-linejoin="round"/><path d="M30 8v8h8" fill="none" stroke="#c14e1c" stroke-width="3" stroke-linejoin="round"/><path d="M14 24h12M14 31h12M14 38h7" stroke="#241c11" stroke-width="2.6" stroke-linecap="round" opacity=".55"/></svg>'
IC_TAG = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><path d="M7 9h14l20 20-12 12L9 21V9Z" fill="none" stroke="#241c11" stroke-width="3" stroke-linejoin="round" transform="rotate(0)"/><circle cx="15" cy="17" r="2.8" fill="#c14e1c"/><path d="M25 27l8 8" stroke="#c14e1c" stroke-width="2.6" stroke-linecap="round"/></svg>'
IC_MIC = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><rect x="19" y="7" width="10" height="20" rx="5" fill="none" stroke="#241c11" stroke-width="3"/><path d="M12 24a12 12 0 0 0 24 0" fill="none" stroke="#c14e1c" stroke-width="3" stroke-linecap="round"/><path d="M24 36v6M16 42h16" stroke="#241c11" stroke-width="3" stroke-linecap="round"/></svg>'
IC_CAL = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><rect x="7" y="11" width="34" height="30" rx="4" fill="none" stroke="#241c11" stroke-width="3"/><path d="M7 19h34" stroke="#241c11" stroke-width="3"/><path d="M15 6v8M33 6v8" stroke="#c14e1c" stroke-width="3" stroke-linecap="round"/><path d="M16 27h6M26 27h6M16 34h6" stroke="#241c11" stroke-width="2.6" stroke-linecap="round" opacity=".55"/></svg>'
IC_QUILL = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><path d="M6 42c6-16 18-28 36-34-2 16-10 28-24 30" fill="none" stroke="#241c11" stroke-width="3" stroke-linejoin="round"/><path d="M12 36l14-16" stroke="#c14e1c" stroke-width="2.6" stroke-linecap="round"/><path d="M6 42c5-2 10-3 16-4" fill="none" stroke="#241c11" stroke-width="2.6" stroke-linecap="round" opacity=".6"/></svg>'
IC_MAIL = '<svg class="ic" viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="12" width="36" height="24" rx="4" fill="none" stroke="#241c11" stroke-width="3"/><path d="M8 14l16 13 16-13" fill="none" stroke="#c14e1c" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

HEROART = ('<svg class="heroart" viewBox="0 0 560 430" role="img" aria-label="Illustration of an open book with an orange bookmark, with faded ghost lines of earlier writing and loose zine pages floating behind it">'
 '<g fill="none" stroke="#d8c49b" stroke-width="6" stroke-linecap="round" opacity=".8"><path d="M64 46h120"/><path d="M64 66h150"/><path d="M64 86h96"/><path d="M338 40h134"/><path d="M338 60h108"/><path d="M338 80h150"/><path d="M44 330h86"/><path d="M470 348h66"/></g>'
 '<g opacity=".55"><rect x="122" y="150" width="330" height="216" rx="12" transform="rotate(-5 287 258)" fill="#ede2ca" stroke="#c9b591" stroke-width="2"/><rect x="104" y="128" width="330" height="216" rx="12" transform="rotate(3 269 236)" fill="#f5eddc" stroke="#c9b591" stroke-width="2"/></g>'
 '<path d="M96 120h176a10 10 0 0 1 10 10v232a10 10 0 0 1-10 10H96a10 10 0 0 1-10-10V130a10 10 0 0 1 10-10Z" transform="rotate(-6 184 245)" fill="#fbf6ea" stroke="#241c11" stroke-width="4"/>'
 '<g transform="rotate(-6 184 245)" fill="none" stroke="#241c11" stroke-width="2.8" opacity=".45"><path d="M112 160h120M112 182h144M112 204h132M112 226h120M112 248h138M112 270h96"/></g>'
 '<path d="M286 148h178a10 10 0 0 1 10 10v232a10 10 0 0 1-10 10H286a10 10 0 0 1-10-10V158a10 10 0 0 1 10-10Z" transform="rotate(5 375 264)" fill="#fbf6ea" stroke="#241c11" stroke-width="4"/>'
 '<g transform="rotate(5 375 264)" fill="none" stroke="#241c11" stroke-width="2.8" opacity=".45"><path d="M302 184h146M302 206h124M302 228h146M302 250h112M302 272h138M302 294h84"/></g>'
 '<path d="M352 132v268" stroke="#241c11" stroke-width="5" transform="rotate(5 375 264)"/>'
 '<path d="M368 120v250l-14-16-14 16V124" transform="rotate(5 375 264)" fill="#c14e1c"/>'
 '<g transform="rotate(-9 118 348)"><rect x="52" y="322" width="92" height="64" rx="6" fill="#ede2ca" stroke="#241c11" stroke-width="3"/><path d="M64 342h52M64 356h66M64 370h40" stroke="#241c11" stroke-width="2.4" stroke-linecap="round" opacity=".5"/><path d="M64 336h26" stroke="#c14e1c" stroke-width="3" stroke-linecap="round"/></g>'
 '<g transform="rotate(8 462 116)"><rect x="416" y="88" width="92" height="64" rx="6" fill="#f5eddc" stroke="#c14e1c" stroke-width="3"/><path d="M428 108h52M428 122h66M428 136h40" stroke="#241c11" stroke-width="2.4" stroke-linecap="round" opacity=".5"/></g>'
 '<circle cx="284" cy="215" r="196" fill="none" stroke="#c9b591" stroke-width="1.6" opacity=".45"/>'
 '<path d="M0 402h560" stroke="#c9b591" stroke-width="2" opacity=".5"/></svg>')

def head(path, title, desc, og=True):
    canonical = ORIGIN + ("" if path == "/" else path)
    out = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{desc}">',
        '<meta name="robots" content="noindex, nofollow">',
        f'<link rel="canonical" href="{canonical}">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
    ]
    if og:
        out += [
            f'<meta property="og:title" content="{title}">',
            f'<meta property="og:description" content="{desc}">',
            f'<meta property="og:url" content="{canonical}">',
            f'<meta property="og:image" content="{ORIGIN}/og.png">',
            '<meta property="og:type" content="website">',
            '<meta name="twitter:card" content="summary_large_image">',
        ]
    out.append('<link rel="stylesheet" href="/style.css">\n</head>')
    return "\n".join(out)

BRAND = f'<a class="brand" href="/">{MARK}<span class="word">Palimpsest Book Studio<small>Book studio &middot; Ybor City, Tampa</small></span></a>'
NAV = ('<nav class="main" aria-label="Main"><ul><li><a href="/browse">Browse</a></li>'
       '<li><a href="/shelves">Shelves</a></li><li><a href="/readings">Readings</a></li>'
       '<li><a href="/story">Our story</a></li><li><a class="btn" href="/contact">Plan a visit</a></li></ul></nav>')
HEADER = f'<header class="top"><div class="wrap">{BRAND}{NAV}</div></header>'

FOOTER = ('<footer class="site"><div class="wrap"><div class="nap"><p class="fbrand">Palimpsest Book Studio</p>'
 '<address>Room 200, 1624 E 7th Ave<br>Ybor City, Tampa, Florida 33605<br>inside Kress Contemporary, second floor<br>'
 'Book studio &amp; shop &middot; open Friday&ndash;Sunday, noon&ndash;4 p.m.</address></div>'
 '<nav aria-label="Footer"><ul><li><a href="/browse">Browse</a></li><li><a href="/shelves">Shelves</a></li>'
 '<li><a href="/readings">Readings</a></li><li><a href="/story">Our story</a></li><li><a href="/contact">Contact</a></li>'
 '<li><a href="/privacy">Privacy</a></li></ul></nav>'
 f'<p class="socials"><a href="{IG}" rel="noopener">Instagram</a> &middot; <a href="mailto:{MAIL}">{MAIL}</a></p>'
 '<p class="footline">&copy; 2026 Palimpsest Book Studio &middot; book studio for readers and writers &middot; Room 200, 1624 E 7th Ave, Tampa, FL 33605 &middot; <a href="mailto:' + MAIL + '">' + MAIL + '</a></p></div></footer>')

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=1) + '\n</script>'

BIZ_ID = ORIGIN + "/#palimpsest"
BIZ = {
    "@type": "BookStore",
    "@id": BIZ_ID,
    "name": SITE,
    "description": "A book studio in Ybor City, Tampa — books ($7 to $25), zines and select consignment pieces, plus a programming calendar of readings and special events for readers and writers.",
    "url": ORIGIN + "/",
    "image": ORIGIN + "/og.png",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Room 200, 1624 E 7th Ave",
        "addressLocality": "Tampa",
        "addressRegion": "FL",
        "postalCode": "33605",
        "addressCountry": "US",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Friday", "Saturday", "Sunday"],
        "opens": "12:00", "closes": "16:00",
    }],
    "priceRange": "$7 - $25",
    "email": f"mailto:{MAIL}",
    "sameAs": [IG],
    "founder": [
        {"@type": "Person", "name": "Micheal Hooker"},
        {"@type": "Person", "name": "Mitzi Jo Gordon"},
    ],
    "areaServed": {"@type": "Place", "name": "Ybor City, Tampa, Florida"},
}

WEBSITE = {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": SITE, "url": ORIGIN + "/"}

def webpage(path, title, desc, extra_graph=None):
    g = [WEBSITE, {
        "@type": "WebPage",
        "@id": ORIGIN + path + "#webpage",
        "name": title,
        "description": desc,
        "url": ORIGIN + ("" if path == "/" else path),
        "isPartOf": {"@id": ORIGIN + "/#website"},
        "about": {"@id": BIZ_ID},
    }]
    if extra_graph:
        g += extra_graph
    return ld({"@graph": g})

def breadcrumb(items):
    el = [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + u} for i, (n, u) in enumerate(items)]
    return {"@type": "BreadcrumbList", "itemListElement": el}

FAQ = [
    ("When are you open?",
     "The studio keeps open hours Friday through Sunday, noon to 4 p.m., as reported by Creative Loafing Tampa. If your timing doesn&rsquo;t fit those hours, email " + MAIL + " and ask."),
    ("Where exactly is Palimpsest?",
     "Room 200 on the second floor of Kress Contemporary at 1624 E 7th Ave, Ybor City, Tampa, FL 33605 — the same floor as galleries, studios and a black box theatre. The map in the <em>Find it</em> section below the FAQ pins the front door."),
    ("What can I buy?",
     "Books priced $7 to $25, zines, and select consignment pieces — the same offerings the studio opened with on November 19, 2026."),
    ("Is it a bookstore or something else?",
     "Creative Loafing Tampa called it &ldquo;more than a store&rdquo; — a book studio that pairs the shelves with a programming calendar for readers and writers."),
    ("How do I reach you?",
     "Email " + MAIL + " — the published inbox on Kress Contemporary&rsquo;s partner page — or use the contact form, and the note lands in the same inbox."),
]

def page(path, title, desc, body, extra_ld=None, utility=False):
    html = [head(path, title, desc, og=not utility), "<body>",
            '<a class="skip" href="#main">Skip to content</a>',
            '<div class="band" aria-hidden="true"></div>', HEADER,
            '<main id="main">', body, "</main>", FOOTER, BUILT]
    if extra_ld:
        html.append(extra_ld)
    html.append("</body>\n</html>")
    return "\n".join(html)

# ---------------------------------------------------------------- HOME
home_body = f'''<section class="hero"><div class="wrap"><div class="herotext"><span class="ghostlayer" aria-hidden="true">PAL&middot;IMP&middot;SEST</span><span class="label">Book studio &middot; Ybor City, Tampa &middot; inside Kress Contemporary</span><h1>A book studio for <em>readers</em> and <em>writers.</em></h1><div class="stubs"><span class="stub">Books &middot; zines &middot; select consignment</span><span class="stub alt">Open Friday&ndash;Sunday, noon&ndash;4 p.m.</span><span class="stub alt">Room 200, Kress Contemporary</span></div><p class="sub">Palimpsest is a new book studio on the second floor of Kress Contemporary in Ybor City — books priced $7 to $25, zines and select consignment pieces, plus a programming calendar of readings and special events. The studio&rsquo;s whole point is analog culture: the written word, held in your hands.</p><hr class="rule"><div class="ctas"><a class="btn" href="/contact">Plan a visit</a><a class="btn ghost" href="mailto:{MAIL}">Email the studio</a></div><p class="heronote">Opened November 19, 2026 with readings on opening night, in Room 200 of Kress Contemporary. Questions before you come over? Email <a href="mailto:{MAIL}">{MAIL}</a>.</p></div><div class="heroartcell">{HEROART}</div></div></section>

<section class="block"><div class="wrap"><span class="label">On the shelves</span><h2>Books, zines and select <em>consignment</em></h2><p class="lede">Everything the studio sells is something you can hold. The book range runs $7 to $25, zines sit on the same shelves, and select consignment pieces round out the tables.</p><div class="strip"><div class="chip">{IC_BOOK}<h3>Books</h3><p>The range that covers the shelves — priced to take home, not just to browse.</p><span class="price">$7 – $25</span><a class="go" href="/shelves">The shelves &rarr;</a></div><div class="chip">{IC_ZINE}<h3>Zines</h3><p>Small-press paper, shelved right alongside the books.</p><a class="go" href="/shelves">The shelves &rarr;</a></div><div class="chip">{IC_TAG}<h3>Consignment</h3><p>Select consignment pieces, placed on the studio&rsquo;s shelves.</p><a class="go" href="/shelves">The shelves &rarr;</a></div></div><span class="qsrc">offerings and price range per Creative Loafing Tampa, November 2026</span></div></section>

<section class="block alt"><div class="wrap"><span class="label">On the calendar</span><h2>Readings, events and <em>more</em></h2><p class="lede">Palimpsest promotes analog culture two ways: through what&rsquo;s on the shelves and through a programming calendar for readers and writers. The studio&rsquo;s opening night was readings, and special events are part of what it runs.</p><div class="strip"><div class="chip">{IC_MIC}<h3>Readings</h3><p>The opening-night format — pages read out loud, in the room.</p><a class="go" href="/readings">The calendar &rarr;</a></div><div class="chip">{IC_CAL}<h3>Special events</h3><p>Gatherings for readers and writers, hosted on the studio&rsquo;s calendar.</p><a class="go" href="/readings">The calendar &rarr;</a></div></div><span class="qsrc">programming and opening-night readings per Creative Loafing Tampa, November 2026</span></div></section>

<section class="quotband"><div class="wrap"><span class="ghostq" aria-hidden="true">palimpsest</span><blockquote>A palimpsest is a writing surface that still bears traces of its earlier form.<span class="qsrc">the meaning behind the studio&rsquo;s name — Creative Loafing Tampa, November 2026</span></blockquote></div></section>

<section class="block"><div class="wrap"><span class="label">Behind the desk</span><h2>Micheal Hooker &amp; Mitzi Jo <em>Gordon</em></h2><p class="lede">The people behind Palimpsest are no strangers to lit-minded Tampe&ntilde;os: Micheal Hooker ran Lector, the Tampa book and wine bar, and Mitzi Jo Gordon ran the Bluebird Books Bus.</p><p>The studio is what they launched next — built, in their words to Creative Loafing Tampa, to honor a combined passion for nontraditional spaces. The bright-orange room inside Kress Contemporary is the newest of them.</p><span class="qsrc">founders and background per Creative Loafing Tampa, November 2026</span><div class="ctas"><a class="btn" href="/story">The full story</a><a class="btn ghost" href="{IG}" rel="noopener">Follow on Instagram</a></div></div></section>

<section class="block alt"><div class="wrap"><span class="label">Before you visit</span><h2>Questions folks ask</h2><div class="faq">{"".join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in FAQ)}</div><span class="qsrc">hours, offerings, location and contact per Creative Loafing Tampa (November 2026) and Kress Contemporary&rsquo;s arts-organizations partner page</span></div></section>

<section class="block"><div class="wrap"><span class="label">Find it</span><h2>Room 200, 1624 E 7th Ave</h2><div class="mapgrid"><div><p class="lede">Second floor of Kress Contemporary, in the middle of Ybor City&rsquo;s arts tenants — the same floor holds galleries, a black box theatre, photography studios and a fiber art boutique.</p><div class="infocards" style="margin-top:22px"><div class="infocard"><h3>Email</h3><p><a href="mailto:{MAIL}">{MAIL}</a> — the inbox published on the studio&rsquo;s Kress Contemporary partner page.</p></div><div class="infocard"><h3>Open hours</h3><p>Friday&ndash;Sunday, noon&ndash;4 p.m.</p></div></div><div class="ctas"><a class="btn" href="/contact">Ask us anything</a><a class="btn ghost" href="{MAP_LINK}" rel="noopener">Directions</a></div></div><div><div class="mapcell">{MAP_EMBED}</div><p class="mapnote"><a href="{MAP_LINK}" rel="noopener">Open in Google Maps</a> &middot; room 200, second floor of Kress Contemporary.</p></div></div></div></section>

<section class="callband"><div class="wrap"><div><span class="ghostc" aria-hidden="true">noon to four</span><h2>Open Friday to Sunday, noon to four.</h2><p>Questions, event ideas, or just a hello — the form and the published inbox reach the same place.</p></div><div class="ctas" style="margin:0"><a class="btn" href="/contact">Send a note</a><a class="btn ghostc" href="mailto:{MAIL}">Email {MAIL}</a></div></div></section>'''

home_ld = ld({"@graph": [BIZ, WEBSITE, {
    "@type": "WebPage", "@id": ORIGIN + "/#webpage",
    "name": "Palimpsest Book Studio — Books, Zines and Readings in Ybor City, Tampa FL",
    "description": "A new book studio inside Ybor City's Kress Contemporary — books ($7–$25), zines and select consignment pieces, plus readings and special events. Open Friday–Sunday, noon–4 p.m.",
    "url": ORIGIN + "/", "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": BIZ_ID}},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&rsquo;", "\u2019").replace("&ldquo;", "\u201c").replace("&rdquo;", "\u201d").replace("&ntilde;", "\u00f1").replace("<em>", "").replace("</em>", "").replace("&middot;", "·").replace("&amp;", "&")}} for q, a in FAQ]}]})

# ---------------------------------------------------------------- BROWSE (hub)
browse_body = f'''<section class="minihero"><div class="wrap"><span class="ghostlayer" aria-hidden="true">shelf &middot; calendar</span><span class="label">Browse</span><h1>The studio, shelf by <em>shelf.</em></h1><p class="sub">Three doors into Palimpsest: what&rsquo;s on the shelves, what&rsquo;s on the calendar, and the story behind the name.</p><hr class="rule"><div class="ctas"><a class="btn" href="/shelves">The shelves</a><a class="btn ghost" href="/readings">The calendar</a></div></div></section>

<section class="block"><div class="wrap"><span class="label">Pick a door</span><h2>What&rsquo;s here</h2><div class="strip"><div class="chip">{IC_BOOK}<h3>The shelves</h3><p>Books priced $7 to $25, zines, and select consignment pieces — the physical part of the studio.</p><a class="go" href="/shelves">Books, zines and consignment &rarr;</a></div><div class="chip">{IC_MIC}<h3>The calendar</h3><p>Readings and special events for readers and writers — the programming side.</p><a class="go" href="/readings">Readings and events &rarr;</a></div><div class="chip">{IC_QUILL}<h3>The story</h3><p>What a palimpsest is, and why Hooker and Gordon built a studio around the word.</p><a class="go" href="/story">Founders and name &rarr;</a></div></div></div></section>

<section class="block alt"><div class="wrap"><span class="label">Come by</span><h2>Friday to Sunday, noon to four</h2><p class="lede">Room 200, second floor of Kress Contemporary, 1624 E 7th Ave, Ybor City. Open hours are Friday through Sunday, noon to 4 p.m.</p><div class="ctas"><a class="btn" href="/contact">Plan a visit</a><a class="btn ghost" href="{MAP_LINK}" rel="noopener">Directions</a></div><span class="qsrc">hours and location per Creative Loafing Tampa (November 2026) and Kress Contemporary</span></div></section>'''

browse_ld = webpage("/browse", "Browse the Studio — Palimpsest Book Studio, Ybor City Tampa FL",
    "Browse Palimpsest Book Studio in Tampa FL — the shelves (books $7–$25, zines, consignment), the event calendar, and the story behind the name.",
    extra_graph=[{"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "The shelves", "url": ORIGIN + "/shelves"},
        {"@type": "ListItem", "position": 2, "name": "The calendar", "url": ORIGIN + "/readings"},
        {"@type": "ListItem", "position": 3, "name": "The story", "url": ORIGIN + "/story"}]},
        breadcrumb([("Home", "/"), ("Browse", "/browse")])])

# ---------------------------------------------------------------- SHELVES (service detail 1)
shelves_body = f'''<section class="minihero"><div class="wrap"><span class="ghostlayer" aria-hidden="true">books &middot; zines</span><span class="label">The shelves</span><h1>Everything you can <em>hold.</em></h1><p class="sub">Books, zines and select consignment pieces — the paper side of the studio, launched the way it was reported: priced to take home.</p><hr class="rule"><div class="ctas"><a class="btn" href="/contact">Plan a visit</a><a class="btn ghost" href="/readings">See the calendar</a></div></div></section>

<section class="block"><div class="wrap"><span class="label">Books</span><h2>$7 to $25, on the <em>shelves</em></h2><p class="lede">The studio opened with books priced $7 to $25 — a range meant for grabbing one on a whim and coming back for the next. Creative Loafing Tampa, which covered the opening, lists the range as part of what the shop carries.</p><span class="qsrc">book pricing per Creative Loafing Tampa, November 2026</span></div></section>

<section class="block alt"><div class="wrap"><span class="label">Zines</span><h2>The small-press <em>shelf</em></h2><p class="lede">Zines share the shelves with the books. If you came for the printed matter — stapled, small-run, made by hand — Palimpsest keeps that tradition in print, in the room, where you can pick it up.</p></div></section>

<section class="block"><div class="wrap"><span class="label">Consignment</span><h2>Select consignment <em>pieces</em></h2><p class="lede">Beyond the books and zines, the studio carries select consignment pieces — items placed on Palimpsest&rsquo;s shelves to be sold through the shop.</p></div></section>

<section class="block alt"><div class="wrap"><span class="label">Why paper</span><h2>The analog argument</h2><p class="lede">This is what the studio means by analog culture: a shop where the inventory gets read with your eyes, turned with your hands, and taken home without a screen getting involved.</p><div class="ctas"><a class="btn" href="/contact">Ask what&rsquo;s on the shelves</a><a class="btn ghost" href="/readings">Then see the calendar &rarr;</a></div></div></section>'''

shelves_ld = webpage("/shelves", "Books, Zines and Consignment — Palimpsest Book Studio, Tampa FL",
    "Books priced $7–$25, zines and select consignment pieces at Palimpsest Book Studio in Ybor City, Tampa FL. Open Friday–Sunday, noon–4 p.m.",
    extra_graph=[{
        "@type": "Service", "@id": ORIGIN + "/shelves#service",
        "name": "Books, zines and consignment",
        "serviceType": "Retail",
        "provider": {"@id": BIZ_ID},
        "areaServed": {"@type": "Place", "name": "Ybor City, Tampa, Florida"},
        "offers": {"@type": "Offer", "priceCurrency": "USD", "priceSpecification": {
            "@type": "PriceRangeSpecification",
            "minPrice": {"@type": "PriceSpecification", "minPrice": "7", "priceCurrency": "USD"},
            "maxPrice": {"@type": "PriceSpecification", "maxPrice": "25", "priceCurrency": "USD"}},
            "availability": "https://schema.org/InStock", "url": ORIGIN + "/shelves"},
    }, breadcrumb([("Home", "/"), ("Browse", "/browse"), ("Shelves", "/shelves")])])

# ---------------------------------------------------------------- READINGS (service detail 2)
readings_body = f'''<section class="minihero"><div class="wrap"><span class="ghostlayer" aria-hidden="true">readings</span><span class="label">On the calendar</span><h1>Readings, and whatever <em>comes next.</em></h1><p class="sub">Palimpsest runs a programming calendar for readers and writers. The studio&rsquo;s opening night — November 19, 2026 — was readings, and special events are part of what it keeps running.</p><hr class="rule"><div class="ctas"><a class="btn" href="mailto:{MAIL}">Ask what&rsquo;s next</a><a class="btn ghost" href="/contact">Send a note</a></div></div></section>

<section class="block"><div class="wrap"><span class="label">The programming calendar</span><h2>Events for readers and <em>writers</em></h2><p class="lede">Creative Loafing Tampa describes Palimpsest as promoting analog culture &ldquo;via what&rsquo;s on the shelves and on the programming calendar for readers and writers.&rdquo; The calendar is the studio half of the studio — readings, gatherings and special events hosted in the orange room on Kress&rsquo;s second floor.</p><span class="qsrc">quote and event coverage per Creative Loafing Tampa, November 2026</span></div></section>

<section class="block alt"><div class="wrap"><span class="label">Start with readings</span><h2>Opening night, November 19, <em>2026</em></h2><p class="lede">The night the doors opened, the room hosted readings — the studio introducing itself the way book studios should: out loud, page by page, with people in the room.</p></div></section>

<section class="block"><div class="wrap"><span class="label">What&rsquo;s coming up</span><h2>Catch it before it&rsquo;s <em>full</em></h2><p class="lede">Event dates run on the studio&rsquo;s own calendar. Email <a href="mailto:{MAIL}">{MAIL}</a> and ask what&rsquo;s next — the inbox is answered, and open hours (Friday&ndash;Sunday, noon&ndash;4 p.m.) are the other way to catch the room in person.</p><div class="ctas"><a class="btn" href="mailto:{MAIL}">Email the studio</a><a class="btn ghost" href="/contact">Use the form</a></div></div></section>'''

readings_ld = webpage("/readings", "Readings and Special Events — Palimpsest Book Studio, Tampa FL",
    "Readings and special events for readers and writers at Palimpsest Book Studio, Ybor City, Tampa FL — opened November 19, 2026 with readings on opening night.",
    extra_graph=[{
        "@type": "Service", "@id": ORIGIN + "/readings#service",
        "name": "Readings and special events",
        "serviceType": "Event",
        "provider": {"@id": BIZ_ID},
        "areaServed": {"@type": "Place", "name": "Ybor City, Tampa, Florida"},
        "audience": {"@type": "Audience", "name": "Readers and writers"},
    }, breadcrumb([("Home", "/"), ("Browse", "/browse"), ("Readings", "/readings")])])

# ---------------------------------------------------------------- STORY
story_body = f'''<section class="minihero"><div class="wrap"><span class="ghostlayer" aria-hidden="true">palimpsest</span><span class="label">Our story</span><h1>The name is the <em>mission.</em></h1><p class="sub">A palimpsest is a writing surface scraped clean and written over — still carrying traces of what came before. That&rsquo;s what the studio is for: keeping earlier forms of the written word alive in a digital town.</p><hr class="rule"><div class="ctas"><a class="btn" href="/contact">Plan a visit</a><a class="btn ghost" href="/readings">See the calendar</a></div></div></section>

<section class="block"><div class="wrap"><span class="label">Say the name</span><h2>Pal&middot;imp&middot;sest — five syllables, two <em>histories</em></h2><p class="lede">The studio leans on the word&rsquo;s layers — it even hyphenates it, the way Creative Loafing Tampa did when it covered the opening. A book that gets resold, a zine passed hand to hand, a page reused: everything here keeps the trace of its earlier form.</p><span class="qsrc">stylization and name meaning per Creative Loafing Tampa, November 2026</span></div></section>

<section class="block alt"><div class="wrap"><span class="label">Behind the desk</span><h2>Micheal Hooker &amp; Mitzi Jo <em>Gordon</em></h2><p class="lede">Micheal Hooker ran Lector, the Tampa book and wine bar that made Ybor&rsquo;s literary scene a destination. Mitzi Jo Gordon ran the Bluebird Books Bus. Palimpsest is what the two launched next — built, as they told Creative Loafing Tampa, to honor their combined passion for nontraditional spaces.</p><span class="qsrc">founder histories per Creative Loafing Tampa, November 2026</span></div></section>

<section class="block"><div class="wrap"><span class="label">The room</span><h2>An orange room in an arts <em>building</em></h2><p class="lede">Room 200, second floor of Kress Contemporary — a Ybor City building that hosts galleries, a black box theatre, commercial photography studios and a fiber art boutique. The studio&rsquo;s own walls are bright orange, in the photographs Dave Decker made the week it opened.</p></div></section>

<section class="block alt"><div class="wrap"><span class="label">Opening night</span><h2>November 19, 2026</h2><p class="lede">Palimpsest opened with readings on opening night — books priced $7 to $25, zines and select consignment pieces on the shelves from day one. The studio&rsquo;s open hours since: Friday through Sunday, noon to 4 p.m.</p><span class="qsrc">opening, offerings and hours per Creative Loafing Tampa, November 2026</span><div class="ctas"><a class="btn" href="/contact">Talk to the studio</a><a class="btn ghost" href="{IG}" rel="noopener">Follow on Instagram</a></div></div></section>'''

story_ld = webpage("/story", "Our Story — Palimpsest Book Studio, Ybor City Tampa FL",
    "Palimpsest Book Studio in Tampa FL: founded by Micheal Hooker (Lector) and Mitzi Jo Gordon (Bluebird Books Bus), opened November 19, 2026 inside Kress Contemporary.",
    extra_graph=[breadcrumb([("Home", "/"), ("Our story", "/story")])])

# ---------------------------------------------------------------- CONTACT
contact_body = f'''<section class="minihero"><div class="wrap"><span class="ghostlayer" aria-hidden="true">hello</span><span class="label">Email or the form</span><h1>Talk to the <em>studio</em></h1><p class="sub">Questions, event ideas, or just hello — the form and the published inbox reach the same place.</p></div></section>
<section class="block"><div class="wrap"><div class="mapgrid"><div><form class="cform" method="post" action="/contact" accept-charset="utf-8"><h2>Leave a note</h2><div class="fields"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div><div class="field"><label for="f-phone">Phone <span style="font-weight:400;text-transform:none;letter-spacing:0">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div><div class="field full"><label for="f-email">Email <span style="font-weight:400;text-transform:none;letter-spacing:0">(optional — so we can answer)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div><div class="field full"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div><button class="btn" type="submit">Send note</button></div><p class="fineprint">Every note lands in the studio&rsquo;s inbox and gets a reply. No newsletter, no list.</p></form></div><div><div class="infocards"><div class="infocard"><h3>Email</h3><p><a href="mailto:{MAIL}">{MAIL}</a> — the inbox published on the studio&rsquo;s Kress Contemporary partner page.</p></div><div class="infocard"><h3>Where &amp; when</h3><p>Room 200, 1624 E 7th Ave (Kress Contemporary, second floor), Ybor City, Tampa, FL 33605 — open Friday&ndash;Sunday, noon&ndash;4 p.m.</p><p><a href="{MAP_LINK}" rel="noopener">Open in Google Maps &rarr;</a></p></div><div class="infocard"><h3>Elsewhere</h3><p>Instagram: <a href="{IG}" rel="noopener">@palimpsest.bookstudio</a></p></div></div><div class="mapcell" style="margin-top:14px">{MAP_EMBED}</div></div></div></div></section>'''

contact_ld = webpage("/contact", "Contact — Palimpsest Book Studio, Ybor City Tampa FL",
    "Contact Palimpsest Book Studio, Ybor City Tampa FL — email palimpsestreads@gmail.com or send a note with the form. Room 200, 1624 E 7th Ave. Open Friday–Sunday, noon–4 p.m.",
    extra_graph=[breadcrumb([("Home", "/"), ("Contact", "/contact")])])

# ---------------------------------------------------------------- PRIVACY
privacy_body = '''<section class="minihero"><div class="wrap"><span class="label">Plain terms</span><h1>Privacy</h1><p class="sub">This site sets no cookies and loads no advertising or tracking scripts. Nothing is counted with analytics.</p></div></section>
<section class="block"><div class="wrap"><p class="lede">The only information collected is what you choose to send through the contact form: your name, an optional phone number, an optional email address, and your message. It is used for one purpose — answering you — and kept only as long as needed to reply and to remember what you asked.</p><p>When you click through to Instagram or Google Maps, those pages run under their own privacy policies.</p><p class="fineprint">effective November 21, 2026</p><p>Questions about privacy? Use the <a href="/contact">contact form</a>, or email <a href="mailto:palimpsestreads@gmail.com">palimpsestreads@gmail.com</a>.</p></div></section>'''

privacy_ld = webpage("/privacy", "Privacy — Palimpsest Book Studio, Tampa FL",
    "No cookies, no trackers. Palimpsest Book Studio collects only what you send through its contact form, used to answer you.",
    extra_graph=[breadcrumb([("Home", "/"), ("Privacy", "/privacy")])])

# ---------------------------------------------------------------- THANKS / 404
thanks_body = f'''<section class="block util"><div class="wrap"><span class="label">Received</span><h1>Your note is <em>on its way</em></h1><p class="lede">It lands in the studio&rsquo;s inbox and gets read — no autoresponder maze. If you&rsquo;d rather say it in person, the room is open Friday to Sunday, noon to four.</p><div class="ctas" style="margin-top:24px"><a class="btn" href="{IG}" rel="noopener">Follow on Instagram</a><a class="btn ghost" href="/">Back to home</a></div></div></section>'''

notfound_body = f'''<section class="block util"><div class="wrap"><span class="label">404</span><h1>This page got <em>scraped clean.</em></h1><p class="lede">Whatever was written here is gone — but the shelves are still on, and so is the calendar.</p><div class="ctas" style="margin-top:24px"><a class="btn" href="/">Back to home</a><a class="btn ghost" href="/shelves">See the shelves</a><a class="btn ghost" href="/contact">Contact</a></div></div></section>'''

# ---------------------------------------------------------------- emit
PAGES = {
    "index.html": page("/", "Palimpsest Book Studio — Books, Zines and Readings in Ybor City, Tampa FL",
        "A new book studio inside Ybor City&rsquo;s Kress Contemporary — books ($7&ndash;$25), zines and select consignment pieces, plus readings and special events. Open Friday&ndash;Sunday, noon&ndash;4 p.m.",
        home_body, home_ld),
    "browse.html": page("/browse", "Browse the Studio — Palimpsest Book Studio, Ybor City Tampa FL",
        "Browse Palimpsest Book Studio in Tampa FL — the shelves (books $7&ndash;$25, zines, consignment), the event calendar, and the story behind the name.",
        browse_body, browse_ld),
    "shelves.html": page("/shelves", "Books, Zines and Consignment — Palimpsest Book Studio, Tampa FL",
        "Books priced $7&ndash;$25, zines and select consignment pieces at Palimpsest Book Studio in Ybor City, Tampa FL. Open Friday&ndash;Sunday, noon&ndash;4 p.m.",
        shelves_body, shelves_ld),
    "readings.html": page("/readings", "Readings and Special Events — Palimpsest Book Studio, Tampa FL",
        "Readings and special events for readers and writers at Palimpsest Book Studio, Ybor City, Tampa FL — opened November 19, 2026 with readings on opening night.",
        readings_body, readings_ld),
    "story.html": page("/story", "Our Story — Palimpsest Book Studio, Ybor City Tampa FL",
        "Palimpsest Book Studio in Tampa FL: founded by Micheal Hooker (Lector) and Mitzi Jo Gordon (Bluebird Books Bus), opened November 19, 2026 inside Kress Contemporary.",
        story_body, story_ld),
    "contact.html": page("/contact", "Contact — Palimpsest Book Studio, Ybor City Tampa FL",
        "Contact Palimpsest Book Studio, Ybor City Tampa FL — email palimpsestreads@gmail.com or send a note with the form. Room 200, 1624 E 7th Ave. Open Friday&ndash;Sunday, noon&ndash;4 p.m.",
        contact_body, contact_ld),
    "privacy.html": page("/privacy", "Privacy — Palimpsest Book Studio, Tampa FL",
        "No cookies, no trackers. Palimpsest Book Studio collects only what you send through its contact form, used to answer you.",
        privacy_body, privacy_ld),
    "thanks.html": page("/thanks", "Thanks — Palimpsest Book Studio, Ybor City Tampa FL",
        "Your note reached Palimpsest Book Studio. The studio reads every message — open Friday to Sunday, noon to four, in Room 200 of Kress Contemporary.",
        thanks_body, None, utility=True),
    "404.html": page("/404", "Page not found — Palimpsest Book Studio, Tampa FL",
        "That page is gone from the Palimpsest Book Studio site. The shelves, the calendar and the contact page are all still here.",
        notfound_body, None, utility=True),
}

SITEMAP = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
''' + "".join(f'<url><loc>{ORIGIN}{p}</loc><lastmod>2026-11-21</lastmod></url>\n' for p in ["/", "/browse", "/shelves", "/readings", "/story", "/contact", "/privacy"]) + "</urlset>\n"

ROBOTS = f'''User-agent: *
Disallow: /thanks
Disallow: /404

Sitemap: {ORIGIN}/sitemap.xml
'''

OG_SRC = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>og</title><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;background:#f5eddc;color:#241c11;font-family:'Iowan Old Style',Palatino,Georgia,serif;position:relative}}
.top{{height:14px;background:linear-gradient(90deg,#c14e1c 0%,#c14e1c 62%,#d8c49b 62%)}}
.pad{{padding:54px 68px;position:relative;z-index:2}}
.kick{{font-family:system-ui,sans-serif;font-size:19px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#a03f13}}
.ghost{{position:absolute;z-index:1;right:40px;top:36px;font-size:150px;line-height:1;font-style:italic;color:#d8c49b;opacity:.55;letter-spacing:.02em}}
h1{{font-size:96px;line-height:1.04;margin-top:120px;letter-spacing:-.015em}}
h1 em{{font-style:italic;color:#c14e1c}}
.tag{{font-size:31px;color:#5f5339;margin-top:26px;max-width:900px;line-height:1.4}}
.strip{{position:absolute;z-index:2;bottom:56px;left:68px;right:68px;display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid #c9b591;padding-top:22px;font-family:system-ui,sans-serif}}
.strip div{{font-size:21px;line-height:1.5;color:#241c11}}
.strip small{{display:block;font-size:16px;color:#5f5339;margin-top:4px}}
.mark{{position:absolute;z-index:3;right:68px;bottom:50px;width:120px;height:120px}}
</style></head><body><div class="top"></div><div class="pad"><span class="ghost">PAL&middot;IMP&middot;SEST</span><span class="kick">Book studio &middot; Ybor City, Tampa FL</span><h1>Palimpsest Book <em>Studio</em></h1><p class="tag">Books ($7&ndash;$25), zines and select consignment — plus readings and special events for readers and writers. Open Friday&ndash;Sunday, noon&ndash;4 p.m.</p></div><div class="strip"><div>Room 200, 1624 E 7th Ave<small>Kress Contemporary &middot; Ybor City &middot; Tampa, FL 33605</small></div><div style="text-align:right">palimpsestreads@gmail.com<small>@palimpsest.bookstudio</small></div></div><svg class="mark" viewBox="0 0 100 100"><rect x="30" y="18" width="46" height="60" rx="6" fill="none" stroke="#d8c49b" stroke-width="3"/><rect x="24" y="24" width="46" height="60" rx="6" fill="none" stroke="#c14e1c" stroke-width="3" opacity=".45"/><rect x="18" y="30" width="46" height="60" rx="6" fill="#f5eddc" stroke="#241c11" stroke-width="4"/><path d="M30 48h22M30 58h22M30 68h13" stroke="#241c11" stroke-width="3.4" stroke-linecap="round" opacity=".55"/><path d="M52 30v22l5-5 5 5V30" fill="#c14e1c"/></svg></body></html>
'''

os.makedirs("public", exist_ok=True)
for fn, doc in PAGES.items():
    with open(os.path.join("public", fn), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote public/" + fn, len(doc))
open("public/sitemap.xml", "w").write(SITEMAP)
open("public/robots.txt", "w").write(ROBOTS)
open("og-src.html", "w", encoding="utf-8").write(OG_SRC)
print("wrote sitemap, robots, og-src.html")
