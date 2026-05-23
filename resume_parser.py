import re
from typing import Optional

def extract_name(text: str) -> str:
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    if lines:
        first_line = lines[0]
        words = first_line.split()
        if 2 <= len(words) <= 4 and all(w[0].isupper() for w in words if w):
            return first_line
    return "Unknown"

def extract_email(text: str) -> Optional[str]:
    pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    return match.group(0) if match else None

def extract_phone(text: str) -> Optional[str]:
    pattern = r'(\+?\d[\d\s\-().]{7,}\d)'
    match = re.search(pattern, text)
    return match.group(0).strip() if match else None

def extract_skills(text: str, skill_keywords: list) -> list:
    text_lower = text.lower()
    found = []
    for skill in skill_keywords:
        if skill.lower() in text_lower:
            found.append(skill)
    return list(dict.fromkeys(found))

def extract_experience_years(text: str) -> float:
    patterns = [
        r'(\d+)\+?\s*years?\s+of\s+experience',
        r'(\d+)\+?\s*years?\s+experience',
        r'experience\s+of\s+(\d+)\+?\s*years?',
    ]
    for pat in patterns:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return 0.0

def parse_resume(text: str, skill_keywords: list) -> dict:
    if not text or not text.strip():
        raise ValueError("Resume text cannot be empty.")
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text, skill_keywords),
        "experience_years": extract_experience_years(text),
        "raw_text": text.strip(),
    }
