def extract_skills(text):
    keys=["python","java","sql","react","aws","machine learning","docker"]
    return [k for k in keys if k in text.lower()]
