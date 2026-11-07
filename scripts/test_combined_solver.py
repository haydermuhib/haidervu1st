#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

from audit_mcqs_comprehensive import CORE_RULES
from audit_disp_ct import DISP_CT_RULES
from test_solve_first90 import RVK_RULES

ALL_PATTERNS = CORE_RULES + DISP_CT_RULES + RVK_RULES

# Add additional comprehensive rules covering Probability, Basics, Sampling, Estimation
ADDITIONAL_RULES = [
    # Probability & Sets
    (r'multiplication theorem', 'p(a) * p(b|a)'),
    (r'independent events.*p\(a\)=0\.40.*p\(b\)=0\.30', '0.12'),
    (r'if p\(a\)=0\.30.*p\(b\)=0\.40.*independent', '0.12'),
    (r'two events a and b are mutually exclusive', 'p(a) + p(b)'),
    (r'mutually exclusive events then p\(a or b\)', 'p(a) + p(b)'),
    (r'mutually exclusive.*p\(a\s*∪\s*b\)', 'p(a) + p(b)'),
    (r'p\s*\(\s*a\s*\|\s*b\s*\)', 'p (a n b)/p (b)'),
    (r'conditional probability p\s*\(a\|b\)', 'p(a ∩ b) / p(b)'),
    (r'conditional probability of b given a', 'p(a ∩ b) / p(a)'),
    (r'if a and b are independent then p\(a\|b\)', 'p(a)'),
    (r'if a and b are independent then p\(b\|a\)', 'p(b)'),
    (r'sample space of rolling one die', '6'),
    (r'sample points.*rolling one die', '6'),
    (r'sample space of tossing two coins', '4'),
    (r'sample space of tossing three coins', '8'),
    (r'sum of 11 when a pair of dice is thrown', 'compound event'),
    (r'sum of probabilities of all mutually exclusive and exhaustive events', '1'),
    (r'sum of all probabilities in a probability distribution', '1'),
    (r'total probability is always', '1'),
    (r'p\(event\) = no\. of favorable outcomes / total', 'objective approach'),
    (r'classical definition of probability', 'equally likely'),
    (r'relative frequency approach', 'empirical'),
    (r'subjective approach.*probability', 'degree of belief'),
    (r'a – b will be', '{1,2}'),
    (r'a ∩ b', '{3,4}'),
    (r'a ∪ b', '{1,2,3,4,5,6}'),
    (r'universal set', 'sample space'),
    (r'null set', 'empty set'),
    (r'box contains two red and three green balls', '2/5'),
    (r'six red, three blue, and five pink ties', '3/14'),
    (r'15 boys and 10 girls.*three students', '21/46'),
    (r'three events a, b, and c, then for exhaustive', 'p(s)'),
    (r'calculate the probability of an event and it turns out to be -0.7', 'we made a mistake'),
    (r'probability.*turns out to be', 'we made a mistake'),
    (r'two dice are thrown simultaneously.*probability of getting a total of', '3/4'),
    (r'jack card from a well-shuffled', '4/52'),
    (r'king card from a well-shuffled', '4/52'),
    (r'ace card from a well-shuffled', '4/52'),
    (r'spade card from a well-shuffled', '13/52'),
    (r'heart card from a well-shuffled', '13/52'),
    (r'diamond card from a well-shuffled', '13/52'),
    (r'club card from a well-shuffled', '13/52'),
    (r'face card from a well-shuffled', '12/52'),
    (r'red card from a well-shuffled', '26/52'),
    (r'black card from a well-shuffled', '26/52'),

    # Data Representation & Basics
    (r'latin words status', 'political state'),
    (r'word “statistics”', 'political state'),
    (r'father of statistics', 'ronald fisher'),
    (r'qualitative variable', 'attribute'),
    (r'quantitative variable', 'numerical'),
    (r'continuous variable', 'infinite number of values'),
    (r'discrete variable', 'countable'),
    (r'temperature.*celsius', 'interval scale'),
    (r'temperature.*fahrenheit', 'interval scale'),
    (r'iq of a student', 'interval scale'),
    (r'nominal scale', 'classification'),
    (r'ordinal scale', 'ranking'),
    (r'ratio scale', 'true zero'),
    (r'absolute zero', 'ratio scale'),
    (r'primary data', 'originally collected'),
    (r'secondary data', 'already collected'),
    (r'questionnaire.*is an example of', 'primary data'),
    (r'census report.*is an example of', 'secondary data'),
    (r'title of the table', 'top'),
    (r'source note', 'bottom'),
    (r'footnotes', 'bottom'),
    (r'rows of a table', 'stubs'),
    (r'columns of a table', 'captions'),
    (r'stubs and captions', 'tabulation'),
    (r'tabulation is a', 'systematic arrangement'),
    (r'classification according to time', 'chronological'),
    (r'classification according to area', 'geographical'),
    (r'classification according to attributes', 'qualitative'),
    (r'classification according to magnitudes', 'quantitative'),
    (r'ogive is also called', 'cumulative frequency polygon'),
    (r'ogive.*graph of', 'cumulative frequency'),
    (r'less than ogive and more than ogive intersect at', 'median'),
    (r'intersection of two ogives', 'median'),
    (r'bar chart.*equal width', 'simple bar chart'),
    (r'multiple bar chart', 'two or more related'),
    (r'component bar chart', 'subdivided'),
    (r'percentage bar chart', '100%'),
    (r'pie chart.*angles', '360'),
    (r'pie diagram.*degrees', '360'),
    (r'stem and leaf display', 'john tukey'),
    (r'box and whisker plot', 'john tukey'),
    (r'box plot.*consists of', 'five-number summary'),
    (r'whiskers in a box plot', 'minimum and maximum'),
    (r'box in a box plot', 'q1, median, q3'),
    (r'interquartile range', 'q3 - q1'),
    (r'semi-interquartile range', '(q3 - q1)/2'),
    (r'shape of the distribution: x f 0', 'negatively skewed'),
    (r'teacher asked 10 of her students how many books', '12,6,7,10'),
    (r'not a graph of qualitative variable', 'pie chart'),
    (r'stem for the following data is: 22, 45, 36, 15, 14, 12', '1 | 2 | 3 | 4 | 5'),
    (r'third parties or witnesses', 'collection through local sources'),
    (r'direct personal investigation', 'primary data'),
    (r'indirect oral investigation', 'primary data'),

    # Sampling & Index Numbers
    (r'complete enumeration', 'census'),
    (r'sample is a.*of population', 'part'),
    (r'sample is a subset of', 'population'),
    (r'sampling with replacement', 'finite population becomes infinite'),
    (r'sampling without replacement', 'hypergeometric'),
    (r'base year.*index number', '100'),
    (r'base period.*taken as', '100'),
    (r'laspeyres.*weights', 'base year quantities'),
    (r'paasche.*weights', 'current year quantities'),
    (r'fisher.*ideal index', 'geometric mean of laspeyres and paasche'),
    (r'marshall edgeworth index', 'average of base and current year'),
    (r'unweighted index number', 'simple aggregative'),
    (r'consumer price index', 'cpi'),
    (r'cost of living index', 'cpi'),
    (r'link relatives', 'pn / pn-1 * 100'),
    (r'chain base method', 'link relatives'),
    (r'fixed base method', 'base year is fixed')
]

FULL_PATTERNS = ALL_PATTERNS + ADDITIONAL_RULES

print(f"Total compiled patterns: {len(FULL_PATTERNS)}")

def clean_opt(o):
    o = str(o).strip()
    o = re.sub(r'\(?\s*Page\s*#?\s*\d+.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Option:.*', '', o, flags=re.I).strip()
    o = re.sub(r'Correct Answer:.*', '', o, flags=re.I).strip()
    o = re.sub(r'^[a-d►\*•\s\.]+', '', o).strip()
    return o

resolved = 0
unresolved = []

for q in mcqs:
    qtext = q['question'].lower()
    
    # 1. Check patterns
    matched_ans = None
    for pat, ans_target in FULL_PATTERNS:
        if re.search(pat, qtext):
            matched_ans = ans_target
            break
            
    # 2. Check leaked option
    leaked_target = None
    for idx, o in enumerate(q['options']):
        m = re.search(r'Correct Option:\s*([A-E])\.?\s*([^\n\r]+)?', o, flags=re.I)
        if m:
            let = m.group(1).lower()
            let_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
            target_idx = let_map.get(let)
            if target_idx is not None and target_idx < len(q['options']):
                leaked_target = clean_opt(q['options'][target_idx])
            break
            
    if matched_ans or leaked_target:
        resolved += 1
    else:
        unresolved.append(q)

print(f"Resolved: {resolved} / {len(mcqs)} ({resolved*100/len(mcqs):.1f}%)")
print(f"Unresolved: {len(unresolved)}")
