#!/usr/bin/env python3
import json, re

print("Running final polish on all question banks...")

# 1. CS101 Fixes
with open("cs101_quiz_bank.json") as f:
    cs = json.load(f)

for idx, q in enumerate(cs):
    qtext = q.get("question", "")
    if "hexadecimal value 'ff'" in qtext.lower():
        q["options"] = ["4 bits", "8 bits", "16 bits", "32 bits"]
        q["answer"] = "8 bits"
    elif "2’s complement notation" in qtext.lower() or "2's complement notation" in qtext.lower():
        q["options"] = ["8 bits", "16 bits", "32 bits", "64 bits"]
        q["answer"] = "8 bits"
    elif "form of magnetic system" in qtext.lower():
        q["question"] = "Which of the following is a form of magnetic storage system?"
        q["options"] = ["Hard Disk", "Compact Disc (CD)", "Flash Drive", "DVD"]
        q["answer"] = "Hard Disk"
    elif "maximum number function will keep on going" in qtext.lower():
        q["options"] = ["Linear Search", "Binary Search", "Bubble Sort", "Insertion Sort"]
        q["answer"] = "Linear Search"
    elif "standard sampling rate for cd-quality" in qtext.lower():
        q["options"] = ["22.05 kHz", "44.1 kHz", "48 kHz", "96 kHz"]
        q["answer"] = "44.1 kHz"
    elif "typical bit depth for standard cd-quality" in qtext.lower():
        q["options"] = ["8 bit", "16 bit", "24 bit", "32 bit"]
        q["answer"] = "16 bit"

with open("cs101_quiz_bank.json", "w") as f:
    json.dump(cs, f, indent=2, ensure_ascii=False)

# 2. ISL202 Fixes
with open("isl202_quiz_bank.json") as f:
    isl = json.load(f)

for idx, q in enumerate(isl):
    qtext = q.get("question", "")
    if "had -e- qazaf" in qtext.lower() or "hadd-e-qazaf" in qtext.lower():
        q["options"] = ["80 Lashes", "100 Lashes", "40 Lashes", "50 Lashes"]
        q["answer"] = "80 Lashes"
    elif "imam shafi took the office of" in qtext.lower():
        q["options"] = ["15 years", "18 years", "20 years", "25 years"]
        q["answer"] = "15 years"
    elif "jehad become mandatory" in qtext.lower() or "jihad become mandatory" in qtext.lower():
        q["options"] = ["1 AH", "2 AH", "3 AH", "4 AH"]
        q["answer"] = "2 AH"
    elif "makkah was conquered in" in qtext.lower():
        q["options"] = ["6 AH", "7 AH", "8 AH", "9 AH"]
        q["answer"] = "8 AH"
    elif "year in which the holy prophet died" in qtext.lower():
        q["options"] = ["632 A.D.", "630 A.D.", "628 A.D.", "634 A.D."]
        q["answer"] = "632 A.D."
    elif "number of ramzan in the islamic calendar" in qtext.lower():
        q["options"] = ["7th", "8th", "9th", "10th"]
        q["answer"] = "9th"
    elif "ghazwa ahzab" in qtext.lower():
        q["options"] = ["3 AH", "4 AH", "5 AH", "6 AH"]
        q["answer"] = "5 AH"

with open("isl202_quiz_bank.json", "w") as f:
    json.dump(isl, f, indent=2, ensure_ascii=False)

# 3. MTH202 Fixes
with open("mth202_objective.json") as f:
    mth = json.load(f)

for q in mth:
    new_opts = []
    for o in q.get("options", []):
        co = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?|\-?\s*Please choose one.*', '', str(o), flags=re.I).strip()
        if co and co not in new_opts:
            new_opts.append(co)
    if len(new_opts) >= 2:
        q["options"] = new_opts
    if q.get("answer") not in q["options"]:
        q["answer"] = q["options"][0]

with open("mth202_objective.json", "w") as f:
    json.dump(mth, f, indent=2, ensure_ascii=False)

# 4. STA301 Fixes
with open("sta301_objective.json") as f:
    sta = json.load(f)

for q in sta:
    new_opts = []
    for o in q.get("options", []):
        co = re.sub(r'\(?\s*Marks\s*:\s*\d+\s*\)?|\-?\s*Please choose one.*', '', str(o), flags=re.I).strip()
        co = re.sub(r'vu\s+\d+\s+\d+.*', '', co, flags=re.I).strip()
        if co and co not in new_opts:
            new_opts.append(co)
    if len(new_opts) >= 2:
        q["options"] = new_opts
    if q.get("answer") not in q["options"]:
        q["answer"] = q["options"][0]
    q["correct_answer"] = q["options"].index(q["answer"])

with open("sta301_objective.json", "w") as f:
    json.dump(sta, f, indent=2, ensure_ascii=False)

print("Finished polishing JSON banks. Now rebuilding quiz_data.js...")
import subprocess
subprocess.run(["python3", "build_clean_quiz_data_js.py"], check=True)
print("All banks and quiz_data.js completely refreshed!")

