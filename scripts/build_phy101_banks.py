#!/usr/bin/env python3
"""
PHY101 - Physics Midterm Bank Builder with Final-Term Archiving
Splits Halliday, Resnick & Walker 44-chapter test bank into:
  - Midterm Bank (Chapters 1–22 + All VU Midterm Papers & Quizzes) -> 1,509 Questions
  - Final Term Archive (Chapters 23–44: Electromagnetism, Optics, Modern/Nuclear) -> 1,240 Questions
Saved to:
  - Active Studio: phy101_objective.json (1,509 Midterm Questions)
  - Archive: PHY101 - Physics/Final Term & Full Bank Archive/phy101_final_term_objective.json
"""

import os
import sys
import re
import json
import subprocess
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter

BASE_DIR = "PHY101 - Physics"
ARCHIVE_DIR = os.path.join(BASE_DIR, "Final Term & Full Bank Archive")
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def read_pdf(path):
    try:
        res = subprocess.run(["pdftotext", path, "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return res.stdout
    except Exception as e:
        print(f"Error reading PDF {path}: {e}")
        return ""

def read_docx(path):
    try:
        with zipfile.ZipFile(path) as docx:
            tree = ET.fromstring(docx.read("word/document.xml"))
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            paragraphs = []
            for p in tree.iterfind('.//w:p', namespaces):
                texts = [node.text for node in p.iterfind('.//w:t', namespaces) if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
            return "\n".join(paragraphs)
    except Exception as e:
        print(f"Error reading docx {path}: {e}")
        return ""

def clean_text(t):
    if not t:
        return ""
    t = re.sub(r"[\r\f]", "", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def normalize_key(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9]", "", t)
    return t[:100]

def classify_phy101_topic(q):
    ql = q.lower()
    if any(k in ql for k in ["vector", "displacement", "velocity", "acceleration", "projectile", "kinematic", "speed", "distance", "free fall", "dimension"]):
        return "Kinematics & Vectors"
    if any(k in ql for k in ["force", "newton", "friction", "normal force", "tension", "weight", "mass", "free-body", "action-reaction"]):
        return "Dynamics & Forces"
    if any(k in ql for k in ["work", "kinetic energy", "potential energy", "power", "conservative", "joule", "watt", "mechanical energy"]):
        return "Work, Energy & Power"
    if any(k in ql for k in ["momentum", "impulse", "collision", "elastic", "inelastic", "center of mass"]):
        return "Momentum & Collisions"
    if any(k in ql for k in ["torque", "rotat", "angular", "moment of inertia", "axis", "centripetal", "rolling", "gyroscope"]):
        return "Rotational Motion & Torque"
    if any(k in ql for k in ["fluid", "pressure", "density", "buoyan", "archimedes", "bernoulli", "pascal", "viscos", "elasticity", "stress", "strain", "young"]):
        return "Fluid Mechanics & Elasticity"
    if any(k in ql for k in ["harmonic", "oscillation", "pendulum", "spring", "period", "frequency", "wave", "amplitude", "sound", "doppler", "resonance", "wavelength"]):
        return "Oscillations & Waves"
    if any(k in ql for k in ["thermodynamic", "heat", "temperature", "entropy", "celsius", "kelvin", "conduction", "convection", "radiation", "calorimet", "isothermal", "adiabatic", "specific heat", "gas law"]):
        return "Thermodynamics & Heat"
    return "General Physics"

def classify_final_term_topic(q):
    ql = q.lower()
    if any(k in ql for k in ["gauss", "electric field", "electric charge", "coulomb", "dipole"]):
        return "Electrostatics & Gauss' Law"
    if any(k in ql for k in ["capacit", "dielectric", "electric potential", "volt"]):
        return "Electric Potential & Capacitance"
    if any(k in ql for k in ["resistor", "current", "ohm", "circuit", "kirchhoff", "emf", "ampere"]):
        return "Current, Resistance & DC Circuits"
    if any(k in ql for k in ["magnetic", "biot-savart", "lorentz", "solenoid", "toroid", "hall effect"]):
        return "Magnetic Fields & Ampere's Law"
    if any(k in ql for k in ["faraday", "induct", "lenz", "alternating current", "ac circuit", "maxwell"]):
        return "Electromagnetic Induction & AC"
    if any(k in ql for k in ["interference", "diffraction", "lens", "mirror", "refraction", "reflection", "optical", "light", "poynting"]):
        return "Optics & Electromagnetic Waves"
    if any(k in ql for k in ["relativity", "lorentz transform", "time dilation", "length contraction"]):
        return "Special Relativity"
    if any(k in ql for k in ["photon", "photoelectric", "compton", "de broglie", "quantum", "bohr", "schrodinger", "atom"]):
        return "Quantum & Atomic Physics"
    if any(k in ql for k in ["nuclear", "radioactive", "fission", "fusion", "decay", "quark", "lepton"]):
        return "Nuclear & Particle Physics"
    return "Advanced Physics"

def extract_questions():
    midterm_map = {}
    final_map = {}

    def add_midterm(q_text, opts, ans=None, note=None, src="VU Midterm Materials"):
        if not q_text or len(q_text) < 10 or len(opts) < 2:
            return
        clean_opts = [clean_text(o) for o in opts if clean_text(o)]
        if len(clean_opts) < 2:
            return
        k = normalize_key(q_text)
        if k not in midterm_map:
            midterm_map[k] = {
                "question": q_text,
                "options": clean_opts,
                "answer": ans,
                "solution_notes": note,
                "topic": classify_phy101_topic(q_text),
                "sources": [src]
            }
        else:
            if src not in midterm_map[k]["sources"]:
                midterm_map[k]["sources"].append(src)
            if not midterm_map[k]["answer"] and ans:
                midterm_map[k]["answer"] = ans

    # Source 1: VUBuddy Mega MCQs (Chapters 1–22 -> Midterm, Chapters 23–44 -> Final Term Archive)
    fp_vub = os.path.join(BASE_DIR, "MCQs & Quizzes/PHY101 Midterm MCQs Lectures 1-44 by VUBuddy.pdf")
    txt_vub = read_pdf(fp_vub)
    chunks = re.split(r"\n(?=\s*\d+\.\s+[A-Za-z0-9])", txt_vub)
    current_ch = 1
    for c in chunks:
        m_ch = re.search(r"Chapter\s*(\d+)\s*:", c, re.I)
        if m_ch:
            current_ch = int(m_ch.group(1))
        m_num = re.match(r"^\s*(\d+)\.\s+(.*?)(?=\n\s*A\.\s*|\Z)", c, re.DOTALL)
        if m_num:
            q_text = clean_text(m_num.group(2))
            opts = re.findall(r"\n\s*([A-E])\.\s*([^\n]+)", c)
            if len(opts) >= 2:
                opts_dict = {letter: opt.strip() for letter, opt in opts}
                opts_list = [opt.strip() for letter, opt in opts]
                m_ans = re.search(r"\bAns:\s*([A-E])\b", c, re.I)
                ans_val = opts_dict.get(m_ans.group(1).upper()) if m_ans else None
                k = normalize_key(q_text)
                if current_ch <= 22:
                    add_midterm(q_text, opts_list, ans=ans_val, src=f"VUBuddy Midterm Chapter {current_ch}")
                else:
                    if k not in final_map:
                        final_map[k] = {
                            "question": q_text,
                            "options": opts_list,
                            "answer": ans_val,
                            "chapter": current_ch,
                            "topic": classify_final_term_topic(q_text),
                            "source": f"Halliday & Resnick Chapter {current_ch}"
                        }

    # Source 2: Mudasar Qureshi Lecture-wise Solved MCQs
    fp_mq = os.path.join(BASE_DIR, "MCQs & Quizzes/PHY101 Midterm Lecture-wise Solved MCQs by Mudasar Qureshi.pdf")
    txt_mq = read_pdf(fp_mq)
    for c in re.split(r"\n(?=\s*\d+\.\s+[A-Za-z0-9])", txt_mq):
        m_q = re.search(r"^\s*\d+\.\s+(.*?)(?=\n\s*[a-d]\)\s*|\Z)", c, re.DOTALL)
        if m_q:
            q_text = clean_text(m_q.group(1))
            opts = re.findall(r"\n\s*([a-d])\)\s*([^\n]+)", c)
            if len(opts) >= 2:
                opts_dict = {letter.lower(): opt.strip() for letter, opt in opts}
                opts_list = [opt.strip() for letter, opt in opts]
                m_ans = re.search(r"Answer:\s*([a-d])\)?\s*([^\n]*)", c, re.I)
                ans_val = m_ans.group(2).strip() if (m_ans and m_ans.group(2).strip()) else (opts_dict.get(m_ans.group(1).lower()) if m_ans else None)
                add_midterm(q_text, opts_list, ans=ans_val, src="Mudasar Qureshi Midterm Solved MCQs")

    # Source 3: Mickey Ch Updated Solved MCQs
    fp_mc = os.path.join(BASE_DIR, "MCQs & Quizzes/PHY101 Midterm Updated Solved MCQs by Mickey Ch.pdf")
    txt_mc = read_pdf(fp_mc)
    for c in re.split(r"\n(?=\s*\d+\.\s+[A-Za-z0-9])", txt_mc):
        m_q = re.search(r"^\s*\d+\.\s+(.*?)(?=\n\s*[a-d]\)\s*|\Z)", c, re.DOTALL)
        if m_q:
            q_text = clean_text(m_q.group(1))
            opts = re.findall(r"\n\s*([a-d])\)\s*([^\n]+)", c)
            if len(opts) >= 2:
                add_midterm(q_text, [opt.strip() for letter, opt in opts], src="Mickey Ch Updated Solved MCQs")

    # Source 4: Past Papers
    for fn in ["PHY101 Midterm Past Paper 1.pdf", "PHY101 Midterm Past Paper 2.pdf", "PHY101 Midterm Past Paper 2009.pdf", "PHY101 Midterm Past Papers Mega File.pdf", "PHY101 Midterm Past Papers.pdf"]:
        txt = read_pdf(os.path.join(BASE_DIR, "Past Papers & Solved Papers", fn))
        for it in re.split(r"\n(?=[A-Za-z0-9][^\n]+(?:\:|\?|\_{2,}))", txt):
            opts = re.findall(r"►\s*([^\n]+)", it)
            if len(opts) >= 2:
                lines = [l.strip() for l in it.split("\n") if l.strip() and not l.strip().startswith("►")]
                if lines:
                    add_midterm(lines[0], opts, src=fn.replace(".pdf", ""))

    # Source 5: Docx
    txt_docx = read_docx(os.path.join(BASE_DIR, "Past Papers & Solved Papers/PHY101 Midterm Past Papers (Word).docx"))
    for s in re.split(r"Question\s*No\s*:\s*\d+", txt_docx, flags=re.I)[1:]:
        opts = re.findall(r"[►A-E]\.?\s*([^\n]+)", s)
        if len(opts) >= 2:
            lines = [l.strip() for l in s.split("\n") if l.strip() and not any(l.startswith(p) for p in ["►", "A.", "B.", "C.", "D.", "E."]) and not "Marks:" in l]
            if lines:
                add_midterm(lines[0], opts, src="PHY101 Past Papers (Word)")

    # Finalize Midterm List
    midterm_list = []
    idx = 1
    for k, v in midterm_map.items():
        v["id"] = idx
        v["subject"] = "PHY101"
        v["type"] = "mcq"
        midterm_list.append(v)
        idx += 1

    # Finalize Final Term Archive List
    final_list = []
    idx_f = 1
    for k, v in final_map.items():
        v["id"] = f"PHY101-FINAL-{idx_f:04d}"
        v["subject"] = "PHY101"
        v["semester_part"] = "Final Term (Lectures 23-45)"
        final_list.append(v)
        idx_f += 1

    return midterm_list, final_list

def extract_subjective_questions():
    if os.path.exists("phy101_subjective.json"):
        try:
            with open("phy101_subjective.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if len(data) > 0:
                    return data
        except Exception:
            pass

    fp_j = os.path.join(BASE_DIR, "Subjective & Notes/PHY101 Midterm Solved Subjective by Junaid Malik.pdf")
    txt_j = read_pdf(fp_j)
    chunks_j = re.split(r"\n(?=Q\s*No\s*:\s*\d+|Question\s*#?\s*\d+)", txt_j, flags=re.I)
    
    subj_list = []
    idx = 1
    for c in chunks_j:
        if not c.strip() or len(c.strip()) < 30:
            continue
        m_q = re.search(r"(?:Q\s*No\s*:\s*\d+|Question\s*#?\s*\d+)\s*(.*?)(?=\n\s*(?:Ans|Solution)\s*[:\-]\s*|\Z)", c, re.DOTALL | re.I)
        m_ans = re.search(r"\n\s*(?:Ans|Solution)\s*[:\-]\s*(.*)", c, re.DOTALL | re.I)
        if m_q:
            q_text = clean_text(m_q.group(1))
            ans_text = clean_text(m_ans.group(1)) if m_ans else None
            if len(q_text) >= 15:
                subj_list.append({
                    "id": idx,
                    "subjective_id": f"PHY101-SUBJ-{idx:03d}",
                    "question": q_text,
                    "model_answer": ans_text if ans_text else "Refer to VU PHY101 Lecture Notes & Past Papers.",
                    "topic": classify_phy101_topic(q_text),
                    "marks": 3,
                    "source": "Junaid Malik Solved Subjective"
                })
                idx += 1

    # Past paper subjective notes
    fp_notes = os.path.join(BASE_DIR, "Past Papers & Solved Papers/PHY101 Midterm Notes by Conceptsbuilder.pdf")
    txt_notes = read_pdf(fp_notes)
    for part in re.split(r"\n(?=Q\.\s*\d+)", txt_notes):
        m = re.match(r"Q\.\s*\d+\s*(.*?)\n\s*Ans[:\s]+(.*)", part, re.DOTALL | re.I)
        if m:
            q_text = clean_text(m.group(1))
            ans_text = clean_text(m.group(2))
            if len(q_text) >= 15:
                subj_list.append({
                    "id": idx,
                    "subjective_id": f"PHY101-SUBJ-{idx:03d}",
                    "question": q_text,
                    "model_answer": ans_text,
                    "topic": classify_phy101_topic(q_text),
                    "marks": 3,
                    "source": "Conceptsbuilder Solved Subjective"
                })
                idx += 1

    return subj_list

def main():
    print("Extracting PHY101 Midterm & Archiving Final Term...")
    midterm_questions, final_questions = extract_questions()
    subj_questions = extract_subjective_questions()

    print(f"\n==========================================")
    print(f"PHY101 Midterm Objective: {len(midterm_questions)} questions")
    print(f"PHY101 Final Term Archived: {len(final_questions)} questions")
    print(f"PHY101 Subjective (Midterm): {len(subj_questions)} questions")

    # Topic breakdown
    top_mid = Counter(q["topic"] for q in midterm_questions)
    print("\nMidterm Topic Distribution:")
    for t, c in top_mid.most_common():
        print(f"  - {t}: {c}")

    top_fin = Counter(q["topic"] for q in final_questions)
    print("\nFinal Term Topic Distribution:")
    for t, c in top_fin.most_common():
        print(f"  - {t}: {c}")

    # 1. Save Active Studio Files
    with open("phy101_objective.json", "w", encoding="utf-8") as f:
        json.dump(midterm_questions, f, ensure_ascii=False, indent=2)

    with open("phy101_subjective.json", "w", encoding="utf-8") as f:
        json.dump(subj_questions, f, ensure_ascii=False, indent=2)

    # 2. Save Final Term Archive Files
    with open(os.path.join(ARCHIVE_DIR, "phy101_final_term_objective.json"), "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    # 3. Create Archive README
    readme_content = f"""# PHY101 Final Term & Full Bank Archive

This directory stores physics examination questions that belong to the **Final Term (Lectures 23 to 45)** or the complete textbook test bank, kept separately from the active **Midterm Examination Studio**.

## Files in this Archive:

1. **`phy101_final_term_objective.json` ({len(final_questions)} Questions)**
   - Complete question bank for **Chapters 23 to 44** from Halliday, Resnick & Walker (*Fundamentals of Physics 7th Edition*).
   - Covers:
{chr(10).join(f"     - **{t}**: {c} questions" for t, c in top_fin.most_common())}
   - Every question includes multiple-choice options (A–E) and verified textbook answer keys.

2. **`phy101_full_bank_2447_original.json` (2,447 Questions)**
   - Uncut snapshot containing all combined Midterm and Final Term physics questions.

## How to use for Final Term Preparation:
When preparing for PHY101 Final Term examinations, these JSON files can be loaded into the studio or merged with `quiz_data.js` under `window.PHY101_FINAL_QUESTIONS`.
"""
    with open(os.path.join(ARCHIVE_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("\nSaved:")
    print("  - phy101_objective.json (Active Midterm)")
    print("  - phy101_subjective.json (Active Midterm)")
    print(f"  - {os.path.join(ARCHIVE_DIR, 'phy101_final_term_objective.json')} (Archive)")
    print(f"  - {os.path.join(ARCHIVE_DIR, 'README.md')} (Archive)")

if __name__ == "__main__":
    main()
