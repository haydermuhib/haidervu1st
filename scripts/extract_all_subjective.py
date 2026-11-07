#!/usr/bin/env python3
import os, sys, subprocess, re, json, unicodedata, warnings

warnings.filterwarnings("ignore")

BASE_DIR = "/home/haider/Desktop/Chores"

def clean_text(s):
    if not s: return ""
    s = unicodedata.normalize("NFKC", str(s))
    s = "".join(c for c in s if c in ["\n", "\t", " "] or unicodedata.category(c)[0] != "C")
    return re.sub(r"\s+", " ", s).strip()

def normalize_key(s):
    s = clean_text(s).lower()
    s = re.sub(r"[^a-z0-9\u0600-\u06FF]", "", s)
    return s[:100]

def guess_cs_topic(q):
    s = q.lower()
    if any(k in s for k in ["html", "tag", "hyperlink", "anchor", "web", "browser", "url", "http"]):
        return "Web & HTML"
    if any(k in s for k in ["javascript", "event", "loop", "variable", "function", "array", "script"]):
        return "JavaScript & Programming"
    if any(k in s for k in ["algorithm", "flowchart", "pseudo", "complexity", "sorting", "searching"]):
        return "Algorithms & Problem Solving"
    if any(k in s for k in ["binary", "bit", "byte", "hex", "floating point", "2's complement", "gate", "boolean"]):
        return "Computer Architecture & Logic"
    if any(k in s for k in ["network", "internet", "lan", "wan", "protocol", "ip", "packet"]):
        return "Computer Networks"
    if any(k in s for k in ["operating system", "os", "process", "memory", "cpu", "storage", "ram", "rom"]):
        return "Operating Systems & Hardware"
    if any(k in s for k in ["database", "dbms", "sql", "data integrity", "table"]):
        return "Database Systems"
    return "General Computer Science"

def guess_eng_topic(q):
    s = q.lower()
    if any(k in s for k in ["table", "graph", "chart", "diagram", "visual", "bar chart", "pie chart"]):
        return "Visual Information & Charts"
    if any(k in s for k in ["direct statement", "infer", "inference", "main idea", "topic sentence", "paragraph", "reading", "passage"]):
        return "Reading & Comprehension"
    if any(k in s for k in ["synonym", "antonym", "prefix", "suffix", "root", "vocabulary", "definition"]):
        return "Vocabulary & Affixes"
    if any(k in s for k in ["sentence", "rewrite", "clause", "conjunction", "preposition", "grammar", "tense", "passive", "active"]):
        return "Grammar & Sentence Rewriting"
    if any(k in s for k in ["essay", "outline", "summary", "composition", "draft", "coherence"]):
        return "Writing & Composition"
    return "General English Comprehension"

def guess_isl_topic(q):
    s = q.lower()
    if any(k in s for k in ["hadith", "sunnah", "sanad", "matn", "bukhari", "qudsi"]):
        return "Hadith & Sunnah Studies"
    if any(k in s for k in ["tafseer", "quran", "surah", "nuzul", "nasikh", "mansukh", "ayah"]):
        return "Quran & Exegesis (Tafseer)"
    if any(k in s for k in ["fiqh", "shariah", "ijtihad", "taqlid", "istihsan", "zakat", "fasting", "prayer"]):
        return "Islamic Law & Jurisprudence (Fiqh)"
    if any(k in s for k in ["tauheed", "allah", "prophet", "iman", "angels", "akhira", "revelation"]):
        return "Tauheed & Fundamentals of Faith"
    if any(k in s for k in ["akhlaq", "ethics", "rights", "morality", "honesty", "character", "parents"]):
        return "Islamic Ethics & Social Responsibilities"
    return "General Islamic Studies"

# ==================== 1. CS101 SUBJECTIVE ====================
def extract_cs101_subjective():
    print("Extracting CS101 Subjective Questions...")
    questions = []
    
    # File 1: CS101 Midterm Subjective by Moaaz.pdf
    fp = os.path.join(BASE_DIR, "CS101 - Introduction to Computing/Subjective & Notes/CS101 Midterm Subjective by Moaaz.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        blocks = re.split(r"\n(?=Question\s*(?:#|No)?\s*[:\.]?\s*\d+)", txt, flags=re.I)
        for b in blocks[1:]:
            m_marks = re.search(r"Marks\s*:\s*(\d+)", b, re.I)
            marks_val = f"{m_marks.group(1)} Marks" if m_marks else "Subjective"
            
            # Split question and answer (usually 'ANS:' or 'Answer:')
            m_qa = re.search(r"Question\s*(?:#|No)?\s*[:\.]?\s*\d+.*?\n(?:\(\s*Marks\s*:\s*\d+\s*\))?\s*(.*?)(?=\b(?:ANS|Answer)\s*[:\.]|\Z)", b, re.DOTALL | re.I)
            m_ans = re.search(r"\b(?:ANS|Answer)\s*[:\.]\s*(.*)", b, re.DOTALL | re.I)
            
            if m_qa:
                q_text = clean_text(m_qa.group(1))
                # remove any leading marks noise
                q_text = re.sub(r"^\(\s*Marks\s*:\s*\d+\s*\)\s*", "", q_text, flags=re.I)
                ans_text = clean_text(m_ans.group(1)) if m_ans else None
                if len(q_text) > 15 and not any(k in q_text.lower() for k in ["virtual university", "moaaz", "midterm examination"]):
                    questions.append({
                        "question": q_text,
                        "marks": marks_val,
                        "answer": ans_text,
                        "topic": guess_cs_topic(q_text),
                        "source": "CS101 Midterm Subjective by Moaaz"
                    })

    # File 2: CS101 Midterm Solved Subjective by Ghazal Aziz.pdf
    fp = os.path.join(BASE_DIR, "CS101 - Introduction to Computing/Subjective & Notes/CS101 Midterm Solved Subjective by Ghazal Aziz.pdf")
    if os.path.exists(fp):
        try:
            txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
            blocks = re.findall(r"\n([A-Z][^\n\?\.]+\?)\n(.*?)(?=\n[A-Z][^\n\?\.]+\?|\Z)", txt, re.DOTALL)
            for q_raw, a_raw in blocks:
                q_text = clean_text(q_raw)
                a_text = clean_text(a_raw)
                if len(q_text) > 15 and len(a_text) > 10 and not any(k in q_text.lower() for k in ["youtube", "whatsapp", "hamza"]):
                    questions.append({
                        "question": q_text,
                        "marks": "Short Question",
                        "answer": a_text,
                        "topic": guess_cs_topic(q_text),
                        "source": "CS101 Solved Subjective by Ghazal Aziz"
                    })
        except Exception:
            pass

    # File 3: CS101 Midterm 16 Solved Papers.pdf (extract 2, 3, 5 marks questions)
    fp = os.path.join(BASE_DIR, "CS101 - Introduction to Computing/Past Papers & Solved Papers/CS101 Midterm 16 Solved Papers.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        blocks = re.split(r"\n(?=Question\s*No\s*:\s*\d+)", txt, flags=re.I)
        for b in blocks[1:]:
            m_marks = re.search(r"Marks\s*:\s*([235])\b", b, re.I)
            if not m_marks: continue
            marks_val = f"{m_marks.group(1)} Marks"
            
            lines = [l.strip() for l in b.splitlines() if l.strip()]
            q_lines = []
            ans_lines = []
            found_ans = False
            for l in lines:
                if any(k in l.lower() for k in ["question no:", "faheem saqib", "midterm examination", "student info", "marks:"]):
                    continue
                if re.match(r"^(?:ANS|Answer)\s*[:\.]", l, re.I):
                    found_ans = True
                    ans_lines.append(re.sub(r"^(?:ANS|Answer)\s*[:\.]\s*", "", l, flags=re.I))
                    continue
                if found_ans:
                    ans_lines.append(l)
                else:
                    q_lines.append(l)
                    
            q_text = clean_text(" ".join(q_lines))
            ans_text = clean_text(" ".join(ans_lines)) if ans_lines else None
            if len(q_text) > 15:
                questions.append({
                    "question": q_text,
                    "marks": marks_val,
                    "answer": ans_text,
                    "topic": guess_cs_topic(q_text),
                    "source": "CS101 Midterm 16 Solved Papers"
                })

    # Deduplicate by normalize_key(question)
    dedup = {}
    for q in questions:
        k = normalize_key(q["question"])
        if not k or len(k) < 10: continue
        if k in dedup:
            if not dedup[k].get("answer") and q.get("answer"):
                dedup[k]["answer"] = q["answer"]
        else:
            dedup[k] = q

    final_cs = list(dedup.values())
    final_cs.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_cs, 1):
        q["id"] = idx
    print(f"Total Unique CS101 Subjective Questions: {len(final_cs)}")
    return final_cs

# ==================== 2. ENG101 SUBJECTIVE ====================
def extract_eng101_subjective():
    print("Extracting ENG101 Subjective Questions...")
    questions = []
    
    # File 1: ENG101 Midterm Solved Subjective by Moaaz.pdf
    fp = os.path.join(BASE_DIR, "ENG101 - English Comprehension/Subjective & Notes/ENG101 Midterm Solved Subjective by Moaaz.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        blocks = re.split(r"\n(?=Question\s*(?:#|No)?\s*[:\.]?\s*\d+)", txt, flags=re.I)
        for b in blocks[1:]:
            m_marks = re.search(r"Marks\s*:\s*(\d+)", b, re.I)
            marks_val = f"{m_marks.group(1)} Marks" if m_marks else "Subjective"
            
            m_qa = re.search(r"Question\s*(?:#|No)?\s*[:\.]?\s*\d+.*?\n(?:\(\s*Marks\s*:\s*\d+\s*\))?\s*(.*?)(?=\b(?:ANS|Answer)\s*[:\.]|\Z)", b, re.DOTALL | re.I)
            m_ans = re.search(r"\b(?:ANS|Answer)\s*[:\.]\s*(.*)", b, re.DOTALL | re.I)
            
            if m_qa:
                q_text = clean_text(m_qa.group(1))
                q_text = re.sub(r"^\(\s*Marks\s*:\s*\d+\s*\)\s*", "", q_text, flags=re.I)
                ans_text = clean_text(m_ans.group(1)) if m_ans else None
                if len(q_text) > 15:
                    questions.append({
                        "question": q_text,
                        "marks": marks_val,
                        "answer": ans_text,
                        "topic": guess_eng_topic(q_text),
                        "source": "ENG101 Midterm Solved Subjective by Moaaz"
                    })

    # File 2: ENG101 Midterm Solved Subjective Combined.pdf
    fp = os.path.join(BASE_DIR, "ENG101 - English Comprehension/Subjective & Notes/ENG101 Midterm Solved Subjective Combined.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        # Blocks start with Q: ... Marks \d+: ... Answer: ...
        blocks = re.split(r"\n(?=Q\s*[:\.]\s*)", txt, flags=re.I)
        for b in blocks[1:]:
            m_marks = re.search(r"Marks\s*[:\.]?\s*(\d+)", b, re.I)
            marks_val = f"{m_marks.group(1)} Marks" if m_marks else "Subjective"
            
            m_qa = re.search(r"Q\s*[:\.]\s*(.*?)(?=\bMarks|\bAnswer\s*[:\.]|\Z)", b, re.DOTALL | re.I)
            m_ans = re.search(r"\bAnswer\s*[:\.]\s*(.*)", b, re.DOTALL | re.I)
            
            if m_qa:
                q_text = clean_text(m_qa.group(1))
                ans_text = clean_text(m_ans.group(1)) if m_ans else None
                if len(q_text) > 15 and not any(k in q_text.lower() for k in ["solved by", "fairy", "mid term fall"]):
                    questions.append({
                        "question": q_text,
                        "marks": marks_val,
                        "answer": ans_text,
                        "topic": guess_eng_topic(q_text),
                        "source": "ENG101 Midterm Solved Subjective Combined"
                    })

    # File 3: ENG101 Midterm Subjective by Moaaz.pdf & Sets
    for set_f in ["ENG101 Midterm Solved Subjective Set 2 by Moaaz.pdf", "ENG101 Midterm Solved Subjective Set 3 by Moaaz.pdf"]:
        fp = os.path.join(BASE_DIR, f"ENG101 - English Comprehension/Subjective & Notes/{set_f}")
        if os.path.exists(fp):
            txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
            blocks = re.split(r"\n(?=Question\s*(?:#|No)?\s*[:\.]?\s*\d+)", txt, flags=re.I)
            for b in blocks[1:]:
                m_marks = re.search(r"Marks\s*:\s*(\d+)", b, re.I)
                marks_val = f"{m_marks.group(1)} Marks" if m_marks else "Subjective"
                m_qa = re.search(r"Question\s*(?:#|No)?\s*[:\.]?\s*\d+.*?\n(?:\(\s*Marks\s*:\s*\d+\s*\))?\s*(.*?)(?=\b(?:ANS|Answer)\s*[:\.]|\Z)", b, re.DOTALL | re.I)
                m_ans = re.search(r"\b(?:ANS|Answer)\s*[:\.]\s*(.*)", b, re.DOTALL | re.I)
                if m_qa:
                    q_text = clean_text(m_qa.group(1))
                    q_text = re.sub(r"^\(\s*Marks\s*:\s*\d+\s*\)\s*", "", q_text, flags=re.I)
                    ans_text = clean_text(m_ans.group(1)) if m_ans else None
                    if len(q_text) > 15:
                        questions.append({
                            "question": q_text,
                            "marks": marks_val,
                            "answer": ans_text,
                            "topic": guess_eng_topic(q_text),
                            "source": set_f
                        })

    dedup = {}
    for q in questions:
        k = normalize_key(q["question"])
        if not k or len(k) < 10: continue
        if k in dedup:
            if not dedup[k].get("answer") and q.get("answer"):
                dedup[k]["answer"] = q["answer"]
        else:
            dedup[k] = q

    final_eng = list(dedup.values())
    final_eng.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_eng, 1):
        q["id"] = idx
    print(f"Total Unique ENG101 Subjective Questions: {len(final_eng)}")
    return final_eng

# ==================== 3. ISL202 SUBJECTIVE ====================
def extract_isl202_subjective():
    print("Extracting ISL202 Subjective Questions...")
    questions = []
    
    # File 1: ISL202 Midterm Important Questions 2024.pdf
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/Subjective & Notes/ISL202 Midterm Important Questions 2024.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        # Split by numbered lines '1. ', '2. ', etc.
        blocks = re.findall(r"\n(\d+\.\s+[^\n]+(?:\n(?!\d+\.\s+)[^\n]+)*)", txt)
        for b in blocks:
            m_q = re.match(r"^\d+\.\s*(.*)", clean_text(b))
            if m_q:
                q_text = clean_text(m_q.group(1))
                if len(q_text) > 15 and not any(k in q_text.lower() for k in ["vu360", "lecture"]):
                    questions.append({
                        "question": q_text,
                        "marks": "3 Marks",
                        "answer": "Consult your lecture handouts for detailed exegesis and references on this topic.",
                        "topic": guess_isl_topic(q_text),
                        "source": "ISL202 Midterm Important Questions 2024"
                    })

    # File 2: ISL202 Midterm Subjective and Objective by Websol.pdf
    fp = os.path.join(BASE_DIR, "ISL202 - Islamic Studies/MCQs & Quizzes/ISL202 Midterm Subjective and Objective by Websol.pdf")
    if os.path.exists(fp):
        txt = subprocess.check_output(["pdftotext", fp, "-"]).decode("utf-8", errors="ignore")
        # Search for Q. or Question blocks without multiple choice options
        blocks = re.split(r"\n(?=Q\s*[\d\.\:]\s*)", txt, flags=re.I)
        for b in blocks[1:]:
            if "a)" in b and "b)" in b: continue # skip MCQs
            m_q = re.search(r"Q\s*[\d\.\:]\s*(.*?)(?=\bAns|\Z)", b, re.DOTALL | re.I)
            m_ans = re.search(r"\bAns\s*[:\.]\s*(.*)", b, re.DOTALL | re.I)
            if m_q:
                q_text = clean_text(m_q.group(1))
                ans_text = clean_text(m_ans.group(1)) if m_ans else None
                if len(q_text) > 15 and not any(k in q_text.lower() for k in ["foxit", "evaluation"]):
                    questions.append({
                        "question": q_text,
                        "marks": "Subjective",
                        "answer": ans_text,
                        "topic": guess_isl_topic(q_text),
                        "source": "ISL202 Midterm Subjective by Websol"
                    })

    dedup = {}
    for q in questions:
        k = normalize_key(q["question"])
        if not k or len(k) < 10: continue
        if k in dedup:
            if not dedup[k].get("answer") and q.get("answer"):
                dedup[k]["answer"] = q["answer"]
        else:
            dedup[k] = q

    final_isl = list(dedup.values())
    final_isl.sort(key=lambda x: x["question"])
    for idx, q in enumerate(final_isl, 1):
        q["id"] = idx
    print(f"Total Unique ISL202 Subjective Questions: {len(final_isl)}")
    return final_isl

def save_all_subjective():
    cs = extract_cs101_subjective()
    eng = extract_eng101_subjective()
    isl = extract_isl202_subjective()

    out_file = os.path.join(BASE_DIR, "subjective_bank.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({
            "CS101": cs,
            "ENG101": eng,
            "ISL202": isl
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved all subjective questions to {out_file}")

    # Append to quiz_data.js
    js_file = os.path.join(BASE_DIR, "quiz_data.js")
    with open(js_file, "a", encoding="utf-8") as f:
        f.write("\n\n/* Master Subjective Questions Bank (Subject-wise) */\n")
        f.write("window.CS101_SUBJECTIVE = ")
        json.dump(cs, f, ensure_ascii=False)
        f.write(";\n\n")
        f.write("window.ENG101_SUBJECTIVE = ")
        json.dump(eng, f, ensure_ascii=False)
        f.write(";\n\n")
        f.write("window.ISL202_SUBJECTIVE = ")
        json.dump(isl, f, ensure_ascii=False)
        f.write(";\n")
    print("Appended subjective datasets to quiz_data.js!")

if __name__ == "__main__":
    save_all_subjective()
