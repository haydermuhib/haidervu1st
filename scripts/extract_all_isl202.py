#!/usr/bin/env python3
import os, sys, subprocess, re, json, glob, time, unicodedata, warnings
import bs4
from bs4 import XMLParsedAsHTMLWarning
from concurrent.futures import ThreadPoolExecutor

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

BASE_DIR = "/home/haider/Desktop/Chores"
ISL_MCQS_DIR = os.path.join(BASE_DIR, "ISL202 - Islamic Studies", "MCQs & Quizzes")
ISL_PAST_DIR = os.path.join(BASE_DIR, "ISL202 - Islamic Studies", "Past Papers & Solved Papers")
MASTER_JSON = os.path.join(BASE_DIR, "isl202_quiz_bank.json")
QUIZ_DATA_JS = os.path.join(BASE_DIR, "quiz_data.js")
TESSDATA_DIR = "/tmp/tessdata"

def clean_text(s):
    if not s: return ""
    s = unicodedata.normalize("NFKC", str(s))
    # Remove unicode control characters except necessary newlines/spaces
    s = "".join(c for c in s if c in ["\n", "\t", " "] or unicodedata.category(c)[0] != "C")
    return re.sub(r"\s+", " ", s).strip()

def normalize_key(s):
    s = clean_text(s).lower()
    s = re.sub(r"^(?:marks\s*:\s*\d+\s*)?(?:please\s+choose\s+one\s*)?", "", s)
    s = re.sub(r"^[‘'\"`]?\s*(?:question|q)\s*(?:no|#|\.)?\s*[:\.]?\s*\d+\s*(?:of\s*\d+)?\s*", "", s)
    # Retain English letters, digits, AND all Arabic/Urdu Unicode blocks
    s = re.sub(r"[^a-z0-9\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", "", s)
    return s[:130]

def guess_isl_topic(q_text):
    ql = q_text.lower()
    if any(k in ql for k in ["tauheed", "tawheed", "oneness", "shirk", "polytheism", "angel", "malaikah", "jibreel", "mikail", "israfeel", "azrael", "revealed book", "torah", "zabur", "injil", "prophet", "nubuwwat", "risalat", "khatam", "akhira", "day of judgement", "resurrection", "destiny", "taqdeer", "iman", "faith"]):
        return "Tauheed & Faith (Aqeedah)"
    if any(k in ql for k in ["quran", "surah", "ayah", "ayat", "makki", "madani", "wahi", "revelation", "tafseer", "tafsir", "al-baqara", "al-shams", "bismillah"]):
        return "Quran & Exegesis (Tafseer)"
    if any(k in ql for k in ["hadith", "sunnah", "sahih bukhari", "sahih muslim", "sahihain", "sunan", "musnad", "sihah sitta", "sanad", "matn", "narrator", "narrated", "rawi", "abu huraira", "ayesha", "ibn umar", "ibn abbas"]):
        return "Hadith & Sunnah"
    if any(k in ql for k in ["salah", "salat", "namaz", "prayer", "wudu", "ablution", "tahajjud", "zakat", "nisab", "sawm", "roza", "fasting", "ramadan", "hajj", "umrah", "tawaf", "arafat", "mina", "muzdalifa", "jihad"]):
        return "Pillars of Islam (Ibadat)"
    if any(k in ql for k in ["fiqh", "shariah", "jurisprudence", "ijtihad", "ijma", "qiyas", "fatwa", "halal", "haram", "makruh", "abu hanifa", "imam malik", "imam shafi", "ahmad ibn hanbal", "jurist", "fuqaha"]):
        return "Islamic Law & Jurisprudence (Fiqh)"
    if any(k in ql for k in ["seerah", "prophet muhammad", "pbuh", "makkah", "madinah", "hijrah", "migration", "ghazwa", "badr", "uhud", "khandaq", "ahzab", "hudaibiyah", "conquest of makkah", "caliph", "khalifa", "abu bakr", "umar", "usman", "ali r.a", "ansar", "muhajireen"]):
        return "Prophetic Biography & History"
    if any(k in ql for k in ["honesty", "truthfulness", "sidq", "patience", "sabr", "modesty", "haya", "taqwa", "piety", "justice", "adl", "charity", "infaq", "ibad-u-rahman", "parents", "neighbor", "rights of"]):
        return "Islamic Ethics & Character (Akhlaq)"
    if any(k in ql for k in ["marriage", "nikah", "divorce", "talaq", "inheritance", "riba", "usury", "trade", "contract", "women", "society", "family"]):
        return "Social & Economic Teachings"
    return "General Islamic Studies"

def clean_question_noise(q_text):
    q = re.sub(r"\(?\s*Marks:\s*\d+\s*\)?|\–\s*Please choose one|-\s*Please choose one|Select\s+(?:the\s+)?correct\s+option\s*:?", "", q_text, flags=re.I)
    q = re.sub(r"^[‘'\"`]?\s*(?:Question|Q)\s*(?:#|No|\.)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?(?:\s*\([^)]*\))?:?", "", q, flags=re.I)
    q = re.sub(r"Start\s*time\s*:\s*\d+:\d+(?::\d+)?\s*(?:AM|PM)?,?\s*\d*\s*\w*\s*\d*\s*\)?", "", q, flags=re.I)
    q = re.sub(r"Quiz\s*Start\s*Time\s*:\s*\d+:\d+(?::\d+)?\s*(?:AM|PM)?,?\s*\d*\s*\w*\s*\d*", "", q, flags=re.I)
    q = re.sub(r"Total\s*Marks\s*:\s*\d+", "", q, flags=re.I)
    q = re.sub(r"Whatsapp\s*[:#\-]?\s*[\d\s\-]+", "", q, flags=re.I)
    q = re.sub(r"Email\s*:\s*[\w\.\@]+", "", q, flags=re.I)
    q = re.sub(r"Reload Math Equations", "", q, flags=re.I)
    q = re.sub(r"MADE BY [\w\s]+", "", q, flags=re.I)
    q = re.sub(r"PAID VU LMS HANDLING.*", "", q, flags=re.I)
    return clean_text(q)

def extract_colored_answers_map(pdf_path):
    answers_map = {}
    try:
        xml_data = subprocess.check_output(
            ["pdftohtml", "-xml", "-stdout", "-i", "-nodrm", pdf_path],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
        soup = bs4.BeautifulSoup(xml_data, "html.parser")
        
        colored_fonts = set()
        for fs in soup.find_all("fontspec"):
            c = fs.get("color", "").lower()
            if c and c not in ["#000000", "#ffffff", "#111111", "#222222", "#333333"]:
                colored_fonts.add(fs.get("id"))
                
        for t in soup.find_all("text"):
            if t.get("font") in colored_fonts:
                txt = t.get_text().strip()
                clean_ans = re.sub(r"^[►•\*\–\-✓✔○●\s]+|\(?[a-dA-D][\)\.\:]\s*", "", txt).strip()
                if len(clean_ans) > 1 and not re.search(r"examination|spring|fall|marks|question|midterm|virtualians", clean_ans, re.I):
                    k = normalize_key(clean_ans)
                    if k:
                        answers_map[k] = clean_ans
    except Exception:
        pass
    return answers_map

def parse_isl_text(txt, source_name, colored_map=None):
    questions = []
    lines = txt.splitlines()
    clean_lines = []

    skip_pats = [
        r"^(?:www\.|https?:\/\/)",
        r"(?:vustudy|vuhunt|vuaskari|virtualinspire|vuinsider|vupages|vutube|virtualians)",
        r"(?:subscribe|youtube|knowledge for us|whatsapp|best of luck)",
        r"(?:mid\s*term\s*examination|spring\s*20\d\d|fall\s*20\d\d|semester\s*fall|semester\s*spring)",
        r"(?:student\s*id|ref\s*no:|session\s*[-–:]\s*\d+|page\s*\d+\s*of\s*\d+)",
        r"^\s*page\s*\d+\s*$",
        r"^(?:for more papers|made and solved by|all students reading|we deal all kind|compiled by)",
        r"^(?:generated by foxit|for evaluation only)"
    ]
    skip_re = re.compile("|".join(skip_pats), re.I)

    for l in lines:
        ls = clean_text(l)
        if not ls:
            clean_lines.append("")
            continue
        if skip_re.search(ls) and len(ls) < 80:
            continue
        clean_lines.append(ls)

    full_clean = "\n".join(clean_lines)

    # PATTERN 1: Standard Question No / Question # / Q. blocks
    split_pat = r"(?:[\u2018\u2019\x27\"\u201c\u201d`]?\s*(?:Question|Q)\s*(?:#|No|\.)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?(?:\s*\([^)]*\))?:?)"
    if re.search(split_pat, full_clean, re.I):
        blocks = re.split(split_pat, full_clean, flags=re.I)
        for b in blocks[1:]:
            blines = [l.strip() for l in b.splitlines() if l.strip()]
            if not blines: continue

            q_lines = []
            opts = []
            ans = None
            notes = []

            for l in blines:
                if re.search(r"(?:marks\s*:\s*\d+|please choose one|select\s+the\s+correct\s+option|select\s+correct\s+option)", l, re.I):
                    continue

                # Check if this line is an explicit answer tag: Answer: b) Moderate
                ans_tag_m = re.match(r"^Answer\s*[:\.]\s*(?:[a-dA-D][\)\.\:]\s*)?(.*)", l, re.I)
                if ans_tag_m:
                    cand = clean_text(ans_tag_m.group(1))
                    if cand:
                        ans = cand
                    continue

                is_opt = bool(re.match(r"^[►•\*\–\-✓✔○●O\x0c]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    raw_opt = l
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", raw_opt).strip()
                    if "✓" in raw_opt or "✔" in raw_opt or "✔️" in raw_opt or "(correct)" in raw_opt.lower() or "right answer" in raw_opt.lower() or "page #" in raw_opt.lower() or "pg #" in raw_opt.lower():
                        clean_ans = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                        if clean_ans:
                            ans = clean_ans
                    clean_opt = re.sub(r"\s*(?:PG|Page)\s*#?\s*\d+.*|\s*\(correct\).*|\s*right\s*answer.*", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    q_lines.append(l)
                else:
                    notes.append(l)

            q_text = clean_question_noise(" ".join(q_lines))
            if not ans and colored_map and opts:
                for opt in opts:
                    k_opt = normalize_key(opt)
                    if k_opt in colored_map:
                        ans = opt
                        break

            if len(q_text) > 10 and not re.search(r"(?:@gmail\.com|whatsapp|waqas\.vu|subscribe|youtube\.com)", q_text, re.I):
                sol_notes = clean_text(" ".join(notes)) if notes else None
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": sol_notes,
                    "topic": guess_isl_topic(q_text),
                    "source": source_name
                })

    # PATTERN 2: Numbered items (e.g. 1. Question statement ... a) ... b) ...)
    numbered_blocks = re.split(r"\n(?=\s*\d+[\.\)]\s+[A-Za-z\u0600-\u06FF])", full_clean)
    if len(numbered_blocks) > 5:
        for b in numbered_blocks:
            blines = [l.strip() for l in b.splitlines() if l.strip()]
            if not blines: continue
            first_line = blines[0]
            m = re.match(r"^\d+[\.\)]\s+(.*)", first_line)
            if not m: continue
            
            q_lead = m.group(1).strip()
            rest = blines[1:]
            q_rest = []
            opts = []
            ans = None
            
            for r in rest:
                if re.search(r"(?:marks\s*:\s*\d+|please choose one|select\s+the\s+correct\s+option|whatsapp|follow us)", r, re.I):
                    continue
                ans_tag_m = re.match(r"^Answer\s*[:\.]\s*(?:[a-dA-D][\)\.\:]\s*)?(.*)", r, re.I)
                if ans_tag_m:
                    cand = clean_text(ans_tag_m.group(1))
                    if cand: ans = cand
                    continue

                is_opt = bool(re.match(r"^[a-dA-D][\)\.]\s+|[►•\*\–\-✓✔○●✔️]", r))
                if is_opt:
                    clean_opt = re.sub(r"^[a-dA-D][\)\.]\s+|[►•\*\–\-✓✔○●✔️\s]+", "", r).strip()
                    if "(✔)" in r or "✓" in r or "✔" in r or "✔️" in r or "(correct)" in r.lower():
                        clean_ans = re.sub(r"\(?[✓✔✔️]\)?|\(correct\)", "", clean_opt, flags=re.I).strip()
                        if clean_ans:
                            ans = clean_ans
                    clean_opt = re.sub(r"\(?[✓✔✔️]\)?|\(correct\)", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    q_rest.append(r)

            full_q = clean_question_noise(q_lead + (" " + " ".join(q_rest) if q_rest else ""))
            if len(full_q) > 10 and not re.search(r"(?:@gmail\.com|whatsapp|subscribe|youtube\.com)", full_q, re.I):
                questions.append({
                    "question": full_q,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": f"Verified Solution: {ans}" if ans else None,
                    "topic": guess_isl_topic(full_q),
                    "source": source_name
                })

    # PATTERN 3: Bulleted items with marked ✔️ (e.g. Miss Mehwish files)
    if len(questions) < 10:
        mehwish_blocks = re.split(r"\n(?=[A-Za-z0-9\u0600-\u06FF][^\n]+\n[•\*\–\-✓✔○●✔️\uf0b7])", full_clean)
        for b in mehwish_blocks:
            blines = [l.strip() for l in b.splitlines() if l.strip()]
            if len(blines) < 2: continue
            q_lead = blines[0]
            opts = []
            ans = None
            for r in blines[1:]:
                is_opt = bool(re.match(r"^[•\*\–\-✓✔○●✔️\uf0b7]\s*(?:O\s*)?", r))
                if is_opt:
                    clean_opt = re.sub(r"^[•\*\–\-✓✔○●✔️\uf0b7\s]+|O\s*", "", r).strip()
                    if "✔️" in r or "✓" in r or "✔" in r:
                        clean_ans = re.sub(r"[✓✔✔️]", "", clean_opt).strip()
                        if clean_ans: ans = clean_ans
                    clean_opt = re.sub(r"[✓✔✔️]", "", clean_opt).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
            full_q = clean_question_noise(q_lead)
            if len(full_q) > 10 and len(opts) >= 2 and not re.search(r"(?:@gmail\.com|whatsapp|paid vu|mam mehwish)", full_q, re.I):
                questions.append({
                    "question": full_q,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": f"Verified Solution: {ans}" if ans else None,
                    "topic": guess_isl_topic(full_q),
                    "source": source_name
                })

    return questions

def process_file(file_path):
    source_name = os.path.basename(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        try:
            txt = subprocess.check_output(["pdftotext", "-enc", "UTF-8", file_path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
        except Exception:
            txt = ""
        
        try:
            info = subprocess.check_output(["pdfinfo", file_path]).decode("utf-8", errors="ignore")
            num_pages = 0
            for l in info.splitlines():
                if l.startswith("Pages:"):
                    num_pages = int(l.split(":")[1].strip())
                    break
        except Exception:
            num_pages = 0

        chars_per_page = len(txt) / num_pages if num_pages else 0
        is_scanned = (len(txt) < 300) or (num_pages > 3 and chars_per_page < 100)
        
        # If text-based and has sufficient text density
        if not is_scanned and len(txt) > 300:
            colored_map = extract_colored_answers_map(file_path)
            return parse_isl_text(txt, source_name, colored_map)
        else:
            # Scanned PDF: multi-threaded OCR with English + Arabic + Urdu
            if num_pages == 0: return []
            num_pages = min(num_pages, 150)
            prefix = f"/tmp/isl202_ocr_{source_name[:8]}"
            
            def ocr_page(p):
                subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p), file_path, f"{prefix}_{p}"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                pfiles = glob.glob(f"{prefix}_{p}*.png")
                if not pfiles: return ""
                txt_out = f"{prefix}_{p}_out"
                
                cmd = ["tesseract", pfiles[0], txt_out]
                if os.path.exists(os.path.join(TESSDATA_DIR, "ara.traineddata")):
                    cmd += ["--tessdata-dir", TESSDATA_DIR, "-l", "eng+ara+urd"]
                
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                out_txt = ""
                if os.path.exists(f"{txt_out}.txt"):
                    try:
                        with open(f"{txt_out}.txt", "r", encoding="utf-8", errors="ignore") as f:
                            out_txt = f.read()
                    except: pass
                    try: os.remove(f"{txt_out}.txt")
                    except: pass
                for pf in pfiles:
                    try: os.remove(pf)
                    except: pass
                return out_txt

            with ThreadPoolExecutor(max_workers=8) as ex:
                pages_text = list(ex.map(ocr_page, range(1, num_pages + 1)))
            full_ocr_txt = "\n\n".join(pages_text)
            return parse_isl_text(full_ocr_txt, source_name + " (Scanned Exam OCR)")

    return []

def main():
    print("=== HIGH-ACCURACY ISL202 ARABIC-PRESERVING EXTRACTION PIPELINE ===")
    all_files = []
    for f in glob.glob(os.path.join(ISL_MCQS_DIR, "*.pdf")):
        all_files.append(f)
    for f in glob.glob(os.path.join(ISL_PAST_DIR, "*.pdf")):
        all_files.append(f)
        
    all_files = sorted(list(set(all_files)))
    print(f"Targeting {len(all_files)} ISL202 source documents.")

    raw_extracted = []
    t0 = time.time()
    for idx, f in enumerate(all_files, 1):
        fname = os.path.basename(f)
        print(f"[{idx}/{len(all_files)}] Processing {fname}...")
        qs = process_file(f)
        print(f"    -> Extracted {len(qs)} question entries.")
        raw_extracted.extend(qs)

    print(f"\nRaw question items captured: {len(raw_extracted)} in {time.time() - t0:.1f}s")

    # DEDUPLICATION & ENRICHMENT
    merged_map = {}
    for q in raw_extracted:
        q_text = clean_text(q["question"])
        if len(q_text) < 14:
            continue
        key = normalize_key(q_text)
        if not key or len(key) < 6:
            continue
            
        src = q.get("source", "ISL202 Paper")
        if key not in merged_map:
            merged_map[key] = {
                "question": q_text,
                "options": q.get("options", []),
                "answer": q.get("answer"),
                "solution_notes": q.get("solution_notes"),
                "topic": q.get("topic") or guess_isl_topic(q_text),
                "sources": [src] if src else []
            }
        else:
            rec = merged_map[key]
            if src and src not in rec["sources"]:
                rec["sources"].append(src)
            if not rec["answer"] and q.get("answer"):
                rec["answer"] = q["answer"]
            if len(q.get("options", [])) > len(rec["options"]):
                rec["options"] = q["options"]
            if not rec["solution_notes"] and q.get("solution_notes"):
                rec["solution_notes"] = q["solution_notes"]
            if rec["topic"] == "General Islamic Studies" and q.get("topic") != "General Islamic Studies":
                rec["topic"] = q["topic"]

    # Finalize ordered list with permanent sequential ID
    final_questions = []
    for idx, (k, item) in enumerate(sorted(merged_map.items(), key=lambda x: x[1]["question"]), 1):
        item["id"] = idx
        clean_opts = []
        for o in item["options"]:
            co = clean_text(o)
            if co and co not in clean_opts:
                clean_opts.append(co)
        item["options"] = clean_opts
        
        # Canonicalize answer matching option
        if item["answer"] and item["options"]:
            for o in item["options"]:
                if o.strip().lower() == item["answer"].strip().lower() or normalize_key(o) == normalize_key(item["answer"]):
                    item["answer"] = o
                    break

        final_questions.append(item)

    print(f"\nStrictly Unique ISL202 Questions: {len(final_questions)}")

    # Count questions containing Arabic characters
    arabic_count = len([q for q in final_questions if any('\u0600' <= c <= '\u06FF' for c in q["question"] + " " + " ".join(q["options"]))])
    print(f"Questions containing preserved Arabic / Urdu Unicode: {arabic_count}")

    # Save to JSON
    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)
    print(f"Saved master JSON: {MASTER_JSON} ({os.path.getsize(MASTER_JSON)/1024:.1f} KB)")

    # Read existing CS101 and ENG101 data to update quiz_data.js
    cs101_file = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
    eng101_file = os.path.join(BASE_DIR, "eng101_quiz_bank.json")
    
    cs101_data = []
    eng101_data = []
    if os.path.exists(cs101_file):
        with open(cs101_file, "r", encoding="utf-8") as f:
            cs101_data = json.load(f)
    if os.path.exists(eng101_file):
        with open(eng101_file, "r", encoding="utf-8") as f:
            eng101_data = json.load(f)

    js_content = f"// Combined Course Bank (Auto-generated)\nwindow.CS101_QUESTIONS = {json.dumps(cs101_data, ensure_ascii=False)};\nwindow.ENG101_QUESTIONS = {json.dumps(eng101_data, ensure_ascii=False)};\nwindow.ISL202_QUESTIONS = {json.dumps(final_questions, ensure_ascii=False)};\n"
    with open(QUIZ_DATA_JS, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Updated {QUIZ_DATA_JS} with CS101 ({len(cs101_data)}), ENG101 ({len(eng101_data)}), and ISL202 ({len(final_questions)})! ({os.path.getsize(QUIZ_DATA_JS)/1024/1024:.2f} MB)")

    # Topic breakdown
    topic_counts = {}
    for q in final_questions:
        topic_counts[q["topic"]] = topic_counts.get(q["topic"], 0) + 1
    print("\nTopic Breakdown:")
    for t, c in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f"  - {t}: {c} questions")

if __name__ == "__main__":
    main()
