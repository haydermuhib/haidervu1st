#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

target_qs = [q for q in mcqs if q.get('topic') in ['Measures of Dispersion', 'Measures of Central Tendency']]
print(f"Target Disp & CT count: {len(target_qs)}")

# Let's inspect unique question stems
stems = set()
for q in target_qs:
    qtext = q['question'].strip()
    qtext = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?\s*(-+\s*Please choose one)?', '', qtext, flags=re.I)
    qtext = re.sub(r'Please choose one', '', qtext, flags=re.I)
    qtext = re.sub(r'Downloaded by.*', '', qtext, flags=re.I)
    qtext = ' '.join(qtext.split())
    stems.add(qtext[:60].lower())

print(f"Unique stems in Disp & CT: {len(stems)}")
