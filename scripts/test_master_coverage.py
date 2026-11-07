#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

# Load rules
from audit_mcqs_comprehensive import CORE_RULES
from audit_disp_ct import DISP_CT_RULES
from test_solve_first90 import RVK_RULES

ALL_PATTERNS = CORE_RULES + DISP_CT_RULES + RVK_RULES

matched = 0
unmatched = []

for q in mcqs:
    qtext = q['question'].lower()
    m = False
    for pat, ans in ALL_PATTERNS:
        if re.search(pat, qtext):
            m = True
            break
    if m:
        matched += 1
    else:
        unmatched.append(q)

print(f"Total MCQs: {len(mcqs)}")
print(f"Matched: {matched} ({matched*100/len(mcqs):.1f}%)")
print(f"Unmatched: {len(unmatched)}")
