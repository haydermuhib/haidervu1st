#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

def normalize_text(text):
    text = str(text)
    replacements = {
        '\uf0c7': '∩', '\uf0c8': '∪', '\uf03d': '=', '\uf0b7': '',
        '\uf028': '(', '\uf029': ')', '\uf02d': '-', '\uf0b4': '*',
        '\uf0e5': '∑', '\uf0b9': '!=', '\uf03c': '<', '\uf03e': '>',
        '\uf0e6': '(', '\uf0e7': '(', '\uf0e8': '(',
        '\uf0f6': ')', '\uf0f7': ')', '\uf0f8': ')'
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?\s*(-+\s*Please choose one)?', '', text, flags=re.I)
    text = re.sub(r'Please choose one', '', text, flags=re.I)
    text = re.sub(r'Downloaded by.*', '', text, flags=re.I)
    text = re.sub(r'Update MCQS.*Marks', '', text, flags=re.I)
    text = re.sub(r'0304-1659294.*', '', text)
    text = re.sub(r'AL-JUNAID.*', '', text, flags=re.I)
    text = re.sub(r'C\s*o\s*m\s*e\s*&\s*Jo\s*in.*', '', text, flags=re.I)
    text = re.sub(r'lOMoARcPSD\|\d+', '', text)
    text = re.sub(r'\(Lesson no \d+.*?\)', '', text, flags=re.I)
    text = re.sub(r'\(rep.*?\)', '', text, flags=re.I)
    text = re.sub(r'\(Doubtful\)', '', text, flags=re.I)
    text = ' '.join(text.split())
    return text

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

print(f"Total MCQs loaded: {len(mcqs)}")
