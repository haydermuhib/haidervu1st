import json

with open('/tmp/final_unsolved.json') as f:
    items = json.load(f)

print(f"Total items to solve: {len(items)}")

# Let's write them all to /tmp/all_423.txt with 50 per page
with open('/tmp/all_423.txt', 'w') as f:
    for i, it in enumerate(items):
        f.write(f"[{i+1}] {it['id']} | {it['q']}\n    {it['opts']}\n\n")

print("Written to /tmp/all_423.txt")
