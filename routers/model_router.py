from registry.models import MODELS

def recommend_model(
    coding,
    reasoning,
    creativity
):

    if coding > 85:
        return "claude-sonnet"

    if reasoning > 80:
        return "claude-sonnet"

    if coding > 60:
        return "deepseek-v3"

    return "gemini-2.5-flash"