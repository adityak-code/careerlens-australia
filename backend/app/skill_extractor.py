import csv
import re
from pathlib import Path

def load_skills() -> list[str]:
    """
    Load skills from skills_list.csv
    """

    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    skills_file = project_root/"data"/"skills_list.csv"

    skills = []

    with open(skills_file, mode='r', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            skill = row["skill"].strip()

            if skill:
                skills.append(skill)

            return skills

def extract_skills_from_text(text: str)-> list[str]:
    """
    Extract skills from text using regex.
    """

    skills_list = load_skills()
    found_skills = []
    text_lower = text.lower()

    for skill in skills_list:
        skill_lower = skill.lower()
        pattern = r"\b" + re.escape(skill_lower) + r"\b"
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(set(found_skills))

            

