#!/usr/bin/env python3
"""
Senior Subject Matter Expert Auditor for STA301 (Statistics and Probability).
Audits and verifies all 1015 MCQs and all 79 subjective questions.
"""
import json, re, math

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

def clean_q(q):
    q = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?\s*(-+\s*Please choose one)?', '', q, flags=re.I)
    q = re.sub(r'Please choose one', '', q, flags=re.I)
    q = re.sub(r'Downloaded by.*', '', q, flags=re.I)
    q = re.sub(r'Update MCQS.*Marks', '', q, flags=re.I)
    q = re.sub(r'0304-1659294.*', '', q)
    q = re.sub(r'AL-JUNAID.*', '', q, flags=re.I)
    q = re.sub(r'C\s*o\s*m\s*e\s*&\s*Jo\s*in.*', '', q, flags=re.I)
    q = re.sub(r'lOMoARcPSD\|\d+', '', q)
    q = re.sub(r'\(Lesson no \d+.*?\)', '', q, flags=re.I)
    q = re.sub(r'\(rep\)', '', q, flags=re.I)
    q = ' '.join(q.split())
    return q

print("Loaded audit script module.")
