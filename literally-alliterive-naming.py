import random

def generate_release_names(num_names=5):
    # Australian geographic landmarks, fauna, and regional terms
    aus_terms = [
        "Arnhem", "Adelaide", "Acheron", "Barossa", "Billabong", "Bondi", "Bushfire", 
        "Ballarat", "Brisbane", "Cairns", "Canberra", "Coober", "Daintree", "Darwin", 
        "Diggity", "Echidna", "Emu", "Exmouth", "Flinders", "Freo", "Gippsland", 
        "Geelong", "Hobart", "Hotham", "Illawarra", "Kakadu", "Kimberley", "Kata", 
        "Larapinta", "Lismore", "Maluka", "Mulga", "Melbourne", "Mallee", "Nullarbor", 
        "Noosa", "Outback", "Oodnadatta", "Perth", "Pilbara", "Queensland", "Red-Center", 
        "Rottnest", "Spinifex", "Sydney", "Snowy", "Tassie", "Toowoomba", "Uluru", 
        "Victoria", "Wallaby", "Wombat", "Whitsunday", "Yarra", "Armidale", "Ashburton", 
        "Bairnsdale", "Balranald", "Bega", "Bellingen", "Bettong", "Bilby", "Biloela", 
        "Birdsville", "Bogong", "Bombala", "Bourke", "Bowen", "Brolga", "Brumby", "Bunbury", 
        "Bundaberg", "Burnie", "Busselton", "Carnarvon", "Casino", "Ceduna", "Cessnock", 
        "Charleville", "Cobar", "Colac", "Condamine", "Cooma", "Coonamble", "Corroboree", 
        "Cowra", "Cronulla", "Dalby", "Dandenong", "Deniliquin", "Derwent", "Devonport", 
        "Diamantina", "Dillybag", "Dongara", "Dorrigo", "Dunnart", "Eden", "Emerald", 
        "Esperance", "Euroa", "Forbes", "Forster", "Frankston", "Glider", "Gosford", 
        "Goulburn", "Grafton", "Griffith", "Gundagai", "Gympie", "Hahndorf", "Hamilton", 
        "Hawkesbury", "Hay", "Healesville", "Hornsby", "Horsham", "Innisfail", "Inverell", 
        "Ivanhoe", "Jackaroo", "Jervis", "Jillaroo", "Junee", "Karratha", "Kelpie", 
        "Kempsey", "Kerang", "Kingaroy", "Kyogle", "Leeton", "Litchfield", "Lithgow", 
        "Lorikeet", "Macadamia", "Maclean", "Magpie", "Maitland", "Mandurah", "Manjimup", 
        "Manly", "Mareeba", "Marsupial", "Monotreme", "Pademelon", "Potoroo", "Rosella", 
        "Taipan", "Torquay", "Traralgon", "Wallaroo", "Wattle", "Whyalla", "Adelaide", 
        "Albany", "Albury", "Alice", "Anzac", "Arnhem", "Atherton", "Ballarat", "Barossa", 
        "Barramundi", "Bathurst", "Bendigo", "Billabong", "Bondi", "Boomerang", 
        "Brisbane", "Broome", "Bungle", "Bunyip", "Bushfire", "Byron", "Cairns", 
        "Canberra", "Cassowary", "Cockatoo", "Coober", "Coogee", "Coolgardie", "Croc", 
        "Daintree", "Dampier", "Darling", "Darwin", "Dingo", "Dubbo", "Echidna", 
        "Echuca", "Emu", "Eureka", "Exmouth", "Eyre", "Fitzroy", "Flinders", "Fremantle", 
        "Freo", "Galah", "Gawler", "Geelong", "Geraldton", "Gippsland", "Goanna", 
        "Grampians", "Hobart", "Hotham", "Hunter", "Illawarra", "Ipswich", "Jabiru", 
        "Jindabyne", "Kakadu", "Kalgoorlie", "Kangaroo", "Kata", "Katoomba", "Katherine", 
        "Kiama", "Kimberley", "Koala", "Kookaburra", "Kosciuszko", "Larapinta", 
        "Launceston", "Lismore", "Mackay", "Mallee", "Melbourne", "Mildura", "Mulga", 
        "Murray", "Newcastle", "Ningaloo", "Noosa", "Nullarbor", "Numbat", "Oodnadatta", 
        "Outback", "Parkes", "Perth", "Pilbara", "Platypus", "Queensland", "Quokka", 
        "Quoll", "Rockhampton", "Rottnest", "Spinifex", "Sydney", "Tasmania", "Uluru", 
        "Wombat"
    ]

    # Medical education, clinical, and emergency services terms
    medical_terms = [
        "Airways", "Ambulance", "Anatomy", "Bandage", "Biopsy", "Burner", "Bradycardia", 
        "Cannula", "Cardio", "Clinic", "Defib", "Doppler", "Diagnostics", "Embolus", 
        "Endo", "Epi", "Fracture", "Femur", "Graft", "Gurney", "Hemorrhage", "Heart", 
        "Intubation", "Iv", "Ketamine", "Kidney", "Laceration", "Larynx", "Medevac", 
        "Myocardium", "Monitor", "Naloxone", "Node", "Oximetry", "Oxygen", "Pathology", 
        "Pulse", "Plaster", "Quad", "Resus", "Rapid", "Scalpel", "Suture", "Stethoscope", 
        "Triage", "Trauma", "Ultrasound", "Vitals", "Ventilator", "Wheeze", "Wound", "Xray", 
        "Abrasion", "Adrenaline", "Affective", "Airway", "Ambulance", "Amiodarone", 
        "Anaphylaxis", "Anatomy", "Andragogy", "Aneurysm", "Anoxia", "Antibody", 
        "Antidote", "Antigen", "Apnea", "Arrhythmia", "Aspirin", "Assessment", "Asystole", 
        "Auscultation", "Bandage", "Beacon", "Blood", "Bolus", "Bradycardia", "Bradypnea", 
        "Breathing", "Burn", "Capnography", "Cardiac", "Cardiology", "Cardioversion", 
        "Catheter", "Certification", "Circulation", "Clinic", "Clinical", "Coagulation", 
        "Cognitive", "Command", "Competency", "Concussion", "Constructivism", "Contusion",
        "Course", "Credentialing", "Crepitus", "Curriculum", "Cyanosis", "Debriefing",
        "Defibrillation", "Defibrillator", "Dextrose", "Diagnosis", "Diaphoresis", 
        "Diastole", "Didactic", "Dispatch", "Dislocation", "Diuresis", "Dose", "Dyspnea", 
        "Edema", "Education", "Electrocardiogram", "Emergency", "Emesis", "Epinephrine", 
        "Erythema", "Evaluation", "Evacuation", "Extrication", "Facilitation", "Feedback", 
        "Fentanyl", "Fibrillation", "Fidelity", "Fluid", "Formative", "Fracture", 
        "Glucagon", "Gurney", "Handoff", "Helmet", "Hemostasis", "Heparin", "Hemorrhage",
        "Hyperglycemia", "Hypertension", "Hyperventilation", "Hypoglycemia", "Hypotension",
         "Hypoventilation", "Hypoxia", "Incident", "Infarction", "Infection", "Inflammation", 
         "Infusion", "Insulin", "Intramuscular", "Intraosseous", "Intravenous", "Intubation", 
         "Ipratropium", "Ischemia", "Jaundice", "Ketamine", "Laceration", "Lecture", "Licensure",
         "Lights", "Manikin", "Mayday", "Mentorship", "Metacognition", "Midazolam", "Module",
         "Morphine", "Naloxone", "Neurology", "Nitroglycerin", "Objective", "Ondansetron",
         "Operations", "Orientation", "Outcome", "Oximetry", "Oxygen", "Pacing", "Pager",
         "Pallor", "Palpation", "Paramedic", "Pathology", "Pedagogy", "Percussion",
         "Pharmacology", "Physiology", "Portfolio", "Practicum", "Preceptorship", "Prognosis",
         "Psychomotor", "Pupil", "Radio", "Rales", "Reactive", "Reflection", "Rescue", 
         "Residency", "Responder", "Response", "Resuscitation", "Rhonchi", "Roster", "Rubric",
         "Salbutamol", "Scaffold", "Scenario", "Seizure", "Seminar", "Sepsis", "Shift", 
         "Shock", "Simulation", "Siren", "Splint", "Sprain", "Standardized", "Station", 
         "Strain", "Stretcher", "Stridor", "Stroke", "Structured", "Subcutaneous", "Summative", 
         "Syllabus", "Symptom", "Syncope", "Syndrome", "Systole", "Tachycardia", "Tachypnea", 
         "Taxonomy", "Tourniquet", "Toxin", "Transfusion", "Trauma", "Triage", "Turnout", 
         "Tutorial", "Ventilation", "Vertigo", "Vignette", "Vital", "Wheeze", "Workshop", 
         "Wound"
    ]

    # Group medical terms by their starting letter for faster alliteration mapping
    medical_by_letter = {}
    for word in medical_terms:
        first_letter = word[0].lower()
        medical_by_letter.setdefault(first_letter, []).append(word)

    # Find all valid alliterative combinations
    valid_pairs = []
    for aus_word in aus_terms:
        first_letter = aus_word[0].lower()
        if first_letter in medical_by_letter:
            for med_word in medical_by_letter[first_letter]:
                valid_pairs.append(f"{aus_word} {med_word}")

    # Prevent requesting more names than physically available in the list
    sample_size = min(num_names, len(valid_pairs))
    
    # Return a random selection of unique pairs
    return random.sample(valid_pairs, sample_size)

# Generate and print 10 unique, alliterative release names
if __name__ == "__main__":
    codenames = generate_release_names(10)
    print("🚀 Your Alliterative Software Release Names:")
    for idx, name in enumerate(codenames, 1):
        print(f"Version {idx}.0: {name}")
