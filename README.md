# 🧠 Intelligent Resume Analyzer

> A Python + HTML system that automates resume screening — parses candidate resumes, calculates weighted match scores (0–100), and generates professional hiring recommendations.

🔗 **Live Demo:** [intelligent-resume-analyzer-cyan.vercel.app](https://intelligent-resume-analyzer-cyan.vercel.app)

---

## 🎯 Features

| Feature | Details |
|---|---|
| **Resume Parsing** | Extracts name, email, phone, skills, and experience years using regex |
| **Matching Algorithm** | Weighted 3-dimension scoring — Skills 60% + Experience 30% + Education 10% |
| **Skill Gap Analysis** | Identifies matched skills and missing required skills against the job |
| **Hiring Recommendation** | Automatic Strong Match / Good Match / Partial Match / Weak Match |
| **Modular Architecture** | Clean separation: parser → matcher → report generator → file handler |
| **Web Interface** | `index.html` — interactive front-end to run analysis in the browser |
| **No External Dependencies** | Pure Python standard library — works anywhere without `pip install` |

---

## 📁 Project Structure

```
intelligent_resume_analyzer_hidevs/
│
├── resume_parser.py       # Extracts name, email, phone, skills, experience from raw text
├── matcher.py             # Calculates weighted match score + recommendation
├── report_generator.py    # Generates structured hiring reports
├── file_handler.py        # JSON save/load for analysis results
├── index.html             # Browser-based interactive front-end
│
├── samples/               # Sample resumes and job descriptions for testing
│
└── output/                # Auto-created — JSON results saved here
```

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/swamy-4422-v/intelligent_resume_analyzer_hidevs.git
cd intelligent_resume_analyzer_hidevs
```

### 2. Run the Python analyzer
```bash
python resume_parser.py
```

### 3. Open the web interface
Open `index.html` in your browser, or visit the live demo:
👉 [intelligent-resume-analyzer-cyan.vercel.app](https://intelligent-resume-analyzer-cyan.vercel.app)

---

## 📊 Scoring Algorithm

```
Total Score (0–100) = Skill Score + Experience Score + Education Score

Skills (60 pts):
  → Required Skills matched in resume text
  → (matched / total required) × 60

Experience (30 pts):
  → (candidate_years / min_required_years) × 30
  → Capped at 30 pts

Education (10 pts):
  → Preferred education keyword found in resume → 10 pts
  → Not found → 0 pts
```

---

## 🏆 Recommendation Thresholds

| Score | Recommendation |
|---|---|
| 80–100 | 🟢 **Strong Match** — Highly recommended for interview |
| 60–79 | 🟡 **Good Match** — Recommended for further review |
| 40–59 | 🟠 **Partial Match** — May qualify with additional screening |
| 0–39  | 🔴 **Weak Match** — Does not meet minimum requirements |

---

## 🧩 Module Overview

### `resume_parser.py`
Parses raw resume text and returns a structured dictionary:
- `extract_name(text)` — reads the first capitalized line (2–4 words)
- `extract_email(text)` — regex email extraction
- `extract_phone(text)` — regex phone extraction
- `extract_skills(text, skill_keywords)` — keyword-match against a provided skills list
- `extract_experience_years(text)` — regex pattern matching for years of experience
- `parse_resume(text, skill_keywords)` — combines all extractors into one dict

### `matcher.py`
Scores a parsed resume against a job description dict:
- `calculate_match_score(resume, job)` — returns scores for skills, experience, education, and a list of matched/missing skills
- `get_recommendation(score)` — maps a total score to a hiring recommendation string

---

## 💻 Sample Output

```
══════════════════════════════════════════════════════
         INTELLIGENT RESUME ANALYZER — REPORT
══════════════════════════════════════════════════════
  Job Title   : Senior Data Scientist

  CANDIDATE PROFILE
  ──────────────────────────────────────
  Name        : Alice Chen
  Email       : alice.chen@email.com
  Experience  : 6.0 years
  Skills (5)  : Python, Machine Learning, SQL, TensorFlow, PyTorch

  MATCH SCORE BREAKDOWN
  ──────────────────────────────────────
  Skills      :  54.0 / 60
  Experience  :  30.0 / 30
  Education   :  10.0 / 10
  ──────────────────────
  TOTAL SCORE :  94.0 / 100

  RECOMMENDATION
  ──────────────────────────────────────
  🟢 Strong Match – Highly recommended for interview.
```

---

## 🛠 Skills Demonstrated

- **Python Programming** — Clean modular design, type hints, PEP 8 compliant
- **Text Processing** — Multi-pattern regex extraction, section parsing
- **Matching Algorithms** — Weighted multi-factor scoring system
- **JSON File Handling** — Structured save/load with error handling
- **Web Development** — Interactive HTML front-end deployed on Vercel

---

## 📹 Demo Video

[▶ Watch Demo on YouTube](https://youtu.be/6y9LKcZZjt4) 

---

## 👤 Author

**Swamy** | [GitHub](https://github.com/swamy-4422-v)

---

*Built for the HiDevs Intelligent Resume Analyzer challenge.*
