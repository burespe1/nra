"""Check the NRA model against the modelling conventions (Guideline 07) and versioning rules (Guideline 06).

Usage:  python tools/check.py [model/NRA.qea] [report.md] [--strict]
Errors break a convention that the documentation or traceability relies on; warnings are worth a look.
With --strict the script exits with code 1 when there are errors (use in CI once the model is clean).
"""
import sys, os, re, sqlite3
from collections import defaultdict

def main(argv):
    strict = '--strict' in argv
    args = [a for a in argv if a != '--strict']
    model = args[0] if args else 'model/NRA.qea'
    out = args[1] if len(args) > 1 else None
    c = sqlite3.connect(f'file:{model}?mode=ro', uri=True)
    pk = {r[0]: (r[1], r[2]) for r in c.execute('select Package_ID, Name, Parent_ID from t_package')}
    def path(pid):
        p = []
        while pid in pk and pk[pid][1] != 0:
            p.append(pk[pid][0]); pid = pk[pid][1]
        return '/'.join(reversed(p))
    obj = {r[0]: dict(id=r[0], name=r[1] or '', type=r[2], st=r[3] or '', kw=r[4] or '', pkg=path(r[5]), guid=r[6], note=r[7] or '')
           for r in c.execute('select Object_ID, Name, Object_Type, Stereotype, PDATA5, Package_ID, ea_guid, Note from t_object')}
    tags = defaultdict(dict)
    for o, p, v in c.execute('select Object_ID, Property, Value from t_objectproperties'):
        tags[o][p] = v
    con = [dict(id=r[0], type=r[1], st=r[2] or '', s=obj.get(r[3]), t=obj.get(r[4]), guid=r[5])
           for r in c.execute('select Connector_ID, Connector_Type, Stereotype, Start_Object_ID, End_Object_ID, ea_guid from t_connector')]
    errors, warnings = [], []
    E = lambda rule, msg: errors.append((rule, msg))
    W = lambda rule, msg: warnings.append((rule, msg))
    frame = [o for o in obj.values() if o['st'].startswith('FRAME_')]
    is_fn = lambda o: o and o['st'] in ('FRAME_Low_Level_Function', 'FRAME_High_Level_Function')
    is_flow = lambda o: o and o['st'] in ('FRAME_Low_Level_Data_Flow', 'FRAME_High_Level_Data_Flow')
    level = lambda o: 1 if 'High_Level' in o['st'] else 0

    # --- documentation: keywords, aliases
    documented = ('NAP Reference Architecture/NAP ', 'NAP Reference Architecture/Supplements/Requirements/', 'NAP Reference Architecture/Supplements/Specifications and Recommendations/')
    for o in frame:
        if not o['kw'] and o['pkg'].startswith(documented) and '/Unresolved' not in o['pkg'] and '/KPI Framework/' not in o['pkg'] + '/':
            E('keywords', f'{o["st"]} **{o["name"]}** has no Keywords (heading in the documentation would read ": {o["name"]}")')
    md_pkgs = set()
    alias_tpl = ('NC_N_PDEnotes', 'NC_NN_Pnotes', 'NC_NN_NNN_PECEnotes', 'NC_NN_NNN_PEDNCEN')  # templates printing {Pkg.Alias}
    for (cls,) in c.execute("select a.Classifier from t_attribute a join t_object o on o.Object_ID=a.Object_ID join t_objectproperties p on p.Object_ID=o.Object_ID and p.Property='RTFTemplate' where o.Stereotype='model document' and p.Value in (%s)" % ','.join("'%s'" % t for t in alias_tpl)):
        o = obj.get(int(cls)) if cls and cls.isdigit() else None
        if o: md_pkgs.add(o['id'])
    for oid in md_pkgs:
        o = obj[oid]
        if o['type'] == 'Package' and not c.execute('select Alias from t_object where Object_ID=?', (oid,)).fetchone()[0]:
            W('alias', f'package **{o["name"]}** is printed by a model document but has no Alias (used as chapter heading)')
    for mid, mname, cls, aname in c.execute("select o.Object_ID, o.Name, a.Classifier, a.Name from t_attribute a join t_object o on o.Object_ID=a.Object_ID where o.Stereotype='model document'"):
        if not (cls and cls.isdigit() and int(cls) in obj):
            E('model-document', f'model document **{mname}** refers to a deleted package “{aname}” – remove the reference')
    # --- versioning tags
    for o in frame + [o for o in obj.values() if o['st'] == 'GlossaryEntry']:
        if 'revised' not in tags[o['id']]:
            E('revised', f'{o["st"]} **{o["name"]}** has no tagged value `revised`')
    for o in obj.values():
        if o['type'] == 'Package' and c.execute('select Version from t_object where Object_ID=?', (o['id'],)).fetchone()[0] not in (None, '', '1.0'):
            W('package-version', f'package **{o["name"]}** carries a Version – the model version is the git tag (Guideline 06)')
    # --- connector conventions
    for k in con:
        s, t = k['s'], k['t']
        if not s or not t:
            E('dangling', f'connector {k["guid"]} has a missing end'); continue
        if k['st'] in ('IN', 'OUT') and (is_fn(s) and is_flow(t) or is_flow(s) and is_fn(t)):
            want = 'OUT' if is_fn(s) else 'IN'
            if k['st'] != want:
                E('in-out', f'{s["name"]} → {t["name"]} is «{k["st"]}», the arrow means «{want}»')
        if k['st'].lower().replace(' ', '') == 'componentof':
            if (is_fn(s) or is_flow(s)) and (is_fn(t) or is_flow(t)) and level(s) > level(t):
                E('componentof', f'«Componentof» {s["name"]} → {t["name"]} runs whole → part (expected low-level → high-level)')
            if s['st'] == 'FRAME_User_Need':
                E('servedby', f'{s["name"]} → {t["name"]} is «{k["st"]}», User Need → function links are «Servedby»')
        if s['st'] == 'FRAME_User_Need' and is_fn(t) and k['st'] != 'Servedby':
            E('servedby', f'{s["name"]} → {t["name"]} is {k["type"]} «{k["st"]}», expected Association «Servedby»')
    # --- requirements
    out_links = defaultdict(list); in_links = defaultdict(list)
    for k in con:
        if k['s'] and k['t']:
            out_links[k['s']['id']].append(k); in_links[k['t']['id']].append(k)
    rx = re.compile(r'^[LSK]\.\d+(\.\d+)+ ')
    for o in obj.values():
        if o['st'] != 'FRAME_Requirement' or '/Requirements/' not in o['pkg'] + '/':
            continue
        if not rx.match(o['name']):
            E('req-name', f'requirement **{o["name"]}** does not follow the naming L.x.y / K.x.y.z')
        fulfilled = [k for k in out_links[o['id']] if k['st'] == 'fulfilled by']
        issue = [k for k in out_links[o['id']] + in_links[o['id']] if (k['t'] if k['s']['id'] == o['id'] else k['s'])['type'] == 'Issue']
        if o['pkg'].endswith('/Unresolved'):
            if not issue: E('req-unresolved', f'unresolved requirement **{o["name"]}** is not linked to an issue')
        elif not fulfilled:
            E('req-fulfilled', f'requirement **{o["name"]}** has no «fulfilled by» link')
        if not any(k['type'] == 'Abstraction' and k['s']['st'] == 'FRAME_Specification' for k in in_links[o['id']]):
            W('req-source', f'requirement **{o["name"]}** has no Abstraction from a Specification')
    for o in obj.values():
        if o['st'] != 'FRAME_Specification' or '/Superseded' in o['pkg'] or '/Obsolete' in o['pkg']:
            continue
        yields = any(k['type'] in ('Abstraction', 'Usage') and k['t']['st'] == 'FRAME_Requirement' for k in out_links[o['id']])
        noreq = any(k['t']['type'] == 'Issue' for k in out_links[o['id']])
        if not yields and not noreq:
            W('spec-yield', f'specification **{o["name"]}** yields no requirement and is not linked to “Does not yield a Requirement”')
    # --- functions: RequirementLevel
    for o in obj.values():
        if o['st'] == 'FRAME_Low_Level_Function':
            lv = tags[o['id']].get('RequirementLevel')
            if lv not in ('MANDATORY', 'OPTIONAL', 'MANDATORY_PLUS'):
                W('req-level', f'function **{o["name"]}** has no valid RequirementLevel')
            elif lv == 'MANDATORY_PLUS' and 'OPTIONAL' not in o['note']:
                E('req-level', f'function **{o["name"]}** is MANDATORY_PLUS but its description has no “OPTIONAL:” part')
    # --- completeness of elements (typical result of new elements from a Word review)
    def links(o, st=None, direction=None, other=None):
        ks = (out_links[o['id']] if direction != 'in' else []) + (in_links[o['id']] if direction != 'out' else [])
        return [k for k in ks if (st is None or k['st'].lower().replace(' ', '') == st or (st == 'componentof' and k['type'] == 'Aggregation'))
                and (other is None or other((k['t'] if k['s']['id'] == o['id'] else k['s'])))]
    for o in obj.values():
        if o['st'] == 'FRAME_Low_Level_Function':
            flows = links(o, other=is_flow)
            if not any(k['st'] == 'IN' for k in flows) or not any(k['st'] == 'OUT' for k in flows):
                W('incomplete', f'function **{o["name"]}** has no {"IN and OUT" if not flows else ("IN" if not any(k["st"] == "IN" for k in flows) else "OUT")} data flows')
            if not links(o, 'componentof', 'out'):
                W('incomplete', f'function **{o["name"]}** is not «componentof» a high level function')
        elif o['st'] == 'FRAME_Role' and not links(o, 'defines'):
            W('incomplete', f'role **{o["name"]}** is not defined by an Actor («defines»)')
        elif o['st'] == 'FRAME_Agreement' and len(links(o, 'adheresto')) < 2:
            W('incomplete', f'agreement **{o["name"]}** has fewer than two parties («adheres to»)')
    # --- open review items and unapproved elements (Guideline 06)
    for oid, kind, prob, st in c.execute("select Object_ID, ProblemType, Problem, Status from t_objectproblems"):
        if (st or '').lower() not in ('resolved', 'closed', 'complete', 'completed', 'done') and oid in obj:
            W('open-items', f'{kind} on **{obj[oid]["name"]}**: {prob}')
    status = {o['id']: c.execute('select Status from t_object where Object_ID=?', (o['id'],)).fetchone()[0] for o in frame}
    for o in (frame if 'Approved' in status.values() else []):  # only once releases set Approved
        if status[o['id']] == 'Proposed':
            W('proposed', f'{o["kw"] or o["st"]} **{o["name"]}** is still Proposed (set Approved at release)')
    # --- duplicates
    seen = defaultdict(list)
    for o in frame:
        seen[(o['st'], o['name'])].append(o)
    for (st, n), lst in seen.items():
        if len(lst) > 1:
            W('duplicate', f'{len(lst)}× {st} **{n}**')
    # --- report
    md = [f'# Model check – {os.path.basename(model)}', '', f'**{len(errors)} errors, {len(warnings)} warnings**', '']
    for title, items in (('Errors', errors), ('Warnings', warnings)):
        if not items: continue
        md += [f'## {title}', '']
        groups = defaultdict(list)
        for r, m in items: groups[r].append(m)
        for r in sorted(groups):
            md.append(f'<details><summary><b>{r}</b> ({len(groups[r])})</summary>\n')
            md += [f'- {m}' for m in sorted(groups[r])]
            md.append('\n</details>\n')
    text = '\n'.join(md) + '\n'
    if out:
        open(out, 'w', encoding='utf-8').write(text); print(f'{len(errors)} errors, {len(warnings)} warnings → {out}')
    else:
        sys.stdout.write(text)
    return 1 if (strict and errors) else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
