from app.llm import build_llm
from app.models.outlook import SignalView

llm = build_llm(temperature=0.15)


def analyze_signals(current_market: dict, indicators: dict, heuristic_signals: list[str]) -> dict:
    prompt = f"""
You are the Signal Agent in a crypto multi-agent system.
Refine the provided heuristic signals into a structured market signal view.
Do not provide financial advice.

Current market:
{current_market}

Indicators:
{indicators}

Heuristic signals:
{heuristic_signals}

Return:
- stance_hint: bullish / bearish / neutral
- confidence_hint: number from 0 to 1
- signals: up to 4 concise bullet points
"""
    structured_llm = llm.with_structured_output(SignalView)
    return structured_llm.invoke(prompt).model_dump()
