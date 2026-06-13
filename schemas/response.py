from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    task_type: str
    complexity: int
    coding_score: int
    reasoning_score: int
    creativity_score: int
    domain: str
    estimated_tokens: int
    recommended_model: str
    estimated_cost: float