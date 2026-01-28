# ATS Score Checker

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/) [![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-10a37f?logo=openai&logoColor=white)](https://openai.com/)

A modern, AI-powered Applicant Tracking System (ATS) resume checker and scoring dashboard. Instantly analyze your resume against any job description using LLMs (GPT-4o), advanced skill extraction, and beautiful interactive charts.

Deployment & Security: Environment-based API keys (.env)
## Features
- *LLM-powered scoring:* Uses GPT-4o to analyze and score Education, Skills, and Experience.
- *Advanced skill matching:* Extracts both required (JD) and resume-listed skills, highlighting matched and missing ones.
- *Interactive visualizations:* Modern Plotly radar, bar, and pie charts for section scores and skill coverage.
- *Intelligent job requirements extraction:* Gathers requirements from bullet points, section headers, and key verbs.
- *Beautiful UI:* Clean, dark-themed dashboard with clear sectioning and branding..

---
## Technologies Used

* **Frontend & UI:** Streamlit
* **Backend:** Python
* **AI / NLP:** OpenAI GPT-3.5, Groq Mixtral, Gemini Pro
* **Text Processing:** Regex, NLTK
* **Visualization:** Plotly (Radar, Bar, Pie charts)
* **Deployment & Security:** Environment-based API keys (.env)
---
## Quickstart

1. *Clone the repo:*
   bash
   https://github.com/Sakshi-meena/ATS-Resume-Score-Checker.git
   cd ATS-score-checker
   
2. *Install dependencies:*
   bash
   pip install -r requirements.txt
   or, if using pyproject.toml
   pip install .
   
4. *Run the app:*
   bash
   streamlit run app.py
   
---

## How to Use
1. *Enter your OpenAI, Groq, or Gemini API key(s) in the sidebar.*
2. *Upload a resume (PDF or DOCX).*
3. *Paste the job description.*
4. *Click "Run ATS Evaluation".*
5. *View your ATS scores, matched/missing skills, and actionable feedback with interactive charts.*

---

## API Keys
- *OpenAI API key required* for GPT-4o scoring. Get yours at [platform.openai.com](https://platform.openai.com/).
- Keys are stored locally and never shared.

---

## Project Demo 
https://ats-resume-score-checker-mtb3f24ml74euzywep7kry.streamlit.app/

---

## Final System Flow

```
User
 |
 | Upload Resume (PDF/DOCX)
 | Paste Job Description
 v
Streamlit UI
 |
 | Text Extraction (parser)
 v
Resume & JD Text
 |
 | Regex → Extract sections, bullets
 | NLP → Match skills intelligently
 v
Scoring Engine
 |
 | Calculate section-wise scores:
 | - Education
 | - Skills
 | - Experience
 | Generate final ATS score (0–100)
 v
Plotly Visualizations
 |
 | Radar Chart → Section Scores
 | Bar Chart → Skill Coverage
 | Pie Chart → Skill Match Overview
 v
Interactive Dashboard → User Insights & Suggestions
