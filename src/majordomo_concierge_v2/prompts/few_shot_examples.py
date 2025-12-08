"""Few-shot examples used to prime agents."""

FEW_SHOT_EXAMPLES = [
    {
        "prompt": "Good morning!",
        "response": (
            "Good morning! Here's your briefing:\n"
            "- Weather: pull latest via Oracle.\n"
            "- Calendar: Scribe summarizes today's events.\n"
            "- Tasks: Taskmaster lists top priorities.\n"
            "- Budgets: Comptroller reports any alerts."
        ),
    },
    {
        "prompt": "I spent £50 at Tesco",
        "response": "Logged £50 to Groceries and updated your month-to-date budget status.",
    },
]
