import os
import requests

BASE_URL = "https://api.coingecko.com/api/v3"
DEMO_KEY = os.getenv("COINGECKO_DEMO_API_KEY", "")


def get_ohlc(coin_id: str = "bitcoin", vs_currency: str = "usd", days: int = 30) -> list[list[float]]:
    headers = {"x-cg-demo-api-key": DEMO_KEY} if DEMO_KEY else {}
    response = requests.get(
        f"{BASE_URL}/coins/{coin_id}/ohlc",
        params={"vs_currency": vs_currency, "days": days},
        headers=headers,
        timeout=20,
    )
    response.raise_for_status()
    return response.json()
