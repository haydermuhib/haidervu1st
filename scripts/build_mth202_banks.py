#!/usr/bin/env python3
"""
Comprehensive MTH202 Discrete Mathematics Examination & Practice Data Extractor
Extracts:
1. Objective MCQs & True/False questions (from MCQs & Quizzes and Past Papers & Solved Papers)
2. Subjective Q&A (from Subjective & Notes and Past Paper descriptive questions)
"""

import os, sys, subprocess, re, json, unicodedata, zipfile, xml.etree.ElementTree as ET

BASE_DIR = "/home/haider/Desktop/Chores/MTH202 - Discrete Mathematics"

def clean_text(s):
    if not s: return ""
    s = unicodedata.normalize("NFKC", str(s))
    s = "".join(c for c in s if c in ["\n", "\t", " "] or unicodedata.category(c)[0] != "C")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()

def normalize_key(s):
    s = clean_text(s).lower()
    s = re.sub(r"[\/\\\[\]\{\}\(\)]", "", s)
    s = re.sub(r"[_\.\-]{2,}", "", s)
    s = re.sub(r"[^a-z0-9]", "", s)
    return s[:120]

def classify_mth202_topic(text):
    t = text.lower()
    if any(k in t for k in ["truth table", "tautolog", "contradiction", "proposition", "negation", "conditional", "converse", "contrapositive", "biconditional", "de morgan", "premise", "valid argument", "hypothesis"]):
        return "Logic & Propositions"
    if any(k in t for k in ["power set", "cartesian product", "disjoint", "subset", "venn diagram", "empty set", "cardinality", "countable"]):
        return "Set Theory"
    if any(k in t for k in ["reflexive", "symmetric", "transitive", "anti-symmetric", "antisymmetric", "irreflexive", "equivalence relation", "congruence", "partition", "modulo", "mod 5", "mod 3"]):
        return "Relations & Partitions"
    if any(k in t for k in ["one-to-one", "bijective", "injective", "surjective", "onto", "composition of f", "fog", "gof", "inverse of", "domain of", "range of", "floor function", "ceiling function"]):
        return "Functions & Mappings"
    if any(k in t for k in ["recurren", "arithmetic progression", "geometric", "fibonacci", "series", "sequence", "nth term", "sum of", "c_n", "a_n"]):
        return "Sequences & Recurrence"
    if any(k in t for k in ["induction", "basis step", "inductive step"]):
        return "Mathematical Induction"
    if any(k in t for k in ["logic gate", "not gate", "and gate", "or gate", "nand", "nor", "boolean algebra", "half adder", "full adder"]):
        return "Boolean Algebra & Circuits"
    if any(k in t for k in ["graph", "vertex", "edge", "degree", "isomorph", "planar", "euler", "adjacency matrix", "digraph"]):
        return "Graphs & Trees"
    return "Discrete Mathematics"

def read_pdf(fp):
    try:
        return subprocess.check_output(["pdftotext", fp, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    except Exception:
        return ""

def read_doc(fp):
    try:
        return subprocess.check_output(["antiword", fp], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    except Exception:
        return ""

def read_docx(fp):
    try:
        with zipfile.ZipFile(fp) as z:
            xml_content = z.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            paras = []
            for p in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
                txt = "".join(p.itertext()).strip()
                if txt:
                    paras.append(txt)
            return "\n".join(paras)
    except Exception:
        return ""

# ----------------- 1. OBJECTIVE EXTRACTION -----------------

def extract_objective_questions():
    questions_map = {} # norm_key -> { question, options, answer, solution_notes, topic, sources }

    def add_question(q_text, opts, ans=None, note=None, src="MTH202 Source"):
        q_text = clean_text(q_text)
        # Strip trailing True/False and checkmarks from question statement
        q_text = re.sub(r"[\s\.\-]+(?:True|False)\s*[✅✔]?\s*$", "", q_text, flags=re.I).strip()
        # Filter watermarks & junk
        if not q_text or len(q_text) < 8: return
        if any(bad in q_text.lower() for bad in ["cs607", "artificial intelligence", "what’s app", "whatsapp", "paid vu lms", "youtube", "mam mehwish 031"]):
            return
        # Clean options
        clean_opts = []
        for o in opts:
            ot = clean_text(o)
            # Remove option letter prefix like A. or 1. or a)
            ot = re.sub(r"^[A-Da-d1-4][\.\)\-]\s*", "", ot).strip()
            # Remove trailing marks like ✅ or (pg 12)
            ot = re.sub(r"[\s✅✔]+$", "", ot).strip()
            if ot and ot not in clean_opts:
                clean_opts.append(ot)

        if len(clean_opts) < 2:
            return

        # Clean answer
        if ans:
            ans = clean_text(ans)
            ans = re.sub(r"^[A-Da-d1-4][\.\)\-]\s*", "", ans).strip()
            ans = re.sub(r"[\s✅✔]+$", "", ans).strip()

        # Check if True/False
        opts_lower = [o.lower() for o in clean_opts]
        if "true" in opts_lower and "false" in opts_lower and len(clean_opts) == 2:
            clean_opts = ["True", "False"]
            if ans:
                ans = "True" if ans.lower() == "true" else ("False" if ans.lower() == "false" else ans)

        k = normalize_key(q_text)
        if k not in questions_map:
            questions_map[k] = {
                "question": q_text,
                "options": clean_opts,
                "answer": ans,
                "solution_notes": note,
                "topic": classify_mth202_topic(q_text),
                "sources": [src]
            }
        else:
            if src not in questions_map[k]["sources"]:
                questions_map[k]["sources"].append(src)
            if len(clean_opts) > len(questions_map[k]["options"]):
                questions_map[k]["options"] = clean_opts
            if not questions_map[k]["answer"] and ans:
                questions_map[k]["answer"] = ans
            if not questions_map[k]["solution_notes"] and note:
                questions_map[k]["solution_notes"] = note

    # Source 1: Miss Mehwish 2024 & Set 2
    for fn in ["MTH202 Midterm MCQs 2024 by Miss Mehwish.pdf", "MTH202 Midterm MCQs 2024 Set 2 by Miss Mehwish.pdf"]:
        fp = os.path.join(BASE_DIR, "MCQs & Quizzes", fn)
        txt = read_pdf(fp)
        # Collapse standalone bullet lines
        txt = re.sub(r"\s*\n\s*", " ", txt)
        # Strip recurring headers
        txt = re.sub(r"All Subjects WhatsApp Groups Available.*?(?:Live Quiz\)?|Available)", "", txt, flags=re.DOTALL)
        txt = re.sub(r"(?:Contact|Miss Mehwish|PAID VU|Note).*?\d{10,}", "", txt)
        
        lines = [l.strip() for l in txt.split("\n") if l.strip()]
        curr_q = []
        curr_opts = []
        for l in lines:
            if l.startswith(""):
                opt = l.replace("", "").strip()
                if opt:
                    curr_opts.append(opt)
            else:
                if curr_opts and curr_q:
                    q_full = " ".join(curr_q)
                    q_full = re.sub(r"^(?:Note:\s*Live quiz MCQs[^\n]*|MTH202[^\n]*)\s*", "", q_full, flags=re.I).strip()
                    q_full = re.sub(r"^\d+\.\s*", "", q_full).strip()
                    ans = None
                    for o in curr_opts:
                        if "✅" in o or "✔" in o:
                            ans = o
                            break
                    add_question(q_full, curr_opts, ans=ans, src=fn.replace(".pdf", ""))
                    curr_q = []
                    curr_opts = []
                curr_q.append(l)

        if curr_opts and curr_q:
            q_full = " ".join(curr_q)
            q_full = re.sub(r"^(?:Note:\s*Live quiz MCQs[^\n]*|MTH202[^\n]*)\s*", "", q_full, flags=re.I).strip()
            q_full = re.sub(r"^\d+\.\s*", "", q_full).strip()
            ans = None
            for o in curr_opts:
                if "✅" in o or "✔" in o:
                    ans = o
                    break
            add_question(q_full, curr_opts, ans=ans, src=fn.replace(".pdf", ""))

    # Source 2: VU Topper RM Sets 2 & 4 (Lettered options A., B., C., D.)
    for fn in ["MTH202 Midterm MCQs Set 2 by VU Topper RM.pdf", "MTH202 Midterm MCQs Set 4 by VU Topper RM.pdf"]:
        fp = os.path.join(BASE_DIR, "MCQs & Quizzes", fn)
        txt = read_pdf(fp)
        matches = re.finditer(r"(?:^|\n)([^\n]+\?|[^\n]+\.{3,}|[^\n]+(?:is|are|called|means|denotes|equal to)\s*[\.\_\-]*)\n\s*A\.\s*([^\n]+)\n\s*B\.\s*([^\n]+)(?:\n\s*C\.\s*([^\n]+))?(?:\n\s*D\.\s*([^\n]+))?", txt)
        for m in matches:
            q_text = m.group(1).strip()
            opts = [m.group(2).strip(), m.group(3).strip()]
            if m.group(4): opts.append(m.group(4).strip())
            if m.group(5): opts.append(m.group(5).strip())
            add_question(q_text, opts, src=fn.replace(".pdf", ""))

    # Source 3: VU Topper RM Set 1 & Set 3 (Solved with ➢ answer)
    for fn in ["MTH202 Midterm MCQs by VU Topper RM.pdf", "MTH202 Midterm MCQs Set 3 by VU Topper RM.pdf"]:
        fp = os.path.join(BASE_DIR, "MCQs & Quizzes", fn)
        txt = read_pdf(fp)
        q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt, flags=re.I)
        for s in q_splits[1:]:
            m_ans = re.search(r"➢\s*([^\n]+)", s)
            if m_ans:
                ans_text = m_ans.group(1).strip()
                q_part = s[:m_ans.start()]
                lines = [l.strip() for l in q_part.split("\n") if l.strip() and not any(k in l.lower() for k in ["marks", "vu-topper", "solution"])]
                q_text = " ".join(lines).strip()
                if q_text:
                    if ans_text.lower() in ["true", "false"]:
                        add_question(q_text, ["True", "False"], ans=ans_text, src="VU Topper Midterm MCQs")
                    else:
                        k = normalize_key(q_text)
                        if k in questions_map and not questions_map[k]["answer"]:
                            questions_map[k]["answer"] = ans_text
                        elif k not in questions_map:
                            add_question(q_text, [ans_text, "None of these"], ans=ans_text, src="VU Topper Midterm MCQs")

    # Source 4: Junaid Past Papers & Solved MCQs (Solved with 'o ')
    for fn in ["MTH202 Midterm Past Papers by Junaid.pdf", "MTH202 Midterm Solved MCQs Set 2 by Junaid.pdf", "MTH202 Midterm Solved MCQs by Junaid.pdf"]:
        fp = os.path.join(BASE_DIR, "Past Papers & Solved Papers" if "Past Papers" in fn else "MCQs & Quizzes", fn)
        txt = read_pdf(fp)
        blocks = re.findall(r"\n([^\n]+\?|[^\n]+\_{2,}|[^\n]+(?:is|are|called|means|defined as)\s*[\.\_\-]*)\n\s*o\s*([^\n]+)", txt)
        for q_text, ans_text in blocks:
            q_text = q_text.strip()
            ans_text = ans_text.strip()
            if ans_text.lower() in ["true", "false"]:
                add_question(q_text, ["True", "False"], ans=ans_text, src="Junaid Midterm MCQs")
            else:
                k = normalize_key(q_text)
                if k in questions_map and not questions_map[k]["answer"]:
                    questions_map[k]["answer"] = ans_text
                elif k not in questions_map:
                    add_question(q_text, [ans_text, "None of these"], ans=ans_text, src="Junaid Midterm MCQs")

    # Source 5: Attiq Kundi Midterm Quiz & Past Papers
    for fn, subf in [("MTH202 Midterm Quiz by Attiq Kundi.pdf", "MCQs & Quizzes"), ("MTH202 Midterm Past Papers Updated June 2022 by Attiq Kundi.pdf", "Past Papers & Solved Papers")]:
        fp = os.path.join(BASE_DIR, subf, fn)
        txt = read_pdf(fp)
        lines = [l.strip() for l in txt.split("\n") if l.strip()]
        for i in range(len(lines) - 1):
            line = lines[i]
            nxt = lines[i+1]
            if nxt.lower() in ["true", "false"] and len(line) > 15 and not line.lower().startswith("question"):
                add_question(line, ["True", "False"], ans=nxt, src="Attiq Kundi Midterm Quiz")
            elif ("___________" in line or line.endswith("?")) and len(line) > 15:
                if len(nxt) > 1 and not nxt.startswith("http") and not nxt.startswith("SUBSCRIBE"):
                    k = normalize_key(line)
                    if k in questions_map and not questions_map[k]["answer"]:
                        questions_map[k]["answer"] = nxt
                    elif k not in questions_map:
                        add_question(line, [nxt, "None of these"], ans=nxt, src="Attiq Kundi Midterm Quiz")

    # Source 6: Student Solved MCQs (.pdf & .doc)
    fp_pdf = os.path.join(BASE_DIR, "MCQs & Quizzes/MTH202 Midterm Solved MCQs with References by Students.pdf")
    fp_doc = os.path.join(BASE_DIR, "MCQs & Quizzes/MTH202 Midterm Solved MCQs with References (Word) by Students.doc")
    txt_students = read_pdf(fp_pdf) + "\n" + read_doc(fp_doc)
    q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt_students, flags=re.I)
    for s in q_splits[1:]:
        opts = re.findall(r"[►]\s*([^\n]+)", s)
        if len(opts) >= 2:
            m_q = re.search(r"Marks\s*:\s*\d+\s*\)\s*(?:-\s*Please choose one)?\s*(.*?)(?=[►]|\Z)", s, re.DOTALL | re.I)
            if m_q:
                q_text = clean_text(m_q.group(1))
                q_text = re.sub(r"^\[pic\]\s*", "", q_text).strip()
                ans = None
                for o in opts:
                    if any(k in o.lower() for k in ["p_", "pg", "page", "ref"]):
                        ans = o
                        break
                add_question(q_text, opts, ans=ans, src="Student Solved MCQs with References")

    # Source 6b: MTH202 Midterm Solved MCQs.pdf
    fp_sm = os.path.join(BASE_DIR, "MCQs & Quizzes/MTH202 Midterm Solved MCQs.pdf")
    txt_sm = read_pdf(fp_sm)
    q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt_sm, flags=re.I)
    for s in q_splits[1:]:
        opts = re.findall(r"►\s*([^\n]+)", s)
        if len(opts) >= 2:
            m_q = re.search(r"Marks\s*:\s*\d+\s*\)\s*(?:-\s*Please choose one)?\s*(.*?)(?=►|\Z)", s, re.DOTALL | re.I)
            if m_q:
                q_text = clean_text(m_q.group(1))
                q_text = re.sub(r"^\[pic\]\s*", "", q_text).strip()
                add_question(q_text, opts, src="MTH202 Midterm Solved MCQs")

    # Source 7: MTH202 Midterm Past Paper.doc
    fp_pp_doc = os.path.join(BASE_DIR, "Past Papers & Solved Papers/MTH202 Midterm Past Paper.doc")
    txt_pp = read_doc(fp_pp_doc)
    q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt_pp, flags=re.I)
    for s in q_splits[1:]:
        opts = re.findall(r"►\s*([^\n]+)", s)
        if len(opts) >= 2:
            m_q = re.search(r"Marks\s*:\s*\d+\s*\)\s*(?:-\s*Please choose one)?\s*(.*?)(?=►|\Z)", s, re.DOTALL | re.I)
            if m_q:
                q_text = clean_text(m_q.group(1))
                q_text = re.sub(r"^\[pic\]\s*", "", q_text).strip()
                add_question(q_text, opts, src="MTH202 Midterm Past Papers")

    # Source 8: Moaaz Midterm Quiz 1 (.docx)
    fp_docx = os.path.join(BASE_DIR, "MCQs & Quizzes/MTH202 Midterm Quiz 1.docx")
    txt_docx = read_docx(fp_docx)
    q_splits = re.split(r"Question\s*No\.?\s*\d+\s*[\:\.]?", txt_docx, flags=re.I)
    for s in q_splits[1:]:
        lines = [l.strip() for l in s.split("\n") if l.strip() and not any(k in l.lower() for k in ["mc1004", "moaaz", "latset", "page"])]
        if len(lines) >= 3:
            q_text = lines[0]
            opts = lines[1:5]
            if len(opts) >= 2:
                ans = None
                for o in opts:
                    if any(k in o.lower() for k in ["(pg", "page"]):
                        ans = o
                        break
                add_question(q_text, opts, ans=ans, src="Moaaz Midterm Quiz 1")

    # Source 9: Mega File (1,287 numbered items!)
    fp_mega = os.path.join(BASE_DIR, "MCQs & Quizzes/MTH202 Midterm MCQs Mega File.pdf")
    txt_mega = read_pdf(fp_mega)
    chunks = re.split(r"\n\s*\d{1,4}\.\s+", txt_mega)
    for c in chunks[1:]:
        lines = [clean_text(l) for l in c.split("\n") if clean_text(l)]
        if not lines: continue
        # Case A: True / False question
        if len(lines) >= 2 and lines[-1].lower() in ["true", "false"]:
            q_text = " ".join(lines[:-1]).strip()
            ans_val = "True" if lines[-1].lower() == "true" else "False"
            add_question(q_text, ["True", "False"], ans=ans_val, src="MTH202 Mega File")
        elif "------" in lines[0] or "is---------" in lines[0]:
            parts = re.split(r"[\-]{3,}", lines[0])
            if len(parts) >= 2:
                q_text = parts[0].strip()
                ans_text = parts[1].strip()
                if ans_text and len(q_text) > 10:
                    add_question(q_text, [ans_text, "None of these"], ans=ans_text, src="MTH202 Mega File")

    # Assemble finalized list
    final_list = []
    idx = 1
    for k, v in questions_map.items():
        if len(v["options"]) < 2:
            continue
        v["id"] = idx
        idx += 1
        final_list.append(v)

    return final_list

# ----------------- 2. SUBJECTIVE EXTRACTION -----------------

def extract_subjective_questions():
    subj_map = {} # norm_key -> { question, marks, answer, topic, source }

    def add_subj(q_text, a_text, marks="3 Marks", src="MTH202 Subjective"):
        q_text = clean_text(q_text)
        a_text = clean_text(a_text)
        if not q_text or len(q_text) < 15: return
        if any(bad in q_text.lower() for bad in ["youtube", "whatsapp", "subscribe", "paid lms"]): return
        k = normalize_key(q_text)
        if k not in subj_map:
            subj_map[k] = {
                "question": q_text,
                "marks": marks,
                "answer": a_text if a_text else None,
                "topic": classify_mth202_topic(q_text),
                "source": src
            }
        else:
            if not subj_map[k]["answer"] and a_text:
                subj_map[k]["answer"] = a_text

    # File 1: MTH202 Midterm Short Questions and Answers.pdf (92 Q&A pairs!)
    fp = os.path.join(BASE_DIR, "Subjective & Notes/MTH202 Midterm Short Questions and Answers.pdf")
    txt = read_pdf(fp)
    q_splits = re.split(r"\n(?=Question\s*[\:\.\d])", txt, flags=re.I)
    for s in q_splits[1:]:
        m = re.search(r"Question\s*[\:\.\d]\s*(.*?)(?=\bAnswer\s*[:\.]|\Z)", s, re.DOTALL | re.I)
        m_ans = re.search(r"\bAnswer\s*[:\.]\s*(.*)", s, re.DOTALL | re.I)
        if m:
            q_t = m.group(1).strip()
            a_t = m_ans.group(1).strip() if m_ans else ""
            add_subj(q_t, a_t, marks="3 Marks", src="MTH202 Short Questions & Answers")

    # File 2: MTH202 Midterm Solved Subjective Papers with References.pdf
    fp = os.path.join(BASE_DIR, "Subjective & Notes/MTH202 Midterm Solved Subjective Papers with References.pdf")
    txt = read_pdf(fp)
    q_splits = re.split(r"\n(?=Q\s*[:\.]\s*)", txt, flags=re.I)
    for s in q_splits[1:]:
        m = re.search(r"Q\s*[:\.]\s*(.*?)(?=\b(?:ANS|Answer)\s*[:\.]|\Z)", s, re.DOTALL | re.I)
        m_ans = re.search(r"\b(?:ANS|Answer)\s*[:\.]\s*(.*)", s, re.DOTALL | re.I)
        if m:
            q_t = m.group(1).strip()
            a_t = m_ans.group(1).strip() if m_ans else ""
            add_subj(q_t, a_t, marks="3 Marks", src="MTH202 Solved Subjective with References")

    # File 3: MTH202 Midterm Solved Subjective by Moaaz.pdf & 2011 Papers
    for fn in ["MTH202 Midterm Solved Subjective by Moaaz.pdf", "MTH202 Midterm Solved Subjective Including 2011 Papers by Moaaz.pdf"]:
        fp = os.path.join(BASE_DIR, "Subjective & Notes", fn)
        txt = read_pdf(fp)
        q_splits = re.split(r"Question\s*(?:no|No|#)?\s*\d+\s*[\:\.]?", txt, flags=re.I)
        for s in q_splits[1:]:
            m_marks = re.search(r"(?:marks|Marx)\s*[:\.]?\s*\(?(\d+)\)?", s, re.I)
            marks_val = f"{m_marks.group(1)} Marks" if m_marks else "3 Marks"
            lines = [clean_text(l) for l in s.split("\n") if clean_text(l) and not any(k in l.lower() for k in ["marks", "genrica", "virtual university", "youtube"])]
            if len(lines) >= 2:
                q_t = lines[0]
                a_t = "\n".join(lines[1:])
                add_subj(q_t, a_t, marks=marks_val, src="Moaaz Solved Midterm Subjective")

    # File 4: MTH202 Midterm Solved Subjective Papers with References (Word).doc
    fp_doc = os.path.join(BASE_DIR, "Subjective & Notes/MTH202 Midterm Solved Subjective Papers with References (Word).doc")
    txt_doc = read_doc(fp_doc)
    q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt_doc, flags=re.I)
    for s in q_splits[1:]:
        m_marks = re.search(r"Marks\s*:\s*(\d+)", s, re.I)
        marks_val = f"{m_marks.group(1)} Marks" if m_marks else "5 Marks"
        lines = [clean_text(l) for l in s.split("\n") if clean_text(l) and not l.startswith("|") and not "Marks:" in l]
        if len(lines) >= 2:
            q_t = lines[0]
            a_t = "\n".join(lines[1:])
            add_subj(q_t, a_t, marks=marks_val, src="MTH202 Solved Subjective Past Papers")

    # File 5: MTH202 Midterm Past Paper Set 2 & Set 3 (.doc)
    for fn in ["MTH202 Midterm Past Paper Set 2.doc", "MTH202 Midterm Past Paper Set 3.doc"]:
        fp = os.path.join(BASE_DIR, "Past Papers & Solved Papers", fn)
        txt = read_doc(fp)
        q_splits = re.split(r"Question\s*No\s*:\s*\d+", txt, flags=re.I)
        for s in q_splits[1:]:
            m_marks = re.search(r"Marks\s*:\s*([2-9])", s, re.I)
            if m_marks:
                marks_val = f"{m_marks.group(1)} Marks"
                lines = [clean_text(l) for l in s.split("\n") if clean_text(l) and not l.startswith("|") and not "Marks:" in l and not "choose one" in l]
                if lines:
                    q_t = lines[0]
                    a_t = "\n".join(lines[1:]) if len(lines) > 1 else ""
                    add_subj(q_t, a_t, marks=marks_val, src="MTH202 Midterm Past Papers")

    final_list = []
    idx = 1
    for k, v in subj_map.items():
        v["id"] = idx
        idx += 1
        final_list.append(v)

    return final_list

def main():
    print("=== EXTRACTING MTH202 OBJECTIVE QUESTIONS ===")
    obj_questions = extract_objective_questions()
    mcq_count = sum(1 for q in obj_questions if not (len(q["options"]) == 2 and "True" in q["options"] and "False" in q["options"]))
    tf_count = sum(1 for q in obj_questions if len(q["options"]) == 2 and "True" in q["options"] and "False" in q["options"])
    with_ans = sum(1 for q in obj_questions if q["answer"])
    print(f"Total Objective: {len(obj_questions)}")
    print(f"  MCQs: {mcq_count}")
    print(f"  True / False: {tf_count}")
    print(f"  With Verified Answer: {with_ans}")

    print("\n=== EXTRACTING MTH202 SUBJECTIVE QUESTIONS ===")
    subj_questions = extract_subjective_questions()
    subj_with_ans = sum(1 for q in subj_questions if q["answer"])
    print(f"Total Subjective: {len(subj_questions)}")
    print(f"  With Model Solution: {subj_with_ans}")

    with open("mth202_objective.json", "w", encoding="utf-8") as f:
        json.dump(obj_questions, f, ensure_ascii=False, indent=2)
    with open("mth202_subjective.json", "w", encoding="utf-8") as f:
        json.dump(subj_questions, f, ensure_ascii=False, indent=2)
    print("\nSaved mth202_objective.json and mth202_subjective.json!")

if __name__ == "__main__":
    main()
