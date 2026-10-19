"""Compare two versions of the NRA model and write a Markdown change report.

Usage:
  python tools/diff.py OLD.qea NEW.qea [report.md]
  python tools/diff.py --git v2.1.0 [HEAD] [report.md]   # compares model/NRA.qea between git refs (needs git + git-lfs)

The report is grouped by view and uses the change types of the Change Protocol
(new object, title change, substantive/editorial description change, connection change, object deleted).
"""
import sys, os, subprocess, tempfile, difflib
sys.path.insert(0, os.path.dirname(__file__))
from nra_model import load, view_of

FIELDS = ('stereotype', 'alias', 'keywords', 'status', 'version', 'package')

def from_git(ref, path='model/NRA.qea'):
    blob = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True, check=True).stdout
    if blob.startswith(b'version https://git-lfs'):
        blob = subprocess.run(['git', 'lfs', 'smudge'], input=blob, capture_output=True, check=True).stdout
    f = tempfile.NamedTemporaryFile(suffix='.qea', delete=False); f.write(blob); f.close()
    return f.name

def word_diff(a, b, limit=600):
    sm = difflib.SequenceMatcher(None, a.split(), b.split())
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        old, new = ' '.join(a.split()[i1:i2]), ' '.join(b.split()[j1:j2])
        out.append(f'~~{old}~~ **{new}**' if old and new else (f'~~{old}~~' if old else f'**{new}**'))
    s = ' … '.join(out)
    return (s[:limit] + ' …') if len(s) > limit else s, sm.ratio()

def compare(old, new):
    rows = []  # (view, package, sort, markdown)
    oe, ne = old['elements'], new['elements']
    for g in sorted(set(oe) | set(ne)):
        a, b = oe.get(g), ne.get(g)
        e = b or a
        if e['type'] in ('Text', 'Boundary', 'Note'):
            continue
        view = view_of(e['package'])
        head = f'**{e["stereotype"] or e["type"]}** {e["name"]} `{g}`'
        if not a:
            rows.append((view, e['package'], e['name'], f'- {head} — *new object*'))
            continue
        if not b:
            rows.append((view, e['package'], e['name'], f'- {head} — *object deleted*'))
            continue
        kinds, det = [], []
        if a['name'] != b['name']:
            kinds.append('title change'); det.append(f'name: ~~{a["name"]}~~ → **{b["name"]}**')
        if a['note'] != b['note']:
            d, ratio = word_diff(a['note'], b['note'])
            kinds.append('substantive description change' if ratio < 0.9 else 'editorial description change')
            det.append(d or '(whitespace/formatting only)')
        for f in FIELDS:
            if a[f] != b[f]:
                kinds.append('metadata change'); det.append(f'{f}: `{a[f]}` → `{b[f]}`')
        if a['tags'] != b['tags']:
            ch = {k: (a['tags'].get(k), b['tags'].get(k)) for k in set(a['tags']) | set(b['tags']) if a['tags'].get(k) != b['tags'].get(k)}
            kinds.append('tagged value change'); det.append(', '.join(f'{k}: `{o}` → `{n}`' for k, (o, n) in sorted(ch.items())))
        if kinds:
            rows.append((view, e['package'], e['name'], f'- {head} — *{"; ".join(dict.fromkeys(kinds))}*\n' + ''.join(f'  - {x}\n' for x in det).rstrip('\n')))
    oc, nc = old['connectors'], new['connectors']
    for g in sorted(set(oc) | set(nc)):
        a, b = oc.get(g), nc.get(g)
        c = b or a
        src = ne.get(c['source']) or oe.get(c['source']) or {'package': ''}
        label = f'{c["source_name"]} → {c["target_name"]} ({c["type"]}{" «" + c["stereotype"] + "»" if c["stereotype"] else ""})'
        if not a:
            rows.append((view_of(src['package']), src['package'], c['source_name'], f'- connection added: {label}'))
        elif not b:
            rows.append((view_of(src['package']), src['package'], c['source_name'], f'- connection removed: {label}'))
        elif (a['source'], a['target'], a['type'], a['stereotype']) != (b['source'], b['target'], b['type'], b['stereotype']):
            olabel = f'{a["source_name"]} → {a["target_name"]} ({a["type"]}{" «" + a["stereotype"] + "»" if a["stereotype"] else ""})'
            rows.append((view_of(src['package']), src['package'], c['source_name'], f'- connection changed: ~~{olabel}~~ → **{label}**'))
    for n in sorted(set(old['templates']) | set(new['templates'])):
        a, b = old['templates'].get(n), new['templates'].get(n)
        if a != b:
            what = 'new' if not a else 'deleted' if not b else 'changed'
            rows.append(('Documentation templates', '', n, f'- template **{n}** {what}'))
    return rows

def report(rows, title):
    out = [f'# {title}', '']
    counts = {}
    for r in rows:
        counts[r[0]] = counts.get(r[0], 0) + 1
    out.append('| View | Changes |'); out.append('|---|---|')
    out += [f'| {v or "(root)"} | {n} |' for v, n in sorted(counts.items())]
    cur_v = cur_p = None
    for v, p, _, md in sorted(rows, key=lambda r: (r[0], r[1], r[2])):
        if v != cur_v:
            out += ['', f'## {v or "(root)"}']; cur_v = v; cur_p = None
        if p != cur_p and p:
            out += ['', f'### {p}']; cur_p = p
        out.append(md)
    return '\n'.join(out) + '\n'

def main(argv):
    if argv and argv[0] == '--git':
        base = argv[1]; head = argv[2] if len(argv) > 2 and not argv[2].endswith('.md') else None
        outp = next((x for x in argv[2:] if x.endswith('.md')), None)
        old_p = from_git(base)
        new_p = from_git(head) if head else 'model/NRA.qea'
        title = f'NRA model changes {base} → {head or "working copy"}'
    else:
        old_p, new_p = argv[0], argv[1]; outp = argv[2] if len(argv) > 2 else None
        title = f'NRA model changes {os.path.basename(old_p)} → {os.path.basename(new_p)}'
    md = report(compare(load(old_p), load(new_p)), title)
    if outp:
        open(outp, 'w', encoding='utf-8').write(md); print(f'written {outp}')
    else:
        sys.stdout.write(md)

if __name__ == '__main__':
    main(sys.argv[1:])
