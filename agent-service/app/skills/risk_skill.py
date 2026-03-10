def generate_risks(current_market: dict, indicators: dict) -> list[str]:
    risks: list[str] = []

    change = indicators.get("price_change_pct", 0)
    vol = indicators.get("volatility_pct", 0)
    trend = indicators.get("trend", "unknown")
    volume = current_market.get("total_volume", 0)

    if vol > 3:
        risks.append("High volatility may increase short-term downside risk.")
    else:
        risks.append("Even moderate volatility can still trigger sharp crypto price moves.")

    if abs(change) > 10:
        risks.append("Large recent moves may raise the risk of momentum reversal.")
    else:
        risks.append("Weak follow-through could reduce conviction in the current trend.")

    if trend == "bullish":
        risks.append("Bullish trend may weaken if buying volume fails to sustain price support.")
    elif trend == "bearish":
        risks.append("Bearish pressure may ease quickly if the market rebounds on stronger demand.")
    else:
        risks.append("Sideways markets can break unexpectedly in either direction.")

    if volume == 0:
        risks.append("Missing or thin volume data can reduce analysis reliability.")

    return risks[:4]
