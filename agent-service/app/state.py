from typing import TypedDict, Dict, Any, List


class MarketState(TypedDict, total=False):
    coin_id: str
    vs_currency: str
    days: int

    current_market: Dict[str, Any]
    history: Dict[str, Any]
    ohlc: List[List[float]]

    indicators: Dict[str, Any]
    signals: List[str]
    risks: List[str]

    market_view: Dict[str, Any]
    signal_view: Dict[str, Any]
    risk_view: Dict[str, Any]

    summary: str
    confidence: float
    stance: str
    outlook: Dict[str, Any]
