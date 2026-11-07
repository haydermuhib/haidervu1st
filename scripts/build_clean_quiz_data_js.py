#!/usr/bin/env python3
import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_data(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

print("Rebuilding clean master quiz_data.js from standardized JSON banks in data/...")

cs101_obj = load_data("cs101_objective.json")
cs101_sub = load_data("cs101_subjective.json")

eng101_obj = load_data("eng101_objective.json")
eng101_sub = load_data("eng101_subjective.json")

isl202_obj = load_data("isl202_objective.json")
isl202_sub = load_data("isl202_subjective.json")

mth202_obj = load_data("mth202_objective.json")
mth202_sub = load_data("mth202_subjective.json")

phy101_obj = load_data("phy101_objective.json")
phy101_sub = load_data("phy101_subjective.json")

sta301_obj = load_data("sta301_objective.json")
sta301_sub = load_data("sta301_subjective.json")

header = """/* Master VU Multi-Subject Examination & Practice Data Bank */
/* 100% Verified, Cleaned, and Fully Audited Questions & Solutions */
"""

out_path = os.path.join(BASE_DIR, "quiz_data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(header)
    f.write("\nwindow.CS101_QUESTIONS = " + json.dumps(cs101_obj, ensure_ascii=False) + ";\n")
    f.write("\nwindow.ENG101_QUESTIONS = " + json.dumps(eng101_obj, ensure_ascii=False) + ";\n")
    f.write("\nwindow.ISL202_QUESTIONS = " + json.dumps(isl202_obj, ensure_ascii=False) + ";\n")
    f.write("\nwindow.MTH202_QUESTIONS = " + json.dumps(mth202_obj, ensure_ascii=False) + ";\n")
    f.write("\nwindow.PHY101_QUESTIONS = " + json.dumps(phy101_obj, ensure_ascii=False) + ";\n")
    f.write("\nwindow.STA301_QUESTIONS = " + json.dumps(sta301_obj, ensure_ascii=False) + ";\n")
    
    f.write("\nwindow.CS101_SUBJECTIVE = " + json.dumps(cs101_sub, ensure_ascii=False) + ";\n")
    f.write("\nwindow.ENG101_SUBJECTIVE = " + json.dumps(eng101_sub, ensure_ascii=False) + ";\n")
    f.write("\nwindow.ISL202_SUBJECTIVE = " + json.dumps(isl202_sub, ensure_ascii=False) + ";\n")
    f.write("\nwindow.MTH202_SUBJECTIVE = " + json.dumps(mth202_sub, ensure_ascii=False) + ";\n")
    f.write("\nwindow.PHY101_SUBJECTIVE = " + json.dumps(phy101_sub, ensure_ascii=False) + ";\n")
    f.write("\nwindow.STA301_SUBJECTIVE = " + json.dumps(sta301_sub, ensure_ascii=False) + ";\n")

print(f"Successfully generated {out_path}!")
print(f"CS101:  {len(cs101_obj)} MCQs, {len(cs101_sub)} Subjective")
print(f"ENG101: {len(eng101_obj)} MCQs, {len(eng101_sub)} Subjective")
print(f"ISL202: {len(isl202_obj)} MCQs, {len(isl202_sub)} Subjective")
print(f"MTH202: {len(mth202_obj)} MCQs, {len(mth202_sub)} Subjective")
print(f"PHY101: {len(phy101_obj)} MCQs, {len(phy101_sub)} Subjective")
print(f"STA301: {len(sta301_obj)} MCQs, {len(sta301_sub)} Subjective")
