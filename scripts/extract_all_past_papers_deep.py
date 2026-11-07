import os, sys, subprocess, re, json, glob, time
import xml.etree.ElementTree as ET
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

def parse_text_stream(txt, source_name):
    questions = []
    
    # Pre-clean known watermarks/headers
    lines = txt.splitlines()
    clean_lines = []
    skip_pats = [
        r"^(?:www\.|https?:\/\/)",
        r"(?:vustudy|vuhunt|vuaskari|virtualinspire|vuinsider|vupages|vutube)",
        r"(?:subscribe|youtube|knowledge for us|whatsapp|best of luck)",
        r"(?:mid\s*term\s*examination|spring\s*20\d\d|fall\s*20\d\d|semester\s*fall|semester\s*spring)",
        r"(?:student\s*id|ref\s*no:|session\s*[-–:]\s*\d+|page\s*\d+\s*of\s*\d+)",
        r"^\s*page\s*\d+\s*$",
        r"^(?:for more papers|made and solved by|all students reading|we deal all kind)"
    ]
    skip_re = re.compile("|".join(skip_pats), re.I)

    for l in lines:
        ls = l.strip()
        if not ls:
            clean_lines.append("")
            continue
        if skip_re.search(ls) and len(ls) < 80:
            continue
        clean_lines.append(ls)

    full_clean = "\n".join(clean_lines)

    # 1. Blocks by "Question No: X" or "Question # X of Y" or "Question X"
    if re.search(r"Question\s*(?:#|No)?\s*[:\.]?\s*\d+", full_clean, re.I):
        blocks = re.split(r"(?:Question\s*(?:#|No)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?(?:\s*\([^)]*\))?)", full_clean, flags=re.I)
        for b in blocks[1:]:
            b_clean = re.sub(r"\(?\s*Marks:\s*\d+\s*\)?|\–\s*Please choose one|Select\s+(?:the\s+)?correct\s+option\s*:?", "", b, flags=re.I).strip()
            blines = [l.strip() for l in b_clean.splitlines() if l.strip()]
            if not blines: continue
            
            q_lines = []
            opts = []
            ans = None
            notes = []
            
            for l in blines:
                is_opt = bool(re.match(r"^[►•\*\–\-✓✔○●O\x0c]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", l).strip()
                    if "✓" in l or "✔" in l or "PG #" in l or "Page #" in l or "(correct)" in l.lower() or "right answer" in l.lower():
                        ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    q_lines.append(l)
                else:
                    # lines after options could be solution notes/explanations
                    notes.append(l)
            
            q_text = clean_text(" ".join(q_lines))
            if len(q_text) > 8 and not re.search(r"^(?:midterm\s*examination|spring\s*20\d\d|fall\s*20\d\d|student\s*info|rules\s*and|guidelines)", q_text, re.I):
                sol_notes = clean_text(" ".join(notes)) if notes else None
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": sol_notes,
                    "topic": guess_topic(q_text),
                    "source": source_name
                })

    # 2. Numbered questions: "1. Statement ..." or "1) Statement ..."
    num_blocks = re.split(r"\n\s*\d+[\.\)]\s+", full_clean)
    if len(num_blocks) > 3:
        for b in num_blocks[1:]:
            blines = [l.strip() for l in b.splitlines() if l.strip()]
            if not blines: continue
            q_lines = []
            opts = []
            ans = None
            notes = []
            for l in blines:
                is_opt = bool(re.match(r"^[►•\*\–\-✓✔○●Oe]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", l).strip()
                    if "✓" in l or "✔" in l or "PG #" in l or "Page #" in l or "(correct)" in l.lower() or "right answer" in l.lower():
                        ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    q_lines.append(l)
                else:
                    notes.append(l)
            q_text = clean_text(" ".join(q_lines))
            if len(q_text) > 8 and not re.search(r"^(?:midterm\s*examination|spring\s*20\d\d|fall\s*20\d\d|student\s*info|session\s*\d+)", q_text, re.I):
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": clean_text(" ".join(notes)) if notes else None,
                    "topic": guess_topic(q_text),
                    "source": source_name
                })

    # 3. Arrow-delimited blocks (VirtualInspire / VUAskari / VUInsider format where questions are not numbered)
    # Pattern: Question line(s) ending with '?' or '____' or colon, followed by 2 to 4 '►' options
    arrow_chunks = re.split(r"(?<=\n)(?=[^►\n]+?\n\s*►)", full_clean)
    if len(arrow_chunks) > 3:
        for ch in arrow_chunks:
            ch_lines = [l.strip() for l in ch.splitlines() if l.strip()]
            if not ch_lines: continue
            q_part = []
            opt_part = []
            ans = None
            for l in ch_lines:
                if l.startswith("►") or l.startswith("•"):
                    clean_opt = re.sub(r"^[►•\s]+", "", l).strip()
                    if "✓" in l or "✔" in l or "PG #" in l or "Page #" in l or "(correct)" in l.lower():
                        ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*", "", clean_opt, flags=re.I).strip()
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*", "", clean_opt, flags=re.I).strip()
                    if clean_opt:
                        opt_part.append(clean_opt)
                elif not opt_part:
                    if not re.search(r"^(?:Question No:|Please choose one|\( Marks: \d+ \))", l, re.I):
                        q_part.append(l)
            q_text = clean_text(" ".join(q_part))
            if len(q_text) > 8 and len(opt_part) >= 2:
                questions.append({
                    "question": q_text,
                    "options": opt_part,
                    "answer": ans,
                    "solution_notes": None,
                    "topic": guess_topic(q_text),
                    "source": source_name
                })

    # 4. Bullet / Q&A format (Attiq Kundi Jun 2022 format: " Question" followed by answer line or options)
    bullet_items = re.split(r"(?<=\n)(?=[o•]\s+)", full_clean)
    if len(bullet_items) > 5:
        for it in bullet_items:
            it_lines = [l.strip() for l in it.splitlines() if l.strip()]
            if not it_lines: continue
            q_line = re.sub(r"^[o•\s]+", "", it_lines[0]).strip()
            rest = it_lines[1:]
            if len(q_line) > 10:
                opts = []
                ans = None
                for r in rest:
                    clean_r = re.sub(r"^[o•\-\*\s]+", "", r).strip()
                    if clean_r:
                        opts.append(clean_r)
                if opts:
                    ans = opts[0] if len(opts) == 1 else None
                questions.append({
                    "question": q_line,
                    "options": opts if len(opts) > 1 else [],
                    "answer": ans,
                    "solution_notes": f"Correct Answer: {ans}" if (ans and not opts[1:]) else None,
                    "topic": guess_topic(q_line),
                    "source": source_name
                })

    return questions

def extract_from_pdf(path, source_name):
    try:
        txt = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    except Exception:
        return []
    if len(txt) < 100:
        return []
    return parse_text_stream(txt, source_name)

def extract_from_docx(path, source_name):
    try:
        with zipfile.ZipFile(path) as z:
            tree = ET.fromstring(z.read("word/document.xml"))
            tag_t = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"
            tag_p = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"
            
            p_texts = []
            for p in tree.iter(tag_p):
                t = clean_text("".join(node.text for node in p.iter(tag_t) if node.text))
                if t: p_texts.append(t)
            full_txt = "\n".join(p_texts)
            return parse_text_stream(full_txt, source_name)
    except Exception:
        return []

def extract_from_doc(path, source_name):
    try:
        res = subprocess.run(["antiword", path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if res.returncode == 0 and len(res.stdout) > 50:
            txt = res.stdout.decode("utf-8", errors="ignore")
            return parse_text_stream(txt, source_name)
    except Exception:
        pass
    return []

def ocr_single_page(args):
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

def extract_scanned_pdf(path, source_name, max_pages=None):
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

    if max_pages and num_pages > max_pages:
        num_pages = max_pages

    tasks = [(path, p, f"/tmp/ocr_{os.path.basename(path)[:10]}") for p in range(1, num_pages + 1)]
    with ThreadPoolExecutor(max_workers=8) as ex:
        page_texts = list(ex.map(ocr_single_page, tasks))

    full_txt = "\n\n--- PAGE BREAK ---\n\n".join(page_texts)
    return parse_text_stream(full_txt, source_name)

def main():
    print("=" * 60)
    print("STARTING DEEP PAST PAPERS EXTRACTION ENGINE")
    print("=" * 60)

    # 1. Load existing question bank
    existing_list = []
    if os.path.exists(MASTER_JSON):
        with open(MASTER_JSON, "r", encoding="utf-8") as f:
            existing_list = json.load(f)
    print(f"Loaded existing question bank: {len(existing_list)} items")

    deduped = {}
    for q in existing_list:
        key = normalize_key(q["question"])
        if key:
            deduped[key] = q

    # 2. Collect all files across Past Papers directory and temp_unpacked
    all_files = []
    
    # Root Past Papers directory
    for f in sorted(os.listdir(PAST_PAPERS_DIR)):
        all_files.append((os.path.join(PAST_PAPERS_DIR, f), f))

    # temp_unpacked directory
    if os.path.exists(TEMP_UNPACKED_DIR):
        for root, dirs, files in os.walk(TEMP_UNPACKED_DIR):
            for f in files:
                all_files.append((os.path.join(root, f), f))

    print(f"Total candidate files gathered across all archives & folders: {len(all_files)}")

    # We will identify scanned PDFs vs text PDFs
    text_files = []
    scanned_files = []

    for path, fname in all_files:
        if fname.endswith(".zip") or fname.endswith(".rar"):
            continue # already unpacked
        if fname.endswith(".pdf"):
            # Check length of pdftotext
            try:
                txt = subprocess.check_output(["pdftotext", path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
                if len(txt) > 300:
                    text_files.append((path, fname))
                else:
                    # Scanned PDF
                    scanned_files.append((path, fname))
            except:
                scanned_files.append((path, fname))
        elif fname.endswith(".docx"):
            text_files.append((path, fname))
        elif fname.endswith(".doc"):
            text_files.append((path, fname))

    print(f"Classified: {len(text_files)} text-extractable documents, {len(scanned_files)} scanned image PDFs")

    total_extracted_raw = 0
    new_questions_added = 0

    # 3. Process Text Files
    print("\n--- Processing Text Documents ---")
    for path, fname in text_files:
        src = fname.rsplit(".", 1)[0]
        qs = []
        if fname.endswith(".pdf"):
            qs = extract_from_pdf(path, src)
        elif fname.endswith(".docx"):
            qs = extract_from_docx(path, src)
        elif fname.endswith(".doc"):
            qs = extract_from_doc(path, src)

        if qs:
            total_extracted_raw += len(qs)
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
                        "reference": f"From {q['source']}",
                        "sources": [q["source"]]
                    }
                    deduped[key] = new_item
                    new_questions_added += 1
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

            print(f"  [TEXT] {fname:50s} -> {len(qs):4d} items parsed")

    # 4. Process Scanned Image PDFs
    # Notice: CS101 Midterm Solved File 1..11 by Team Hadi are duplicates of CS101 Midterm File 1..11.
    # To avoid duplicate OCR work, we filter out exact name duplicates.
    unique_scanned = []
    seen_scanned_names = set()
    for path, fname in scanned_files:
        norm_name = re.sub(r"\s+", " ", fname).strip().lower()
        if "team hadi" in norm_name:
            continue # Subsumed by CS101 Midterm File 1..11
        if norm_name not in seen_scanned_names:
            seen_scanned_names.add(norm_name)
            unique_scanned.append((path, fname))

    print(f"\n--- Processing {len(unique_scanned)} Scanned Image PDFs with Multi-threaded OCR ---")
    for path, fname in unique_scanned:
        src = fname.rsplit(".", 1)[0]
        t0 = time.time()
        qs = extract_scanned_pdf(path, src)
        dur = time.time() - t0
        if qs:
            total_extracted_raw += len(qs)
            file_new = 0
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
                        "reference": f"From {q['source']} (Scanned Exam Paper)",
                        "sources": [q["source"]]
                    }
                    deduped[key] = new_item
                    new_questions_added += 1
                    file_new += 1
                else:
                    existing = deduped[key]
                    if q["source"] not in existing.setdefault("sources", []):
                        existing["sources"].append(q["source"])
                    if q.get("answer") and not existing.get("answer"):
                        existing["answer"] = q["answer"]
                    if not existing.get("options") and q.get("options"):
                        existing["options"] = q["options"]

            print(f"  [OCR]  {fname:45s} -> {len(qs):3d} items parsed ({file_new} new) in {dur:.1f}s")
        else:
            print(f"  [OCR]  {fname:45s} -> 0 items ({dur:.1f}s)")

    # 5. Clean, re-index and save
    final_list = list(deduped.values())
    for idx, q in enumerate(final_list, start=1):
        q["id"] = idx

    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(final_list, f, indent=2, ensure_ascii=False)

    with open(QUIZ_DATA_JS, "w", encoding="utf-8") as f:
        f.write("window.CS101_QUESTIONS = " + json.dumps(final_list, ensure_ascii=False) + ";\n")

    print("\n" + "=" * 60)
    print("EXTRACTION COMPLETE REPORT")
    print("=" * 60)
    print(f"Total raw question instances parsed: {total_extracted_raw}")
    print(f"Net new unique questions added to bank: {new_questions_added}")
    print(f"Final Total Question Bank Size: {len(final_list)}")
    print(f"Questions with verified answer: {sum(1 for q in final_list if q.get('answer'))}")
    print(f"Questions with options: {sum(1 for q in final_list if q.get('options'))}")
    print(f"Master files updated:\n  -> {MASTER_JSON}\n  -> {QUIZ_DATA_JS}")

if __name__ == "__main__":
    main()

