#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

# Let's inspect unique questions when normalized
def norm(t):
    t = str(t).lower()
    replacements = {
        '\uf0c7': '∩', '\uf0c8': '∪', '\uf03d': '=', '\uf0b7': '',
        '\uf028': '(', '\uf029': ')', '\uf02d': '-', '\uf0b4': '*',
        '\uf0e5': '∑', '\uf0b9': '!=', '\uf03c': '<', '\uf03e': '>',
        '\uf0e6': '(', '\uf0e7': '(', '\uf0e8': '(',
        '\uf0f6': ')', '\uf0f7': ')', '\uf0f8': ')'
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    t = re.sub(r'\(?\s*marks\s*:\s*\d+\s*\)?\s*(-+\s*please choose one)?', '', t)
    t = re.sub(r'please choose one', '', t)
    t = re.sub(r'downloaded by.*', '', t)
    t = re.sub(r'update mcqs.*marks', '', t)
    t = re.sub(r'0304-1659294.*', '', t)
    t = re.sub(r'al-junaid.*', '', t)
    t = re.sub(r'c\s*o\s*m\s*e\s*&\s*jo\s*in.*', '', t)
    t = re.sub(r'lomoarcpsd\|\d+', '', t)
    t = re.sub(r'\(lesson no \d+.*?\)', '', t)
    t = re.sub(r'\(rep.*?\)', '', t)
    t = re.sub(r'\(doubtful\)', '', t)
    t = ' '.join(t.split())
    return t

print(f"Total MCQs: {len(mcqs)}")
