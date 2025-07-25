import streamlit as st
from modules import parser, scorer, llm_handler, utils
import os
from dotenv import load_dotenv

# Load .env as fallback for API keys
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

st.set_page_config(page_title="AI-Powered ATS Resume Shortlisting", page_icon="🧑‍💼", layout="wide")
st.title("🤖 AI-Powered ATS Resume Shortlisting System")

# Sidebar - API keys and LLM selection
st.sidebar.header("🔐 API Keys & LLM Selection")
llm_options = ["OpenAI gpt-3.5-turbo", "Groq (Mixtral)", "Gemini Pro"]
llm_choice = st.sidebar.selectbox("Select LLM", llm_options, index=0)

openai_key = st.sidebar.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
groq_key = st.sidebar.text_input("Groq API Key", value=os.getenv("GROQ_API_KEY", ""), type="password")
gemini_key = st.sidebar.text_input("Gemini API Key", value=os.getenv("GEMINI_API_KEY", ""), type="password")

st.sidebar.info("""
- Enter your API keys above (these stay local!)
- Select which LLM to use for matching
- Upload resumes and paste the job description below
""")

# --- Sakshi Meena details ---
st.sidebar.markdown("""
<hr style='border:1px solid #444;margin:1.2em 0;'>
<div style='text-align:center;'>
    <span style='font-size:1.3em;font-weight:bold;color:#4e54c8;'>Sakshi Meena</span><br>
     <a href='mailto:sakshimeena7357@gmail.com' target='_blank' style='margin:0 6px;'>
        <img src='https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/gmail.svg' width='28' height='28' alt='Gmail' style='vertical-align:middle;filter:invert(36%) sepia(83%) saturate(2083%) hue-rotate(346deg) brightness(97%) contrast(97%);'>
    </a>
     <a href='https://github.com/Sakshi-meena' target='_blank' style='margin:0 6px;'>
        <img src='https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg' width='28' height='28' alt='GitHub' style='vertical-align:middle;filter:invert(100%) grayscale(100%);'>
    </a>
    <a href='https://www.linkedin.com/in/sakshimeena' target='_blank' style='margin:0 6px;'>
        <img src='https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg' width='28' height='28' alt='LinkedIn' style='vertical-align:middle;filter:invert(33%) sepia(95%) saturate(746%) hue-rotate(182deg) brightness(94%) contrast(91%);'>
    </a>
    <a href='https://x.com/SMeena73?t=_1qWs4p3ihHZbmb8R-9KOA&s=09' target='_blank' style='margin:0 6px;'>
        <img src='https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/x.svg' width='28' height='28' alt='Twitter (X)' style='vertical-align:middle;filter:invert(100%) grayscale(100%);'>
    </a>
    <br>
    <span style='font-size:0.93em;color:#aaa;'>researcher@datafyassociates.com</span>
</div>
""", unsafe_allow_html=True)

# Main app - Upload resumes and job description
st.subheader("🧾 Upload Resumes (PDF/DOCX)")
resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=False)

st.subheader("📋 Paste Job Description")
job_description = st.text_area("Enter the job description here", height=200)

if st.button("Run ATS Evaluation"):
    if not resume_file or not job_description.strip():
        st.error("Please upload a resume and enter a job description.")
    else:
        import pandas as pd
        st.subheader("🎯 ATS Results")
        with st.spinner("Processing resume..."):
            resume_text = parser.extract_text(resume_file)
            ats_result = scorer.score_resume(
                resume_text,
                job_description,
                llm_choice,
                {"openai": openai_key, "groq": groq_key, "gemini": gemini_key}
            )
            ats_result["filename"] = resume_file.name
        # Extract requirements and improved skill matching using NLTK
        from modules.utils import match_skills
        # Improved Job Requirements extraction
        import re
        job_lines = [line.strip() for line in job_description.splitlines() if line.strip()]
        requirements = []
        # Extract bullet points and lines with key verbs
        for line in job_lines:
            l = line.lower()
            if (re.match(r'^[\-•*]', l) or
                any(word in l for word in ["require", "must", "should", "responsible", "expect", "qualif", "need"])):
                requirements.append(line)
        # Extract lines under 'requirements', 'qualifications', 'responsibilities' sections
        section_patterns = [r'requirements?', r'qualifications?', r'responsibilit(y|ies)']
        for i, line in enumerate(job_lines):
            for pat in section_patterns:
                if re.match(pat, line, re.IGNORECASE):
                    # Collect up to 10 lines after the section header
                    for next_line in job_lines[i+1:i+11]:
                        if next_line and not re.match(r'^[A-Z ]{4,}$', next_line):
                            requirements.append(next_line)
        # Deduplicate and filter
        requirements = list(dict.fromkeys([r for r in requirements if len(r) > 4]))
        if not requirements:
            requirements = job_lines

        jd_skills, resume_skills, matched_skills, missing_skills = match_skills(job_description, resume_text)

        # Infographic: Interactive and modern visualizations with Plotly
        import plotly.graph_objects as go
        import plotly.express as px
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(f"### 📝 {ats_result['filename']}")
            st.markdown("#### Section Scores (Radar Chart)")
            # Plotly radar/spider chart for section scores
            categories = ["Education", "Skills", "Experience"]
            scores = [ats_result["education_score"], ats_result["skills_score"], ats_result["experience_score"]]
            radar_fig = go.Figure()
            radar_fig.add_trace(go.Scatterpolar(r=scores + [scores[0]], theta=categories + [categories[0]], fill='toself', name='Section Score', line_color='#4e54c8'))
            radar_fig.update_layout(
                polar=dict(bgcolor='#262730', radialaxis=dict(visible=True, range=[0, 100], showticklabels=True, ticks=''), angularaxis=dict(linecolor='white', gridcolor='gray')),
                showlegend=False, paper_bgcolor='#262730', font_color='white', margin=dict(l=10, r=10, t=40, b=10), title_font_size=18, title_text='ATS Section Scores'
            )
            st.plotly_chart(radar_fig, use_container_width=True)
            # Interactive bar chart for skill coverage
            st.markdown("#### Skill Coverage (Bar Chart)")
            skill_labels = ["Matched Skills", "Missing Skills"]
            skill_counts = [len(matched_skills), len(missing_skills)]
            bar_fig = px.bar(x=skill_counts, y=skill_labels, orientation='h', color=skill_labels, color_discrete_sequence=["#4CAF50", "#FF6666"], text=skill_counts)
            bar_fig.update_layout(
                xaxis_title='Count', yaxis_title='', plot_bgcolor='#262730', paper_bgcolor='#262730', font_color='white',
                showlegend=False, margin=dict(l=10, r=10, t=40, b=10), title_font_size=18, title_text='Skill Coverage'
            )
            bar_fig.update_traces(textposition='outside')
            st.plotly_chart(bar_fig, use_container_width=True)
            # Interactive pie chart for skill match
            st.markdown("#### Skill Match Overview (Pie Chart)")
            sizes = [len(matched_skills), len(missing_skills)]
            labels = ['Matched', 'Missing']
            if sum(sizes) > 0:
                pie_fig = px.pie(values=sizes, names=labels, color=labels, color_discrete_map={'Matched':'#4CAF50','Missing':'#FF6666'}, hole=0.3)
                pie_fig.update_traces(textinfo='percent+label', textfont_size=14)
                pie_fig.update_layout(
                    showlegend=True, legend_title_text='', paper_bgcolor='#262730', font_color='white',
                    margin=dict(l=10, r=10, t=40, b=10), title_font_size=18, title_text='Skill Match Overview'
                )
                st.plotly_chart(pie_fig, use_container_width=True)
            else:
                st.info('No required skills found in the job description. Pie chart not displayed.')
        with col2:
            st.markdown(f"<div style='background:linear-gradient(90deg,#4e54c8,#8f94fb);padding:1.5em 1em;border-radius:16px;margin-bottom:1em;'>"
                        f"<span style='font-size:2em;font-weight:bold;color:white;'>Final Score: {ats_result['final_score']}/100</span>"
                        f"<br><span style='color:white;font-size:1.1em;'>{ats_result['overall_explanation']}</span>"
                        f"</div>", unsafe_allow_html=True)
            st.markdown("#### Job Requirements")
            for req in requirements:
                st.markdown(f"- {req}")
            st.markdown("#### Skills Overview")
            st.markdown(f"<span style='color:#2196f3;font-weight:bold;'>Required (JD) Skills:</span> {', '.join(jd_skills) if jd_skills else 'None'}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#ffa726;font-weight:bold;'>Skills Found in Resume:</span> {', '.join(resume_skills) if resume_skills else 'None'}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:lightgreen;font-weight:bold;'>Matched Skills:</span> {', '.join(matched_skills) if matched_skills else 'None'}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#ff6666;font-weight:bold;'>Missing Skills:</span> {', '.join(missing_skills) if missing_skills else 'None'}", unsafe_allow_html=True)
            st.markdown("#### Suggestions & Recommendations 🛠️")
            st.markdown(f"- **Education:** {ats_result['education_suggestions']}")
            st.markdown(f"- **Skills:** {ats_result['skills_suggestions']}")
            st.markdown(f"- **Experience:** {ats_result['experience_suggestions']}")
            st.markdown("#### Reasoning 🧠")
            st.markdown(f"- **Education:** {ats_result['education_reasoning']}")
            st.markdown(f"- **Skills:** {ats_result['skills_reasoning']}")
            st.markdown(f"- **Experience:** {ats_result['experience_reasoning']}")
