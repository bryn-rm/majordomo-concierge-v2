# Majordomo Concierge V2

Production-ready multi-agent concierge built on Google ADK. Majordomo orchestrates seven specialists (Oracle, Scribe, Comptroller, Archivist, Concierge, Sentinel, Taskmaster) to handle research, memory, finance, documents, lifestyle, smart home simulation, and productivity.

## Quick Start
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add `GOOGLE_API_KEY` and `BRAVE_API_KEY`.
4. `python scripts/setup/init_databases.py`
5. `adk web --config config/adk_config.yaml` from the project root (root agent: `majordomo_agent.agent:root_agent`).

## Features
- 🧠 **Majordomo orchestration** with seven delegated specialists
- 🌐 **Oracle** web + Wikipedia via MCP Brave Search/Wikipedia
- 📝 **Scribe** journaling, preferences, and memory recall
- 💸 **Comptroller** expense logging, auto-categorization, and budgets
- 📂 **Archivist** document/memory indexing and search
- 🍽️ **Concierge** recipes, shopping list, and lifestyle suggestions
- 🏠 **Sentinel** smart home control (simulated)
- ✅ **Taskmaster** todos, habits, and daily briefing generator

## Architecture
- Root agent defined in `majordomo_agent/agent.py` (exports `root_agent`).
- Python package under `src/majordomo_concierge_v2/` with agents, tools, orchestration, memory stores, and prompts.
- SQLite data stores live in `data/databases/` (journal.db, finance.db, tasks.db, recipes.db).
- MCP toolsets configured for Brave Search and Wikipedia.

## Demo Commands
- “Hello, who are you?” → Majordomo intro
- “What’s the latest news about AI?” → Oracle web search
- “Remember I like pizza” → Scribe stores preference
- “I spent £50 at Tesco” → Comptroller logs and reports budget status
- “Good morning” → Taskmaster briefing (weather hook, calendar, tasks, budgets)

## Environment
- Requires Python 3.11+ and Google ADK ≥1.19.0.
- Set `GOOGLE_API_KEY` and `BRAVE_API_KEY` in `.env`.

## Troubleshooting
- Re-run `python scripts/setup/init_databases.py` if SQLite files are missing.
- Ensure `npx` is available for MCP tool servers (Brave/Wikipedia).
- If ADK cannot find the root agent, confirm `majordomo_agent/agent.py` exports `root_agent` and run with `adk web --config config/adk_config.yaml`.
- For tests: `python -m pytest`

## License
MIT License. See `LICENSE`.
