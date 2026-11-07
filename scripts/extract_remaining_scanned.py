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
    if any(k in ql for k in ["search engine", "google", "query", "crawler", "pagerank"]): return "Search Engines"
    if any(k in ql for k in ["abacus", "babbage", "eniac", "cray", "vacuum tube", "ada", "first commercial"]): return "Roots of Computing"
    if any(k in ql for k in ["boolean", "and gate", "or gate", "not gate", "xor", "truth table"]): return "Boolean Operations"
    if any(k in ql for k in ["hexadecimal", "hex"]): return "Hexadecimal Notation"
    if any(k in ql for k in ["2's complement", "two's complement"]): return "2's Complement Notation"
    if any(k in ql for k in ["binary", "bit", "byte", "binary addition", "excess notation"]): return "Binary Addition & Representation"
    if any(k in ql for k in ["floating point", "mantissa", "exponent", "truncation"]): return "Floating Point Notation"
    if any(k in ql for k in ["ram", "rom", "cpu", "register", "alu", "main memory", "mass storage", "dram", "cache", "bus", "driver"]): return "CPU & Memory Basics"
    if any(k in ql for k in ["mp3", "mpeg", "compression", "lossy", "lossless", "audio", "jpeg"]): return "Compressing Audio & Video"
    if any(k in ql for k in ["deadlock", "multitasking", "process", "semaphore", "starvation"]): return "Deadlock & Concurrency"
    if any(k in ql for k in ["operating system", "os", "kernel", "boot", "gui", "shell", "device driver"]): return "Operating System Concepts"
    if any(k in ql for k in ["lan", "wan", "man", "pan", "network", "topology", "star", "bus topology"]): return "Network & Internet Classification"
    if any(k in ql for k in ["protocol", "http", "tcp", "udp", "ip address", "dns", "ftp", "smtp", "url"]): return "Protocols & Layered Approach"
    if any(k in ql for k in ["html", "css", "web page", "browser", "hyperlink", "tag"]): return "HTML & Web Basics"
    if any(k in ql for k in ["xml", "markup"]): return "XML & Data Formats"
    if any(k in ql for k in ["virus", "worm", "trojan", "firewall", "encryption", "security"]): return "Security & Cryptography"
    if any(k in ql for k in ["algorithm", "flowchart", "pseudocode", "sorting", "search"]): return "Algorithms & Problem Solving"
    if any(k in ql for k in ["loop", "while", "for loop", "recursion", "recursive"]): return "Iterative & Recursive Structures"
    if any(k in ql for k in ["database", "sql", "relational", "table", "record"]): return "Database Systems"
    if any(k in ql for k in ["javascript", "variable", "compiler", "interpreter", "syntax", "function", "cgi"]): return "Programming Languages & Paradigms"
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

def parse_special_ocr(page_txt, src_name):
    # 1. Hadi Midterm Files 4, 5, 6:
    if "Answer ( Please select your correct option )" in page_txt or "Please select your correct option" in page_txt:
        parts = re.split(r"Answer\s*\(\s*Please select your correct option\s*\)", page_txt, flags=re.I)
        top = parts[0]
        bottom = parts[1] if len(parts) > 1 else ""
        q_raw = re.sub(r"^[\s\S]*?Question No\s*:\s*\d+\s*of\s*\d+[^\n]*\n", "", top, flags=re.I).strip()
        q_clean = clean_text(q_raw)
        
        opts = []
        ans = None
        for l in bottom.splitlines():
            ls = l.strip()
            if not ls or re.search(r"(?:email|whatsapp|hadirajput|warning|best of luck)", ls, re.I):
                continue
            if re.match(r"^[a-d0-9\(\)\[\]\.\:\s]+$", ls) and len(ls) < 4:
                continue
            if "CORRECT ANSWER" in ls:
                opt_str = re.sub(r"[\s\d\–\-]*CORRECT ANSWER.*", "", ls, flags=re.I).strip()
                if opt_str and len(opt_str) > 1:
                    ans = opt_str
                    opts.append(opt_str)
                elif opts:
                    ans = opts[-1]
            else:
                clean_l = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", ls).strip()
                if len(clean_l) > 1:
                    opts.append(clean_l)
        if len(q_clean) > 8:
            return [{
                "question": q_clean,
                "options": opts,
                "answer": ans,
                "topic": guess_topic(q_clean),
                "source": src_name
            }]

    # 2. Waqar Siddhu format:
    if "genrica" in page_txt.lower() or "waqar siddhu" in page_txt.lower():
        lines = [l.strip() for l in page_txt.splitlines() if l.strip()]
        valid_lines = []
        for l in lines:
            if re.search(r"(?:genrica|youtube|virtualuniversitypakistan|waqar|page\s*\d+)", l, re.I):
                continue
            if re.match(r"^[a-z0-9\(\)\[\]\.\:\s]+$", l) and len(l) < 4:
                continue
            valid_lines.append(l)
        if len(valid_lines) >= 2:
            q_line = valid_lines[0]
            opts = valid_lines[1:]
            if len(q_line) > 8:
                return [{
                    "question": q_line,
                    "options": opts[:4] if len(opts) >= 2 else [],
                    "answer": None,
                    "topic": guess_topic(q_line),
                    "source": src_name
                }]

    # 3. Handwritten questions (2022 exam sheet):
    if "CamScanner" in page_txt or "Q1" in page_txt:
        lines = page_txt.splitlines()
        found = []
        for l in lines:
            ls = l.strip()
            m = re.match(r"^(?:Q\s*\d+|Question\s*\d+)[\.\:\)]\s*(.+)$", ls, re.I)
            if m:
                q_t = clean_text(m.group(1))
                if len(q_t) > 10:
                    found.append({
                        "question": q_t,
                        "options": [],
                        "answer": None,
                        "topic": guess_topic(q_t),
                        "source": src_name
                    })
        if found: return found

    return []

def main():
    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        master_list = json.load(f)

    deduped = {normalize_key(q["question"]): q for q in master_list if normalize_key(q["question"])}
    
    target_files = [
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm File 4.pdf"), "CS101 Midterm File 4"),
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm File 5.pdf"), "CS101 Midterm File 5"),
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm File 6.pdf"), "CS101 Midterm File 6"),
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm Solved Paper 1 by Waqar Siddhu.pdf"), "CS101 Midterm Solved Paper 1 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 1.pdf"), "CS101 - 1 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 2.pdf"), "CS101 - 2 by Waqar Siddhu"),
        (os.path.join(TEMP_UNPACKED_DIR, "CS101 midterm solved by waqar", "CS101 - 3.pdf"), "CS101 - 3 by Waqar Siddhu"),
        (os.path.join(PAST_PAPERS_DIR, "CS101 Midterm 2022.pdf"), "CS101 Midterm 2022 Handwritten"),
    ]

    total_new = 0
    for path, src in target_files:
        if not os.path.exists(path): continue
        out = subprocess.check_output(["pdfinfo", path]).decode("utf-8", errors="ignore")
        num_pages = int(re.search(r"Pages:\s*(\d+)", out).group(1))
        tasks = [(path, p, f"/tmp/spec_ocr_{os.path.basename(path)[:8]}") for p in range(1, num_pages + 1)]
        with ThreadPoolExecutor(max_workers=8) as ex:
            page_texts = list(ex.map(ocr_page, tasks))

        file_added = 0
        for pt in page_texts:
            qs = parse_special_ocr(pt, src)
            for q in qs:
                key = normalize_key(q["question"])
                if not key: continue
                if key not in deduped:
                    new_item = {
                        "id": len(deduped) + 1,
                        "question": q["question"],
                        "options": q.get("options") or [],
                        "answer": q.get("answer"),
                        "solution_notes": q.get("solution_notes"),
                        "topic": q["topic"],
                        "reference": f"From {q['source']} (Scanned Exam Paper)",
                        "sources": [q["source"]]
                    }
                    deduped[key] = new_item
                    total_new += 1
                    file_added += 1
                else:
                    existing = deduped[key]
                    if q["source"] not in existing.setdefault("sources", []):
                        existing["sources"].append(q["source"])
                    if q.get("answer") and not existing.get("answer"):
                        existing["answer"] = q["answer"]
                    if not existing.get("options") and q.get("options"):
                        existing["options"] = q["options"]
        print(f"Processed {os.path.basename(path)} -> {file_added} new questions added")

    final_list = list(deduped.values())
    for idx, q in enumerate(final_list, start=1):
        q["id"] = idx

    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)

    with open(QUIZ_DATA_JS, "w", encoding="utf-8") as f:
        f.write("window.CS101_QUESTIONS = " + json.dumps(final_list, ensure_ascii=False) + ";\n")

    print(f"\nFinal Bank Count: {len(final_list)} (Added {total_new} new items)")

if __name__ == "__main__":
    main()

