#!/usr/bin/env python3
"""
Comprehensive STA301 (Statistics and Probability) Question Bank Builder
Extracts pristine objective questions (MCQs & True/False) and subjective questions (2, 3, 5 marks)
from all STA301 course materials.
"""

import os
import re
import glob
import json
import subprocess
from collections import Counter

WORKSPACE = "/home/haider/Desktop/Chores"
STA301_DIR = os.path.join(WORKSPACE, "STA301 - Statistics and Probability")
MCQ_DIR = os.path.join(STA301_DIR, "MCQs & Quizzes")
PAST_DIR = os.path.join(STA301_DIR, "Past Papers & Solved Papers")
SUBJ_DIR = os.path.join(STA301_DIR, "Subjective & Notes")

def clean_text(t):
    if not t:
        return ""
    t = re.sub(r'[\r\f]', '', t)
    t = re.sub(r'[ \t]+', ' ', t)
    return t.strip()

def normalize_q(q):
    q = q.lower()
    q = re.sub(r'[^a-z0-9]', '', q)
    return q[:90]

def classify_topic(text):
    t = text.lower()
    if any(k in t for k in ['regression', 'correlation', 'scatter', 'least squares', 'dependent variable', 'independent variable', 'coefficient of determination', 'r =', 'r2', 'slope', 'intercept', 'fitted line']):
        return "Simple Linear Regression & Correlation"
    if any(k in t for k in ['probability', 'permutation', 'combination', 'dice', 'coin', 'card', 'mutually exclusive', 'independent event', 'bayes', 'sample space', 'event', 'urn', 'factorial', 'npr', 'ncr', 'drawing', 'exhaustive', 'joint prob', 'p(a']):
        return "Probability & Counting Rules"
    if any(k in t for k in ['random variable', 'binomial', 'poisson', 'normal distribution', 'hypergeometric', 'expected value', 'e(x)', 'density function', 'p(x', 'standard normal', 'variance of annual accidents']):
        return "Random Variables & Distributions"
    if any(k in t for k in ['moment', 'skewness', 'kurtosis', 'leptokurtic', 'platykurtic', 'mesokurtic', 'bowley', 'sheppard', 'peakedness', 'symmetry', 'asymmetry', 'first moment']):
        return "Moments, Skewness & Kurtosis"
    if any(k in t for k in ['variance', 'standard deviation', 'dispersion', 'range', 'coefficient of variation', 'c.v', 'chebychev', 'interquartile', 'quartile deviation', 'mean deviation', 's.d']):
        return "Measures of Dispersion"
    if any(k in t for k in ['mean', 'median', 'mode', 'harmonic', 'geometric', 'quartile', 'decile', 'percentile', 'central tendency', 'average', 'mid-point', 'five number summ', 'ogive', 'middle value']):
        return "Measures of Central Tendency"
    return "Data Representation & Basics"

def extract_pdf_layout(path):
    try:
        res = subprocess.run(['pdftotext', '-layout', path, '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout
    except Exception as e:
        print(f"Error reading layout {path}: {e}")
        return ""

def extract_pdf_plain(path):
    try:
        res = subprocess.run(['pdftotext', path, '-'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout
    except Exception as e:
        print(f"Error reading plain {path}: {e}")
        return ""

def extract_doc(path):
    try:
        res = subprocess.run(['antiword', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout
    except Exception as e:
        print(f"Error reading doc {path}: {e}")
        return ""

# Non-STA301 question filter (e.g. from STA630 Research Methods or CS/Management questions accidentally in bundles)
NON_STA301_KEYWORDS = [
    'literature review', 'hypothesis refers to', 'research methods', 'sta630',
    'primary key', 'foreign key', 'database', 'c++', 'html', 'compiler',
    'mass communication', 'cognitive development', 'railroad companies'
]

def is_valid_sta301(q_text):
    ql = q_text.lower()
    for kw in NON_STA301_KEYWORDS:
        if kw in ql:
            return False
    return True

all_objective_questions = []
seen_q_signatures = set()

def add_objective(q_text, options, correct_idx, has_verified, source, explanation=""):
    if not is_valid_sta301(q_text) or len(options) < 2:
        return False
    if len(q_text) > 350 or len(q_text) < 10:
        return False
    if re.search(r'Question\s*(?:#|No:?\s*\d+)', q_text, re.IGNORECASE):
        return False
    # Ensure options are clean and unique
    cleaned_opts = []
    seen_opts = set()
    mapped_correct = -1
    for idx, opt in enumerate(options):
        o = clean_text(opt)
        if len(o) > 180 or re.search(r'Question\s*(?:#|No:?\s*\d+)', o, re.IGNORECASE):
            continue
        if o and o not in seen_opts:
            seen_opts.add(o)
            cleaned_opts.append(o)
            if idx == correct_idx:
                mapped_correct = len(cleaned_opts) - 1
    
    if len(cleaned_opts) < 2 or len(cleaned_opts) > 6:
        return False
    
    sig = normalize_q(q_text)
    if sig in seen_q_signatures:
        return False
    seen_q_signatures.add(sig)
    
    topic = classify_topic(q_text)
    is_tf = len(cleaned_opts) == 2 and any(o.lower() in ['true', 'false'] for o in cleaned_opts)
    
    if mapped_correct == -1:
        mapped_correct = 0
        has_verified = False
        
    all_objective_questions.append({
        "id": f"STA301-OBJ-{len(all_objective_questions)+1:04d}",
        "subject": "STA301",
        "topic": topic,
        "type": "true_false" if is_tf else "mcq",
        "question": q_text,
        "options": cleaned_opts,
        "correct_answer": mapped_correct,
        "has_verified_answer": has_verified,
        "explanation": explanation or "Standard examination question from Virtual University STA301 syllabus.",
        "source": source
    })
    return True

# -------------------------------------------------------------
# 1. PARSE MOAAZ SOLVED MCQs
# -------------------------------------------------------------
def parse_moaaz_files():
    moaaz_files = [
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs with References by Moaaz.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs with References Set 2 by Moaaz.pdf")
    ]
    extracted = 0
    for mf in moaaz_files:
        if not os.path.exists(mf):
            continue
        text = extract_pdf_layout(mf)
        blocks = re.split(r'\n(?=Question No:\s*\d+)', text, flags=re.IGNORECASE)
        for b in blocks:
            if not b.strip() or 'Please choose one' not in b:
                continue
            lines = [l.rstrip() for l in b.split('\n') if l.strip()]
            q_lines = []
            opt_lines = []
            parsing_opts = False
            for line in lines[1:]:
                sline = line.strip()
                if sline.startswith('►') or sline.startswith('*►'):
                    parsing_opts = True
                    opt_lines.append(line)
                elif parsing_opts:
                    if opt_lines and not sline.startswith(('Question', 'MIDTERM', 'STA301', 'Moaaz', 'http', 'Page')):
                        opt_lines[-1] += " " + sline
                else:
                    if not any(k in sline for k in ['MIDTERM', 'STA301', 'Page', 'http', 'Moaaz']):
                        q_lines.append(sline)
            
            q_text = clean_text(" ".join(q_lines))
            if not q_text or len(q_text) < 10:
                continue
            
            options = []
            correct_idx = -1
            for opt_raw in opt_lines:
                is_correct = bool(re.search(r'\(Page|\( Page|\(Lec|\( Lec|\*►', opt_raw, re.IGNORECASE))
                clean_opt = re.sub(r'^\*?►\s*', '', opt_raw.strip())
                clean_opt = re.sub(r'\s*\((?:Page|Lec)[^\)]*\)', '', clean_opt, flags=re.IGNORECASE).strip()
                clean_opt = re.sub(r'\s*click here for detail.*$', '', clean_opt, flags=re.IGNORECASE).strip()
                if clean_opt:
                    options.append(clean_opt)
                    if is_correct and correct_idx == -1:
                        correct_idx = len(options) - 1
            
            if add_objective(q_text, options, correct_idx, correct_idx != -1, "Moaaz Solved MCQs", "Extracted from Moaaz Solved Midterm Papers with handout references."):
                extracted += 1
    print(f"Moaaz parsed: {extracted} questions")

# -------------------------------------------------------------
# 2. PARSE MISS MEHWISH (2024 Midterm MCQs)
# -------------------------------------------------------------
def parse_mehwish():
    path = os.path.join(MCQ_DIR, "STA301 Midterm MCQs 2024 by Miss Mehwish.pdf")
    if not os.path.exists(path):
        return
    text = extract_pdf_plain(path)
    raw_blocks = re.split(r'\n\s*(\d+)[\.\)]\s+', text)
    extracted = 0
    for i in range(1, len(raw_blocks), 2):
        b = raw_blocks[i+1]
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        q_lines = []
        opt_lines = []
        parsing_opts = False
        for l in lines:
            if re.match(r'^[•\-\*]?\s*[A-Da-d][\)\.]', l):
                parsing_opts = True
                opt_lines.append(l)
            elif parsing_opts:
                if opt_lines and not re.match(r'^(?:Note:|For More|Miss)', l):
                    opt_lines[-1] += " " + l
            else:
                if not re.match(r'^(?:Note:|Live quiz|Exam)', l):
                    q_lines.append(l)
        
        q_text = clean_text(" ".join(q_lines))
        if not q_text or len(q_text) < 10:
            continue
        
        options = []
        correct_idx = -1
        for o_str in opt_lines:
            is_correct = bool('✔' in o_str or '✅' in o_str)
            clean_opt = re.sub(r'^[•\-\*]?\s*[A-Da-d][\)\.]\s*', '', o_str)
            clean_opt = clean_opt.replace('✔', '').replace('✅', '').strip()
            if clean_opt:
                options.append(clean_opt)
                if is_correct and correct_idx == -1:
                    correct_idx = len(options) - 1
        
        if add_objective(q_text, options, correct_idx, correct_idx != -1, "Miss Mehwish 2024", "Extracted from 2024 Midterm Examination Quizzes by Miss Mehwish."):
            extracted += 1
    print(f"Miss Mehwish parsed: {extracted} questions")

# -------------------------------------------------------------
# 3. PARSE JUNAID FILES (3 Sets + Past Papers)
# -------------------------------------------------------------
def parse_junaid_files():
    jfiles = [
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs by Junaid.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs Set 2 by Junaid.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs Set 3 by Junaid.pdf"),
        os.path.join(PAST_DIR, "STA301 Midterm Past Papers by Junaid.pdf")
    ]
    extracted = 0
    for jf in jfiles:
        if not os.path.exists(jf):
            continue
        text = extract_pdf_layout(jf)
        lines = [l.rstrip() for l in text.split('\n')]
        current_q = []
        current_opts = []
        
        for line in lines:
            sline = line.strip()
            m = re.match(r'^([a-d])\.\s+(.*)$', sline, re.IGNORECASE)
            if m:
                current_opts.append(sline)
            else:
                if current_opts:
                    q_text = clean_text(" ".join(current_q))
                    if q_text and len(q_text) >= 10:
                        options = []
                        correct_idx = -1
                        for opt_raw in current_opts:
                            is_corr = bool(re.search(r'\(Lecture|\(Handouts|\(Page|\bAnswer\b|page \d+', opt_raw, re.IGNORECASE))
                            clean_opt = re.sub(r'^[a-d]\.\s*', '', opt_raw, flags=re.IGNORECASE)
                            clean_opt = re.sub(r'\s*\((?:Lecture|Handouts|Page)[^\)]*\)', '', clean_opt, flags=re.IGNORECASE)
                            clean_opt = re.sub(r'\s*page \d+.*$', '', clean_opt, flags=re.IGNORECASE)
                            if clean_opt:
                                options.append(clean_opt)
                                if is_corr and correct_idx == -1:
                                    correct_idx = len(options) - 1
                        
                        if add_objective(q_text, options, correct_idx, correct_idx != -1, "Al-Junaid Solved Papers", "Extracted from Al-Junaid Midterm MCQs with lecture references."):
                            extracted += 1
                    current_q = []
                    current_opts = []
                
                if sline and not any(k in sline for k in ['AL-JUNAID', '0304-1659294', 'pg.', 'Solution:', 'MIDTERM']):
                    current_q.append(sline)
            
    print(f"Junaid parsed: {extracted} questions")

# -------------------------------------------------------------
# 4. PARSE ARSLAN & UZAIR FILES
# -------------------------------------------------------------
def parse_arslan_uzair():
    files = [
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs by Arslan.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs with References by Arslan.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm Solved MCQs by Uzair.pdf")
    ]
    extracted = 0
    for f in files:
        if not os.path.exists(f):
            continue
        text = extract_pdf_layout(f)
        blocks = re.split(r'\n\s*(\d+)[\.\)]\s+', text)
        for i in range(1, len(blocks), 2):
            b = blocks[i+1]
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            q_lines = []
            opt_lines = []
            parsing_opts = False
            for l in lines:
                if re.match(r'^[o•\-\*]\s+', l):
                    parsing_opts = True
                    opt_lines.append(l)
                elif parsing_opts:
                    if opt_lines and not re.match(r'^(?:PG|Lec|The total|MidTerm)', l):
                        opt_lines[-1] += " " + l
                else:
                    if not re.match(r'^(?:MidTerm|STA301|BY Arslan|V-U|Www)', l):
                        q_lines.append(l)
            
            q_text = clean_text(" ".join(q_lines))
            if not q_text or len(q_text) < 10:
                continue
            
            options = []
            correct_idx = -1
            for o_str in opt_lines:
                is_correct = bool(re.search(r'PG\s*#|Lec\s*#', o_str, re.IGNORECASE))
                clean_opt = re.sub(r'^[o•\-\*]\s*', '', o_str)
                clean_opt = re.sub(r'\s*PG\s*#.*$', '', clean_opt, flags=re.IGNORECASE)
                if clean_opt:
                    options.append(clean_opt)
                    if is_correct and correct_idx == -1:
                        correct_idx = len(options) - 1
            
            if add_objective(q_text, options, correct_idx, correct_idx != -1, "Arslan & Uzair Solved Papers", "Extracted from Arslan/Uzair Solved Midterm Papers with handout page references."):
                extracted += 1
    print(f"Arslan/Uzair parsed: {extracted} questions")

# -------------------------------------------------------------
# 5. PARSE LUCKY PAST PAPERS (Both Question # and Question No:)
# -------------------------------------------------------------
def parse_lucky():
    path = os.path.join(PAST_DIR, "STA301 Midterm Past Papers by Lucky.pdf")
    if not os.path.exists(path):
        return
    text = extract_pdf_plain(path)
    
    # 5a. Split by Question #
    blocks = re.split(r'\n(?=Question\s*#\s*\d+)', text, flags=re.IGNORECASE)
    extracted = 0
    for b in blocks:
        if not b.strip() or 'Question #' not in b:
            continue
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        q_lines = []
        opt_lines = []
        parsing_opts = False
        for l in lines[1:]:
            if l.startswith('•'):
                parsing_opts = True
                opt_lines.append(l)
            elif parsing_opts:
                if opt_lines and not l.startswith(('Question', 'Correct Ans', 'Sta301')):
                    opt_lines[-1] += " " + l
                elif 'Correct Ans' in l and opt_lines:
                    opt_lines[-1] += " [CORRECT]"
            else:
                if not any(k in l for k in ['Sta301', 'Mid term', 'Objective Questions']):
                    q_lines.append(l)
        
        q_text = clean_text(" ".join(q_lines))
        if q_text and len(q_text) >= 10:
            options = []
            correct_idx = -1
            for o_str in opt_lines:
                is_corr = '[CORRECT]' in o_str
                clean_opt = o_str.replace('•', '').replace('[CORRECT]', '').strip()
                if clean_opt:
                    options.append(clean_opt)
                    if is_corr and correct_idx == -1:
                        correct_idx = len(options) - 1
            
            if add_objective(q_text, options, correct_idx, correct_idx != -1, "Lucky Past Papers", "Extracted from Lucky Midterm Past Papers collection."):
                extracted += 1

    # 5b. Split by Question No:
    blocks2 = re.split(r'\n(?=Question No:\s*\d+)', text, flags=re.IGNORECASE)
    for b in blocks2:
        if not b.strip() or 'Please choose one' not in b:
            continue
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        q_lines = []
        opt_lines = []
        parsing_opts = False
        for l in lines[1:]:
            if l.startswith('►') or l.startswith('*►'):
                parsing_opts = True
                opt_lines.append(l)
            elif parsing_opts:
                if opt_lines and not l.startswith(('Question', 'MIDTERM', 'STA301', 'Moaaz', 'http')):
                    opt_lines[-1] += " " + l
            else:
                if not any(k in l for k in ['MIDTERM', 'STA301', 'Page', 'http', 'Moaaz']):
                    q_lines.append(l)
        
        q_text = clean_text(" ".join(q_lines))
        if q_text and len(q_text) >= 10:
            options = []
            correct_idx = -1
            for opt_raw in opt_lines:
                is_correct = bool(re.search(r'\(Page|\( Page|\(Lec|\( Lec|\*►', opt_raw, re.IGNORECASE))
                clean_opt = re.sub(r'^\*?►\s*', '', opt_raw.strip())
                clean_opt = re.sub(r'\s*\((?:Page|Lec)[^\)]*\)', '', clean_opt, flags=re.IGNORECASE).strip()
                if clean_opt:
                    options.append(clean_opt)
                    if is_correct and correct_idx == -1:
                        correct_idx = len(options) - 1
            
            if add_objective(q_text, options, correct_idx, correct_idx != -1, "Lucky Past Papers", "Extracted from Lucky Midterm Past Papers collection."):
                extracted += 1

    print(f"Lucky parsed: {extracted} questions")

# -------------------------------------------------------------
# 6. PARSE VU TOPPER RM FILES (Sets 1, 2, 3, 4 with trailing Page markers)
# -------------------------------------------------------------
def parse_vu_topper():
    files = [
        os.path.join(MCQ_DIR, "STA301 Midterm MCQs by VU Topper RM.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm MCQs Set 2 by VU Topper RM.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm MCQs Set 3 by VU Topper RM.pdf"),
        os.path.join(MCQ_DIR, "STA301 Midterm MCQs Set 4 by VU Topper RM.pdf")
    ]
    extracted = 0
    for vf in files:
        if not os.path.exists(vf):
            continue
        text = extract_pdf_plain(vf)
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        
        current_q = []
        current_opts = []
        correct_idx = -1
        
        for line in lines:
            # Check for Page reference line referring to the previous option
            if re.match(r'^(?:Page|Lec|Handouts)\s*\d+', line, re.IGNORECASE) and current_opts:
                correct_idx = len(current_opts) - 1
                continue
                
            m = re.match(r'^([A-D])[\.\)]\s*(.*)$', line)
            if m:
                opt_str = line
                if re.search(r'\bPage\s*\d+|\bLec\s*\d+', opt_str, re.IGNORECASE):
                    correct_idx = len(current_opts)
                current_opts.append(opt_str)
            else:
                if current_opts:
                    q_text = clean_text(" ".join(current_q))
                    q_text = re.sub(r'^Question\s*No:\s*\d+\s*(?:\(Marks:\s*\d+\))?\s*(?:Vu-Topper RM)?', '', q_text, flags=re.IGNORECASE).strip()
                    if q_text and len(q_text) >= 10:
                        options = []
                        mapped_correct = -1
                        for idx, opt_raw in enumerate(current_opts):
                            clean_opt = re.sub(r'^[A-D][\.\)]\s*', '', opt_raw)
                            clean_opt = re.sub(r'\bPage\s*\d+.*$', '', clean_opt, flags=re.IGNORECASE)
                            clean_opt = clean_text(clean_opt)
                            if clean_opt:
                                options.append(clean_opt)
                                if idx == correct_idx:
                                    mapped_correct = len(options) - 1
                        
                        if add_objective(q_text, options, mapped_correct, mapped_correct != -1, "VU Topper RM", "Extracted from VU Topper RM Midterm MCQs."):
                            extracted += 1
                    current_q = []
                    current_opts = []
                    correct_idx = -1
                
                if line and not any(k in line for k in ['STA-301', 'Vu-Topper RM', '03224021365', '0322-4021365', 'Marks:1', 'What’s app']):
                    current_q.append(line)
            
    print(f"VU Topper parsed: {extracted} questions")

# -------------------------------------------------------------
# 7. PARSE PAST PAPERS 1 TO 6 & SESSION PAPERS
# -------------------------------------------------------------
def parse_past_paper_series():
    files = sorted(glob.glob(os.path.join(PAST_DIR, "STA301 Midterm Past Paper *.pdf")))
    extracted = 0
    for pf in files:
        text = extract_pdf_plain(pf)
        blocks = re.split(r'\n(?=Question\s*(?:No\.?|#)\s*:\s*\d+)', text, flags=re.IGNORECASE)
        for b in blocks:
            if not b.strip() or 'Please choose one' not in b:
                continue
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            q_lines = []
            opt_lines = []
            parsing_opts = False
            for l in lines[1:]:
                if l.startswith('►') or l.startswith('*►'):
                    parsing_opts = True
                    opt_lines.append(l)
                elif parsing_opts:
                    if opt_lines and not l.startswith(('Question', 'www.vu786', 'http')):
                        opt_lines[-1] += " " + l
                else:
                    if not any(k in l for k in ['www.vu786', 'http', 'STA301', 'MIDTERM', 'Ref No:']):
                        q_lines.append(l)
            
            q_text = clean_text(" ".join(q_lines))
            if not q_text or len(q_text) < 10:
                continue
            
            options = []
            correct_idx = -1
            for o_str in opt_lines:
                is_corr = o_str.startswith('*►')
                clean_opt = re.sub(r'^\*?►\s*', '', o_str)
                if clean_opt:
                    options.append(clean_opt)
                    if is_corr and correct_idx == -1:
                        correct_idx = len(options) - 1
            
            if add_objective(q_text, options, correct_idx, correct_idx != -1, os.path.basename(pf), "Extracted from official VU Midterm Past Examination Papers."):
                extracted += 1
    print(f"Past Paper series parsed: {extracted} questions")

# -------------------------------------------------------------
# 8. PARSE SUBJECTIVE QUESTIONS
# -------------------------------------------------------------
all_subjective_questions = []
seen_subj_signatures = set()

def add_subjective(q_text, sol_text, marks, source, explanation=""):
    if not is_valid_sta301(q_text) or len(q_text) < 15 or len(sol_text) < 5:
        return False
    sig = normalize_q(q_text)
    if sig in seen_subj_signatures:
        return False
    seen_subj_signatures.add(sig)
    topic = classify_topic(q_text)
    marks_str = f"{marks} Marks" if isinstance(marks, int) else str(marks)
    if "marks" not in marks_str.lower():
        marks_str = f"{marks_str} Marks"
    all_subjective_questions.append({
        "id": len(all_subjective_questions) + 1,
        "question": q_text,
        "marks": marks_str,
        "answer": sol_text,
        "topic": topic,
        "source": source
    })
    return True

def parse_subjective():
    # A. Moaaz Solved Subjective PDF & Doc
    subj_files = [
        os.path.join(SUBJ_DIR, "STA301 Midterm Solved Subjective with References by Moaaz.pdf"),
        os.path.join(SUBJ_DIR, "STA301 Midterm Solved Subjective 2012.pdf"),
        os.path.join(SUBJ_DIR, "STA301 Midterm Solved Subjective with References (Word) by Moaaz.doc"),
        os.path.join(SUBJ_DIR, "STA301 Midterm Solved Subjective with References (Word) Set 2 by Moaaz.doc")
    ]
    extracted = 0
    for sf in subj_files:
        if not os.path.exists(sf):
            continue
        ext = os.path.splitext(sf)[1].lower()
        if ext == '.doc':
            raw_text = extract_doc(sf)
            text = re.sub(r'^[\|\s]+|[\|\s]+$', '', raw_text, flags=re.MULTILINE)
        else:
            text = extract_pdf_plain(sf)
            
        blocks = re.split(r'\n(?=Question\s*(?:\(\s*Marks|\s*No:|\s*#))', text, flags=re.IGNORECASE)
        for b in blocks:
            if not b.strip() or not re.search(r'Question', b, re.IGNORECASE):
                continue
            
            m_marks = re.search(r'Marks:\s*(\d+)', b, re.IGNORECASE)
            marks = int(m_marks.group(1)) if m_marks else 3
            
            m_sol = re.search(r'\n\s*(?:Solution|Answer)\s*[:-]\s*', b, re.IGNORECASE)
            if m_sol:
                q_part = b[:m_sol.start()]
                sol_part = b[m_sol.end():]
            else:
                lines = [l.strip() for l in b.split('\n') if l.strip()]
                if len(lines) >= 3:
                    q_part = " ".join(lines[1:3])
                    sol_part = "\n".join(lines[3:])
                else:
                    continue
            
            q_lines = [l.strip() for l in q_part.split('\n') if l.strip()]
            cleaned_qlines = []
            for l in q_lines:
                if re.match(r'^Question\s*(?:\(\s*Marks|\s*No:|\s*#)', l, re.IGNORECASE):
                    continue
                if not any(k in l for k in ['STA301', 'MIDTERM', 'Moaaz', 'http']):
                    cleaned_qlines.append(l)
            
            q_text = clean_text(" ".join(cleaned_qlines))
            sol_text = clean_text(sol_part)
            sol_text = re.split(r'\n\s*Question', sol_text, flags=re.IGNORECASE)[0].strip()
            
            if add_subjective(q_text, sol_text, marks, "Moaaz Solved Subjective"):
                extracted += 1

    # B. Masters Midterm Preparation & Data
    masters_files = [
        os.path.join(SUBJ_DIR, "STA301 Midterm Preparation by Masters.pdf"),
        os.path.join(PAST_DIR, "STA301 Midterm Data by Masters.pdf")
    ]
    for mf in masters_files:
        if os.path.exists(mf):
            m_text = extract_pdf_plain(mf)
            lines = [l.strip() for l in m_text.split('\n') if l.strip()]
            for idx, l in enumerate(lines[:-1]):
                if l.endswith('?') and len(l) > 15:
                    q_text = re.sub(r'^\d+[\.\)]\s*', '', l).strip()
                    ans_text = lines[idx+1].strip()
                    if not ans_text.endswith('?') and len(ans_text) >= 3 and not any(k in ans_text for k in ['PREPARED BY', 'MASTERS', 'MID TERM']):
                        if add_subjective(q_text, ans_text, 2, "Masters Midterm Preparation", "Core statistical concept question with concise definitive answer."):
                            extracted += 1

    # C. Prince Alvi Current Papers
    prince_path = os.path.join(PAST_DIR, "STA301 Midterm Current Solved Papers Spring 2022 by Prince Alvi.pdf")
    if os.path.exists(prince_path):
        p_text = extract_pdf_plain(prince_path)
        blocks = re.split(r'\n(?=Q\d+[\)\.])', p_text)
        for b in blocks:
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            if len(lines) >= 2:
                q_line = re.sub(r'^Q\d+[\)\.]\s*', '', lines[0]).strip()
                ans_lines = [l for l in lines[1:] if not any(k in l for k in ['princealvi', 'SPRING 2022', 'STA301'])]
                ans_text = clean_text(" ".join(ans_lines))
                if q_line and len(q_line) >= 10 and ans_text and len(ans_text) >= 15:
                    if add_subjective(q_line, ans_text, 3, "Prince Alvi Current Solved Papers", "Current midterm examination solved subjective question."):
                        extracted += 1

    print(f"Subjective parsed: {len(all_subjective_questions)} questions")

# Execute extraction
print("Starting STA301 Extraction Pipeline...")
parse_moaaz_files()
parse_mehwish()
parse_junaid_files()
parse_arslan_uzair()
parse_lucky()
parse_vu_topper()
parse_past_paper_series()
parse_subjective()

print(f"\n==========================================")
print(f"STA301 Objective Questions Extracted: {len(all_objective_questions)}")
print(f"STA301 Subjective Questions Extracted: {len(all_subjective_questions)}")

tf_count = sum(1 for q in all_objective_questions if q['type'] == 'true_false')
mcq_count = sum(1 for q in all_objective_questions if q['type'] == 'mcq')
verified_count = sum(1 for q in all_objective_questions if q['has_verified_answer'])
print(f"  - MCQs: {mcq_count}")
print(f"  - True / False: {tf_count}")
print(f"  - Verified Answers: {verified_count} ({verified_count/len(all_objective_questions)*100:.1f}%)")

obj_topics = Counter(q['topic'] for q in all_objective_questions)
print("\nObjective Topic Distribution:")
for top, cnt in obj_topics.most_common():
    print(f"  - {top}: {cnt}")

subj_topics = Counter(q['topic'] for q in all_subjective_questions)
print("\nSubjective Topic Distribution:")
for top, cnt in subj_topics.most_common():
    print(f"  - {top}: {cnt}")

# Save JSON outputs
with open(os.path.join(WORKSPACE, "sta301_objective.json"), "w", encoding="utf-8") as f:
    json.dump(all_objective_questions, f, indent=2, ensure_ascii=False)

with open(os.path.join(WORKSPACE, "sta301_subjective.json"), "w", encoding="utf-8") as f:
    json.dump(all_subjective_questions, f, indent=2, ensure_ascii=False)

print("\nFiles written successfully: sta301_objective.json, sta301_subjective.json")
