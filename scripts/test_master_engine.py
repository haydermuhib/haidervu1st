#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

def clean_opt(o):
    o = str(o).strip()
    replacements = {
        '\uf0c7': '∩', '\uf0c8': '∪', '\uf03d': '=', '\uf0b7': '',
        '\uf028': '(', '\uf029': ')', '\uf02d': '-', '\uf0b4': '*',
        '\uf0e5': '∑', '\uf0b9': '!=', '\uf03c': '<', '\uf03e': '>',
        '\uf0e6': '(', '\uf0e7': '(', '\uf0e8': '(',
        '\uf0f6': ')', '\uf0f7': ')', '\uf0f8': ')'
    }
    for k, v in replacements.items():
        o = o.replace(k, v)
    o = re.sub(r'\(?\s*Page\s*#?\s*\d+.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Option:.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Answer:.*', '', o, flags=re.I).strip()
    o = re.sub(r'^[a-d►\*•\s\.]+', '', o).strip()
    o = re.sub(r'\(rep.*?\)', '', o, flags=re.I).strip()
    o = re.sub(r'\(Doubtful\)', '', o, flags=re.I).strip()
    o = re.sub(r'^\)\s*', '', o).strip()
    return o

def norm_q(q):
    q = str(q).lower()
    replacements = {
        '\uf0c7': '∩', '\uf0c8': '∪', '\uf03d': '=', '\uf0b7': '',
        '\uf028': '(', '\uf029': ')', '\uf02d': '-', '\uf0b4': '*',
        '\uf0e5': '∑', '\uf0b9': '!=', '\uf03c': '<', '\uf03e': '>',
        '\uf0e6': '(', '\uf0e7': '(', '\uf0e8': '(',
        '\uf0f6': ')', '\uf0f7': ')', '\uf0f8': ')'
    }
    for k, v in replacements.items():
        q = q.replace(k, v)
    q = re.sub(r'\(?\s*marks\s*:\s*\d+\s*\)?\s*(-+\s*please choose one)?', '', q)
    q = re.sub(r'please choose one', '', q)
    q = re.sub(r'downloaded by.*', '', q)
    q = re.sub(r'update mcqs.*marks', '', q)
    q = re.sub(r'0304-1659294.*', '', q)
    q = re.sub(r'al-junaid.*', '', q)
    q = re.sub(r'c\s*o\s*m\s*e\s*&\s*jo\s*in.*', '', q)
    q = re.sub(r'lomoarcpsd\|\d+', '', q)
    q = re.sub(r'\(lesson no \d+.*?\)', '', q)
    q = re.sub(r'\(rep.*?\)', '', q)
    q = re.sub(r'\(doubtful\)', '', q)
    q = ' '.join(q.split())
    return q

print("Testing parser...")
