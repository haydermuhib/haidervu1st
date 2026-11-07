#!/usr/bin/env python3
import json, re

def restore_truncated_word(w):
    if not w: return ""
    w_clean = w.strip()
    # Common truncated prefixes where regex stripped leading 'e' or 'o'
    replacements = {
        "xhort": "exhort",
        "xonerated": "exonerated",
        "xpatriated": "expatriated",
        "xpose": "expose",
        "xposed": "exposed",
        "mbarrassment": "embarrassment",
        "mbarrassmment": "embarrassment",
        "mbarrasment": "embarrassment",
        "mbarasment": "embarrassment",
        "mulatet": "emulate",
        "mulate": "emulate",
        "ppose": "oppose",
        "pposed": "opposed",
        "pposethem": "oppose them",
        "ne": "one",
        "nly": "only",
        "utput": "output",
        "vercome": "overcome",
        "ver": "over",
        "verflowing": "overflowing",
        "verconfident": "overconfident",
        "verstated": "overstated",
        "rganize": "organize",
        "rder": "order",
        "pinion": "opinion",
        "bject": "object",
        "bjective": "objective",
        "ccur": "occur",
        "ccurrence": "occurrence",
        "rigin": "origin",
        "riginal": "original"
    }
    low = w_clean.lower()
    if low in replacements:
        # Preserve capitalization
        if w_clean[0].isupper():
            return replacements[low].capitalize()
        return replacements[low]
    return w_clean

def clean_eng_opt(opt):
    if not opt: return ""
    o = str(opt).strip()
    # Strip any leading letter markers like a. b. c. d. (a) (b)
    o = re.sub(r'^\(?[a-dA-D][\)\.\:\s]+', '', o).strip()
    o = re.sub(r'^(?:[►•\*\–\-✓✔○●✔️\uf0b7\d\.\:\s]+)', '', o).strip()
    o = re.sub(r'\(correct\).*|\(✔\).*|right answer.*', '', o, flags=re.I).strip()
    
    words = o.split()
    fixed_words = [restore_truncated_word(w) for w in words]
    res = " ".join(fixed_words)
    return res

print("ENG101 helper functions defined.")

