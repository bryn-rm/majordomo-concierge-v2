"""Basic health check for Majordomo Concierge setup."""

from __future__ import annotations

import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / "src"))

from majordomo_concierge_v2 import DATA_DIR, JOURNAL_DB, FINANCE_DB, TASK_DB, RECIPE_DB


def main() -> None:
    missing_env = [key for key in ("GOOGLE_API_KEY", "BRAVE_API_KEY") if not os.getenv(key)]
    if missing_env:
        print(f"Warning: missing environment variables: {', '.join(missing_env)}")
    else:
        print("Environment variables detected.")

    paths = [DATA_DIR, JOURNAL_DB, FINANCE_DB, TASK_DB, RECIPE_DB]
    for path in paths:
        print(f"{path}: {'exists' if Path(path).exists() else 'missing'}")


if __name__ == "__main__":
    main()
