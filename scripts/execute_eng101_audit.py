#!/usr/bin/env python3
"""
Senior Subject Matter Expert Auditor for ENG101 (English Comprehension)
Full execution script:
- Verifies and updates eng101_quiz_bank.json (671 MCQs)
- Verifies and updates subjective_bank.json['ENG101'] (57 Subjective questions)
- Rebuilds quiz_data.js
"""

import json, re

print("==================================================================")
print("ENG101 SENIOR SUBJECT MATTER EXPERT AUDIT & RECTIFICATION")
print("==================================================================")

# Load existing banks
with open('/home/haider/Desktop/Chores/eng101_quiz_bank.json') as f:
    mcqs = json.load(f)

with open('/home/haider/Desktop/Chores/subjective_bank.json') as f:
    subj_master = json.load(f)

eng_subj = subj_master.get("ENG101", [])

print(f"Loaded {len(mcqs)} MCQs and {len(eng_subj)} Subjective questions.")

# -------------------------------------------------------------
# 1. Truncated word replacements
# -------------------------------------------------------------
TRUNCATED_WORD_REPLACEMENTS = {
    "ither": "either",
    "rmer": "former",
    "ptimistic": "optimistic",
    "ptions": "options",
    "bjective": "objective",
    "vergeneralization": "overgeneralization",
    "vidence": "evidence",
    "xonerate": "exonerate",
    "xonerated": "exonerated",
    "ssist": "assist",
    "cstatic": "ecstatic",
    "vinces": "evinces",
    "ntertain": "entertain",
    "xhaust": "exhaust",
    "xigent": "exigent",
    "xpecting": "expecting",
    "xternal": "external",
    "xude": "exude",
    "xygen": "oxygen",
    "perating": "operating",
    "peration": "operation",
    "perators": "operators",
    "pithet": "epithet",
    "qualizes": "equalizes",
    "quitable": "equitable",
    "rdered": "ordered",
    "rganization": "organization",
    "scillates": "oscillates",
    "soteric": "esoteric",
    "victs": "evicts",
    "vokes": "evokes",
    "volves": "evolves",
    "xam": "exam",
    "xamination": "examination",
    "xcess": "excess",
    "xcited": "excited",
    "xpensive": "expensive",
    "xplains": "explains",
    "xplicates": "explicates",
    "xpressions": "expressions",
    "xtended": "extended",
    "xtensive": "extensive",
    "xtensively": "extensively",
    "xtracted": "extracted",
    "urn o n": "turn down",
    "ave on": "have on",
    "f value": "of value",
    "nd": "end",
    "asy": "easy",
    "ffect": "effect",
    "ffects": "effects",
    "ffective": "effective",
    "lder": "older",
    "ldest": "oldest",
    "liminate": "eliminate",
    "maciated": "emaciated",
    "minent": "eminent",
    "bedience": "obedience",
    "bedient": "obedient",
    "bediently": "obediently",
    "bserving": "observing",
    "ccasion": "occasion",
    "ccentric": "eccentric",
    "clectic": "eclectic",
    "cliptic": "ecliptic",
    "cstasy": "ecstasy",
    "fficient": "efficient",
    "nthusiastic": "enthusiastic",
    "utside": "outside",
    "bey": "obey",
    "ff": "off",
    "m": "emulate",
    "m late": "emulate",
    "lo t": "flout"
}

def restore_word(word):
    if not word: return ""
    clean = word.strip()
    low = clean.lower()
    if low in TRUNCATED_WORD_REPLACEMENTS:
        rep = TRUNCATED_WORD_REPLACEMENTS[low]
        if clean[0].isupper():
            return rep.capitalize()
        return rep
    return clean

def fix_all_truncated_words(text):
    if not text: return ""
    t = text
    t = re.sub(r'\bEitherorfallacy\(\)', 'Either/or fallacy', t)
    t = re.sub(r'\bEitherorfallacy\b', 'Either/or fallacy', t)
    t = re.sub(r'\bptimistic\(\)', 'Optimistic', t)
    t = re.sub(r'\bptimistic\b', 'optimistic', t, flags=re.I)
    t = re.sub(r'\bptions\b', 'options', t, flags=re.I)
    t = re.sub(r'\bvergeneralization\b', 'overgeneralization', t, flags=re.I)
    t = re.sub(r'\bbjective\b', 'objective', t, flags=re.I)
    t = re.sub(r'\bither\b', 'either', t, flags=re.I)
    t = re.sub(r'\brmer\b', 'former', t, flags=re.I)
    t = re.sub(r'\burn o n\b', 'turn down', t, flags=re.I)
    t = re.sub(r'\bave on\b', 'have on', t, flags=re.I)
    t = re.sub(r'\bxonerate\b', 'exonerate', t, flags=re.I)
    t = re.sub(r'\bxonerated\b', 'exonerated', t, flags=re.I)
    t = re.sub(r'\bssist\b', 'assist', t, flags=re.I)
    t = re.sub(r'\bcstatic\b', 'ecstatic', t, flags=re.I)
    t = re.sub(r'\bvinces\b', 'evinces', t, flags=re.I)
    t = re.sub(r'\bvolves\b', 'evolves', t, flags=re.I)
    t = re.sub(r'\bntertain\b', 'entertain', t, flags=re.I)
    t = re.sub(r'\bxude\b', 'exude', t, flags=re.I)
    t = re.sub(r'\bstasy\b', 'ecstasy', t, flags=re.I)
    t = re.sub(r'\bToprovideevidenceandsupport\b', 'To provide evidence and support', t)
    t = re.sub(r'\bToimproveclarity,coherence,andconcision\(\)', 'To improve clarity, coherence, and concision', t)
    t = re.sub(r'\bToplan,organize,andrevise\(\)', 'To plan, organize, and revise', t)
    t = re.sub(r'\bReadingcomprehension\.', 'Reading comprehension', t)
    t = re.sub(r'\bToreadbetweenthelines\b', 'To read between the lines', t)
    t = re.sub(r'\bAstylethatisfullofwords\.', 'A style that is full of words', t)
    t = re.sub(r'\bMainIdea\.', 'Main Idea', t)
    t = re.sub(r'\bBasewords\b', 'Base words', t)
    t = re.sub(r'\bThevioladidnotfalloffthebike\.', 'impolitical', t)
    t = re.sub(r'\bcannotbeconverted\b', 'can be converted', t)
    t = re.sub(r'\bshowdifferences\.', 'show differences', t)
    t = re.sub(r'\bDeadloss\b', 'Dead loss', t)
    t = re.sub(r'\bHearse\(\)', 'Hearse', t)
    t = re.sub(r'\bTrue\.\(\)', 'True', t)
    t = re.sub(r'\bFalse\.\(\)', 'False', t)
    t = re.sub(r'\bTrue\.', 'True', t)
    t = re.sub(r'\bFalse\.', 'False', t)
    t = re.sub(r'\bFatalist\.', 'Fatalist', t)
    t = re.sub(r'\bMake\.', 'Make', t)
    t = re.sub(r'\bAntonyms\.', 'Antonyms', t)
    t = re.sub(r'\bsynonyms\.', 'synonyms', t)
    
    words = t.split()
    fixed_words = [restore_word(w) for w in words]
    return " ".join(fixed_words)

def clean_watermarks_from_question(q):
    if not q: return ""
    res = q.strip()
    res = re.sub(r'VISIT\s*\(?ANY\s*MORE\s*SOLUTIONS\)?', '', res, flags=re.I)
    res = re.sub(r'VISIT\s*ANY\s*1MORE\s*SOLUTIONS', '', res, flags=re.I)
    res = re.sub(r'STUDENTS\s*A\s*FACEBOOK\s*OF\s*VU', '', res, flags=re.I)
    res = re.sub(r'FILE\s*MARGE\s*BY\s*ALI\s*KHAN\s*WA-\s*NUM\s*03169948478', '', res, flags=re.I)
    res = re.sub(r'Contact\s*for\s*paid\s*LMS\s*Handling\s*Ali\s*Khan\s*0316\s*9948478', '', res, flags=re.I)
    res = re.sub(r'VU\s*TOOLKIT\s*BY\s*PARADOXCIAL.*?(?:Date:[^\n]+)?', '', res, flags=re.I)
    res = re.sub(r'Downloaded\s*by\s*[^\n]+lOMoARcPSD\|\d+', '', res, flags=re.I)
    res = re.sub(r'lOMoARcPSD\|\d+', '', res, flags=re.I)
    res = re.sub(r'Compiled\s*by\s*Barbie', '', res, flags=re.I)
    res = re.sub(r'vuhelp', '', res, flags=re.I)
    res = re.sub(r'FINALTERM\s*EXAMINATION[^\n]*', '', res, flags=re.I)
    res = re.sub(r'MIDTERM\s*EXAMINATION[^\n]*', '', res, flags=re.I)
    res = re.sub(r'MID\s*TERM', '', res, flags=re.I)
    res = re.sub(r'Most\s*Important\s*&\s*Repeated\s*MCQS\s*Midterm\s*Eng101', '', res, flags=re.I)
    res = re.sub(r'ENG101-\s*English\s*Comprehension', '', res, flags=re.I)
    res = re.sub(r'Please\s*choose\s*one\s*', '', res, flags=re.I)
    res = re.sub(r'\s+', ' ', res).strip()

    replacements_starts = [
        (r'^answer from the given options\.?\s*', 'Choose the best answer from the given options: '),
        (r'^appropriate connector\.?\s*', 'Fill in the blank with the appropriate connector: '),
        (r'^appropriate parallel structure\.?\s*', 'Fill in the blank with the appropriate parallel structure: '),
        (r'^appropriate phrasal verb\.?\s*', 'Fill in the blank with an appropriate phrasal verb: '),
        (r'^appropriate prepositions?:?\s*', 'Fill in the blank with the appropriate preposition: '),
        (r'^appropriate verb given below\.?\s*', 'Fill in the blank with the appropriate verb given below: '),
        (r'^appropriate word given below\.?\s*', 'Fill in the blank with the appropriate word given below: '),
        (r'^in the blank with appropriate phrasal verb\.?\s*', 'Fill in the blank with an appropriate phrasal verb: '),
        (r'^in the blank with appropriate verb given below\.?\s*', 'Fill in the blank with the appropriate verb given below: '),
        (r'^meaning for the highlighted word\.?\s*', 'Choose the best meaning for the highlighted word: '),
        (r'^meaning for the word underlined\.?\s*', 'Choose the best meaning for the underlined word: '),
        (r'^the sentence by choosing the best option\.?\s*', 'Complete the sentence by choosing the best option: '),
        (r'^the grammatical error in the following sentence\.?\s*', 'Identify the grammatical error in the following sentence: '),
        (r'^the relationship in which sentences and groups of sentences combine\.?\s*', 'What is the relationship in which sentences and groups of sentences combine? '),
        (r'^true of the following sentence\??\s*', 'Which of the following is true of the sentence: '),
        (r'^of the following example\??\s*', 'Which of the following is true of the example: '),
        (r'^following example\??\s*', 'Which of the following is true of the example: '),
        (r'^following sentence\??\s*', 'Which of the following is true of the sentence: '),
        (r'^following statements expresses fact\??\s*', 'Which of the following statements expresses a fact? '),
        (r'^hich one of these', 'Which one of these'),
        (r'^oneChoose a suitable option', 'Choose a suitable option'),
        (r'^oneFill in the blank', 'Fill in the blank'),
        (r'^option to complete the sentence\.?\s*', 'Choose the correct option to complete the sentence: '),
        (r'^option to fill in the blank\.?\s*', 'Choose the correct option to fill in the blank: '),
        (r'^option\.\s*', 'Choose the correct option: '),
        (r'^properly placed commas\.?\s*', 'Identify the sentence with properly placed commas: '),
        (r'^sentence by choosing the best option\.?\s*', 'Complete the sentence by choosing the best option: '),
        (r'^sentence by choosing the correct option\.?\s*', 'Complete the sentence by choosing the correct option: '),
        (r'^that best describes the sentence\.?\s*', 'Choose the option that best describes the sentence: '),
        (r'^that you think is correct\.?\s*', 'Click on the option that you think is correct: '),
        (r'^the best meaning for the highlighted word\.?\s*', 'Choose the best meaning for the highlighted word: '),
        (r'^the best meaning for the word underlined\.?\s*', 'Choose the best meaning for the underlined word: '),
        (r'^the blank with appropriate phrasal verb\.?\s*', 'Fill in the blank with an appropriate phrasal verb: '),
        (r'^the blank with appropriate verb given below\.?\s*', 'Fill in the blank with the appropriate verb given below: '),
        (r'^the blank with appropriate word given below\.?\s*', 'Fill in the blank with the appropriate word given below: '),
        (r'^the blank with the most suitable phrasal verb\.?\s*', 'Fill in the blank with the most suitable phrasal verb: '),
        (r'^the following example\??\s*', 'Which of the following is true of the example: '),
        (r'^the following is a sentence fragment\??\s*', 'Which of the following is a sentence fragment?'),
        (r'^the gap by choosing the best answer\.?\s*', 'Fill in the gap by choosing the best answer: '),
        (r'^there are three common purpose of communication', 'There are three common purposes of communication'),
        (r'^verb most similar in meaning to:\s*', 'Choose the phrasal verb most similar in meaning to: '),
        (r'^which best describes the sentence\.?\s*', 'Select the option which best describes the sentence: '),
        (r'^with appropriate phrasal verb\.?\s*', 'Fill in the blank with an appropriate phrasal verb: '),
        (r'^blank with appropriate', 'Fill in the blank with appropriate'),
        (r'^choosing the best answer\.\s*', 'Fill in the blank by choosing the best answer: '),
        (r'^choosing the correct option\.\s*', 'Complete the sentence by choosing the correct option: '),
        (r'^correct option\.\s*', 'Choose the correct option: '),
        (r'^for the underlined word\.\s*', 'Choose the antonym for the underlined word: '),
        (r'^gap by choosing the best answer\.\s*', 'Fill in the gap by choosing the best answer: '),
        (r'^give us the ability', 'Variables give us the ability'),
        (r'^given below\.\s*', 'Choose the correct transitional word for the sentence given below: '),
        (r'^is a related collection', 'A website is a related collection'),
        (r'^is the intro farce used', 'Stress is the force used'),
        (r'^it was cold and windy', 'Although it was cold and windy'),
        (r'^not\.\.\.\.\.\.\.\.\.\.\. Them\.\s*', 'Children should obey their parents, not disobey them: ')
    ]
    for pat, repl in replacements_starts:
        res = re.sub(pat, repl, res, flags=re.I)
    
    res = fix_all_truncated_words(res)
    return res.strip()

def clean_option(opt):
    if not opt: return ""
    o = str(opt).strip()
    o = re.sub(r'^\(?[a-dA-D][\)\.\:\s]+', '', o).strip()
    o = re.sub(r'^(?:[►•\*\–\-✓✔○●✔️\uf0b7\d\.\:\s]+)', '', o).strip()
    o = re.sub(r'\s*\(correct\).*|\s*\(✔\).*|\s*right answer.*', '', o, flags=re.I).strip()
    o = re.sub(r'\(\)$', '', o).strip()
    o = fix_all_truncated_words(o)
    return o.strip()

# -------------------------------------------------------------
# 2. Master Specific Overrides for Problematic MCQs
# -------------------------------------------------------------
MCQ_OVERRIDES = {
    4: {
        "question": "A diode functions as the electronic version of a __________-way valve.",
        "options": ["one", "two", "three", "four"],
        "answer": "one"
    },
    6: {
        "question": "A microprocessor can be made more powerful by increasing its ________.",
        "options": ["Clock frequency", "Word length", "Clock frequency and Word length", "None of above"],
        "answer": "Clock frequency and Word length"
    },
    7: {
        "question": "A student of contemporary art must also study the classic works of artists from the past, recognizing that modern art owes much to the former.",
        "options": ["former", "modern", "religious", "secular"],
        "answer": "former"
    },
    8: {
        "question": "A student of contemporary art must also study the classic works of artists from the past, recognizing that modern art owes much to the former.",
        "options": ["former", "modern", "religious", "secular"],
        "answer": "former"
    },
    9: {
        "question": "A suffix is added to the beginning of a root word.",
        "options": ["True", "False"],
        "answer": "False"
    },
    16: {
        "question": "As a successful reader, you should know the main point and also recognize the ________.",
        "options": ["supporting details and related examples", "grammar of the sentences", "number of words", "font style"],
        "answer": "supporting details and related examples"
    },
    18: {
        "question": "Bringing subsystems together to form the system is called ________.",
        "options": ["Integration", "Merging", "Splitting", "Maintenance"],
        "answer": "Integration"
    },
    20: {
        "question": "Choose a suitable option to fill in the blank: His possession of the murder weapon ________ him in the crime.",
        "options": ["implicates", "explicates", "oscillates", "mitigates"],
        "answer": "implicates"
    },
    22: {
        "question": "Choose a suitable option to fill in the blank. Coach Calhoun tried to ________ his team to try harder in the face of overwhelming odds.",
        "options": ["exhort", "instigate", "emulate", "flout"],
        "answer": "exhort"
    },
    23: {
        "question": "Choose a suitable option to fill in the blank. Coach Calhoun tried to ________ his team to try harder in the face of overwhelming odds.",
        "options": ["exhort", "instigate", "emulate", "flout"],
        "answer": "exhort"
    },
    28: {
        "question": "Choose a suitable option to fill in the blank: Newton imagined light to ________ of particles emitted from luminous bodies.",
        "options": ["consist", "assist", "resist", "persist"],
        "answer": "consist"
    },
    31: {
        "question": "Choose the antonym for the underlined word: 'Our investigation will reveal the truth.'",
        "options": ["conceal", "expose", "inspect", "announce"],
        "answer": "conceal"
    },
    35: {
        "question": "Choose the antonym for the word in capital letters: 'The new governor will FREE the innocent prisoner.'",
        "options": ["imprison", "release", "pardon", "acquit"],
        "answer": "imprison"
    },
    37: {
        "question": "Choose one alternative from the options which can be substituted for the given statement: 'One who believes that all things and events in life are predetermined is a ________.'",
        "options": ["Fatalist", "Puritan", "Pessimist", "Optimist"],
        "answer": "Fatalist"
    },
    43: {
        "question": "Choose the best answer from the given options: You must have been ________ late or absent.",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    44: {
        "question": "Choose the best answer from the given options: He wanted to join the navy ________ his parents would not let him.",
        "options": ["but", "if", "either", "since"],
        "answer": "but"
    },
    45: {
        "question": "Choose the best answer from the given options: James usually has his lunch at this restaurant ________ sometimes he eats elsewhere.",
        "options": ["but", "either", "as", "if"],
        "answer": "but"
    },
    46: {
        "question": "Choose the best answer from the given options: James was so worried about his coming examination results that he could ________ sleep ________ eat properly.",
        "options": ["neither...nor", "either...or", "both...and", "both...or"],
        "answer": "neither...nor"
    },
    47: {
        "question": "Choose the best answer from the given options: Mother said, 'You ________ help me prepare dinner ________ do your homework.'",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    48: {
        "question": "Choose the best answer from the given options: Mr. James cannot speak English ________ he can speak Mandarin very well.",
        "options": ["but", "because", "since", "while"],
        "answer": "but"
    },
    49: {
        "question": "Choose the best answer from the given options: 'Could I come over at ________ three ________ four o\\'clock?' asked Joan.",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    50: {
        "question": "Choose the best answer from the given options: Rocky called ________ told me what happened.",
        "options": ["and", "but", "nor", "or"],
        "answer": "and"
    },
    53: {
        "question": "Choose the best answer from the given options: They can watch ________ the detective series ________ the foreign movies.",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    56: {
        "question": "Choose the best answer from the given options: You must have been either daydreaming or sleeping in class again. Which correlative conjunction is used?",
        "options": ["Either...or", "Neither...nor", "Both...and", "Neither...or"],
        "answer": "Either...or"
    },
    57: {
        "question": "Choose the best answer from the given options: ________ the men ________ their supervisor is to be blamed for the mishap.",
        "options": ["Neither...nor", "Either...or", "Both...and", "Either...nor"],
        "answer": "Neither...nor"
    },
    58: {
        "question": "Choose the best answer from the given options: 'Lower your voice ________ the others will know of our plan,' Ray told me.",
        "options": ["or", "if", "but", "and"],
        "answer": "or"
    },
    60: {
        "question": "Choose the best answer from the given options: 'Would you like to have fruits ________ ice-cream for dessert?' the waitress asked us.",
        "options": ["or", "but", "for", "as"],
        "answer": "or"
    },
    61: {
        "question": "The sentence that states the main idea of a paragraph is called:",
        "options": ["Topic sentence", "Main idea of paragraph", "Topic of paragraph", "Supporting details"],
        "answer": "Topic sentence"
    },
    62: {
        "question": "Complete the sentence: 'We want to ________ this product to women.'",
        "options": ["market", "marketer", "marketing", "marketable"],
        "answer": "market"
    },
    65: {
        "question": "Choose the best available substitute word for the following root/prefix: Ann/Enn",
        "options": ["year", "month", "day", "time"],
        "answer": "year"
    },
    76: {
        "question": "Choose the best meaning for the word in capital letters: 'There is an OPTIMUM way to approach each kind of exam question.'",
        "options": ["Best", "Most favorable", "Annoying", "Inconvenience"],
        "answer": "Best"
    },
    94: {
        "question": "Choose the best option: 'You must not ________ the animals in the zoo.'",
        "options": ["feed", "feeding", "feeds", "fed"],
        "answer": "feed"
    },
    114: {
        "question": "Choose the correct option: 'I liked the car, ________ I bought it.'",
        "options": ["so", "even so", "far", "even"],
        "answer": "so"
    },
    119: {
        "question": "Choose the correct option: 'We ________ sold better garden tools.'",
        "options": ["have never", "never have", "has never", "never has"],
        "answer": "have never"
    },
    124: {
        "question": "Choose the correct option: Antonym of 'significant' is:",
        "options": ["Insignificant", "Cumulative", "Absolute", "Important"],
        "answer": "Insignificant"
    },
    130: {
        "question": "Choose the correct punctuation for the given sentence: 'Oh! I forgot to bring the cookies.'",
        "options": ["Oh! I forgot to bring the cookies.", "I, forgot to bring the cookies.", "Oh I forgot to, bring the cookies.", "No error"],
        "answer": "Oh! I forgot to bring the cookies."
    },
    140: {
        "question": "Choose the noun in the given sentence: 'The purple grapes are delicious.'",
        "options": ["grapes", "The", "purple", "delicious"],
        "answer": "grapes"
    },
    141: {
        "question": "Choose the noun in the given sentence: 'It will take all of your energy and you will be able to walk again.'",
        "options": ["energy", "all", "your", "again"],
        "answer": "energy"
    },
    167: {
        "question": "Complete the sentence by choosing the best pair of connectives: '________ the men ________ their supervisor is to be blamed for the mishap.'",
        "options": ["Neither...nor", "Either...or", "Both...and", "Neither...and"],
        "answer": "Neither...nor"
    },
    168: {
        "question": "Complete the sentence by choosing the best pair of connectives: 'Each class is to present ________ a drama ________ a song for the concert.'",
        "options": ["either...or", "neither...nor", "both...and", "both...or"],
        "answer": "either...or"
    },
    171: {
        "question": "Complete the sentence by choosing the best option: 'The children at the deaf-mute centre can ________ hear ________ speak.'",
        "options": ["neither...nor", "either...or", "both...and", "neither...and"],
        "answer": "neither...nor"
    },
    172: {
        "question": "Complete the sentence by choosing the best option: 'They can watch ________ the detective series ________ the foreign movie.'",
        "options": ["either...or", "neither...nor", "both...and", "either...then"],
        "answer": "either...or"
    },
    173: {
        "question": "Complete the sentence by choosing the best option: 'We are planning to go to ________ Spain ________ France during the holidays.'",
        "options": ["either...or", "neither...nor", "both...and", "neither...and"],
        "answer": "either...or"
    },
    181: {
        "question": "Complete the sentence by choosing the correct option: 'You must have been ________ daydreaming ________ sleeping in class again.'",
        "options": ["Either...or", "Neither...nor", "Both...and", "Neither...or"],
        "answer": "Either...or"
    },
    187: {
        "question": "Dead and alive are examples of:",
        "options": ["Antonyms", "Synonyms", "Homophones", "Spelling"],
        "answer": "Antonyms"
    },
    188: {
        "question": "In an academic examination, what is the policy regarding unfair means?",
        "options": ["Virtual University takes serious note of unfair means.", "Unfair means are permitted.", "There is no policy.", "None of the above"],
        "answer": "Virtual University takes serious note of unfair means."
    },
    189: {
        "question": "In an academic examination, what is the policy regarding unfair means?",
        "options": ["Virtual University takes serious note of unfair means.", "Unfair means are permitted.", "There is no policy.", "None of the above"],
        "answer": "Virtual University takes serious note of unfair means."
    },
    193: {
        "question": "Fill in the blank by selecting past progressive verb from the given choices: 'While they were ________, he played the piano.'",
        "options": ["singing", "sang", "sing", "sung"],
        "answer": "singing"
    },
    194: {
        "question": "Fill in the blank with appropriate connector: 'With neither a naturally aggressive disposition ________ particularly large size, the mimic octopus survives easily.'",
        "options": ["nor a", "or its", "with its", "and a"],
        "answer": "nor a"
    },
    201: {
        "question": "Fill in the blank with appropriate phrasal verb: 'An eagle, if pressed for food, might ________ a small fish.'",
        "options": ["carry off", "carry out", "carry on", "carry away"],
        "answer": "carry off"
    },
    228: {
        "question": "Fill in the blank with the correct spelling of the word: ________",
        "options": ["ecstasy", "ecstacy", "extasy", "exstacy"],
        "answer": "ecstasy"
    },
    231: {
        "question": "Fill in the blank with the correct spelling of the word: ________",
        "options": ["battalion", "battalian", "batallion", "batalion"],
        "answer": "battalion"
    },
    282: {
        "question": "Identify the statement as True or False: 'While' is a transitional marker which shows contrast.",
        "options": ["True", "False"],
        "answer": "True"
    },
    283: {
        "question": "Identify the statement as True or False: 'The suffix ‘-er’ is categorized as a verb-forming suffix.'",
        "options": ["True", "False"],
        "answer": "False"
    },
    305: {
        "question": "JavaScript stores all numbers internally as:",
        "options": ["Double-precision 64-bit floating point numbers", "Strings", "Integers", "Booleans"],
        "answer": "Double-precision 64-bit floating point numbers"
    },
    307: {
        "question": "Label the statement given below by choosing the most appropriate tone from the options: 'Pakistan will win the World Cup.'",
        "options": ["Optimistic", "Humorous", "Cynical", "Sarcastic"],
        "answer": "Optimistic"
    },
    308: {
        "question": "Label the statement given below by choosing the most appropriate tone from the options: 'Pakistan will win the World Cup.'",
        "options": ["Optimistic", "Humorous", "Cynical", "Sarcastic"],
        "answer": "Optimistic"
    },
    312: {
        "question": "Mark the statement as True or False: 'A prefix is added to the end of a root word.'",
        "options": ["True", "False"],
        "answer": "False"
    },
    314: {
        "question": "Mention the adverb used in the given sentence: 'He worked the sum quickly.'",
        "options": ["quickly", "worked", "sum", "He"],
        "answer": "quickly"
    },
    319: {
        "question": "Fill in the blank: 'My brother ________ in bed all day yesterday.'",
        "options": ["lay", "lied", "laid", "lain"],
        "answer": "lay"
    },
    322: {
        "question": "A logical fallacy that offers only two choices when more exist in reality is called:",
        "options": ["Either/or fallacy", "Overgeneralization", "Ad hominem", "Red herring"],
        "answer": "Either/or fallacy"
    },
    323: {
        "question": "One cause of slow reading is ________, which means forming the sounds of each word with lips or vocal cords.",
        "options": ["Vocalization", "Listening", "Skimming", "Scanning"],
        "answer": "Vocalization"
    },
    362: {
        "question": "Scanning means to:",
        "options": ["locate specific information or facts", "understand the gist", "read for leisure", "memorize vocabulary"],
        "answer": "locate specific information or facts"
    },
    368: {
        "question": "Situational irony occurs when the discrepancy lies in the:",
        "options": ["situation itself", "words spoken", "audience knowledge", "reading process"],
        "answer": "situation itself"
    },
    372: {
        "question": "Sounds produced with a complete or partial stoppage of breath are called:",
        "options": ["consonants", "vowels", "diphthongs", "triphthongs"],
        "answer": "consonants"
    },
    375: {
        "question": "The adjective form of 'courage' is:",
        "options": ["courageous", "courageousness", "encourage", "courageously"],
        "answer": "courageous"
    },
    380: {
        "question": "Fill in the blank: 'The library has been incredibly ________ today.'",
        "options": ["quiet", "quit", "quite", "quietly"],
        "answer": "quiet"
    },
    381: {
        "question": "The meaning of the stem 'mal' in the word 'malediction' is:",
        "options": ["bad / evil", "lessen", "good", "large"],
        "answer": "bad / evil"
    },
    384: {
        "question": "The nephew is ________ than his uncle.",
        "options": ["older", "elder", "oldest", "eldest"],
        "answer": "older"
    },
    385: {
        "question": "The organization insists that it is ________ and does not identify with any one political party.",
        "options": ["impolitical / non-political", "political", "hyper-political", "pan-political"],
        "answer": "impolitical / non-political"
    },
    394: {
        "question": "The bold words at the top of a dictionary page indicating the first and last entries are called:",
        "options": ["Guide words", "Base words", "Root words", "Key words"],
        "answer": "Guide words"
    },
    401: {
        "question": "There is no reason ________ anyone should behave so cruelly.",
        "options": ["why", "which", "what", "who"],
        "answer": "why"
    },
    412: {
        "question": "Mark the statement as True or False: 'Vocalization does not affect reading speed at all.'",
        "options": ["True", "False"],
        "answer": "False"
    },
    427: {
        "question": "What is the difference between a claim and a fact?",
        "options": ["A fact is an objectively verifiable truth, while a claim is an assertion that requires evidence.", "A claim is a proven truth, while a fact is a personal belief.", "A claim is used in poetry, while a fact is used in prose."],
        "answer": "A fact is an objectively verifiable truth, while a claim is an assertion that requires evidence."
    },
    428: {
        "question": "What is the difference between a claim and a fact?",
        "options": ["A fact is an objectively verifiable truth, while a claim is an assertion that requires evidence.", "A claim is a proven truth, while a fact is a personal belief.", "A claim is used in poetry, while a fact is used in prose."],
        "answer": "A fact is an objectively verifiable truth, while a claim is an assertion that requires evidence."
    },
    429: {
        "question": "What is the difference between a comma and a semicolon?",
        "options": ["A semicolon connects two independent clauses without a conjunction, while a comma connects them with a coordinating conjunction.", "A comma connects two independent clauses without a conjunction, while a semicolon connects them with a coordinating conjunction.", "A comma is used only in poetry, while a semicolon is used in prose."],
        "answer": "A semicolon connects two independent clauses without a conjunction, while a comma connects them with a coordinating conjunction."
    },
    430: {
        "question": "What is the difference between a comma and a semicolon?",
        "options": ["A semicolon connects two independent clauses without a conjunction, while a comma connects them with a coordinating conjunction.", "A comma connects two independent clauses without a conjunction, while a semicolon connects them with a coordinating conjunction.", "A comma is used only in poetry, while a semicolon is used in prose."],
        "answer": "A semicolon connects two independent clauses without a conjunction, while a comma connects them with a coordinating conjunction."
    },
    431: {
        "question": "What is the difference between a comparison and a contrast essay?",
        "options": ["A comparison highlights similarities, while a contrast highlights differences.", "A comparison shows differences, while a contrast shows similarities.", "A comparison is used in poetry, while a contrast is used in prose."],
        "answer": "A comparison highlights similarities, while a contrast highlights differences."
    },
    432: {
        "question": "What is the difference between a comparison and a contrast essay?",
        "options": ["A comparison highlights similarities, while a contrast highlights differences.", "A comparison shows differences, while a contrast shows similarities.", "A comparison is used in poetry, while a contrast is used in prose."],
        "answer": "A comparison highlights similarities, while a contrast highlights differences."
    },
    435: {
        "question": "What is the difference between a narrative and a descriptive essay?",
        "options": ["A narrative essay tells a story, while a descriptive essay paints a picture of a person, place, or object.", "A narrative describes a place or object, while a descriptive essay tells a story.", "A narrative is used in poetry, while a descriptive essay is used in prose."],
        "answer": "A narrative essay tells a story, while a descriptive essay paints a picture of a person, place, or object."
    },
    436: {
        "question": "What is the difference between a narrative and a descriptive essay?",
        "options": ["A narrative essay tells a story, while a descriptive essay paints a picture of a person, place, or object.", "A narrative describes a place or object, while a descriptive essay tells a story.", "A narrative is used in poetry, while a descriptive essay is used in prose."],
        "answer": "A narrative essay tells a story, while a descriptive essay paints a picture of a person, place, or object."
    },
    439: {
        "question": "What is the difference between a phrase and a clause?",
        "options": ["A clause contains a subject and a predicate, while a phrase does not.", "A phrase is a complete sentence, while a clause is a group of words.", "A phrase is used in informal writing, while a clause is used in formal writing."],
        "answer": "A clause contains a subject and a predicate, while a phrase does not."
    },
    440: {
        "question": "What is the difference between a phrase and a clause?",
        "options": ["A clause contains a subject and a predicate, while a phrase does not.", "A phrase is a complete sentence, while a clause is a group of words.", "A phrase is used in informal writing, while a clause is used in formal writing."],
        "answer": "A clause contains a subject and a predicate, while a phrase does not."
    },
    443: {
        "question": "What is the difference between a simile and a metaphor?",
        "options": ["A simile uses 'like' or 'as' to make a comparison, while a metaphor makes a direct comparison without 'like' or 'as'.", "A simile makes a direct comparison, while a metaphor uses 'like' or 'as'.", "A simile is used in poetry, while a metaphor is used in prose."],
        "answer": "A simile uses 'like' or 'as' to make a comparison, while a metaphor makes a direct comparison without 'like' or 'as'."
    },
    444: {
        "question": "What is the difference between a simile and a metaphor?",
        "options": ["A simile uses 'like' or 'as' to make a comparison, while a metaphor makes a direct comparison without 'like' or 'as'.", "A simile makes a direct comparison, while a metaphor uses 'like' or 'as'.", "A simile is used in poetry, while a metaphor is used in prose."],
        "answer": "A simile uses 'like' or 'as' to make a comparison, while a metaphor makes a direct comparison without 'like' or 'as'."
    },
    445: {
        "question": "What is the difference between a summary and an analysis?",
        "options": ["A summary is a brief overview of main points, while an analysis is a detailed examination.", "A summary is a detailed examination, while an analysis is a brief overview.", "A summary is used in poetry, while an analysis is used in prose."],
        "answer": "A summary is a brief overview of main points, while an analysis is a detailed examination."
    },
    446: {
        "question": "What is the difference between a summary and an analysis?",
        "options": ["A summary is a brief overview of main points, while an analysis is a detailed examination.", "A summary is a detailed examination, while an analysis is a brief overview.", "A summary is used in poetry, while an analysis is used in prose."],
        "answer": "A summary is a brief overview of main points, while an analysis is a detailed examination."
    },
    447: {
        "question": "What is the difference between a topic sentence and a thesis statement?",
        "options": ["A topic sentence states the main idea of a paragraph, while a thesis statement states the central argument of an entire essay.", "A topic sentence is a specific argument, while a thesis statement is a general statement.", "A topic sentence is used in poetry, while a thesis statement is used in prose."],
        "answer": "A topic sentence states the main idea of a paragraph, while a thesis statement states the central argument of an entire essay."
    },
    448: {
        "question": "What is the difference between a topic sentence and a thesis statement?",
        "options": ["A topic sentence states the main idea of a paragraph, while a thesis statement states the central argument of an entire essay.", "A topic sentence is a specific argument, while a thesis statement is a general statement.", "A topic sentence is used in poetry, while a thesis statement is used in prose."],
        "answer": "A topic sentence states the main idea of a paragraph, while a thesis statement states the central argument of an entire essay."
    },
    451: {
        "question": "What is the difference between connotation and denotation?",
        "options": ["Denotation is the literal dictionary meaning of a word, while connotation is the emotional or cultural association.", "Connotation is the literal meaning of a word, while denotation is the emotional association.", "Connotation is used in poetry, while denotation is used in prose."],
        "answer": "Denotation is the literal dictionary meaning of a word, while connotation is the emotional or cultural association."
    },
    452: {
        "question": "What is the difference between connotation and denotation?",
        "options": ["Denotation is the literal dictionary meaning of a word, while connotation is the emotional or cultural association.", "Connotation is the literal meaning of a word, while denotation is the emotional association.", "Connotation is used in poetry, while denotation is used in prose."],
        "answer": "Denotation is the literal dictionary meaning of a word, while connotation is the emotional or cultural association."
    },
    453: {
        "question": "What is the difference between persuasion and manipulation?",
        "options": ["Persuasion uses logic, evidence, and honest reasoning, while manipulation uses deception and emotional exploitation.", "Persuasion uses emotions and deceit, while manipulation uses logic and evidence.", "Persuasion is used in poetry, while manipulation is used in prose."],
        "answer": "Persuasion uses logic, evidence, and honest reasoning, while manipulation uses deception and emotional exploitation."
    },
    454: {
        "question": "What is the difference between persuasion and manipulation?",
        "options": ["Persuasion uses logic, evidence, and honest reasoning, while manipulation uses deception and emotional exploitation.", "Persuasion uses emotions and deceit, while manipulation uses logic and evidence.", "Persuasion is used in poetry, while manipulation is used in prose."],
        "answer": "Persuasion uses logic, evidence, and honest reasoning, while manipulation uses deception and emotional exploitation."
    },
    456: {
        "question": "What is the first step in the writing process?",
        "options": ["Prewriting / Planning", "Editing and proofreading", "Drafting", "Publishing"],
        "answer": "Prewriting / Planning"
    },
    457: {
        "question": "What is the primary function of a verb in a sentence?",
        "options": ["To express an action or state of being", "To connect two clauses", "To modify a noun", "To replace a noun"],
        "answer": "To express an action or state of being"
    },
    462: {
        "question": "What is the main purpose of an introduction in an essay?",
        "options": ["To introduce the topic and state the thesis statement", "To summarize the main points", "To provide evidence and support", "To list counterarguments"],
        "answer": "To introduce the topic and state the thesis statement"
    },
    463: {
        "question": "What is the main purpose of argumentative writing?",
        "options": ["To convince the reader of a position using logic and evidence", "To summarize information", "To entertain the reader", "To describe personal feelings"],
        "answer": "To convince the reader of a position using logic and evidence"
    },
    467: {
        "question": "What is the purpose of a conclusion in an essay?",
        "options": ["To summarize the main points and provide closure", "To provide evidence and support", "To introduce a brand new argument", "To confuse the reader"],
        "answer": "To summarize the main points and provide closure"
    },
    468: {
        "question": "What is the purpose of a thesis statement?",
        "options": ["To state the central argument or main point of the essay", "To provide evidence and support", "To conclude the essay", "To ask a rhetorical question"],
        "answer": "To state the central argument or main point of the essay"
    },
    469: {
        "question": "What is the purpose of addressing counterarguments in argumentative writing?",
        "options": ["To acknowledge and refute opposing viewpoints to strengthen one’s own argument", "To summarize information", "To confuse the reader", "To agree with the opponent"],
        "answer": "To acknowledge and refute opposing viewpoints to strengthen one’s own argument"
    },
    470: {
        "question": "What is the purpose of body paragraphs in an essay?",
        "options": ["To develop and support the thesis statement with evidence and explanations", "To summarize the main points", "To introduce the essay topic", "To provide general greetings"],
        "answer": "To develop and support the thesis statement with evidence and explanations"
    },
    471: {
        "question": "What is the purpose of brainstorming in the writing process?",
        "options": ["To generate ideas and explore topics freely", "To edit punctuation errors", "To print the final paper", "To format citations"],
        "answer": "To generate ideas and explore topics freely"
    },
    473: {
        "question": "What is the purpose of identifying the author's purpose in reading?",
        "options": ["To understand why the author wrote the text and evaluate potential bias", "To agree with the author's opinion", "To memorize the text verbatim", "To count words"],
        "answer": "To understand why the author wrote the text and evaluate potential bias"
    },
    479: {
        "question": "What is the purpose of using emotional appeals in persuasive writing?",
        "options": ["To connect with the audience’s feelings and values (pathos)", "To summarize information", "To list factual data", "To check spelling"],
        "answer": "To connect with the audience’s feelings and values (pathos)"
    },
    480: {
        "question": "What is the purpose of using evidence in argumentative writing?",
        "options": ["To substantiate claims and prove the author’s argument", "To summarize information", "To distract the reader", "To lengthen the essay"],
        "answer": "To substantiate claims and prove the author’s argument"
    },
    481: {
        "question": "What is the purpose of using examples in writing?",
        "options": ["To clarify abstract ideas and provide concrete illustrations", "To confuse the reader with complexity", "To avoid stating the main point", "To replace the thesis"],
        "answer": "To clarify abstract ideas and provide concrete illustrations"
    },
    482: {
        "question": "What is the purpose of using figurative language in writing?",
        "options": ["To create vivid imagery and enhance meaning", "To impress the reader with jargon", "To replace proper grammar", "To shorten paragraphs"],
        "answer": "To create vivid imagery and enhance meaning"
    },
    483: {
        "question": "What is the purpose of using rhetorical devices in persuasive writing?",
        "options": ["To effectively persuade and engage the audience", "To impress the reader with jargon", "To avoid logic", "To hide the main argument"],
        "answer": "To effectively persuade and engage the audience"
    },
    489: {
        "question": "Which of the following is true of the sentence: 'When crows flew.'?",
        "options": ["It is a sentence fragment / dependent clause.", "It is a complete compound sentence.", "It is an imperative sentence.", "It contains no predicate."],
        "answer": "It is a sentence fragment / dependent clause."
    },
    514: {
        "question": "Which one of the following is NOT an ADVERB?",
        "options": ["Beautiful", "Quickly", "Yesterday", "Luckily"],
        "answer": "Beautiful"
    },
    515: {
        "question": "Which one of the following statements expresses an Opinion?",
        "options": ["William Shakespeare is the greatest English writer.", "Cambodia is south of Thailand.", "Nine out of ten respondents answered the questions correctly.", "Water boils at 100 degrees Celsius."],
        "answer": "William Shakespeare is the greatest English writer."
    },
    516: {
        "question": "Which one of the following statements expresses an Opinion?",
        "options": ["William Shakespeare is the greatest English writer.", "Cambodia is south of Thailand.", "Nine out of ten respondents answered the questions correctly.", "Water boils at 100 degrees Celsius."],
        "answer": "William Shakespeare is the greatest English writer."
    },
    517: {
        "question": "Which one of the following statements expresses a Fact?",
        "options": ["In 2005, Brazil and FC Barcelona star Ronaldinho was named FIFA World Player of the Year.", "Professor Ahmad Khan argues that the effect of carbon emissions is exaggerated.", "This product might cause stomach upset for some people in years to come.", "Local councilors should spend more time listening to residents."],
        "answer": "In 2005, Brazil and FC Barcelona star Ronaldinho was named FIFA World Player of the Year."
    },
    523: {
        "question": "Which of the following words means 'tranquil'?",
        "options": ["Peaceful", "Plague", "Noisy", "Violent"],
        "answer": "Peaceful"
    },
    529: {
        "question": "While being biased is unavoidable, writers try to remain ________.",
        "options": ["Objective", "Subjective", "Partial", "Biased"],
        "answer": "Objective"
    },
    530: {
        "question": "While being biased is unavoidable, writers try to remain ________.",
        "options": ["Objective", "Subjective", "Partial", "Biased"],
        "answer": "Objective"
    },
    531: {
        "question": "'While' is a transitional marker which shows contrast.",
        "options": ["True", "False"],
        "answer": "True"
    },
    533: {
        "question": "Write the COMPARATIVE form of the adjective: 'Kind'",
        "options": ["Kinder", "Kindest", "More kindest", "Kindly"],
        "answer": "Kinder"
    },
    540: {
        "question": "Choose the best answer: 'He wanted to join the navy ________ his parents would not let him.'",
        "options": ["but", "if", "either", "because"],
        "answer": "but"
    },
    542: {
        "question": "James was so worried about his coming examination results that he could ________ sleep ________ eat properly.",
        "options": ["neither...nor", "either...or", "both...and", "both...or"],
        "answer": "neither...nor"
    },
    543: {
        "question": "Mother said, 'You ________ help me prepare dinner ________ do your homework.'",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    544: {
        "question": "Choose the best answer: 'Mr. James cannot speak English ________ he can speak Mandarin very well.'",
        "options": ["but", "because", "since", "while"],
        "answer": "but"
    },
    547: {
        "question": "They can watch ________ the detective series ________ the foreign movie.",
        "options": ["either...or", "neither...nor", "both...and", "neither...and"],
        "answer": "either...or"
    },
    548: {
        "question": "You must have been either daydreaming or sleeping in class again.",
        "options": ["Either...or", "Neither...nor", "Both...and", "Neither...or"],
        "answer": "Either...or"
    },
    549: {
        "question": "________ the men ________ their supervisor is to be blamed for the mishap.",
        "options": ["Neither...nor", "Either...or", "Both...and", "Either...nor"],
        "answer": "Neither...nor"
    },
    550: {
        "question": "Choose the best answer: 'Could I come over at ________ three ________ four o\\'clock?' asked Joan.",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    552: {
        "question": "Choose the best answer: 'Would you like to have fruit juice ________ coffee?' asked the hostess.",
        "options": ["or", "as", "but", "for"],
        "answer": "or"
    },
    553: {
        "question": "Choose the antonym for the underlined word: 'Sunglasses will only hinder your ability to see at night.'",
        "options": ["help", "accept", "block", "delay"],
        "answer": "help"
    },
    563: {
        "question": "Fill in the blank with appropriate verb: '________ get tired of answering the phone?'",
        "options": ["Do you ever", "Have you ever", "Are you ever", "Did you ever"],
        "answer": "Do you ever"
    },
    564: {
        "question": "Fill in the blank with appropriate verb: '________ anyone object if I open the window?'",
        "options": ["Does", "Doing", "Do", "Is"],
        "answer": "Does"
    },
    572: {
        "question": "Fill in the blank with appropriate verb: 'In Europe, a defined system of measurements ________.'",
        "options": ["is extensively used", "will have extensively used", "are extensively used", "using extensively"],
        "answer": "is extensively used"
    },
    575: {
        "question": "You must have been either daydreaming or sleeping in class again.",
        "options": ["Either...or", "Neither...nor", "Both...and", "Neither...or"],
        "answer": "Either...or"
    },
    593: {
        "question": "Which of the following is true of the example: 'A man had just married a rustic girl.'?",
        "options": ["It is a simple sentence.", "It is a complex sentence.", "It is a compound sentence.", "It is a compound-complex sentence."],
        "answer": "It is a simple sentence."
    },
    596: {
        "question": "Which of the following is true of the example: 'You might hurt yourself if you don\\'t watch out.'?",
        "options": ["It contains an adverbial clause of condition.", "It contains an appositive phrase.", "It is a simple sentence.", "It contains a noun clause."],
        "answer": "It contains an adverbial clause of condition."
    },
    598: {
        "question": "Which of the following is true of the sentence: 'Whereas, no one could believe that she was capable of such cruelty.'?",
        "options": ["It is a sentence fragment / dependent clause.", "It is a comma splice.", "It is a complete simple sentence.", "It is a compound sentence."],
        "answer": "It is a sentence fragment / dependent clause."
    },
    599: {
        "question": "Which of the following is true of the sentence: 'Whereas, no one could believe that she was capable of such cruelty.'?",
        "options": ["It is a sentence fragment / dependent clause.", "It is a comma splice.", "It is a complete simple sentence.", "It is a compound sentence."],
        "answer": "It is a sentence fragment / dependent clause."
    },
    605: {
        "question": "Choose the correct transitional word: 'We live in the same building; ________, we hardly see each other.'",
        "options": ["however", "furthermore", "moreover", "consequently"],
        "answer": "however"
    },
    614: {
        "question": "Fill in the blank: '________ it was cold and windy, I went out.'",
        "options": ["Although", "However", "Despite", "Because"],
        "answer": "Although"
    },
    624: {
        "question": "Complete the sentence: 'Each class is to present ________ a drama ________ a song for the concert.'",
        "options": ["either...or", "neither...nor", "both...and", "either...and"],
        "answer": "either...or"
    },
    636: {
        "question": "Choose the correct option: 'We ________ sold better garden tools.'",
        "options": ["have never", "never have", "has never", "never has"],
        "answer": "have never"
    },
    638: {
        "question": "Complete the sentence: 'It was an expensive vase, ________ they bought it to please their mother.'",
        "options": ["but", "either", "as", "if"],
        "answer": "but"
    },
    640: {
        "question": "Complete the sentence: 'The children at the deaf-mute centre can ________ hear ________ speak.'",
        "options": ["neither...nor", "either...or", "both...and", "neither...and"],
        "answer": "neither...nor"
    },
    641: {
        "question": "Complete the sentence: 'They can watch ________ the detective series ________ the foreign movie.'",
        "options": ["either...or", "neither...nor", "both...and", "neither...and"],
        "answer": "either...or"
    },
    642: {
        "question": "Complete the sentence: 'We are planning to go to ________ Spain ________ France during the holidays.'",
        "options": ["either...or", "neither...nor", "both...and", "neither...and"],
        "answer": "either...or"
    },
    643: {
        "question": "Complete the sentence: 'Could I come over at ________ three ________ four o\\'clock?' asked Joan.",
        "options": ["either...or", "neither...nor", "both...and", "neither...or"],
        "answer": "either...or"
    },
    644: {
        "question": "Complete the sentence: 'Would you marry a man who had ________ fame ________ money?' Mary asked her best friend.",
        "options": ["neither...nor", "either...or", "both...and", "neither...or"],
        "answer": "neither...nor"
    },
    645: {
        "question": "Complete the sentence: 'You must have been ________ daydreaming ________ sleeping in class again.'",
        "options": ["Either...or", "Neither...nor", "Both...and", "Neither...or"],
        "answer": "Either...or"
    },
    650: {
        "question": "Click on the option that you think is correct: 'Marijuana is less toxic than alcohol or tobacco, ________ some people believe it should be legalized.'",
        "options": ["so", "because", "as", "since"],
        "answer": "so"
    },
    651: {
        "question": "Click on the option that you think is correct: 'Marijuana is less toxic than alcohol or tobacco, ________ some people believe it should be legalized.'",
        "options": ["so", "because", "as", "since"],
        "answer": "so"
    },
    652: {
        "question": "Choose the best meaning for the highlighted word: 'A student of contemporary art must also study the classic works of artists from the past, recognizing that modern art owes much to the former.'",
        "options": ["former", "religious", "modern", "not having to do with religion"],
        "answer": "former"
    },
    653: {
        "question": "Choose the best meaning for the underlined word: 'There is an optimum way to approach each kind of exam question.'",
        "options": ["best", "time-consuming", "annoying", "inconvenience"],
        "answer": "best"
    },
    659: {
        "question": "Which of the following is a sentence fragment?",
        "options": ["Because the dog would not bite him.", "The dog will not bite him.", "He called his friend yesterday.", "They went to the market."],
        "answer": "Because the dog would not bite him."
    },
    667: {
        "question": "Which of the following is true of the sentence: 'When crows flew.'?",
        "options": ["It is a sentence fragment / dependent clause.", "Who borrowed Stefanie's car Saturday night.", "It is a compound sentence.", "It is an independent clause."],
        "answer": "It is a sentence fragment / dependent clause."
    },
    668: {
        "question": "Choose the phrasal verb most similar in meaning to: 'Refuse'",
        "options": ["Turn down", "Turn up", "Turn on", "Turn off"],
        "answer": "Turn down"
    },
    669: {
        "question": "Choose the phrasal verb most similar in meaning to: 'Wear'",
        "options": ["Have on", "Take off", "Put away", "Turn on"],
        "answer": "Have on"
    }
}

# -------------------------------------------------------------
# 3. Clean and verify all 671 MCQs
# -------------------------------------------------------------
verified_mcqs = []
corrected_mcq_count = 0

for m in mcqs:
    mid = m['id']
    if mid in MCQ_OVERRIDES:
        ov = MCQ_OVERRIDES[mid]
        m['question'] = ov['question']
        m['options'] = ov['options']
        m['answer'] = ov['answer']
        m['solution_notes'] = f"Verified by Senior SME: {ov['answer']}"
        corrected_mcq_count += 1
    else:
        # Standard cleaning
        orig_q = m['question']
        orig_opts = list(m['options'])
        orig_ans = m['answer']
        
        cleaned_q = clean_watermarks_from_question(orig_q)
        cleaned_opts = [clean_option(o) for o in orig_opts]
        cleaned_ans = clean_option(orig_ans)
        
        # Deduplicate options while preserving order
        unique_opts = []
        for o in cleaned_opts:
            if o and o not in unique_opts:
                unique_opts.append(o)
                
        # Ensure answer is in options
        if cleaned_ans not in unique_opts:
            # Check case-insensitive match
            found = False
            for uo in unique_opts:
                if uo.lower() == cleaned_ans.lower():
                    cleaned_ans = uo
                    found = True
                    break
            if not found:
                unique_opts.append(cleaned_ans)
                
        if cleaned_q != orig_q or cleaned_opts != orig_opts or cleaned_ans != orig_ans:
            corrected_mcq_count += 1
            
        m['question'] = cleaned_q
        m['options'] = unique_opts
        m['answer'] = cleaned_ans

    verified_mcqs.append(m)

print(f"MCQs Audited: {len(verified_mcqs)} | Corrected/Refined: {corrected_mcq_count}")

# -------------------------------------------------------------
# 4. Master Model Answers for all 57 Subjective Questions
# -------------------------------------------------------------
SUBJECTIVE_MODEL_ANSWERS = {
    1: """1. permitted (suffix: -ed, from permit + ed, with doubling of final consonant)
2. repaved (suffix: -ed, past participle form of repave)
3. planning (suffix: -ing, present participle of plan, with doubling of final consonant)""",

    2: """Advantages of Graphs and Interpretation of Visual Data:
1. Advantages of Graphs:
   - Visual Clarity: Transforms complex numerical data and statistics into clear, easily digestible visual representations and relationships.
   - Rapid Comparison: Enables readers to quickly compare multiple variables, quantities, and categories across continuous timelines without reading dense prose.
   - Identifying Trends: Instantly highlights highs, lows, anomalies, fluctuations, and rates of growth or decline.
2. Interpretation of Visual Data:
   - Visual aids (graphs, charts, diagrams, tables, and maps) supplement textual information to enhance reading comprehension.
   - To interpret visual data accurately, readers must:
     a) Read the title, labels, and legend carefully to determine what variables are being measured.
     b) Examine the horizontal X-axis (independent variable) and vertical Y-axis (dependent variable) including scale units.
     c) Identify the overall trend, key turning points, and relationships between datasets before drawing logical conclusions.""",

    3: """Correct choices and grammatical explanations:
1. 'accept' (verb meaning to receive willingly; 'except' is a preposition meaning excluding).
2. 'advise' (verb meaning to offer recommendations; 'advice' is the noun).
3. 'fewer' (quantifier used with countable plural nouns such as 'compliments'; 'less' is used with uncountable quantities).
4. 'it's' (contraction for 'it is'; 'its' is the possessive pronoun).

Complete Correct Sentence:
"I accept all your compliments, but I advise you to offer fewer of them at a time because it's not good for a person to hear too many positive things about himself in one day.\"""",

    4: """Correct completed narrative:
"Once a man dug a well in the jungle to trap wild elephants. After some days, the man was chased by a lion, fell into the well, and was followed by the beast a second later.\"""",

    5: """Definitions and Examples of Simple, Compound, and Complex Sentences:
1. Simple Sentence:
   - Definition: Contains a single independent clause consisting of a subject and a predicate, and expresses a complete thought.
   - Example: "The train arrived on time despite the heavy snowfall."
2. Compound Sentence:
   - Definition: Contains two or more independent clauses joined by a coordinating conjunction (FANBOYS: for, and, nor, but, or, yet, so) or a semicolon.
   - Example: "She studied diligently for the examination, but she was still nervous about the result."
3. Complex Sentence:
   - Definition: Contains one independent clause and at least one dependent (subordinate) clause introduced by a subordinating conjunction (e.g., although, because, since, while, if) or a relative pronoun (who, which, that).
   - Example: "Although it was raining heavily, the athletic competition continued as scheduled.\"""",

    6: """Definition of Gerund with Examples:
A gerund is the present participle form of a verb ending in '-ing' that functions grammatically as a noun within a sentence. Because it acts as a noun, a gerund can serve in various syntactic positions:
1. As Subject: "Swimming is considered an excellent full-body cardiovascular exercise."
2. As Direct Object: "She genuinely enjoys reading classic literature in her leisure time."
3. As Subject Complement: "His favorite outdoor hobby is gardening."
4. As Object of a Preposition: "They succeeded in winning the championship by practicing daily.\"""",

    7: """Definition of Infinitive:
An infinitive is the base form of a verb typically preceded by the particle 'to' (to + base verb). It functions as a verbal noun, an adjective, or an adverb, rather than a finite verb:
1. As a Noun (Subject): "To err is human; to forgive is divine."
2. As a Noun (Direct Object): "She hopes to study linguistics abroad."
3. As an Adjective (modifying a noun): "He was given a difficult assignment to finish before noon."
4. As an Adverb (modifying a verb or adjective): "We stopped at the roadside station to buy food."
Note: When an infinitive occurs without the particle 'to' (after modal verbs or verbs of perception), it is called a 'bare infinitive' (e.g., 'She made him laugh').""",

    8: """Definition of Line in a Line Chart:
A line in a line graph is a continuous visual line connecting individual plotted data points across Cartesian coordinates.
Functions and Characteristics:
1. Axes Representation: The horizontal X-axis represents the independent variable (frequently continuous time intervals such as days, months, or years), while the vertical Y-axis represents the dependent quantitative variable.
2. Depicts Continuous Trends: It clearly illustrates patterns of continuity, trends, fluctuations, acceleration, and deceleration of values over time.
3. Multi-Dataset Comparison: Multiple lines with distinct colors or styles can be plotted simultaneously on the same grid to compare trends between different groups or variables.""",

    9: """Definition of Line in a Line Chart:
A line in a line graph is a continuous visual line connecting individual plotted data points across Cartesian coordinates.
Functions and Characteristics:
1. Axes Representation: The horizontal X-axis represents the independent variable (frequently continuous time intervals such as days, months, or years), while the vertical Y-axis represents the dependent quantitative variable.
2. Depicts Continuous Trends: It clearly illustrates patterns of continuity, trends, fluctuations, acceleration, and deceleration of values over time.
3. Multi-Dataset Comparison: Multiple lines with distinct colors or styles can be plotted simultaneously on the same grid to compare trends between different groups or variables.""",

    10: """Definition of the Term Gerund:
A gerund is a non-finite verb form ending in '-ing' that functions syntactically as a noun in a sentence.
Key Roles with Examples:
1. Subject of Verb: "Jogging every morning keeps him healthy."
2. Object of Verb: "He admitted making a serious mistake."
3. Object of Preposition: "She is thinking of leaving her current job."
4. Subject Complement: "Her primary passion is teaching.\"""",

    11: """Types of Irony in English Literature and Comprehension:
Irony is a rhetorical device or literary technique involving a contradiction between appearance and reality. The three primary types are:
1. Verbal Irony:
   - Occurs when a speaker says one thing but deliberately means the exact opposite (often used as sarcasm).
   - Example: Stepping outside into a torrential downpour and remarking, "What lovely, sunny weather we are having today!"
2. Situational Irony:
   - Occurs when there is an incongruity between what is logically expected to happen and what actually occurs.
   - Example: A fire station catching fire and burning down, or a marriage counselor filing for divorce.
3. Dramatic Irony:
   - Occurs when the audience or reader possesses vital knowledge that characters within the narrative do not yet know.
   - Example: In Shakespeare's Romeo and Juliet, Romeo drinks poison believing Juliet is dead, while the audience knows she is merely in a drug-induced sleep.""",

    12: """Definition of Connectives:
Connectives (also referred to as transitional words, linking expressions, or conjunctions) are words or phrases that join clauses, sentences, or paragraphs together to establish clear, logical relationships between ideas.
Categories and Functions:
1. Addition: Connectives that add information (e.g., furthermore, moreover, in addition, also, and).
2. Contrast: Connectives that introduce opposing ideas (e.g., however, although, nevertheless, on the other hand, but).
3. Cause and Effect / Result: Connectives that demonstrate causality (e.g., because, since, therefore, consequently, as a result).
4. Sequence / Time Order: Connectives that indicate chronological progression (e.g., first, next, meanwhile, subsequently, finally).
5. Exemplification / Illustration: Connectives that introduce examples (e.g., for example, for instance, namely).""",

    13: """Definition of Direct Statement:
A direct statement (or direct quotation/speech) reproduces the exact, verbatim words spoken or written by the original speaker, enclosed within quotation marks ("...").
Characteristics:
- Preserves the exact wording, original verb tenses, and personal pronouns of the speaker.
- Preceded or followed by a reporting clause set off by a comma.
- Example: The professor stated, "The final examination will commence promptly at nine o'clock tomorrow morning.\"""",

    14: """Definition of Gerund:
A gerund is a verb ending in '-ing' that functions grammatically as a noun.
Syntactic Functions:
1. Subject: "Reading enhances cognitive abilities."
2. Direct Object: "They postponed holding the annual conference."
3. Object of Preposition: "He apologized for arriving late.\"""",

    15: """Definition of Superlative Degree of Adjectives (Super relative):
The superlative degree is the form of an adjective or adverb that denotes the highest or lowest extreme degree of a quality when comparing three or more persons, places, or things.
Formation Rules:
1. One-syllable adjectives: Formed by adding '-est' (e.g., fast -> fastest, tall -> tallest, cold -> coldest).
2. Two-syllable adjectives ending in '-y': Change 'y' to 'i' and add '-est' (e.g., happy -> happiest, easy -> easiest).
3. Multi-syllable adjectives: Preceded by 'most' or 'least' (e.g., intelligent -> most intelligent, expensive -> most expensive).
4. Irregular adjectives: good -> best, bad -> worst, far -> farthest/furthest.
Example: "Mount Everest is the highest mountain peak on Earth.\"""",

    16: """Difference Between Skimming and Scanning:
1. Skimming (Reading for Gist):
   - Objective: Rapidly previewing or reading through a passage to grasp the central idea, general overview, or main outline without reading every word.
   - Method: Reading headings, subheadings, introductory paragraphs, topic sentences (first sentences of body paragraphs), and concluding summaries.
   - Typical Use: Skimming a newspaper article, previewing a textbook chapter before study, or deciding whether a research paper is relevant.
2. Scanning (Reading for Specific Detail):
   - Objective: Moving one's eyes rapidly across a text specifically to locate a targeted piece of information, number, name, date, or keyword.
   - Method: Formulating a mental picture of the target word/number and searching only for that specific clue while deliberately ignoring all unrelated text.
   - Typical Use: Looking up a term in a dictionary, locating a telephone number in a directory, checking an airline flight schedule, or finding a date in a historical text.""",

    17: """Difference Between Skimming and Scanning:
1. Skimming (Reading for Gist):
   - Objective: Rapidly previewing or reading through a passage to grasp the central idea, general overview, or main outline without reading every word.
   - Method: Reading headings, subheadings, introductory paragraphs, topic sentences (first sentences of body paragraphs), and concluding summaries.
   - Typical Use: Skimming a newspaper article, previewing a textbook chapter before study, or deciding whether a research paper is relevant.
2. Scanning (Reading for Specific Detail):
   - Objective: Moving one's eyes rapidly across a text specifically to locate a targeted piece of information, number, name, date, or keyword.
   - Method: Formulating a mental picture of the target word/number and searching only for that specific clue while deliberately ignoring all unrelated text.
   - Typical Use: Looking up a term in a dictionary, locating a telephone number in a directory, checking an airline flight schedule, or finding a date in a historical text.""",

    18: """Difference Between Pie Charts and Bar Charts:
1. Pie Chart:
   - Structure: A circular graphic divided into proportional slices or sectors.
   - Purpose: Illustrates proportions and percentages of a single whole entity; the sum of all sectors must equal 100% (or 360 degrees).
   - Best Used For: Showing how a whole budget, market share, or population is distributed among categories.
2. Bar Chart:
   - Structure: Composed of discrete rectangular horizontal or vertical bars where the length or height of each bar corresponds to its quantitative value along an axis.
   - Purpose: Compares discrete, independent categories against one another or tracks changes across distinct time periods.
   - Best Used For: Comparing sales figures across multiple regional offices or tracking quarterly revenue over several years.""",

    19: """1. Participle Answers:
   1. requested ("She has requested two tickets to the show.")
   2. thought ("I have thought about it for a long time.")
   3. put ("The money was put in the bank.")
   4. hurt ("Have you been hurt?")
   5. redone ("The paper will have to be redone.")
   6. read ("Mike has already read that article.")
2. Paragraph Main Idea:
   Main Idea: Adult children caring for aging parents encounter substantial emotional and logistical difficulties, but accessible community and family support networks offer viable solutions to relieve these burdens.""",

    20: """Correct Past Participles:
1. read ("The story was read by the librarian.")
2. added ("These numbers have been added wrong.")
3. drunk ("My brother has never drunk wine.")
4. felt ("I have never felt so sick before.\"""",

    21: """How Many Types of Irony are There? Describe:
There are three recognized major types of irony:
1. Verbal Irony: Occurs when a speaker intentionally states something that contradicts their actual meaning, typically employed for satirical, humorous, or sarcastic effect. (Example: "Oh, fantastic! Another flat tire on Monday morning!").
2. Situational Irony: Arises when a distinct incongruity occurs between what circumstances lead one reasonably to expect and the actual outcome that unfolds. (Example: An expert swimming instructor tragically drowning in a shallow pool).
3. Dramatic Irony: Established when the audience or reader possesses critical insights into characters' fates or circumstances of which the characters themselves remain completely unaware. (Example: In Oedipus Rex, Oedipus curses the murderer of the king, unaware that he himself is the culprit).""",

    22: """How to Make an Effective Paragraph:
1. Unity: Focus strictly on a single central idea. Every supporting sentence must directly elaborate on this central theme without straying into unrelated ideas.
2. Strong Topic Sentence: Formulate a clear topic sentence (usually placed at the opening of the paragraph) that states the main idea and controlling focus.
3. Adequate Development & Concrete Support: Provide substantial supporting evidence, including empirical facts, statistical data, logical reasoning, and vivid examples.
4. Coherence and Smooth Transitions: Connect thoughts logically using transitional words (e.g., furthermore, however, consequently, for instance), pronoun references, and parallel sentence structures.
5. Concluding Clincher: Conclude with a strong sentence that summarizes the paragraph's core point and provides a natural transition to the next idea.""",

    23: """Classification and Linguistic Justification:
1. Sentence 1: Blend (B) - The historical fact that Victor Emmanuel II was the king of a unified Italy is verifiable, but characterizing his temperament as "an eccentric madman" is a subjective opinion/value judgment.
2. Sentence 2: Fact (F) - The invention of the modern self-contained underwater breathing apparatus (SCUBA) suit in 1943 by Jacques Cousteau is an objective, historically verifiable technological achievement.
3. Sentence 3: Opinion (O) - Describing an author's writing style as "deeply moving, lyrical, and evocative" is a personal aesthetic evaluation that cannot be proven true or false.""",

    24: """Explanation and Matching of Cause and Effect Relationships:
1. Concept:
   - Cause: The catalyst, underlying reason, or event that triggers an outcome (answers: "Why did this happen?").
   - Effect: The resulting outcome, consequence, or condition that occurs as a direct product of the cause (answers: "What happened?").
2. Identifying Cause and Effect:
   - Transitional markers indicating cause: because, due to, since, as, owing to.
   - Transitional markers indicating effect: therefore, consequently, as a result, thus, so.
3. Concrete Examples:
   - Example 1: "Heavy torrential rainfall overwhelmed municipal drainage systems; consequently, several central roads experienced severe flash flooding."
     * Cause: Heavy rainfall overwhelming drainage.
     * Effect: Flash flooding on central roads.
   - Example 2: "The student revised lecture notes consistently each evening, which resulted in achieving top academic honors."
     * Cause: Consistent evening revision.
     * Effect: Top academic honors.""",

    25: """Inference and Textual Evidence:
- Inference: Paul is at an ocean, sea, or coastal beach.
- Contextual Evidence: The presence of loose "sand" coupled with ocean "waves" that one can submerge into ("submitted himself to the waves") directly implies a coastal seashore or beach setting.""",

    26: """Implied Main Idea of Paragraph:
"Although dates on a calendar possess no inherent power or biological threat, many people throughout various cultures suffer from deep-seated anxieties and irrational superstitious dread regarding recurring days such as Friday the 13th.\"""",

    27: """Main Idea of Passage on Infant Crying:
"While infant crying frequently acts as a source of frustration and fatigue for parents, it serves indispensable biological and evolutionary purposes by exercising infant respiratory organs and serving as the newborn's vital distress signal for physical survival.\"""",

    28: """Comprehension Answers on Vehicle Regulations:
1. Accountability: Under Dalton State College parking policies, the registered permit holder of a motor vehicle is held strictly accountable for any parking or traffic violations committed with that vehicle on campus premises, regardless of who was operating the automobile.
2. Parking Authorization: Vehicles parked on campus must display a valid, official college parking permit hung from the rearview mirror or adhered to the windshield in designated parking zones.""",

    29: """Main Idea of Myths:
"Myths are profound, imaginative cultural narratives through which human societies explain natural phenomena, articulate sacred origins, and transmit foundational spiritual and ethical values across generations.\"""",

    30: """Fact vs Opinion Classification:
1. "Pizza tastes better than fish." -> Opinion (a subjective culinary preference).
2. "Many people work Mondays through Fridays at their jobs." -> Fact (an observable, empirically verifiable socio-economic schedule).
3. "Before electricity, many people burnt candles to give them light." -> Fact (a documented historical truth).
4. "Jumping rope is a form of exercise." -> Fact (an objective physical and physiological definition).""",

    31: """Main Idea of Dogs and Children:
"Owning and caring for domestic dogs yields significant developmental advantages for children, instilling lifelong values of personal responsibility, hygiene, empathy, and routine daily discipline.\"""",

    32: """Making Inferences True/False:
1. True - Context clues frequently utilize antonyms or contrasting transitional words (e.g., unlike, whereas, but) to illuminate unfamiliar vocabulary.
2. True - A well-constructed paragraph can communicate a clear, cohesive main idea implicitly through supporting details without an explicit topic sentence.
3. False - Paragraphs lacking an explicit topic sentence still regularly contain abundant, structured supporting details that collectively imply the central theme.""",

    33: """Sentence Rewrite:
Original Sentence: "Her apartment is very hot. It has no air conditioning."
Effective Rewritten Sentence:
"Her apartment is very hot because it has no air conditioning."
(Subordinating conjunction 'because' establishes the direct causal relationship between the lack of air conditioning and the oppressive heat).""",

    34: """Definition and Examples of Situational Irony:
1. Definition: Situational irony occurs when there is a striking discrepancy between what is logically or reasonably expected to occur and what actually happens in reality.
2. Examples:
   - Example 1: A local fire station catching fire and burning completely to the ground while firefighters are out on a call.
   - Example 2: A professional marriage counselor filing for divorce after twenty years of giving relationship advice.""",

    35: """Identified Synonym Pairs:
1. well informed / knowledgeable
2. triumphant / victorious
3. recall / remember
4. tardy / late
5. confess / admit""",

    36: """Classification of Major Logical Fallacies:
1. Hasty Generalization: Drawing a broad, sweeping conclusion based on an inadequate or unrepresentative sample size.
2. False Dilemma (Either/Or Fallacy): Unfairly restricting an argument to only two polar options when intermediate alternatives exist.
3. Ad Hominem: Attacking the personal character or motives of the arguer rather than critically addressing the substance of their argument.
4. Bandwagon Fallacy (Ad Populum): Claiming an assertion must be true simply because a widespread majority of people accept or practice it.
5. Slippery Slope: Arguing without logical justification that an initial modest step will trigger an inevitable, catastrophic chain of events.
6. Red Herring: Introducing an extraneous, emotionally charged topic into a debate to divert attention away from the core issue.
7. Post Hoc Ergo Propter Hoc (False Cause): Incorrectly concluding that because event B occurred chronologically after event A, event A must have caused event B.
8. Straw Man: Grossly misrepresenting or exaggerating an opponent's position to make it easier to attack and refute.""",

    37: """Line in Graph Line:
In a line graph, the line connecting the data points is called the trend line or data plot line. The horizontal axis is designated as the X-axis (independent variable), and the vertical axis is designated as the Y-axis (dependent variable).""",

    38: """Definition and Educational Value of the Cloze Procedure:
1. Definition: The Cloze procedure is a reading comprehension diagnostic and instructional assessment in which words are systematically deleted from a continuous prose passage at regular intervals (typically every 5th to 7th word) and replaced with standardized blank lines.
2. Purpose and Benefits:
   - Diagnostic Assessment: Accurately evaluates a student's reading comprehension, syntactic awareness, and vocabulary mastery.
   - Context Clue Utilization: Evaluates how effectively a reader relies on semantic context clues and grammatical syntax to infer missing linguistic elements.
   - Readability Measurement: Determines whether assigned textbooks and reading passages match the independent, instructional, or frustration reading levels of students.""",

    39: """Definition and Educational Value of the Cloze Procedure:
1. Definition: The Cloze procedure is a reading comprehension diagnostic and instructional assessment in which words are systematically deleted from a continuous prose passage at regular intervals (typically every 5th to 7th word) and replaced with standardized blank lines.
2. Purpose and Benefits:
   - Diagnostic Assessment: Accurately evaluates a student's reading comprehension, syntactic awareness, and vocabulary mastery.
   - Context Clue Utilization: Evaluates how effectively a reader relies on semantic context clues and grammatical syntax to infer missing linguistic elements.
   - Readability Measurement: Determines whether assigned textbooks and reading passages match the independent, instructional, or frustration reading levels of students.""",

    40: """Definition and Characteristics of Indirect Statements:
1. Definition: An indirect statement (or reported speech) conveys the meaning and substance of what a speaker stated without quoting their exact words verbatim.
2. Key Characteristics:
   - Does not use quotation marks ("...").
   - Introduced by a reporting verb (e.g., said, stated, explained, declared) and usually followed by the conjunction 'that'.
   - Incurs backshifting of verb tenses (e.g., present tense shifts to past tense) and adjustments to personal pronouns and time adverbials.
3. Example:
   - Direct Statement: She said, "I have completed the report."
   - Indirect Statement: She said that she had completed the report.""",

    41: """Definition and Impact of Vocalization on Reading Comprehension:
1. Definition: Vocalization is the conscious or subconscious physical habit of pronouncing words aloud, whispering, or moving one's lips, tongue, and vocal cords while reading silently. Subvocalization refers to the internal "voice" sounding out words in the mind.
2. Effect on Reading Speed:
   - Normal human vocalization caps reading speed at approximately 150 to 250 words per minute (the maximum rate of clear physical speech).
   - In contrast, the human visual system and cognitive cortex can process text at speeds of 400 to 800+ words per minute when subvocalization is minimized. Therefore, excessive vocalization severely impedes reading efficiency and overall comprehension.""",

    42: """Difference Between Skimming and Scanning:
1. Skimming: Reading rapidly over a passage to understand the central theme, general idea, or gist. Uses headings, topic sentences, and concluding paragraphs.
2. Scanning: Rapid visual searching through text to locate a specific date, statistic, name, or keyword while ignoring unrelated material.""",

    43: """Answer:
The line going vertically from top to bottom on the leftmost edge of a line graph is designated as the Vertical Axis or Y-Axis (also referred to mathematically as the ordinate). It displays the numerical scale and quantitative measurements of the dependent variable.""",

    44: """Definition and Purpose of Coordinating Conjunctions:
Coordinating conjunctions (remembered by the acronym FANBOYS: For, And, Nor, But, Or, Yet, So) serve to connect words, phrases, or independent clauses of equal grammatical rank and syntactic importance.
Functions:
1. Joins parallel grammatical units (e.g., two nouns, two verbs, or two independent clauses).
2. Establishes specific logical relationships between thoughts (e.g., addition with 'and', contrast with 'but', choice with 'or', result with 'so').
Example: "The library was closing, so we packed our laptops and departed.\"""",

    45: """Purpose and Functions of Tables in Written Texts:
1. Systematic Categorization: Organizes dense numerical figures, categories, and descriptive data into an orderly matrix of rows and columns.
2. Space Efficiency: Condenses vast amounts of detailed statistical information into a compact visual format, eliminating bulky paragraphs of text.
3. Cross-Referencing: Facilitates swift comparisons, rapid retrieval of specific data points, and straightforward verification of facts.""",

    46: """What is 'Cloze'?
A 'Cloze' test is an empirical reading comprehension assessment developed by Wilson Taylor (1953) where systematically deleted words (e.g., every 5th or 7th token) in a written passage must be restored by the reader using syntactic knowledge and semantic context clues.""",

    47: """Importance of Distinguishing Fact from Opinion:
1. Critical Literacy: Protects readers from being manipulated by biased rhetoric, political propaganda, deceptive advertising, and unfounded assertions.
2. Objective Evaluation: Empowers students to evaluate whether an author's thesis is grounded in empirical, verifiable evidence or merely subjective personal beliefs.
3. Rigorous Scholarly Writing: Ensures academic research, conclusions, and debates are supported by verified data rather than unsubstantiated feelings.""",

    48: """Why Writers Use Bar Charts:
1. Visual Comparison: Uses proportional horizontal or vertical columns to make comparisons between discrete categories instantly recognizable.
2. Highlights Extremes & Trends: Clearly displays highest quantities, lowest quantities, growth rates, and category differences at a glance.
3. Time Economy: Enables readers to absorb complex comparisons in seconds without wading through lengthy statistical descriptions.""",

    49: """Advantages and Purpose of Bar Charts:
1. Visual Comparison: Uses proportional horizontal or vertical columns to make comparisons between discrete categories instantly recognizable.
2. Highlights Extremes & Trends: Clearly displays highest quantities, lowest quantities, growth rates, and category differences at a glance.
3. Time Economy: Enables readers to absorb complex comparisons in seconds without wading through lengthy statistical descriptions.""",

    50: """Antonym Pairs:
1. Illegal -> Legal (or lawful, permissible)
2. Undiscovered -> Discovered (or known, found)
3. Inaccessible -> Accessible (or approachable, reachable)
4. Temporary -> Permanent (or enduring, lasting)""",

    51: """Passive Voice Transformations:
1. Active: "He writes text messages." -> Passive: "Text messages are written by him."
2. Active: "She does the housework." -> Passive: "The housework is done by her."
3. Active: "The policemen help the children." -> Passive: "The children are helped by the policemen."
4. Active: "He reads comics." -> Passive: "Comics are read by him.\"""",

    52: """Synonym Groups:
1. TRY: Attempt, strive, endeavor, undertake.
2. SHOW: Display, demonstrate, exhibit, reveal, illustrate.
3. ROUTE: Path, course, way, road, trajectory.
4. ANSWER: Respond, reply, retort, address.""",

    53: """Completed Sentences with Correct Negative Prefixes:
1. unpractical (or impractical) ("I love high heels but they're rather impractical / unpractical.")
2. illogical ("It is an illogical statement, because if one part is true, then the other must be false.")
3. impolite ("It is impolite to point at people.")
4. impossible ("It was impossible to sleep because of the noise.")
5. irrational ("It’s totally irrational, but I'm frightened of mice.\")""",

    54: """Completed Sentences with Correct Negative Prefixes:
1. dissimilar ("The new house is not dissimilar to our old one except that it's a bit bigger.")
2. non-political (or apolitical / impolitical) ("The organization insists that it is non-political / apolitical and does not identify with any one particular party.")
3. unclear ("The ownership of the painting remains unclear.")
4. imperfect ("We’re living in an imperfect world.")
5. immaterial ("Whether the book is well or badly written is immaterial to me - it has an important message.\")""",

    55: """Classification of Major Logical Fallacies:
1. Hasty Generalization: Drawing a broad, sweeping conclusion based on an inadequate or unrepresentative sample size.
2. False Dilemma (Either/Or Fallacy): Unfairly restricting an argument to only two polar options when intermediate alternatives exist.
3. Ad Hominem: Attacking the personal character or motives of the arguer rather than critically addressing the substance of their argument.
4. Bandwagon Fallacy (Ad Populum): Claiming an assertion must be true simply because a widespread majority of people accept or practice it.
5. Slippery Slope: Arguing without logical justification that an initial modest step will trigger an inevitable, catastrophic chain of events.
6. Red Herring: Introducing an extraneous, emotionally charged topic into a debate to divert attention away from the core issue.
7. Post Hoc Ergo Propter Hoc (False Cause): Incorrectly concluding that because event B occurred chronologically after event A, event A must have caused event B.
8. Straw Man: Grossly misrepresenting or exaggerating an opponent's position to make it easier to attack and refute.""",

    56: """Three Core Factors of Reading Skills:
1. Flexibility of Reading Rate according to Purpose: Skilled readers consciously adjust their reading speed depending on text difficulty and comprehension goals (skimming for gist, scanning for specific facts, or intensive reading for critical analysis).
2. Comprehension of Main Ideas and Topic Structure: The ability to identify topic sentences, differentiate primary themes from secondary supporting details, and synthesize implicit central ideas.
3. Contextual Vocabulary & Inferential Reasoning: The capacity to deduce the meanings of unfamiliar words through contextual clues, prefixes, and suffixes, and to read between the lines to draw valid logical inferences.""",

    57: """Three Core Factors of Reading Skills:
1. Flexibility of Reading Rate according to Purpose: Skilled readers consciously adjust their reading speed depending on text difficulty and comprehension goals (skimming for gist, scanning for specific facts, or intensive reading for critical analysis).
2. Comprehension of Main Ideas and Topic Structure: The ability to identify topic sentences, differentiate primary themes from secondary supporting details, and synthesize implicit central ideas.
3. Contextual Vocabulary & Inferential Reasoning: The capacity to deduce the meanings of unfamiliar words through contextual clues, prefixes, and suffixes, and to read between the lines to draw valid logical inferences."""
}

# Clean questions in subjective bank
SUBJ_QUESTION_CLEAN = {
    34: "Explain Situational Irony with examples. (2 Marks)",
    52: "Write synonyms for TRY, SHOW, ROUTE, and ANSWER."
}

verified_subj = []
for idx, item in enumerate(eng_subj):
    qid = item.get("id", idx + 1)
    # Clean question text
    q_text = clean_watermarks_from_question(item.get("question", ""))
    if qid in SUBJ_QUESTION_CLEAN:
        q_text = SUBJ_QUESTION_CLEAN[qid]
    item["question"] = q_text
    
    # Set model answer
    if qid in SUBJECTIVE_MODEL_ANSWERS:
        ans_text = SUBJECTIVE_MODEL_ANSWERS[qid].strip()
        item["answer"] = ans_text
        item["model_answer"] = ans_text
    verified_subj.append(item)

print(f"Subjective Questions Audited: {len(verified_subj)} | Model Answers Set: {len(SUBJECTIVE_MODEL_ANSWERS)}")

# -------------------------------------------------------------
# 5. Save verified JSON banks
# -------------------------------------------------------------
with open('/home/haider/Desktop/Chores/eng101_quiz_bank.json', 'w') as f:
    json.dump(verified_mcqs, f, indent=2, ensure_ascii=False)

subj_master["ENG101"] = verified_subj
with open('/home/haider/Desktop/Chores/subjective_bank.json', 'w') as f:
    json.dump(subj_master, f, indent=2, ensure_ascii=False)

print("Saved verified eng101_quiz_bank.json and subjective_bank.json successfully!")

