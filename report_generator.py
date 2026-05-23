import sys
sys.path.insert(0, 'intelligent_resume_analyzer')
from matcher import get_recommendation

_DIVIDER = "=" * 60
_THIN = "-" * 60

def generate_report(resume: dict, match_result: dict, job: dict) -> str:
    score = match_result["total_score"]
    recommendation = get_recommendation(score)
    lines = [
        _DIVIDER,
        "          INTELLIGENT RESUME ANALYSIS REPORT",
        _DIVIDER,
        "",
        "CANDIDATE INFORMATION",
        _THIN,
        f"  Name            : {resume.get('name', 'N/A')}",
        f"  Email           : {resume.get('email', 'N/A')}",
        f"  Phone           : {resume.get('phone', 'N/A')}",
        f"  Experience      : {resume.get('experience_years', 0)} year(s)",
        "",
        "JOB REQUIREMENTS",
        _THIN,
        f"  Job Title       : {job.get('title', 'N/A')}",
        f"  Min. Experience : {match_result['required_experience_years']} year(s)",
        f"  Required Skills : {', '.join(job.get('required_skills', [])) or 'N/A'}",
        "",
        "MATCH ANALYSIS",
        _THIN,
        f"  Skills Score    : {match_result['skill_score']:>6.1f} / 60",
        f"  Experience Score: {match_result['exp_score']:>6.1f} / 30",
        f"  Education Bonus : {match_result['edu_score']:>6.1f} / 10",
        f"  TOTAL SCORE     : {score:>6.1f} / 100",
        "",
        "SKILL DETAILS",
        _THIN,
        f"  Matched Skills  : {', '.join(match_result['matched_skills']) or 'None'}",
        f"  Missing Skills  : {', '.join(match_result['missing_skills']) or 'None'}",
        "",
        "RECOMMENDATION",
        _THIN,
        f"  {recommendation}",
        "",
        _DIVIDER,
    ]
    return "\n".join(lines)

def print_report(resume, match_result, job):
    print(generate_report(resume, match_result, job))
