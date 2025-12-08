"""Sentinel agent factory (simulated smart home)."""

from google.adk.agents import Agent

from ..agents.base import wrap_functions
from ..prompts import SENTINEL_PROMPT


def set_light(room: str, state: str = "on") -> str:
    """Simulate toggling a light."""
    return f"Set {room} lights {state} (simulated)."


def set_temperature(celsius: float) -> str:
    """Simulate thermostat adjustment."""
    return f"Adjusted thermostat to {celsius:.1f}°C (simulated)."


def create_sentinel_agent() -> Agent:
    """Build the Sentinel agent."""
    tools = wrap_functions([set_light, set_temperature])
    return Agent(
        name="sentinel",
        model="gemini-2.5-flash-lite",
        description="Controls smart home devices (simulation).",
        instruction=SENTINEL_PROMPT,
        tools=tools,
    )
