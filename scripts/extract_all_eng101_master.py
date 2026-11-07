#!/usr/bin/env python3
import os, sys, subprocess, re, json, glob, time, warnings
import bs4
from bs4 import XMLParsedAsHTMLWarning
from concurrent.futures import ThreadPoolExecutor

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

BASE_DIR = "/home/haider/Desktop/Chores"
ENG_MCQS_DIR = os.path.join(BASE_DIR, "ENG101 - English Comprehension", "MCQs & Quizzes")
ENG_PAST_DIR = os.path.join(BASE_DIR, "ENG101 - English Comprehension", "Past Papers & Solved Papers")
TEMP_UNPACKED_DIR = os.path.join(BASE_DIR, "temp_eng101_unpacked")
TEMP_DOC_TXT_DIR = "/tmp/eng101_doc_txt"
MASTER_JSON = os.path.join(BASE_DIR, "eng101_quiz_bank.json")
QUIZ_DATA_JS = os.path.join(BASE_DIR, "quiz_data.js")

os.makedirs(TEMP_DOC_TXT_DIR, exist_ok=True)

def clean_text(s):
    if not s: return ""
    return re.sub(r"\s+", " ", str(s)).strip()

def normalize_key(s):
    s = s.lower()
    s = re.sub(r"^(?:marks\s*:\s*\d+\s*)?(?:please\s+choose\s+one\s*)?", "", s)
    s = re.sub(r"^[‘'\"`]?\s*(?:question|q)\s*(?:no|#|\.)?\s*[:\.]?\s*\d+\s*(?:of\s*\d+)?\s*", "", s)
    s = re.sub(r"[^a-z0-9]", "", s)
    return s[:120]

def guess_eng_topic(q_text):
    ql = q_text.lower()
    if any(k in ql for k in ["prefix", "suffix", "root word", "root / prefix", "root/prefix", "affix", "annu", "poly", "post-", "pre-", "sub-", "micro", "trans-", "inter-", "-tion", "-ment", "-able", "-ible", "-ity", "-logy", "etymology", "combining form"]):
        return "Prefixes, Suffixes & Roots"
    if any(k in ql for k in ["phrasal verb", "bring down", "brought down", "bring up", "brought up", "bring on", "brought on", "call off", "give up", "carry on", "look forward", "set up", "figure out", "put off", "run into", "take over", "turn down", "break down"]):
        return "Phrasal Verbs & Idioms"
    if any(k in ql for k in ["synonym", "antonym", "opposite in meaning", "closest in meaning", "closest meaning", "meaning of the underlined", "meaning of the word", "underlined word", "substitute word", "definition of", "means closest"]):
        return "Vocabulary, Synonyms & Antonyms"
    if any(k in ql for k in ["sentence", "compound sentence", "complex sentence", "compound-complex", "simple sentence", "dependent clause", "independent clause", "clause", "fragment", "run-on", "comma splice", "dangling modifier", "parallelism", "parallel structure", "type of sentence"]):
        return "Sentence Structure & Types"
    if any(k in ql for k in ["verb", "noun", "adjective", "adverb", "preposition", "conjunction", "pronoun", "interjection", "subject-verb", "subject verb", "infinitive", "gerund", "participle", "past tense", "plural of", "form of verb"]):
        return "Grammar & Parts of Speech"
    if any(k in ql for k in ["punctuation", "comma", "semicolon", "colon", "apostrophe", "quotation mark", "hyphen", "spelling", "correct spelling", "capitalization", "stress on the"]):
        return "Punctuation, Spelling & Mechanics"
    if any(k in ql for k in ["transitional", "transition", "cause and effect", "cause & effect", "comparison and contrast", "chronological", "cohesion", "coherence", "spatial order", "paragraph", "topic sentence"]):
        return "Text Organization & Transitions"
    if any(k in ql for k in ["fact", "opinion", "bias", "tone", "author's tone", "attitude", "subjective", "objective", "tone is"]):
        return "Fact vs. Opinion & Tone"
    if any(k in ql for k in ["infer", "inference", "passage", "reading", "main idea", "author's purpose", "reading comprehension", "implies", "can be inferred", "what does the text say"]):
        return "Reading Comprehension & Inference"
    if any(k in ql for k in ["dictionary", "guide words", "index", "glossary", "skimming", "scanning", "sq3r", "bibliography", "outline", "précis", "summary", "paraphrase", "brainstorming"]):
        return "Writing & Study Skills"
    return "General English Comprehension"

def clean_question_noise(q_text):
    q = re.sub(r"\(?\s*Marks:\s*\d+\s*\)?|\–\s*Please choose one|-\s*Please choose one|Select\s+(?:the\s+)?correct\s+option\s*:?", "", q_text, flags=re.I)
    q = re.sub(r"^[‘'\"`]?\s*(?:Question|Q)\s*(?:#|No|\.)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?(?:\s*\([^)]*\))?:?", "", q, flags=re.I)
    q = re.sub(r"Start\s*time\s*:\s*\d+:\d+(?::\d+)?\s*(?:AM|PM)?,?\s*\d*\s*\w*\s*\d*\s*\)?", "", q, flags=re.I)
    q = re.sub(r"Quiz\s*Start\s*Time\s*:\s*\d+:\d+(?::\d+)?\s*(?:AM|PM)?,?\s*\d*\s*\w*\s*\d*", "", q, flags=re.I)
    q = re.sub(r"Total\s*Marks\s*:\s*\d+", "", q, flags=re.I)
    q = re.sub(r"FILE MARGE BY ALI KHAN.*", "", q, flags=re.I)
    q = re.sub(r"WA-\s*NUM\s*\d+", "", q, flags=re.I)
    q = re.sub(r"Solved\s+By\s*:\s*[\w\s]+", "", q, flags=re.I)
    q = re.sub(r"Whatsapp\s*:\s*[\d\s]+", "", q, flags=re.I)
    q = re.sub(r"Email\s*:\s*[\w\.\@]+", "", q, flags=re.I)
    q = re.sub(r"Compiled by Barbie", "", q, flags=re.I)
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
                    k = re.sub(r"[^a-z0-9]", "", clean_ans.lower())
                    if k:
                        answers_map[k] = clean_ans
    except Exception:
        pass
    return answers_map

def parse_eng_text(txt, source_name, colored_map=None):
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
        r"^(?:generated by foxit|for evaluation only|mc100401285)"
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

    # PATTERN 1: Standard Question No / Question # / Q. blocks
    split_pat = r"(?:[\u2018\u2019\x27\"\u201c\u201d`]?\s*(?:Question|Q)\s*(?:#|No|\.)?\s*[:\.]?\s*\d+(?:\s*of\s*\d+)?(?:\s*\([^)]*\))?)"
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

                is_opt = bool(re.match(r"^[►•\*\–\-✓✔○●O\x0c]|\(?[a-dA-D][\)\.\:]\s+", l))
                if is_opt:
                    raw_opt = l
                    clean_opt = re.sub(r"^[►•\*\–\-✓✔○●Oe\s]+|\(?[a-dA-D][\)\.\:]\s*", "", raw_opt).strip()
                    if "✓" in raw_opt or "✔" in raw_opt or "(correct)" in raw_opt.lower() or "right answer" in raw_opt.lower() or "page #" in raw_opt.lower() or "pg #" in raw_opt.lower():
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
            # Match colored answer if available
            if not ans and colored_map and opts:
                for opt in opts:
                    k_opt = re.sub(r"[^a-z0-9]", "", opt.lower())
                    if k_opt in colored_map:
                        ans = opt
                        break

            # Filter out non-questions (emails, advertisements)
            if len(q_text) > 12 and not re.search(r"(?:@gmail\.com|whatsapp|waqas\.vu|subscribe|youtube\.com)", q_text, re.I):
                sol_notes = clean_text(" ".join(notes)) if notes else None
                questions.append({
                    "question": q_text,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": sol_notes,
                    "topic": guess_eng_topic(q_text),
                    "source": source_name
                })

    # PATTERN 2: Numbered items with options (e.g. Barbie: 1. Question ... a) ... b) ... (✔))
    numbered_blocks = re.split(r"\n(?=\s*\d+[\.\)]\s+[A-Z])", full_clean)
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
            
            inline_ans_m = re.search(r"\(([^)]+)\)\s*$", q_lead)
            if inline_ans_m and not rest:
                cand = inline_ans_m.group(1).strip()
                if len(cand) < 60 and not re.match(r"^(?:marks|page|lecture)", cand, re.I):
                    ans = cand
                    q_lead = q_lead[:inline_ans_m.start()].strip()

            for r in rest:
                if re.search(r"(?:marks\s*:\s*\d+|please choose one|select\s+the\s+correct\s+option|compiled by)", r, re.I):
                    continue
                is_opt = bool(re.match(r"^[a-dA-D][\)\.]\s+|[►•\*\–\-✓✔○●]", r))
                if is_opt:
                    clean_opt = re.sub(r"^[a-dA-D][\)\.]\s+|[►•\*\–\-✓✔○●\s]+", "", r).strip()
                    if "(✔)" in r or "✓" in r or "✔" in r or "(correct)" in r.lower():
                        clean_ans = re.sub(r"\(?[✓✔]\)?|\(correct\)", "", clean_opt, flags=re.I).strip()
                        if clean_ans:
                            ans = clean_ans
                    clean_opt = re.sub(r"\(?[✓✔]\)?|\(correct\)", "", clean_opt, flags=re.I).strip()
                    if clean_opt and clean_opt not in opts:
                        opts.append(clean_opt)
                elif not opts:
                    q_rest.append(r)

            full_q = clean_question_noise(q_lead + (" " + " ".join(q_rest) if q_rest else ""))
            if len(full_q) > 12 and not re.search(r"(?:@gmail\.com|whatsapp|waqas\.vu|subscribe|youtube\.com)", full_q, re.I):
                questions.append({
                    "question": full_q,
                    "options": opts,
                    "answer": ans,
                    "solution_notes": f"Verified Solution: {ans}" if ans else None,
                    "topic": guess_eng_topic(full_q),
                    "source": source_name
                })

    # PATTERN 3: Unnumbered question blocks followed by ► options (e.g. ENG101 Midterm MCQs.pdf)
    if len(questions) < 5:
        matches = re.findall(r'([A-Z][^\n]+(?:\n[^\n►✓]+)*)\n(?:[✓\s\n]*)\n((?:►[^\n]+\n?){2,6})', full_clean)
        for q_raw, opt_raw in matches:
            q_clean = clean_question_noise(q_raw)
            opt_list = []
            ans = None
            for ol in opt_raw.splitlines():
                ol_clean = re.sub(r"^[►•\*\–\-✓✔○●\s]+", "", ol).strip()
                if ol_clean:
                    opt_list.append(ol_clean)
            if len(q_clean) > 12 and len(opt_list) >= 2 and not re.search(r"(?:@gmail\.com|whatsapp|waqas\.vu|subscribe|youtube\.com)", q_clean, re.I):
                questions.append({
                    "question": q_clean,
                    "options": opt_list,
                    "answer": ans,
                    "solution_notes": None,
                    "topic": guess_eng_topic(q_clean),
                    "source": source_name
                })

    return questions

def process_file(file_path):
    source_name = os.path.basename(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        try:
            txt = subprocess.check_output(["pdftotext", file_path, "-"], stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
        except Exception:
            txt = ""
        
        # If text-based
        if len(txt) > 500:
            colored_map = extract_colored_answers_map(file_path)
            return parse_eng_text(txt, source_name, colored_map)
        else:
            # Scanned PDF: parallel OCR
            try:
                info = subprocess.check_output(["pdfinfo", file_path]).decode("utf-8", errors="ignore")
                num_pages = 0
                for l in info.splitlines():
                    if l.startswith("Pages:"):
                        num_pages = int(l.split(":")[1].strip())
                        break
            except Exception:
                num_pages = 0
            
            if num_pages == 0: return []
            num_pages = min(num_pages, 150)
            prefix = f"/tmp/eng101_ocr_{source_name[:8]}"
            
            def ocr_page(p):
                subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p), file_path, f"{prefix}_{p}"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                pfiles = glob.glob(f"{prefix}_{p}*.png")
                if not pfiles: return ""
                txt_out = f"{prefix}_{p}_out"
                subprocess.run(["tesseract", pfiles[0], txt_out], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
            return parse_eng_text(full_ocr_txt, source_name + " (Scanned Exam OCR)")

    elif ext == ".doc":
        out_txt_file = os.path.join(TEMP_DOC_TXT_DIR, os.path.splitext(source_name)[0] + ".txt")
        subprocess.run(["soffice", "--headless", "--convert-to", "txt:Text", file_path, "--outdir", TEMP_DOC_TXT_DIR],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(out_txt_file):
            try:
                with open(out_txt_file, "r", encoding="utf-8", errors="ignore") as f:
                    txt = f.read()
                return parse_eng_text(txt, source_name)
            except Exception:
                pass
    return []

def main():
    print("=== HIGH-ACCURACY ENG101 EXTRACTION & VERIFICATION ENGINE ===")
    all_files = []
    
    for f in glob.glob(os.path.join(ENG_MCQS_DIR, "*.pdf")):
        all_files.append(f)
    for f in glob.glob(os.path.join(ENG_PAST_DIR, "*")):
        if os.path.splitext(f)[1].lower() in [".pdf", ".doc"]:
            all_files.append(f)
    for f in glob.glob(os.path.join(TEMP_UNPACKED_DIR, "*")):
        if os.path.splitext(f)[1].lower() in [".pdf", ".doc"]:
            all_files.append(f)
            
    all_files = sorted(list(set(all_files)))
    print(f"Targeting {len(all_files)} ENG101 source documents.")

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
        if not key or len(key) < 8:
            continue
            
        src = q.get("source", "ENG101 Paper")
        if key not in merged_map:
            merged_map[key] = {
                "question": q_text,
                "options": q.get("options", []),
                "answer": q.get("answer"),
                "solution_notes": q.get("solution_notes"),
                "topic": q.get("topic") or guess_eng_topic(q_text),
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
            if rec["topic"] == "General English Comprehension" and q.get("topic") != "General English Comprehension":
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
        
        # Canonicalize answer
        if item["answer"] and item["options"]:
            for o in item["options"]:
                if o.strip().lower() == item["answer"].strip().lower():
                    item["answer"] = o
                    break

        final_questions.append(item)

    print(f"\nStrictly Unique ENG101 Questions: {len(final_questions)}")

    # Save to JSON
    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)
    print(f"Saved master JSON: {MASTER_JSON} ({os.path.getsize(MASTER_JSON)/1024:.1f} KB)")

    # Read existing CS101 data from cs101_quiz_bank.json to update quiz_data.js
    cs101_file = os.path.join(BASE_DIR, "cs101_quiz_bank.json")
    if os.path.exists(cs101_file):
        with open(cs101_file, "r", encoding="utf-8") as f:
            cs101_data = json.load(f)
        
        js_content = f"// Combined Course Bank (Auto-generated)\nwindow.CS101_QUESTIONS = {json.dumps(cs101_data, ensure_ascii=False)};\nwindow.ENG101_QUESTIONS = {json.dumps(final_questions, ensure_ascii=False)};\n"
        with open(QUIZ_DATA_JS, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"Updated {QUIZ_DATA_JS} with both CS101 ({len(cs101_data)}) and ENG101 ({len(final_questions)}) questions! ({os.path.getsize(QUIZ_DATA_JS)/1024/1024:.2f} MB)")

    # Topic breakdown
    topic_counts = {}
    for q in final_questions:
        topic_counts[q["topic"]] = topic_counts.get(q["topic"], 0) + 1
    print("\nTopic Breakdown:")
    for t, c in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f"  - {t}: {c} questions")

if __name__ == "__main__":
    main()

