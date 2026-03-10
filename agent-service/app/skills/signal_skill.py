def generate_signals(current_market: dict, indicators: dict) -> list[str]:
    signals: list[str] = []

    trend = indicators.get("trend", "unknown")
    change = indicators.get("price_change_pct", 0)
    vol = indicators.get("volatility_pct", 0)
    daily_change = current_market.get("price_change_percentage_24h", 0)

    if trend == "bullish":
        signals.append("Short-term moving average remains above the longer-term average.")
    elif trend == "bearish":
        signals.append("Short-term moving average remains below the longer-term average.")
    else:
        signals.append("Trend appears range-bound with limited separation between moving averages.")

    if change > 5:
        signals.append("Recent price momentum is positive over the selected time window.")
    elif change < -5:
        signals.append("Recent price momentum is negative over the selected time window.")
    else:
        signals.append("Price change is moderate without a strong directional breakout.")

    if daily_change > 2:
        signals.append("The latest 24h move suggests stronger near-term demand.")
    elif daily_change < -2:
        signals.append("The latest 24h move suggests weaker near-term sentiment.")
    else:
        signals.append("The latest 24h move is relatively muted.")

    if vol < 2:
        signals.append("Observed volatility is relatively contained.")
    else:
        signals.append("Volatility remains elevated, suggesting larger short-term swings.")

    return signals[:4]
