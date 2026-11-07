import json, re
from sta301_knowledge_base import KNOWLEDGE_RULES
try:
    from sta301_expert_rules import EXPERT_RULES
except:
    EXPERT_RULES = []
from sta301_authoritative_engine import clean_opt, norm_text

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

ALL_RULES = EXPERT_RULES + KNOWLEDGE_RULES

def match_target(target, opt):
    t_clean = re.sub(r'[^a-zA-Z0-9]', '', target).lower()
    o_clean = re.sub(r'[^a-zA-Z0-9]', '', opt).lower()
    if not t_clean or not o_clean:
        return False
    return t_clean == o_clean or t_clean in o_clean or o_clean in t_clean

unmatched = []
for q in mcqs:
    raw_opts = q.get('options', [])
    clean_options = [clean_opt(o) for o in raw_opts]
    unique_opts = []
    for o in clean_options:
        if o and o not in unique_opts:
            unique_opts.append(o)
    if len(unique_opts) < 2:
        unique_opts = clean_options if len(clean_options) >= 2 else ['True', 'False']
        
    qtext_norm = norm_text(q.get('question', ''))
    
    best_idx = None
    for pat, ans_target, expl in ALL_RULES:
        if re.search(pat, qtext_norm):
            for oi, opt in enumerate(unique_opts):
                if match_target(ans_target, opt):
                    best_idx = oi
                    break
            if best_idx is not None:
                break
    if best_idx is None:
        for oi, raw_o in enumerate(raw_opts):
            m = re.search(r'Correct Option:\s*([A-E])\.?\s*([^\n\r]+)?', str(raw_o), flags=re.I)
            if m:
                let = m.group(1).lower()
                let_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
                t_idx = let_map.get(let)
                if t_idx is not None and t_idx < len(unique_opts):
                    best_idx = t_idx
                break
    if best_idx is None:
        unmatched.append({
            'id': q['id'],
            'q': q['question'],
            'opts': unique_opts,
            'raw_opts': raw_opts
        })

print(f"Total unmatched: {len(unmatched)}")
with open('/tmp/unmatched_420.json', 'w') as f:
    json.dump(unmatched, f, indent=2)
