# Architecture Overview

## Agent Topology
- **Majordomo (root)**: Orchestrator delegating to seven specialists.
- **Oracle**: Brave Search + Wikipedia via MCP toolsets.
- **Scribe**: Journal, preferences, and calendar/date parsing.
- **Comptroller**: Finance tracking, auto-categorization, and budgets.
- **Archivist**: Document and memory indexing/search.
- **Concierge**: Lifestyle (recipes, shopping list).
- **Sentinel**: Smart home simulation.
- **Taskmaster**: Tasks, habits, and daily briefings.

## Packages
- `majordomo_agent/agent.py`: ADK entrypoint exposing `root_agent`.
- `src/majordomo_concierge_v2/agents/`: Agent factories and prompts.
- `src/majordomo_concierge_v2/tools/`: Local tools (finance, tasks, recipes) and MCP integrations.
- `src/majordomo_concierge_v2/memory/`: SQLite persistence layer and cache.
- `src/majordomo_concierge_v2/orchestration/`: Routing, workflows, and cost controls.
- `scripts/setup/`: Install + database initialization helpers.

## Data Layer
- SQLite databases under `data/databases/`:
  - `journal.db`: journal_entries, conversations, preferences
  - `finance.db`: expenses, budgets
  - `tasks.db`: tasks, habits
  - `recipes.db`: recipes
- `VectorStore`: optional ChromaDB with in-memory fallback.

## Tooling
- **MCP**: Brave Search + Wikipedia via `MCPToolset` + `StdioServerParameters`.
- **FunctionTool**: Wraps local Python functions for CRUD operations.
- **AgentTool**: Wraps specialist agents for Majordomo delegation.

## Cost Controls
- Lightweight cache (`CacheManager`) and model selection:
  - Flash Lite for Sentinel/Taskmaster
  - Flash for Oracle/Archivist/Concierge
  - Flash full for Majordomo/Scribe/Comptroller

## Request Flow
1. `adk web` loads `root_agent`.
2. Majordomo receives a prompt, routes intent, and calls appropriate AgentTool.
3. Specialists invoke MCP or local FunctionTools.
4. Results are synthesized and returned to the user.
