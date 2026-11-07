#!/usr/bin/env python3
import json, re

# Load original objective questions
with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

print(f"Master audit engine processing {len(mcqs)} MCQs...")
