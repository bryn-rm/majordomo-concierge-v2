"""Weather lookup stub with optional OpenWeather integration."""

from __future__ import annotations

import os
from typing import Optional

import httpx


def get_weather(city: str = "London", country: str = "GB") -> str:
    """Fetch current weather via OpenWeather if API key exists, else return a stub."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return f"Weather lookup unavailable (missing OPENWEATHER_API_KEY). Assume clear skies in {city}."

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": f"{city},{country}", "appid": api_key, "units": "metric"}
        resp = httpx.get(url, params=params, timeout=5.0)
        resp.raise_for_status()
        data = resp.json()
        main = data.get("weather", [{}])[0].get("description", "unknown")
        temp = data.get("main", {}).get("temp")
        feels = data.get("main", {}).get("feels_like")
        return f"{city}: {main}, {temp}°C (feels {feels}°C)"
    except Exception as exc:
        return f"Weather lookup failed: {exc}"
