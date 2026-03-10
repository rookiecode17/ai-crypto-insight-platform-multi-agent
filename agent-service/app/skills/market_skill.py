import os
import requests

BASE_URL = "https://api.coingecko.com/api/v3"
DEMO_KEY = os.getenv("COINGECKO_DEMO_API_KEY", "")


def _headers() -> dict:
    if DEMO_KEY:
        return {"x-cg-demo-api-key": DEMO_KEY}
    return {}


def get_current_market(coin_id: str = "bitcoin", vs_currency: str = "usd") -> dict:
    response = requests.get(
        f"{BASE_URL}/coins/markets",
        params={"vs_currency": vs_currency, "ids": coin_id},
        headers=_headers(),
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()
    return data[0] if data else {}


def get_history_market(coin_id: str = "bitcoin", vs_currency: str = "usd", days: int = 30) -> dict:
    response = requests.get(
        f"{BASE_URL}/coins/{coin_id}/market_chart",
        params={"vs_currency": vs_currency, "days": days},
        headers=_headers(),
        timeout=20,
    )
    response.raise_for_status()
    return response.json()
