#!/usr/bin/env python3
"""
Master Audit & Correction Engine for ISL202 (Islamic Studies) Quiz Bank & Subjective Bank.
Authored by Senior Subject Matter Expert Auditor for Islamic Studies.
"""
import json, re

# Load files
with open('isl202_quiz_bank.json') as f:
    questions = json.load(f)

with open('subjective_bank.json') as f:
    subj_data = json.load(f)

print(f"Loaded {len(questions)} MCQs and {len(subj_data.get('ISL202', []))} subjective questions.")

# 1. Clean merged words dictionary
CLEAN_PHRASES = {
    'AchapterintheQuran': 'A chapter in the Quran',
    'Actionsandactivities': 'Actions and activities',
    'Actionsandbattles': 'Actions and battles',
    'Actionsandsayings': 'Actions and sayings',
    'Actionsandworship': 'Actions and worship',
    'AftertheagreementofHudabiya': 'After the agreement of Hudabiya',
    'AfterthebattleofBadar': 'After the battle of Badar',
    'AfterthebattleofUhad': 'After the battle of Uhad',
    'AfterthevictoryofMakkah': 'After the victory of Makkah',
    'AlAzharUniversity': 'Al-Azhar University',
    'AllahandHisProphet': 'Allah and His Prophet',
    'Allahandexecutiveauthority': 'Allah and executive authority',
    'Allahandangels': 'Allah and angels',
    'Allahandsaints': 'Allah and saints',
    'AllamIsmaeelbinUmarKatheer': 'Allama Ismaeel bin Umar Kathir',
    'AllhumansareequalinthesightofAllah': 'All humans are equal in the sight of Allah',
    'Allofgivenoption': 'All of the given options',
    'Allofthegivenoption': 'All of the given options',
    'Allreligioustextsshouldbeinterpretedinthesameway': 'All religious texts should be interpreted in the same way',
    'Allthegivenoption': 'All of the given options',
    'Allthegivenoptions': 'All of the given options',
    'Alloptions': 'All of the given options',
    'Architecturalstyles': 'Architectural styles',
    'AscribingpartnerswithAllah': 'Ascribing partners with Allah (Shirk)',
    'AspecificIslamicdynasty': 'A specific Islamic dynasty',
    'Avoidinghardship': 'Avoiding hardship',
    'Awareofissuesonwhichconsensushasbeendone': 'Aware of issues on which consensus has been done',
    'Backbitingandquarreling': 'Backbiting and quarreling',
    'Basedoncustomsandtraditions': 'Based on customs and traditions',
    'Basedontheprinciplesofnature': 'Based on the principles of nature',
    'BeliefinDayofJudgment': 'Belief in Day of Judgment',
    'BeliefinMessengers': 'Belief in Messengers',
    'BeliefinProphets': 'Belief in Prophets',
    'Beliefinaholytrinity': 'Belief in a holy trinity',
    'Beliefinmanygods': 'Belief in many gods',
    'Beliefinreincarnation': 'Belief in reincarnation',
    'BeliefinAllah': 'Belief in Allah',
    'BeliefinAngels': 'Belief in Angels',
    'BeliefinDestiny': 'Belief in Destiny',
    'BolognaUniversity': 'Bologna University',
    'Bothmeanthesamething': 'Both mean the same thing',
    'BukhariandMuslim': 'Bukhari and Muslim',
    'ClassDistinction': 'Class distinction',
    'Comprehensiveness': 'Comprehensiveness',
    'ContentmentandCarelessness': 'Contentment and Carelessness',
    'ContentmentandPersonalintegrity': 'Contentment and Personal integrity',
    'Contentmentandenjoyment': 'Contentment and enjoyment',
    'Contentmentandheedlessness': 'Contentment and heedlessness',
    'Controloftemperament': 'Control of temperament',
    'Culturalpractices': 'Cultural practices',
    'DarulUloomDeoband': 'Darul Uloom Deoband',
    'Desireformaterialsuccess': 'Desire for material success',
    'Disobedienceofparents': 'Disobedience of parents',
    'Donoteatthemealtopoor': 'Do not feed the poor',
    'Easingoflawstopreventhardship': 'Easing of laws to prevent hardship',
    'Eatinganddrinking': 'Eating and drinking',
    'Economicpolicies': 'Economic policies',
    'Efforttointerpretreligiousissues': 'Effort to interpret religious issues',
    'Encouragingasceticism': 'Encouraging asceticism',
    'Ensuringjusticeandfairnessinsociety': 'Ensuring justice and fairness in society',
    'Ethicalstandards': 'Ethical standards',
    'ExpertinArabiclanguage': 'Expert in Arabic language',
    'FabricatedHadith': 'Fabricated Hadith (Mawdu)',
    'Fearlessnessofdeath': 'Fearlessness of death',
    'FleeingfromJihad': 'Fleeing from Jihad',
    'Followingpreviousscholarsblindly': 'Following previous scholars blindly',
    'Followingsocialcustoms': 'Following social customs',
    'Followtheprophets': 'Follow the prophets',
    'FollowtheSunnah': 'Follow the Sunnah',
    'Freedomandequality': 'Freedom and equality',
    'Hardshipordifficulty': 'Hardship or difficulty',
    'HazratAbdulUtbah': 'Hazrat Abdul Utbah',
    'HazratAbdullahbinMasood': 'Hazrat Abdullah bin Masood',
    'HazratJafarTayyar': 'Hazrat Jafar Tayyar',
    'ImamAhmadbinHunbal': 'Imam Ahmad bin Hanbal',
    'Increasedpoverty': 'Increased poverty',
    'Indifferencetowealth': 'Indifference to wealth',
    'IslamiclawderivedfromtheQuranandHadith': 'Islamic law derived from the Quran and Hadith',
    'Islamicmysticism': 'Islamic mysticism',
    'Islamicphilosophy': 'Islamic philosophy',
    'IstanbulUniversity': 'Istanbul University',
    'ItcelebratesthebirthoftheProphetMuhammad': 'It celebrates the birth of the Prophet Muhammad',
    'ItcommemoratesthefirstrevelationoftheQuran': 'It commemorates the first revelation of the Quran',
    'ItdeterminesthelengthoftheHadith': 'It determines the length of the Hadith',
    'ItensurestheauthenticityoftheHadith': 'It ensures the authenticity of the Hadith',
    'ItexplainsthemeaningoftheHadith': 'It explains the meaning of the Hadith',
    'Itisadayforcelebratingcreation': 'It is a day for celebrating creation',
    'Itisthedaywhenallbeingswillbejudgedfortheirdeeds': 'It is the day when all beings will be judged for their deeds',
    'ItmarksthebeginningoftheIslamiccalendar': 'It marks the beginning of the Islamic calendar',
    'Itmarksthebeginningoftheuniverse': 'It marks the beginning of the universe',
    'ItprovidescontextfortheHadith': 'It provides context for the Hadith',
    'Itsfocusonrituals': 'Its focus on rituals',
    'Itshistoricalbackground': 'Its historical background',
    'ItsignifiesthecompletionoftheQuran': 'It signifies the completion of the Quran',
    'Itsprinciplesofnatureandflexiblelaws': 'Its principles of nature and flexible laws',
    'Justiceshouldbeupheldwithoutcausingunnecessaryhardship': 'Justice should be upheld without causing unnecessary hardship',
    'Knowledgeandwisdom': 'Knowledge and wisdom',
    'Lazyinofferingprayer': 'Lazy in offering prayer',
    'Lazyinofferingprayeranddonoteatthemealtopoor': 'Lazy in offering prayer and do not feed the poor',
    'Loveandcompassion': 'Love and compassion',
    'Memorizingitonly': 'Memorizing it only',
    'Menandwomenshouldhaveequalrolesinsociety': 'Men and women should have equal roles in society',
    'MuhammadbinIsmail': 'Muhammad bin Ismail',
    'OnenessofAlmightyAllah': 'Oneness of Almighty Allah (Tauheed)',
    'nenessofAllah': 'Oneness of Allah (Tauheed)',
    'Politicaldominance': 'Political dominance',
    'Politicalreforms': 'Political reforms',
    'RasheedAhmadRaza': 'Rasheed Ahmad Raza',
    'RecitationofHolyQuran': 'Recitation of Holy Quran',
    'SafaandJableNoor': 'Safa and Jabal-e-Noor',
    'SafaandMarwa': 'Safa and Marwa',
    'SafaandTour': 'Safa and Toor',
    'SafaandUhad': 'Safa and Uhud',
    'Similarityininnerandouterself': 'Similarity in inner and outer self',
    'Slavegivingbirthtohermistress': 'Slave giving birth to her mistress',
    'Socialstratification': 'Social stratification',
    'SoundorauthenticHadith': 'Sound or authentic Hadith (Sahih)',
    'Spiritualdestiny': 'Spiritual destiny',
    'Spiritualpurification': 'Spiritual purification',
    'Strengthandpower': 'Strength and power',
    'Strictlyprohibited': 'Strictly prohibited',
    'Taqwaanddisobedience': 'Taqwa and disobedience (Fajur)',
    'Taqwaandobedience': 'Taqwa and obedience',
    'Taqwaandreliability': 'Taqwa and reliability',
    'Teachingandspreadingitsknowledge': 'Teaching and spreading its knowledge',
    'Technologicaladvancement': 'Technological advancement',
    'Temporaryandadaptable': 'Temporary and adaptable',
    'TheBibleandtheTorah': 'The Bible and the Torah',
    'TheBooksofProphets': 'The Books of Prophets',
    'TheConquestofMakkah': 'The Conquest of Makkah',
    'TheConstitutionandcommonlaw': 'The Constitution and common law',
    'TheIslamiccommunityworldwide': 'The Islamic community worldwide',
    'ThePersianswillprevail': 'The Persians will prevail',
    'TheQuranandSunnah': 'The Quran and Sunnah',
    'TheRomanswillbedefeated': 'The Romans will be defeated',
    'TheRomanswillprevail': 'The Romans will prevail',
    'TheVedasandUpanishads': 'The Vedas and Upanishads',
    'Thecommoncausebetweenoriginalandinferredrulings': 'The common cause between original and inferred rulings',
    'Thedesiredordercombiningthebranchwiththeoriginal': 'The desired order combining the branch with the original',
    'ThelanguageofHadith': 'The language of Hadith',
    'TheoriginaltextofHadith': 'The original text of Hadith',
    'ThepolytheistsofMakkah': 'The polytheists of Makkah',
    'Thepracticeoffasting': 'The practice of fasting',
    'Theprocessofmakingalegaldecisionbyindependentinterpretation': 'The process of making a legal decision by independent interpretation',
    'TherulingofpastMujtahids': 'The ruling of past Mujtahids',
    'ThesayingsandactionsoftheProphetMuhammad': 'The sayings and actions of the Prophet Muhammad',
    'ThesunwillrisefromtheEast': 'The sun will rise from the East',
    'ThesunwillrisefromtheNorth': 'The sun will rise from the North',
    'ThesunwillrisefromtheSouth': 'The sun will rise from the South',
    'Thesunwillrisefromthewest': 'The sun will rise from the West',
    'Theverdictgivenforaspecificissue': 'The verdict given for a specific issue',
    'Theyarecompletelyunrelated': 'They are completely unrelated',
    'ToProvideguidance': 'To provide guidance / Carry out divine orders',
    'Toaparticularnation': 'To a particular nation',
    'Toaspecificregion': 'To a specific region',
    'Tobecometheirking': 'To become their king',
    'Tocelebrateharvest': 'To celebrate harvest',
    'TocommemoratethefirstrevelationoftheQuran': 'To commemorate the first revelation of the Quran',
    'Tocomparewithotherreligioustexts': 'To compare with other religious texts',
    'Todiscardoldtexts': 'To discard old texts',
    'TodocumentthehistoryofIslam': 'To document the history of Islam',
    'Toeliminatethesocietyfromtheevils': 'To eliminate the society from the evils',
    'ToensuretheimplementationoftheSharia': 'To ensure the implementation of the Sharia',
    'Toestablishastableeconomicsystem': 'To establish a stable economic system',
    'Tofulfillhumanrights': 'To fulfill human rights',
    'TohonorthebirthoftheProphetMuhammad': 'To honor the birth of the Prophet Muhammad',
    'TomarkthebeginningoftheIslamicnewyear': 'To mark the beginning of the Islamic new year',
    'TorewritetheQuran': 'To rewrite the Quran',
    'Toteachrevelation': 'To teach revelation',
    'TounderstandandapplytheteachingsoftheProphet': 'To understand and apply the teachings of the Prophet',
    'Unawareoftheabrogationofcommands': 'Unaware of the abrogation of commands',
    'Uprightfortuousness': 'Uprightness',
    'Wealthaccumulation': 'Wealth accumulation',
    'Wealthdeterminessuperiority': 'Wealth determines superiority',
    'Wealthshouldbedistributedequallyamongallpeople': 'Wealth should be distributed equally among all people',
    'WellversedinQuranandSunnah': 'Well versed in Quran and Sunnah',
    'WorshipingGodasthoughyouseeHim': 'Worshiping God as though you see Him',
    'Worshipofprophets': 'Worship of prophets',
    'WorshipofAllah': 'Worship of Allah',
    'bedienceandsubmission': 'Obedience and submission',
    'nlymenaresuperior': 'Only men are superior',
    'nceinalife': 'Once in a life',
    'Twiceinalife': 'Twice in a life',
    'Thriceinalife': 'Thrice in a life',
    'Heartandsoul': 'Heart and soul',
    'Tenyears': 'Ten years',
    'Elevenyears': 'Eleven years',
    'Twelveyears': 'Twelve years',
    'Thirteenyears': 'Thirteen years',
    'ThirtyYears': 'Thirty Years',
    'EighteenYears': 'Eighteen Years',
    'TwentyYears': 'Twenty Years',
    'FiveYears': 'Five Years',
    'Tobepurified': 'To be purified',
    'Toberefined': 'To be refined',
    'Tobepolished': 'To be polished',
    'SafaandMarwah': 'Safa and Marwah',
    'Minavalley': 'Mina valley',
    'Muzdalifavalley': 'Muzdalifa valley',
    'Areaandcountry': 'Area and country',
    'Areaandassets': 'Area and assets',
    'Areaandregion': 'Area and region',
    'Areaandestate': 'Area and estate',
    'SaadBinAbiwaqas': 'Saad Bin Abi Waqas (RA)',
    'SaadBinUbaid': 'Saad Bin Ubaid (RA)',
    'SaadbinAbada': 'Saad Bin Ubada (RA)',
    'HazratHamza': 'Hazrat Hamza (RA)',
    'AbbasidPeriod': 'Abbasid Period',
    'UmmayadDynasty': 'Umayyad Dynasty',
    'Hisownself': 'His own self',
    'Noneofthese': 'None of these',
    'Alloptions': 'All of the given options',
    'Prophet(S.A.W)': 'Prophet Muhammad (PBUH)',
    'HazratAbuBakarR.A': 'Hazrat Abu Bakar (RA)',
    'HazratUmerFarooqR.A': 'Hazrat Umar Farooq (RA)',
    'HazratAliR.A': 'Hazrat Ali (RA)',
    'Islam,Christianity,Judaism': 'Islam, Christianity, Judaism',
    'Hinduism,Islam,Christianity': 'Hinduism, Islam, Christianity',
    'Judaism,Islam,Hinduism': 'Judaism, Islam, Hinduism',
    'Judaism,Christianity,Hinduism': 'Judaism, Christianity, Hinduism'
}

def clean_text_str(s):
    if not s: return ""
    s = s.strip()
    if s in CLEAN_PHRASES:
        return CLEAN_PHRASES[s]
    # Check camelCase
    s_cleaned = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    s_cleaned = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s_cleaned)
    return s_cleaned.strip()

# Explicit master verification overrides by ID
OVERRIDES = {
    29: {
        "answer": "All of the given options",
        "options": ["Authority", "Sustainer", "Creator", "All of the given options"],
        "notes": "According to the Quranic doctrine of Tawhid, Allah alone is the Creator (Khaliq), Sustainer (Razzaq), and ultimate Sovereign Authority (Malik) of the universe."
    },
    30: {
        "answer": "Allah and His Prophet",
        "options": ["Allah and angels", "Allah and His Prophet", "Allah and executive authority", "Allah and saints"],
        "notes": "Surah An-Nisa (4:59): 'And if you dispute over anything, refer it to Allah and the Messenger, if you should believe in Allah and the Last Day.'"
    },
    43: {
        "answer": "Seek",
        "options": ["Neglect", "Seek", "Demolish", "All of the given options"],
        "notes": "Taqwa inspires believers to actively search for and seek out righteous actions and virtues, while abstaining from evil."
    },
    46: {
        "question": "The delegation of Quraish offered what to the King of Abyssinia (Negus)?",
        "answer": "Gifts",
        "options": ["To become their king", "Social reforms", "Political reforms", "Gifts"],
        "notes": "Historical Seerah (Ibn Hisham): The Quraish delegation led by Amr ibn al-Aas brought luxurious gifts of leather and merchandise to the Negus to induce him to hand over Muslim refugees."
    },
    51: {
        "answer": "9th Zil Hajjah",
        "options": ["2nd Safar", "3rd Ramadan", "1st Shawwal", "9th Zil Hajjah"],
        "notes": "Wuquf-e-Arafat, the central pillar of Hajj ('Al-Hajj Arafah'), occurs on the 9th day of Zil Hajjah."
    },
    56: {
        "answer": "Once in a life",
        "options": ["Once in a life", "Twice in a life", "Thrice in a life", "None of the given options"],
        "notes": "Hajj is Fard once in a lifetime for every Muslim who is physically and financially capable (Sahih Muslim 1337)."
    },
    58: {
        "answer": "Sahifa al Sahiha",
        "options": ["Sahifa al Sahiha", "Sahifa al Muhammadiyyah", "Sahifa al Sadiqa", "Sahifa al Jamia"],
        "notes": "Hammam ibn Munabbih compiled 'Al-Sahifah al-Sahiha' from Abu Hurairah (RA). (Al-Sahifah al-Sadiqa was compiled by Abdullah ibn Amr ibn al-Aas)."
    },
    66: {
        "answer": "Three",
        "options": ["One", "Two", "Three", "Four"],
        "notes": "In Islamic ethics and ISL202 handouts, truthfulness (Sidq) comprises three essential aspects: truth in words (Sidq al-Aqwal), truth in actions (Sidq al-Af'al), and truth in intentions/heart (Sidq al-Niyyat)."
    },
    68: {
        "answer": "Seventy",
        "options": ["Fifty", "Seventy", "Eighty", "Hundred"],
        "notes": "In the Battle of Badr (2 AH), 70 prominent Quraish leaders were killed and 70 were taken as prisoners of war (Sahih al-Bukhari 3986)."
    },
    69: {
        "answer": "Seven",
        "options": ["Five", "Seven", "Nine", "Eleven"],
        "notes": "Hazrat Hajra ran seven times between Mount Safa and Mount Marwa in search of water for infant Ismaeel, which forms the ritual of Sa'i in Hajj and Umrah."
    },
    73: {
        "answer": "Imam Malik",
        "options": ["Imam Ahmad bin Hanbal", "Imam Malik", "Imam Shafi", "Imam Abu Hanifa"],
        "notes": "Imam Malik ibn Anas lived and taught in Madinah throughout his life and is classically honored with the title 'Imam Dar al-Hijrah'."
    },
    83: {
        "answer": "Religion",
        "options": ["Sect", "Religion", "Personality", "Morality"],
        "notes": "Hadith (Musnad Ahmad 12386): 'There is no faith for the one who has no trustworthiness, and no religion for the one who does not keep his covenant (ولا دين لمن لا عهد له)'."
    },
    86: {
        "answer": "AlFatah",
        "options": ["AlFatah", "Al-Nasr", "BaniIsraeel", "AlAnfaal"],
        "notes": "Bay'at al-Ridwan (the pledge under the tree before the Treaty of Hudaybiyyah) is explicitly mentioned in Surah Al-Fath (48:18): 'Indeed, Allah was pleased with the believers when they pledged allegiance to you under the tree'."
    },
    87: {
        "answer": "Qaf",
        "options": ["At-Tur", "Qaf", "Al-Hadid", "An-Najam"],
        "notes": "Surah Qaf (50:17-18): 'When the two receivers receive, seated on the right and on the left. Not a word does he utter but there is by him an observer ready (Raqib and Atid)'."
    },
    89: {
        "answer": "Period of ignorance",
        "options": ["Modern times", "Middle ages", "Period of ignorance", "Before history"],
        "notes": "Female infanticide (burying infant girls alive) was a barbarous pre-Islamic practice during the Age of Ignorance (Jahiliyyah), strictly abolished by Islam (Surah At-Takwir 81:8-9)."
    },
    91: {
        "answer": "Hazrat Abu Bakr R.A",
        "options": ["Hazrat Abu Bakr R.A", "Hazrat Umar R.A", "Hazrat Usman R.A", "Hazrat Ali R.A"],
        "notes": "When a grandmother came to Caliph Abu Bakr (RA) asking for her inheritance, he initially stated he found nothing in the Quran or known Sunnah, until Al-Mughirah and Muhammad ibn Maslamah testified to the Prophet's verdict giving her 1/6th (Sunan Abu Dawood 2894)."
    },
    109: {
        "answer": "Al-Baqarah",
        "options": ["Al-Anfaal", "Al-Imran", "Al-Maidah", "Al-Baqarah"],
        "notes": "Surah Al-Baqarah is the longest Surah in the Holy Quran, containing 286 verses."
    },
    111: {
        "answer": "Safa and Marwah",
        "options": ["Arafat", "Haram", "Safa and Marwah", "Mina"],
        "notes": "The ritual of Sa'i during Hajj and Umrah is performed between the two hilltops of Safa and Marwah (Surah Al-Baqarah 2:158)."
    },
    113: {
        "answer": "Knotted",
        "options": ["Approval", "Knotted", "Reality", "Custom"],
        "notes": "'Aqeedah stems from the Arabic root 'A-Q-D (ع-ق-د), which literally means to tie a knot firmly, signifying an unshakeable, deeply knotted conviction in the heart."
    },
    114: {
        "answer": "Hazrat Musa (A.S)",
        "options": ["Hazrat Esa (A.S)", "Hazrat Ibrahim (A.S)", "Hazrat Younus (A.S)", "Hazrat Musa (A.S)"],
        "notes": "Pharaoh was drowned in the Red Sea when pursuing Hazrat Musa (Moses A.S) and the Children of Israel (Surah Yunus 10:90-92)."
    },
    116: {
        "answer": "The Romans will prevail",
        "options": ["The Conquest of Makkah", "The Persians will prevail", "The Romans will be defeated", "The Romans will prevail"],
        "notes": "Surah Ar-Rum (30:2-4): 'The Romans have been defeated. In the nearest land. But they, after their defeat, will overcome/prevail within three to nine years.'"
    },
    118: {
        "answer": "Al-Baqarah",
        "options": ["Al-Anfaal", "Al-Baqarah", "Al-Imran", "Al-Maidah"],
        "notes": "Surah Al-Baqarah is the longest chapter of the Quran with 286 verses."
    },
    119: {
        "answer": "Oneness of Almighty Allah (Tauheed)",
        "options": ["Day of Judgment", "Prophethood", "Angels", "Oneness of Almighty Allah (Tauheed)"],
        "notes": "Tawhid (Absolute monotheism) is the foundational cornerstone of all revealed divine religions."
    },
    123: {
        "answer": "Fear and honor",
        "options": ["Fear and collective", "Fear and awful", "Fear and appalling", "Fear and honor"],
        "notes": "In German philology ('ehrfurcht'), 'Ehre' denotes honor and 'Furcht' denotes awe/reverential fear, meaning awe and honor in ethical demeanor."
    },
    124: {
        "answer": "The scale",
        "options": ["The place", "The scale", "The bridge", "The sword"],
        "notes": "Al-Mizan literally and technically signifies the cosmic Scale upon which human deeds are weighed on the Day of Judgment."
    },
    127: {
        "answer": "Makkah",
        "options": ["Makkah", "Madina", "Quba", "Khaibar"],
        "notes": "The Night Journey and Ascension (Al-Isra wal-Mi'raj) occurred before the Hijrah while the Prophet (PBUH) was residing in Makkah (Surah Al-Isra 17:1)."
    },
    135: {
        "answer": "Safa and Marwa",
        "options": ["Safa and Uhud", "Safa and Marwa", "Safa and Jabal-e-Noor", "Safa and Toor"],
        "notes": "Hazrat Ibrahim (AS) left Hazrat Hajra and Hazrat Ismaeel in the uncultivated valley between Safa and Marwah by the command of Allah."
    },
    136: {
        "answer": "Quba",
        "options": ["Safa", "Tabook", "Khaibar", "Quba"],
        "notes": "During the Hijrah, the Prophet (PBUH) stayed at Quba for 14 days, where he founded Masjid Quba, the first mosque of Islam."
    },
    138: {
        "answer": "Following the commands and sayings of the Prophet (PBUH)",
        "options": ["Following social customs", "Following the commands and sayings of the Prophet (PBUH)", "Obeying one's desires", "None of the above"],
        "notes": "Obedience (Ita'ah) in Islam is obeying the commands of Allah and the Prophet (PBUH)."
    },
    139: {
        "answer": "Muhammad (PBUH)",
        "options": ["Quran", "Muhammad (PBUH)", "Hazrat Abraham (Ibrahim)", "Hazrat Jesus"],
        "notes": "Surah An-Nisa (4:80): 'He who obeys the Messenger has indeed obeyed Allah.'"
    },
    144: {
        "answer": "Lazy in offering prayer and do not feed the poor",
        "options": ["Lazy in offering prayer", "Do not feed the poor", "Lazy in offering prayer and do not feed the poor", "None of the given options"],
        "notes": "Surah Al-Muddaththir (74:42-44): 'What caused you to enter Saqar? They will say: We were not of those who prayed, nor did we feed the poor.'"
    },
    146: {
        "answer": "Entire humanity",
        "options": ["Muslims", "Entire humanity", "Christianity", "Jews"],
        "notes": "The Holy Quran is a guidance for all mankind (Hudan lin-naas, Surah Al-Baqarah 2:185)."
    },
    147: {
        "answer": "Hazrat Adam A.S",
        "options": ["Hazrat Ibrahim A.S", "Hazrat Esa A.S", "Hazrat Noah A.S", "Hazrat Adam A.S"],
        "notes": "Prophethood commenced with Adam (AS) and reached finality with Muhammad (PBUH), Khatam an-Nabiyyin."
    },
    148: {
        "answer": "Pre Islamic days",
        "options": ["Modern times", "Pre Islamic days", "Westernization", "Islamic period"],
        "notes": "False tribal pride, boastfulness in ignorance, and glorification of wickedness were hallmarks of Jahiliyyah (Pre-Islamic days)."
    },
    159: {
        "answer": "Let them then produce a recital like unto it, if they speak the truth!",
        "options": [
            "But they have no knowledge therein. They follow nothing but conjecture",
            "Bring then ten forged Chapters like this",
            "Therefore, shun those who turn away from Our message",
            "Let them then produce a recital like unto it, if they speak the truth!"
        ],
        "notes": "Surah At-Tur (52:34): 'فَلْيَأْتُوا بِحَدِيثٍ مِّثْلِهِ إِن كَانُوا صَادِقِينَ' - 'Let them then produce a recital like unto it, if they speak the truth!'"
    },
    164: {
        "answer": "The polytheists of Makkah",
        "options": ["Christians", "Jews", "The polytheists of Makkah", "Muslims"],
        "notes": "During the Byzantine-Sasanian wars, the Makkan polytheists sympathized with the Zoroastrian Persians due to shared paganism, whereas Muslims favored the monotheistic Christian Romans."
    },
    167: {
        "answer": "All of the given options",
        "options": ["Turn life in to the right path", "Restrain man from evil", "Purify oneself", "All of the given options"],
        "notes": "Taqwa restrains humanity from transgressive evil, purifies the soul, and guides conduct onto the righteous path (Sirat al-Mustaqim)."
    },
    170: {
        "answer": "Highest",
        "options": ["Medium", "High", "Higher", "Highest"],
        "notes": "Sahih Muslim (2552): The Prophet (PBUH) declared: 'The highest form of filial righteousness is that a person maintains cordial ties with his father's friends.'"
    },
    174: {
        "answer": "52 1/2 Tolas",
        "options": ["52 1/2 Tolas", "7 1/2 Tolas", "10 Tolas", "40 Tolas"],
        "notes": "The Nisab of Zakat for silver is 200 Dirhams, universally calculated in South Asia as 52.5 (52 1/2) Tolas (approx. 612.36 grams)."
    },
    175: {
        "answer": "7 1/2 Tolas",
        "options": ["7 1/2 Tolas", "52 1/2 Tolas", "10 Tolas", "20 Tolas"],
        "notes": "The Nisab of Zakat for gold is 20 Mithqals / Dinars, calculated as 7.5 (7 1/2) Tolas (approx. 87.48 grams)."
    },
    180: {
        "answer": "Laws of Nature",
        "options": ["Ancestry", "Traditions", "Laws of Nature", "Wealth"],
        "notes": "Islamic Shariah is intrinsically aligned with human nature (Din al-Fitrah, Surah Ar-Rum 30:30)."
    },
    181: {
        "answer": "Prophet Muhammad (PBUH)",
        "options": ["Prophet Muhammad (PBUH)", "Hazrat Abu Bakar (RA)", "Hazrat Umar Farooq (RA)", "Hazrat Ali (RA)"],
        "notes": "Sunan an-Nasa'i (3939): The Prophet (PBUH) said: '...and the coolness of my eyes was placed in prayer (وَجُعِلَتْ قُرَّةُ عَيْنِي فِي الصَّلَاةِ).'"
    },
    182: {
        "answer": "Gifts",
        "options": ["To become their king", "Social reforms", "Political reforms", "Gifts"],
        "notes": "The Quraish dispatched expensive gifts to the Negus and his courtiers to persuade them to extradite the emigrant Muslims."
    },
    184: {
        "answer": "One",
        "options": ["One", "Two", "Three", "Four"],
        "notes": "Fidya (compensation for missed fasting due to chronic incapacity) is feeding one poor person (miskeen) two meals for each missed fast (Surah Al-Baqarah 2:184)."
    },
    192: {
        "answer": "For the sake of Allah",
        "options": ["For a good life", "For self satisfaction", "For the sake of Allah", "For worship"],
        "notes": "The highest and pure stage of Ikhlas is dedicating the act solely and purely for the pleasure and sake of Allah Almighty alone, free from ostentation (Riya)."
    },
    195: {
        "answer": "To stop / abstain",
        "options": ["To find", "To start", "To stop / abstain", "To be hungry"],
        "notes": "Linguistically, Sawm (صوم) means to hold back, abstain, and refrain (Imsak)."
    },
    196: {
        "answer": "Worship of Allah",
        "options": ["Worship of Allah", "Worship of prophets", "Follow the Sunnah", "Follow the prophets"],
        "notes": "Surah Adh-Dhariyat (51:56): 'And I did not create the jinn and mankind except to worship Me.'"
    },
    205: {
        "answer": "Muhammad bin Ismail",
        "options": ["Saeed bin Hatem", "Ali", "Zaid", "Muhammad bin Ismail"],
        "notes": "The full name of Imam Bukhari is Abu Abdillah Muhammad bin Ismail bin Ibrahim bin al-Mughirah al-Bukhari (194–256 AH)."
    },
    206: {
        "answer": "The Old Testament",
        "options": ["The Old Testament", "The New Testament", "The Books of Prophets", "Scriptures"],
        "notes": "The canonical scriptures revealed prior to Hazrat Isa (Jesus AS) constitute the Old Testament."
    },
    209: {
        "answer": "Coming at the end",
        "options": ["Coming at the end", "Coming in the middle", "Never coming", "Coming at the beginning"],
        "notes": "Al-Akhirah literally signifies that which comes at the end, referring to the ultimate life after death and Resurrection."
    },
    210: {
        "answer": "Coming at the end",
        "options": ["Coming at the end", "Coming in the middle", "Never coming", "Coming at the beginning"],
        "notes": "Al-Akhirah denotes the final, everlasting destination coming at the conclusion of worldly temporal life."
    },
    213: {
        "answer": "Almighty Allah",
        "options": ["Father", "Angel", "Almighty Allah", "Teacher"],
        "notes": "Surah An-Nisa (4:80): 'He who obeys the Messenger has obeyed Allah.'"
    },
    218: {
        "answer": "Follow the Sunnah of the Holy Prophet (PBUH)",
        "options": ["Show off his wealth", "Follow the Sunnah of the Holy Prophet (PBUH)", "Do Jihad for the sake of the booty", "Have riya in his actions"],
        "notes": "Taqwa requires pure obedience to divine mandates through diligent emulation of the Prophetic Sunnah."
    },
    220: {
        "answer": "To the whole world",
        "options": ["To a particular nation", "To a specific region", "To the whole world", "To the Arab tribes"],
        "notes": "Surah Al-Anbiya (21:107): 'And We have not sent you, [O Muhammad], except as a mercy to the worlds.'"
    },
    223: {
        "answer": "Resurrection (hasher)",
        "options": ["Resurrection (hasher)", "Ending of life", "Nuclear war", "None of the given options"],
        "notes": "Sahih al-Bukhari (59): The Prophet (PBUH) declared: 'When honesty is lost, then await the Hour (Resurrection/Qiyamah).'"
    },
    226: {
        "answer": "Teaching and spreading its knowledge",
        "options": ["Writing it", "Teaching and spreading its knowledge", "Memorizing it only", "Keeping it secret"],
        "notes": "The Sahaba were distinguished for propagating, teaching, and preserving the recitation, interpretation, and practical application of the Quran across civilizations."
    },
    232: {
        "answer": "Recitation",
        "options": ["Books", "Opening", "Writing", "Recitation"],
        "notes": "The word 'Qur'an' is an infinitive noun from Qara'a (قرأ), meaning 'The Recitation' or 'The Continually Recited Book'."
    },
    243: {
        "answer": "Avoiding hardship",
        "options": ["Permissibility", "Avoiding hardship", "Mandatory action", "Spiritual purity"],
        "notes": "The cardinal legal maxim 'Nafi al-Haraj' (نفي الحرج) means the removal and avoidance of undue hardship (Surah Al-Hajj 22:78)."
    },
    245: {
        "answer": "Easing of laws to prevent hardship",
        "options": ["Prohibition", "Hardship or difficulty", "Easing of laws to prevent hardship", "Mandatory action"],
        "notes": "Nafi al-Haraj entails granting legal dispensations (Rukhsah) to avert debilitating strain and hardship."
    },
    248: {
        "answer": "Sound or authentic Hadith (Sahih)",
        "options": ["Weak Hadith", "Sound or authentic Hadith (Sahih)", "Fabricated Hadith (Mawdu)", "Good Hadith (Hasan)"],
        "notes": "A Sahih Hadith is a rigorously authenticated tradition narrated by just, highly competent transmitters with a continuous chain free of irregularities or defects."
    },
    250: {
        "answer": "Islamic law derived from the Quran and Hadith",
        "options": ["Islamic mysticism", "Islamic philosophy", "Islamic law derived from the Quran and Hadith", "Islamic history"],
        "notes": "Fiqh technically is the science of deriving practical legal rules of Shariah from detailed textual evidences."
    },
    256: {
        "answer": "Bukhari and Muslim",
        "options": ["Mishkat", "Bukhari", "Bukhari and Muslim", "Ibne Majah"],
        "notes": "Al-Sahihain ('The Two Authentic Collections') refers specifically to Sahih al-Bukhari and Sahih Muslim."
    },
    257: {
        "answer": "Bukhari and Muslim",
        "options": ["Mishkat", "Bukhari", "Bukhari and Muslim", "Ibne Majah"],
        "notes": "Al-Sahihain refers to the twin canonical Hadith collections of Imam Bukhari and Imam Muslim."
    },
    258: {
        "answer": "Bukhari and Muslim",
        "options": ["Mishkat", "Bukhari", "Bukhari and Muslim", "Ibne Majah"],
        "notes": "Al-Sahihain refers to Sahih al-Bukhari and Sahih Muslim."
    },
    261: {
        "answer": "Ensuring justice and fairness in society",
        "options": ["Wealth accumulation", "Ensuring justice and fairness in society", "Political dominance", "Encouraging asceticism"],
        "notes": "The paramount objective of Islamic jurisprudence (Maqasid al-Shariah) is securing universal justice, equity, and human welfare (Maslahah)."
    },
    264: {
        "answer": "Zakat",
        "options": ["Sawm", "Zakat", "Hajj", "Salat"],
        "notes": "Zakat is the obligatory fiscal charity and the third pillar of Islam."
    },
    265: {
        "answer": "Hajj",
        "options": ["Zakat", "Salat", "Hajj", "Sawm"],
        "notes": "Hajj is the annual holy pilgrimage to Makkah, the fifth pillar of Islam."
    },
    271: {
        "answer": "Similarity in inner and outer self",
        "options": ["Believe in Faith with worldly benefits", "Similarity in inner and outer self", "Efficiency", "All of the given options"],
        "notes": "Sincerity (Ikhlas) fundamentally demands complete conformity between the inward heart and outward deeds, banishing hypocrisy."
    },
    272: {
        "answer": "Belief in Allah",
        "options": ["Belief in Angels", "Belief in Allah", "Belief in Prophets", "Belief in Day of Judgment"],
        "notes": "The first and supreme pillar of Iman is belief in Allah Almighty (Al-Imanu Billah)."
    },
    274: {
        "answer": "Belief in one God (Tawhid)",
        "options": ["Belief in many gods", "Belief in one God (Tawhid)", "Belief in reincarnation", "Belief in a holy trinity"],
        "notes": "Tawhid—strict, uncompromised monotheism—is the distinctive essence of Islam."
    },
    280: {
        "answer": "Spiritual purification",
        "options": ["Wealth accumulation", "Spiritual purification", "Political dominance", "Social stratification"],
        "notes": "The primary objective of Islamic teachings and worship is Tazkiyat al-Nafs (purification of the soul from vice and sin)."
    },
    283: {
        "answer": "The Old Testament",
        "options": ["The New Testament", "The Old Testament", "The Books of Prophets", "Scriptures"],
        "notes": "The first principal division of the Christian Bible is the Old Testament."
    },
    284: {
        "answer": "Khutba Taqwa",
        "options": ["Khutba Taqwa", "Khutba Hajja-tul-weda", "Khutba Rasool", "None of the given options"],
        "notes": "The sermon delivered by the Holy Prophet (PBUH) upon arrival at Quba during the Hijrah is historically known as Khutbah at-Taqwa."
    },
    286: {
        "answer": "7th",
        "options": ["First", "7th", "Ninth", "Eleventh"],
        "notes": "Rajab is the 7th month of the Islamic lunar calendar and one of the four sacred months (Al-Ashhur al-Hurum)."
    },
    287: {
        "answer": "To commemorate the first revelation of the Quran",
        "options": ["To celebrate harvest", "To commemorate the first revelation of the Quran", "To honor the birth of the Prophet Muhammad", "To mark the beginning of the Islamic new year"],
        "notes": "Surah Al-Baqarah (2:185): 'The month of Ramadan in which was revealed the Quran, a guidance for the people...'"
    },
    289: {
        "answer": "To understand and apply the teachings of the Prophet",
        "options": ["To discard old texts", "To understand and apply the teachings of the Prophet", "To rewrite the Quran", "To compare with other religious texts"],
        "notes": "The textual analysis (Dirayat al-Hadith) aims at comprehending the prophetic legal wisdom and embodying its moral teachings."
    },
    290: {
        "answer": "1/20",
        "options": ["1/20", "1/5", "1/10", "1/15"],
        "notes": "Agricultural produce irrigated by artificial means (canals, tube-wells) is subject to 1/20 (5%, Nisf al-Ushr), whereas rainfed land is subject to 1/10 (10%, Ushr)."
    },
    294: {
        "answer": "Justice should be upheld without causing unnecessary hardship",
        "options": ["Wealth should be distributed equally among all people", "Justice should be upheld without causing unnecessary hardship", "Men and women should have equal roles in society", "All religious texts should be interpreted in the same way"],
        "notes": "Juridical equity (Istihsan) ensures that rigid formal rules yield to equitable solutions preventing undue hardship."
    },
    295: {
        "answer": "It is the day when all beings will be judged for their deeds",
        "options": ["It marks the beginning of the universe", "It is a day of rest", "It is the day when all beings will be judged for their deeds", "It is a day for celebrating creation"],
        "notes": "The Day of Judgment (Yawm al-Din) is the day of absolute accountability where all souls are judged for their earthly conduct."
    },
    297: {
        "answer": "It ensures the authenticity of the Hadith",
        "options": ["It determines the length of the Hadith", "It ensures the authenticity of the Hadith", "It provides context for the Hadith", "It explains the meaning of the Hadith"],
        "notes": "The chain of narration (Sanad/Isnad) is the hallmark Islamic method guaranteeing textual authenticity back to the Prophet (PBUH)."
    },
    298: {
        "answer": "Abu Abdullah",
        "options": ["Abu Muhammad", "Abu Ahmad", "Abu Abdul Rehman", "Abu Abdullah"],
        "notes": "Imam Ibn Majah's full name is Abu Abdullah Muhammad bin Yazid bin Majah al-Qazwini (209–273 AH)."
    },
    302: {
        "answer": "Shahada",
        "options": ["Zakat", "Shahada", "Salat", "Sawm"],
        "notes": "The Shahada (testimony of faith: 'There is no god but Allah and Muhammad is His Messenger') is the first pillar of Islam."
    },
    307: {
        "answer": "Taqwa and disobedience (Fajur)",
        "options": ["Taqwa", "Taqwa and obedience", "Taqwa and respect", "Taqwa and disobedience (Fajur)"],
        "notes": "Surah Ash-Shams (91:8): 'فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَاهَا' - 'And inspired it with its wickedness (Fujur) and its righteousness (Taqwa).'"
    },
    309: {
        "answer": "Paternal Cousin",
        "options": ["Nephew", "Brother", "Paternal Cousin", "Brother in Law"],
        "notes": "Hazrat Abdullah bin Abbas (RA) was the son of Abbas bin Abdul-Muttalib, paternal uncle of the Prophet (PBUH); hence he was the Prophet's paternal first cousin."
    },
    317: {
        "answer": "Sahih Bukhari",
        "options": ["Sunan Ibn Majah", "Sahih Bukhari", "Sunan al-Nasa'i", "Musnad Ahmad"],
        "notes": "Sahih al-Bukhari is unanimously acknowledged across the Muslim world as the most authentic book after the Holy Quran (Asahh al-Kutub ba'd Kitabillah)."
    },
    323: {
        "answer": "AlNamal",
        "options": ["AlNehal", "AlNamal", "AlAhzaab", "AlNoor"],
        "notes": "Surah An-Naml (Chapter 27) contains Bismillah twice: at the opening and in verse 30 ('Indeed, it is from Solomon, and indeed it is: In the name of Allah, the Entirely Merciful, the Especially Merciful')."
    },
    329: {
        "answer": "Qur'an",
        "options": ["Qur'an", "Zubur", "Torah", "Injil"],
        "notes": "The Holy Quran is the final, complete, and most comprehensive scripture sent down for all humanity until the end of time."
    },
    333: {
        "answer": "Holy Quran",
        "options": ["Splitting of moon", "None of the given options", "Ascension (Miraj)", "Holy Quran"],
        "notes": "The Holy Quran is the supreme, eternal, and living miracle (Mu'jizah) of Prophet Muhammad (PBUH), continuing to challenge humanity throughout the ages."
    },
    335: {
        "answer": "Saum",
        "options": ["Salat", "Zakah", "Saum"],
        "notes": "Surah Al-Baqarah (2:185): 'فَمَن شَهِدَ مِنكُمُ الشَّهْرَ فَلْيَصُمْهُ' ('So whoever among you sights the month, let him fast it')."
    },
    337: {
        "answer": "Flexible and adaptable",
        "options": ["Fixed and unchangeable", "Rigid and uncompromising", "Flexible and adaptable", "Complex and confusing"],
        "notes": "While primary credal tenets are constant, Islamic legal jurisprudence possesses dynamic flexibility and adaptability to meet novel human circumstances through Ijtihad."
    },
    339: {
        "answer": "Sunan Ibn e Maja",
        "options": ["Sahih Muslim", "Sahihain", "Sunan Ibn e Maja", "Sahih Bukhari"],
        "notes": "Books titled 'Sunan' (such as Sunan Ibn Majah, Sunan Abi Dawood) are arranged strictly according to legal/jurisprudential categories (Abwab Fiqhiyyah)."
    },
    346: {
        "answer": "Sunan Al-Nisai",
        "options": ["Sunan Al-Nisai", "Sunan Abi-Dawood", "Sunan Ibn e Maja", "Sunan Tirmidhi"],
        "notes": "Imam an-Nasa'i's canonical work is titled 'Al-Sunan al-Sughra' (also called 'Al-Mujtaba'), distilled from his larger compilation 'Al-Sunan al-Kubra'."
    },
    355: {
        "answer": "Saad Bin Abi Waqas (RA)",
        "options": ["Saad Bin Ubaid (RA)", "Saad Bin Ubada (RA)", "Saad Bin Abi Waqas (RA)", "Hazrat Hamza (RA)"],
        "notes": "Hazrat Sa'd ibn Abi Waqqas (RA) is one of the ten Companions given glad tidings of Paradise in a single sitting (Al-Asharah al-Mubashsharun)."
    },
    363: {
        "answer": "Alat",
        "options": ["Qiyas", "Ijma", "Alat", "Fatwa"],
        "notes": "In Usul al-Fiqh, the underlying effective legal cause connecting the original case to the new branch is the 'Illah (termed 'Alat' in Urdu/Perso-Arabic script)."
    },
    368: {
        "answer": "Hazrat Umar (R.A)",
        "options": ["Hazrat Umar (R.A)", "Hazrat Uthman (R.A)", "Hazrat Ali (R.A)", "Hazrat Zaid (R.A)"],
        "notes": "After many Huffaz were martyred at Yamama, Hazrat Umar (RA) advised Caliph Abu Bakr (RA) to compile the Quran into a single codex (Sahih al-Bukhari 4986)."
    },
    383: {
        "answer": "Hazrat Abdullah bin Ariqat (R.A)",
        "options": ["Hazrat Saad bin Ubada (R.A)", "Hazrat Utab bin Usaid (R.A)", "Hazrat Abdullah bin Ariqat (R.A)"],
        "notes": "Abdullah ibn Urayqit was hired by the Prophet (PBUH) and Abu Bakr (RA) as an expert desert guide to steer them to Madinah along uncharted coastal routes."
    },
    391: {
        "answer": "Taqwa (piety), sincerity and sacrifice",
        "options": ["Taqwa (piety), sincerity and sacrifice", "Altruism and Fascism", "Egoism and insensitivity", "All of the given options"],
        "notes": "Taqwa, sincerity (Ikhlas), and self-sacrifice (Ithar) are core ethical virtues of the Islamic way of life."
    },
    394: {
        "answer": "Al-Asr",
        "options": ["Al-Nasr", "Al-Asr", "Al-Qadr", "Al-Takathur"],
        "notes": "Imam Ash-Shafi famously stated: 'If people were to reflect upon Surah Al-Asr alone, it would suffice them,' as it encapsulates faith, righteous deeds, mutual counsel of truth, and steadfast patience."
    },
    399: {
        "answer": "Hazrat Abdullah bin Umar bin Alaas",
        "options": ["Hazrat Abdullah bin Abbas", "Hazrat Abdullah bin Umar bin Alaas", "Hazrat Abdullah bin Masood", "Hazrat Abdullah bin Zubair"],
        "notes": "Hazrat Abdullah ibn Amr ibn al-Aas (RA) wrote down every tradition directly from the Prophet (PBUH) with permission, compiled in Al-Sahifah al-Sadiqa (Sunan Abi Dawood 3646)."
    },
    403: {
        "answer": "Imam Ghazali",
        "options": ["Allama Iqbal", "Imam Ghazali", "Sir Syed Ahmad Khan", "Liaquat Ali Khan"],
        "notes": "In Ihya 'Ulum al-Din, Imam Abu Hamid al-Ghazali defined character (Khuluq) as an established state of the human soul from which actions emerge easily without arduous deliberation."
    },
    406: {
        "answer": "Hazrat Abu Bakar",
        "options": ["Hazrat Abu Bakar", "Hazrat Umar", "Hazrat Usman", "Hazrat Ali"],
        "notes": "Caliph Abu Bakr as-Siddiq (RA) proclaimed this in his renowned inaugural address upon assuming the Khilafah: 'Obey me so long as I obey Allah and His Messenger; if I disobey them, you owe me no obedience.'"
    }
}

# Process every question
modified_count = 0
for q in questions:
    qid = q['id']
    
    # 1. Clean question text
    q_text = q['question'].strip()
    # Remove trailing source or page artifacts
    q_text = re.sub(r'ISL202/201\(Islamiat\)\s+Page\s+\d+\s+of\s+\d+', '', q_text).strip()
    q_text = re.sub(r'\s+58$', '', q_text).strip()
    q_text = re.sub(r'\s+Options:$', '', q_text).strip()
    q['question'] = q_text

    # 2. Check if explicit override exists
    if qid in OVERRIDES:
        ovr = OVERRIDES[qid]
        if "question" in ovr:
            q['question'] = ovr['question']
        q['options'] = ovr['options']
        q['answer'] = ovr['answer']
        q['solution_notes'] = ovr.get('notes', q.get('solution_notes'))
        modified_count += 1
        continue

    # 3. Clean options
    raw_opts = q.get('options', [])
    clean_opts = []
    # Filter junk options injected erroneously
    junk_set = {'One tenth (1/10)', 'Safa and Marwah', 'Hazrat Hajra', 'Hazrat Abu-baker', 'Medium', "Qur'an", 'B', 'C', 'A', 'D'}
    
    for opt in raw_opts:
        # If length is long or multiple options, clean
        cleaned = clean_text_str(opt)
        if cleaned not in clean_opts and (len(raw_opts) <= 4 or opt not in junk_set):
            clean_opts.append(cleaned)
            
    # If options ended up empty or less than 2, restore original
    if len(clean_opts) < 2:
        clean_opts = [clean_text_str(o) for o in raw_opts]

    # Clean answer
    ans = clean_text_str(q['answer'])
    
    # Ensure answer is in clean_opts
    if ans not in clean_opts:
        # Check case-insensitive match
        matched = False
        for c in clean_opts:
            if c.lower() == ans.lower():
                ans = c
                matched = True
                break
        if not matched:
            clean_opts.append(ans)

    q['options'] = clean_opts
    q['answer'] = ans

print(f"Applied master verifications. Total questions: {len(questions)}")

# Verify 100% of questions have answer in options
invalid = [q for q in questions if q['answer'] not in q['options']]
print(f"Invalid questions after pass: {len(invalid)}")
if invalid:
    for inv in invalid[:5]:
        print(f"ID {inv['id']}: ans '{inv['answer']}' not in {inv['options']}")
    raise ValueError("Found invalid questions!")

# Save isl202_quiz_bank.json
with open('isl202_quiz_bank.json', 'w') as f:
    json.dump(questions, f, indent=2)
print("Successfully saved isl202_quiz_bank.json.")

# Rebuild quiz_data.js
import subprocess
res = subprocess.run(['python3', 'build_clean_quiz_data_js.py'], capture_output=True, text=True)
print("Rebuilt quiz_data.js:")
print(res.stdout)
if res.stderr:
    print("Stderr:", res.stderr)
