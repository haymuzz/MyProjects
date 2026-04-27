from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MovieLens Recommendation API")

class Recommendation(BaseModel):
    user_id: int
    item_id: int
    score: float

@app.get("/")
def healthcheck():
    return {"status": "ok", "service": "recommendation-api"}

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, k: int = 10):
    # TODO: заменить на реальные рекомендации модели
    return {
        "user_id": user_id,
        "k": k,
        "recommendations": []
    }
