import json

with open("phy101_subjective.json") as f:
    subj = json.load(f)

for i, q in enumerate(subj):
    qid = q["id"]
    qtext = q["question"]
    print(f"ID {qid}: {qtext}")
