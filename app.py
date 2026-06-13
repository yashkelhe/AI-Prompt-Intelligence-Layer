from pydantic import BaseModel
from fastapi import FastAPI

from analyzers.prompt_analyzer import (
    get_analysis
)

from routers.model_router import (
    recommend_model
)

from estimators.token_estimator import (
    estimate_tokens
)

from estimators.cost_estimator import (
    estimate_cost
)

from registry.models import MODELS

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "AI Prompt Intelligence Layer"
    }


class PromptRequest(BaseModel):
    prompt: str

@app.post("/analyze")
def analyze(data: PromptRequest):
    print(data)
    prompt = data.prompt

    analysis = get_analysis(
        prompt
    )

    tokens = estimate_tokens(
        prompt
    )

    model = recommend_model(
        analysis["coding_score"],
        analysis["reasoning_score"],
        analysis["creativity_score"]
    )

    model_info = next(
        m for m in MODELS
        if m["name"] == model
    )

    cost = estimate_cost(
        tokens,
        model_info[
            "cost_per_1m_tokens"
        ]
    )

    return {
        "analysis": analysis,
        "recommended_model": model,
        "estimated_tokens": tokens,
        "estimated_cost": cost
    }