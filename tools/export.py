"""Export the NRA model to readable, diff-friendly YAML files.

Usage:  python tools/export.py [model/NRA.qea] [export]
Every package becomes one YAML file; templates, diagrams and the glossary get their own files.
Only stable content is exported (no modification timestamps), so git diffs show real changes.
"""
import sys, os, json, shutil, re
sys.path.insert(0, os.path.dirname(__file__))
from nra_model import load

def q(s):
    return json.dumps(s, ensure_ascii=False)

def block(key, text, ind):
    if not text:
        return f'{ind}{key}: ""\n'
    lines = text.split('\n')
    return f'{ind}{key}: |\n' + ''.join(f'{ind}  {l}\n' for l in lines)

def safe(p):
    return re.sub(r'[<>:"\\|?*]', '_', p)

def main(model='model/NRA.qea', out='export'):
    m = load(model)
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    by_pkg = {}
    for e in m['elements'].values():
        if e['type'] == 'Package':
            continue
        by_pkg.setdefault(e['package'], []).append(e)
    outgoing = {}
    for c in m['connectors'].values():
        outgoing.setdefault(c['source'], []).append(c)
    pkg_info = {e['package'] + '/' + e['name']: e for e in m['elements'].values() if e['type'] == 'Package'}
    for path in sorted(set(m['packages'].values()) | set(by_pkg)):
        if not path:
            continue
        fn = os.path.join(out, 'model', *[safe(p) for p in path.split('/')]) + '.yaml'
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        info = pkg_info.get(path, {})
        s = f'package: {q(path)}\n'
        if info:
            s += f'guid: {q(info["guid"])}\nalias: {q(info["alias"])}\nversion: {q(info["version"])}\n' + block('note', info['note'], '')
            if info['tags']:
                s += 'tags:\n' + ''.join(f'  {q(k)}: {q(v)}\n' for k, v in info['tags'].items())
        s += 'elements:\n' if by_pkg.get(path) else 'elements: []\n'
        for e in sorted(by_pkg.get(path, []), key=lambda e: (e['tpos'], e['name'], e['guid'])):
            s += f'  - name: {q(e["name"])}\n    guid: {q(e["guid"])}\n    type: {q(e["type"])}\n'
            for k in ('stereotype', 'alias', 'keywords', 'status', 'version'):
                if e[k]:
                    s += f'    {k}: {q(e[k])}\n'
            s += f'    order: {e["tpos"]}\n'
            if e['tags']:
                s += '    tags:\n' + ''.join(f'      {q(k)}: {q(v)}\n' for k, v in e['tags'].items())
            s += block('note', e['note'], '    ')
            links = sorted(outgoing.get(e['guid'], []), key=lambda c: (c['type'], c['stereotype'], c['target_name'], c['guid']))
            if links:
                s += '    links:\n'
                for c in links:
                    st = f' «{c["stereotype"]}»' if c['stereotype'] else ''
                    s += f'      - {q(c["type"] + st + " → " + c["target_name"])}  # {c["guid"]} → {c["target"]}\n'
        with open(fn, 'w', encoding='utf-8', newline='\n') as f:
            f.write(s)
    with open(os.path.join(out, 'diagrams.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        for d in sorted(m['diagrams'].values(), key=lambda d: (d['package'], d['name'])):
            f.write(f'- name: {q(d["name"])}\n  guid: {q(d["guid"])}\n  package: {q(d["package"])}\n' + block('note', d['note'], '  ') +
                    '  elements:\n' + ''.join(f'    - {q(x)}\n' for x in d['elements']))
    with open(os.path.join(out, 'glossary.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        for t, g in sorted(m['glossary'].items(), key=lambda x: x[0].lower()):
            f.write(f'- term: {q(t)}\n  type: {q(g["type"])}\n' + block('meaning', g['meaning'], '  '))
    os.makedirs(os.path.join(out, 'templates'))
    for n, t in sorted(m['templates'].items()):
        with open(os.path.join(out, 'templates', safe(n) + '.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(f'name: {n}\nid: {t.get("id")}\nkind: {t.get("kind")}\nsections: {t.get("sections")}\noptions: {t.get("options")}\n\n{t.get("content", t.get("error"))}\n')
    print(f'exported {len(m["elements"])} elements, {len(m["connectors"])} connectors, {len(m["diagrams"])} diagrams to {out}/')

if __name__ == '__main__':
    main(*sys.argv[1:])
