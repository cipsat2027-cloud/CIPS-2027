"""Generates the site pages (HTML) into the project root. Run build_dist.py afterwards."""
import os
SC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SC)
exec(open(SC + "/icons.py").read())   # ICONS + ic()

SITE = "CIPS International Procurement &amp; Supply Chain Summit 2027"
NAV = [("index.html", "Home"), ("about-cips.html", "About CIPS"), ("about-summit.html", "About the Summit"), ("speakers.html", "Speakers"), ("awards.html", "Awards")]
ALT = 'alt="CIPS – Chartered Institute of Procurement &amp; Supply"'
THEMES = ["Transform", "Resilience", "Value", "Responsibility", "Future"]
ARROW = ic("arrow")
EVENT_NAME = '<p class="event-name"><span>CIPS International</span> Procurement &amp; Supply Chain Summit <b>2027</b></p>'


def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#fbfcff">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{SITE}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<link rel="stylesheet" href="css/site.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''


def header(page):
    cur = lambda h: ' aria-current="page"' if h == page else ""
    links = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in NAV)
    sheet = "".join(f'<li><a href="{h}"{cur(h)}><i>0{i+1}</i>{t}</a></li>' for i, (h, t) in enumerate(NAV))
    reg_cur = ' aria-current="page"' if page == "register.html" else ""
    return f'''<div class="top"><div class="wrap"><span>{SITE}</span><span><b>07 January 2027</b> &nbsp;|&nbsp; ITC Maratha, Mumbai, India</span></div></div>
<header class="hd" data-header><div class="wrap hd-in">
  <a class="logo" href="index.html" aria-label="{SITE} — home"><img src="assets/img/cips-logo-dark.png" {ALT} width="145" height="54"><small>International Procurement &amp; Supply Chain Summit</small></a>
  <nav class="mn" aria-label="Main">{links}</nav>
  <a class="btn hd-cta" href="register.html"{reg_cur}>Register Now {ARROW}</a>
  <button class="burger" data-menu-toggle aria-expanded="false" aria-controls="menu" aria-label="Menu"><span class="o">Menu</span><span class="c">Close</span><i></i></button>
</div></header>
<div class="sheet" id="menu" data-menu><ol>{sheet}</ol><div class="sf"><span>07 January 2027 &nbsp;|&nbsp; ITC Maratha, Mumbai, India</span><a class="btn" href="register.html">Register Now {ARROW}</a></div></div>
'''


def footer():
    ex = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV + [("register.html", "Register Now"), ("pay.html", "Complete a Payment")])
    th = "".join(f'<li><a href="about-summit.html#themes">{t}</a></li>' for t in THEMES)
    return f'''<footer class="foot"><div class="wrap">
<div class="foot-top"><h3>Intelligence. <em>Resilience.</em> Value.</h3><a class="btn light" href="register.html">Register Now {ARROW}</a></div>
<div class="foot-cols">
<div class="f-brand"><img src="assets/img/cips-logo-light.png" {ALT} width="171" height="64"><p>Advancing the procurement &amp; supply profession globally.</p></div>
<div><h4>Explore</h4><ul>{ex}</ul></div>
<div><h4>The Summit</h4><ul><li>07 January 2027</li><li>ITC Maratha</li><li>Mumbai, India</li><li>One-day leadership summit</li><li>Senior Procurement &amp; Supply Chain Leaders</li></ul></div>
<div><h4>Five Themes</h4><ul>{th}</ul></div></div>
<div class="foot-bot"><span>&copy; 2027 {SITE}</span><nav class="foot-legal" aria-label="Legal"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="cancellation.html">Cancellation Policy</a></nav><a href="#main">Back to top &uarr;</a></div></div></footer>
<script src="js/config.js"></script>
<script src="js/site.js"></script>
</body>
</html>
'''


ROUTE = '''<svg class="route" viewBox="0 0 320 120" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M8 100C70 10 170 10 240 70" stroke-dasharray="4 6"/><path d="M60 112C140 40 220 40 312 20" stroke-dasharray="4 6" opacity=".6"/><circle cx="8" cy="100" r="4" fill="currentColor"/><circle cx="240" cy="70" r="4" fill="currentColor"/><circle cx="312" cy="20" r="4" fill="currentColor"/><circle cx="60" cy="112" r="4" fill="currentColor"/></svg>'''


def cta_band(h="Be Part of the <em>Conversation</em>", btn="Register for the Summit",
             p="Connect with senior peers. Exchange ideas. Discover new perspectives. Take actionable thinking back to your organisation.", href="register.html"):
    return f'''<section class="cta-band"><div class="wrap"><div class="in reveal"><h2>{h}</h2><p>{p}</p><a class="btn light" href="{href}">{btn} {ARROW}</a></div></div></section>'''


# (photo, name, credential line, role line) — order and titles per the client's speaker invitation, Nov 2026
PEOPLE = [("ben-farrell.jpg", "Ben Farrell", "MBE", "Global CEO, CIPS"),
          ("sam-achampong.jpg", "Sam Achampong", "FCIPS", "Regional Director, CIPS | Middle East, Africa &amp; Asia-Pacific"),
          ("ram-trivedi.jpg", "Ram Trivedi", "FCIPS Chartered", "Country Director, CIPS"),
          ("shantanu-roy.jpg", "Shri Shantanu Roy", "Speaker", "Chairman and Managing Director, BEML, Ministry of Defence, Government of India"),
          ("mihir-kumar.jpg", "Shri Mihir Kumar", "IDAS", "Chief Executive Officer (CEO), Government e-Marketplace (GeM), Ministry of Commerce &amp; Industry, Government of India"),
          ("sandeep-verma.jpg", "Shri Sandeep Verma", "IAS", "Additional Chief Secretary, Government of Rajasthan"),
          ("ajit-kumar-mishra.jpg", "Ajit Mishra", "Speaker", "Director, IRCON (Government of India Undertaking)"),
          ("senthil-arasu.jpg", "Senthil Arasu", "Speaker", "Head of Procurement, Kotak Life"),
          ("viraj-lal.jpg", "Viraj Lal", "Speaker", "Sales Director – Europe, Resilinc")]
SPK_MORE = '<p class="spk-more reveal">More influential voices from India and the global procurement community to be announced soon.</p>'


def spk_cards(first_row=False):
    """Speaker cards. Photos: WebP at 480/800 px wide (made by build_dist.py), the JPEG as fallback.
    first_row=True (the Speakers page, where they are the first thing seen): the first 3 load straight away and skip the scroll fade."""
    def card(i, f, n, c, r):
        b = f[:-4]
        top = first_row and i < 3
        load = (' fetchpriority="high"' if i == 0 else "") + ' decoding="async"' if top else ' loading="lazy" decoding="async"'
        pic = (f'<picture><source type="image/webp" srcset="assets/img/{b}-480.webp 480w, assets/img/{b}-800.webp 800w" '
               f'sizes="(max-width: 560px) 46vw, (max-width: 960px) 92vw, 380px">'
               f'<img src="assets/img/{f}" alt="{n}, {r}" width="800" height="1000"{load}></picture>')
        return (f'<article class="card{" fade" if top else " reveal"}" style="--d:{i*0.1:.1f}s"><div class="ph">{pic}</div>'
                f'<small>{c}</small><h3>{n}</h3><p>{r}</p></article>')
    return "".join(card(i, *p) for i, p in enumerate(PEOPLE))


PROD_DOMAIN = "https://www.cips2027.online"
DOMAIN = os.environ.get("SITE_URL", PROD_DOMAIN).rstrip("/")   # set SITE_URL to build a preview for another host

# ---- SEO: search-result titles (<=60 chars) and descriptions (<=160 chars), keyed by file name
SEO = {
    "index.html": ("CIPS International Procurement &amp; Supply Chain Summit 2027",
                   "Senior procurement leaders, CPOs and CIPS leadership meet at ITC Maratha, Mumbai on 07 January 2027 to shape what comes next. Register now."),
    "about-cips.html": ("About CIPS – Chartered Institute of Procurement &amp; Supply",
                        "CIPS is the world’s largest professional body for procurement and supply: 70,000+ members in 150+ countries, a Royal Charter since 1992, and the MCIPS and FCIPS designations."),
    "about-summit.html": ("About the Summit | CIPS Procurement Summit 2027",
                          "A senior, international procurement leadership summit for CIPS leaders, CPOs and supply chain decision-makers. 07 January 2027, ITC Maratha."),
    "speakers.html": ("Speakers | CIPS Procurement &amp; Supply Chain Summit 2027",
                      "Meet the speakers: Ben Farrell MBE, Sam Achampong FCIPS and Ram Trivedi of CIPS, with Shantanu Roy (BEML), Mihir Kumar (GeM), Sandeep Verma IAS and more."),
    "awards.html": ("CIPS India Awards 2027 | Categories, Criteria &amp; Fees",
                    "CIPS India Awards 2027: 4 individual and 8 company categories, eligibility, judging criteria and nomination fees. 07 January 2027, ITC Maratha, Mumbai."),
    "nominate.html": ("Submit a Nomination | CIPS India Awards 2027",
                      "Nominate for the CIPS India Awards 2027: choose a category, complete the form, upload evidence, then review and pay the nomination fee online."),
    "pay.html": ("Complete Your Payment | CIPS Procurement Summit 2027",
                 "Pay your delegate registration or CIPS India Awards 2027 nomination fee online using the reference from your confirmation."),
    "register.html": ("Register for the CIPS Procurement Summit 2027 | ITC Maratha",
                      "Register to attend the CIPS International Procurement &amp; Supply Chain Summit on 07 January 2027 at ITC Maratha, Mumbai. Delegate fee ₹10,000 + GST."),
    "privacy.html": ("Privacy Policy | CIPS Procurement Summit 2027", None),
    "terms.html": ("Terms of Use | CIPS Procurement Summit 2027", None),
    "cancellation.html": ("Cancellation Policy | CIPS Procurement Summit 2027", "Cancellation, refund and substitution terms for registering as a delegate at the CIPS International Procurement &amp; Supply Chain Summit 2027."),
    "404.html": ("Page not found | CIPS Procurement Summit 2027", None),
}
CRUMBS = {"about-cips.html": "About CIPS", "about-summit.html": "About the Summit", "speakers.html": "Speakers",
          "awards.html": "Awards", "nominate.html": "Submit a Nomination", "register.html": "Register", "pay.html": "Complete Your Payment", "privacy.html": "Privacy Policy",
          "terms.html": "Terms of Use", "cancellation.html": "Cancellation Policy"}
_ORG = {"@type": "Organization", "@id": DOMAIN + "/#cips", "name": "CIPS – Chartered Institute of Procurement & Supply",
        "url": "https://www.cips.org", "logo": DOMAIN + "/assets/img/cips-logo-dark.png"}
_SPK = [(n, r.replace("&amp;", "&")) for _f, n, _c, r in PEOPLE]


def _event_ld():
    return {"@type": "Event", "@id": DOMAIN + "/#event",
            "name": "CIPS International Procurement & Supply Chain Summit 2027",
            "description": "A senior, international procurement leadership summit bringing together CIPS leadership, CPOs and supply chain decision-makers.",
            "startDate": "2027-01-07", "endDate": "2027-01-07",
            "eventStatus": "https://schema.org/EventScheduled",
            "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
            "location": {"@type": "Place", "name": "ITC Maratha", "address": {"@type": "PostalAddress", "addressLocality": "Mumbai", "addressRegion": "Maharashtra", "addressCountry": "IN"}},
            "image": [DOMAIN + "/assets/og-image.png"],
            "organizer": _ORG,
            "performer": [dict({"@type": "Person", "name": n, "jobTitle": t}, **({"worksFor": _ORG} if "CIPS" in t else {})) for n, t in _SPK],
            "offers": {"@type": "Offer", "url": DOMAIN + "/register.html", "price": "10000", "priceCurrency": "INR",
                       "availability": "https://schema.org/InStock", "validFrom": "2026-09-22"}}


def _ld(name, url):
    import json
    g = [_ORG, {"@type": "WebSite", "@id": DOMAIN + "/#site", "url": DOMAIN + "/", "name": "CIPS International Procurement & Supply Chain Summit 2027",
                "inLanguage": "en", "publisher": {"@id": DOMAIN + "/#cips"}}]
    if name in ("index.html", "about-summit.html", "speakers.html", "register.html"):
        g.append(_event_ld())
    if name == "awards.html":
        g.append({"@type": "ItemList", "name": "CIPS India Awards 2027 categories", "numberOfItems": len(AWARD_CATS),
                  "itemListElement": [{"@type": "ListItem", "position": int(n), "name": nm} for n, nm, _t, _i in AWARD_CATS]})
    if name in CRUMBS:
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": CRUMBS[name], "item": url}]})
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def write(name, html):
    import re as _re
    url = DOMAIN + "/" + ("" if name == "index.html" else name)
    title, desc = SEO[name]
    html = _re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1)
    html = _re.sub(r'(<meta property="og:title" content=")[^"]*"', rf'\g<1>{title}"', html, count=1)
    if desc:
        html = _re.sub(r'(<meta name="description" content=")[^"]*"', rf'\g<1>{desc}"', html, count=1)
        html = _re.sub(r'(<meta property="og:description" content=")[^"]*"', rf'\g<1>{desc}"', html, count=1)
    d = _re.search(r'<meta name="description" content="([^"]*)"', html).group(1)
    robots = "noindex, nofollow" if DOMAIN != PROD_DOMAIN else "noindex, follow" if name == "404.html" else "index, follow, max-image-preview:large, max-snippet:-1"
    alt = "CIPS International Procurement &amp; Supply Chain Summit 2027 — 07 January 2027, ITC Maratha, Mumbai"
    html = html.replace('<meta name="twitter:card" content="summary">',
        '<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="' + title + '">\n<meta name="twitter:description" content="' + d + '">\n<meta name="twitter:image" content="' + DOMAIN + '/assets/og-image.png">\n<meta name="twitter:image:alt" content="' + alt + '">')
    head_extra = ('<meta name="robots" content="' + robots + '">\n'
                  + ('' if name == "404.html" else '<link rel="canonical" href="' + url + '">\n<meta property="og:url" content="' + url + '">\n')
                  + '<meta property="og:locale" content="en_IN">\n<meta property="og:image" content="' + DOMAIN + '/assets/og-image.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="' + alt + '">')
    html = html.replace('<meta name="theme-color" content="#fbfcff">', '<meta name="theme-color" content="#fbfcff">\n' + head_extra)
    html = html.replace('<link rel="apple-touch-icon" href="assets/img/favicon.png">', '<link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png">')
    if name != "404.html":
        html = html.replace("</head>", _ld(name, url) + "\n</head>", 1)
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(html)



# ---- Page-header illustrations (one per page, fine-line editorial style)
import math as _m
def _pill(x, y, label, w=None):
    w = w or (len(label) * 8.2 + 30)
    return f'<g class="ilp"><rect x="{x - w/2:.1f}" y="{y - 14}" width="{w:.1f}" height="28" rx="14"/><text x="{x:.1f}" y="{y + 4}" text-anchor="middle">{label}</text></g>'

# Register: delegate pass
bars = ""
_x = 306
for w in [2,1,3,1,2,1,1,3,1,2,1,3,1,1,2,3,1,2]:
    bars += f'<rect x="{_x:.1f}" y="66" width="{w}" height="78"/>'; _x += w + 1.5
REGISTER_ART = f'''<figure class="il-fig" aria-hidden="true"><svg class="il solid" viewBox="0 0 400 330" fill="none" stroke="currentColor" stroke-width="1.5">
<g transform="rotate(-3 200 150)">
<path d="M22 36H378V126a17 17 0 0 0 0 34V254H22V160a17 17 0 0 0 0-34Z" fill="#0b5cff" stroke="none"/>
<line x1="292" y1="52" x2="292" y2="238" stroke="#fff" stroke-dasharray="3 6" stroke-opacity=".55"/>
<text class="cap" x="46" y="74">DELEGATE PASS</text>
<text class="ser" x="46" y="112" font-size="23">Procurement &amp; Supply</text>
<text class="ser" x="46" y="140" font-size="23" font-style="italic" fill="#7fe3ff">Chain Summit 2027</text>
<line x1="46" y1="172" x2="120" y2="172" stroke="#00c2ff" stroke-width="2"/>
<text class="cap" x="46" y="198">07 JAN 2027 &#183; ITC MARATHA</text>
<text class="cap" x="46" y="220">SENIOR PROCUREMENT LEADERS</text>
<g fill="#fff" stroke="none">{bars}</g>
<text class="cap" x="306" y="166" font-size="8.5">NO. 2027</text>
<g class="stamp" stroke="#00c2ff" transform="rotate(-12 335 208)"><circle cx="335" cy="208" r="27" stroke-dasharray="2 4"/><circle cx="335" cy="208" r="20"/><path d="M325 208l7 7 13-14" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>
</g>
<path d="M40 302C120 268 280 268 360 302" stroke-dasharray="4 7" stroke-opacity=".6"/><circle cx="40" cy="302" r="4" fill="currentColor" stroke="none"/><circle cx="360" cy="302" r="4" fill="currentColor" stroke="none"/>
</svg></figure>'''

# About the Summit: roundtable + five formats
def _summit_art():
    cx, cy = 200, 190
    seats = ""
    for i in range(10):
        a = _m.radians(-90 + 36 * i)
        sx, sy = cx + 74 * _m.cos(a), cy + 74 * _m.sin(a)
        seats += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="9.5" fill="#0b5cff" stroke="none"/>'
    forms = ["KEYNOTES", "PANELS", "FIRESIDE", "ROUNDTABLES", "NETWORKING"]
    pills = ""
    for i, f in enumerate(forms):
        a = _m.radians(-90 + 72 * i)
        px, py = cx + 152 * _m.cos(a), cy + 138 * _m.sin(a)
        pills += _pill(px, py, f)
    return f'''<figure class="il-fig" aria-hidden="true"><svg class="il solid" viewBox="0 0 400 380" fill="none" stroke="currentColor" stroke-width="1.5">
<ellipse cx="{cx}" cy="{cy}" rx="152" ry="138" stroke-dasharray="3 8" stroke-opacity=".5"/>
<circle cx="{cx}" cy="{cy}" r="48" fill="#0b5cff" stroke="none"/>
<text class="cap" x="{cx}" y="{cy - 3}" text-anchor="middle" font-size="8.5">ONE DAY</text><text class="ser" x="{cx}" y="{cy + 16}" text-anchor="middle" font-size="17" font-style="italic" fill="#7fe3ff">150–200</text>
{seats}
{pills}
</svg></figure>'''
SUMMIT_ART = _summit_art()

# Speakers: "voices" stage - mic, ripples, confirmed portraits + open slots
def _speakers_art():
    cx, cy = 220, 274
    R = 154
    slots = [("ben-farrell.jpg", "Ben Farrell"), ("sam-achampong.jpg", "Sam Achampong"), ("ram-trivedi.jpg", "Ram Trivedi")]
    angs = [-138, -90, -42]
    defs = spokes = nodes = dots = ""
    for i, ((img, nm), ang) in enumerate(zip(slots, angs)):
        a = _m.radians(ang)
        nx, ny = cx + R * _m.cos(a), cy + (R - 6) * _m.sin(a)
        r = 37
        d = f"M{cx + 50 * _m.cos(a):.1f} {cy + 46 * _m.sin(a):.1f}L{nx:.1f} {ny:.1f}"
        spokes += f'<path d="{d}" stroke="#fff" stroke-opacity=".38" stroke-width="1.3" stroke-dasharray="3 6"/>'
        dots += f'<circle r="3" fill="#7fe3ff"><animateMotion dur="{3 + (i % 3) * .7:.1f}s" begin="-{i * .8:.1f}s" repeatCount="indefinite" path="{d}"/></circle>'
        if nm:
            defs += f'<clipPath id="sp{i}"><circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r}"/></clipPath>'
            h = r * 2.5
            nodes += (f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r + 6}" fill="#fff" fill-opacity=".14"/>'
                      f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r}" fill="#fff"/>'
                      f'<image href="assets/img/{img[:-4]}-480.webp" x="{nx - h / 2:.1f}" y="{ny - h * .42:.1f}" width="{h:.1f}" height="{h:.1f}" clip-path="url(#sp{i})" preserveAspectRatio="xMidYMid slice"/>'
                      f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r}" fill="none" stroke="#fff" stroke-width="3"/>')
        else:
            nodes += (f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{r}" fill="#fff" fill-opacity=".08" stroke="#7fe3ff" stroke-width="1.6" stroke-dasharray="4 5"/>'
                      f'<text class="qm" x="{nx:.1f}" y="{ny + 10:.1f}" text-anchor="middle">?</text>')
    ripples = "".join(f'<circle cx="{cx}" cy="{cy}" r="52" fill="none" stroke="#7fe3ff" stroke-width="1.4"><animate attributeName="r" from="52" to="200" dur="5.4s" begin="-{k * 1.8:.1f}s" repeatCount="indefinite"/><animate attributeName="opacity" from=".6" to="0" dur="5.4s" begin="-{k * 1.8:.1f}s" repeatCount="indefinite"/></circle>' for k in range(3))
    return f'''<figure class="il-fig spk-art" aria-hidden="true"><svg class="il" viewBox="0 0 440 420" role="img">
<defs><linearGradient id="spg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a6bff"/><stop offset="1" stop-color="#0a3fbd"/></linearGradient>
<pattern id="spgrid" width="22" height="22" patternUnits="userSpaceOnUse"><path d="M22 0H0V22" fill="none" stroke="#fff" stroke-opacity=".07"/></pattern>
<clipPath id="spcard"><rect width="440" height="420" rx="22"/></clipPath>{defs}</defs>
<rect width="440" height="420" rx="22" fill="url(#spg)"/><rect width="440" height="420" rx="22" fill="url(#spgrid)"/>
<rect x="6" y="6" width="428" height="408" rx="17" fill="none" stroke="#fff" stroke-opacity=".28"/>
<g clip-path="url(#spcard)">{ripples}
<ellipse cx="{cx}" cy="{cy + 6}" rx="190" ry="52" fill="none" stroke="#fff" stroke-opacity=".16" stroke-dasharray="3 7"/></g>
<text class="sk" x="220" y="40" text-anchor="middle">VOICES FROM INDIA &amp; AROUND THE WORLD</text>
{spokes}{dots}{nodes}
<circle cx="{cx}" cy="{cy}" r="46" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="46" fill="none" stroke="#00c2ff" stroke-width="2.5" stroke-dasharray="2 6"/>
<g transform="translate({cx - 17} {cy - 19}) scale(1.42)" fill="none" stroke="#0b5cff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{ICONS["mic"]}</g>
<line x1="24" y1="352" x2="416" y2="352" stroke="#fff" stroke-opacity=".3" stroke-dasharray="3 6"/>
<g><rect x="96" y="368" width="248" height="30" rx="15" fill="#fff"/><text class="sn" x="220" y="387" text-anchor="middle">CONFIRMED CIPS LEADERSHIP</text></g>
</svg></figure>'''
SPEAKERS_ART = _speakers_art()

# About CIPS: chartered seal (emblem + four values)
def _cips_art():
    cx, cy = 190, 190
    def icon(name, x, y):
        return f'<g transform="translate({x - 13:.1f} {y - 13:.1f}) scale(1.08)" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'
    med = ""
    spots = [("award", 0, -148, "EXCELLENCE", 0, -184), ("globe", 148, 0, "COMMUNITY", 186, 0), ("book", 0, 148, "KNOWLEDGE", 0, 184), ("compass", -148, 0, "LEADERSHIP", -186, 0)]
    pills = ""
    for ic_name, dx, dy, lab, px, py in spots:
        mx, my = cx + dx, cy + dy
        med += f'<circle cx="{mx}" cy="{my}" r="28" fill="#0b5cff" stroke="#fbfcff" stroke-width="3"/>{icon(ic_name, mx, my)}'
    # community network inside the globe
    import random as _r
    _r.seed(4)
    pts = []
    for k in range(9):
        a = _m.radians(k * 40 + _r.randint(-10, 10)); r = _r.randint(72, 104)
        pts.append((cx + r * _m.cos(a), cy + r * _m.sin(a)))
    net = "".join(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke-dasharray="2 5" stroke-opacity=".55"/>' for a, b in zip(pts, pts[1:] + pts[:1]))
    net += "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="#7fe3ff" stroke="none"/>' for x, y in pts)
    return f'''<figure class="il-fig" aria-hidden="true"><svg class="il solid" viewBox="0 0 380 380" fill="none" stroke="currentColor" stroke-width="1.5">
<defs><path id="cipsring" d="M{cx - 148} {cy} a148 148 0 1 1 296 0 a148 148 0 1 1 -296 0"/></defs>
<path d="M{cx - 163} {cy}a163 163 0 1 0 326 0a163 163 0 1 0 -326 0ZM{cx - 133} {cy}a133 133 0 1 1 266 0a133 133 0 1 1 -266 0Z" fill="#0b5cff" fill-rule="evenodd" stroke="none"/>
<g class="rt"><text class="ringtxt" text-anchor="middle"><textPath href="#cipsring" startOffset="116">CHARTERED INSTITUTE</textPath></text><text class="ringtxt" text-anchor="middle"><textPath href="#cipsring" startOffset="348">PROCUREMENT &amp; SUPPLY</textPath></text><text class="ringtxt" text-anchor="middle"><textPath href="#cipsring" startOffset="581">PROFESSIONAL BODY</textPath></text><text class="ringtxt" text-anchor="middle"><textPath href="#cipsring" startOffset="813">GLOBAL COMMUNITY</textPath></text></g>
<circle cx="{cx}" cy="{cy}" r="112" fill="#0b5cff" stroke="none"/>
<g stroke="#fff">
<ellipse cx="{cx}" cy="{cy}" rx="44" ry="112" stroke-opacity=".28"/><ellipse cx="{cx}" cy="{cy}" rx="84" ry="112" stroke-opacity=".28"/><line x1="{cx}" y1="{cy - 112}" x2="{cx}" y2="{cy + 112}" stroke-opacity=".28"/>
<ellipse cx="{cx}" cy="{cy}" rx="112" ry="40" stroke-opacity=".28"/><line x1="{cx - 112}" y1="{cy}" x2="{cx + 112}" y2="{cy}" stroke-opacity=".28"/>
{net}</g>
<circle cx="{cx}" cy="{cy}" r="56" fill="#fff" stroke="#fbfcff" stroke-width="3"/>
<image href="assets/img/cips-emblem.png" x="{cx - 43}" y="{cy - 45}" width="86" height="90"/>
{med}
</svg></figure>'''
CIPS_ART = _cips_art()



# ---- Home hero: editorial globe with hub labels
import json as _json
# hub labels over the globe (left/top in % of the globe image; "main" = the host city)
_lab = [{"t": "New Delhi", "l": 64.72, "tp": 35.73, "main": True}, {"t": "London", "l": 15.33, "tp": 13.97, "main": False},
        {"t": "Dubai", "l": 26.86, "tp": 49.53, "main": False}, {"t": "Singapore", "l": 83.83, "tp": 67.9, "main": False},
        {"t": "Shanghai", "l": 86.19, "tp": 30.86, "main": False}]
HERO_GLOBE = '<figure class="hero-globe"><img src="assets/globe-editorial.svg?v=2" alt="Global routes connecting New Delhi with London, Dubai, Singapore and other hubs" width="392" height="392" fetchpriority="high" decoding="async">' + "".join(
    f'<span class="hg-pill{" main" if l["main"] else ""}" style="left:{l["l"]}%;top:{l["tp"]}%">{l["t"]}</span>' for l in _lab) + '</figure>'

# =========================================================== HOME
tick = "".join(f"<span>{t}</span>" for t in THEMES) * 4
rows = "".join(f'''<a class="trow reveal" href="about-summit.html#themes"><i>0{i+1}</i><b>{t}</b><p>{d}</p>{ARROW}</a>''' for i, (t, d) in enumerate([
    ("Transform", "AI, digital procurement and technology-led transformation"),
    ("Resilience", "Risk, agility and stronger supply networks"),
    ("Value", "Strategic sourcing, productivity and enterprise impact"),
    ("Responsibility", "Sustainability, ethics and responsible procurement"),
    ("Future", "Leadership, talent and future-ready organisations")]))
chain = "".join(f"<li><i>{ic(i)}</i><b>{t}</b></li>" for i, t in [("search", "Sourcing"), ("factory", "Production"), ("ship", "Logistics"), ("warehouse", "Warehousing"), ("truck", "Delivery")])

VENN = '''<figure class="venn reveal" style="--d:.1s" aria-label="Insights, connections and perspectives, leading to intelligence, resilience and value"><svg viewBox="0 0 400 380" role="img" aria-hidden="true">
<circle class="orbit" cx="200" cy="190" r="178" fill="none" stroke="#0b5cff" stroke-opacity=".45" stroke-width="1.2" stroke-dasharray="4 8"/>
<circle cx="150" cy="150" r="110" fill="#0b5cff" fill-opacity=".86" stroke="#fbfcff" stroke-width="2.5"/>
<circle cx="250" cy="150" r="110" fill="#0b5cff" fill-opacity=".86" stroke="#fbfcff" stroke-width="2.5"/>
<circle cx="200" cy="236" r="110" fill="#0b5cff" fill-opacity=".86" stroke="#fbfcff" stroke-width="2.5"/>
<text class="vl" x="104" y="112" text-anchor="middle">Insights</text>
<text class="vl" x="296" y="112" text-anchor="middle">Connections</text>
<text class="vl" x="200" y="318" text-anchor="middle">Perspectives</text>
<path d="M200 166l6.5 12-6.5 12-6.5-12z" fill="#00c2ff"/>
<text class="vc" x="200" y="204" text-anchor="middle">LEAD</text>
<g class="pill"><rect x="150" y="1" width="100" height="24" rx="12"/><text x="200" y="17" text-anchor="middle">Intelligence</text></g>
<g class="pill"><rect x="311" y="267" width="86" height="24" rx="12"/><text x="354" y="283" text-anchor="middle">Resilience</text></g>
<g class="pill"><rect x="3" y="267" width="86" height="24" rx="12"/><text x="46" y="283" text-anchor="middle">Value</text></g>
</svg></figure>'''

def _award_fig():
    """Three CIPS-branded trophies on a podium: a crystal (Excellence), the CIPS cup and a star column (Leadership)."""
    W, H, cx = 460, 460, 230
    star = "M0,-8 L2,-2 L8,0 L2,2 L0,8 L-2,2 L-8,0 L-2,-2 Z"
    sparkles = "".join(f'<path class="aw-sp" d="{star}" transform="translate({x} {y}) scale({k})" style="animation-delay:{d}s"/>'
                       for x, y, k, d in [(70, 120, 0.7, 0), (392, 96, 0.55, -0.6), (402, 238, 0.5, -1.1), (56, 262, 0.45, -1.8), (300, 46, 0.4, -0.9)])
    def star5(x, y, R, r):
        pts = " ".join(f"{x + (R if i % 2 == 0 else r) * _m.sin(_m.pi * i / 5):.1f},{y - (R if i % 2 == 0 else r) * _m.cos(_m.pi * i / 5):.1f}" for i in range(10))
        return pts
    def base(x0, x1, top, h, label):
        mid = (x0 + x1) / 2
        return (f'<rect x="{x0}" y="{top}" width="{x1 - x0}" height="{h}" rx="2" fill="url(#awbase)"/>'
                f'<rect x="{x0}" y="{top}" width="{x1 - x0}" height="2" fill="#4d8dff" opacity=".7"/>'
                f'<rect x="{x0 + 8}" y="{top + 6}" width="{x1 - x0 - 16}" height="{h - 12}" rx="1.5" fill="none" stroke="#bfe9ff" stroke-opacity=".35"/>'
                f'<text x="{mid}" y="{top + h / 2 + 2.2}" text-anchor="middle" class="aw-pl">{label}</text>')
    podium = (f'<ellipse cx="{cx}" cy="446" rx="214" ry="10" fill="#4d8dff" opacity=".16"/>'
              f'<path d="M34 400H170V444H34Z" fill="#0b1f4d"/><path d="M290 400H426V444H290Z" fill="#0b1f4d"/>'
              f'<path d="M34 400H170V404H34Z M290 400H426V404H290Z" fill="#2f6bff" opacity=".55"/>'
              f'<path d="M150 372H310V444H150Z" fill="#0d2766"/><path d="M150 372H310V376H150Z" fill="#4d8dff" opacity=".8"/>'
              f'<text x="{cx}" y="404" text-anchor="middle" class="aw-pod">CIPS</text>'
              f'<text x="{cx}" y="422" text-anchor="middle" class="aw-pod-s">INDIA AWARDS 2027</text>'
              )
    # left: faceted crystal on a plinth
    crystal = (base(60, 144, 378, 22, "EXCELLENCE") +
               '<polygon points="84,378 120,378 128,262 104,206 80,250" fill="#bfe9ff" opacity=".22"/>'
               '<polygon points="84,378 104,378 104,206 80,250" fill="url(#awglass)"/>'
               '<polygon points="104,378 120,378 128,262 104,206" fill="#7fb7ff" opacity=".55"/>'
               '<polygon points="104,206 128,262 104,240 80,250" fill="#fff" opacity=".55"/>'
               '<polygon points="84,378 120,378 128,262 104,206 80,250" fill="none" stroke="#fff" stroke-opacity=".75" stroke-width="1.2" stroke-linejoin="round"/>'
               f'<polygon points="{star5(104, 300, 9, 4)}" fill="#fff" opacity=".85"/>')
    # right: star on a fluted column
    column = (base(316, 400, 378, 22, "LEADERSHIP") +
              '<rect x="344" y="298" width="28" height="80" fill="url(#awcup)"/>'
              '<rect x="340" y="292" width="36" height="8" rx="2" fill="#0a3fbd"/><rect x="340" y="370" width="36" height="8" rx="2" fill="#0a3fbd"/>'
              '<path d="M352 300V370M358 300V370M364 300V370" stroke="#fff" stroke-opacity=".28"/>'
              '<rect x="355" y="276" width="6" height="18" fill="#0a3fbd"/>'
              f'<polygon class="aw-star" points="{star5(358, 252, 30, 13)}" fill="url(#awstar)" stroke="#fff" stroke-width="2" stroke-linejoin="round"/>')
    # centre: the CIPS cup with the emblem
    cup = (f'<circle cx="{cx}" cy="186" r="118" fill="url(#awglow)"/>'
           + base(178, 282, 338, 34, "CIPS INDIA AWARDS &#183; 2027") +
           f'<rect x="192" y="318" width="76" height="20" rx="2" fill="#0a2a95"/><rect x="192" y="318" width="76" height="2" fill="#4d8dff" opacity=".7"/>'
           f'<path d="M216 318L222 290H238L244 318Z" fill="url(#awcup)"/>'
           f'<ellipse cx="{cx}" cy="286" rx="18" ry="6" fill="#0a3fbd"/>'
           f'<path d="M222 286L226 262H234L238 286Z" fill="url(#awcup)"/>'
           f'<path d="M166 128C128 128 124 196 186 214" fill="none" stroke="url(#awcup)" stroke-width="10" stroke-linecap="round"/>'
           f'<path d="M294 128C332 128 336 196 274 214" fill="none" stroke="url(#awcup)" stroke-width="10" stroke-linecap="round"/>'
           f'<path d="M158 118H302C302 204 268 250 244 262H216C192 250 158 204 158 118Z" fill="url(#awcup)" stroke="#fff" stroke-opacity=".55" stroke-width="1.5"/>'
           f'<ellipse cx="{cx}" cy="118" rx="72" ry="11" fill="#0733a8" stroke="#bfe9ff" stroke-opacity=".8" stroke-width="1.5"/>'
           f'<path d="M172 128C173 186 192 228 212 246C198 222 184 186 184 128Z" fill="#fff" opacity=".32"/>'
           f'<circle cx="{cx}" cy="178" r="31" fill="#fff"/><circle cx="{cx}" cy="178" r="35" fill="none" stroke="#bfe9ff" stroke-opacity=".6" stroke-dasharray="2 4"/>'
           f'<image href="assets/img/cips-emblem.png" x="{cx - 21}" y="155.5" width="42" height="44"/>')
    rings = (f'<g class="ring-spin"><circle cx="{cx}" cy="186" r="150" fill="none" stroke="#4d8dff" stroke-opacity=".4" stroke-width="1.2" stroke-dasharray="3 9"/>'
             f'<circle cx="{cx}" cy="186" r="182" fill="none" stroke="#00c2ff" stroke-opacity=".25" stroke-width="1" stroke-dasharray="1 12"/></g>')
    return (f'<figure class="award-fig" aria-hidden="true"><svg viewBox="0 0 {W} {H}">'
            '<defs>'
            '<linearGradient id="awbeam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4d8dff" stop-opacity=".45"/><stop offset="1" stop-color="#4d8dff" stop-opacity="0"/></linearGradient>'
            '<linearGradient id="awcup" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7fb2ff"/><stop offset=".35" stop-color="#2f74ff"/><stop offset=".7" stop-color="#0b5cff"/><stop offset="1" stop-color="#0733a8"/></linearGradient>'
            '<linearGradient id="awbase" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#123a9e"/><stop offset="1" stop-color="#061a4d"/></linearGradient>'
            '<linearGradient id="awglass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e6f4ff" stop-opacity=".95"/><stop offset="1" stop-color="#7fe3ff" stop-opacity=".45"/></linearGradient>'
            '<linearGradient id="awstar" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#7fe3ff"/><stop offset="1" stop-color="#2f74ff"/></linearGradient>'
            '<radialGradient id="awglow"><stop offset="0" stop-color="#4d8dff" stop-opacity=".45"/><stop offset="1" stop-color="#4d8dff" stop-opacity="0"/></radialGradient>'
            '</defs>'
            f'<text x="{cx}" y="262" text-anchor="middle" class="aw-yr">2027</text>'
            f'<path d="M{cx} -24L{cx + 132} 300L{cx - 132} 300Z" fill="url(#awbeam)"/>'
            f'{rings}{sparkles}{podium}{crystal}{column}{cup}</svg></figure>')
AWARD_FIG = _award_fig()

WIIFM = ["The event is intended for senior procurement and supply chain leaders, providing opportunities for strategic networking, collaboration and knowledge sharing.",
         "Gain practical insights on AI, resilience, sourcing, sustainability and transformation.",
         "Connect with CPOs and decision-makers from India and international markets.",
         "Discover new ideas, solutions and approaches that can be applied within your organisation.",
         "Benchmark with peers facing similar procurement and supply chain challenges.",
         "Build high-value professional relationships across industries and markets.",
         "Take back actionable perspectives to improve strategy, performance and business impact."]
wiifm = "".join(f'<li class="reveal" style="--d:{i*0.05:.2f}s"><i>0{i+1}</i><p>{w}</p></li>' for i, w in enumerate(WIIFM))

home = head(SITE, "Where global procurement leadership meets to shape what comes next. A senior, international summit for CIPS leadership, top CPOs and supply chain decision-makers. 07 January 2027, ITC Maratha, Mumbai, India.") + header("index.html") + f'''
<main id="main">
<div class="wrap"><section class="hero">
  <div class="fade"><div class="ev-row">{EVENT_NAME}<img class="powered-by" src="assets/img/powered-by-navi-mumbai.png" alt="Powered by CIPS Navi Mumbai Branch" width="150" height="84"></div><div class="kicker"><span>Intelligence</span><span>Resilience</span><span>Value</span></div>
    <h1>Where Procurement Leaders <em>Shape What Comes Next</em></h1>
    <p class="lede">A premier international platform bringing together senior procurement and supply chain leaders from India and global markets to exchange perspectives, challenge convention and explore the future of the profession.</p>
    <div class="cta"><a class="btn" href="register.html">Register Now {ARROW}</a><a class="btn ghost" href="about-summit.html">Explore the Summit</a></div></div>
  <aside class="issue fade" style="--d:.15s">{HERO_GLOBE}
    <dl><div class="ev"><dt>Event</dt><dd>{SITE}</dd></div><div><dt>Date</dt><dd>07 January 2027</dd></div><div><dt>Venue</dt><dd>ITC Maratha, Mumbai, India</dd></div><div><dt>Audience</dt><dd>Senior Procurement &amp; Supply Chain Leaders</dd></div></dl></aside>
</section></div>
<div class="ticker" aria-hidden="true"><div>{tick}</div></div>

<section class="sec"><div class="wrap">
  <div class="two"><div class="reveal"><div class="eyebrow">The Summit</div><h2>The Leadership Conversation <em>Procurement Needs Now</em></h2></div>
  <div class="body drop reveal" style="--d:.1s"><p>Procurement has moved far beyond sourcing and cost control. Today, it sits at the centre of <strong>business resilience, digital transformation, sustainability, enterprise value and growth.</strong></p><p>The CIPS International Procurement &amp; Supply Chain Summit 2027 brings together the leaders driving this transformation — creating one focused platform for insight, collaboration and meaningful industry dialogue.</p></div></div>
  <div class="chain-wrap reveal"><p class="chain-cap">Procurement connects every link in the chain</p><ul class="chain">{chain}</ul></div>
</div></section>

<div class="wrap"><div class="stats reveal"><div class="stat"><b><span data-count="150">150</span>–<span data-count="200">200</span></b><p>Senior Decision-Makers</p></div><div class="stat"><b class="t">India &amp; Beyond</b><p>Global Procurement Community</p></div><div class="stat"><b><span data-count="1">1</span> Day</b><p>High-Impact Leadership Exchange</p></div><div class="stat"><b><span data-count="5">5</span></b><p>Strategic Themes — Transform, Resilience, Value, Responsibility, Future</p></div></div></div>

<section class="sec" id="why-attend"><div class="wrap two why">
  <div class="why-l"><div class="reveal"><div class="eyebrow">What’s In It for You</div><h2>Gain the insights, connections and perspectives you need to lead procurement with greater <em>intelligence, resilience and value.</em></h2></div>
    {VENN}</div>
  <ol class="wiifm">{wiifm}</ol>
</div></section>

<section class="sec tint"><div class="wrap"><div class="eyebrow">Five Themes</div><h2 style="margin-bottom:56px">The Conversations <em>Shaping the Profession</em></h2>{rows}</div></section>

<section class="sec"><div class="wrap"><div class="eyebrow">Speakers</div><h2 style="margin-bottom:24px" class="reveal">Leadership Voices from <em>India &amp; Around the World</em></h2><p class="lede reveal" style="margin-bottom:56px">Hear from senior CIPS leadership, government and public-sector leaders, CPOs and business leaders sharing real-world perspectives on the future of procurement and supply chain.</p>
<div class="spk">{spk_cards()}</div>{SPK_MORE}
<div class="more" style="justify-content:flex-end"><a class="btn ghost" href="speakers.html">Meet the Speakers {ARROW}</a></div></div></section>

<section class="awards"><div class="wrap awards-grid">
  <div class="awards-copy">
    <div class="eyebrow reveal">CIPS India Awards 2027</div>
    <h2 class="reveal" style="--d:.06s">Celebrating <em>Procurement Excellence</em></h2>
    <p class="lede reveal" style="--d:.1s">Recognising Excellence. Celebrating Leadership. Inspiring the Future. Across 12 award categories, the awards celebrate exceptional leadership, innovation, sustainability, digital transformation and measurable contributions to the profession.</p>
    <ul class="awards-chips reveal" style="--d:.14s"><li>4 Individual</li><li>8 Company</li><li>07 January 2027</li><li>ITC Maratha</li></ul>
    <a class="btn light reveal" style="--d:.18s" href="awards.html">Explore the Awards {ARROW}</a>
  </div>
  <div class="reveal" style="--d:.12s">{AWARD_FIG}</div>
</div></section>

{cta_band()}
</main>
''' + footer()
write("index.html", home)

# =========================================================== ABOUT CIPS
def _anchor_art():
    """Summit hub linked to the five forces named in the 'Why CIPS anchors' copy."""
    cx, cy, R = 240, 236, 165
    forces = [("globe", "GEOPOLITICS", -90), ("cpu", "AI &amp; DIGITAL", -18), ("shield", "RESILIENCE", 54), ("leaf", "SUSTAINABILITY", 126), ("ship", "TRADE CORRIDORS", 198)]
    spokes = nodes = ""
    for i, (name, lab, deg) in enumerate(forces):
        a = _m.radians(deg); x, y = cx + R * _m.cos(a), cy + R * _m.sin(a)
        ly = y - 46 if deg == -90 else y + 52
        spokes += f'<line class="flow" style="animation-delay:{-i * 0.3:.1f}s" x1="{x:.1f}" y1="{y:.1f}" x2="{cx}" y2="{cy}"/>'
        nodes += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="31" fill="#0a1b36" stroke="#4d8dff" stroke-width="1.5"/>'
                  f'<g transform="translate({x - 13:.1f} {y - 13:.1f}) scale(1.08)" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'
                  f'<text class="cap" x="{x:.1f}" y="{ly:.1f}" text-anchor="middle">{lab}</text>')
    return f'''<svg class="il solid st-art" viewBox="0 0 480 480" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
<circle cx="{cx}" cy="{cy}" r="{R}" stroke="#fff" stroke-opacity=".14" stroke-dasharray="2 6"/>
<circle cx="{cx}" cy="{cy}" r="110" stroke="#fff" stroke-opacity=".08"/>
<g class="orbit"><circle cx="{cx + R}" cy="{cy}" r="3.5" fill="#7fe3ff" stroke="none"/><circle cx="{cx - R}" cy="{cy}" r="3.5" fill="#7fe3ff" stroke="none"/></g>
<g stroke="#7fb0ff" stroke-width="1.8">{spokes}</g>
<circle class="pulse" cx="{cx}" cy="{cy}" r="74" stroke="#4d8dff"/>
<circle cx="{cx}" cy="{cy}" r="74" fill="#0b5cff" stroke="none"/>
<text class="cap" x="{cx}" y="{cy - 22}" text-anchor="middle" style="fill:#cfe0ff">CIPS</text>
<text class="ser" x="{cx}" y="{cy + 8}" text-anchor="middle" font-size="26" font-weight="700" letter-spacing="-.5">Summit</text>
<text class="ser" x="{cx}" y="{cy + 34}" text-anchor="middle" font-size="26" font-weight="700" letter-spacing="-.5">2027</text>
{nodes}
</svg>'''
VISION = [("cpu", "Intelligent"), ("shield", "Resilient"), ("search", "Transparent"), ("award", "Ethically governed")]

MILESTONES = [("1932", "The Beginning", "Founded in the United Kingdom as the Purchasing Officers Association (POA), establishing early professional standards for industrial purchasing during a period of global economic uncertainty."),
              ("1967", "Strengthening the Profession", "The formation of the Institute of Purchasing and Supply (IPS), through a merger with the Institute of Public Supplies, brought together commercial and public-sector procurement expertise."),
              ("1992", "Royal Charter Recognition", "Awarded a Royal Charter by Her Majesty Queen Elizabeth II, recognising procurement as a chartered profession committed to professional excellence and public benefit."),
              ("2014", "A New Global Identity", "Renamed the Chartered Institute of Procurement &amp; Supply, reflecting the expanding role of procurement across end-to-end supply chain management and strengthening the recognition of Chartered Professional status."),
              ("Today", "A Global Professional Authority", "CIPS continues to advance international procurement standards through its regional presence and professional networks across the United Kingdom, Europe, the Middle East, Africa, Asia, Australasia and the Americas.")]
tl = "".join(f'<li class="reveal" style="--d:{i*0.07:.2f}s"><b>{y}</b><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (y, t, d) in enumerate(MILESTONES))

def _ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
MCIPS = ('<article class="desig reveal"><span class="fee-lab">MCIPS</span><h3>Member of the Chartered Institute of Procurement &amp; Supply</h3><p class="dg-tag">The International Benchmark for Procurement Professionals</p>'
    '<p>MCIPS is a globally recognised professional designation demonstrating advanced procurement expertise, commercial competence and the ability to manage complex supply chain responsibilities.</p>'
    '<h4>What MCIPS Represents</h4><p>MCIPS reflects professional capability across key areas of procurement and supply management, including:</p>' + _ul(["Strategic sourcing and category management", "Commercial contracting and supplier relationships", "Contractual and financial risk management", "Sustainable and ethical procurement", "Advanced negotiation and supply chain governance"]) +
    '<h4>Pathways to MCIPS</h4><p>Professionals can pursue MCIPS through established qualification and assessment routes, including:</p>' + _ul(["<strong>Examination Pathway:</strong> Completion of CIPS Level 4 Diploma, Level 5 Advanced Diploma and Level 6 Professional Diploma, supported by a minimum of three years of relevant professional experience.", "<strong>Accredited Academic Pathway:</strong> Recognition of eligible accredited university qualifications.", "<strong>Management Entry Route (MER):</strong> A structured assessment pathway for experienced senior procurement professionals."]) +
    '<h4>Maintaining Chartered Professional Status</h4><p>Eligible MCIPS members maintaining Chartered Procurement and Supply Professional status are required to complete 30 hours of Continuing Professional Development (CPD) annually and renew the CIPS Ethical Procurement and Supply certification each year.</p></article>')
FCIPS = ('<article class="desig solid reveal" style="--d:.1s"><span class="fee-lab">FCIPS</span><h3>Fellow of the Chartered Institute of Procurement &amp; Supply</h3><p class="dg-tag">Recognising Exceptional Leadership in Procurement</p>'
    '<p>FCIPS represents the highest level of professional recognition within CIPS, acknowledging individuals who have demonstrated outstanding leadership, strategic influence and sustained contributions to the procurement and supply chain profession.</p>'
    '<h4>What FCIPS Represents</h4><p>Fellowship recognises senior professionals who have made a significant impact through:</p>' + _ul(["Executive leadership and strategic decision-making", "Procurement and supply chain transformation", "Contributions to professional standards and industry development", "Mentorship and advancement of future procurement leaders", "Influence on organisational, public-sector and global supply policy"]) +
    '<h4>Eligibility and Professional Standing</h4><p>FCIPS is intended for experienced leaders, including Chief Procurement Officers, Global Supply Chain Directors, senior government procurement professionals and distinguished industry experts.</p><p>Candidates demonstrate sustained professional achievement, leadership impact and contributions to the profession through a formal assessment and peer-review process.</p><p>FCIPS members represent an influential community helping shape the future direction of procurement and global supply chain management.</p></article>')
# Each h4 block becomes a disclosure: open by default, collapsed on phones by site.js
import re as _re
MCIPS, FCIPS = (_re.sub(r'<h4>(.*?)</h4>(.*?)(?=<h4>|</article>)', r'<details class="dg-sec" open><summary>\1</summary><div class="dg-body">\2</div></details>', x) for x in (MCIPS, FCIPS))

STAGES = [("Stage 1", "Foundations &amp; Tactical Procurement", [("Level 2", "Certificate in Procurement and Supply Operations", "An introduction to fundamental procurement activities, including purchasing processes, purchase orders, administrative controls and supplier communication."),
                                                                  ("Level 3", "Advanced Certificate in Procurement and Supply Operations", "Develops tactical procurement capabilities, including cost analysis, commercial agreements, inventory monitoring and supplier management.")]),
          ("Stage 2", "Professional &amp; Strategic Development", [("Level 4", "Diploma in Procurement and Supply", "Builds operational procurement competence through commercial contracting, sourcing methodologies, whole-life costing and negotiation strategies."),
                                                                   ("Level 5", "Advanced Diploma in Procurement and Supply", "Develops management-level expertise in category management, contractual and financial risk, ethical supply practices and team leadership."),
                                                                   ("Level 6", "Professional Diploma in Procurement and Supply", "Focuses on executive-level procurement capabilities, including corporate strategy, enterprise supply chain design, procurement transformation and strategic leadership.")]),
          ("Stage 3", "MCIPS — Professional Recognition", [("MCIPS", "", "Represents the internationally recognised benchmark for qualified procurement professionals. The standard qualification pathway combines the Level 6 Professional Diploma with relevant professional experience, while alternative recognised academic and management-entry routes may also apply.")]),
          ("Stage 4", "FCIPS — Fellowship &amp; Leadership Excellence", [("FCIPS", "", "The highest level of professional recognition, awarded to accomplished procurement and supply chain leaders who demonstrate exceptional strategic impact, mentorship and sustained contributions to the advancement of the profession.")])]
# Interactive stepper: one panel per stage; without JS every panel shows, stacked
STAGE_META = [("Foundation", "Levels 2–3"), ("Professional", "Levels 4–6"), ("MCIPS", "Chartered professional"), ("FCIPS", "Fellowship")]
def _plv(lv, nm, d):
    n = lv.replace("Level ", "")
    return (f'<article class="plv"><span class="plv-n{" wide" if not n.isdigit() else ""}">{n}</span><div>'
            f'<b>{(lv + " — " + nm) if nm else lv}</b><p>{d}</p></div></article>')
_steps = _panels = ""
for i, ((s, t, lvls), (short, rng)) in enumerate(zip(STAGES, STAGE_META)):
    nxt = f'<button type="button" class="path-go" data-go="{i + 1}">Next: {STAGE_META[i + 1][0]} {ARROW}</button>' if i < len(STAGES) - 1 else '<a class="path-go" href="register.html">Register for the Summit ' + ARROW + '</a>'
    prv = f'<button type="button" class="path-go back" data-go="{i - 1}" aria-label="Previous stage">{ARROW}</button>' if i else ""
    _steps += (f'<li><button type="button" role="tab" id="ps-{i}" aria-controls="pp-{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">'
               f'<span class="dot">{i + 1}</span><span class="ps-t"><small>{s}</small><b>{short}</b></span></button></li>')
    _panels += (f'<section class="path-panel" id="pp-{i}" role="tabpanel" aria-labelledby="ps-{i}"{"" if i == 0 else " hidden"}>'
                f'<header><span class="path-k">{s} of {len(STAGES)} · {rng}</span><h3>{t}</h3><div class="path-nav">{prv}{nxt}</div></header>'
                f'<div class="path-lvls">' + "".join(_plv(*l) for l in lvls) + '</div></section>')
pathway = (f'<div class="path reveal" data-path style="--i:0"><div class="path-track"><ol class="path-steps" role="tablist" aria-label="CIPS qualification stages">{_steps}</ol>'
           f'<div class="path-bar" aria-hidden="true"><i></i></div></div>{_panels}</div>')

def _tab_intro(eyebrow, h2, paras):
    return f'<div class="two sec-intro"><div class="reveal"><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2></div><div class="body drop reveal" style="--d:.1s">' + "".join(f"<p>{x}</p>" for x in paras) + '</div></div>'
TABS = [("legacy", "The CIPS Legacy", _tab_intro("The CIPS Legacy", "A Legacy of Advancing the <em>Procurement Profession</em>", ["From its origins in 1932 to its position as a globally recognised professional institution, CIPS has played a defining role in transforming procurement from an administrative function into a strategic driver of business value, organisational resilience and sustainable growth."]) + f'<div class="eyebrow">Key Milestones</div><ol class="tl">{tl}</ol>'),
        ("recognition", "Professional Recognition", _tab_intro("Professional Recognition", "The Global Benchmark for <em>Procurement Excellence</em>", ["CIPS professional designations are internationally recognised credentials that demonstrate expertise, strategic leadership and a commitment to ethical procurement practices.", "Through its professional qualifications and membership framework, CIPS establishes benchmarks for procurement capability at different stages of a professional’s career."]) + f'<div class="fees desigs">{MCIPS}{FCIPS}</div>'),
        ("pathway", "Qualification Pathway", _tab_intro("The CIPS Qualification Pathway", "A Structured Journey from Foundation to <em>Global Leadership</em>", ["CIPS provides a progressive qualification framework designed to develop professional capability from foundational procurement knowledge to advanced strategic leadership."]) + pathway)]
# Three stacked sections (formerly tabs); ids kept for deep links like #recognition
about_secs = "\n".join(f'<section class="sec{" tint" if i != 1 else ""}" id="{k}"><div class="wrap">{b}</div></section>' for i, (k, _t, b) in enumerate(TABS))

about_cips = head(f"About CIPS | {SITE}", "The Chartered Institute of Procurement & Supply (CIPS) is a global professional body dedicated to advancing excellence across procurement and supply.") + header("about-cips.html") + f'''
<main id="main">
<div class="wrap"><section class="phead phead-seal phead-long">
  <div class="fade"><div class="kicker"><span>About CIPS</span></div><h1>Shaping the Global Standards of <em>Procurement &amp; Supply Chain Excellence</em></h1>
  <p class="lede">The Chartered Institute of Procurement &amp; Supply (CIPS) is the world’s largest professional body dedicated to procurement and supply chain management. Operating under a Royal Charter granted in 1992, CIPS represents a global network of over 70,000 members across more than 150 countries.</p></div>
  <aside class="aside fade" style="--d:.15s">{CIPS_ART}</aside>
</section></div>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="eyebrow reveal">Who We Are</div><div class="two who"><p class="who-lead reveal">As the independent custodian of the procurement profession, CIPS sets internationally recognised standards for <em>professional capability, ethical conduct and supply chain governance.</em></p>
<div class="body reveal" style="--d:.1s"><p>Bridging public and private sector interests, CIPS works to strengthen procurement practices, advance professional excellence and build transparent, sustainable and resilient global supply networks.</p></div></div>
<div class="stats stats-3 reveal"><div class="stat"><b><span data-count="150">150</span>+</b><p>Countries</p></div><div class="stat"><b><span data-count="70000">70,000</span>+</b><p>Members</p></div><div class="stat"><b>1992</b><p>Royal Charter since</p></div></div></div></section>

{about_secs}

<section class="statement anchor"><div class="wrap"><div class="eyebrow" style="color:var(--blue-400)">Why CIPS Anchors Summit 2027</div><h2 class="reveal">Connecting Global Expertise. <em>Shaping the Future of Procurement.</em></h2>
<div class="st-grid"><div class="st-copy"><div class="st-body reveal"><p>The CIPS International Procurement &amp; Supply Chain Summit 2027 brings together the global procurement community at a time when organisations are redefining how they source, collaborate, innovate and build resilience.</p><p>As global supply networks respond to geopolitical shifts, AI-driven transformation, supply chain disruptions, sustainability commitments and evolving trade corridors, procurement has emerged as a critical driver of enterprise strategy.</p><p>Anchored by CIPS’s professional expertise and global leadership network, the summit creates a platform for Chief Procurement Officers, MCIPS and FCIPS professionals, industry leaders and senior decision-makers to exchange insights, share practical experiences and explore the next generation of procurement practices.</p><p>Through strategic dialogue and collaboration, the summit aims to advance a shared vision of intelligent, resilient, transparent and ethically governed global supply chains.</p></div>
<a class="btn light reveal" href="about-summit.html">About the Summit {ARROW}</a></div>
<figure class="st-fig reveal" style="--d:.15s">{_anchor_art()}</figure></div>
<div class="st-vision reveal"><span class="st-vlab">A shared vision for global supply chains</span><ul>{"".join(f"<li>{ic(n)}<b>{t}</b></li>" for n, t in VISION)}</ul></div></div></section>

{cta_band()}
</main>
''' + footer()
write("about-cips.html", about_cips)


# ---- USP hub diagram (About the Summit)
import math
def usp_fig():
    import random as _rr
    _rr.seed(21)
    W, Hh, cx, cy = 640, 560, 320, 276
    themes = ["AI &amp; DIGITAL", "RESILIENCE", "STRATEGIC VALUE", "RESPONSIBLE", "FUTURE-READY"]
    plain = ["AI & DIGITAL", "RESILIENCE", "STRATEGIC VALUE", "RESPONSIBLE", "FUTURE-READY"]
    # particle field
    stars = ""
    for i in range(46):
        x, y = _rr.uniform(10, W - 10), _rr.uniform(10, Hh - 10)
        if (x - cx) ** 2 / 1.0 + (y - cy) ** 2 < 70 ** 2: continue
        r = _rr.choice([0.8, 1, 1.3, 1.7]); d = _rr.uniform(0, 4)
        stars += f'<circle class="st" cx="{x:.0f}" cy="{y:.0f}" r="{r}" style="animation-delay:-{d:.1f}s"/>'
    # tilted gyroscope orbits + comets
    def orbit(rot, rx, ry, dur, begin, cls=""):
        path = f"M{cx - rx} {cy}a{rx} {ry} 0 1 0 {2 * rx} 0a{rx} {ry} 0 1 0 {-2 * rx} 0"
        return (f'<g transform="rotate({rot} {cx} {cy})"><path class="orb {cls}" d="{path}" fill="none" stroke="url(#orbg)" stroke-width="1.3"/>'
                f'<g filter="url(#glow)"><circle r="4" fill="#fff"><animateMotion dur="{dur}s" begin="-{begin}s" repeatCount="indefinite" path="{path}"/></circle>'
                f'<circle r="9" fill="#00c2ff" opacity=".35"><animateMotion dur="{dur}s" begin="-{begin}s" repeatCount="indefinite" path="{path}"/></circle></g></g>')
    orbits = orbit(-22, 250, 84, 9, 1) + orbit(22, 250, 84, 11, 6) + orbit(90, 190, 62, 8, 3, "o3")
    beams = nodes = pills = ""
    for i, (lab, pl) in enumerate(zip(themes, plain)):
        ang = math.radians(-90 + 72 * i)
        nx, ny = cx + 176 * math.cos(ang), cy + 148 * math.sin(ang)
        px, py = cx + 236 * math.cos(ang), cy + 232 * math.sin(ang)
        w = len(pl) * 9.4 + 62
        beams += f'<line class="beam" x1="{cx + 56 * math.cos(ang):.1f}" y1="{cy + 56 * math.sin(ang):.1f}" x2="{nx:.1f}" y2="{ny:.1f}" style="animation-delay:-{i * 0.5:.1f}s"/>'
        nodes += (f'<g filter="url(#glow)"><circle cx="{nx:.1f}" cy="{ny:.1f}" r="13" fill="url(#nodeg)"/></g>'
                  f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="5.5" fill="#fff"/>'
                  f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="12" fill="none" stroke="#00c2ff" stroke-width="1.2"><animate attributeName="r" from="12" to="34" dur="3.2s" begin="-{i * 0.6:.1f}s" repeatCount="indefinite"/><animate attributeName="opacity" from=".75" to="0" dur="3.2s" begin="-{i * 0.6:.1f}s" repeatCount="indefinite"/></circle>')
        pills += (f'<g class="pl"><rect x="{px - w / 2:.1f}" y="{py - 20:.1f}" width="{w:.1f}" height="40" rx="20"/>'
                  f'<text class="pn" x="{px - w / 2 + 20:.1f}" y="{py + 4.6:.1f}">0{i + 1}</text>'
                  f'<text x="{px - w / 2 + 44:.1f}" y="{py + 4.8:.1f}">{lab}</text></g>')
    ripples = "".join(f'<circle cx="{cx}" cy="{cy}" r="60" fill="none" stroke="#4d8dff" stroke-width="1.4"><animate attributeName="r" from="60" to="270" dur="6s" begin="-{k * 2}s" repeatCount="indefinite"/><animate attributeName="opacity" from=".55" to="0" dur="6s" begin="-{k * 2}s" repeatCount="indefinite"/></circle>' for k in range(3))
    # core sphere meridians
    mer = "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="54" fill="none" stroke="#fff" stroke-opacity=".22" stroke-width="1"/>' for rx in (18, 36)) + f'<ellipse cx="{cx}" cy="{cy}" rx="54" ry="18" fill="none" stroke="#fff" stroke-opacity=".22"/><ellipse cx="{cx}" cy="{cy}" rx="54" ry="38" fill="none" stroke="#fff" stroke-opacity=".14"/>'
    return f'''<figure class="usp-fig reveal" style="--d:.15s" aria-label="Procurement leadership at the centre of AI, resilience, strategic value, responsible sourcing and future-ready leadership"><svg viewBox="0 0 {W} {Hh}" role="img" aria-hidden="true">
<defs>
<radialGradient id="aura" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#0b5cff" stop-opacity=".55"/><stop offset=".55" stop-color="#0b5cff" stop-opacity=".12"/><stop offset="1" stop-color="#0b5cff" stop-opacity="0"/></radialGradient>
<radialGradient id="coreg" cx="38%" cy="30%" r="80%"><stop offset="0" stop-color="#7fb0ff"/><stop offset=".38" stop-color="#1f6bff"/><stop offset="1" stop-color="#0a2a95"/></radialGradient>
<radialGradient id="nodeg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7fe3ff"/><stop offset="1" stop-color="#0b5cff"/></radialGradient>
<linearGradient id="orbg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00c2ff" stop-opacity=".05"/><stop offset=".5" stop-color="#4d8dff" stop-opacity=".85"/><stop offset="1" stop-color="#00c2ff" stop-opacity=".05"/></linearGradient>
<filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<circle cx="{cx}" cy="{cy}" r="290" fill="url(#aura)"/>
{stars}
<circle cx="{cx}" cy="{cy}" r="262" fill="none" stroke="#4d8dff" stroke-opacity=".28" stroke-width="1" stroke-dasharray="2 9"/>
{ripples}
{orbits}
{beams}
<g filter="url(#glow)"><circle cx="{cx}" cy="{cy}" r="60" fill="#0b5cff" opacity=".55"/></g>
<circle cx="{cx}" cy="{cy}" r="54" fill="url(#coreg)"/>
{mer}
<ellipse cx="{cx - 16}" cy="{cy - 26}" rx="24" ry="11" fill="#fff" opacity=".22" transform="rotate(-24 {cx - 16} {cy - 26})"/>
<text class="hub" x="{cx}" y="{cy + 2}" text-anchor="middle">PROCUREMENT</text><text class="hub" x="{cx}" y="{cy + 17}" text-anchor="middle">LEADERSHIP</text>
{nodes}{pills}
</svg></figure>'''
USPFIG = usp_fig()


# ---- About the Summit: luxurious vertical delegate pass
def _pass():
    import random as _r
    _r.seed(9)
    rings = "".join(f'<circle cx="250" cy="330" r="{r}"/>' for r in range(30, 300, 14))
    arcs = ('<path d="M26 452C96 414 206 412 314 436"/><path d="M26 458C116 430 224 438 314 424" stroke-opacity=".5"/>'
            '<circle cx="26" cy="452" r="3.4" fill="#00c2ff" stroke="none"/><circle cx="314" cy="436" r="3.4" fill="#00c2ff" stroke="none"/>')
    bars = ""; x = 0
    for w in [2,1,3,1,2,1,1,3,1,2,1,3,1,1,2,3,1,2,1,1,3,2,1,3,1,2,1,1,2,3,1,2,1,3,1,1,2]:
        bars += f'<rect x="{x}" y="0" width="{w}" height="46"/>'; x += w + 2.4
    art = f'''<svg class="pass-art" viewBox="0 0 340 560" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g fill="none" stroke="#fff" stroke-opacity=".09" stroke-width="1">{rings}</g><g fill="none" stroke="#00c2ff" stroke-opacity=".8" stroke-width="1.3" stroke-dasharray="3 6">{arcs}</g></svg>'''
    return f'''<figure class="pass-wrap reveal" aria-label="Delegate pass: {SITE}, 07 January 2027, ITC Maratha, Mumbai, India">
<div class="pass-sway">
  <div class="lanyard" aria-hidden="true"><span class="strap"><i>CIPS &#183; SUMMIT 2027 &#183; CIPS &#183; SUMMIT 2027</i></span><span class="clip"></span></div>
  <div class="pass">
    {art}
    <span class="slot" aria-hidden="true"></span>
    <div class="pass-in">
      <div class="pass-top"><img src="assets/img/cips-logo-light.png" {ALT} width="72" height="48"><span class="pass-no">No. 2027 &#183; IN</span></div>
      <div class="pass-kick">Delegate Pass</div>
      <div class="pass-yr" aria-hidden="true">2027</div>
      <p class="pass-name"><span>CIPS International</span>Procurement &amp; Supply Chain Summit</p>
      <div class="pass-facts"><div><small>Date</small><b>07 Jan 2027</b></div><div><small>Venue</small><b>ITC Maratha</b></div></div>
      <p class="pass-aud">Senior Procurement &amp; Supply Chain Leaders</p>
      <div class="pass-perf" aria-hidden="true"></div>
      <div class="pass-stub"><svg class="pass-bars" viewBox="0 0 {x:.0f} 46" preserveAspectRatio="none" aria-hidden="true"><g fill="#fff">{bars}</g></svg><span>CIPS &#183; SUMMIT &#183; 2027 &#183; IN</span></div>
    </div>
  </div>
</div></figure>'''
PASS = _pass()
import re as _re_p
_PASS_ART = _re_p.search(r'<svg class="pass-art".*?</svg>', PASS, _re_p.S).group(0)
_LANYARD = _re_p.search(r'<div class="lanyard".*?</span></div>', PASS, _re_p.S).group(0)
# Filled in by site.js after a registration: holder name, role, organisation, reference and a barcode strip drawn from the reference
# Pay with Razorpay Checkout for one reference (filled in by site.js: the amount comes from the Google Sheet script)
PAYBOX = f'''<div class="paybox" data-paybox>
              <button type="button" class="btn pay-now" data-pay-now><span data-pay-label>Pay securely</span>{ARROW}</button>
              <p class="paybox-sub">Card, UPI, netbanking or wallet &middot; secured by Razorpay</p>
              <p class="paybox-msg" data-pay-msg role="status" aria-live="polite" hidden></p>
            </div>'''
CONF_TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def RECEIPT(item_kind):
    """The payment receipt shown on both confirmation pages (and printed on its own by 'Save or print receipt')."""
    return f'''<article class="rcpt" data-receipt aria-labelledby="rcpt-h-{item_kind}">
          <header class="rcpt-head">
            <img class="rcpt-logo" src="assets/img/cips-logo-dark.png" {ALT} width="96" height="36">
            <span class="rcpt-stamp">{CONF_TICK}Paid</span>
          </header>
          <div class="rcpt-title"><h3 id="rcpt-h-{item_kind}">Payment receipt</h3><p>Receipt no. <b class="mono" data-ref></b></p></div>
          <dl class="rcpt-meta">
            <div><dt>Billed to</dt><dd><b data-rc="name"></b><span data-rc="org"></span><span data-rc="email"></span></dd></div>
            <div><dt>Paid on</dt><dd data-conf="when"></dd></div>
          </dl>
          <table class="rcpt-lines">
            <thead><tr><th scope="col">Description</th><th scope="col">Amount</th></tr></thead>
            <tbody>
              <tr><td><b data-rc="item"></b><span data-rc="itemSub"></span></td><td data-rc="base"></td></tr>
              <tr class="rcpt-tax"><td>GST at 18%</td><td data-rc="gst"></td></tr>
            </tbody>
            <tfoot><tr><th scope="row">Total paid</th><td data-rc="total"></td></tr></tfoot>
          </table>
          <p class="rcpt-words" data-rc="words"></p>
          <dl class="rcpt-pay">
            <div data-conf-row="pid"><dt>Razorpay payment ID</dt><dd class="mono" data-conf="pid"></dd></div>
            <div><dt>Paid by</dt><dd>Online payment through Razorpay</dd></div>
          </dl>
          <p class="rcpt-note">Computer-generated receipt, no signature required. A PDF copy is attached to your confirmation email.</p>
          <button type="button" class="btn ghost rcpt-btn" data-print-receipt><span>Save or print receipt</span>{ic("arrow")}</button>
        </article>'''
MY_PASS = f'''<figure class="pass-wrap my-pass" aria-label="Your delegate pass">
<div class="pass-sway">
  {_LANYARD}
  <div class="pass">
    {_PASS_ART}
    <span class="slot" aria-hidden="true"></span>
    <div class="pass-in">
      <div class="pass-top"><img src="assets/img/cips-logo-light.png" {ALT} width="72" height="48"><span class="pass-no" data-pass="ref"></span></div>
      <div class="pass-kick">Delegate Pass</div>
      <div class="pass-holder"><b data-pass="name"></b><span data-pass="role"></span><span class="org" data-pass="org"></span></div>
      <p class="pass-name pass-ev"><span>CIPS International</span>Procurement &amp; Supply Chain Summit 2027</p>
      <div class="pass-facts"><div><small>Date</small><b>07 Jan 2027</b></div><div><small>Venue</small><b>ITC Maratha</b></div></div>
      <p class="pass-aud">Confirmed &#183; Paid</p>
      <div class="pass-perf" aria-hidden="true"></div>
      <div class="pass-stub"><svg class="pass-bars" data-pass="bars" viewBox="0 0 100 46" preserveAspectRatio="none" aria-hidden="true"><g fill="#fff"></g></svg><span data-pass="ref2"></span></div>
    </div>
  </div>
</div></figure>'''


# ---- About the Summit: "Who will be in the room" floor plan
def _room():
    tables = [(95, 148), (230, 148), (365, 148), (162, 232), (298, 232), (95, 316), (230, 316), (365, 316)]
    hi = {(230, 148): [0, 3], (162, 232): [1, 4], (298, 232): [2], (365, 316): [5, 1], (95, 148): [3]}
    seats = tabs = ""
    for (tx, ty) in tables:
        tabs += f'<circle cx="{tx}" cy="{ty}" r="19" fill="#fff" fill-opacity=".14" stroke="#fff" stroke-opacity=".7" stroke-width="1.4"/>'
        for k in range(6):
            a = _m.radians(-90 + 60 * k)
            sx, sy = tx + 30 * _m.cos(a), ty + 30 * _m.sin(a)
            on = k in hi.get((tx, ty), [])
            seats += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{5.4 if on else 4.6}" fill="{"#00c2ff" if on else "#fff"}" fill-opacity="{1 if on else .85}"/>'
    links = ""
    pairs = [((230,148),(162,232)), ((230,148),(298,232)), ((162,232),(95,316)), ((298,232),(365,316)), ((162,232),(230,316)), ((95,148),(162,232)), ((365,148),(298,232))]
    for i, ((x1, y1), (x2, y2)) in enumerate(pairs):
        d = f"M{x1} {y1}L{x2} {y2}"
        links += f'<path class="rl" d="{d}"/><circle r="3" fill="#7fe3ff"><animateMotion dur="{3 + (i % 3) * .8:.1f}s" begin="-{i * .7:.1f}s" repeatCount="indefinite" path="{d}"/></circle>'
    return f'''<figure class="room reveal" style="--d:.1s" aria-label="Floor plan of the summit room: a keynote stage and round tables of senior delegates"><svg viewBox="0 0 460 412" role="img" aria-hidden="true">
<defs><linearGradient id="roomg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a6bff"/><stop offset="1" stop-color="#0a3fbd"/></linearGradient>
<pattern id="roomgrid" width="23" height="23" patternUnits="userSpaceOnUse"><path d="M23 0H0V23" fill="none" stroke="#fff" stroke-opacity=".07"/></pattern></defs>
<rect width="460" height="412" rx="20" fill="url(#roomg)"/><rect width="460" height="412" rx="20" fill="url(#roomgrid)"/>
<rect x="6" y="6" width="448" height="400" rx="15" fill="none" stroke="#fff" stroke-opacity=".28"/>
<path d="M120 26h220a16 16 0 0 1 16 16v14H104V42a16 16 0 0 1 16-16Z" fill="#fff" fill-opacity=".16" stroke="#00c2ff" stroke-width="1.4"/>
<text class="rt" x="230" y="46" text-anchor="middle">KEYNOTE STAGE</text>
<path d="M230 62v22" stroke="#00c2ff" stroke-width="1.4" stroke-dasharray="3 4"/>
<text class="rt2" x="230" y="98" text-anchor="middle">FIRESIDE &#183; PANELS &#183; ROUNDTABLES</text>
{links}{tabs}{seats}
<line x1="24" y1="360" x2="436" y2="360" stroke="#fff" stroke-opacity=".3" stroke-dasharray="3 6"/><g><rect x="86" y="368" width="288" height="28" rx="14" fill="#fff"/><text class="rn" x="230" y="386" text-anchor="middle">150&#8211;200 SENIOR DECISION-MAKERS</text></g>
</svg></figure>'''
ROOM_ART = _room()

# =========================================================== ABOUT THE SUMMIT
expect = [("mic", "Leadership Keynotes", "Big-picture thinking from senior industry voices."),
          ("users", "Executive Panels", "Multiple perspectives on the profession’s most critical priorities."),
          ("chat", "Fireside Conversations", "Focused, insight-led discussions with senior leaders."),
          ("table", "Executive Roundtables", "Smaller peer-level conversations around shared challenges."),
          ("net", "Networking &amp; Collaboration", "Meaningful connections across industries, regions and functions.")]
ex = "".join(f'<article class="ex reveal" style="--d:{i*0.07:.2f}s"><i>{ic(icn)}</i><h3>{t}</h3><p>{d}</p></article>' for i, (icn, t, d) in enumerate(expect))
aud = ["Chief Procurement Officers", "Procurement Directors", "Heads of Procurement", "Supply Chain Leaders", "Strategic Sourcing Leaders", "Category Leaders", "Digital &amp; Transformation Heads", "Sustainability &amp; Responsible Sourcing Leaders", "Senior Business Decision-Makers"]
aud_html = "".join(f'<li class="reveal">{a}</li>' for a in aud)
themes = [("cpu", "AI &amp; Digital Transformation", "How technology is reshaping procurement strategy and decision-making."),
          ("shield", "Resilience &amp; Agility", "Building stronger and more adaptive supply networks."),
          ("trend", "Strategic Value", "Moving procurement from cost management to enterprise impact."),
          ("leaf", "Responsible Procurement", "Embedding sustainability, ethics and accountability into sourcing decisions."),
          ("compass", "Future-Ready Leadership", "Building the talent, capabilities and partnerships required for what comes next.")]
thm = "".join(f'<article class="thm reveal"><span class="n">0{i+1}</span><i>{ic(icn)}</i><div><h3>{t}</h3><p>{d}</p></div></article>' for i, (icn, t, d) in enumerate(themes))
CLOSER = "".join(f'<li class="pc"><div class="pcard"><div class="pc-top"><span>Side B &#183; 0{i+1} / 04</span><span>{lab}</span></div><div class="pc-body"><i>{ic(icn)}</i><span class="pc-h">{txt}</span><b class="pc-n" aria-hidden="true">0{i+1}</b></div><div class="pc-perf" aria-hidden="true"></div><div class="pc-stub" aria-hidden="true"><span class="pc-bars"></span><span class="pc-code">CIPS &#183; 2027 &#183; IN</span></div></div></li>' for i, (icn, txt, lab) in enumerate([("cal", "One Day.", "One Day"), ("users", "Senior Perspectives.", "Senior Perspectives"), ("globe", "Global Conversations.", "Global Conversations"), ("award", "Lasting Impact.", "Lasting Impact")]))
DOTS = "".join(f'<button type="button" aria-label="Show card {i+1}"{" aria-current=%strue%s" % (chr(34),chr(34)) if i==0 else ""}></button>' for i in range(4))
about_summit = head(f"About the Summit | {SITE}", "A senior, international procurement leadership platform bringing together CIPS leadership, top CPOs and supply chain decision-makers to discuss the issues shaping the future of the profession. January 2027, India.") + header("about-summit.html") + f'''
<main id="main">
<div class="wrap"><section class="phead phead-pass">
  <div class="fade">{EVENT_NAME}<div class="kicker"><span>About the Summit</span></div><h1>Where Global Procurement Leadership <em>Comes Together</em></h1>
  <p class="lede">The CIPS International Procurement &amp; Supply Chain Summit 2027 is a one-day leadership platform created for senior professionals navigating a rapidly changing global business environment.</p></div>
  <aside class="aside fade" style="--d:.15s">{PASS}</aside>
</section></div>

<section class="sec"><div class="wrap two"><div class="reveal"><div class="eyebrow">The Forum</div><h2>Not simply a conference — <em>a curated forum</em></h2></div>
<div class="body drop reveal" style="--d:.1s"><p>The summit will bring together CPOs, procurement directors, supply chain leaders, transformation heads and senior business decision-makers to explore the strategies, technologies and leadership priorities redefining the profession.</p><p><strong>This is not simply a conference — it is a curated forum for senior-level conversation, knowledge exchange and peer connection.</strong></p></div></div></section>

<section class="usp"><div class="wrap usp-grid"><div class="usp-t"><div class="eyebrow">The Summit’s Promise</div><h2 class="reveal">Where global procurement leadership meets to <em>shape what comes next.</em></h2>
<p class="reveal" style="--d:.1s">A senior, international procurement leadership platform that brings together CIPS leadership, top CPOs and supply chain decision-makers to discuss the issues shaping the future of the profession — from AI and resilience to strategic value, responsible sourcing and future-ready leadership.</p></div>{USPFIG}</div></section>

<section class="sec tint"><div class="wrap"><div class="eyebrow">The Programme</div><h2 style="margin-bottom:56px" class="reveal">What to <em>Expect</em></h2><div class="expect">{ex}</div></div></section>

<section class="sec"><div class="wrap two"><div class="aud-l"><div class="reveal"><div class="eyebrow">The Audience</div><h2>Who Will Be <em>in the Room</em></h2></div>{ROOM_ART}</div><ul class="aud">{aud_html}</ul></div></section>

<section class="sec tint" id="themes" style="scroll-margin-top:80px"><div class="wrap"><div class="eyebrow">Five Themes</div><h2 style="margin-bottom:56px" class="reveal">The Five <em>Summit Themes</em></h2>{thm}</div></section>

<section class="closer"><div class="wrap"><p class="deck-cap">The other side of the pass</p><ul class="deck" id="deck" aria-label="Summit highlights">{CLOSER}</ul><div class="deck-dots" role="group" aria-label="Choose a card">{DOTS}</div></div></section>

{cta_band(h="Join the <em>Conversation</em>")}
</main>
''' + footer()
write("about-summit.html", about_summit)

# =========================================================== SPEAKERS
speakers = head(f"Speakers | {SITE}", "Confirmed CIPS leadership speaking at the CIPS International Procurement & Supply Chain Summit 2027: Ram Trivedi, Ben Farrell MBE and Sam Achampong. January 2027, India.") + header("speakers.html") + f'''
<main id="main">
<div class="wrap"><section class="phead phead-seal">
  <div class="fade"><div class="kicker"><span>Speakers</span></div><h1>Voices Shaping the Future of <em>Procurement</em></h1>
  <p class="lede">Uniting Top Voices from India and the Global Procurement Leadership Community. A distinguished line-up of procurement and supply chain leaders will come together to share experience, challenge thinking and contribute to the conversations defining the future of the profession.</p></div>
  <aside class="aside fade" style="--d:.15s">{SPEAKERS_ART}<dl class="facts"><div><dt>Date</dt><dd>07 January 2027</dd></div><div><dt>Venue</dt><dd>ITC Maratha, Mumbai, India</dd></div></dl></aside>
</section></div>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="eyebrow">Confirmed</div><h2 style="margin-bottom:56px" class="reveal">Confirmed <em>Speakers</em></h2><div class="spk">{spk_cards(first_row=True)}</div>{SPK_MORE}</div></section>

{cta_band(h="Join the <em>Conversation</em>", btn="Register to Join the Conversation")}
</main>
''' + footer()
write("speakers.html", speakers)


# =========================================================== REGISTER
def field(name, label, typ="text", req=True, auto="", extra=""):
    star = "<i aria-hidden='true'>*</i>" if req else ""
    return f'''<div class="field"><label for="{name}">{label}{star}</label><input id="{name}" name="{name}" type="{typ}"{" required" if req else ""}{f' autocomplete="{auto}"' if auto else ""} {extra}><span class="err" role="alert"></span></div>'''


wiifm_reg = "".join(f"<li><i>0{i+1}</i><span>{w}</span></li>" for i, w in enumerate(WIIFM))

register = head(f"Register Now | {SITE}", "Register your interest to attend the CIPS International Procurement & Supply Chain Summit 2027 — 07 January 2027, ITC Maratha, Mumbai, India.") + header("register.html") + f'''
<main id="main">
<div class="wrap"><section class="phead reg-head">
  <div class="fade"><div class="kicker"><span>Register Now</span></div><h1>Join the Leaders Shaping <em>What Comes Next</em></h1>
  <p class="lede">Register your interest to attend the CIPS International Procurement &amp; Supply Chain Summit 2027 and become part of a senior international community of procurement and supply chain professionals.</p>
  <p class="pay-link">Already registered? <a href="pay.html">Complete your payment {ARROW}</a></p></div>
  <aside class="aside fade" style="--d:.15s">{REGISTER_ART}</aside>
</section></div>

<div class="wrap reg">
  <aside class="details reveal" aria-label="Event details"><h2>Event <em>Details</em></h2>
    <dl><div><dt>Event</dt><dd>{SITE}</dd></div><div><dt>Date</dt><dd>07 January 2027</dd></div><div><dt>Venue</dt><dd>ITC Maratha, Mumbai, India</dd></div><div><dt>Registration Fee</dt><dd>&#8377;10,000 per delegate <small>+ GST</small></dd></div><div><dt>Audience</dt><dd>Senior Procurement &amp; Supply Chain Leaders</dd></div></dl></aside>

  <aside class="why-reg reveal" style="--d:.06s" aria-label="Why attend"><div class="eyebrow">What’s In It for You</div>
    <h2>Why <em>attend</em></h2>
    <p class="wr-lead">Gain the insights, connections and perspectives you need to lead procurement with greater intelligence, resilience and value.</p>
    <ol>{wiifm_reg}</ol></aside>

  <div class="form-card reveal" style="--d:.1s">
    <h2 class="form-intro">Registration <em>Form</em></h2>
    <p class="note form-intro">Fields marked * are required.</p>
    <form id="register-form" novalidate>
      <fieldset class="fs"><legend><span>01</span>Personal Information</legend>
        <div class="grid-2">
          {field("firstName", "First Name", auto="given-name")}
          {field("lastName", "Last Name", auto="family-name")}
          {field("email", "Official Email Address", "email", auto="email")}
          {field("mobile", "Mobile Number", "tel", auto="tel", extra='inputmode="tel" placeholder="+91 …"')}
          <div class="field"><label for="country">Country<i aria-hidden="true">*</i></label><select id="country" name="country" required autocomplete="country-name"><option value="">Select your country</option></select><span class="err" role="alert"></span></div>
          {field("city", "City", req=False, auto="address-level2")}
        </div>
      </fieldset>
      <fieldset class="fs"><legend><span>02</span>Professional Information</legend>
        <div class="grid-2">
          {field("organisation", "Organisation / Company", auto="organization")}
          {field("designation", "Designation", auto="organization-title")}
        </div>
      </fieldset>
      <fieldset class="fs"><legend><span>03</span>Participation Interest</legend>
        <label class="check"><input type="checkbox" name="attending" checked><span class="box">{ic("check")}</span><span><strong>Attending the Summit</strong></span></label>
      </fieldset>
      <fieldset class="fs"><legend><span>04</span>Consent</legend>
        <label class="check"><input type="checkbox" name="consent"><span class="box">{ic("check")}</span><span class="t">I agree to receive event-related communication and updates regarding the {SITE}.</span></label>
      </fieldset>
      <p class="form-legal">By submitting this form you agree to the <a href="terms.html">Terms of Use</a> and acknowledge the <a href="privacy.html">Privacy Policy</a>. See the <a href="cancellation.html">Cancellation Policy</a> if you need to withdraw.</p>
      <div class="hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
      <p class="form-alert" role="alert"></p>
      <div class="form-actions">
        <small><i>*</i> Required information</small>
        <button class="btn" type="submit"><span>Submit Registration</span>{ARROW}</button>
      </div>
    </form>

    <div class="success reg-done" id="register-success" role="status">
      <ol class="flow-steps" aria-label="Registration progress">
        <li class="done"><span>{ic("check")}</span>Your details</li>
        <li class="cur" data-flow="pay"><span>2</span>Payment</li>
        <li data-flow="done"><span>3</span>Confirmed</li>
      </ol>

      <section class="reg-paystep" data-reg-step="pay">
        <h2>Complete Your <em>Payment</em></h2>
        <p>Your details are saved under reference <b class="ref-inline" data-ref></b> <button type="button" class="nm-copy" data-copy>Copy</button><br>We&rsquo;ve emailed it to <b data-pass="email"></b>.</p>
        <div class="order">
          <div class="order-item"><small>Delegate Pass</small><b>{SITE}</b><span>07 January 2027 &middot; ITC Maratha, Mumbai</span></div>
          <dl class="order-who"><div><dt>Delegate</dt><dd data-sum-name></dd></div><div><dt>Organisation</dt><dd data-sum-org></dd></div></dl>
          <dl class="order-lines"><div><dt>Registration fee</dt><dd>&#8377;10,000</dd></div><div><dt>GST (18%)</dt><dd>&#8377;1,800</dd></div><div class="tot"><dt>Total</dt><dd>&#8377;11,800</dd></div></dl>
          {PAYBOX}
        </div>
        <p class="reg-note pay-later">Not ready to pay now? Use the link in your email, or <a data-pay-later href="pay.html">pay later with your reference</a>.</p>
      </section>

      <section class="reg-confirm" data-reg-step="done" tabindex="-1" hidden>
        <div class="conf-stage">
          <div class="conf-copy">
            <p class="conf-kicker"><span class="conf-badge">{CONF_TICK}</span>Payment confirmed</p>
            <h2>You&rsquo;re registered, <span data-conf="first"></span>.</h2>
            <p class="conf-sub">We&rsquo;ll see you on Thursday, 07 January 2027 at ITC Maratha, Mumbai. Your pass and receipt are on their way to <b data-pass="email"></b>.</p>
            <div class="conf-ref"><span>Booking reference</span><b class="mono" data-ref></b><button type="button" class="conf-copy-btn" data-copy>Copy</button></div>
            <div class="conf-acts">
              <button type="button" class="btn conf-btn" data-print-pass><span>Save or print pass</span>{ic("arrow")}</button>
              <button type="button" class="btn conf-btn ghost" data-ics><span>Add to calendar</span>{ic("cal")}</button>
              <a class="btn conf-btn ghost" href="https://www.google.com/maps/search/?api=1&amp;query=ITC+Maratha+Mumbai" target="_blank" rel="noopener"><span>Get directions</span>{ARROW}</a>
            </div>
          </div>
          <div class="conf-show">{MY_PASS}</div>
        </div>
        <div class="conf-body">
          {RECEIPT("reg")}
          <div class="conf-side">
            <section class="conf-card" aria-labelledby="conf-who-reg">
              <h3 id="conf-who-reg">Your booking</h3>
              <dl class="conf-dl">
                <div><dt>Delegate</dt><dd data-sum-name></dd></div>
                <div><dt>Organisation</dt><dd data-sum-org></dd></div>
                <div><dt>Email</dt><dd data-pass="email"></dd></div>
                <div><dt>Event</dt><dd>Thursday, 07 January 2027<br>ITC Maratha, Mumbai</dd></div>
              </dl>
            </section>
            <section class="conf-next" aria-labelledby="conf-next-reg">
              <h3 id="conf-next-reg">What happens next</h3>
              <ol>
                <li class="ok"><b>Pass and receipt emailed</b><span>Sent to <b data-pass="email"></b>. Not there in a few minutes? Check your spam or promotions folder.</span></li>
                <li><b>Save the date</b><span>Add the summit to your calendar so the day is blocked.</span></li>
                <li><b>On the day</b><span>Show your pass, on your phone or printed, with a photo ID at the registration desk.</span></li>
              </ol>
            </section>
          </div>
        </div>
        <p class="conf-help">Questions about your booking? Reply to your confirmation email and our team will help. <a href="index.html">Back to the home page</a></p>
      </section>
    </div>
  </div>
</div>
</main>
''' + footer()
write("register.html", register)

# ---- Complete your payment: pay later (or retry) with the reference from a registration or nomination
pay_page = head("Complete Your Payment | CIPS Summit 2027", "Pay your delegate registration or CIPS India Awards nomination fee using the reference from your confirmation.") + header("pay.html") + f'''
<main id="main">
<div class="wrap"><section class="phead pay-head">
  <div class="fade"><div class="kicker"><span>Payments</span></div><h1>Complete Your <em>Payment</em></h1>
  <p class="lede">Closed the page before paying, or your payment didn&rsquo;t go through? Enter the reference from your registration or nomination to pay the fee.</p></div>
</section></div>

<div class="wrap pay-wrap">
  <div class="form-card pay-card reveal">
    <form id="pay-form" novalidate>
      <h2>Find Your <em>Booking</em></h2>
      <p class="note">Your reference is on the thank-you screen and in the confirmation email we sent you.</p>
      <div class="field"><label for="pay-ref">Your reference<i aria-hidden="true">*</i></label>
        <input id="pay-ref" name="ref" type="text" placeholder="e.g. CIPS27-DEL-AB12C" autocomplete="off" autocapitalize="characters" spellcheck="false" required>
        <span class="err" role="alert"></span></div>
      <button class="btn" type="submit"><span>Find My Booking</span>{ARROW}</button>
    </form>
    <div class="pay-out" role="status" tabindex="-1" hidden>
      <div class="nm-ref"><span data-po="kind"></span><b data-po="ref"></b></div>
      <p class="pay-msg" data-po="msg"></p>
      <div class="nm-pay" data-po="paybox">{PAYBOX}</div>
      <p class="reg-note" data-po="note"></p>
      <button type="button" class="btn ghost" data-po="again"><span>Use a different reference</span></button>
    </div>
  </div>
  <aside class="details pay-how reveal" style="--d:.08s" aria-label="How it works"><h2>How It <em>Works</em></h2>
    <ol>
      <li><b>Enter your reference</b><span>It looks like CIPS27-DEL-AB12C (delegates) or CIPS27-IND01-AB12C (award nominations).</span></li>
      <li><b>Pay securely with Razorpay</b><span>Card, UPI, netbanking or wallet. Your payment is linked to your reference automatically.</span></li>
      <li><b>Check your inbox</b><span>Delegates receive their pass by email, and nominators a payment confirmation, usually within 10 minutes.</span></li>
    </ol></aside>
</div>
</main>
''' + footer()
write("pay.html", pay_page)
print("site pages written")


# =========================================================== LEGAL PAGES
# ===== DEMO VALUES — replace with real details before launch (see README "Placeholders") =====
CONTACT_EMAIL = "cipsat2027@gmail.com"   # the event mailbox (also sends the pass and confirmation emails)
RETENTION = "12 months after the Summit"  # DEMO
GOVERNING = "India"                       # DEMO
COURTS = "New Delhi"                      # DEMO
FEE_TEXT = "The registration fee of <strong>&#8377;10,000 per delegate (plus GST)</strong>"  # CONFIRMED amount; refund schedule below is still DEMO
REFUNDS = [("30 days or more before the Summit", "Full refund", "Free of charge"),
           ("15 to 29 days before the Summit", "50% refund", "Free of charge"),
           ("Fewer than 15 days before the Summit", "No refund", "Up to 7 days before, at our discretion"),
           ("No-show", "No refund", "Not available")]  # DEMO
# ==========================================================================================
UPDATED = "22 September 2026"
if CONTACT_EMAIL:
    CONTACT = f'by email at <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>'
else:
    CONTACT = "by replying to any email you receive from the Summit organising team"

def legal_page(fname, title, kicker, lede, sections, desc):
    toc = "".join(f'<li><a href="#s{i+1}">{h}</a></li>' for i, (h, _) in enumerate(sections))
    body = "".join(f'<section id="s{i+1}"><h2><span>{i+1:02d}</span>{h}</h2>{b}</section>' for i, (h, b) in enumerate(sections))
    html = head(f"{title} | {SITE}", desc) + header(fname) + f'''
<main id="main">
<div class="wrap"><section class="legal-hero fade">{EVENT_NAME}<div class="kicker"><span>{kicker}</span></div><h1>{title}</h1><p class="lede">{lede}</p><p class="updated">Last updated: {UPDATED}</p></section></div>
<div class="wrap legal-wrap">
  <aside class="toc" aria-label="On this page"><p>On this page</p><ol>{toc}</ol><div class="toc-links"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="cancellation.html">Cancellation Policy</a></div></aside>
  <div class="prose">{body}<p class="draftnote">Questions about this page? Contact the Summit organising team {CONTACT}.</p></div>
</div>
</main>
''' + footer()
    html = html.replace('<main id="main">', '<!-- DEMO VALUES: contact email, retention period, governing law and refund schedule on this page are placeholders. Replace before launch. -->\n<main id="main">', 1)
    write(fname, html)

legal_page("privacy.html", "Privacy Policy", "Legal", "How we collect, use and protect the personal information you give us when you register your interest in the CIPS International Procurement &amp; Supply Chain Summit 2027.", [
 ("Who we are", f"<p>This website is operated for the {SITE} (the “Summit”) by the Summit organising team (“we”, “us”). This policy explains what personal information we collect through <strong>www.cips2027.online</strong>, why we collect it, and the choices you have.</p>"),
 ("Information we collect", "<p>When you complete the registration form we collect:</p><ul><li><strong>Personal information:</strong> first name, last name, official email address, mobile number, country and (optionally) city.</li><li><strong>Professional information:</strong> organisation or company and designation.</li><li><strong>Your choices:</strong> that you wish to attend the Summit, and whether you agreed to receive event-related communication.</li><li><strong>Submission details:</strong> the date and time of your submission.</li></ul><p>We do not ask for payment card details, government identity numbers or any sensitive personal data through this website.</p>"),
 ("How we use your information", "<ul><li>To receive, review and manage your registration and to contact you about your participation.</li><li>To plan and run the Summit, including attendee communication, access and logistics.</li><li>To send you event-related updates about the Summit, <strong>only if you ticked the consent box</strong>. You can withdraw this at any time.</li><li>To keep the Summit secure, prevent misuse of the form and meet legal obligations.</li></ul><p>We do not sell your personal information.</p>"),
 ("Legal basis and consent", "<p>We process your registration details to take the steps you request when you register, and, where you have ticked the consent box, on the basis of your consent to receive event communication. Where applicable law requires a specific basis (for example the EU/UK GDPR or India’s Digital Personal Data Protection Act, 2023), we rely on the basis that applies to your circumstances.</p>"),
 ("Who we share it with", "<p>Your information is stored in a Google Sheets spreadsheet, so Google acts as a service provider that hosts it on our behalf. Access is limited to the Summit organising team and authorised people supporting the Summit, such as CIPS colleagues and event service providers, and only to the extent needed to run the event. We may also disclose information where the law requires it.</p>"),
 ("Cookies and analytics", "<p>This website does not set cookies and does not use advertising or analytics trackers. It uses the system typeface already installed on your device, so no font files are requested from any third party. Registration data is sent only when you submit the form.</p>"),
 ("International transfers", "<p>The Summit brings together delegates from India and other countries, and our service providers may process data on servers outside your country. Where we transfer information across borders, we take steps to make sure it stays protected in line with applicable law.</p>"),
 ("How long we keep it", "<p>We keep registration information for up to <strong>" + RETENTION + "</strong>, which allows us to run the Summit, follow up with you as you have agreed, and meet legal or reporting requirements. After that we delete or anonymise it. If you withdraw or ask us to delete your details sooner, we will do so unless the law requires us to keep them.</p>"),
 ("Security", "<p>We use reasonable technical and organisational measures to protect your information, including access limited to authorised people and encrypted connections (HTTPS). No online service can be guaranteed to be completely secure.</p>"),
 ("Your rights", "<p>Subject to applicable law, you can ask us to: give you a copy of your information; correct it; delete it; restrict or object to how we use it; and withdraw your consent to event communication at any time. You can also unsubscribe from any update we send. To exercise a right, contact us as set out at the end of this page. You may also complain to your local data protection authority.</p>"),
 ("Children", "<p>The Summit and this website are intended for senior professionals. We do not knowingly collect information from anyone under 18.</p>"),
 ("Changes to this policy", "<p>We may update this policy as the Summit develops. The “Last updated” date at the top shows when it last changed. Significant changes will be highlighted on this page.</p>"),
], "How the CIPS International Procurement & Supply Chain Summit 2027 collects, uses and protects your personal information.")

legal_page("terms.html", "Terms of Use", "Legal", "The terms that apply when you use this website and register your interest in the CIPS International Procurement &amp; Supply Chain Summit 2027.", [
 ("Acceptance", "<p>By using this website or submitting the registration form you agree to these Terms of Use and acknowledge our <a href=\"privacy.html\">Privacy Policy</a>. If you do not agree, please do not use the website.</p>"),
 ("About the Summit and this website", "<p>The Summit is a one-day international procurement and supply chain leadership event planned for <strong>07 January 2027 at ITC Maratha, Mumbai, India</strong>. This website provides information about the Summit and lets you register your interest to attend. Information on the site, including the date, location, programme, themes and speakers, is provided in good faith and may change as planning progresses.</p>"),
 ("Registration", "<ul><li>Submitting the form registers your <strong>interest</strong> to attend. It is not a guarantee of a place.</li><li>Our team will review your details and share further information regarding your participation. A place is confirmed only when we tell you so.</li><li>The Summit is designed for senior procurement and supply chain professionals. We may decline or withdraw a registration, for example where the audience or capacity requirements are not met.</li><li>You agree that the information you give is accurate and that you will keep it up to date. Please use your official work email address.</li></ul>"),
 ("Changes to the event", "<p>We may change the date, venue, format, programme or speakers, or cancel or reschedule the Summit, where we reasonably need to. If a change materially affects you, we will contact you using the details you provided. See the <a href=\"cancellation.html\">Cancellation Policy</a> for your options.</p>"),
 ("Acceptable use", "<p>You agree not to misuse this website, including by submitting false or misleading information, using automated tools to submit the form, attempting to gain unauthorised access, interfering with its operation, or copying content for commercial use without permission.</p>"),
 ("Intellectual property", "<p>The website design, text, graphics and photographs, the CIPS name and logo, and the Summit name and branding belong to their respective owners or licensors and are protected by law. You may view the site and share its pages for personal, non-commercial purposes. You may not reproduce, modify or redistribute content, or use the CIPS name or logo, without written permission.</p>"),
 ("Links and third parties", "<p>This website may link to or rely on third-party services (for example, Google for hosting typefaces and storing registration data). We are not responsible for the content or practices of third parties.</p>"),
 ("Disclaimer and liability", "<p>The website and its content are provided “as is”. To the fullest extent permitted by law, we do not guarantee that the site will be uninterrupted or error-free, and we are not liable for indirect or consequential loss arising from your use of it. Nothing in these terms limits any liability that cannot be limited by law.</p>"),
 ("Governing law", "<p>These terms and any dispute arising from your use of this website are governed by the laws of <strong>" + GOVERNING + "</strong>, and the courts of <strong>" + COURTS + "</strong> have exclusive jurisdiction, subject to any mandatory rights you have under the law of your own country.</p>"),
 ("Changes to these terms", "<p>We may update these terms from time to time. The “Last updated” date shows the current version. Continued use of the website after a change means you accept the updated terms.</p>"),
], "Terms of Use for www.cips2027.online and registration for the CIPS International Procurement & Supply Chain Summit 2027.")

legal_page("cancellation.html", "Cancellation Policy", "Legal", "What happens if you can no longer attend, and what happens if the Summit changes.", [
 ("Registering your interest", "<p>The registration form on this website records your <strong>interest</strong> in attending. Our team then reviews your details and confirms your participation. This website itself does not take payments.</p>"),
 ("If you can no longer attend", "<ul><li>Please tell us as early as you can, so that we can offer your place to another delegate. Contact the organising team " + CONTACT + ", quoting your name and organisation.</li><li>Once we receive your message, we will cancel your registration and confirm this to you.</li><li>If you are unable to attend, you may ask to nominate a colleague in your place. Substitutes are subject to our approval, because the Summit is designed for senior decision-makers.</li></ul>"),
 ("Fees and refunds", "<p>" + FEE_TEXT + " is invoiced separately after your place is confirmed. If you cancel a confirmed place, the following schedule applies, counted from the date we receive your cancellation:</p><div class=\"tablewrap\"><table class=\"refund\"><thead><tr><th>When you cancel</th><th>Refund</th><th>Substitute delegate</th></tr></thead><tbody>" + "".join(f"<tr><td>{a}</td><td><strong>{b}</strong></td><td>{c}</td></tr>" for a, b, c in REFUNDS) + "</tbody></table></div><p>Refunds are made to the original payer, normally within a reasonable period after we confirm your cancellation. If the conditions in your own confirmation differ from this schedule, your confirmation applies.</p>"),
 ("If we change or cancel the Summit", "<p>We may need to change the date, venue, format, programme or speakers, or to reschedule or cancel the Summit, including for reasons outside our control such as safety concerns, government restrictions, severe weather, travel disruption or insufficient capacity. If that happens, we will contact you as soon as reasonably possible using the details you gave us and explain your options. If the Summit is rescheduled or materially changed, you may withdraw your registration. If we cancel the Summit, any fee you have paid will be refunded in full or, if you prefer, credited to a future edition.</p>"),
 ("Changes to speakers and programme", "<p>Speaker line-ups and programme details can change. A change of speaker or session is not, by itself, a reason for cancellation.</p>"),
 ("No-shows", "<p>If you have a confirmed place and do not attend without telling us, we may treat your registration as cancelled and any conditions in your confirmation will apply.</p>"),
 ("Your information after cancelling", "<p>When you cancel we stop using your details for the Summit, except where we need to keep them for a legal reason. You can ask us to delete your registration details. See the <a href=\"privacy.html\">Privacy Policy</a>.</p>"),
], "Cancellation Policy for the CIPS International Procurement & Supply Chain Summit 2027.")

# =========================================================== 404
nf = head(f"Page not found | {SITE}", "The page you are looking for could not be found.") + header("404.html") + f'''
<main id="main"><div class="wrap"><section class="nf fade"><p class="nf-n" aria-hidden="true">404</p><div class="kicker"><span>Page not found</span></div><h1>This page has <em>moved on</em></h1><p class="lede">The page you are looking for does not exist or has been moved. Head back to the summit home page, or register your interest to attend.</p><div class="cta"><a class="btn" href="index.html">Back to Home {ARROW}</a><a class="btn ghost" href="register.html">Register Now</a></div></section></div></main>
''' + footer()
nf = nf.replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n<meta name="theme-color"', 1)
write("404.html", nf)


# =========================================================== AWARDS PAGE
# Content per the client's "CIPS WEBSITE CHANGES" doc (Nov 2026): individual awards first, then company awards.
# (name, icon, about, eligibility, [evaluation criteria], supporting evidence or "")
IND_AWARDS = [
    ("Procurement Excellence Award", "award",
     "Recognises procurement professionals who demonstrate outstanding performance, commercial expertise and measurable contributions to organisational success.",
     "Minimum three years of procurement or supply chain experience; professionals working below head-of-function level.",
     ["Measurable savings, cost avoidance, efficiency or quality improvements.", "Excellence in sourcing, negotiation, contracting and supplier management.",
      "Ethical procurement practices and compliance.", "Positive influence on stakeholders and colleagues."],
     "One or two quantified case studies and a line-manager endorsement."),
    ("Procurement Leader of the Year", "compass",
     "Honours procurement leaders who have delivered exceptional strategic, financial or organisational impact while developing high-performing teams.",
     "Department Heads, General Managers, Directors or equivalent leaders, excluding CPOs.",
     ["Significant financial, cultural or reputational impact.", "Advancement of organisational procurement strategy.",
      "Increased visibility and influence of the procurement function.", "Team development, talent management and succession planning."],
     "Quantified strategic achievements and two testimonials (senior executive and team member)."),
    ("Emerging Procurement Leader", "trend",
     "Celebrates rising procurement professionals demonstrating exceptional achievements, initiative and leadership potential early in their careers.",
     "Age 30 or below as of 1 January 2027, or fewer than five years of procurement experience (final rule to be confirmed).",
     ["Achievements exceeding expectations for career stage.", "Initiative, collaboration and leadership potential.",
      "Progress in professional qualifications and development.", "Contributions through mentoring, volunteering or knowledge sharing."],
     "Professional achievements and supporting testimonials, where available."),
    ("CPO of the Year", "award",
     "Recognises senior procurement executives who have positioned procurement as a strategic driver of enterprise value, transformation and business resilience.",
     "CPO, Head of Procurement or equivalent, reporting to the CEO, CFO or COO, with at least 12 months in the role.",
     ["Procurement’s strategic influence at board level.", "Enterprise-wide value creation, risk management and ESG outcomes.",
      "Functional transformation through digitalisation and talent development.", "Contributions to India’s procurement ecosystem."],
     "CEO/board endorsement and two to three quantified enterprise-level achievements."),
]
COM_AWARDS = [
    ("Best Procurement Team (Large Organization)", "users",
     "Recognises procurement teams delivering exceptional business performance, organisational influence and measurable value.",
     "Proposed annual turnover of ₹1,000 crore or more (subject to confirmation).",
     ["Strategic influence of the procurement function.", "Performance and organisational culture improvements.",
      "Measurable savings, efficiency and competitive advantage.", "Team capability and employee engagement."], ""),
    ("Best Procurement Team (Small Organization)", "users",
     "Celebrates procurement teams delivering outstanding results through innovation, efficiency and effective resource utilisation.",
     "Proposed fewer than 250 employees and/or annual turnover below ₹1,000 crore (subject to confirmation).",
     ["Procurement’s organisational contribution and influence.", "Improvements in performance and team culture.",
      "Measurable business value relative to available resources.", "Team development and operational efficiency."], ""),
    ("Best Sustainability Project / Program", "leaf",
     "Recognises procurement initiatives delivering measurable environmental, social and governance impact.",
     "Procurement-led or organisation-led projects with demonstrated procurement involvement.",
     ["Clear and achievable ESG objectives.", "Measurable outcomes in emissions, waste, water or responsible sourcing.",
      "Supplier engagement and capability development.", "Contributions to sustainability, human rights and social value."], ""),
    ("Best Digital Transformation Project", "cpu",
     "Recognises procurement teams successfully implementing AI, automation or digital solutions to improve business performance.",
     "In-house procurement or supply chain teams.",
     ["Clear business challenge and technology-led solution.", "Successful adoption and change management.",
      "Measurable improvements in efficiency, savings, compliance or data quality.", "Procurement leadership and solution scalability."], ""),
    ("Public Procurement Projects", "shield",
     "Celebrates public procurement initiatives demonstrating transparency, accountability and measurable improvements in public-service delivery.",
     "Government departments, PSUs, autonomous bodies and eligible GeM-based procurement projects.",
     ["Compliance with public procurement rules and policies.", "Value for money and improved citizen or service outcomes.",
      "Transparency, fairness and audit readiness.", "Replicability across public institutions."], ""),
    ("Best Knowledge Infusion", "book",
     "Recognises learning and development initiatives that strengthen procurement capabilities and professional excellence.",
     "Organisations, training institutions or consortia delivering structured procurement learning programmes.",
     ["Development of procurement and leadership capabilities.", "Measurable improvement in organisational performance.",
      "Training reach and professional qualifications achieved.", "Mentoring, knowledge sharing and industry contribution."], ""),
    ("Best Technology Partner", "net",
     "Recognises outstanding partnerships between technology providers and procurement teams that deliver measurable business improvements through successful technology implementation.",
     "Technology/SaaS providers or implementation partners with a named client organisation. Joint entries with client procurement teams are encouraged.",
     ["Quantifiable client business outcomes.", "Partnership quality, collaboration and implementation support.",
      "Technology adoption and user experience.", "Client satisfaction and successful delivery."],
     "Mandatory client testimonial."),
    ("Best Procurement Solution", "box",
     "Recognises innovative procurement products, platforms or services demonstrating proven market impact across multiple organisations.",
     "Solution providers with live clients in India.",
     ["Innovation and differentiation from existing solutions.", "Measurable results across at least two client organisations.",
      "Relevance to Indian procurement requirements.", "Data security, protection and future development roadmap."], ""),
]
FEE_IND, FEE_COM = "25,000", "50,000"   # nomination fees, exclusive of GST (client PDF, Oct 2026)
# (position, name, type, icon) for the JSON-LD ItemList
AWARD_CATS = [(i + 1, a[0], "Individual", a[1]) for i, a in enumerate(IND_AWARDS)] + \
             [(len(IND_AWARDS) + i + 1, a[0], "Company", a[1]) for i, a in enumerate(COM_AWARDS)]

def _award_card(i, a, typ):
    name, icn, about, elig, crit, ev = a
    ind = typ == "Individual"
    body = (f'<h4>Eligibility</h4><p>{elig}</p><h4>Evaluation Criteria</h4>{_ul(crit)}'
            + (f'<h4>Supporting Evidence</h4><p>{ev}</p>' if ev else ""))
    return (f'<article class="ac reveal" data-type="{typ.lower()}" data-key="{"ind" if ind else "com"}-{i + 1:02d}" style="--d:{(i % 4) * 0.06:.2f}s"><span class="ac-n" aria-hidden="true">{i + 1:02d}</span>'
            f'<i>{ic(icn)}</i><h3>{name}</h3><p class="ac-about">{about}</p>'
            f'<details class="ac-more"><summary>Eligibility &amp; criteria<span class="ac-go" aria-hidden="true">{ARROW}</span></summary><div class="ac-body">{body}</div></details>'
            f'<div class="ac-meta"><span class="tag {"ind" if ind else "com"}">{typ}</span><span class="ac-fee">&#8377;{FEE_IND if ind else FEE_COM} + GST</span></div></article>')

ind_cards = "".join(_award_card(i, a, "Individual") for i, a in enumerate(IND_AWARDS))
com_cards = "".join(_award_card(i, a, "Company") for i, a in enumerate(COM_AWARDS))

GUIDES = [("Participation", "Open to CIPS members and non-members."),
          ("Eligibility Period", "Completed work with measurable results, proposed within the previous 12–24 months."),
          ("Geographic Scope", "Nominees or projects based in or primarily serving India (subject to confirmation)."),
          ("Evidence", "Quantified achievements, case studies and supporting testimonials where required."),
          ("Individual Entries", "Each nominee may enter only one individual award category."),
          ("Attachments", "Individual headshot or team photograph and supporting PDF or image files. Photos are resized automatically."),
          ("Client Disclosure", "Mandatory for consultancy and technology-provider nominations."),
          ("Confidentiality", "Entries accessible only to the authorised awards team and judges."),
          ("Judging", "Proposed independent MCIPS/FCIPS judging panel, with conflicts of interest declared. Judges’ decisions are final, with no correspondence on shortlisting or winners.")]
guides = "".join(f'<div class="gd reveal" style="--d:{(i % 3) * 0.06:.2f}s"><b>{t}</b><p>{d}</p></div>' for i, (t, d) in enumerate(GUIDES))

STEPS = [("Select Your Award Category", "Choose the category that best reflects your achievements."),
         ("Complete the Nomination Form", "Provide nominee details, project information and relevant achievements."),
         ("Submit Supporting Evidence", "Upload measurable results, case studies, endorsements and required documents."),
         ("Finalise Your Nomination", "Review your submission and complete the applicable nomination payment.")]
steps = "".join(f'<li class="reveal" style="--d:{i * 0.08:.2f}s"><span class="st-n">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))

SCORE_COM = [("Measurable Results &amp; Value", 35), ("Innovation &amp; Approach", 20), ("Strategic Alignment &amp; Procurement’s Role", 15),
             ("Stakeholder &amp; Supplier Collaboration", 15), ("Sustainability &amp; Replicability", 15)]
SCORE_IND = [("Measurable Results &amp; Value", 30), ("Innovation &amp; Approach", 15), ("Strategic Alignment &amp; Leadership", 25),
             ("Stakeholder &amp; Supplier Collaboration", 10)]
def _score(title, rows, total_lab):
    top = max(p for _c, p in rows)
    li = "".join(f'<li><span>{c}</span><b>{p}</b><i style="--w:{p / top * 100:.0f}%"></i></li>' for c, p in rows)
    return (f'<article class="score reveal"><span class="fee-lab">{title}</span><ol>{li}</ol>'
            f'<div class="score-t"><span>{total_lab}</span><b>{sum(p for _c, p in rows)}</b><small>points</small></div></article>')

awards_page = head(f"Awards | {SITE}", "CIPS India Awards 2027: twelve award categories for individuals and organisations, with eligibility, judging criteria and nomination fees.") + header("awards.html") + f'''
<main id="main">
<div class="wrap"><section class="phead phead-seal">
  <div class="fade">{EVENT_NAME}<div class="kicker"><span>Awards</span></div><h1>CIPS India <em>Awards 2027</em></h1>
  <p class="aw-tag">Recognising Excellence. Celebrating Leadership. Inspiring the Future.</p>
  <p class="lede">The CIPS India Awards 2027, held in conjunction with the CIPS International Procurement &amp; Supply Chain Summit 2027, recognise outstanding individuals, teams and organisations driving excellence in procurement and supply chain management.</p>
  <p class="lede aw-lede2">Across {len(AWARD_CATS)} award categories, the awards celebrate exceptional leadership, innovation, sustainability, digital transformation and measurable contributions to the profession.</p>
  <div class="cta"><a class="btn" href="#categories">Explore Award Categories {ARROW}</a><a class="btn ghost" href="nominate.html">Nominate Now</a></div></div>
  <aside class="aside fade" style="--d:.15s"><div class="award-stage">{AWARD_FIG}</div></aside>
</section></div>

<section class="sec" style="padding-top:0"><div class="wrap"><div class="eyebrow reveal">Event Information</div>
  <div class="afacts reveal">
    <div class="af"><i>{ic("cal")}</i><small>Date</small><b>07 January 2027</b></div>
    <div class="af"><i>{ic("pin")}</i><small>Venue</small><b>ITC Maratha, Mumbai</b></div>
    <div class="af"><i>{ic("award")}</i><small>Award Categories</small><b>{len(IND_AWARDS)} Individual &middot; {len(COM_AWARDS)} Company</b></div>
  </div>
</div></section>

<section class="sec tint" id="categories"><div class="wrap">
  <div class="aw-intro reveal"><div class="eyebrow">Individual Awards &middot; 01&ndash;04</div><h2>Celebrating Outstanding <em>Procurement Professionals &amp; Leaders</em></h2></div>
  <div class="acats acats-4">{ind_cards}</div>

  <div class="aw-intro aw-group reveal"><div class="eyebrow">Company, Team &amp; Organisation Awards &middot; 01&ndash;08</div><h2>Recognising Innovation, Performance &amp; <em>Organisational Impact</em></h2></div>
  <div class="acats acats-4">{com_cards}</div>

  <aside class="aw-diff reveal" aria-label="Categories 07 and 08 compared"><h3>Understanding the Difference Between Categories 07 &amp; 08</h3>
    <div><b><span>07</span>Best Technology Partner</b><p>Recognises the success of a specific partnership between a technology provider and a client organisation, focusing on collaboration, implementation and measurable outcomes.</p></div>
    <div><b><span>08</span>Best Procurement Solution</b><p>Recognises the broader innovation and market impact of a procurement product, platform or service, supported by proven results across multiple client organisations.</p></div>
  </aside>
</div></section>

<section class="sec" id="guidelines"><div class="wrap">
  <div class="eyebrow">Before You Apply</div><h2 class="reveal" style="margin-bottom:clamp(36px,5vw,56px)">General Nomination <em>Guidelines</em></h2>
  <div class="guides">{guides}</div>
</div></section>

<section class="sec tint" id="nominate"><div class="wrap">
  <div class="eyebrow">How to Enter</div><h2 class="reveal" style="margin-bottom:clamp(36px,5vw,56px)">Nomination <em>Process</em></h2>
  <ol class="steps4">{steps}</ol>
  <div class="steps-go reveal"><a class="btn" href="nominate.html">Start Your Nomination {ARROW}</a><span>Takes about 15 minutes. Your answers are saved on this device as you go.</span></div>
</div></section>

<section class="sec" id="fees"><div class="wrap"><div class="eyebrow">Nomination Fees</div><h2 style="margin-bottom:48px" class="reveal">Nomination <em>Fees</em></h2>
  <div class="fees">
    <article class="fee reveal"><span class="fee-lab">Individual Awards</span><h3>Categories 01&ndash;04</h3><p>{len(IND_AWARDS)} categories recognising individual professionals and leaders.</p><div class="fee-price"><small>&#8377;</small>{FEE_IND}</div><p class="fee-gst">Plus GST, per nomination</p><a class="fee-go" href="nominate.html">Start an individual nomination {ARROW}</a></article>
    <article class="fee solid reveal" style="--d:.1s"><span class="fee-lab">Company Awards</span><h3>Categories 01&ndash;08</h3><p>{len(COM_AWARDS)} categories recognising teams, projects and organisations.</p><div class="fee-price"><small>&#8377;</small>{FEE_COM}</div><p class="fee-gst">Plus GST, per nomination</p><a class="fee-go" href="nominate.html">Start a company nomination {ARROW}</a></article>
  </div>
  <p class="fee-note reveal">All fees are exclusive of GST and payable online when you finalise your nomination.</p>
</div></section>

<section class="sec tint" id="judging"><div class="wrap">
  <div class="two sec-intro"><div class="reveal"><div class="eyebrow">How Nominations Are Assessed</div><h2>Judging &amp; <em>Evaluation</em></h2></div>
  <div class="body reveal" style="--d:.1s"><p>Nominations will be assessed on demonstrated achievements, measurable business value, innovation, procurement leadership and stakeholder impact.</p></div></div>
  <div class="scores">{_score("Proposed Company / Team / Project Scoring", SCORE_COM, "Total")}{_score("Proposed Individual Award Scoring", SCORE_IND, "Subtotal")}</div>
</div></section>

{cta_band(h="Your Excellence Deserves <em>Recognition</em>", btn="Nominate Now", href="nominate.html", p="Showcase your achievements and celebrate your contribution to the future of procurement and supply chain management.")}
<dialog class="aw-dlg" id="aw-dlg" aria-labelledby="aw-dlg-t">
  <div class="aw-dlg-in">
    <header class="aw-dlg-hd"><span class="aw-dlg-k"></span><button type="button" class="aw-dlg-x" data-close aria-label="Close award details"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></header>
    <div class="aw-dlg-bd"></div>
    <footer class="aw-dlg-ft"><button type="button" class="aw-dlg-nav prev" data-step="-1" aria-label="Previous award">{ARROW}</button><span class="aw-dlg-pos"></span><button type="button" class="aw-dlg-nav" data-step="1" aria-label="Next award">{ARROW}</button><a class="btn aw-dlg-nom" href="nominate.html">Nominate for this Award {ARROW}</a></footer>
  </div>
</dialog>
</main>
''' + footer()
write("awards.html", awards_page)

# =========================================================== NOMINATE (4-step nomination flow)
# Award data for the wizard; keys like "ind-01" / "com-07" are what ?award= and the sheet use.
import json as _json_n
def _aw_key(typ, i): return f'{"ind" if typ == "Individual" else "com"}-{i + 1:02d}'
NOM_AWARDS = ([{"key": _aw_key("Individual", i), "n": f"{i + 1:02d}", "name": a[0], "type": "Individual", "fee": FEE_IND, "elig": a[3], "crit": a[4], "ev": a[5]} for i, a in enumerate(IND_AWARDS)] +
              [{"key": _aw_key("Company", i), "n": f"{i + 1:02d}", "name": a[0], "type": "Company", "fee": FEE_COM, "elig": a[3], "crit": a[4], "ev": a[5]} for i, a in enumerate(COM_AWARDS)])
# Categories where an endorsement / testimonial is part of the required evidence (per the awards copy)
ENDORSE_REQ = ["ind-01", "ind-02", "ind-04", "com-07"]
for _a in NOM_AWARDS: _a["endorse"] = _a["key"] in ENDORSE_REQ

def _cat_radio(a):
    return (f'<label class="nm-cat"><input type="radio" name="award" value="{a["key"]}" required>'
            f'<span class="nm-cat-n">{a["n"]}</span><span class="nm-cat-t">{a["name"]}</span><span class="nm-cat-f">&#8377;{a["fee"]} + GST</span></label>')

def tarea(name, label, maxlen, hint="", req=True):
    star = "<i aria-hidden='true'>*</i>" if req else ""
    return (f'<div class="field field-wide"><label for="{name}">{label}{star}</label>'
            + (f'<p class="hint">{hint}</p>' if hint else "") +
            f'<textarea id="{name}" name="{name}" rows="6" maxlength="{maxlen}"{" required" if req else ""}></textarea>'
            f'<span class="count" data-count-for="{name}">0 / {maxlen}</span><span class="err" role="alert"></span></div>')

def sel(name, label, opts, req=True, placeholder="Select"):
    star = "<i aria-hidden='true'>*</i>" if req else ""
    o = f'<option value="">{placeholder}</option>' + "".join(f'<option>{x}</option>' for x in opts)
    return f'<div class="field"><label for="{name}">{label}{star}</label><select id="{name}" name="{name}"{" required" if req else ""}>{o}</select><span class="err" role="alert"></span></div>'

def filebox(name, label, hint, accept, multiple=False, req=True, extra=""):
    star = "<i aria-hidden='true'>*</i>" if req else ""
    return (f'<div class="field field-wide filebox" data-file="{name}"{extra}><label for="{name}">{label}<i aria-hidden="true" class="req-star"{"" if req else " hidden"}>*</i></label>'
            f'<p class="hint">{hint}</p>'
            f'<label class="drop" for="{name}">{ic("box")}<span><b>Choose file{"s" if multiple else ""}</b> or drag {"them" if multiple else "it"} here</span></label>'
            f'<input id="{name}" name="{name}" type="file" accept="{accept}"{" multiple" if multiple else ""}{" required" if req else ""}>'
            f'<ul class="files" aria-live="polite"></ul><span class="err" role="alert"></span></div>')

_ind_cats = "".join(_cat_radio(a) for a in NOM_AWARDS if a["type"] == "Individual")
_com_cats = "".join(_cat_radio(a) for a in NOM_AWARDS if a["type"] == "Company")
NOM_STEPS = [s[0] for s in STEPS]
_cur = ' aria-current="step"'
_nm_steps = "".join(f'<li data-s="{i + 1}"{_cur if i == 0 else ""}><span>{i + 1:02d}</span><b>{t}</b></li>' for i, t in enumerate(NOM_STEPS))
_EXP = ["Less than 3 years", "3–5 years", "5–10 years", "10–15 years", "15+ years"]
_TURN = ["Below ₹100 crore", "₹100–999 crore", "₹1,000–4,999 crore", "₹5,000 crore or more", "Not applicable / public body"]
_EMP = ["Fewer than 50", "50–249", "250–999", "1,000–4,999", "5,000 or more"]

nominate_page = head(f"Submit a Nomination | {SITE}", "Nominate for the CIPS India Awards 2027 in four steps: choose a category, complete the form, upload supporting evidence, then review and pay the nomination fee.") + header("awards.html") + f'''
<main id="main">
<div class="wrap"><section class="phead nm-head">
  <div class="fade"><div class="kicker"><span>CIPS India Awards 2027</span></div><h1>Submit a <em>Nomination</em></h1>
  <p class="lede">Four steps: select your award category, complete the nomination form, submit supporting evidence, then review your entry and pay the nomination fee.</p>
  <p class="pay-link">Already nominated? <a href="pay.html">Complete your payment {ARROW}</a></p></div>
</section></div>

<div class="wrap nm">
  <aside class="nm-side" aria-label="Your nomination">
    <div class="nm-sum">
      <span class="fee-lab">Your Nomination</span>
      <p class="nm-sum-t" data-sum="name">No category selected yet</p>
      <p class="nm-sum-k" data-sum="meta"></p>
      <div class="nm-sum-fee" data-sum="fee" hidden></div>
    </div>
    <details class="nm-tipbox" open><summary>Before you start</summary><ul class="nm-tips">
      <li>{ic("check")}<span>Open to CIPS members and non-members.</span></li>
      <li>{ic("check")}<span>Each nominee may enter only one individual award category.</span></li>
      <li>{ic("check")}<span>Attachments: PDF or images. Photos are resized automatically; PDFs up to 30 MB in total.</span></li>
      <li>{ic("check")}<span>Your answers are saved on this device as you go, so you can come back later. Files need to be attached again.</span></li>
    </ul>
    <a class="nm-link" href="awards.html#guidelines">Read the nomination guidelines {ARROW}</a></details>
  </aside>

  <div class="form-card nm-card" id="nm-card">
    <ol class="nm-steps" aria-label="Nomination steps">{_nm_steps}</ol>
    <p class="nm-now" aria-hidden="true"></p>
    <noscript><p class="form-alert show">Please enable JavaScript to submit a nomination.</p></noscript>
    <form id="nominate-form" novalidate>
      <script type="application/json" id="nm-awards">{_json_n.dumps(NOM_AWARDS, ensure_ascii=False)}</script>
      <div class="nm-chip" data-chip hidden><span><b data-chip-name></b><small data-chip-fee></small></span><button type="button" data-goto="1">Change</button></div>

      <section class="nm-step" data-step="1" aria-labelledby="nm-h1">
        <h2 id="nm-h1">Select Your <em>Award Category</em></h2>
        <p class="note">Choose the category that best reflects your achievements.</p>
        <div class="nm-find" role="search">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
          <input type="search" id="nm-q" placeholder="Search awards, e.g. ESG" aria-label="Search award categories" aria-describedby="nm-q-n" autocomplete="off" enterkeyhint="search" spellcheck="false">
          <button type="button" class="nm-find-x" aria-label="Clear search" hidden>&times;</button>
        </div>
        <div class="nm-find-tags" aria-label="Quick filters"><button type="button" data-q="leadership">Leadership</button><button type="button" data-q="teams">Teams</button><button type="button" data-q="sustainability">Sustainability</button><button type="button" data-q="digital">Digital</button><button type="button" data-q="technology">Technology</button><button type="button" data-q="public sector">Public sector</button></div>
        <p class="nm-find-n" id="nm-q-n" aria-live="polite" hidden></p>
        <fieldset class="nm-cats" data-group="award"><legend>Individual Awards &middot; 01&ndash;04 <small>&#8377;{FEE_IND} + GST</small></legend>{_ind_cats}</fieldset>
        <fieldset class="nm-cats"><legend>Company, Team &amp; Organisation Awards &middot; 01&ndash;08 <small>&#8377;{FEE_COM} + GST</small></legend>{_com_cats}</fieldset>
        <span class="err nm-err" data-err="award" role="alert"></span>
      </section>

      <section class="nm-step" data-step="2" aria-labelledby="nm-h2" hidden>
        <h2 id="nm-h2">Complete the <em>Nomination Form</em></h2>
        <p class="note">Provide nominee details, project information and relevant achievements. Fields marked * are required.</p>
        <div class="nm-elig"><b>Eligibility for <span data-fill="name"></span></b><p data-fill="elig"></p></div>

        <fieldset class="fs"><legend><span>A</span>About You (Nominator)</legend>
          <div class="grid-2">
            {field("nomName", "Full Name", auto="name")}
            {field("nomEmail", "Official Email Address", "email", auto="email")}
            {field("nomMobile", "Mobile Number", "tel", auto="tel", extra='inputmode="tel" placeholder="+91 …"')}
            {field("nomOrg", "Organisation", auto="organization")}
            {field("nomDesignation", "Designation", auto="organization-title")}
            {sel("membership", "CIPS Membership", ["CIPS member", "Not a CIPS member"])}
            <div data-if-member hidden>{field("memberNo", "CIPS Membership Number")}</div>
          </div>
        </fieldset>

        <fieldset class="fs" data-for="Individual"><legend><span>B</span>The Nominee</legend>
          <label class="check nm-self"><input type="checkbox" name="selfNominate"><span class="box">{ic("check")}</span><span><strong>I am nominating myself</strong> <span class="t">— copies your details into the nominee fields.</span></span></label>
          <div class="grid-2">
            {field("nomineeName", "Nominee Full Name")}
            {field("nomineeEmail", "Nominee Email Address", "email")}
            {field("nomineeDesignation", "Nominee Designation")}
            {field("nomineeOrg", "Nominee Organisation")}
            {sel("experience", "Procurement / Supply Chain Experience", _EXP)}
            <div data-for-award="ind-03">{field("dob", "Date of Birth", "date", req=False)}</div>
          </div>
        </fieldset>

        <fieldset class="fs" data-for="Company" hidden><legend><span>B</span>The Organisation &amp; Entry</legend>
          <div class="grid-2">
            {field("orgName", "Organisation Name", auto="organization")}
            {field("entryTitle", "Team / Project / Solution Name")}
            {field("leadName", "Team or Project Lead")}
            {field("leadDesignation", "Lead’s Designation")}
            {field("leadEmail", "Lead’s Email Address", "email")}
            {field("sector", "Industry / Sector")}
            {sel("turnover", "Annual Turnover", _TURN)}
            {sel("employees", "Number of Employees", _EMP)}
          </div>
          <div data-for-award="com-07,com-08" class="grid-2 nm-client">
            {field("clientOrg", "Client Organisation(s)", extra='placeholder="Named client(s) for this entry"')}
            <p class="hint nm-client-h">Client disclosure is mandatory for consultancy and technology-provider nominations. Best Procurement Solution entries need results across at least two client organisations.</p>
          </div>
        </fieldset>

        <fieldset class="fs"><legend><span>C</span>Nomination Details</legend>
          <div class="grid-2">
            {field("city", "City / Location", req=False, auto="address-level2")}
            {field("period", "Period of the Work", extra='placeholder="e.g. Apr 2025 – Sep 2026"')}
          </div>
          <div class="nm-crit"><b>What the judges look for</b><ul data-fill="crit"></ul></div>
          {tarea("summary", "Nomination Summary", 2500, "Describe the nominee, team or project and what makes this entry stand out.")}
          {tarea("results", "Measurable Results &amp; Achievements", 2000, "Quantify the impact: savings, cost avoidance, efficiency, quality, ESG or service outcomes, with the time period.")}
          <label class="check"><input type="checkbox" name="eligible" required><span class="box">{ic("check")}</span><span class="t">I confirm the nominee or entry meets the eligibility criteria for this category, and the work was completed with measurable results within the last 12–24 months.</span></label>
          <span class="err nm-err" data-err="eligible" role="alert"></span>
        </fieldset>
      </section>

      <section class="nm-step" data-step="3" aria-labelledby="nm-h3" hidden>
        <h2 id="nm-h3">Submit Supporting <em>Evidence</em></h2>
        <p class="note">Upload measurable results, case studies, endorsements and required documents. PDF or images (JPEG, PNG, HEIC, WebP). Photos are resized for you, so any size is fine; PDFs can be up to 30 MB in total.</p>
        <div class="nm-elig" data-ev-box><b>Required for <span data-fill="name"></span></b><p data-fill="ev"></p></div>
        {filebox("photo", '<span data-photo-label>Individual Headshot</span>', "A clear, recent photograph. Any size: we resize it for you.", "image/*")}
        {filebox("docs", "Case Studies &amp; Supporting Documents", "Up to 3 files: quantified case studies, results summaries or project reports (PDF or images).", "application/pdf,image/*", multiple=True)}
        {filebox("endorse", "Endorsements &amp; Testimonials", "Up to 2 files, e.g. a line-manager, senior-executive, CEO/board or client endorsement (PDF or images).", "application/pdf,image/*", multiple=True, req=False)}
        {field("evidenceLink", "Link to Additional Evidence", "url", req=False, extra='placeholder="https://… (optional: video, article or shared folder)"')}
      </section>

      <section class="nm-step" data-step="4" aria-labelledby="nm-h4" hidden>
        <h2 id="nm-h4">Finalise Your <em>Nomination</em></h2>
        <p class="note">Review your submission, then submit it and complete the applicable nomination payment.</p>
        <div class="nm-review" data-review></div>
        <div class="nm-fee"><div><span class="fee-lab">Nomination Fee</span><b data-fill="fee"></b></div><p>Plus GST, payable after you submit. You will receive a nomination reference to use with your payment.</p></div>
        <fieldset class="fs nm-decl"><legend><span>D</span>Declarations</legend>
          <label class="check"><input type="checkbox" name="declAccurate" required><span class="box">{ic("check")}</span><span class="t">The information and evidence provided are accurate, and I have permission to share them, including any client or third-party details.</span></label>
          <label class="check" data-for="Individual"><input type="checkbox" name="declOne" required><span class="box">{ic("check")}</span><span class="t">The nominee has not been entered in any other individual award category.</span></label>
          <label class="check"><input type="checkbox" name="declJudging" required><span class="box">{ic("check")}</span><span class="t">I accept that entries are reviewed only by the authorised awards team and judges, and that the judges’ decisions are final, with no correspondence on shortlisting or winners.</span></label>
          <label class="check"><input type="checkbox" name="declPrivacy" required><span class="box">{ic("check")}</span><span class="t">I agree to the <a href="terms.html">Terms of Use</a> and acknowledge the <a href="privacy.html">Privacy Policy</a>.</span></label>
          <span class="err nm-err" data-err="decl" role="alert"></span>
        </fieldset>
        <div class="hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
      </section>

      <p class="form-alert" role="alert"></p>
      <div class="nm-nav">
        <button type="button" class="btn ghost" data-back hidden>{ARROW}<span>Back</span></button>
        <span class="nm-pos" aria-live="polite">Step 1 of 4</span>
        <button type="button" class="btn" data-next><span>Continue</span>{ARROW}</button>
        <button type="submit" class="btn" data-submit hidden><span>Submit Nomination</span>{ARROW}</button>
      </div>
    </form>

    <div class="success nm-done" id="nominate-success" role="status">
      <ol class="flow-steps" aria-label="Nomination progress">
        <li class="done"><span>{ic("check")}</span>Nomination</li>
        <li class="cur" data-flow="pay"><span>2</span>Payment</li>
        <li data-flow="done"><span>3</span>Confirmed</li>
      </ol>

      <section class="reg-paystep" data-nm-step="pay">
        <h2>Complete Your <em>Payment</em></h2>
        <p>Your nomination is saved under reference <b class="ref-inline" data-ref></b> <button type="button" class="nm-copy" data-copy>Copy</button><br>We&rsquo;ve emailed it to <b data-fill="nomEmail"></b>.</p>
        <div class="order">
          <div class="order-item"><small data-nc="type"></small><b data-nc="award"></b><span>CIPS India Awards 2027 &middot; 07 January 2027 &middot; ITC Maratha, Mumbai</span></div>
          <dl class="order-who"><div><dt>Nominee</dt><dd data-nc="nominee"></dd></div><div><dt>Nominated by</dt><dd data-nc="nominator"></dd></div></dl>
          <dl class="order-lines"><div><dt>Nomination fee</dt><dd data-nc="base"></dd></div><div><dt>GST (18%)</dt><dd data-nc="gst"></dd></div><div class="tot"><dt>Total</dt><dd data-nc="total"></dd></div></dl>
          {PAYBOX}
        </div>
        <p class="reg-note pay-later">Not ready to pay now? Use the link in your email, or <a data-pay-later href="pay.html">pay later with your reference</a>.</p>
      </section>

      <section class="reg-confirm" data-nm-step="done" tabindex="-1" hidden>
        <div class="conf-stage">
          <div class="conf-copy">
            <p class="conf-kicker"><span class="conf-badge">{CONF_TICK}</span>Payment confirmed</p>
            <h2>Your nomination is in.</h2>
            <p class="conf-sub">The entry for the <b data-nc="award"></b> is complete and now goes to the judging panel. Your confirmation and receipt are on their way to <b data-fill="nomEmail"></b>.</p>
            <div class="conf-ref"><span>Nomination reference</span><b class="mono" data-ref></b><button type="button" class="conf-copy-btn" data-copy>Copy</button></div>
            <div class="conf-acts">
              <a class="btn conf-btn" href="nominate.html"><span>Submit another nomination</span>{ARROW}</a>
              <a class="btn conf-btn ghost" href="awards.html"><span>See all awards</span>{ARROW}</a>
            </div>
          </div>
          <div class="conf-show">
            <figure class="entry-card" aria-label="Your nomination entry">
              <div class="entry-top"><img src="assets/img/cips-logo-light.png" {ALT} width="84" height="32"><span class="mono" data-ref></span></div>
              <p class="entry-ev">CIPS India Awards 2027</p>
              <p class="entry-type" data-nc="type"></p>
              <p class="entry-award" data-nc="award"></p>
              <dl class="entry-who"><div><dt>Nominee</dt><dd data-nc="nominee"></dd></div><div><dt>Nominated by</dt><dd data-nc="nominatorName"></dd></div></dl>
              <p class="entry-foot">{CONF_TICK}Entry received and paid</p>
            </figure>
          </div>
        </div>
        <div class="conf-body">
          {RECEIPT("nm")}
          <div class="conf-side">
            <section class="conf-card" aria-labelledby="conf-who-nm">
              <h3 id="conf-who-nm">Your nomination</h3>
              <dl class="conf-dl">
                <div><dt>Award</dt><dd><span data-nc="award"></span><br><small data-nc="type"></small></dd></div>
                <div><dt>Nominee</dt><dd data-nc="nominee"></dd></div>
                <div><dt>Nominated by</dt><dd data-nc="nominator"></dd></div>
                <div><dt>Email</dt><dd data-fill="nomEmail"></dd></div>
              </dl>
            </section>
            <section class="conf-next" aria-labelledby="conf-next-nm">
              <h3 id="conf-next-nm">What happens next</h3>
              <ol>
                <li class="ok"><b>Confirmation and receipt emailed</b><span>Sent to <b data-fill="nomEmail"></b>. Not there in a few minutes? Check your spam or promotions folder.</span></li>
                <li><b>Judging</b><span>The panel reviews every entry against the published criteria and may contact you if they need anything more.</span></li>
                <li><b>Shortlist and awards night</b><span>Shortlisted nominees hear from us ahead of the ceremony on 07 January 2027 at ITC Maratha, Mumbai.</span></li>
              </ol>
            </section>
          </div>
        </div>
        <p class="conf-help">Questions about your nomination? Reply to your confirmation email and our team will help.</p>
      </section>
    </div>
  </div>
</div>
</main>
''' + footer()
write("nominate.html", nominate_page)
