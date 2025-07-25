# 🤖 ATS Score Checker

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/) [![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-10a37f?logo=openai&logoColor=white)](https://openai.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, AI-powered Applicant Tracking System (ATS) resume checker and scoring dashboard. Instantly analyze your resume against any job description using LLMs (GPT-4o), advanced skill extraction, and beautiful interactive charts.

---

## 🚀 Features
- *LLM-powered scoring:* Uses GPT-4o to analyze and score Education, Skills, and Experience.
- *Advanced skill matching:* Extracts both required (JD) and resume-listed skills, highlighting matched and missing ones.
- *Interactive visualizations:* Modern Plotly radar, bar, and pie charts for section scores and skill coverage.
- *Intelligent job requirements extraction:* Gathers requirements from bullet points, section headers, and key verbs.
- *Beautiful UI:* Clean, dark-themed dashboard with clear sectioning and branding.
- *Personal branding:* Sidebar includes links and contact info for [Rizwan Rizwan](https://www.linkedin.com/in/rizwan-rizwan-1351a650/).

---

## 📸 UI Preview
![ATS Score Checker UI](assets/ats-ui-screenshot.png) 

---

## 🛠 Quickstart

1. *Clone the repo:*
   bash
   git clone https://github.com/Rizwankaka/ATS-score-checker.git
   cd ATS-score-checker
   
2. *Install dependencies:*
   bash
   pip install -r requirements.txt
   # or, if using pyproject.toml
   pip install .
   
3. *Run the app:*
   bash
   streamlit run app.py
   

---

## 💡 How to Use
1. *Enter your OpenAI, Groq, or Gemini API key(s) in the sidebar.*
2. *Upload a resume (PDF or DOCX).*
3. *Paste the job description.*
4. *Click "Run ATS Evaluation".*
5. *View your ATS scores, matched/missing skills, and actionable feedback with interactive charts.*

---

## 🔑 API Keys
- *OpenAI API key required* for GPT-4o scoring. Get yours at [platform.openai.com](https://platform.openai.com/).
- Keys are stored locally and never shared.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE)

---

## 👤 Author & Branding
*Rizwan Rizwan*  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077b5?logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/rizwan-rizwan-1351a650/) [![YouTube](https://img.shields.io/badge/-YouTube-ff0000?logo=youtube&logoColor=white&style=flat-square)](https://www.youtube.com/@RizwanRizwan2R) [![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=flat-square)](https://github.com/Rizwankaka) [![Kaggle](https://img.shields.io/badge/-Kaggle-20beff?logo=kaggle&logoColor=white&style=flat-square)](https://www.kaggle.com/rizwanrizwannazir)  
✉ researcher@datafyassociates.com

---

## 🌐 Repo
[github.com/Rizwankaka/ATS-score-checker](https://github.com/Rizwankaka/ATS-score-checker)

---

> Built with ❤ by Rizwan Rizwan. Powered by OpenAI, Streamlit, and Plotly.
{resume_text}

Respond with:
Score: <number>
Explanation: <detailed reasoning>
```

---

- Modular code: extend modules/ for new LLMs, parsers, or features.
- API keys are stored locally and never shared.
- For issues or feature requests, open an issue or PR.
