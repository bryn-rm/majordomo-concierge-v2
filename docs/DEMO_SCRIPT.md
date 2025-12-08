# Demo Script (10 Minutes)

## Opening (1 min)
- Introduce Majordomo Concierge V2 and seven agents.
- Mention ADK root agent at `majordomo_agent/agent.py`.

## Warm-up (2 min)
- Prompt: “Hello, who are you?”
- Expect: Majordomo introduction + capabilities list.

## Research (Oracle) (1 min)
- Prompt: “What’s the latest news about AI?”
- Expect: Oracle runs Brave/Wikipedia via MCP, returns concise summary with sources.

## Memory (Scribe) (1 min)
- Prompt: “Remember I like pizza.”
- Prompt: “What do I like?”
- Expect: Preference stored/retrieved from `journal.db`.

## Finance (Comptroller) (1.5 min)
- Prompt: “I spent £52.30 at Tesco.”
- Expect: Auto-categorized to Groceries, expense logged, budget status shown with % and remaining days.

## Productivity (Taskmaster) (1.5 min)
- Prompt: “Good morning.”
- Expect: Daily briefing with tasks, habits, budgets, and weather hook via Oracle.

## Lifestyle (Concierge) (1 min)
- Prompt: “Add a recipe for lemon pasta.”
- Prompt: “Find a recipe with pasta.”
- Expect: Stored and returned from `recipes.db`, shopping list optional.

## Smart Home (Sentinel) (0.5 min)
- Prompt: “Turn on the living room lights.”
- Expect: Simulated confirmation (no real devices).

## Closing (0.5 min)
- Highlight privacy (local SQLite), cost optimization (Flash/Lite + caching), and MCP integrations.
