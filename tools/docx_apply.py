#!/usr/bin/env python3
"""Apply review changes imported by docx_import.py to an EA model (EA must be closed).

    python tools/docx_apply.py REVIEW.docx BASE.qea TARGET.qea [--changes changes/NAME.yaml] [--date YYYY-MM-DD]

Writes element names and notes, package notes, Status = Proposed and revised = date.
Word comments become EA maintenance items of the element: "TODO ..." → Task, everything else
unresolved → Issue (replies go into the notes). Entries with "apply: false" in the YAML are skipped;
new elements, connection changes and conflicts are left for manual work in EA.
"""
import sys, re, sqlite3, argparse, os
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx_import import run

def skipped(yaml_path):
    if not yaml_path or not os.path.exists(yaml_path): return set()
    s, out = open(yaml_path, encoding='utf8').read(), set()
    for blk in re.split(r'\n  - guid: ', s)[1:]:
        g = blk.split('\n', 1)[0].strip('"'); 
        if re.search(r'\n    apply: false', blk): out.add(g.upper())
    return out

def tag(c, oid, prop, val, note=None):
    r = c.execute("select PropertyID from t_objectproperties where Object_ID=? and Property=?", (oid, prop)).fetchone()
    if r: c.execute("update t_objectproperties set Value=? where PropertyID=?", (val, r[0]))
    else:
        import uuid
        c.execute("insert into t_objectproperties(Object_ID,Property,Value,Notes,ea_guid) values(?,?,?,?,?)",
                  (oid, prop, val, note, '{' + str(uuid.uuid4()).upper() + '}'))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('docx'); ap.add_argument('base'); ap.add_argument('target')
    ap.add_argument('--changes'); ap.add_argument('--date', default=str(date.today())); a = ap.parse_args()
    changes, unmapped, _ = run(a.docx, a.base, a.target)
    skip = skipped(a.changes)
    c = sqlite3.connect(a.target); n = dict(names=0, notes=0, packages=0, tasks=0, issues=0, manual=0, skipped=0)
    for ch in changes:
        g = ch.get('guid', '').upper()
        if ch['kind'] == 'new element' or ch.get('conflict') or g in skip: n['skipped' if g in skip else 'manual'] += 1; continue
        if 'manual' in ch.get('change', ''): n['manual'] += 1
        if ch['kind'] == 'package':
            pid = c.execute("select Package_ID from t_package where ea_guid=?", (ch['guid'],)).fetchone()[0]
            c.execute("update t_package set Notes=? where Package_ID=?", (ch['note_new'], pid))
            c.execute("update t_object set Note=? where Object_Type='Package' and PDATA1=?", (ch['note_new'], str(pid)))
            oid = c.execute("select Object_ID from t_object where Object_Type='Package' and PDATA1=?", (str(pid),)).fetchone()[0]
            n['packages'] += 1
        else:
            oid = c.execute("select Object_ID from t_object where ea_guid=?", (ch['guid'],)).fetchone()[0]
            if ch.get('name_new'): c.execute("update t_object set Name=? where Object_ID=?", (ch['name_new'], oid)); n['names'] += 1
            if ch.get('note_new') is not None: c.execute("update t_object set Note=? where Object_ID=?", (ch['note_new'], oid)); n['notes'] += 1
            if ch.get('name_new') or ch.get('note_new') is not None:
                c.execute("update t_object set Status='Proposed' where Object_ID=?", (oid,))
                tag(c, oid, 'revised', a.date, 'Date of the last approved change of the element.')
        for m in ch['comments']:
            if m['done']: continue
            todo = m['text'].upper().startswith('TODO')
            text = re.sub(r'^(TODO|ISSUE)\s*:?\s*', '', m['text'], flags=re.I) or m['text']
            notes = m['text'] + ''.join(f"\r\n{r['author']} ({r['date']}): {r['text']}" for r in m['replies'])
            c.execute("insert or replace into t_objectproblems(Object_ID,Problem,ProblemType,DateReported,Status,ProblemNotes,ReportedBy,Priority,Version) "
                      "values(?,?,?,?,?,?,?,?,?)", (oid, text[:250], 'Task' if todo else 'Issue', m['date'], 'New', notes, m['author'], 'Medium',
                                                   os.path.basename(a.docx)))
            n['tasks' if todo else 'issues'] += 1
    c.commit()
    print(', '.join(f'{k} {v}' for k, v in n.items()), f'| unmapped sections {len(unmapped)}')

if __name__ == '__main__':
    main()
