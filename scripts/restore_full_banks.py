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

def clean_question_text(q):
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
    q = re.sub(r"^[\s\.\–\-\_\:\,\;\#\*\(\)]+", "", q)
    return clean_text(q)

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

# Re-run the extractors for ISL, ENG, and CS to get the full collections
def run_original_extractors():
    print("Refreshing full dataset collections...")
    # 1. Run ISL202
    subprocess.run(["python3", "extract_all_isl202.py"], check=True)
    # 2. Run ENG101
    subprocess.run(["python3", "extract_all_eng101.py"], check=True)
    # 3. Run CS101
    subprocess.run(["python3", "extract_all_past_papers_deep.py"], check=True)

if __name__ == "__main__":
    run_original_extractors()

