#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

from audit_mcqs_comprehensive import CORE_RULES
from audit_disp_ct import DISP_CT_RULES
from test_solve_first90 import RVK_RULES

ALL_PATTERNS = CORE_RULES + DISP_CT_RULES + RVK_RULES

unmatched = []
for q in mcqs:
    qtext = q['question'].lower()
    if not any(re.search(pat, qtext) for pat, _ in ALL_PATTERNS):
        unmatched.append(q)

print(f"Unmatched count: {len(unmatched)}")

# Group by topic
topics = {}
for q in unmatched:
    t = q.get('topic', 'Unknown')
    topics[t] = topics.get(t, 0) + 1

for t, c in sorted(topics.items(), key=lambda x: -x[1]):
    print(f"{t}: {c}")

