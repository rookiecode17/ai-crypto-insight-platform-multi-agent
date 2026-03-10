from app.llm import build_llm
from app.models.outlook import OutlookResult

llm = build_llm(temperature=0.2)


def synthesize_outlook(
    coin_id: str,
    current_market: dict,
    indicators: dict,
    market_view: dict,
    signal_view: dict,
    risk_view: dict,
) -> dict:
    prompt = f"""
You are the Supervisor Agent in a crypto multi-agent system.
Your job is to synthesize specialist outputs into the final outlook.
Do not provide direct trading advice.

Coin:
{coin_id}

Current market:
{current_market}

Indicators:
{indicators}

Market agent view:
{market_view}

Signal agent view:
{signal_view}

Risk agent view:
{risk_view}

Return:
- stance: bullish / bearish / neutral
- confidence: number from 0 to 1
- summary: 2-4 concise sentences
- signals: up to 4 concise bullet points
- risks: up to 4 concise bullet points
- indicatorSnapshot: return the indicators exactly
- contributors: list 3 items with agent and summary for Market Agent, Signal Agent, Risk Agent
"""
    structured_llm = llm.with_structured_output(OutlookResult)
    result = structured_llm.invoke(prompt).model_dump()
    result["indicatorSnapshot"] = indicators
    return result
