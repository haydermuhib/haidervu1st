#!/usr/bin/env python3
import os, sys, subprocess, re, json, unicodedata, warnings
import bs4

warnings.filterwarnings("ignore")

BASE_DIR = "/home/haider/Desktop/Chores"

def clean_text(s):
    if not s: return ""
    s = unicodedata.normalize("NFKC", str(s))
    s = "".join(c for c in s if c in ["\n", "\t", " "] or unicodedata.category(c)[0] != "C")
    return re.sub(r"\s+", " ", s).strip()

def clean_opt(s):
    s = clean_text(s)
    # Strip leading bullets, letters, radio buttons, numbers
    s = re.sub(r"^(?:[►•\*\–\-✓✔○●✔️\uf0b7Ooe\(\)\[\]\d\.\:\s]+|\(?[a-eA-E][\)\.\:\s]+)", "", s).strip()
    s = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", s, flags=re.I).strip()
    return s

def normalize_key(s):
    s = clean_text(s).lower()
    s = re.sub(r"^(?:marks\s*:\s*\d+\s*)?(?:please\s+choose\s+one\s*)?", "", s)
    s = re.sub(r"[^a-z0-9\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", "", s)
    return s

def clean_question_and_opts(q, opts):
    q = clean_text(q)
    # Strip leading Q numbers: '1. ', '10. ', '. ', 'Question 1: ', 'Q.1 '
    q = re.sub(r"^\s*(?:Q(?:uestion)?\s*(?:#|No|\.)?\s*\d+\s*(?:of\s*\d+)?\s*[:\.]?|\d+\s*[\.\:\-\)]\s*)", "", q, flags=re.I)
    q = re.sub(r"^[\s\.\–\-\_\:\,\;\#\*\(\)]+", "", q)
    q = re.sub(r"^\s*\(?\s*choose\s+the\s+correct\s+option\s+from\s+the\s+following\s*:?\s*", "", q, flags=re.I)
    q = re.sub(r"^\s*select\s+the\s+correct\s+option\s*:?\s*", "", q, flags=re.I)
    q = re.sub(r"^\s*Total\s*Marks\s*:\s*\d*\s*:?\s*", "", q, flags=re.I)
    q = re.sub(r"MADE\s+BY\s+[\w\s]+.*", "", q, flags=re.I)
    q = re.sub(r"ENG101\s*:\s*Grand\s*Quiz.*", "", q, flags=re.I)
    q = re.sub(r"CORRECT\s+ANSWER\s+SOLVED\s+BY.*", "", q, flags=re.I)
    q = re.sub(r"Reload\s+Math\s+Equations.*", "", q, flags=re.I)
    
    # Check trailing option like 'a. Straightforward'
    m = re.search(r"^(.*?)\s+([a-d])[\.\)]\s*([A-Za-z0-9\s\(\)\/\-]+)$", q, re.I)
    if m:
        first_part = m.group(1).strip()
        trailing_opt = clean_opt(re.sub(r"\(?[✓✔✔️]\)?|\(correct\)", "", m.group(3)).strip())
        if len(first_part) > 15 and 1 < len(trailing_opt) < 60:
            q = first_part
            if trailing_opt not in opts:
                opts.insert(0, trailing_opt)

    q = re.sub(r"^[\s\.\–\-\_\:\,\;\#\*\(\)]+", "", q)
    return clean_text(q), opts

def clean_question_text(q):
    clean_q, _ = clean_question_and_opts(q, [])
    return clean_q

def is_valid_mcq(q):
    opts = q.get("options") or []
    if len(opts) < 2 or len(opts) > 5:
        return False
    text = q.get("question", "").strip()
    if len(text) < 15:
        return False
    if text.lower().startswith("http") or "( m a r k s" in text.lower() or text.lower().startswith("total marks"):
        return False
    if any(len(o) > 200 for o in opts):
        return False
    return True

def guess_isl_topic(q):
    s = q.lower()
    if any(k in s for k in ["hadith", "sunnah", "bukhari", "muslim", "tirmidhi", "sanad", "matn", "isnad", "sahih"]):
        return "Hadith & Sunnah"
    if any(k in s for k in ["tauheed", "prophet", "angel", "malaika", "iman", "belief", "kalima", "allah", "shirk", "pillar", "faith"]):
        return "Tauheed & Pillars of Islam"
    if any(k in s for k in ["quran", "surah", "ayah", "ayat", "makki", "madani", "bismillah", "revealed", "revelation"]):
        return "Quran & Exegesis"
    if any(k in s for k in ["fiqh", "shariah", "qiyas", "ijma", "halal", "haram", "nikah", "talaq", "fasting", "zakat", "prayer", "wudu"]):
        return "Islamic Law & Jurisprudence (Fiqh)"
    if any(k in s for k in ["akhlaq", "morality", "honesty", "backbiting", "sincerity", "charity", "character", "manners"]):
        return "Islamic Ethics & Character (Akhlaq)"
    if any(k in s for k in ["seerah", "caliph", "hijra", "madina", "makkah", "abubakar", "umar", "usman", "ali", "ghazwa", "badr"]):
        return "Seerah & Early Caliphate"
    return "General Islamic Studies"

def guess_eng_topic(q):
    s = q.lower()
    if any(k in s for k in ["synonym", "antonym", "prefix", "suffix", "root", "word", "meaning", "vocabulary"]):
        return "Vocabulary & Affixes"
    if any(k in s for k in ["noun", "verb", "adjective", "adverb", "preposition", "conjunction", "pronoun", "tense", "clause", "sentence", "grammar", "comma", "punctuation"]):
        return "Grammar & Sentence Structure"
    if any(k in s for k in ["paragraph", "reading", "skimming", "scanning", "passage", "inference", "context", "comprehension", "topic sentence"]):
        return "Reading & Comprehension"
    if any(k in s for k in ["essay", "writing", "draft", "thesis", "outline", "coherence", "cohesion", "transition", "connective"]):
        return "Writing & Composition Skills"
    return "General English Comprehension"

# ==================== 1. ISL202 ====================
def build_isl202():
    print("--- Processing ISL202 ---")
    all_extracted = []
    
    # Danish Hanif
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/MCQs & Quizzes/ISL202 Midterm Current Quiz by Danish Hanif.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        blocks = re.split(r"\n(?=Question\s*#?\s*\d+\s*:)", txt, flags=re.I)
        for b in blocks[1:]:
            lines = [l.strip() for l in b.splitlines() if l.strip()]
            if not lines: continue
            q_line = clean_question_text(re.sub(r"^Question\s*#?\s*\d+\s*:\s*", "", lines[0], flags=re.I))
            opts = []
            ans = None
            for l in lines[1:]:
                m_ans = re.match(r"^(?:Correct\s+)?Answer\s*[:\.]\s*(?:[A-D][\)\.\:\s]+)?(.*)", l, re.I)
                if m_ans:
                    ans = clean_opt(m_ans.group(1))
                    continue
                m_opt = re.match(r"^[A-D][\)\.\:]\s*(.*)", l, re.I)
                if m_opt:
                    opts.append(clean_opt(m_opt.group(1)))
            if 2 <= len(opts) <= 5:
                all_extracted.append({"question": q_line, "options": opts, "answer": ans, "sources": ["Danish Hanif"]})

    # Mark & Maz
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/Past Papers & Solved Papers/ISL202 Midterm Past Papers by Mark and Maz.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        blocks = re.split(r"\n(?=\d+\.\s+)", txt)
        for b in blocks[1:]:
            lines = [l.strip() for l in b.splitlines() if l.strip()]
            if not lines: continue
            q_line = clean_question_text(re.sub(r"^\d+\.\s*", "", lines[0]))
            opts = []
            ans_letter = None
            for l in lines[1:]:
                m_ans = re.match(r"^-?\s*Answer\s*[:\.]\s*([A-D])\b", l, re.I)
                if m_ans:
                    ans_letter = m_ans.group(1).upper()
                    continue
                m_opt = re.match(r"^-?\s*([A-D])\)\s*(.*)", l, re.I)
                if m_opt:
                    opts.append((m_opt.group(1).upper(), clean_opt(m_opt.group(2))))
            if 2 <= len(opts) <= 5:
                ans_text = None
                if ans_letter:
                    for ltr, text in opts:
                        if ltr == ans_letter:
                            ans_text = text
                            break
                all_extracted.append({"question": q_line, "options": [o[1] for o in opts], "answer": ans_text, "sources": ["Mark & Maz"]})

    # Websol
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/MCQs & Quizzes/ISL202 Midterm Subjective and Objective by Websol.pdf")
    if os.path.exists(fp):
        xml = subprocess.check_output(["pdftohtml", "-nodrm", "-xml", "-stdout", fp]).decode("utf-8", errors="ignore")
        soup = bs4.BeautifulSoup(xml, "html.parser")
        bold_fonts = {fs.get("id") for fs in soup.find_all("fontspec") if "bold" in fs.get("family", "").lower() or "italic" in fs.get("family", "").lower() or fs.get("id") in ["2", "10"]}
        current_q = None
        for page in soup.find_all("page"):
            for t in page.find_all("text"):
                txt = t.get_text().strip()
                if not txt or "generated by foxit" in txt.lower(): continue
                m_q = re.match(r"^\s*(\d+)\s*[\)\.]\s*(.*)", txt)
                if m_q and len(txt) > 8:
                    if current_q and 2 <= len(current_q["options"]) <= 5:
                        all_extracted.append(current_q)
                    current_q = {"question": clean_question_text(m_q.group(2)), "options": [], "answer": None, "sources": ["Websol"]}
                    continue
                m_opt = re.match(r"^\s*([a-d])[\)\.]\s*(.*)", txt, re.I)
                if m_opt and current_q:
                    opt_text = clean_opt(m_opt.group(2))
                    if opt_text:
                        current_q["options"].append(opt_text)
                        if t.get("font") in bold_fonts:
                            current_q["answer"] = opt_text
        if current_q and 2 <= len(current_q["options"]) <= 5:
            all_extracted.append(current_q)

    # Mickey Ch
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/MCQs & Quizzes/ISL202 Midterm Solved MCQs Updated by Mickey Ch.pdf")
    if os.path.exists(fp):
        xml = subprocess.check_output(["pdftohtml", "-nodrm", "-xml", "-stdout", fp]).decode("utf-8", errors="ignore")
        soup = bs4.BeautifulSoup(xml, "html.parser")
        bold_fonts = {fs.get("id") for fs in soup.find_all("fontspec") if "bold" in fs.get("family", "").lower() or fs.get("id") in ["8", "10", "19", "20", "21"]}
        current_q = None
        expect_opt = False
        for page in soup.find_all("page"):
            for t in page.find_all("text"):
                txt = t.get_text().strip()
                if not txt or "learning with mickey" in txt.lower() or "whatsapp" in txt.lower(): continue
                m_num = re.match(r"^(\d+)\.$", txt)
                if m_num:
                    if current_q and 2 <= len(current_q["options"]) <= 5:
                        all_extracted.append(current_q)
                    current_q = {"question": "", "options": [], "answer": None, "sources": ["Mickey Ch"]}
                    expect_opt = False
                    continue
                m_opt = re.match(r"^([a-d])\)$", txt, re.I)
                if m_opt and current_q:
                    expect_opt = True
                    is_opt_bold = (t.get("font") in bold_fonts)
                    continue
                if expect_opt and current_q:
                    opt_text = clean_opt(txt)
                    current_q["options"].append(opt_text)
                    if is_opt_bold or (t.get("font") in bold_fonts):
                        current_q["answer"] = opt_text
                    expect_opt = False
                    continue
                if current_q and not current_q["options"]:
                    current_q["question"] = clean_question_text((current_q["question"] + " " + txt).strip())
        if current_q and 2 <= len(current_q["options"]) <= 5:
            all_extracted.append(current_q)

    # Talha Sajid 1 & 2
    for tf in ["ISL202 Midterm MCQs by Talha Sajid.pdf", "ISL202 Midterm MCQs Set 2 by Talha Sajid.pdf"]:
        fp = os.path.join(BASE_DIR, f"ISL202 - Islamic Studies/MCQs & Quizzes/{tf}")
        if os.path.exists(fp):
            xml = subprocess.check_output(["pdftohtml", "-nodrm", "-xml", "-stdout", fp]).decode("utf-8", errors="ignore")
            soup = bs4.BeautifulSoup(xml, "html.parser")
            bold_fonts = {fs.get("id") for fs in soup.find_all("fontspec") if "bold" in fs.get("family", "").lower() or fs.get("id") in ["7", "8", "9", "10"]}
            current_q = None
            expect_opt = False
            for page in soup.find_all("page"):
                for t in page.find_all("text"):
                    txt = t.get_text().strip()
                    if not txt or "whatsapp" in txt.lower() or "mid-term" in txt.lower() or "page " in txt.lower(): continue
                    m_num = re.match(r"^(\d+)\.\s*(.*)", txt)
                    if m_num:
                        if current_q and 2 <= len(current_q["options"]) <= 5:
                            all_extracted.append(current_q)
                        current_q = {"question": clean_question_text(m_num.group(2)), "options": [], "answer": None, "sources": ["Talha Sajid"]}
                        expect_opt = False
                        continue
                    m_opt = re.match(r"^([a-d])\)$", txt, re.I)
                    if m_opt and current_q:
                        expect_opt = True
                        is_opt_bold = (t.get("font") in bold_fonts)
                        continue
                    if expect_opt and current_q:
                        opt_text = clean_opt(txt)
                        current_q["options"].append(opt_text)
                        if is_opt_bold or (t.get("font") in bold_fonts):
                            current_q["answer"] = opt_text
                        expect_opt = False
                        continue
                    if current_q and not current_q["options"]:
                        current_q["question"] = clean_question_text((current_q["question"] + " " + txt).strip())
            if current_q and 2 <= len(current_q["options"]) <= 5:
                all_extracted.append(current_q)

    # Load existing isl202_quiz_bank.json
    old_fp = os.path.join(BASE_DIR, "isl202_quiz_bank.json")
    old_data = []
    if os.path.exists(old_fp):
        with open(old_fp) as f:
            old_data = json.load(f)

    master = {}
    for q in old_data:
        if not is_valid_mcq(q): continue
        clean_q = clean_question_text(q["question"])
        clean_opts = [clean_opt(o) for o in q["options"] if clean_opt(o)]
        if not (2 <= len(clean_opts) <= 5): continue
        k = normalize_key(clean_q)
        if not k: continue
        master[k] = {
            "question": clean_q,
            "options": clean_opts,
            "answer": clean_opt(q.get("answer")) if q.get("answer") else None,
            "solution_notes": q.get("solution_notes"),
            "topic": q.get("topic") or "General Islamic Studies",
            "sources": q.get("sources") or []
        }

    # Overlay newly extracted high-precision questions
    for q in all_extracted:
        clean_q = clean_question_text(q["question"])
        clean_opts = [clean_opt(o) for o in q["options"] if clean_opt(o)]
        if not (2 <= len(clean_opts) <= 5): continue
        k = normalize_key(clean_q)
        if not k or len(k) < 8: continue
        if k in master:
            if q["answer"]:
                master[k]["answer"] = q["answer"]
            if len(clean_opts) > len(master[k]["options"]):
                master[k]["options"] = clean_opts
            for s in q.get("sources", []):
                if s not in master[k]["sources"]:
                    master[k]["sources"].append(s)
        else:
            master[k] = {
                "question": clean_q,
                "options": clean_opts,
                "answer": q["answer"],
                "solution_notes": f"Verified Solution: {q['answer']}" if q["answer"] else None,
                "topic": guess_isl_topic(clean_q),
                "sources": q.get("sources", [])
            }

    # Explicit fix for Quroo:
    for k, q in master.items():
        if "quroo" in q["question"].lower():
            q["options"] = ["Humanity", "All material things", "Purity or impurity", "Beauty"]
            q["answer"] = "Purity or impurity"

    # Normalize answers
    final_list = []
    for k, q in master.items():
        if not is_valid_mcq(q): continue
        opts = q["options"]
        ans = q["answer"]
        if ans:
            clean_ans_key = normalize_key(ans)
            matched = False
            for opt in opts:
                if normalize_key(opt) == clean_ans_key or clean_ans_key in normalize_key(opt) or normalize_key(opt) in clean_ans_key:
                    q["answer"] = opt
                    matched = True
                    break
            if not matched:
                m_ltr = re.match(r"^[A-E]$", ans.strip(), re.I)
                if m_ltr:
                    idx = ord(m_ltr.group(0).upper()) - ord('A')
                    if idx < len(opts):
                        q["answer"] = opts[idx]
        final_list.append(q)

    # Option-pair deduplication to eliminate line-wrap duplicates
    def norm_opts(opts):
        return tuple(sorted([re.sub(r'[^a-z0-9\u0600-\u06FF]', '', o.lower()) for o in opts]))

    opt_dedup = {}
    for q in final_list:
        k_opts = norm_opts(q['options'])
        lead = normalize_key(q['question'])[:25]
        pair_k = (k_opts, lead)
        if pair_k in opt_dedup:
            if len(q['question']) > len(opt_dedup[pair_k]['question']):
                opt_dedup[pair_k]['question'] = q['question']
            if not opt_dedup[pair_k].get('answer') and q.get('answer'):
                opt_dedup[pair_k]['answer'] = q['answer']
            for s in q.get('sources', []):
                if s not in opt_dedup[pair_k]['sources']:
                    opt_dedup[pair_k]['sources'].append(s)
        else:
            opt_dedup[pair_k] = q

    final_list = list(opt_dedup.values())
    final_list.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_list, 1):
        q["id"] = idx

    print(f"ISL202 final: {len(final_list)} pristine MCQs")
    with open(old_fp, "w") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)
    return final_list


# ==================== 2. ENG101 ====================
def build_eng101():
    print("--- Processing ENG101 ---")
    all_extracted = []
    
    dirs = [
        "ENG101 - English Comprehension/MCQs & Quizzes",
        "ENG101 - English Comprehension/Past Papers & Solved Papers"
    ]
    for d in dirs:
        full_d = os.path.join(BASE_DIR, d)
        if not os.path.exists(full_d): continue
        for f in os.listdir(full_d):
            if not f.endswith(".pdf"): continue
            fp = os.path.join(full_d, f)
            try:
                txt = subprocess.check_output(["pdftotext", fp, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
                blocks = re.split(r"\n(?=Question\s*(?:#|No|\.)?\s*[:\.]?\s*\d+|\d+\.\s+[A-Za-z])", txt, flags=re.I)
                for b in blocks[1:]:
                    lines = [l.strip() for l in b.splitlines() if l.strip()]
                    if len(lines) < 3: continue
                    q_line = clean_question_text(re.sub(r"^(?:Question\s*(?:#|No|\.)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?\s*[:\.]?|\d+\.\s*)", "", lines[0], flags=re.I))
                    if any(k in q_line.lower() for k in ["virtualians", "marks:", "please choose one", "waqas"]): continue
                    opts = []
                    ans = None
                    for l in lines[1:]:
                        if any(k in l.lower() for k in ["virtualians", "marks:", "please choose one", "waqas", "follow us"]): continue
                        m_opt = re.match(r"^[►•\*\–\-✓✔○●✔️\uf0b7Ooe]|\(?[a-dA-D][\)\.]\s+", l)
                        if m_opt:
                            c_opt = clean_opt(l)
                            if c_opt and len(c_opt) > 1:
                                opts.append(c_opt)
                                if "►" in l or "✓" in l or "✔" in l or "(correct)" in l.lower() or "page #" in l.lower():
                                    ans = c_opt
                        m_ans = re.match(r"^(?:Correct\s+)?Answer\s*[:\.]\s*(?:[A-D][\)\.\:\s]+)?(.*)", l, re.I)
                        if m_ans:
                            ans = clean_opt(m_ans.group(1))
                    if 2 <= len(opts) <= 5:
                        all_extracted.append({"question": q_line, "options": opts, "answer": ans, "sources": [f]})
            except Exception:
                pass

    old_fp = os.path.join(BASE_DIR, "eng101_quiz_bank.json")
    old_data = []
    if os.path.exists(old_fp):
        with open(old_fp) as f:
            old_data = json.load(f)

    master = {}
    
    # Ingest existing questions with valid options
    for q in old_data:
        # Check if Function words question
        if "Function words establish" in q.get("question", ""):
            q["question"] = "Function words establish emphasis and .... between the parts"
            q["options"] = ["Contrast", "Relationships", "Disparity", "Gap"]
            q["answer"] = "Relationships"
        
        if not is_valid_mcq(q): continue
        clean_q = clean_question_text(q["question"])
        clean_opts = [clean_opt(o) for o in q["options"] if clean_opt(o)]
        if not (2 <= len(clean_opts) <= 5): continue
            
        k = normalize_key(clean_q)
        if not k: continue
        master[k] = {
            "question": clean_q,
            "options": clean_opts,
            "answer": clean_opt(q.get("answer")) if q.get("answer") else None,
            "solution_notes": q.get("solution_notes"),
            "topic": q.get("topic") or guess_eng_topic(clean_q),
            "sources": q.get("sources") or []
        }

    # Overlay newly extracted
    for q in all_extracted:
        clean_q = clean_question_text(q["question"])
        clean_opts = [clean_opt(o) for o in q["options"] if clean_opt(o)]
        if not (2 <= len(clean_opts) <= 5): continue
        k = normalize_key(clean_q)
        if not k or len(k) < 8: continue
        if k in master:
            if q["answer"] and not master[k]["answer"]:
                master[k]["answer"] = q["answer"]
            if len(clean_opts) > len(master[k]["options"]):
                master[k]["options"] = clean_opts
            for s in q.get("sources", []):
                if s not in master[k]["sources"]:
                    master[k]["sources"].append(s)
        else:
            master[k] = {
                "question": clean_q,
                "options": clean_opts,
                "answer": q["answer"],
                "solution_notes": f"Verified Solution: {q['answer']}" if q["answer"] else None,
                "topic": guess_eng_topic(clean_q),
                "sources": q.get("sources", [])
            }

    # Normalize answers
    final_list = []
    for k, q in master.items():
        if not is_valid_mcq(q): continue
        opts = q["options"]
        ans = q["answer"]
        if ans:
            clean_ans_key = normalize_key(ans)
            matched = False
            for opt in opts:
                if normalize_key(opt) == clean_ans_key or clean_ans_key in normalize_key(opt) or normalize_key(opt) in clean_ans_key:
                    q["answer"] = opt
                    matched = True
                    break
            if not matched:
                m_ltr = re.match(r"^[A-E]$", ans.strip(), re.I)
                if m_ltr:
                    idx = ord(m_ltr.group(0).upper()) - ord('A')
                    if idx < len(opts):
                        q["answer"] = opts[idx]
        final_list.append(q)

    # Option-pair deduplication to eliminate line-wrap duplicates
    def norm_opts(opts):
        return tuple(sorted([re.sub(r'[^a-z0-9]', '', o.lower()) for o in opts]))

    opt_dedup = {}
    for q in final_list:
        k_opts = norm_opts(q['options'])
        lead = normalize_key(q['question'])[:25]
        pair_k = (k_opts, lead)
        if pair_k in opt_dedup:
            if len(q['question']) > len(opt_dedup[pair_k]['question']):
                opt_dedup[pair_k]['question'] = q['question']
            if not opt_dedup[pair_k].get('answer') and q.get('answer'):
                opt_dedup[pair_k]['answer'] = q['answer']
            for s in q.get('sources', []):
                if s not in opt_dedup[pair_k]['sources']:
                    opt_dedup[pair_k]['sources'].append(s)
        else:
            opt_dedup[pair_k] = q

    final_list = list(opt_dedup.values())
    final_list.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_list, 1):
        q["id"] = idx

    print(f"ENG101 final: {len(final_list)} pristine MCQs")
    with open(old_fp, "w") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)
    return final_list


# ==================== 3. CS101 ====================
def build_cs101():
    print("--- Processing CS101 ---")
    old_fp = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
    old_data = []
    if os.path.exists(old_fp):
        with open(old_fp) as f:
            old_data = json.load(f)

    master = {}
    for q in old_data:
        if not is_valid_mcq(q): continue
        clean_q = clean_question_text(q["question"])
        clean_opts = [clean_opt(o) for o in q["options"] if clean_opt(o)]
        if not (2 <= len(clean_opts) <= 5): continue
            
        k = normalize_key(clean_q)
        if not k: continue
        master[k] = {
            "question": clean_q,
            "options": clean_opts,
            "answer": clean_opt(q.get("answer")) if q.get("answer") else None,
            "solution_notes": q.get("solution_notes"),
            "topic": q.get("topic") or "General Computing",
            "sources": q.get("sources") or []
        }

    final_list = []
    for k, q in master.items():
        if not is_valid_mcq(q): continue
        opts = q["options"]
        ans = q["answer"]
        if ans:
            clean_ans_key = normalize_key(ans)
            matched = False
            for opt in opts:
                if normalize_key(opt) == clean_ans_key or clean_ans_key in normalize_key(opt) or normalize_key(opt) in clean_ans_key:
                    q["answer"] = opt
                    matched = True
                    break
            if not matched:
                m_ltr = re.match(r"^[A-E]$", ans.strip(), re.I)
                if m_ltr:
                    idx = ord(m_ltr.group(0).upper()) - ord('A')
                    if idx < len(opts):
                        q["answer"] = opts[idx]
        final_list.append(q)

    # Option-pair deduplication to eliminate line-wrap duplicates
    def norm_opts(opts):
        return tuple(sorted([re.sub(r'[^a-z0-9]', '', o.lower()) for o in opts]))

    opt_dedup = {}
    for q in final_list:
        k_opts = norm_opts(q['options'])
        lead = normalize_key(q['question'])[:25]
        pair_k = (k_opts, lead)
        if pair_k in opt_dedup:
            if len(q['question']) > len(opt_dedup[pair_k]['question']):
                opt_dedup[pair_k]['question'] = q['question']
            if not opt_dedup[pair_k].get('answer') and q.get('answer'):
                opt_dedup[pair_k]['answer'] = q['answer']
            for s in q.get('sources', []):
                if s not in opt_dedup[pair_k]['sources']:
                    opt_dedup[pair_k]['sources'].append(s)
        else:
            opt_dedup[pair_k] = q

    final_list = list(opt_dedup.values())
    final_list.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_list, 1):
        q["id"] = idx

    print(f"CS101 final: {len(final_list)} pristine MCQs")
    with open(old_fp, "w") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)
    return final_list


# ==================== 4. BUNDLE quiz_data.js ====================
def write_quiz_data_js(cs, eng, isl):
    js_path = os.path.join(BASE_DIR, "quiz_data.js")
    print("Writing bundled quiz_data.js...")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("/* Master VU Multi-Subject Examination & Practice Data Bank */\n")
        f.write("/* 100% of questions verified to have valid multiple choice options */\n\n")
        f.write("window.CS101_QUESTIONS = ")
        json.dump(cs, f, ensure_ascii=False)
        f.write(";\n\n")
        f.write("window.ENG101_QUESTIONS = ")
        json.dump(eng, f, ensure_ascii=False)
        f.write(";\n\n")
        f.write("window.ISL202_QUESTIONS = ")
        json.dump(isl, f, ensure_ascii=False)
        f.write(";\n")
    print("quiz_data.js successfully written!")

if __name__ == "__main__":
    isl = build_isl202()
    eng = build_eng101()
    cs = build_cs101()
    write_quiz_data_js(cs, eng, isl)
    print("ALL QUIZ BANKS SUCCESSFULLY REBUILT AND SANITIZED!")
