import os, sys, subprocess, re, json, glob, time
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = "/home/haider/Desktop/Chores"
PAST_PAPERS_DIR = os.path.join(BASE_DIR, "CS101 - Introduction to Computing", "Past Papers & Solved Papers")
TEMP_UNPACKED_DIR = os.path.join(BASE_DIR, "temp_unpacked")
MASTER_JSON = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
QUIZ_DATA_JS = os.path.join(BASE_DIR, "quiz_data.js")

def clean_text(s):
    if not s: return ""
    return re.sub(r"\s+", " ", str(s)).strip()

def normalize_key(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s[:120]

def guess_topic(q_text):
    ql = q_text.lower()
    if any(k in ql for k in ["search engine", "google", "query", "crawler", "pagerank", "spider"]):
        return "Search Engines"
    if any(k in ql for k in ["abacus", "babbage", "eniac", "cray", "vacuum tube", "ada", "first commercial", "deep blue", "turing", "ada lovelace", "punch card", "von neumann"]):
        return "Roots of Computing"
    if any(k in ql for k in ["boolean", "and gate", "or gate", "not gate", "xor", "truth table", "flip-flop"]):
        return "Boolean Operations"
    if any(k in ql for k in ["hexadecimal", "hex"]):
        return "Hexadecimal Notation"
    if any(k in ql for k in ["2's complement", "two's complement"]):
        return "2's Complement Notation"
    if any(k in ql for k in ["binary", "bit", "byte", "binary addition", "excess notation"]):
        return "Binary Addition & Representation"
    if any(k in ql for k in ["floating point", "mantissa", "exponent", "truncation"]):
        return "Floating Point Notation"
    if any(k in ql for k in ["ram", "rom", "cpu", "register", "alu", "main memory", "mass storage", "dram", "cache", "bus", "machine cycle", "program counter", "instruction register"]):
        return "CPU & Memory Basics"
    if any(k in ql for k in ["mp3", "mpeg", "compression", "lossy", "lossless", "audio", "jpeg", "bitmap", "pixel", "dithering", "rgb"]):
        return "Compressing Audio & Video"
    if any(k in ql for k in ["deadlock", "multitasking", "process", "semaphore", "starvation", "multiprogramming", "time sharing", "time-sharing"]):
        return "Deadlock & Concurrency"
    if any(k in ql for k in ["operating system", "os", "kernel", "boot", "gui", "shell", "device driver", "file manager", "memory manager"]):
        return "Operating System Concepts"
    if any(k in ql for k in ["lan", "wan", "man", "pan", "network", "topology", "star topology", "bus topology", "ring topology", "ethernet", "wifi"]):
        return "Network & Internet Classification"
    if any(k in ql for k in ["protocol", "http", "tcp", "udp", "ip address", "dns", "ftp", "smtp", "url", "packet", "router", "gateway"]):
        return "Protocols & Layered Approach"
    if any(k in ql for k in ["html", "css", "web page", "browser", "hyperlink", "tag", "website", "<p>", "href", "<input", "form"]):
        return "HTML & Web Basics"
    if any(k in ql for k in ["xml", "markup"]):
        return "XML & Data Formats"
    if any(k in ql for k in ["virus", "worm", "trojan", "firewall", "encryption", "public key", "private key", "security", "attack", "malware"]):
        return "Security & Cryptography"
    if any(k in ql for k in ["algorithm", "flowchart", "pseudocode", "pseudo code", "sorting", "search", "binary search", "sequential search", "bubble sort", "insertion sort"]):
        return "Algorithms & Problem Solving"
    if any(k in ql for k in ["loop", "while", "for loop", "recursion", "recursive", "iteration"]):
        return "Iterative & Recursive Structures"
    if any(k in ql for k in ["database", "sql", "relational", "table", "record", "field", "dbms", "primary key", "query language"]):
        return "Database Systems"
    if any(k in ql for k in ["javascript", "variable", "compiler", "interpreter", "syntax", "function", "java", "scripting", "server side", "client side", "event"]):
        return "Programming Languages & Paradigms"
    return "General Computer Science"

def ocr_page(args):
    pdf, page, prefix = args
    png_base = f"{prefix}_{page}_p"
    subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", str(page), "-l", str(page), pdf, png_base],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pfiles = glob.glob(f"{png_base}*.png")
    if not pfiles: return ""
    txt_prefix = f"{prefix}_{page}_txt"
    subprocess.run(["tesseract", pfiles[0], txt_prefix], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    txt_file = f"{txt_prefix}.txt"
    res = ""
    if os.path.exists(txt_file):
        try:
            with open(txt_file, "r", encoding="utf-8", errors="ignore") as f:
                res = f.read()
        except: pass
    for p in pfiles:
        try: os.remove(p)
        except: pass
    try: os.remove(txt_file)
    except: pass
    return res

def parse_ocr_page_text(page_txt, source_name):
    questions = []
    
    # Check for VU LMS quiz question pattern
    # Pattern: Question # X of Y ( Start time: ... ) \n [Question text] \n Select the correct option \n [Options]
    if "Select the correct option" in page_txt or "Select correct option" in page_txt:
        parts = re.split(r"Select (?:the )?correct option\s*:?", page_txt, flags=re.I)
        top = parts[0]
        bottom = parts[1] if len(parts) > 1 else ""

        # Extract question prompt from top
        q_clean = re.sub(r"^[\s\S]*?Question\s*#?\s*\d+\s*of\s*\d+[^\n]*\n", "", top, flags=re.I).strip()
        q_clean = clean_text(q_clean)
        
        # Parse options from bottom
        opts_raw = [l.strip() for l in bottom.splitlines() if l.strip()]
        radio_chars = {"o", "e", "c", "0", "v", "©", "•", "●", "el", "es", "fe"}
        opts = []
        ans = None
        for l in opts_raw:
            if re.search(r"(?:team hadi|waqar siddhu|genrica|youtube|facebook|warning:|best of luck)", l, re.I):
                continue
            if l.lower() in radio_chars:
                if l.lower() in {"e", "•", "●"} and opts:
                    ans = opts[-1] # mark last option as selected
                continue
            clean_l = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", l).strip()
            if len(clean_l) > 1:
                opts.append(clean_l)

        if len(q_clean) > 8 and not re.search(r"^(?:virtual university|we deal all kind|mid term|past paper)", q_clean, re.I):
            questions.append({
                "question": q_clean,
                "options": opts,
                "answer": ans,
                "topic": guess_topic(q_clean),
                "source": source_name
            })
    else:
        # Generic split on Question # or Q1, Q2, etc.
        q_splits = re.split(r"\n\s*(?:Question\s*#?\s*\d+|Q\s*\d+[\.\:]\s*)", page_txt, flags=re.I)
        if len(q_splits) > 1:
            for qs in q_splits[1:]:
                lines = [l.strip() for l in qs.splitlines() if l.strip()]
                if not lines: continue
                q_text = clean_text(lines[0])
                if len(q_text) > 10 and not re.search(r"^(?:virtual university|we deal all kind|mid term|past paper)", q_text, re.I):
                    opts = [clean_text(l) for l in lines[1:] if len(l) > 1 and not re.search(r"(?:team hadi|genrica|youtube|facebook)", l, re.I)]
                    questions.append({
                        "question": q_text,
                        "options": opts[:4] if len(opts) >= 2 else [],
                        "answer": None,
                        "solution_notes": clean_text(" ".join(lines[1:])) if len(opts) < 2 else None,
                        "topic": guess_topic(q_text),
                        "source": source_name
                    })

    return questions

def process_scanned_pdf(path, source_name):
    try:
        out = subprocess.check_output(["pdfinfo", path]).decode("utf-8", errors="ignore")
        num_pages = 0
        for l in out.splitlines():
            if l.startswith("Pages:"):
                num_pages = int(l.split(":")[1].strip())
                break
        if num_pages == 0: return []
    except Exception:
        return []

    print(f"  [OCR SCANNING] {os.path.basename(path)} ({num_pages} pages)...")
    tasks = [(path, p, f"/tmp/deep_ocr_{os.path.basename(path)[:8]}") for p in range(1, num_pages + 1)]
    with ThreadPoolExecutor(max_workers=8) as ex:
        page_texts = list(ex.map(ocr_page, tasks))

    all_qs = []
    for pt in page_texts:
        qs = parse_ocr_page_text(pt, source_name)
        all_qs.extend(qs)

    print(f"    -> Extracted {len(all_qs)} questions from {os.path.basename(path)}")
    return all_qs

def main():
    print("=" * 60)
    print("SCANNING ALL IMAGE-BASED EXAM PAPERS WITH OCR")
    print("=" * 60)

    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        master_list = json.load(f)

    print(f"Starting master bank: {len(master_list)} questions")
    deduped = {}
    for q in master_list:
        key = normalize_key(q["question"])
        if key:
            deduped[key] = q

    # Target scanned files
    scanned_files = []
    for i in range(1, 16):
        p = os.path.join(PAST_PAPERS_DIR, f"CS101 Midterm File {i}.pdf")
        if os.path.exists(p):
            scanned_files.append((p, f"CS101 Midterm File {i}"))

    # Also Waqar Siddhu files
    wq_files = [
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm Solved Paper 1 by Waqar Siddhu.pdf"), "CS101 Midterm Solved Paper 1 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 1.pdf"), "CS101 - 1 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 2.pdf"), "CS101 - 2 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 3.pdf"), "CS101 - 3 by Waqar Siddhu"),
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm 2022.pdf"), "CS101 Midterm 2022 Handwritten"),
    ]
    for p, name in wq_files:
        if os.path.exists(p):
            scanned_files.append((p, name))

    print(f"Total scanned files to process: {len(scanned_files)}")

    total_found = 0
    new_added = 0
    t_start = time.time()

    for path, src in scanned_files:
        qs = process_scanned_pdf(path, src)
        total_found += len(qs)
        for q in qs:
            q_text = clean_text(q["question"])
            if len(q_text) < 10: continue
            key = normalize_key(q_text)
            if not key: continue

            if key not in deduped:
                new_item = {
                    "id": len(deduped) + 1,
                    "question": q_text,
                    "options": q.get("options") or [],
                    "answer": q.get("answer"),
                    "solution_notes": q.get("solution_notes"),
                    "topic": q["topic"],
                    "reference": f"From {q['source']} (Scanned Real Exam Paper)",
                    "sources": [q["source"]]
                }
                deduped[key] = new_item
                new_added += 1
            else:
                existing = deduped[key]
                if q["source"] not in existing.setdefault("sources", []):
                    existing["sources"].append(q["source"])
                if q.get("answer") and not existing.get("answer"):
                    existing["answer"] = q["answer"]
                if not existing.get("options") and q.get("options"):
                    existing["options"] = q["options"]
                if not existing.get("solution_notes") and q.get("solution_notes"):
                    existing["solution_notes"] = q.get("solution_notes")

    # Re-index
    updated_list = list(deduped.values())
    for idx, q in enumerate(updated_list, start=1):
        q["id"] = idx

    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(updated_list, f, indent=2, ensure_ascii=False)

    with open(QUIZ_DATA_JS, "w", encoding="utf-8") as f:
        f.write("window.CS101_QUESTIONS = " + json.dumps(updated_list, ensure_ascii=False) + ";\n")

    t_total = time.time() - t_start
    print("\n" + "=" * 60)
    print("OCR SCANNING & MERGE COMPLETE")
    print("=" * 60)
    print(f"Time taken: {t_total:.1f}s")
    print(f"Total raw items found in scanned files: {total_found}")
    print(f"Net new questions added to bank: {new_added}")
    print(f"Final Total Question Bank Size: {len(updated_list)}")
    print(f"Questions with verified answer: {sum(1 for q in updated_list if q.get('answer'))}")
    print(f"Questions with options: {sum(1 for q in updated_list if q.get('options'))}")
    print(f"Master files updated:\n  -> {MASTER_JSON}\n  -> {QUIZ_DATA_JS}")

if __name__ == "__main__":
    main()

