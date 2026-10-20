#!/usr/bin/env python3
"""Apply review changes imported by docx_import.py to an EA model (EA must be closed).

    python tools/docx_apply.py REVIEW.docx BASE.qea TARGET.qea [--changes changes/NAME.yaml]
                               [--date YYYY-MM-DD] [--since X.Y.Z] [--author NAME]

Applied automatically (entries with apply: true):
  - names and notes of existing elements, package descriptions; Status = Proposed, revised = date
  - new elements: created from an element with the same Keywords (stereotype, type), Status = Proposed,
    revised/since; every connection the element still needs becomes an EA task (Maintenance tab)
Recorded but not applied (WIP, proposals incl. changes by Claude, conflicts, apply: false):
  - an EA task "Pending review proposal" on the element with the proposed text in its notes
Comments: "TODO" → task, "ISSUE"/other unresolved → issue, "WIP"/"PROPOSAL" → task, "DELETE" → removal task;
replies go into the notes.
Lint warnings of the import → issue "Review import warning". Connection changes stay manual (see the report).
"""
import sys, re, sqlite3, argparse, os, uuid
from datetime import date, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_import import run, plain_lines, ckind

G = lambda: '{' + str(uuid.uuid4()).upper() + '}'

def apply_flags(yaml_path):
    """guid/name → apply flag as edited by the user in the YAML."""
    if not yaml_path or not os.path.exists(yaml_path): return {}
    out = {}
    for blk in re.split(r'\n  - guid: ', open(yaml_path, encoding='utf8').read())[1:]:
        g = blk.split('\n', 1)[0].strip('"'); o = re.search(r'\n    object: "(.*)"', blk)
        m = re.search(r'\n    apply: (true|false)', blk)
        if m: out[(g or (o.group(1) if o else '')).upper()] = m.group(1) == 'true'
    return out

def tag(c, oid, prop, val, note=None):
    r = c.execute("select PropertyID from t_objectproperties where Object_ID=? and Property=?", (oid, prop)).fetchone()
    if r: c.execute("update t_objectproperties set Value=? where PropertyID=?", (val, r[0]))
    else: c.execute("insert into t_objectproperties(Object_ID,Property,Value,Notes,ea_guid) values(?,?,?,?,?)", (oid, prop, val, note, G()))

def item(c, oid, kind, title, notes, who, when, src):
    c.execute("insert or replace into t_objectproblems(Object_ID,Problem,ProblemType,DateReported,Status,ProblemNotes,ReportedBy,Priority,Version) "
              "values(?,?,?,?,?,?,?,?,?)", (oid, title[:250], kind, when, 'New', notes, who, 'Medium', src))

def create(c, ch, a):
    kw = ch.get('keyword', '')
    tpl = c.execute("select Object_ID, Package_ID, ea_guid from t_object where lower(PDATA5)=lower(?) order by Object_ID desc", (kw,)).fetchall()
    if not tpl: return None, f'no element with Keywords “{kw}” to copy from'
    pid = None
    if ch.get('package_guid'):
        r = c.execute("select Package_ID from t_package where ea_guid=?", (ch['package_guid'],)).fetchone()
        if r and c.execute("select count(*) from t_object where Package_ID=? and lower(PDATA5)=lower(?)", (r[0], kw)).fetchone()[0]: pid = r[0]
    if pid is None:  # package holding most elements of this kind
        pid = c.execute("select Package_ID from t_object where lower(PDATA5)=lower(?) group by Package_ID order by count(*) desc", (kw,)).fetchone()[0]
    if c.execute("select count(*) from t_object where Package_ID=? and Name=?", (pid, ch['name'])).fetchone()[0]:
        return None, 'an element with this name already exists in the target package'
    cols = [r[1] for r in c.execute("pragma table_info(t_object)")]
    row = dict(zip(cols, c.execute("select * from t_object where Object_ID=?", (tpl[0][0],)).fetchone()))
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S'); g = G()
    row.pop('Object_ID')
    row.update(Name=ch['name'], Alias=None, Note=ch.get('text') or '', Package_ID=pid, ea_guid=g, Status='Proposed', Backcolor=-1,
               CreatedDate=now, ModifiedDate=now, Author=a.author, Version='1.0', Classifier=0, ParentID=0,
               TPos=(c.execute("select max(TPos) from t_object where Package_ID=?", (pid,)).fetchone()[0] or 0) + 1)
    c.execute(f"insert into t_object({','.join(chr(34) + k + chr(34) for k in row)}) values({','.join('?' * len(row))})", list(row.values()))
    oid = c.execute("select Object_ID from t_object where ea_guid=?", (g,)).fetchone()[0]
    xr = c.execute("select * from t_xref where Client=? and Name='Stereotypes'", (tpl[0][2],)).fetchone()
    if xr:
        xc = [r[1] for r in c.execute("pragma table_info(t_xref)")]; d = dict(zip(xc, xr)); d['XrefID'] = G(); d['Client'] = g
        c.execute(f"insert into t_xref({','.join(chr(34) + k + chr(34) for k in d)}) values({','.join('?' * len(d))})", list(d.values()))
    tag(c, oid, 'revised', a.date, 'Date of the last approved change of the element.')
    if a.since: tag(c, oid, 'since', a.since)
    if kw.lower() == 'low level function': tag(c, oid, 'RequirementLevel', 'MANDATORY')
    hint = ('Candidate links: ' + '; '.join(ch['mentions'])) if ch.get('mentions') else ''
    for r in ch.get('required', []):
        item(c, oid, 'Task', 'Missing: ' + r, hint, a.author, a.date, os.path.basename(a.docx))
    return oid, None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('docx'); ap.add_argument('base'); ap.add_argument('target')
    ap.add_argument('--changes'); ap.add_argument('--date', default=str(date.today())); ap.add_argument('--since')
    ap.add_argument('--author', default='Review import'); a = ap.parse_args()
    changes, unmapped, _ = run(a.docx, a.base, a.target)
    flags = apply_flags(a.changes); src = os.path.basename(a.docx)
    c = sqlite3.connect(a.target)
    n = dict(names=0, notes=0, packages=0, created=0, pending=0, tasks=0, issues=0, warnings=0, manual=0)
    for ch in changes:
        key = (ch.get('guid') or ch.get('name', '')).upper()
        do = flags.get(key, ch.get('apply', True))
        oid = None
        if ch['kind'] == 'new element':
            if do:
                oid, err = create(c, ch, a)
                if oid: n['created'] += 1
                else: n['manual'] += 1; print('  manual:', ch['name'], '–', err)
            else: n['pending'] += 1; print('  not created (', ', '.join(ch.get('flags', [])) or 'apply: false', '):', ch['name'])
        elif ch['kind'] == 'package':
            pid = c.execute("select Package_ID from t_package where ea_guid=?", (ch['guid'],)).fetchone()[0]
            oid = c.execute("select Object_ID from t_object where Object_Type='Package' and PDATA1=?", (str(pid),)).fetchone()[0]
            if do:
                c.execute("update t_package set Notes=? where Package_ID=?", (ch['note_new'], pid))
                c.execute("update t_object set Note=? where Object_ID=?", (ch['note_new'], oid)); n['packages'] += 1
        else:
            oid = c.execute("select Object_ID from t_object where ea_guid=?", (ch['guid'],)).fetchone()[0]
            if 'manual' in ch.get('change', ''): n['manual'] += 1
            if do and (ch.get('name_new') or ch.get('note_new') is not None):
                if ch.get('name_new'): c.execute("update t_object set Name=? where Object_ID=?", (ch['name_new'], oid)); n['names'] += 1
                if ch.get('note_new') is not None: c.execute("update t_object set Note=? where Object_ID=?", (ch['note_new'], oid)); n['notes'] += 1
                c.execute("update t_object set Status='Proposed' where Object_ID=?", (oid,))
                tag(c, oid, 'revised', a.date, 'Date of the last approved change of the element.')
            elif not do and (ch.get('name_new') or ch.get('note_new') is not None):
                why = ', '.join(ch.get('flags', [])) or ch.get('conflict') or 'apply: false'
                txt = (f"New name: {ch['name_new']}\r\n" if ch.get('name_new') else '') + '\r\n'.join(plain_lines(ch.get('note_new') or ''))
                item(c, oid, 'Task', f'Pending review proposal ({why})', txt, ', '.join(ch.get('authors', [])) or a.author, a.date, src)
                n['pending'] += 1
        if not oid: continue
        if 'object deleted' in ch.get('change', ''):
            item(c, oid, 'Task', 'Remove element (deleted in review) – follow the deprecation rules of Guideline 06', '', ', '.join(ch.get('authors', [])) or a.author, a.date, src)
            n['tasks'] += 1
        for m in ch['comments']:
            if m['done']: continue
            k = ckind(m['text'])
            if k == 'delete': continue  # handled as removal task above
            text = re.sub(r'^(TODO|ISSUE|WIP|DRAFT|PROPOSAL)\s*:?\s*', '', m['text'], flags=re.I) or m['text']
            notes = m['text'] + ''.join(f"\r\n{r['author']} ({r['date']}): {r['text']}" for r in m['replies'])
            kind = 'Issue' if k in ('issue', 'comment') else 'Task'
            item(c, oid, kind, text, notes, m['author'], m['date'], src); n['tasks' if kind == 'Task' else 'issues'] += 1
        for w in ch.get('warnings', []):
            item(c, oid, 'Issue', 'Review import warning: ' + w, '', a.author, a.date, src); n['warnings'] += 1
    c.commit()
    print(', '.join(f'{k} {v}' for k, v in n.items()), f'| unmapped sections {len(unmapped)}')

if __name__ == '__main__':
    main()
