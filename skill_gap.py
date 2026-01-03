def load_skills(file_path="skills_list.txt"):
    with open(file_path, "r") as file:
        skills = [skill.strip().lower() for skill in file.readlines()]
    return skills

def find_skill_gap(resume_text, skills):
    present_skills = []
    missing_skills = []

    for skill in skills:
        if skill in resume_text:
            present_skills.append(skill)
        else:
            missing_skills.append(skill)

    return present_skills, missing_skills
