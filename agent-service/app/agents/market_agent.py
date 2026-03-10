from app.llm import build_llm
from app.models.outlook import MarketView

llm = build_llm(temperature=0.1)


def analyze_market_context(current_market: dict, history: dict, indicators: dict) -> dict:
    prompt = f"""
You are the Market Agent in a crypto multi-agent system.
Summarize the market context using only the provided data.
Do not provide financial advice.

Current market:
{current_market}

History:
{history}

Indicators:
{indicators}

Return:
- market_summary: 2 concise sentences
- stance_hint: bullish / bearish / neutral
- key_observations: 3 short bullet points
"""
    structured_llm = llm.with_structured_output(MarketView)
    return structured_llm.invoke(prompt).model_dump()
