import json
import re

with open("skills_db.json", "r") as f:
    skills_data = json.load(f)

ALL_SKILLS = [
    skill for category in skills_data.values() for skill in category
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))


def extract_skills_by_category(text):
    text = text.lower()
    result = {}

    for category, skills in skills_data.items():
        found = []
        for skill in skills:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text):
                found.append(skill)

        if found:
            result[category] = found

    return result


def calculate_score(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    score = len(matched) / len(job_skills) * 100 if job_skills else 0
    return round(score, 2), list(matched)