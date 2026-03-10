from typing import List
from pydantic import BaseModel, Field


class AgentContribution(BaseModel):
    agent: str
    summary: str


class MarketView(BaseModel):
    market_summary: str = Field(description="Concise summary of current market context")
    stance_hint: str = Field(description="bullish, bearish, or neutral")
    key_observations: List[str] = Field(default_factory=list)


class SignalView(BaseModel):
    stance_hint: str = Field(description="bullish, bearish, or neutral")
    confidence_hint: float = Field(description="Number from 0 to 1")
    signals: List[str] = Field(default_factory=list)


class RiskView(BaseModel):
    risk_level: str = Field(description="low, medium, or high")
    risks: List[str] = Field(default_factory=list)
    caution_summary: str


class IndicatorSnapshot(BaseModel):
    price_change_pct: float
    avg_volume: float
    ma7: float
    ma30: float
    volatility_pct: float
    ohlc_close_avg: float
    trend: str


class OutlookResult(BaseModel):
    stance: str = Field(description="bullish, bearish, or neutral")
    confidence: float = Field(description="Number from 0 to 1")
    summary: str
    signals: List[str]
    risks: List[str]
    indicatorSnapshot: IndicatorSnapshot
    contributors: List[AgentContribution] = Field(default_factory=list)