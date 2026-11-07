import json, re

# Load existing subjective questions
with open("phy101_subjective.json", "r", encoding="utf-8") as f:
    subj = json.load(f)

print(f"Loaded {len(subj)} subjective questions.")
