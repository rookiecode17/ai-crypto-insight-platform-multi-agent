import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.models.outlook import OutlookResult

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.2,
    api_key=os.getenv("OPENAI_API_KEY"),
)


def generate_summary(current_market: dict, indicators: dict, signals: list[str], risks: list[str]) -> dict:
    prompt = f"""
You are a cautious crypto market analyst.

Given the following inputs, produce a concise and structured crypto outlook.
Do not provide direct financial advice.
Keep the tone analytical and practical.

Current market:
{current_market}

Indicators:
{indicators}

Signals:
{signals}

Risks:
{risks}

Return JSON matching the schema exactly.

Fields:
- stance: bullish / bearish / neutral
- confidence: number from 0 to 1
- summary: 2–4 sentences
- signals: use the provided signals
- risks: use the provided risks
- indicatorSnapshot:
  - price_change_pct
  - avg_volume
  - ma7
  - ma30
  - volatility_pct
  - ohlc_close_avg
  - trend
"""

    structured_llm = llm.with_structured_output(OutlookResult)
    result = structured_llm.invoke(prompt)

    return result.model_dump()