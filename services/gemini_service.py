import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("GEMINI_API_KEY"))
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def analyze_prompt(prompt: str):
    system_prompt = f"""
You are an AI Prompt Analyzer.

Analyze the user prompt and return JSON.

Fields:

task_type
complexity (1-10)
coding_score (0-100)
reasoning_score (0-100)
creativity_score (0-100)
domain

Prompt:
{prompt}
"""

    response = model.generate_content(
        system_prompt
    )

    return response.text