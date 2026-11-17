# Using This Template

This document provides step-by-step guidance for instantiating a new solution from this template.

> **💡 Quick Tip:** To have your AI coding agent (Antigravity CLI, Cursor, Claude Code, Gemini CLI) execute this setup autonomously, run the prompt in [`Using-This-Template-Prompt.md`](Using-This-Template-Prompt.md).

---

## 🔍 Step 1: Project Naming & Placeholders
When creating a new project from this template, choose a project name and derive two formats:
1. **`kebab-case`**: Used for directory names, repository names, and service identifiers (e.g., `my-solution`).
2. **`snake_case`**: Used for database names, dataset identifiers, and Python module names (e.g., `my_solution`).

Search the repository for `[REPLACE_ME]` or generic placeholders and update them with your project details:
- Project Name in `README.md` and `AUTHORS.md`.
- Target environment variables in `agent-config.json`.
- Architecture overview in `docs/llms.txt`.

---

## 🔗 Step 2: Universal Symlink Setup
Ensure universal symlinks point to `AGENTS.md` so all AI assistants follow the same system instructions. Run from the project root:

```bash
# Create the symbolic links pointing to AGENTS.md
ln -sf AGENTS.md .cursorrules
ln -sf AGENTS.md .clinerules
ln -sf AGENTS.md CLAUDE.md
ln -sf AGENTS.md GEMINI.md

# Verify links
ls -la | grep AGENTS.md
```

---

## ⚙️ Step 3: Configure Environment State
Edit `agent-config.json` at the root of the project to match your target environment:

```json
{
  "environment": "dev",
  "project-id": "my-solution-dev",
  "region": "us-central1",
  "database-name": "my_solution_db",
  "storage-bucket": "my-solution-storage-bucket",
  "service-identity": "my-solution-sa@my-solution-dev.local"
}
```

---

## 📝 Step 4: Define Requirements & Architecture
1. **Requirements:** Place customer requirements, user stories, or PRDs in `docs/requirements/`.
2. **Architecture Spec:** Update `docs/llms.txt` with your data plane topology, APIs, and schema contracts.
3. **Feature Decomposition:** Author initial feature specifications in `docs/design/DESIGN-01-*.md`.

---

## 🔄 Step 5: Synchronize the Specification Ledger
Run the deterministic spec ledger to validate YAML frontmatter, track prompt hashes, and generate `docs/design/index.md`:

```bash
python3 .agents/skills/spec-ledger/scripts/run.py
```

---

## 🧪 Step 6: Verify Governance & Tests
Run automated security and compliance evaluations:

```bash
pytest evals/security-audits/
```
