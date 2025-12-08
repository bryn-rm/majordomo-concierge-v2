#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
python scripts/setup/init_databases.py
echo "Installation complete. Run 'source .venv/bin/activate' then 'adk web'."
