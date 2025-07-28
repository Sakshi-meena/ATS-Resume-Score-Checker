from .llm_handler import query_llm
from typing import Dict, Any
import re

ATS_SCORING_PROMPT = '''Given the following resume and job description, evaluate the candidate in these areas:
- Education (score 0-100)
- Skills (score 0-100)
- Experience (score 0-100)

For each section, provide:
- Score
- Reasoning
- Suggestions to improve

At the end, provide a weighted final score (Education 25%, Skills 40%, Experience 35%).

IMPORTANT: ONLY output the following fields, in exactly this format, with NO extra commentary or text. Do not add explanations before or after. Do not use markdown or bullet points. Use numbers only for scores.

Job Description:
{job_description}

Resume:
{resume_text}

Respond with:
Education Score: <number>
Education Reasoning: <text>
Education Suggestions: <text>
Skills Score: <number>
Skills Reasoning: <text>
Skills Suggestions: <text>
Experience Score: <number>
Experience Reasoning: <text>
Experience Suggestions: <text>
Final Score: <number>
Overall Explanation: <text>
'''

def score_resume(resume_text: str, job_description: str, llm_choice: str, api_keys: Dict[str, str]) -> Dict[str, Any]:
    prompt = ATS_SCORING_PROMPT.format(job_description=job_description, resume_text=resume_text)
    response = query_llm(llm_choice, prompt, api_keys)

    result = {
        'education_score': 0,
        'education_reasoning': '',
        'education_suggestions': '',
        'skills_score': 0,
        'skills_reasoning': '',
        'skills_suggestions': '',
        'experience_score': 0,
        'experience_reasoning': '',
        'experience_suggestions': '',
        'final_score': 0,
        'overall_explanation': ''
    }

    if not response or "Error" in response:
        result['overall_explanation'] = f"LLM error or empty response.\n\n[DEBUG: Raw LLM output]\n{response}"
        return result

    try:
        # Clean up and parse each line
        lines = [line.strip() for line in response.splitlines() if line.strip()]
        for line in lines:
            key = line.lower().replace(" ", "").split(":")[0]
            value = line.partition(":")[2].strip()

            if key == "educationscore":
                result["education_score"] = int(re.findall(r"\d+", value)[0]) if re.findall(r"\d+", value) else 0
            elif key == "educationreasoning":
                result["education_reasoning"] = value
            elif key == "educationsuggestions":
                result["education_suggestions"] = value
            elif key == "skillsscore":
                result["skills_score"] = int(re.findall(r"\d+", value)[0]) if re.findall(r"\d+", value) else 0
            elif key == "skillsreasoning":
                result["skills_reasoning"] = value
            elif key == "skillssuggestions":
                result["skills_suggestions"] = value
            elif key == "experiencescore":
                result["experience_score"] = int(re.findall(r"\d+", value)[0]) if re.findall(r"\d+", value) else 0
            elif key == "experiencereasoning":
                result["experience_reasoning"] = value
            elif key == "experiencesuggestions":
                result["experience_suggestions"] = value
            elif key == "finalscore":
                result["final_score"] = int(re.findall(r"\d+", value)[0]) if re.findall(r"\d+", value) else 0
            elif key == "overallexplanation":
                result["overall_explanation"] = value

        # If still all scores are 0, something went wrong with parsing
        if all(result[k] == 0 for k in ['education_score', 'skills_score', 'experience_score', 'final_score']):
            result['overall_explanation'] += f"\n\n[DEBUG: Raw LLM output]\n{response}"

    except Exception as e:
        result['overall_explanation'] = f"Exception during parsing: {str(e)}\n\n[DEBUG: Raw LLM output]\n{response}"

    return result
