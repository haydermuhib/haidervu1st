import os, sys, subprocess, re, json, hashlib
import xml.etree.ElementTree as ET

BASE_DIR = "/home/haider/Desktop/Chores"
CS101_DIR = os.path.join(BASE_DIR, "CS101 - Introduction to Computing", "MCQs & Quizzes")

TOPICS = [
    "Search Engines", "Roots of Computing", "Boolean Operations",
    "Hexadecimal Notation", "Binary Addition & Representation", "2's Complement Notation",
    "Floating Point Notation", "CPU & Memory Basics", "Compressing Audio & Video",
    "Program Execution & Logic", "Arithmetic & Operators", "Deadlock & Concurrency",
    "Software Classification", "Operating System Concepts", "Network & Internet Classification",
    "Protocols & Layered Approach", "HTML & Web Basics", "XML & Data Formats",
    "Security & Cryptography", "Algorithms & Problem Solving", "Iterative & Recursive Structures",
    "Software Verification & Testing", "Database Systems", "Programming Languages & Paradigms",
    "General Computer Science"
]

def guess_topic(q_text):
    ql = q_text.lower()
    if any(k in ql for k in ["search engine", "google", "query", "crawler", "pagerank"]):
        return "Search Engines"
    if any(k in ql for k in ["abacus", "babbage", "eniac", "cray", "vacuum tube", "ada", "first commercial", "deep blue"]):
        return "Roots of Computing"
    if any(k in ql for k in ["boolean", "and gate", "or gate", "not gate", "xor", "truth table"]):
        return "Boolean Operations"
    if any(k in ql for k in ["hexadecimal", "hex"]):
        return "Hexadecimal Notation"
    if any(k in ql for k in ["2's complement", "two's complement"]):
        return "2's Complement Notation"
    if any(k in ql for k in ["binary", "bit", "byte", "binary addition"]):
        return "Binary Addition & Representation"
    if any(k in ql for k in ["floating point", "mantissa", "exponent", "truncation"]):
        return "Floating Point Notation"
    if any(k in ql for k in ["ram", "rom", "cpu", "register", "alu", "main memory", "mass storage", "dram", "cache"]):
        return "CPU & Memory Basics"
    if any(k in ql for k in ["mp3", "mpeg", "compression", "lossy", "lossless", "audio", "jpeg"]):
        return "Compressing Audio & Video"
    if any(k in ql for k in ["deadlock", "multitasking", "process", "semaphore", "starvation"]):
        return "Deadlock & Concurrency"
    if any(k in ql for k in ["operating system", "os", "kernel", "boot", "gui", "shell", "device driver"]):
        return "Operating System Concepts"
    if any(k in ql for k in ["lan", "wan", "man", "pan", "network", "topology", "bus", "star topology"]):
        return "Network & Internet Classification"
    if any(k in ql for k in ["protocol", "http", "tcp", "udp", "ip address", "dns", "ftp", "smtp", "url"]):
        return "Protocols & Layered Approach"
    if any(k in ql for k in ["html", "css", "web page", "browser", "hyperlink", "tag", "website"]):
        return "HTML & Web Basics"
    if any(k in ql for k in ["xml", "markup"]):
        return "XML & Data Formats"
    if any(k in ql for k in ["virus", "worm", "trojan", "firewall", "encryption", "public key", "private key", "security", "attack"]):
        return "Security & Cryptography"
    if any(k in ql for k in ["algorithm", "flowchart", "pseudocode", "pseudo code", "sorting", "search"]):
        return "Algorithms & Problem Solving"
    if any(k in ql for k in ["loop", "while", "for loop", "recursion", "recursive", "iteration"]):
        return "Iterative & Recursive Structures"
    if any(k in ql for k in ["database", "sql", "relational", "table", "record", "field"]):
        return "Database Systems"
    if any(k in ql for k in ["javascript", "variable", "compiler", "interpreter", "syntax", "function", "java"]):
        return "Programming Languages & Paradigms"
    return "General Computer Science"

def clean_text(s):
    if not s: return ""
    return re.sub(r"\s+", " ", str(s)).strip()

def normalize_key(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s[:120]

def parse_2026():
    path = os.path.join(CS101_DIR, "CS101 Midterm MCQs 2026.pdf")
    if not os.path.exists(path): return []
    txt = subprocess.check_output(["pdftotext", path, "-"]).decode("utf-8", errors="ignore")
    blocks = re.split(r"\n(?=Topic:|\s*Q\d+\.)", txt)
    questions = []
    current_topic = "General Computer Science"
    for b in blocks:
        b = b.strip()
        if b.startswith("Topic:"):
            lines = b.splitlines()
            current_topic = clean_text(lines[0].replace("Topic:", ""))
            b = "\n".join(lines[1:]).strip()
        m = re.search(r"Q\d+\.\s*(.+?)\n\s*A\.\s*(.+?)\n\s*B\.\s*(.+?)\n\s*C\.\s*(.+?)\n\s*D\.\s*(.+?)\n\s*Correct Option:\s*([A-D])\s*(?:\((.*?)\))?", b, re.DOTALL | re.I)
        if m:
            opts = [clean_text(m.group(2)), clean_text(m.group(3)), clean_text(m.group(4)), clean_text(m.group(5))]
            ans_letter = m.group(6).upper()
            idx = ord(ans_letter) - ord("A")
            ans_val = opts[idx] if 0 <= idx < len(opts) else clean_text(m.group(7))
            questions.append({
                "question": clean_text(m.group(1)),
                "options": opts,
                "answer": ans_val,
                "topic": current_topic if current_topic != "General" else guess_topic(m.group(1)),
                "reference": None,
                "source": "CS101 Midterm MCQs 2026"
            })
    return questions

def parse_lecture_wise():
    path = os.path.join(CS101_DIR, "CS101 Midterm Lecture-wise Solved MCQs.pdf")
    if not os.path.exists(path): return []
    txt = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    blocks = re.split(r"\n\s*\d+\s*-\s*", txt)
    questions = []
    for b in blocks[1:]:
        m = re.search(r"(.+?)\n\s*1\.\s*(.+?)\n\s*2\.\s*(.+?)\n\s*3\.\s*(.+?)\n\s*4\.\s*(.+?)\n\s*Correct Choice\s*:\s*(\d)(?:\s*From\s*(Lectuer\s*#?\s*\d+))?", b, re.DOTALL | re.I)
        if m:
            q_text = clean_text(m.group(1))
            opts = [clean_text(m.group(2)), clean_text(m.group(3)), clean_text(m.group(4)), clean_text(m.group(5))]
            c_idx = int(m.group(6)) - 1
            ans_val = opts[c_idx] if 0 <= c_idx < len(opts) else None
            ref = clean_text(m.group(7)) if m.group(7) else None
            questions.append({
                "question": q_text,
                "options": opts,
                "answer": ans_val,
                "topic": guess_topic(q_text),
                "reference": ref,
                "source": "Lecture-wise Solved MCQs"
            })
    return questions

def parse_arslan():
    path = os.path.join(CS101_DIR, "CS101 Midterm Solved MCQs with References by Arslan.pdf")
    if not os.path.exists(path): return []
    txt = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    blocks = re.split(r"\n\s*\d+\.\s*", txt)
    questions = []
    for b in blocks[1:]:
        m = re.search(r"(.+?)\n\s*o\s*(.+?)\n\s*o\s*(.+?)\n\s*o\s*(.+?)\n\s*o\s*(.+?)(?=\n\s*\d+\.|\Z)", b, re.DOTALL)
        if m:
            q_text = clean_text(m.group(1))
            raw_opts = [m.group(2), m.group(3), m.group(4), m.group(5)]
            opts = []
            answer = None
            ref = None
            for ro in raw_opts:
                pg_m = re.search(r"(PG\s*#?\s*\d+)", ro, re.I)
                clean_opt = clean_text(re.sub(r"PG\s*#?\s*\d+.*", "", ro, flags=re.I))
                opts.append(clean_opt)
                if pg_m:
                    answer = clean_opt
                    ref = pg_m.group(1)
            # check explanation trailing
            expl_m = re.search(r"(?:Read Only Memory|http|Reference|Page|\bAccording\b)(.+)", b)
            if expl_m and not ref:
                ref = clean_text(expl_m.group(0))[:100]
            if opts and len(opts) >= 2:
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": answer,
                    "topic": guess_topic(q_text),
                    "reference": ref,
                    "source": "Solved MCQs by Arslan"
                })
    return questions

def parse_xml_bold_file(filename):
    path = os.path.join(CS101_DIR, filename)
    if not os.path.exists(path): return []
    cmd = ["pdftohtml", "-i", "-nodrm", "-xml", "-stdout", path]
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=20)
        raw = proc.stdout.decode("utf-8", errors="replace")
    except Exception:
        return []

    raw = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", raw)
    try:
        root = ET.fromstring(raw)
    except Exception:
        return []

    bold_fonts = set()
    colored_fonts = set()
    for f in root.findall(".//fontspec"):
        fid = f.get("id")
        fam = f.get("family", "").lower()
        col = f.get("color", "").lower()
        if "bold" in fam:
            bold_fonts.add(fid)
        if col and col not in ["#000000", "#666666", "#333333", "#ffffff", "#000", "#fff", ""]:
            colored_fonts.add(fid)

    items = []
    for page in root.findall(".//page"):
        for t in page.findall("text"):
            s = "".join(t.itertext()).strip()
            if not s: continue
            is_bold = t.find("b") is not None or t.get("font") in bold_fonts
            is_col = t.get("font") in colored_fonts
            items.append((s, is_bold or is_col))

    questions = []
    curr_q_lines = []
    curr_opts = []
    correct_opt = None
    curr_ref = ""
    in_q = False

    def flush():
        nonlocal curr_q_lines, curr_opts, correct_opt, curr_ref, in_q
        q_text = clean_text(" ".join(curr_q_lines))
        if q_text and len(curr_opts) >= 2:
            questions.append({
                "question": q_text,
                "options": curr_opts,
                "answer": correct_opt,
                "topic": guess_topic(q_text),
                "reference": curr_ref.strip() if curr_ref else None,
                "source": filename.replace(".pdf", "")
            })
        curr_q_lines = []
        curr_opts = []
        correct_opt = None
        curr_ref = ""
        in_q = False

    for s, is_hi in items:
        if re.search(r"^(?:www\.[a-z0-9\.]+|vustudy|vuhunt|vuhelp|03\d{9}|midterm\s*mcqs|solved\s*by|for\s*more\s*files|whatsapp\b)", s, re.I):
            continue
        if re.search(r"^(?:–\s*)?Please choose one\b", s, re.I):
            continue

        m_ans = re.match(r"^Correct\s*(?:option|answer)\s*[:\.]\s*(.+)$", s, re.I)
        if m_ans:
            ans_val = m_ans.group(1).strip()
            ans_clean = clean_text(re.sub(r"^[a-dA-D][\)\.]\s*", "", ans_val))
            correct_opt = ans_clean
            continue

        if re.match(r"^(?:Page|PG|Ref)\s*#?\s*\d+", s, re.I):
            curr_ref = (curr_ref + " " + s).strip()
            continue

        is_q_start = bool(re.search(r"^(?:Question\s*(?:No)?\s*[:\.]?\s*\d+|Q\s*[:\.]?\s*\d+|\d+[\.\)]\s*[A-Za-z_])", s, re.I))
        if is_q_start:
            flush()
            clean_q = re.sub(r"^(?:Question\s*(?:No)?\s*[:\.]?\s*\d+[\s\:\.\-]*|Q\s*[:\.]?\s*\d+[\s\:\.\-]*|\d+[\.\)]\s*)", "", s, flags=re.I).strip()
            clean_q = re.sub(r"\(?\s*Marks:\s*\d+\s*\)?|\–\s*Please choose one", "", clean_q, flags=re.I).strip()
            in_q = True
            curr_q_lines = [clean_q] if clean_q else []
            continue

        m_opt = re.match(r"^(?:[►•\*\–\-✔]|\(?[a-dA-D][\)\.\:\-]\s*)(.+)$", s)
        if m_opt and in_q:
            opt_str = clean_text(m_opt.group(1))
            if "✔" in s or "" in s or "PG #" in s or "Page #" in s:
                correct_opt = clean_text(re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", opt_str, flags=re.I))
            elif is_hi and not correct_opt:
                correct_opt = opt_str
            clean_opt = clean_text(re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", opt_str, flags=re.I))
            if clean_opt and clean_opt not in curr_opts:
                curr_opts.append(clean_opt)
        elif in_q and not curr_opts:
            if not re.search(r"Marks:\s*\d|Please choose one", s, re.I):
                curr_q_lines.append(s)
        elif curr_opts and not is_q_start:
            if re.search(r"(?:http|page|handout|module)", s, re.I):
                curr_ref = (curr_ref + " " + s).strip()

    flush()
    return questions

def main():
    all_questions = []
    
    # 1. 2026 file (highest quality)
    q_2026 = parse_2026()
    print(f"Parsed 2026 MCQs: {len(q_2026)}")
    all_questions.extend(q_2026)

    # 2. Lecture-wise
    q_lec = parse_lecture_wise()
    print(f"Parsed Lecture-wise MCQs: {len(q_lec)}")
    all_questions.extend(q_lec)

    # 3. Arslan with references
    q_arslan = parse_arslan()
    print(f"Parsed Arslan MCQs: {len(q_arslan)}")
    all_questions.extend(q_arslan)

    # 4. XML-based files with bold/colored answers
    xml_files = [
        "CS101 Midterm 100 Solved MCQs.pdf",
        "CS101 Midterm 300 MCQs.pdf",
        "CS101 Midterm MCQs 2025.pdf",
        "CS101 Midterm MCQs 2024 by Miss Mehwish.pdf",
        "CS101 Midterm Solved MCQs with References by Masoom Fairy.pdf"
    ]
    for xf in xml_files:
        qs = parse_xml_bold_file(xf)
        with_ans = sum(1 for q in qs if q["answer"])
        print(f"Parsed {xf}: {len(qs)} (with answer: {with_ans})")
        all_questions.extend(qs)

    # Deduplication and merging
    deduped = {}
    for q in all_questions:
        q_text = clean_text(q["question"])
        if len(q_text) < 8 or len(q["options"]) < 2:
            continue
        key = normalize_key(q_text)
        
        if key not in deduped:
            deduped[key] = {
                "id": len(deduped) + 1,
                "question": q_text,
                "options": q["options"],
                "answer": q["answer"],
                "topic": q["topic"],
                "reference": q.get("reference"),
                "sources": [q["source"]]
            }
        else:
            existing = deduped[key]
            if q["source"] not in existing["sources"]:
                existing["sources"].append(q["source"])
            # If current has answer and existing doesn't, update it
            if q["answer"] and not existing["answer"]:
                existing["answer"] = q["answer"]
                existing["options"] = q["options"]
            if q.get("reference") and not existing.get("reference"):
                existing["reference"] = q["reference"]
            if existing["topic"] == "General Computer Science" and q["topic"] != "General Computer Science":
                existing["topic"] = q["topic"]

    quiz_list = list(deduped.values())
    # Re-index
    for i, q in enumerate(quiz_list, start=1):
        q["id"] = i

    out_file = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(quiz_list, f, indent=2, ensure_ascii=False)

    ans_count = sum(1 for q in quiz_list if q["answer"])
    print("\n" + "="*50)
    print(f"SUCCESS! Extracted {len(quiz_list)} unique questions ({ans_count} with verified answers)")
    print(f"Saved dataset to {out_file}")

    # Breakdown by topic
    topics_count = {}
    for q in quiz_list:
        t = q["topic"]
        topics_count[t] = topics_count.get(t, 0) + 1
    print("\nBreakdown by Topic:")
    for t, c in sorted(topics_count.items(), key=lambda x: -x[1]):
        print(f"  - {t}: {c} questions")

if __name__ == "__main__":
    main()

