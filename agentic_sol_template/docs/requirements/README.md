# Requirements & Context Staging (`docs/requirements/`)

This directory serves as the intake staging area for raw requirements, PRDs, user stories, architecture diagrams, and problem statements.

## How to Use This Directory
1. **Stage Raw Inputs:** Place raw text, PDFs, user stories, API contracts, or customer interview notes here.
2. **Master Agentic Prompt:** Use [`MASTER_AGENTIC_PROMPT.md`](MASTER_AGENTIC_PROMPT.md) as the initial prompt to guide an AI agent through context ingestion, architecture synthesis (`docs/llms.txt`), and feature decomposition (`docs/design/DESIGN-*.md`).
3. **Traceability:** Keep raw inputs intact so the agent and human developers can cross-reference business drivers against technical designs.
