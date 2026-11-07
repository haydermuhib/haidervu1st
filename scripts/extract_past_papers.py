import os, sys, subprocess, re, json, zipfile
import xml.etree.ElementTree as ET

BASE_DIR = "/home/haider/Desktop/Chores"
PAST_PAPERS_DIR = os.path.join(BASE_DIR, "CS101 - Introduction to Computing", "Past Papers & Solved Papers")

def clean_text(s):
    if not s: return ""
    return re.sub(r"\s+", " ", str(s)).strip()

def normalize_key(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s[:120]

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

def extract_from_pdf(path, fname):
    try:
        txt = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    except Exception:
        return []
    if len(txt) < 300:
        return []

    questions = []
    
    # 1. Split by "Question No: X" or "Question X"
    if re.search(r"Question\s*(?:No)?\s*[:\.]?\s*\d+", txt, re.I):
        blocks = re.split(r"(?:Question\s*(?:No)?\s*[:\.]?\s*\d+)", txt, flags=re.I)
        for b in blocks[1:]:
            b_clean = re.sub(r"\(?\s*Marks:\s*\d+\s*\)?|\–\s*Please choose one", "", b, flags=re.I).strip()
            lines = [l.strip() for l in b_clean.splitlines() if l.strip()]
            if not lines: continue
            q_lines = []
            opts = []
            ans = None
            for l in lines:
                is_opt = bool(re.match(r"^[►•\*\–\-✓✔]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔\s]+|\(?[a-dA-D][\)\.\:]\s*", "", l).strip()
                    # Check if marked with checkmark or PG reference
                    if "✓" in l or "✔" in l or "PG #" in l or "Page #" in l:
                        ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", clean_opt, flags=re.I).strip()
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    if not re.search(r"(?:www\.|vustudy|vuhunt|page\s*\d+|session\s*\d+|ref\s*no:|student\s*id:)", l, re.I):
                        q_lines.append(l)
            q_text = clean_text(" ".join(q_lines))
            if len(q_text) > 10 and not re.search(r"^(?:midterm\s*examination|spring\s*20\d\d|fall\s*20\d\d|student\s*info)", q_text, re.I):
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "topic": guess_topic(q_text),
                    "source": fname.replace(".pdf", "")
                })

    # 2. Numbered questions: "1. Statement ..."
    num_blocks = re.split(r"\n\s*\d+[\.\)]\s+", txt)
    if len(num_blocks) > 3:
        for b in num_blocks[1:]:
            lines = [l.strip() for l in b.splitlines() if l.strip()]
            if not lines: continue
            q_lines = []
            opts = []
            ans = None
            for l in lines:
                is_opt = bool(re.match(r"^[►•\*\–\-✓✔]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔\s]+|\(?[a-dA-D][\)\.\:]\s*", "", l).strip()
                    if "✓" in l or "✔" in l or "PG #" in l or "Page #" in l:
                        ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", clean_opt, flags=re.I).strip()
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    if not re.search(r"(?:www\.|vustudy|vuhunt|page\s*\d+|subscribe|knowledge for us|whatsapp)", l, re.I):
                        q_lines.append(l)
            q_text = clean_text(" ".join(q_lines))
            if len(q_text) > 10 and not re.search(r"^(?:midterm\s*examination|spring\s*20\d\d|fall\s*20\d\d|student\s*info)", q_text, re.I):
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "topic": guess_topic(q_text),
                    "source": fname.replace(".pdf", "")
                })

    return questions

def extract_from_docx(path, fname):
    try:
        with zipfile.ZipFile(path) as z:
            tree = ET.fromstring(z.read("word/document.xml"))
            tag_t = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"
            tag_p = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"
            tag_r = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r"
            
            questions = []
            curr_q_lines = []
            curr_opts = []
            in_q = False

            for p in tree.iter(tag_p):
                p_text = clean_text("".join(node.text for node in p.iter(tag_t) if node.text))
                if not p_text: continue

                m_start = re.match(r"^(?:Question\s*(?:No)?\s*[:\.]?\s*\d+|\d+[\.\)]\s+)(.+)$", p_text, re.I)
                if m_start:
                    if curr_q_lines:
                        q_t = clean_text(" ".join(curr_q_lines))
                        if len(q_t) > 10:
                            questions.append({
                                "question": q_t,
                                "options": curr_opts,
                                "answer": None,
                                "topic": guess_topic(q_t),
                                "source": fname.replace(".docx", "")
                            })
                    curr_q_lines = [m_start.group(1)]
                    curr_opts = []
                    in_q = True
                    continue

                m_opt = re.match(r"^(?:[►•\*\–\-✓✔]|\(?[a-dA-D][\)\.\:]\s*)(.+)$", p_text)
                if m_opt and in_q:
                    curr_opts.append(clean_text(m_opt.group(1)))
                elif in_q and not curr_opts:
                    if not re.search(r"(?:subscribe|youtube|knowledge for us|page\s*\d+)", p_text, re.I):
                        curr_q_lines.append(p_text)

            if curr_q_lines:
                q_t = clean_text(" ".join(curr_q_lines))
                if len(q_t) > 10:
                    questions.append({
                        "question": q_t,
                        "options": curr_opts,
                        "answer": None,
                        "topic": guess_topic(q_t),
                        "source": fname.replace(".docx", "")
                    })
            return questions
    except Exception:
        return []

def main():
    # Load existing question bank
    existing_file = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
    with open(existing_file, "r", encoding="utf-8") as f:
        existing_list = json.load(f)

    print(f"Loaded existing question bank: {len(existing_list)} items")
    deduped = {}
    for q in existing_list:
        key = normalize_key(q["question"])
        deduped[key] = q

    # Extract from Past Papers & Solved Papers
    past_files = sorted(os.listdir(PAST_PAPERS_DIR))
    total_found = 0
    new_added = 0

    for f in past_files:
        path = os.path.join(PAST_PAPERS_DIR, f)
        qs = []
        if f.endswith(".pdf"):
            qs = extract_from_pdf(path, f)
        elif f.endswith(".docx"):
            qs = extract_from_docx(path, f)

        if qs:
            total_found += len(qs)
            for q in qs:
                q_text = clean_text(q["question"])
                if len(q_text) < 10:
                    continue
                key = normalize_key(q_text)
                if key not in deduped:
                    new_item = {
                        "id": len(deduped) + 1,
                        "question": q_text,
                        "options": q["options"],
                        "answer": q.get("answer"),
                        "topic": q["topic"],
                        "reference": q.get("reference") or f"From {q['source']}",
                        "sources": [q["source"]]
                    }
                    deduped[key] = new_item
                    new_added += 1
                else:
                    existing = deduped[key]
                    if q["source"] not in existing["sources"]:
                        existing["sources"].append(q["source"])
                    if q.get("answer") and not existing.get("answer"):
                        existing["answer"] = q["answer"]
                    if not existing.get("options") and q.get("options"):
                        existing["options"] = q["options"]

    updated_list = list(deduped.values())
    for i, q in enumerate(updated_list, start=1):
        q["id"] = i

    # Save updated json
    with open(existing_file, "w", encoding="utf-8") as f:
        json.dump(updated_list, f, indent=2, ensure_ascii=False)

    # Save quiz_data.js
    js_file = os.path.join(BASE_DIR, "quiz_data.js")
    with open(js_file, "w", encoding="utf-8") as f:
        f.write("window.CS101_QUESTIONS = " + json.dumps(updated_list, ensure_ascii=False) + ";\n")

    print("\n" + "="*50)
    print(f"Total raw items found in Past Papers: {total_found}")
    print(f"Net new unique questions/MCQs added: {new_added}")
    print(f"Grand Total Questions in Bank: {len(updated_list)}")
    print(f"Verified Answered: {sum(1 for q in updated_list if q.get('answer'))}")
    print(f"Updated {existing_file} and {js_file}")

if __name__ == "__main__":
    main()

