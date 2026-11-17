# Agentic Project Structure & Intent-Driven Engineering

Welcome to the **Agentic Solution Engineering Template**. This repository is an optimized environment built for **Intent-Driven Engineering**.

In this paradigm, developers shift from *manually writing line-by-line boilerplate* to *architecting context, boundaries, and specifications*. You define the desired business outcomes, safety guardrails, and architectural rules in structured markdown specifications, and orchestrate AI agents (such as Antigravity CLI, Cursor, Claude Code, Windsurf, or Gemini) to generate, test, deploy, and verify solutions autonomously within those bounds.

---

## 🗺️ The 7-Layer Architecture Overview

This template enforces a strict separation of concerns across 7 distinct operational layers:

```text
.
├── AGENTS.md                  # Layer 1: Command & Control, agent persona, and routing
├── agent-config.json          # Layer 1: Environment state, project IDs, regions, resources
├── GEMINI.md / CLAUDE.md      # Layer 1: Universal symlinks resolving to AGENTS.md
├── .agents/
│   ├── rules/                 # Layer 2: Modular governance and safety guardrails
│   └── skills/                # Layer 3: Reusable agent automation tools & CLI extensions
├── docs/
│   ├── design/                # Layer 4: Feature design specs (DESIGN-*.md) and ledger index.md
│   ├── requirements/          # Layer 4: Raw inputs, customer requirements, Master Prompt
│   └── llms.txt               # Layer 4: Machine-readable system architecture and data plane
├── evals/                     # Layer 5: Automated verification, compliance, and security tests
│   └── security-audits/       # Layer 5: Automated secret scanning and configuration audits
├── graphify-out/              # Layer 6: Architectural dependency graph (Graphify output)
└── src/                       # Layer 7: Execution layer: applications, pipelines, and scripts
```

---

## 📂 Detailed Layer Breakdown

### Layer 1: Command, Control & State (`AGENTS.md` & `agent-config.json`)
- **`AGENTS.md`**: Master system instructions for AI coding assistants. It establishes agent identity, progressive disclosure domain routing, safety constraints, and the definition-of-done self-correction loop.
- **`agent-config.json`**: Machine-readable configuration storing active project identifiers, regions, endpoints, and service identities. All code and scripts read dynamically from this file; environment identifiers are never hardcoded.
- **Universal Symlinks (`.cursorrules`, `.clinerules`, `CLAUDE.md`, `GEMINI.md`)**: Direct symbolic links pointing to `AGENTS.md`, guaranteeing identical behavior across all AI tools and IDEs.

### Layer 2: Modular Governance & Guardrails (`.agents/rules/`)
Non-negotiable architectural constraints and security laws loaded progressively on-demand:
- `architecture_standards.md`: Declarative IaC, modular architecture, idempotency, and strict prohibition on unconfirmed destructive commands.
- `agent_skills_standards.md`: Standards for agent automation tools (lightweight dependencies, REST API preferences, dynamic config loading).
- `git_standards.md`: Read-only Git inspection protocols (agents cannot commit, push, or delete in version control).
- `secrets_management.md`: Zero-trust secrets standards (zero plain-text credentials, dynamic runtime environment injection, secure vaulting).
- `identity_and_access_standards.md`: Least-privilege identity and access control (dedicated workload identities, no default broad admin roles).
- `security_standards.md`: Enterprise zero-trust security and authentication standards.

### Layer 3: Agent Skills & Automation (`.agents/skills/`)
Custom executable automation tools for the agent:
- `spec-ledger/`: Automatically computes SHA256 hashes of human prompts in `docs/design/DESIGN-*.md`, enforces non-overwritten human specs, manages the audit trail (`## Implementation Notes & Design Deltas`), and generates `docs/design/index.md`.
- `skill-creator/`: Capability to scaffold, test, and package new agent skills.

### Layer 4: Intent & Context (`docs/`)
The brain of Intent-Driven Engineering:
- `docs/requirements/`: Raw human inputs, PRDs, problem statements, customer notes, and the `MASTER_AGENTIC_PROMPT.md`.
- `docs/design/`: Sequential, modular feature specifications (`DESIGN-01-*.md`, `DESIGN-02-*.md`, etc.) and the auto-generated routing index (`index.md`).
- `docs/llms.txt`: Machine-readable architectural summary, data contracts, and component interfaces.

### Layer 5: Automated Verification (`evals/`)
The evaluation and definition-of-done validation suite:
- `evals/security-audits/`: Automated tests checking for leaked credentials, exposed secrets, and configuration hygiene.
- Domain unit and integration tests that verify feature completion before an agent marks a task done.

### Layer 6: Architectural Dependency Graph (`graphify-out/`)
Machine-readable codebase knowledge graphs allowing AI agents to understand relationships, imports, and system dependencies without reading every file.

### Layer 7: Execution Layer (`src/` & `infrastructure/`)
The actual payload and application code:
- `src/app/`: Web applications, APIs, microservices, and client interfaces.
- `src/pipelines/`: Data pipelines, streaming ingestion, batch processing jobs.
- `src/scripts/`: Database DDL, migration scripts, and utility tools.
- `infrastructure/`: Infrastructure as Code (Terraform / OpenTofu modules and environments).
