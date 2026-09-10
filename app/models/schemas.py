from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    project: str
    version: str


class PredictionResponse(BaseModel):
    case_id: str
    prediction: str
    confidence: float
    probabilities: dict[str, float]
    disclaimer: str