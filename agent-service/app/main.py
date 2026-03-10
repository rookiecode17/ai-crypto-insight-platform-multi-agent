from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import build_graph

app = FastAPI(title="AI Crypto Insight Agent")
graph = build_graph()


class OutlookRequest(BaseModel):
    coin_id: str = "bitcoin"
    vs_currency: str = "usd"
    days: int = 30


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent/outlook")
def outlook(req: OutlookRequest):
    result = graph.invoke(
        {"coin_id": req.coin_id, "vs_currency": req.vs_currency, "days": req.days}
    )
    return result["outlook"]
