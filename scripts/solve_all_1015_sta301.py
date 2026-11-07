#!/usr/bin/env python3
import json, re, math

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

def clean_text(t):
    t = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?\s*(-+\s*Please choose one)?', '', t, flags=re.I)
    t = re.sub(r'Please choose one', '', t, flags=re.I)
    t = re.sub(r'Downloaded by.*', '', t, flags=re.I)
    t = re.sub(r'Update MCQS.*Marks', '', t, flags=re.I)
    t = re.sub(r'0304-1659294.*', '', t)
    t = re.sub(r'AL-JUNAID.*', '', t, flags=re.I)
    t = re.sub(r'C\s*o\s*m\s*e\s*&\s*Jo\s*in.*', '', t, flags=re.I)
    t = re.sub(r'lOMoARcPSD\|\d+', '', t)
    t = re.sub(r'\(Lesson no \d+.*?\)', '', t, flags=re.I)
    t = re.sub(r'\(rep\)', '', t, flags=re.I)
    t = ' '.join(t.split())
    return t

def clean_opt(o):
    o = str(o).strip()
    o = re.sub(r'\(?\s*Page\s*#?\s*\d+.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Option:.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Answer:.*', '', o, flags=re.I).strip()
    o = re.sub(r'^[a-d►\*•\s\.]+', '', o).strip()
    o = re.sub(r'\(rep.*?\)', '', o, flags=re.I).strip()
    o = re.sub(r'\(Doubtful\)', '', o, flags=re.I).strip()
    o = re.sub(r'^\)\s*', '', o).strip()
    return o

print("Loaded cleaner functions.")
