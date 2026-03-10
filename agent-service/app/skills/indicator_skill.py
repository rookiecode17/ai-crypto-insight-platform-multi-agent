from statistics import mean


def calc_indicators(history: dict, ohlc: list) -> dict:
    prices = history.get("prices", [])
    volumes = history.get("total_volumes", [])

    if len(prices) < 2:
        return {
            "price_change_pct": 0,
            "avg_volume": 0,
            "ma7": 0,
            "ma30": 0,
            "volatility_pct": 0,
            "trend": "unknown",
        }

    price_values = [float(item[1]) for item in prices]
    volume_values = [float(item[1]) for item in volumes] if volumes else []

    first_price = price_values[0]
    last_price = price_values[-1]
    price_change_pct = ((last_price - first_price) / first_price) * 100 if first_price else 0

    ma7 = mean(price_values[-7:]) if len(price_values) >= 7 else mean(price_values)
    ma30 = mean(price_values[-30:]) if len(price_values) >= 30 else mean(price_values)
    avg_volume = mean(volume_values) if volume_values else 0

    returns = []
    for i in range(1, len(price_values)):
        prev_price = price_values[i - 1]
        cur_price = price_values[i]
        if prev_price != 0:
            returns.append((cur_price - prev_price) / prev_price * 100)

    volatility_pct = mean([abs(x) for x in returns]) if returns else 0

    if ma30 == 0:
        trend = "unknown"
    elif abs(ma7 - ma30) / ma30 < 0.01:
        trend = "sideways"
    elif ma7 > ma30:
        trend = "bullish"
    else:
        trend = "bearish"

    ohlc_closes = [row[4] for row in ohlc] if ohlc else []
    ohlc_close_avg = mean(ohlc_closes) if ohlc_closes else 0

    return {
        "price_change_pct": round(price_change_pct, 2),
        "avg_volume": round(avg_volume, 2),
        "ma7": round(ma7, 2),
        "ma30": round(ma30, 2),
        "volatility_pct": round(volatility_pct, 2),
        "ohlc_close_avg": round(ohlc_close_avg, 2),
        "trend": trend,
    }
