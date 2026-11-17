# Agent Skills & Scripting Standards
**Trigger:** Read this file whenever you are asked to write a new Python script, CLI automation, or custom Agent Skill (`SKILL.md` / `run.py`).

## 🌐 1. Dependency Preferences (Lightweight & Portable)
- **Highly Preferred:** Default to lightweight, standard libraries and minimal third-party dependencies (e.g., standard library, `requests` or `httpx`). Keep the agent execution environment lightweight, fast, and portable.
- **Client Libraries:** Use specialized SDKs or thick client libraries only when necessary (e.g., complex binary protocols, streaming, or large chunked transfers).
- **Explicit Requirements:** Every skill script that uses external packages must declare them in its local `scripts/requirements.txt`.

## 📂 2. Skill Directory Structure
All custom skills designed for the AI agent must adhere to this standardized layout:
- Path: `.agents/skills/[skill-name]/`
- `SKILL.md`: The markdown definition telling the agent what the tool does, when to invoke it, and example code.
- `scripts/run.py`: The execution logic implementing the capability.
- `scripts/requirements.txt`: The required dependencies for the script.

## 📥 3. Dynamic Configuration Pattern (CRITICAL)
When providing example usage or writing execution scripts in a skill, **NEVER hardcode project IDs, regions, endpoints, or resource names.**

You MUST instruct the agent to dynamically append the script path and load environment variables from `agent-config.json` at the workspace root:

```python
import sys
import os
import json
from pathlib import Path

# 1. Resolve project root and append skill path dynamically
WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
SKILL_DIR = WORKSPACE_ROOT / ".agents" / "skills" / "[skill-name]" / "scripts"
sys.path.append(str(SKILL_DIR))

import run

# 2. Read the environment config from workspace root
config_file = WORKSPACE_ROOT / "agent-config.json"
with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)

# 3. Call the function using config values dynamically
result = run.execute_task(
    project_id=config["project-id"],
    region=config.get("region", "us-central1")
)
print(result)
```

## 🛡️ 4. Robust Execution & Error Handling
- **Idempotency:** Scripts should be safe to run multiple times without duplicating state or corrupting resources.
- **Meaningful Exit Codes:** Return exit code `0` on success and non-zero on failure.
- **Structured Output:** Return JSON or well-formatted summaries so the agent can parse execution outcomes reliably.
