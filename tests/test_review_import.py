"""Regression test of the Word review import: python tests/test_review_import.py

tests/review-sample.docx is the WG 4.6.3 Organisational View document with added test cases:
a new function (with TBD and an unknown abbreviation), a new role marked [WIP], changes by Claude
in the Member State section, a TODO and a WIP comment.
"""
import os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(root, 'tools'))
from docx_import import run, ckind

model = os.path.join(root, 'model', 'NRA.qea')
ch, unmapped, comments = run(os.path.join(root, 'tests', 'review-sample.docx'), model, model)
new = {c['name']: c for c in ch if c['kind'] == 'new element'}
assert not unmapped, unmapped
assert set(new) == {'F3.6.12 Publish NAP Statistics', 'NAP Data Steward (DS)', 'Content provision contract/agreement (NO to CP)'}, set(new)
fn = new['F3.6.12 Publish NAP Statistics']
assert fn['apply'] and any('TBD' in w for w in fn['warnings']) and any('XYZQ' in w for w in fn['warnings'])
assert any('data flows' in r for r in fn['required'])
assert new['NAP Data Steward (DS)']['flags'] == ['wip'] and not new['NAP Data Steward (DS)']['apply']
ms = [c for c in ch if c.get('name') == 'Member State' and c.get('type') == 'Actor'][0]
assert 'proposal by Claude' in ms['flags'] and not ms['apply']
kinds = sorted(ckind(m['text']) for c in ch for m in c['comments'])
assert kinds == ['todo', 'wip'], kinds
print(f'OK – {len(ch)} sections, {len(new)} new elements, {sum(1 for c in ch if not c["apply"])} not applied')
