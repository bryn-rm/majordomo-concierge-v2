# Getting Started

1. **Install dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
2. **Environment variables**
   - Copy `.env.example` → `.env`
   - Add `GOOGLE_API_KEY` and `BRAVE_API_KEY`
3. **Initialize databases**
   ```bash
   python scripts/setup/init_databases.py
   ```
4. **Run the app**
   ```bash
   adk web
   ```
5. **Smoke test**
   - “Hello, who are you?” → Majordomo intro
   - “What’s the latest news about AI?” → Oracle uses Brave search
   - “I spent £50 at Tesco” → Comptroller logs expense with budget context

## Project Layout
- `majordomo_agent/agent.py` — root agent exported as `root_agent`
- `src/majordomo_concierge_v2/agents/` — agent factories and prompts
- `src/majordomo_concierge_v2/tools/` — MCP + local tools
- `src/majordomo_concierge_v2/memory/` — SQLite stores and cache
- `scripts/setup/` — install + init scripts

## Troubleshooting
- Missing databases: rerun `python scripts/setup/init_databases.py`
- MCP errors: ensure `npx` is installed and `.env` has `BRAVE_API_KEY`
- Root agent not found: confirm `majordomo_agent/agent.py` exports `root_agent`
