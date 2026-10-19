"""Shared loader for the NRA Enterprise Architect model (.qea = SQLite)."""
import sqlite3, re, html, zipfile, io, base64

VOLATILE = {'ModifiedDate'}  # fields that change on every save and are not exported

def connect(path):
    c = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
    c.row_factory = sqlite3.Row
    return c

def plain(note):
    """EA notes are stored as light HTML; keep text readable and stable."""
    if not note:
        return ''
    t = note.replace('\r\n', '\n')
    t = re.sub(r'<li>', '- ', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return '\n'.join(l.rstrip() for l in t.split('\n')).strip()

def load(path):
    """Return a dict with packages, elements, connectors, diagrams, glossary, templates."""
    c = connect(path)
    pk = {r['Package_ID']: dict(r) for r in c.execute('select * from t_package')}
    def ppath(pid):
        parts = []
        while pid in pk and pk[pid]['Parent_ID'] != 0:
            parts.append(pk[pid]['Name']); pid = pk[pid]['Parent_ID']
        return '/'.join(reversed(parts))
    tags = {}
    for r in c.execute('select Object_ID, Property, Value from t_objectproperties'):
        tags.setdefault(r['Object_ID'], {})[r['Property']] = r['Value'] or ''
    objs = {}
    for r in c.execute('select * from t_object'):
        o = dict(r)
        objs[o['Object_ID']] = {
            'guid': o['ea_guid'], 'name': o['Name'] or '', 'type': o['Object_Type'],
            'stereotype': o['Stereotype'] or '', 'alias': o['Alias'] or '', 'keywords': o['PDATA5'] or '',
            'status': o['Status'] or '', 'version': o['Version'] or '', 'tpos': o['TPos'] or 0,
            'package': ppath(o['Package_ID']), 'note': plain(o['Note']),
            'tags': {k: v for k, v in sorted(tags.get(o['Object_ID'], {}).items())},
            'pdata1': o['PDATA1'],
        }
    cons = {}
    for r in c.execute('select * from t_connector'):
        s, t = objs.get(r['Start_Object_ID']), objs.get(r['End_Object_ID'])
        cons[r['ea_guid']] = {
            'guid': r['ea_guid'], 'type': r['Connector_Type'], 'stereotype': r['Stereotype'] or '',
            'source': s['guid'] if s else None, 'target': t['guid'] if t else None,
            'source_name': s['name'] if s else '?', 'target_name': t['name'] if t else '?',
            'name': r['Name'] or '', 'note': plain(r['Notes']),
        }
    diags = {}
    for r in c.execute('select * from t_diagram'):
        els = sorted(objs[d[0]]['name'] for d in c.execute('select Object_ID from t_diagramobjects where Diagram_ID=?', (r['Diagram_ID'],)) if d[0] in objs)
        diags[r['ea_guid']] = {'guid': r['ea_guid'], 'name': r['Name'], 'package': ppath(r['Package_ID']), 'type': r['Diagram_Type'], 'note': plain(r['Notes']), 'elements': els}
    gloss = {r['Term']: {'type': r['Type'], 'meaning': plain(r['Meaning'])} for r in c.execute('select * from t_glossary')}
    tmpl = {}
    for r in c.execute("select DocName, DocID, BinContent, Version from t_document where DocType='SSDOCSTYLE'"):
        try:
            s = zipfile.ZipFile(io.BytesIO(r['BinContent'])).read('str.dat').decode('utf-16le')
            m = re.search(r'<SSDocument\.Document[^>]*>(.*?)</SSDocument\.Document>', s, re.S)
            rtf = base64.b64decode(re.sub(r'\s', '', m.group(1))).decode('latin-1') if m else ''
            opts = re.search(r'<SSDocument\.Options ([^>]*)>', s)
            secs = re.findall(r'<SSDocument\.Section name="([^"]*)"[^>]*enabled="1"', s)
            body = rtf[rtf.find('Pkg_Begin}'):] if 'Pkg_Begin}' in rtf else rtf[-4000:]
            body = re.sub(r'\{\\\*\\bkmk(start|end) [^}]*\}', '', body)
            body = re.sub(r"\\'[0-9a-f]{2}", '', body); body = re.sub(r'\\[a-z]+-?\d* ?', '', body); body = re.sub(r'[{}]', '', body)
            text = ' '.join(body.split())
            tmpl[r['DocName']] = {'id': r['DocID'], 'kind': {2: 'cover', 3: 'stylesheet', 4: 'toc'}.get(r['Version'], 'template/fragment'),
                                  'options': opts.group(1) if opts else '', 'sections': secs, 'content': text}
        except Exception as e:
            tmpl[r['DocName']] = {'id': r['DocID'], 'error': str(e)}
    return {'packages': {pid: ppath(pid) for pid in pk}, 'elements': {o['guid']: o for o in objs.values()},
            'connectors': cons, 'diagrams': diags, 'glossary': gloss, 'templates': tmpl}

def view_of(package_path):
    """Top-level grouping used in reports, e.g. 'NAP Organisational View' or 'Supplements'."""
    parts = package_path.split('/')
    return parts[1] if len(parts) > 1 else (parts[0] if parts else '')
