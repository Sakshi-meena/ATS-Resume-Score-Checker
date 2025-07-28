# Helper functions for ATS system
import os
from typing import List, Tuple, Set
import re

# Curated list of common technical, business, and soft skills
SKILLS_WHITELIST = set([
    # Technical
    "python", "r", "java", "c++", "c#", "sql", "nosql", "mongodb", "mysql", "postgresql", "oracle", "excel", "powerpoint", "word", "tableau", "power bi", "sas", "stata", "matlab", "vba", "html", "css", "javascript", "typescript", "react", "angular", "node.js", "flask", "django", "spring", "aws", "azure", "gcp", "docker", "kubernetes", "git", "linux", "bash", "unix", "jira", "confluence", "rest api", "graphql", "machine learning", "deep learning", "nlp", "data science", "data analysis", "data visualization", "statistics", "regression", "classification", "clustering", "forecasting", "etl", "big data", "hadoop", "spark", "airflow", "ci/cd", "devops",
    # Business
    "project management", "agile", "scrum", "kanban", "stakeholder management", "budgeting", "forecasting", "business analysis", "requirement gathering", "risk management", "product management", "crm", "erp", "salesforce", "marketing", "seo", "sem", "content marketing", "digital marketing", "market research", "customer service", "supply chain", "logistics", "procurement", "negotiation", "accounting", "finance", "financial modeling", "investment analysis", "presentation", "public speaking", "report writing", "documentation", "training", "mentoring",
    # Soft skills
    "communication", "teamwork", "leadership", "problem solving", "critical thinking", "creative thinking", "adaptability", "time management", "organization", "collaboration", "conflict resolution", "decision making", "attention to detail", "initiative", "self-motivation", "empathy", "emotional intelligence", "persuasion", "networking", "active listening", "customer focus", "multitasking", "work ethic", "stress management", "flexibility", "analytical skills", "resourcefulness", "presentation skills"
])

import re
from typing import Set, Tuple, List

def extract_skills_from_text(text: str) -> Set[str]:
    text = text.lower()
    found_skills = set()
    for skill in SKILLS_WHITELIST:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.add(skill)
    return found_skills

def extract_all_resume_skills(text: str) -> Set[str]:
    """
    Extract plausible skills listed in resume by looking for lines with commas, bullets, or sections titled 'Skills'.
    """
    text = text.lower()
    skills = set()
    # Extract lines under 'skills' section
    skill_section = re.findall(r'skills[\s:]*([\s\S]{0,400})', text)
    for block in skill_section:
        # Split by comma, semicolon, newlines
        for part in re.split(r'[\n,;•\-]', block):
            s = part.strip().replace('.', '')
            if 2 < len(s) < 40 and any(c.isalpha() for c in s):
                skills.add(s)
    # Also pick up any comma-separated lines
    for line in text.splitlines():
        if ',' in line or '•' in line:
            for part in re.split(r'[\n,;•\-]', line):
                s = part.strip().replace('.', '')
                if 2 < len(s) < 40 and any(c.isalpha() for c in s):
                    skills.add(s)
    # Remove obvious non-skills
    blacklist = {'skills', 'summary', 'experience', 'education', 'work', 'professional', 'profile', 'responsibilities', 'projects', 'objective', 'certifications', 'languages', 'interests'}
    skills = {s for s in skills if s not in blacklist}
    return skills

def match_skills(job_description: str, resume_text: str) -> Tuple[List[str], List[str], List[str], List[str]]:
    jd_skills = sorted(list(extract_skills_from_text(job_description)))
    resume_whitelist_skills = sorted(list(extract_skills_from_text(resume_text)))
    resume_all_skills = sorted(list(extract_all_resume_skills(resume_text)))
    matched = sorted(list(set(jd_skills) & set(resume_whitelist_skills + resume_all_skills)))
    missing = sorted(list(set(jd_skills) - set(matched)))
    return jd_skills, resume_all_skills, matched, missing

def get_file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1].lower()

def filter_top_resumes(results: List[dict], threshold: int = 70) -> List[dict]:
    """Return resumes with score >= threshold."""
    return [r for r in results if r.get('score', 0) >= threshold]

