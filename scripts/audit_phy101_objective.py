import json, re, subprocess

print("Starting deep audit of phy101_objective.json...")

with open("phy101_objective.json", "r", encoding="utf-8") as f:
    obj = json.load(f)

print(f"Total MCQs loaded: {len(obj)}")

# Let's inspect all questions that need fixing
