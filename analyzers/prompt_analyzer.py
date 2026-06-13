import json

from services.gemini_service import (
    analyze_prompt
)

def get_analysis(prompt):

    result = analyze_prompt(prompt)

    cleaned = (
        result
        .replace("```json", "")
        .replace("```", "")
    )
    # parser the data into a dictionary and return it
    return json.loads(cleaned)