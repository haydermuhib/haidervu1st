#!/usr/bin/env python3
import json, re

with open("isl202_quiz_bank.json") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} ISL202 questions.")

# Verified solutions dictionary matching normalized question signatures
# For precision, we use key phrases or regex matching to verify each question
VERIFIED_ANSWERS = {
    "severe against disbelievers": ("Sahaba (Companions of the Holy Prophet)", ["Sahaba (Companions of the Holy Prophet)", "Tabe'een", "Muslims", "Saints"]),
    "quroo": ("Purity or impurity", ["Humanity", "All material things", "Purity or impurity", "Beauty"]),
    "following in islam means": ("Emulating the Prophet's (PBUH) actions", ["Imitating social customs", "Emulating the Prophet's (PBUH) actions", "Pursuing material success", "None of the above"]),
    "given a new shariat": ("Rasool", ["Rasool", "Nabi", "Saint", "Rector"]),
    "female is coffined in": ("Five Sheets", ["Eight Sheets", "Five Sheets", "One Sheet", "Ten Sheets"]),
    "indicates the name of": ("Hazrat Zaid", ["Hazrat Usman", "Hazrat Muaaz", "Hazrat Saad", "Hazrat Zaid"]),
    "war against": ("Negators of Zakat", ["Negators of Zakat", "Mushrikeen", "Christians", "Jews"]),
    "abul-qasim al-zahrawi": ("Surgeon", ["Mathematician", "Scholar", "Surgeon", "Physician"]),
    "if the is right then every system": ("Heart", ["Brain", "Heart", "Arms", "Head"]),
    "what happens after death": ("Eternal life in heaven or hell", ["Complete annihilation", "Reincarnation", "Eternal life in heaven or hell", "Temporary oblivion"]),
    "muhammad iqbal, what distinguishes": ("Its external aspects of life", ["Its wealth", "Its external aspects of life", "Its military strength", "Its geographical location"]),
    "main source of islamic jurisprudence": ("The Holy Quran", ["Ijma (Consensus)", "Qiyas (Analogy)", "Hadith (Traditions)", "The Holy Quran"]),
    "best stage of goodness (ihsan)": ("You see Allah and He sees you", ["You see Allah and He sees you", "You see yourself", "Allah sees to prophets", "All of the given options"]),
    "only religion acceptable to allah": ("Islam", ["Christianity", "Judaism", "Hinduism", "Islam"]),
    "inclined towards reconciliation": ("Incline towards reconciliation as well", ["Ignore them", "Oppose them", "Incline towards reconciliation as well", "Convert them to Islam"]),
    "most honorable among people": ("The one who fears Allah the most", ["The wealthiest", "The one who fears Allah the most", "The most educated", "The bravest in battle"]),
    "dead body has been preserved": ("Pharaoh", ["Clergyman", "Pharaoh", "Monk", "Caliph"]),
    "actions that keep away man from allah's love": ("All of the given options", ["Aggression", "Arrogance", "Ungratefulness", "All of the given options"]),
    "al-idrisi is a famous": ("Geographer", ["Physician", "Scholar", "Mathematician", "Geographer"]),
    "al-muqdisi is a famous": ("Geographer", ["Geographer", "Mathematician", "Scholar", "Physician"]),
    "al-qanun fi al-tibb": ("Ibn Sina", ["Ibn Batuta", "Khalaf Abul-Qasim Al-Zahrawi", "Ibn Sina", "Al-Razi"]),
    "al-razi is a famous": ("Physician", ["Geographer", "Mathematician", "Astronomer", "Physician"]),
    "holy prophet (pbuh) was confirmed the miracle of ascension {mi'raj}": ("Hazrat Abu-baker", ["Hazrat Abu-baker", "Hazrat Ommer", "Hazrat Usman", "Hazrat Ali"]),
    "miracle of ascension": ("Hazrat Abu-baker", ["Hazrat Abu-baker", "Hazrat Ommer", "Hazrat Usman", "Hazrat Ali"]),
    "translation of the given verse: (16:44)": ("And We revealed to you the message that you may make clear to the people what was sent down to them", [
        "And We sent down with them the Book and the Balance that men may stand in justice",
        "And We sent down Iron, in which is mighty war and benefits for mankind",
        "And We have already sent down Clear Signs",
        "And We revealed to you the message that you may make clear to the people what was sent down to them"
    ]),
    "condition of the prayer is": ("All of the given options", ["Cleanliness of dress", "Cleanliness of body", "Cleanliness of ground", "All of the given options"]),
    "quality of taqwa": ("All the given options", ["Search", "Seek", "Explore", "All the given options"]),
    "entire structure of religion": ("Rely", ["Confidence", "Assurance", "Rely", "Pledge"]),
    "hearing and obeying are the duties": ("Social reforms", ["To become their king", "Social reforms", "Political reforms", "Gifts"]),
    "fundamental islamic worship": ("Prayer", ["Prayer", "Remembrance", "Charity", "Praise"]),
    "herald the beginning of the life of man": ("Couple", ["Man", "Woman", "Couple", "None of the given options"]),
    "good manners are related to": ("Frequently", ["Frequently", "Intermittently", "From time to time", "Sporadically"]),
    "how does islam view its universality": ("It is a universal religion.", ["It belongs to a specific nation.", "It is a regional religion.", "It is a universal religion.", "It is meant for a particular era."]),
    "how does islamic law view equality": ("All people are equal in the sight of Allah", ["All people are equal in the sight of Allah", "Some people are inherently superior", "Men are superior to women", "Wealthy people are favored"]),
    "how many days hazrat moses stayed on mountain": ("Forty", ["Thirty", "Forty", "Fifty", "Fifty five"]),
    "in how many sections is the bible divided": ("Two", ["Two", "Three", "Four", "Five"]),
    "superior to the whole creations": ("Human Beings", ["Devils", "Jinns", "Human Beings", "Animals"]),
    "creatures are acknowledged as superior": ("Human Beings", ["Devils", "Jinns", "Human Beings", "Animals"]),
    "romans follow": ("Christianity", ["Islam", "Judaism", "Christianity"]),
    "which victory is prophesied?": ("The Conquest of Makka", ["Badar", "The Conquest of Makka", "Tabuk", "Uhud"]),
    "concept of honesty is": ("Wide and Universal", ["Narrow", "Constricted", "Wide and Universal", "Lean"]),
    "mandatory worship": ("Fasting in the month of Ramadan", ["Fasting in the month of Ramadan", "Acts of self sacrifice", "Attending religious gatherings", "Reading the Qur’an"]),
    "qualities of mutteqeen": ("Believe in the unseen", ["Believe in the Abatement", "Believe in the Manifest", "Believe in the Abhor", "Believe in the unseen"]),
    "literal meaning of “imaan”": ("All of the given options", ["Peace", "Calm", "Quiet", "All of the given options"]),
    "longest surah of the holy qur’an": ("Al Baqarah", ["Al Anfaal", "Al Imran", "Al Maidah", "Al Baqarah"]),
    "usher": ("One tenth (1/10)", ["One fifth", "One tenth (1/10)", "One quarter", "One eighth"]),
    "sayi": ("Safa and Marwah", ["Arafat", "Haram", "Safa and Marwah", "Minna"]),
    "how many divine books": ("4", ["3", "4", "5", "6"]),
    "meaning of the term “belief”": ("Approval", ["Approval", "Knotted", "Reality", "Doubt"]),
    "pharaoh was drowned during the prophethood of": ("Hazrat Musa (A.S)", ["Hazrat Esa (A.S)", "Hazrat Ibrahim (A.S)", "Hazrat Younus (A.S)", "Hazrat Musa (A.S)"]),
    "verse predicts that pharaoh's body is": ("Safe", ["Disappeared", "Safe", "Buried", "Drowned"]),
    "what is prophesied in the following verse?": ("The Romans will prevail", ["The Conquest of Makkah", "The Persians will prevail", "The Romans will be defeated", "The Romans will prevail"]),
    "role assigned to hazrat israfeel": ("Blow the trumpet", ["Control death", "Help People", "Blow the trumpet", "Send rain and food"]),
    "longest surah of the holy qur": ("Al Baqarah", ["Al Anfaal", "Al Baqarah", "Al Imran", "Al Maidah"]),
    "core belief of divine": ("Oneness of Almighty Allah (Tauheed)", ["Day of Judgment", "Prophethood", "Angels", "Oneness of Almighty Allah (Tauheed)"]),
    "meaning of respect is": ("Fear and awful", ["Fear and collective", "Fear and awful", "Fear and appalling"]),
    "mizan": ("The scale", ["The place", "The scale", "The bridge", "The book"]),
    "meaning of the word “ ”میزان": ("Scale", ["Heart", "Scale", "Tongue", "Eye"]),
    "meaning of the word “ ”میزانis": ("Scale", ["Heart", "Scale", "Tongue", "Eye"]),
    "handful of dust/soil on disbelievers": ("Badar", ["Badar", "Uhad", "Tabook", "Khyber"]),
    "muslims migrated to": ("Abyssinia (Habsha)", ["Yaman", "Iran", "Abyssinia (Habsha)", "Taif"]),
    "namaz-e-istisqa": ("Rain", ["Blessing of God", "Pardon", "Rain", "Sleep"]),
    "mountains where hazrat abraham left his wife": ("Safa and Marwa", ["Safa and Uhad", "Safa and Marwa", "Safa and Jabl-e-Noor", "Safa and Toor"]),
    "obedience in islam refers to": ("Following the commands and sayings of the Prophet (PBUH)", ["Following social customs", "Following the commands and sayings of the Prophet (PBUH)", "Obeying one's desires", "None of the above"]),
    "obedience of allah is not possible without": ("Muhammad (PBUH)", ["Quran", "Muhammad (PBUH)", "Hazrat Abraham", "Hazrat Jesus"]),
    "mountain hazrat moses stayed": ("Toor", ["Safa", "Marwa", "Uhad", "Toor"]),
    "overspending on necessities": ("Tabzeer", ["Falah", "Iqtasad", "Tabzeer", "Israf"]),
    "holy quran aims to create an ideal soc": ("Entire humanity", ["Muslims", "Entire humanity", "Christianity", "Jews"]),
    "truthful and able to be trusted": ("Honesty", ["Uprightness", "Dedication", "Honesty", "Peacefulness"]),
    "religion is a ________ matter in non islamic system": ("Private", ["Social", "Civil", "Private", "Public"]),
    "respect of parents is an order of": ("Quran", ["Quran", "Hadith", "Fiqh", "Qiyas"]),
    "sadaq-e-eid-ul-fitr has been proclaimed": ("2 Hijri", ["1 Hijri", "2 Hijri", "3 Hijri", "4 Hijri"]),
    "conjecture": ("Therefore, shun those who turn away from Our message and desire nothing but the life of this world", [
        "But they have no knowledge therein. They follow nothing but conjecture",
        "Bring then ten forged Chapters like this",
        "Therefore, shun those who turn away from Our message and desire nothing but the life of this world",
        "Let them then produce a recital like unto it"
    ]),
    "single-minded devotion": ("Inner reality", ["Inner reality", "Outer reality", "World reality", "All of the given options"]),
    "war between rome and persia were with": ("The polytheists of Makkah", ["Christians", "Jews", "The polytheists of Makkah", "Muslims"]),
    "prophet muhamamd (pbuh) was born in": ("571 A.D.", ["570 A.D.", "571 A.D.", "572 A.D.", "575 A.D."]),
    "may his _______ rubbed in dust": ("Nose", ["Hand", "Forehead", "Nose", "Foot"]),
    "hypocrites shall be cast into the": ("Lowest", ["Upper", "Medium", "Lowest", "None of the given options"]),
    "hypocrite shall be cast into the level of the hell": ("Lowest", ["Upper", "Medium", "Lowest", "None of the given options"]),
    "nisab of zakat in gold": ("7 1/2 Tolas", ["5 1/2 Tolas", "7 1/2 Tolas", "10 Tolas", "52 1/2 Tolas"]),
    "governor of": ("Yaman", ["Kufa", "Makkah", "Medina", "Yaman"]),
    "zakat levied on agriculture": ("Ushr", ["Ushoor", "Ushr", "Ashroon", "None of the given options"]),
    "address of holy prophet muhammad (pbuh) given in quba": ("Medium", ["Shortest", "Medium", "Longest", "All the given options"]),
    "coolness of my eyes lies in salat": ("Prophet (S.A.W)", ["Prophet (S.A.W)", "Hazrat Abu Bakar R.A", "Hazrat Umer Farooq R.A", "Hazrat Ali R.A"]),
    "effective zakat system can ensure the elimination of": ("Poverty", ["Poverty", "Interest", "Class Distinction", "Ignorance"]),
    "expiation of fasting involves feeding the miskeen": ("One (per day missed)", ["One (per day missed)", "Two", "Three", "Four"]),
    "famous revealed books are": ("All of the given options", ["Quran", "Torah", "Zabur", "Injil", "All of the given options"]),
    "first duty of a man is": ("Believe in Allah", ["Believe in Allah", "Learning", "Teaching", "All of the given options"]),
    "first revelation to holy prophet muhammad (pbuh) showed": ("Knowledge", ["Morality", "Knowledge", "Taqwa", "Sincerity"]),
    "saum": ("To stop / abstain", ["To find", "To start", "To stop / abstain", "To be hungry"]),
    "literal meaning of \"saum": ("To stop / abstain", ["To find", "To start", "To stop / abstain", "To be hungry"]),
    "funny talks and jokes": ("Prohibited (in excess)", ["Permitted", "Rewarded", "Prohibited (in excess)", "Cause of goodness"]),
    "sent as a messenger": ("To the whole world", ["To a particular nation", "To a specific region", "To the whole world", "To the Arab tribes"]),
    "companions of the prophet known for": ("Teaching and spreading its knowledge", ["Writing it", "Teaching and spreading its knowledge", "Memorizing it only", "None of the above"]),
    "characteristics of \"angels": ("Innocent", ["Attractive", "Innocent", "Intelligent", "Immortal"]),
    "main sources of islamic law": ("The Quran and Sunnah", ["The Bible and the Torah", "The Quran and Sunnah", "The Vedas and Upanishads", "Civil laws"]),
    "principles of nature": ("Based on the principles of nature", ["Based on customs and traditions", "Based on the principles of nature", "Temporary and adaptable", "Rigid and complex"]),
    "what is ijtihad in islamic law": ("The process of making a legal decision by independent interpretation", ["A form of charity", "The process of making a legal decision by independent interpretation", "A type of prayer", "A ritual pilgrimage"]),
    "sahihain": ("Bukhari and Muslim", ["Mishkat", "Bukhari", "Bukhari and Muslim", "Abu Dawood and Tirmidhi"]),
    "duties assigned to the \"angels": ("To Provide guidance / Carry out divine orders", ["To Provide guidance / Carry out divine orders", "To preach people", "To help people", "To punish humans"]),
    "testimony of faith": ("Shahada", ["Zakat", "Salat", "Shahada", "Sawm"]),
    "distinguishes it from other religions": ("Belief in one God (Tawhid)", ["Belief in many gods", "Belief in one God (Tawhid)", "Belief in reincarnation", "Denial of prophets"]),
    "meaning of \"malak\"": ("Messenger", ["Judge", "Helper", "Messenger", "Ruler"]),
    "first part of the bible": ("The Old Testament", ["The New Testament", "The Old Testament", "The Books of Prophets", "The Gospels"]),
    "address of holy prophet muhammad (pbuh) given on the occasion of hajj": ("Khutba Hajjat-ul-Wida", ["Khutba Taqwa", "Khutba Hajjat-ul-Wida", "Khutba Rasool", "None of the given options"]),
    "tubewell": ("1/20 (5%)", ["1/20 (5%)", "1/5 (20%)", "1/10 (10%)", "1/15"]),
    "ratio of ushr on the land which is irrigated": ("1/20 (5%)", ["1/20 (5%)", "1/5 (20%)", "1/10 (10%)", "1/15"]),
    "nakirayn": ("Ask questions in the grave", ["Help People", "Ask questions in the grave", "Blow the trumpet", "Control death"]),
    "significance of the kaaba": ("It is the direction Muslims face during prayer", ["It is a place for animal sacrifices", "It is the direction Muslims face during prayer", "It is a burial site for prophets", "It is the place where the Quran was revealed"]),
    "night journey of the prophet muhammad": ("Isra and Mi'raj", ["Hajj", "Isra and Mi'raj", "Ramadan", "Yawm al-Qiyamah"]),
    "what we plant here will be harvested on the day of": ("Judgment", ["Jihad", "Arafaat", "Eid", "Judgment"]),
    "second trumpet": ("Resurrected", ["Brought", "Slept", "Resurrected", "Threatened"]),
    "reference indicates that prophet muhammad (pbuh) was sent": ("Sahih Bukhari, 335", ["Sahih Bukhari, 335", "Sahih Muslim, 245", "Sunan Abu Dawood, 412", "Jami` at-Tirmidhi, 55"]),
    "kalimullah": ("Hazrat Musa A.S", ["Hazrat Musa A.S", "Hazrat Esa A.S", "Hazrat Dawood A.S", "Hazrat Muhammad PBUH"]),
    "title and position of kalimullah": ("Hazrat Musa A.S", ["Hazrat Musa A.S", "Hazrat Esa A.S", "Hazrat Dawood A.S", "Hazrat Muhammad PBUH"]),
    "delivered revelations to the prophets": ("Gabriel (Jibreel)", ["Michael", "Raphael", "Gabriel (Jibreel)", "Azrael"]),
    "delivered revelations": ("Gabriel (Jibreel)", ["Michael", "Raphael", "Gabriel (Jibreel)", "Azrael"]),
    "battle is predicted to be a victory": ("Badar", ["The Conquest of Khyber", "Uhud", "The Conquest of Makka", "Badar"]),
    "most comprehensive": ("Qur'an", ["Qur'an", "Zubur", "Torah", "Injil"]),
    "mandatory act of worship is referred to in the following verse": ("Salat", ["Salat", "Zakah", "Saum"]),
    "not a duty of the holy prophet": ("Lead wars", ["Teach the Book", "Teach wisdom", "Purify hearts", "Lead wars"]),
    "literal meaning of the holy quran": ("Collect", ["Advice", "Approach", "Collect", "Meet"]),
    "peace, harmony, and security": ("Salam", ["Zakat", "Salam", "Hajj", "Sawm"]),
    "composed first": ("Tafseer al-Tabari", ["Tafseer al-Kabeer", "Tafseer al-Tabari", "Tafseer Ibn Kathir", "Tafseer al-Naeemi"]),
    "fifth for exegesis (tafseer)": ("Arabic Language", ["The Sayings of the Companions and their Followers", "The Principles of Shari'ah", "Ahadith of the Prophet (PBUH)", "Arabic Language"]),
    "second for exegesis (tafseer)": ("Hadith", ["Hadith", "Holy Qur’an", "Previous Divine Books", "Arabic dictionary"]),
    "prophet left his wife in desert": ("Hazrat Abraham", ["Hazrat Moses", "Hazrat Jesus", "Hazrat Abraham", "Hazrat Abu Bakar"]),
    "one third of the holy quran": ("Al-Ikhlas", ["Al-Fateha", "Al-Kousar", "Al-Ikhlas", "Al-Qadar"]),
    "common cause in islamic legal reasoning": ("Qiyas", ["Qiyas", "Ijma", "Illat", "Fatwa"]),
    "enter islam perfectly": ("Al-Baqarah, 2:208", ["Al-Baqarah, 2:208", "Aal-e-Imran, 3:19", "Al-Anfal, 8:61", "Al-Nisa, 4:34"]),
    "people of the book": ("Christians and Jews", ["Christians and Jews", "Hindus and Buddhists", "Atheists and Agnostics", "Sikhs and Jains"]),
    "who can perform ijtihad": ("A Mujtahid with specific qualifications", ["Any Muslim", "A Mujtahid with specific qualifications", "Only the Prophet (PBUH)", "Anyone with basic knowledge of Islam"]),
    "final prophet": ("Muhammad", ["Moses", "Jesus", "Muhammad", "Abraham"]),
    "run between the mountains in search of water": ("Hazrat Hajra", ["Hazrat Hajra", "Hazrat Saira", "Hazrat Asia", "Hazrat Ayesha"]),
    "disciple of hazrat ubayy bin ka'b": ("Zaid bin Aslam R.A", ["Zaid bin Ali R.A", "Zaid bin Aslam R.A", "Zaid bin Harith R.A", "Zaid bin Sabit R.A"]),
    "mafateeh al-ghaib": ("Allama Fakhruddin al-Razi", ["Allama Ismaeel bin Umar Kathir", "Allama Muhammad bin Ahmad al-Ghazali", "Allama Fakhruddin al-Razi", "Allama Jalaluddin al-Sayyuti"]),
    "control over the air": ("Hazrat Suleiman", ["Hazrat Abraham", "Hazrat Adam", "Hazrat Daood", "Hazrat Suleiman"]),
    "write whatever muhammad (pbuh) said": ("Hazrat Abdullah bin Umar bin Alaas", ["Hazrat Abdullah bin Abbas", "Hazrat Abdullah bin Umar bin Alaas", "Hazrat Abdullah bin Masood", "Hazrat Abdullah bin Zubair"]),
    "comprehensive surah on islamic social system": ("Al-Asar", ["Al-Nasar", "Al-Asar", "Al-Qadar", "Al-Takasar"]),
    "one of the worst habits": ("Backbiting", ["Proud", "Sake of fun", "Backbiting", "All of the given options"]),
    "forbearance, fear and abstinence": ("Taqwa", ["Justice", "Ethics", "Morality", "Taqwa"]),
    "fourth kalimah": ("Kalimah Tauheed", ["Kalimah Tauheed", "Kalimah Risalat", "Kalimah Tamjeed", "Kalimah Shahadat"]),
    "ordered to divorce his wife": ("Abdullah bin Umar", ["Abdullah bin Umar", "Hazrat Hussain", "Souban", "Ibn-i-Abbas"]),
    "first person who confirmed the miracle of ascension": ("Hazrat Abu-baker", ["Hazrat Abu-baker", "Hazrat Ommer", "Hazrat Usman", "Hazrat Ali"]),
    "kitab-al-umm": ("Imam Shafi", ["Abu Hanifa", "Imam Malik", "Imam Shafi", "Ahmad bin Hanbal"]),
    "goodness towards his parents": ("Divine order", ["Divine order", "Hadith", "Saying of Hazrat Abu-bakar", "Saying of Hazrat Umar"]),
    "obey me as long as i obey allah": ("Hazrat Abu Bakar", ["Hazrat Abu Bakar", "Hazrat Ommer", "Hazrat Usman", "Hazrat Ali"])
}

from audit_and_fix_isl202 import split_camel_or_merged

fixed_count = 0
for idx, q in enumerate(questions):
    qtext = q.get("question", "").strip()
    raw_opts = q.get("options", [])
    raw_ans = q.get("answer")
    
    # Check if opts is compressed into one string like ['ptions:A,B,C', 'CorrectOption:B']
    new_opts = []
    embedded_correct = None
    for o in raw_opts:
        if "CorrectOption:" in o or "Answer:" in o:
            m = re.search(r'(?:CorrectOption|Answer)\s*[:\.]\s*(?:[a-dA-D][\)\.\:]\s*)?(.*)', o, re.I)
            if m:
                embedded_correct = m.group(1).strip()
        elif "ptions:" in o:
            parts = o.replace("ptions:", "").split(",")
            for p in parts:
                cleaned_p = split_camel_or_merged(p)
                if cleaned_p and cleaned_p not in new_opts:
                    new_opts.append(cleaned_p)
        else:
            # Check if option is an answer tag
            if re.match(r'^Answer\s*[:\.]', o, re.I):
                m = re.search(r'Answer\s*[:\.]\s*(?:[a-dA-D][\)\.\:]\s*)?(.*)', o, re.I)
                if m:
                    embedded_correct = m.group(1).strip()
            else:
                cleaned_o = split_camel_or_merged(o)
                if cleaned_o and cleaned_o not in new_opts:
                    new_opts.append(cleaned_o)
                    
    # Clean qtext of watermarks and numbers
    qtext = re.sub(r'Learning With Mickey ch.*', '', qtext, flags=re.I).strip()
    qtext = re.sub(r'0328-4090195.*', '', qtext).strip()
    qtext = re.sub(r'MCQ:\s*', '', qtext, flags=re.I).strip()
    qtext = re.sub(r'IdeasChoose', 'Choose', qtext, flags=re.I).strip()
    qtext = re.sub(r'Please choose one', '', qtext, flags=re.I).strip()
    qtext = re.sub(r'^\s*[\.\:\-\_]+\s*', '', qtext).strip()
    q["question"] = qtext
    
    # Try to match from VERIFIED_ANSWERS
    matched_verified = False
    norm_q = qtext.lower()
    for k, v in VERIFIED_ANSWERS.items():
        if k in norm_q:
            best_ans, canonical_opts = v
            # If canonical_opts given, ensure they are present
            if len(new_opts) < 2:
                new_opts = canonical_opts
            # Standardize answer text
            q["answer"] = best_ans
            # Make sure best_ans is in new_opts
            if not any(best_ans.lower() == opt.lower() or opt.lower() in best_ans.lower() or best_ans.lower() in opt.lower() for opt in new_opts):
                new_opts.append(best_ans)
            else:
                # canonicalize to match exactly one option
                for i_o, opt in enumerate(new_opts):
                    if opt.lower() == best_ans.lower() or best_ans.lower() in opt.lower():
                        q["answer"] = opt
                        break
            matched_verified = True
            break
            
    if not matched_verified:
        # Check embedded correct
        if embedded_correct:
            cand = split_camel_or_merged(embedded_correct)
            for opt in new_opts:
                if cand.lower() == opt.lower() or cand.lower() in opt.lower() or opt.lower() in cand.lower():
                    q["answer"] = opt
                    matched_verified = True
                    break
            if not matched_verified:
                new_opts.append(cand)
                q["answer"] = cand
                matched_verified = True
        elif raw_ans:
            clean_raw = split_camel_or_merged(raw_ans)
            matched = False
            for opt in new_opts:
                if clean_raw.lower() == opt.lower() or clean_raw.lower() in opt.lower():
                    q["answer"] = opt
                    matched = True
                    break
            if not matched:
                new_opts.append(clean_raw)
                q["answer"] = clean_raw
        else:
            # Fallback if any option has (correct) or similar
            for opt in new_opts:
                if "correct" in opt.lower():
                    q["answer"] = opt
                    break

    q["options"] = new_opts
    if q.get("answer"):
        fixed_count += 1

print(f"Verified & Resolved: {fixed_count} / {len(questions)} ISL202 questions!")

# Check any remaining without answer
unresolved = [q for q in questions if not q.get("answer") or q.get("answer") not in q.get("options", [])]
print(f"Remaining unresolved ISL202 questions: {len(unresolved)}")
for u in unresolved[:10]:
    print("Q:", u["question"][:65])
    print("Opts:", u["options"])
    print("Ans:", u.get("answer"))
    print("---")

