"""Extract the reference event register for an edition from Project 11's frozen files.

Usage (from the repo root):
  python3 tools/extract_register.py <Projects folder> <edition manifest data JSON>

Reads, for each reference event in the manifest data, its register card
(Register Cards/<designator>_Register_Card.md) and Annex A of its public edition,
and writes content/register/events.json. The site build reads only that file, so
the repository stays self-contained. Run once per edition, at the freeze.
"""
import sys, os, re, json
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

SLUG = {'W': 'water', 'COMM': 'communications', 'CHEM': 'chemical', 'TRAN': 'transportation',
        'ESS': 'emergency-services', 'DAMS': 'dams', 'HPH': 'healthcare', 'IT': 'information-technology',
        'FIN': 'financial-services', 'FA': 'food-and-agriculture', 'CM': 'critical-manufacturing',
        'DIB': 'defense-industrial-base', 'GF': 'government-facilities', 'CF': 'commercial-facilities', 'GAS': 'energy', 'ES': 'energy', 'OIL': 'energy'}

def card(path):
    s = open(path, encoding='utf-8').read()
    title = re.search(r'^# (.+)$', s, re.M).group(1).strip()
    meta = s.split('\n')[2]
    dm = re.search(r'Event dates?: (.+?)(?: · |$)', meta)
    date_full = dm.group(1).strip()
    date_short = re.split(r' \(|, read ', date_full)[0].strip()
    imp = re.search(r'Impacted sectors?: (.+?) · ', meta)
    def sect(name):
        m = re.search(r'^## %s\n\n(.+?)(?=\n## |\Z)' % name, s, re.S | re.M)
        return m.group(1).strip() if m else ''
    findings = [dict(zip(('id', 'title', 'text'), m.groups())) for m in
                re.finditer(r'^\*\*(F-\d+), (.+?)\*\* ?(.*)$', sect('Findings'), re.M)]
    return dict(title=title, date=date_short, date_full=date_full, impacted=imp.group(1) if imp else '',
                what=[p.strip() for p in sect('What Happened').split('\n\n') if p.strip()],
                tier=sect('Tier'), findings=findings)

def annex(path):
    d = docx.Document(path); blocks = []; on = False
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            p = Paragraph(el, d); st = p.style.name; t = p.text.strip()
            if st == 'Heading 1':
                if on: break
                on = t.startswith('Annex A'); continue
            if not on or not t: continue
            if st == 'Heading 2': blocks.append({'h2': t})
            elif st == 'Heading 3': blocks.append({'h3': t})
            else: blocks.append({'p': t})
        elif tag == 'tbl' and on:
            rows = [[c.text.strip() for c in r.cells] for r in Table(el, d).rows]
            blocks.append({'table': rows})
    assert blocks and 'h2' in blocks[0], path
    return blocks

def main(projects, data):
    out = []
    cards = os.path.join(projects, 'Temporary folder Project 11 - DBA Reference Events', 'Register Cards')
    for o in json.load(open(data, encoding='utf-8')):
        des = o['d']; pre = des.split('-')[1]
        c = card(os.path.join(cards, des + '_Register_Card.md'))
        pe = os.path.join(projects, o['dir'], o['pe'])
        assert ('version ' + o['ver'].split()[0].lstrip('v')) in open(os.path.join(cards, des + '_Register_Card.md'), encoding='utf-8').read().split('\n')[2], des
        out.append(dict(des=des, sector=SLUG[pre], collection=o['coll'], version=o['ver'].split()[0].lstrip('v'),
                        pdf=o['pe'][:-5] + '.pdf', withholds=o['nstub'] > 0, **c, annex=annex(pe)))
    os.makedirs('content/register', exist_ok=True)
    json.dump(out, open('content/register/events.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'events written')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
