from app.llm import build_llm
from app.models.outlook import RiskView

llm = build_llm(temperature=0.15)


def analyze_risks(current_market: dict, indicators: dict, heuristic_risks: list[str]) -> dict:
    prompt = f"""
You are the Risk Agent in a crypto multi-agent system.
Refine the provided heuristic risks into a structured risk view.
Do not provide financial advice.

Current market:
{current_market}

Indicators:
{indicators}

Heuristic risks:
{heuristic_risks}

Return:
- risk_level: low / medium / high
- risks: up to 4 concise bullet points
- caution_summary: 1-2 concise sentences
"""
    structured_llm = llm.with_structured_output(RiskView)
    return structured_llm.invoke(prompt).model_dump()
