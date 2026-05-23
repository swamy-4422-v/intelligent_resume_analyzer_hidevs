def calculate_match_score(resume: dict, job: dict) -> dict:
    if not isinstance(resume, dict) or not isinstance(job, dict):
        raise TypeError("Both resume and job must be dictionaries.")

    required_skills = job.get("required_skills", [])
    min_exp = float(job.get("min_experience_years", 0))
    preferred_edu = job.get("preferred_education", "").lower()

    candidate_skills_lower = [s.lower() for s in resume.get("skills", [])]
    if required_skills:
        matched = [s for s in required_skills if s.lower() in candidate_skills_lower]
        skill_score = (len(matched) / len(required_skills)) * 60
    else:
        matched = []
        skill_score = 60.0

    candidate_exp = resume.get("experience_years", 0.0)
    if min_exp > 0:
        exp_score = min(candidate_exp / min_exp, 1.0) * 30
    else:
        exp_score = 30.0

    edu_score = 0.0
    if preferred_edu and preferred_edu in resume.get("raw_text", "").lower():
        edu_score = 10.0

    total_score = round(skill_score + exp_score + edu_score, 2)

    return {
        "total_score": total_score,
        "skill_score": round(skill_score, 2),
        "exp_score": round(exp_score, 2),
        "edu_score": round(edu_score, 2),
        "matched_skills": matched,
        "missing_skills": [s for s in required_skills if s.lower() not in candidate_skills_lower],
        "candidate_experience_years": candidate_exp,
        "required_experience_years": min_exp,
    }

def get_recommendation(score: float) -> str:
    if score >= 80:
        return "Strong Match – Highly recommended for interview."
    elif score >= 60:
        return "Good Match – Recommended for further review."
    elif score >= 40:
        return "Partial Match – May qualify with additional screening."
    else:
        return "Weak Match – Does not meet minimum requirements."
