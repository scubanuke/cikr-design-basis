"""Build the CIKR Design Basis Examples site from content/ into static HTML at the repo root.
Run from the repo root:  python3 tools/build.py
"""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = lambda *p: os.path.join(ROOT, *p)

# ---- configuration -------------------------------------------------------
EDITION = 'CIKR Design Basis Examples, Edition 1 (November 2026)'
EDITION_DATE = '1 November 2026'
VERSION_DOI = '10.5281/zenodo.23863986'
CONCEPT_DOI = '10.5281/zenodo.23863985'
FD_EDITION_DOI = '10.5281/zenodo.23401272'   # FD, November 2026 Edition (carries FD-DBL)
SCRM_DOI = '10.5281/zenodo.21365261'
PDF_BASE = 'https://scubanuke.github.io/publications/cikr/edition-1/'
SUBSTACK = 'https://timroxey.substack.com'
DRAFT_BANNER = True          # set False for the public launch
BANNER_TEXT = 'Early preview — November 2026'
MASTER_DRAFT_LIVE = False    # set True when Project 2 deposits the master draft
MASTER_DRAFT_DOI = ''        # fill when deposited
MASTER_DRAFT_CHAPTERS = {}   # sector slug -> chapter title, from Project 2's chapter-to-sector map

SECTORS = [  # card file, slug, display name
 ('01_Water.md','water','Water and Wastewater'),('02_Communications.md','communications','Communications'),
 ('03_Chemical.md','chemical','Chemical'),('04_Transportation.md','transportation','Transportation'),
 ('05_Emergency_Services.md','emergency-services','Emergency Services'),('06_Dams.md','dams','Dams'),
 ('07_Healthcare.md','healthcare','Healthcare and Public Health'),('08_Information_Technology.md','information-technology','Information Technology'),
 ('09_Financial_Services.md','financial-services','Financial Services'),('10_Food_and_Agriculture.md','food-and-agriculture','Food and Agriculture'),
 ('11_Critical_Manufacturing.md','critical-manufacturing','Critical Manufacturing'),('12_Defense_Industrial_Base.md','defense-industrial-base','Defense Industrial Base'),
 ('13_Government_Facilities.md','government-facilities','Government Facilities'),('14_Commercial_Facilities.md','commercial-facilities','Commercial Facilities'),
 ('15_Energy.md','energy','Energy')]
ALIASES = {'Water':'water','Healthcare':'healthcare','Healthcare and Public Health':'healthcare','Food and Agriculture':'food-and-agriculture'}
for f,s,n in SECTORS: ALIASES.setdefault(n,s); ALIASES.setdefault(n.split(' and ')[0] if s=='water' else n,s)
KIND = {'Sector framework':'sf','Facility class':'fc','Use case':'uc','Reference event':'re'}
ON_REQUEST = 'This document is available to defenders and regulators on request.'

e = html.escape
def inline(t):
    t = e(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)

# ---- content -------------------------------------------------------------
def parse_card(path):
    s = open(path, encoding='utf-8').read()
    d = {'cards': []}
    d['name'] = re.search(r'^# (.+)$', s, re.M).group(1).strip()
    d['sowhat'] = re.search(r'\*\*So what\?\*\* (.+)', s).group(1).strip()
    d['depends'] = re.search(r'\*\*Depends on:\*\* (.+)', s).group(1).strip()
    d['dependedby'] = re.search(r'\*\*Depended on by:\*\* (.+)', s).group(1).strip()
    for m in re.finditer(r'^## (Sector framework|Facility class|Use case|Reference event) — (.+?) \(([^)]+)\)\n(.+?)\n\*Source: ([^*]+)\*', s, re.M | re.S):
        body = m.group(4).strip()
        d['cards'].append({'kind': m.group(1), 'title': m.group(2).strip(), 'des': m.group(3).strip(),
                           'body': body.replace(ON_REQUEST, '').strip(), 'onreq': ON_REQUEST in body,
                           'src': m.group(5).strip()})
    assert len(d['cards']) == 4, path
    return d

GLOSSARY = json.load(open(C('content', 'glossary.json'), encoding='utf-8'))
FC = json.load(open(C('content', 'facility_classes.json'), encoding='utf-8'))['sectors']
READERS = json.load(open(C('content', 'readers.json'), encoding='utf-8'))
PAGES = json.load(open(C('content', 'pages.json'), encoding='utf-8'))
DATA = [(slug, name, parse_card(C('content', 'cards', f))) for f, slug, name in SECTORS]

# ---- layout --------------------------------------------------------------
NAV = [('index.html','Sectors'),('design-basis.html','What is a design basis?'),('readers/public.html','For the public'),
       ('readers/regulators.html','Regulators'),('readers/defenders.html','Defenders'),('readers/supply-chain.html','Supply chain'),
       ('glossary.html','Glossary'),('request.html','Ask for more')]
EXTERNAL_NAV = [('https://scubanuke.github.io/publications/','Publications')]
def page(path, title, body, desc='', terms=True):
    depth = path.count('/'); r = '../' * depth
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (r, h, ' class="on" aria-current="page"' if h == path else '', e(t)) for h, t in NAV)
    nav += ''.join('<a href="%s">%s</a>' % (h, e(t)) for h, t in EXTERNAL_NAV)
    gl = {k: {'t': v['term'], 'd': v['def'], 'm': v['match']} for k, v in GLOSSARY.items()}
    banner = '<div class="draftbar">%s</div>' % e(BANNER_TEXT) if DRAFT_BANNER else ''
    out = f'''<!DOCTYPE html>
<html lang="en" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body{'' if terms else ' class="no-terms"'}>
<a class="skip" href="#main">Skip to content</a>
{banner}
<header class="top"><div class="in">
<a class="brand" href="{r}index.html"><span class="eyebrow">Eclectic Technologies</span><span class="name">CIKR Design Basis Examples</span></a>
<nav aria-label="Site">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="in">
<p>Every document linked from this site is frozen in <em>{e(EDITION)}</em>, <a href="https://doi.org/{VERSION_DOI}">doi:{VERSION_DOI}</a>, as it stood on {EDITION_DATE}. Each is a working draft, marked DRAFT on its cover. The working documents continue to change, and later editions will record them.</p>
<p>Timothy E. Roxey, Eclectic Technologies. Text and documents licensed CC BY 4.0. Questions and requests: a private message through <a href="{SUBSTACK}">timroxey.substack.com</a>.</p>
<p>The full library of Eclectic Technologies documents, with their DOIs: <a href="https://scubanuke.github.io/publications/">Publications</a>.</p>
</div></footer>
<script>window.CIKR_GLOSSARY={json.dumps(gl, ensure_ascii=False)};</script>
<script src="{r}assets/glossary.js"></script>
</body>
</html>
'''
    full = C(path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(out)

def strip(slug, r):
    cells = []
    for _, s, n in SECTORS:
        cells.append('<a href="%ssectors/%s.html" title="%s"%s></a>' % (r, s, e(n), ' class="on" aria-current="page"' if s == slug else ''))
    cells.append('<span title="Nuclear Reactors, Materials and Waste: in development"></span>')
    return '<div class="strip" aria-label="All sixteen sectors">%s</div>' % ''.join(cells)

def deplinks(text, r):
    if text.lower().startswith('none'): return e(text)
    parts = [p.strip() for p in text.split(',')]
    out = []
    for p in parts:
        s = ALIASES.get(p)
        if s: out.append('<a href="%ssectors/%s.html">%s</a>' % (r, s, e(p)))
        elif p.startswith('Nuclear'): out.append('%s <span class="note">(in development)</span>' % e(p))
        else: out.append(e(p))
    return ', '.join(out)

# ---- sector pages ----------------------------------------------------------
def sector_page(slug, name, d):
    r = '../'
    cards = []
    order = {'sf': 0, 'fc': 1, 're': 2, 'uc': 3}
    for c in sorted(d['cards'], key=lambda c: order[KIND[c['kind']]]):
        k = KIND[c['kind']]
        label = {'re': 'Observed · Reference event', 'uc': 'Postulated · Use case'}.get(k, c['kind'])
        if k == 'uc':
            foot = '<p class="onreq"><a href="%srequest.html">%s</a></p><p class="note">Summary card only. Use cases are not published.</p>' % (r, ON_REQUEST)
        else:
            foot = '<a href="%s%s.pdf">Read the frozen document (PDF) →</a><br><span class="note">Frozen in Edition 1, %s · <a href="https://doi.org/%s">doi:%s</a></span>' % (PDF_BASE, e(c['src']), EDITION_DATE, VERSION_DOI, VERSION_DOI)
        cards.append(f'''<article class="card {k}">
<span class="kind">{e(label)}</span>
<h3>{e(c['title'])}</h3><p class="des">{e(c['des'])}</p>
<p>{inline(c['body'])}</p>
<div class="foot">{foot}</div>
</article>''')
    extra = ''
    if slug == 'energy':
        extra = f'<p class="prose">Energy is one sector with three subsectors: electric power, natural gas and petroleum. The edition also freezes the <a href="{PDF_BASE}DBA-GAS-Sector_Framework_v1_13.pdf">Natural Gas Sector Framework</a> (DBA-GAS-Sector_Framework, version 1.13), under which the facility class and the reference event shown here sit.</p>'
    others = FC.get(slug, [])
    olist = ''
    if others:
        groups = {}
        for o in others: groups.setdefault(o.get('group', ''), []).append(o)
        parts = []
        for g, items in groups.items():
            lis = ''.join('<li>%s <span class="st">— %s</span></li>' % (e(o['title']), 'written, available on request' if o['status'] == 'written' else 'planned') for o in items)
            parts.append(('<h3>%s</h3>' % e(g) if g else '') + '<ul>%s</ul>' % lis)
        olist = '<section class="others"><h2>Other facility classes in this sector</h2>%s<p class="note">These may change as the facility class work rolls out.</p></section>' % ''.join(parts)
    chapter = ''
    if MASTER_DRAFT_LIVE and slug in MASTER_DRAFT_CHAPTERS:
        chapter = '<p class="notice">The master draft reads this example in <a href="%smaster-draft.html">%s</a>.</p>' % (r, e(MASTER_DRAFT_CHAPTERS[slug]))
    body = f'''<p class="eyebrow">Sector</p>
<h1>{e(name)}</h1>
{strip(slug, r)}
<p class="sowhat"><strong>So what?</strong> {inline(d['sowhat'])}</p>
<div class="deps"><div><span class="lbl">Depends on</span><br>{deplinks(d['depends'], r)}</div><div><span class="lbl">Depended on by</span><br>{deplinks(d['dependedby'], r)}</div></div>
{extra}
<p class="prose note">The framework and facility class set the design basis. The last two cards keep evidence and hypothesis apart: <strong>Observed</strong> is a real event and what it showed; <strong>Postulated</strong> is a scenario the design must withstand.</p>
<div class="cards">
{''.join(cards)}
</div>
{chapter}
{olist}'''
    page('sectors/%s.html' % slug, '%s — CIKR Design Basis Examples' % name, body, d['sowhat'])

# ---- top pages -----------------------------------------------------------
def home():
    tree = ''.join('<a href="sectors/%s.html">%s<small>%s</small></a>' % (s, e(n), e(d['cards'][1]['title'])) for s, n, d in DATA)
    tree += '<span class="held">Nuclear Reactors, Materials and Waste<small>In development</small></span>'
    sw = ''.join('<p>%s</p>' % inline(p) for p in PAGES['home']['sowhat'])
    readers = ''.join('<li><a href="readers/%s.html">%s</a> — %s</li>' % (k, e(v['title']), e(v['blurb'])) for k, v in READERS.items())
    md = '<p>The master draft that reads these examples together, <a href="master-draft.html"><em>Governing Generative AI in Critical Infrastructure Control</em></a>, has a page of its own.</p>' if MASTER_DRAFT_LIVE else ''
    body = f'''<p class="eyebrow">One worked example for each critical infrastructure sector</p>
<h1>What we design against, and why it matters to you</h1>
<div class="prose">{sw}</div>
<figure><img src="assets/figures/nipp-to-life-happens.svg" alt="Diagram: the National Infrastructure Protection Plan defines sixteen sectors. The Foundational Definitions sit under all of them. Each sector framework leads to facility classes, which lead to use cases (what we postulate) and reference events (what happened), and to a progression from design basis to design basis accident to deliberate military action. Real events feed back to revise the design basis.">
<figcaption>From NIPP to Life Happens: how to read everything on this site. Each sector page shows one example of each layer.</figcaption></figure>
<h2 id="sectors">The sectors</h2>
<p class="prose">Choose a sector. Each page gives a one-line answer to “so what?”, the sectors it leans on and those that lean on it, and four cards: the sector framework, one facility class, one real event (observed) and one use case (postulated).</p>
<nav class="tree" aria-label="Sectors">{tree}</nav>
<h2>Four ways in</h2>
<ul class="prose">{readers}</ul>
<p class="prose">New to the idea? Start with <a href="design-basis.html">What is a design basis?</a></p>
{md}
<h2>Citing this site</h2>
<p class="prose">Cite the edition: T. Roxey, <em>{e(EDITION)}</em>, Eclectic Technologies, November 2026, <a href="https://doi.org/{VERSION_DOI}">https://doi.org/{VERSION_DOI}</a>. To cite the example set as it currently stands, across editions, use <a href="https://doi.org/{CONCEPT_DOI}">https://doi.org/{CONCEPT_DOI}</a>.</p>'''
    page('index.html', 'CIKR Design Basis Examples', body, 'One worked design basis example for each critical infrastructure sector: the sector framework, a facility class, a use case and a real event.')

def design_basis():
    p = PAGES['design_basis']
    paras = ''.join('<p>%s</p>' % inline(x) for x in p['body'])
    body = f'''<p class="eyebrow">The idea underneath every page</p>
<h1>What is a design basis?</h1>
<div class="prose">{''.join('<p>%s</p>' % inline(x) for x in p['intro'])}</div>
<figure><img src="assets/figures/design-basis-layers.svg" alt="Three layers side by side. Design basis: the function and its limits; success is delivering the function within limits. Design basis accident: accidents from experience; success is recovery, or a safe condition recovered with outside help. Deliberate military action: an adversary who chooses the moment, keeps coming, aims at what matters most and blocks help; success is reaching and holding a protected state with only what is at the facility. The function and the requirement to do it safely are kept through every layer. Conditions widen while the designs that meet them narrow.">
<figcaption>Simplified from Figure 1 of FD-DBL (<em>Design Basis Layers</em>), in <a href="https://doi.org/{FD_EDITION_DOI}">FD — Foundational Definitions, November 2026 Edition</a>. Where this picture and that text differ, the text governs.</figcaption></figure>
<div class="prose">{paras}</div>'''
    page('design-basis.html', 'What is a design basis? — CIKR Design Basis Examples', body, 'The three layers of design basis analysis in plain language.')

def readers():
    for k, v in READERS.items():
        qa = ''.join('<dt>%s</dt><dd>%s</dd>' % (inline(q['q']), ''.join('<p>%s</p>' % x for x in q['a'])) for q in v['qa'])
        body = f'''<p class="eyebrow">A path through the examples</p>
<h1>{e(v['title'])}</h1>
<p class="lede prose">{inline(v['intro'])}</p>
<p class="notice">This page is a guided path through material the site already shows. It is not regulatory guidance and not a compliance checklist.</p>
<dl class="qa">{qa}</dl>
<h2>Wanting more</h2>
<p class="prose">Fuller use cases and more detailed versions are released to defenders, regulators and researchers on request. See <a href="../request.html">Ask for more</a>.</p>'''
        page('readers/%s.html' % k, '%s — CIKR Design Basis Examples' % v['title'], body, v['blurb'])

def glossary():
    items = ''.join('<dt id="%s">%s</dt><dd>%s</dd>' % (k, e(v['term']), inline(v['def'])) for k, v in sorted(GLOSSARY.items(), key=lambda x: x[1]['term'].lower()))
    body = f'''<p class="eyebrow">Terms in plain language</p><h1>Glossary</h1>
<p class="prose">These are the terms the site uses, in plain language. A dotted underline anywhere on the site marks a term defined here; tap it to see the definition. The authoritative definitions are in the <a href="https://doi.org/{FD_EDITION_DOI}">Foundational Definitions</a>, and where the two differ, those govern.</p>
<dl class="gloss">{items}</dl>'''
    page('glossary.html', 'Glossary — CIKR Design Basis Examples', body, 'Plain-language definitions of the terms used on this site.', terms=False)

def request():
    paras = ''.join('<p>%s</p>' % x for x in PAGES['request'])
    body = f'<p class="eyebrow">For defenders, regulators and researchers</p><h1>Ask for more</h1><div class="prose">{paras}</div>'
    page('request.html', 'Ask for more — CIKR Design Basis Examples', body, 'How defenders, regulators and researchers can request fuller material.')

def master_draft():
    chapters = ''.join('<li><a href="sectors/%s.html">%s</a>: %s</li>' % (s, e(n), e(MASTER_DRAFT_CHAPTERS[s])) for s, n, _ in DATA if s in MASTER_DRAFT_CHAPTERS)
    paras = ''.join('<p>%s</p>' % x for x in PAGES['master_draft'])
    body = f'''<p class="eyebrow">The master draft</p><h1>Governing Generative AI in Critical Infrastructure Control</h1>
<div class="prose">{paras}<p>Cite it as <a href="https://doi.org/{MASTER_DRAFT_DOI}">doi:{MASTER_DRAFT_DOI}</a>.</p></div>
<h2>The sectors it reads</h2><ul class="prose">{chapters}</ul>'''
    page('master-draft.html', 'Master draft — CIKR Design Basis Examples', body, 'The master draft that reads the sector examples together.')

if __name__ == '__main__':
    for slug, name, d in DATA: sector_page(slug, name, d)
    home(); design_basis(); readers(); glossary(); request()
    if MASTER_DRAFT_LIVE: master_draft()
    elif os.path.exists(C('master-draft.html')): os.remove(C('master-draft.html'))
    print('built', len(DATA), 'sector pages')
