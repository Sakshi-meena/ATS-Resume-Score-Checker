# from typing import Dict
# import openai
# import google.generativeai as genai

# def query_llm(llm_choice: str, prompt: str, api_keys: Dict[str, str]) -> str:
#     """
#     Query the selected LLM with the given prompt and API keys.
#     llm_choice: 'OpenAI GPT-4o', 'Groq (Mixtral)', or 'Gemini Pro'
#     Returns: LLM response as string
#     """

#     # ✅ OpenAI GPT-4o
#     if llm_choice.startswith("OpenAI"):
#         try:
#             client = openai.OpenAI(api_key=api_keys.get("openai"))
#             response = client.chat.completions.create(
#                 model="gpt-4o",
#                 messages=[{"role": "user", "content": prompt}],
#                 max_tokens=600,
#                 temperature=0.2,
#             )
#             return response.choices[0].message.content.strip()
#         except Exception as e:
#             return f"OpenAI Error: {str(e)}"

#     # ✅ Gemini Pro (Google Generative AI)
#     elif llm_choice.startswith("Gemini"):
#         try:
#             genai.configure(api_key=api_keys.get("gemini"))
#             model = genai.GenerativeModel(model_name="models/gemini-pro")  # ✅ CORRECTED LINE
#             response = model.generate_content(prompt)
#             return response.text.strip()
#         except Exception as e:
#             return f"Gemini Error: {str(e)}"

#     # 🔧 TODO: Add Groq here when you're ready
#     # elif llm_choice.startswith("Groq"):
#     #     ...

#     # 🪂 Fallback if no LLM worked
#     return (
#         "Education Score: 0\nEducation Reasoning: Not evaluated.\nEducation Suggestions: N/A\n"
#         "Skills Score: 0\nSkills Reasoning: Not evaluated.\nSkills Suggestions: N/A\n"
#         "Experience Score: 0\nExperience Reasoning: Not evaluated.\nExperience Suggestions: N/A\n"
#         "Final Score: 0\nOverall Explanation: No LLM response."
#     )


#real one

# Handles LLM selection, API auth, and querying
from typing import Dict, Tuple

import openai

def query_llm(llm_choice: str, prompt: str, api_keys: Dict[str, str]) -> str:
    """
    Query the selected LLM with the given prompt and API keys.
    llm_choice: 'OpenAI GPT-4o', 'Groq (Mixtral)', or 'Gemini Pro'
    api_keys: dict with possible keys: 'openai', 'groq', 'gemini'
    Returns: LLM response as string
    """
    if llm_choice.startswith("OpenAI"):
        client = openai.OpenAI(api_key=api_keys.get("openai"))
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.2,
        )
        return response.choices[0].message.content
    # Optionally, add Groq and Gemini (Google Generative AI) support here
    # For now, return a fallback response
    return (
        "Education Score: 0\nEducation Reasoning: Not evaluated.\nEducation Suggestions: N/A\n"
        "Skills Score: 0\nSkills Reasoning: Not evaluated.\nSkills Suggestions: N/A\n"
        "Experience Score: 0\nExperience Reasoning: Not evaluated.\nExperience Suggestions: N/A\n"
        "Final Score: 0\nOverall Explanation: No LLM response."
    )
