#!/usr/bin/env python3
"""
Senior Subject Matter Expert Auditor for ENG101 (English Comprehension)
Master verification script that audits and fixes:
1. eng101_quiz_bank.json (671 MCQs)
2. subjective_bank.json['ENG101'] (57 Subjective questions)
"""

import json, re

print("Starting ENG101 Comprehensive Master Audit...")

# -------------------------------------------------------------
# 1. Truncated word dictionary & text cleaning helpers
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
    # Check exact match
    low = clean.lower()
    if low in TRUNCATED_WORD_REPLACEMENTS:
        rep = TRUNCATED_WORD_REPLACEMENTS[low]
        if clean[0].isupper():
            return rep.capitalize()
        return rep
    return clean

def fix_all_truncated_words(text):
    if not text: return ""
    # Replace known phrases
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
    
    # Split tokens to fix individual words if needed
    words = t.split()
    fixed_words = [restore_word(w) for w in words]
    return " ".join(fixed_words)

def clean_watermarks_from_question(q):
    if not q: return ""
    res = q.strip()
    # Remove known scraper headers & watermarks
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

    # Fix truncated question starts
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
    # Strip leading markers like a. b. c. d. (a) (b) ► • ✔
    o = re.sub(r'^\(?[a-dA-D][\)\.\:\s]+', '', o).strip()
    o = re.sub(r'^(?:[►•\*\–\-✓✔○●✔️\uf0b7\d\.\:\s]+)', '', o).strip()
    o = re.sub(r'\s*\(correct\).*|\s*\(✔\).*|\s*right answer.*', '', o, flags=re.I).strip()
    o = re.sub(r'\(\)$', '', o).strip()
    o = fix_all_truncated_words(o)
    return o.strip()

print("Helper functions ready.")
