"""Build the CIKR Design Basis Examples site from content/ into static HTML at the repo root.
Run from the repo root:  python3 tools/build.py
"""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = lambda *p: os.path.join(ROOT, *p)

# ---- configuration -------------------------------------------------------
EDITION = 'CIKR Design Basis Examples, Edition 2 (November 2026)'
EDITION_DATE = '21 November 2026'
# The four Edition 2 records. Fill each version DOI when Zenodo reserves it; the build marks
# the site "DOIs pending" and FINAL refuses to build until every one is filled.
VERSION_DOI = '10.5281/zenodo.24427984'                              # Edition 1 record, version 2 (frameworks and classes)
CONCEPT_DOI = '10.5281/zenodo.23863985'
EDITION1_VERSION_DOI = '10.5281/zenodo.23863986'
COLLECTIONS = {   # name -> slug, concept DOI, version DOI for this edition
 'Lifelines': {'slug': 'lifelines', 'concept': '10.5281/zenodo.24428020', 'version': '10.5281/zenodo.24428021'},
 'Public Safety and Government': {'slug': 'public-safety-and-government', 'concept': '10.5281/zenodo.24428030', 'version': '10.5281/zenodo.24428031'},
 'Industry and Economy': {'slug': 'industry-and-economy', 'concept': '10.5281/zenodo.24428037', 'version': '10.5281/zenodo.24428038'},
}
FINAL = True     # True only for the build pushed after Zenodo publishes
FD_EDITION_DOI = '10.5281/zenodo.23401272'   # FD, November 2026 Edition (carries FD-DBL)
SCRM_DOI = '10.5281/zenodo.21365261'
PDF_BASE = 'https://scubanuke.github.io/publications/cikr/edition-2/'
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
        meta = {}
        if m.group(1) == 'Reference event':   # date and tier feed the cross-sector index
            for key in ('Date', 'Tier'):
                mm = re.match(r'\*\*%s:\*\* (.+)\n' % key, body); assert mm, (path, key)
                meta[key.lower()] = mm.group(1).strip(); body = body[mm.end():]
        d['cards'].append({**meta, 'kind': m.group(1), 'title': m.group(2).strip(), 'des': m.group(3).strip(),
                           'body': body.replace(ON_REQUEST, '').strip(), 'onreq': ON_REQUEST in body,
                           'src': m.group(5).strip()})
    assert len(d['cards']) == 4, path
    return d

GLOSSARY = json.load(open(C('content', 'glossary.json'), encoding='utf-8'))
# Terms shared across the sites are defined once, in the Foundational Definitions glossary
# (scubanuke/foundational-definitions, glossary.json). An entry here that carries "fd" takes its
# definition from there at build time, so the foundational-definitions repo must be checked out
# beside this one. Nothing is restated here.
FD_GLOSSARY_URL = 'https://scubanuke.github.io/foundational-definitions/#/glossary'
FD_GLOSSARY = {t['id']: t for t in json.load(open(os.path.join(ROOT, '..', 'foundational-definitions', 'glossary.json'), encoding='utf-8'))['terms']}
for _k, _v in GLOSSARY.items():
    if 'fd' in _v:
        _v['def'] = FD_GLOSSARY[_v['fd']]['def']
FC = json.load(open(C('content', 'facility_classes.json'), encoding='utf-8'))['sectors']
READERS = json.load(open(C('content', 'readers.json'), encoding='utf-8'))
PAGES = json.load(open(C('content', 'pages.json'), encoding='utf-8'))
DESIGN = json.load(open(C('content', 'design_lines.json'), encoding='utf-8'))
DATA = [(slug, name, parse_card(C('content', 'cards', f))) for f, slug, name in SECTORS]
EVENTS = json.load(open(C('content', 'register', 'events.json'), encoding='utf-8'))
TIERS = json.load(open(C('content', 'register', 'tiers.json'), encoding='utf-8'))
for _ev in EVENTS: _ev['tier_label'] = TIERS[_ev['des']]['tier']
EV = {x['des']: x for x in EVENTS}
SNAME = {s: n for f, s, n in SECTORS}
_missing = [k for k, v in COLLECTIONS.items() if not v['version'] or not v['concept']] + ([] if VERSION_DOI else ['Edition record'])
if FINAL: assert not _missing, ('DOIs not filled', _missing)
def doi(d): return '<a href="https://doi.org/%s">doi:%s</a>' % (d, d) if d else '<span class="note">DOI pending</span>'
def re_pdf(x): return '%s%s' % (PDF_BASE, x['pdf'])   # the mirror is flat, as Edition 1's was
def re_page(x): return 'events/%s.html' % x['des'].lower()

# ---- layout --------------------------------------------------------------
# Eclectic Technologies cross-site switcher: the same block carried by all eight sites.
ET_SWITCHER = '''<!-- Eclectic Technologies site switcher -->
<style>
.etnav{background:#0A1628;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:14px;line-height:1.4;border-bottom:1px solid #24344a;}
.etnav__in{max-width:1080px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:9px 20px;}
.etnav__brand{font-weight:700;letter-spacing:.02em;color:#f0f4f8;text-decoration:none;white-space:nowrap;}
.etnav__brand span{color:#C8893A;}
.etnav__links{display:flex;gap:4px;flex-wrap:wrap;}
.etnav__links a{color:#c3d0df;text-decoration:none;padding:5px 12px;border-radius:6px;font-weight:600;}
.etnav__links a:hover{background:#1a2b42;color:#fff;}
.etnav__links a[aria-current="page"]{background:#C8893A;color:#0A1628;}
</style>
<nav class="etnav" aria-label="Eclectic Technologies sites">
  <div class="etnav__in">
    <a class="etnav__brand" href="https://scubanuke.github.io/publications/">Eclectic <span>Technologies</span></a>
    <div class="etnav__links">
      <a href="https://scubanuke.github.io/ai-governance-course/">Course</a>
      <a href="https://scubanuke.github.io/foundational-definitions/">Foundational Definitions</a>
      <a href="https://scubanuke.github.io/cikr-design-basis/" aria-current="page">CIKR Examples</a>
      <a href="https://scubanuke.github.io/dba-en-navigation/">Energy Series</a>
      <a href="https://scubanuke.github.io/command-broker/">Command Broker</a>
      <a href="https://scubanuke.github.io/smr-licensing/">SMR Licensing</a>
      <a href="https://scubanuke.github.io/publications/">Publications</a>
    </div>
  </div>
</nav>'''

NAV = [('index.html','Sectors'),('reference-events.html','Reference events'),('design-basis.html','What is a design basis?'),('readers/public.html','For the public'),
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
{ET_SWITCHER}
{banner}
<header class="top"><div class="in">
<a class="brand" href="{r}index.html"><span class="eyebrow">Eclectic Technologies</span><span class="name">CIKR Design Basis Examples</span></a>
<nav aria-label="Site">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="in">
<p>Every document linked from this site is frozen in <em>{e(EDITION)}</em>, as it stood on {EDITION_DATE}: the sector frameworks and facility classes in the edition record ({doi(VERSION_DOI)}), and the reference events in three collections, Lifelines, Public Safety and Government, and Industry and Economy. Each is a working draft, marked DRAFT on its cover. The working documents continue to change, and later editions will record them. <a href="https://doi.org/{EDITION1_VERSION_DOI}">Edition 1</a> stays citable for what it contains.</p>
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

MONTHS = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
def date_key(t):
    y = re.search(r'(1[89]|20)\d\d', t).group(0)
    m = re.search(r'\b(%s)' % '|'.join(MONTHS), t.lower())
    dd = re.match(r'(?:from (?:about )?|at least )?(\d{1,2})\b', t)
    return (y, MONTHS.index(m.group(1)) if m else -1, int(dd.group(1)) if dd else 0)

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
        elif k == 're':
            x = EV[c['des']]
            foot = '<a href="%s%s">The event, its findings and what owners can do →</a><br><a href="%s">Read the frozen public edition (PDF) →</a><br><span class="note">Frozen in Edition 2, %s · %s collection · %s</span>' % (r, re_page(x), re_pdf(x), EDITION_DATE, e(x['collection']), doi(COLLECTIONS[x['collection']]['version']))
        else:
            foot = '<a href="%s%s.pdf">Read the frozen document (PDF) →</a><br><span class="note">Frozen in Edition 2, %s · %s</span>' % (PDF_BASE, e(c['src']), EDITION_DATE, doi(VERSION_DOI))
        cards.append(f'''<article class="card {k}" id="{e(c['des'].lower())}">
<span class="kind">{e(label)}</span>
<h3>{e(c['title'])}</h3><p class="des">{e(c['des'])}</p>
<p>{inline(c['body'])}</p>
<div class="foot">{foot}</div>
</article>''')
    extra = ''
    if slug == 'energy':
        extra = f'<p class="prose">Energy is one sector with three subsectors: electric power, natural gas and petroleum. The edition also freezes the <a href="{PDF_BASE}DBA-GAS-Sector_Framework_v1_16.pdf">Natural Gas Sector Framework</a> (DBA-GAS-Sector_Framework, version 1.16), under which the facility class and the reference event shown here sit.</p>'
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
    design = ''
    dl = DESIGN['lines'].get(slug)
    if dl and not dl.get('hold'):
        retitle = [c['title'] for c in d['cards'] if KIND[c['kind']] == 're'][0]
        design = '<section class="design"><h2>What it means for the design</h2><p class="note">%s</p><p class="prose">%s %s</p><p class="note">From the findings of <em>%s</em> (%s).</p></section>' % (e(DESIGN['intro']), inline(dl['t']), inline(dl['c']), e(retitle), e(dl['f']))
    sevs = sorted([x for x in EVENTS if x['sector'] == slug], key=lambda x: date_key(x['date']), reverse=True)
    feat = [c['des'] for c in d['cards'] if KIND[c['kind']] == 're'][0]
    lis = ''.join('<li><a href="%s%s">%s</a>%s <span class="st">— %s · %s</span></li>' % (r, re_page(x), e(x['title']), ' <span class="note">(shown above)</span>' if x['des'] == feat else '', e(x['date']), e(x['tier_label'])) for x in sevs)
    register = '<section class="others" id="register"><h2>Every reference event in this sector</h2><p class="note">Newest first. Each opens to a page of its own, with what happened, the tier, each finding in a line, the annex for asset owners, and the frozen public edition.</p><ul>%s</ul></section>' % lis
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
{design}
{register}
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
<p class="prose">Cite the edition: T. Roxey, <em>{e(EDITION)}</em>, Eclectic Technologies, November 2026, {doi(VERSION_DOI)}. To cite the example set as it currently stands, across editions, use <a href="https://doi.org/{CONCEPT_DOI}">doi:{CONCEPT_DOI}</a>. A reference event is cited by its collection's DOI, given on the event's own page.</p>'''
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

TIER_ORDER = ['Military-action tier met', 'Military action, tier not established', 'Adversarial, not military action', 'No adversary established']
def reference_events():
    rows = sorted(EVENTS, key=lambda x: (date_key(x['date']), x['des']))
    trs = ''.join('<tr data-date="%s" data-tier="%d"><td><a href="%s">%s</a><br><span class="note">%s</span></td><td><a href="sectors/%s.html">%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>'
                  % ('%s-%02d-%02d' % (lambda k: (k[0], k[1] + 1, k[2]))(date_key(x['date'])), TIER_ORDER.index(x['tier_label']), re_page(x), e(x['title']), e(x['des']), x['sector'], e(SNAME[x['sector']]), e(x['collection']), e(x['date']), e(x['tier_label'])) for x in rows)
    body = f'''<p class="eyebrow">Observed events, all sectors</p><h1>The reference event register</h1>
<p class="prose">A reference event reads a real event back through the design basis to ask whether the method was sufficient. This register lists every reference event in <em>{e(EDITION)}</em>: {len(EVENTS)} events across fifteen sectors, oldest first. Select a column heading to sort by it. Each event opens to a page of its own with what happened, the tier, each finding in a line, the annex written for asset owners, and the frozen public edition with its DOI. Nuclear events join at the edition nuclear enters the site.</p>
<p class="prose note">The tier is the instrument's reading of whether the event shows all four marks of deliberate military action: intentionality, persistence, precision and denial. It is not a finding of who acted.</p>
<div class="tablewrap"><table class="reidx sortable"><thead><tr><th data-k="0">Event</th><th data-k="1">Sector</th><th data-k="2">Collection</th><th data-k="date">Date</th><th data-k="tier">Tier</th></tr></thead><tbody>{trs}</tbody></table></div>
<script>
document.querySelectorAll('table.sortable th').forEach(function(th){{th.style.cursor='pointer';th.addEventListener('click',function(){{
 var tb=th.closest('table').tBodies[0],k=th.dataset.k,rows=[].slice.call(tb.rows),asc=th.dataset.asc!=='1';
 rows.sort(function(a,b){{var x,y;if(k==='date'){{x=a.dataset.date;y=b.dataset.date}}else if(k==='tier'){{x=+a.dataset.tier;y=+b.dataset.tier;return asc?x-y:y-x}}else{{x=a.cells[+k].textContent;y=b.cells[+k].textContent}}return asc?x.localeCompare(y):y.localeCompare(x)}});
 rows.forEach(function(r){{tb.appendChild(r)}});th.closest('tr').querySelectorAll('th').forEach(function(h){{delete h.dataset.asc}});th.dataset.asc=asc?'1':'0';}});}});
</script>'''
    page('reference-events.html', 'Reference event register — CIKR Design Basis Examples', body, 'Every reference event in the edition, across fifteen sectors, with its date, collection and tier.')

STUB_NOTE = 'One section of this document is withheld from the public edition and is available to defenders and regulators on request.'
def annex_html(blocks):
    out = []
    for b in blocks:
        if 'h2' in b: out.append('<h3>%s</h3>' % e(b['h2']))
        elif 'h3' in b: out.append('<h4>%s</h4>' % e(b['h3']))
        elif 'p' in b: out.append('<p>%s</p>' % e(b['p']))
        elif 'table' in b:
            head, *rest = b['table']
            out.append('<div class="tablewrap"><table class="reidx"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (''.join('<th>%s</th>' % e(c) for c in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % e(c) for c in row) for row in rest)))
    return ''.join(out)
def event_pages():
    for x in EVENTS:
        r = '../'; col = COLLECTIONS[x['collection']]
        what = ''.join('<p>%s</p>' % e(p) for p in x['what'])
        fl = ''.join('<li><strong>%s, %s</strong> %s</li>' % (e(f['id']), e(f['title']), e(f['text'])) for f in x['findings'])
        imp = '<p class="note">Impacted sector: %s</p>' % e(x['impacted']) if x['impacted'] else ''
        wh = '<p class="notice">%s <a href="%srequest.html">Ask for more</a>.</p>' % (STUB_NOTE, r) if x['withholds'] else ''
        cite = 'T. Roxey, <em>%s</em> (%s), version %s, Public Edition, in <em>CIKR Design Basis Reference Events: %s, Edition 2 (November 2026)</em>, Eclectic Technologies, November 2026, %s.' % (e(x['title']), e(x['des']), e(x['version']), e(x['collection']), doi(col['version']))
        body = f'''<p class="eyebrow"><a href="{r}sectors/{x['sector']}.html">{e(SNAME[x['sector']])}</a> · Reference event · {e(x['des'])}</p>
<h1>{e(x['title'])}</h1>
<p class="note">Event date: {e(x['date_full'])} · Read from instrument version {e(x['version'])} · {e(x['collection'])} collection</p>
{imp}
<h2>What happened</h2><div class="prose">{what}</div>
<h2>Tier</h2><p class="prose"><strong>{e(x['tier_label'])}.</strong> {e(x['tier'])}</p>
<h2>Findings</h2><ul class="prose findings">{fl}</ul>
<h2>For asset owners</h2><p class="prose note">Annex A of the instrument, in full. It is written for owners and operators, and it states no requirement.</p>
<div class="prose annex">{annex_html(x['annex'])}</div>
<h2>The frozen document</h2>
{wh}
<p class="prose"><a href="{re_pdf(x)}">Read the frozen public edition (PDF) →</a></p>
<p class="prose note">Cite as: {cite}</p>
<p class="prose"><a href="{r}reference-events.html">All reference events →</a></p>'''
        page(re_page(x), '%s — CIKR Design Basis Examples' % x['title'], body, ' '.join(x['what'])[:200])

def glossary():
    items = ''.join('<dt id="%s">%s</dt><dd>%s%s</dd>' % (k, e(v['term']), inline(v['def']), ' <span class="note">From the <a href="%s">Foundational Definitions glossary</a>.</span>' % FD_GLOSSARY_URL if 'fd' in v else '') for k, v in sorted(GLOSSARY.items(), key=lambda x: x[1]['term'].lower()))
    body = f'''<p class="eyebrow">Terms in plain language</p><h1>Glossary</h1>
<p class="prose">These are the terms the site uses, in plain language. A dotted underline anywhere on the site marks a term defined here; tap it to see the definition. Terms shared with the other Eclectic Technologies sites come from the <a href="{FD_GLOSSARY_URL}">Foundational Definitions glossary</a>, where they are defined once. The authoritative definitions are in the <a href="https://doi.org/{FD_EDITION_DOI}">Foundational Definitions</a>, and where the two differ, those govern.</p>
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
    home(); design_basis(); readers(); reference_events(); event_pages(); glossary(); request()
    if _missing: print('DOIs pending:', ', '.join(_missing))
    if MASTER_DRAFT_LIVE: master_draft()
    elif os.path.exists(C('master-draft.html')): os.remove(C('master-draft.html'))
    print('built', len(DATA), 'sector pages')
