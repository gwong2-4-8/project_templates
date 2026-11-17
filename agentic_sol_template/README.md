# Agentic Solution Engineering Template (`agentic_sol_template`)

> **A Production-Ready, Vendor-Agnostic Blueprint for Intent-Driven Engineering with Autonomous AI Agents**  
> *Engineered for modern AI Engineering workflows across Antigravity CLI (AGY), Claude Code, Cursor, Gemini CLI, Windsurf, and Cline.*

---

## 🌟 Executive Summary & Engineering Motivation

Modern AI-assisted software development often suffers from the **"unbounded generation trap"**: developers ask an LLM or coding agent to produce features directly in code, leading to context drift, hallucinated dependencies, security anti-patterns, and lack of reproducible architectural boundaries.

This repository demonstrates **Intent-Driven Engineering**—an enterprise architectural methodology where:
1. **Humans engineer the context, contracts, and guardrails** (intent specifications, progressive disclosure rules, and strict evals).
2. **Autonomous AI agents execute within strict boundaries** (sequential design implementation, automated self-correction, and audit trails).
3. **Spec ledgers and evals guarantee zero drift** (hash integrity verification, automated security scans, and configuration hygiene).

This template was created to showcase rigorous, production-grade AI system architecture, agent orchestration, and automated governance for real-world AI Engineering applications.

---

## 🏛️ The 7-Layer Architectural Taxonomy

The project follows a strict 7-layer taxonomy designed for deterministic agent reasoning:

```text
.
├── AGENTS.md                  # [Layer 1: Router & State] Global system prompt, progressive disclosure & routing
├── agent-config.json          # [Layer 1: Router & State] Machine-readable environment parameters & boundary values
├── CLAUDE.md / GEMINI.md      # [Layer 1: Router & State] Universal symlinks resolving to AGENTS.md (.cursorrules, .clinerules)
├── .agents/
│   ├── rules/                 # [Layer 2: Governance Rules] Modular, non-negotiable architectural & security standards
│   └── skills/                # [Layer 3: Autonomous Skills] Reusable agent tool extensions and deterministic scripts
├── docs/
│   ├── requirements/          # [Layer 4: Intent & Contracts] Master agentic prompts, PRDs, and business requirements
│   ├── design/                # [Layer 4: Intent & Contracts] Sequential design specs (DESIGN-*.md) and index.md
│   └── llms.txt               # [Layer 4: Intent & Contracts] Machine-readable system topology and data plane
├── evals/                     # [Layer 5: Automated Evaluations] Security audits, config verification, and unit tests
│   └── security-audits/       # [Layer 5: Automated Evaluations] Secret scanning and configuration hygiene tests
├── graphify-out/              # [Layer 6: Knowledge Graph] Visualized architectural dependency & entity relationships
├── infrastructure/            # [Layer 7: Execution Layer] Declarative Infrastructure as Code (IaC) modules
└── src/                       # [Layer 7: Execution Layer] Application source, data pipelines, and utility scripts
```

---

## 🛡️ Architectural & Governance Standards (Layer 2)

Agents operating in this repository do not guess behaviors; they adhere to modular standards dynamically injected via progressive disclosure:

| Rule File | Core Responsibility |
| :--- | :--- |
| [`architecture_standards.md`](.agents/rules/architecture_standards.md) | Enforces declarative IaC, modular components, idempotency, and explicit confirmation before destructive mutations. |
| [`security_standards.md`](.agents/rules/security_standards.md) | Enforces enterprise zero-trust security, strict input sanitization, least-privilege scoping, and transport encryption. |
| [`secrets_management.md`](.agents/rules/secrets_management.md) | Prohibits hardcoded API keys and credentials; mandates dynamic vault injection and environment isolation. |
| [`identity_and_access_standards.md`](.agents/rules/identity_and_access_standards.md) | Mandates dedicated workload identities, explicit role bindings, and zero default superuser privileges. |
| [`git_standards.md`](.agents/rules/git_standards.md) | Enforces agent boundaries: read-only git operations, prohibiting unauthorized commits, check-ins, or branch deletion. |
| [`agent_skills_standards.md`](.agents/rules/agent_skills_standards.md) | Enforces Unix-style composability for agent tools (`SKILL.md` + `scripts/run.py`), structured JSON output, and CLI resilience. |

---

## 🤖 Multi-Agent / Multi-IDE Universal Compatibility

Different AI engineering tools expect instructions in different files. This template implements a **zero-duplication symlink architecture** rooted in [`AGENTS.md`](AGENTS.md):

- **Antigravity CLI (AGY):** Reads `AGENTS.md` and `.agents/`
- **Claude Code:** Automatically loads [`CLAUDE.md`](CLAUDE.md) (`-> AGENTS.md`)
- **Gemini CLI:** Automatically loads [`GEMINI.md`](GEMINI.md) (`-> AGENTS.md`)
- **Cursor IDE:** Automatically loads [`.cursorrules`](.cursorrules) (`-> AGENTS.md`)
- **Cline:** Automatically loads [`.clinerules`](.clinerules) (`-> AGENTS.md`)
- **Windsurf:** Reads `AGENTS.md` natively

---

## 🔄 The Spec Ledger: Deterministic Synchronization (Layer 3)

Included in `.agents/skills/spec-ledger/` is an automated synchronization engine that maintains mathematical alignment between human intent and AI execution:
- Computes SHA-256 hashes of original human design specs.
- Guarantees AI agents cannot overwrite human intent.
- Auto-extracts discovered resources (`db:`, `topic:`, `subscription:`, `queue:`, `storage:`, `service:`, `secrets:`).
- Generates a centralized index at [`docs/design/index.md`](docs/design/index.md).

```bash
# Verify spec ledger synchronization and detect architectural drift
python3 .agents/skills/spec-ledger/scripts/run.py --check
```

---

## 🧪 Automated Evals & Verification (Layer 5)

An AI system is only as reliable as its automated evaluations. This template ships with built-in audit harnesses:

```bash
# Run automated security audits and configuration tests
python3 -m unittest discover -s evals/security-audits -p "test_*.py"
```
- **Secret Leak Audit (`test_no_leaked_secrets.py`):** Scans the codebase for high-entropy tokens, cloud access keys, private key blocks, and bearer tokens.
- **Configuration Hygiene Audit (`test_configuration_hygiene.py`):** Validates environment state files (`agent-config.json`) and flags improper placeholders.

---

## 🚀 How to Use This Template

### 1. Initialize Your Solution Repository
```bash
# Clone this repository
git clone https://github.com/gwong2-4-8/project_templates.git my-agentic-project
cd my-agentic-project

# Or use it directly as a template on GitHub
```

### 2. Autonomous Scaffolding
Open your terminal in the repo using your preferred AI agent and run:
```text
Run the scaffolding instructions in @Using-This-Template-Prompt.md
```
The agent will configure the project name, scaffold domain modules, and establish clean design files.

### 3. Step-by-Step Feature Implementation Workflow
1. **Define Intent:** Place requirements in `docs/requirements/` and update `docs/llms.txt`.
2. **Author Design Specs:** Create sequential specifications in `docs/design/DESIGN-*.md`.
3. **Index Ledger:** Run `python3 .agents/skills/spec-ledger/scripts/run.py` to lock spec hashes.
4. **Agent Execution:** Instruct the agent:
   ```text
   Execute docs/design/DESIGN-01-feature.md adhering strictly to .agents/rules/
   ```
5. **Verify Evals:** Run `pytest evals/` to confirm all security and logic gates pass.

---

## 📂 Repository Structure Overview

```text
├── .agents/
│   ├── rules/                 # Governance standards (architecture, security, git, secrets)
│   └── skills/
│       ├── skill-creator/     # Autonomous tool authoring skill
│       └── spec-ledger/       # Deterministic spec synchronization engine
├── docs/
│   ├── design/                # Feature designs & index.md ledger
│   ├── requirements/          # Master agentic prompt & PRDs
│   └── llms.txt               # Machine-readable architectural contract
├── evals/
│   └── security-audits/       # Automated secret & configuration audits
├── infrastructure/            # IaC modules (Terraform, CloudFormation, Pulumi)
├── src/
│   ├── app/                   # Core application services & APIs
│   ├── pipelines/             # Data processing & ETL pipelines
│   └── scripts/               # Operational & deployment utilities
├── AGENTS.md                  # Master agent system instructions
├── agent-config.json          # Machine-readable environment state
├── AGENTIC-PROJECT-STRUCTURE.md # Deep dive into the 7 architectural layers
├── Using-This-Template.md     # Developer onboarding guide
└── Using-This-Template-Prompt.md # Autonomous agent scaffolding prompt
```

---

## 📄 License

Distributed under the Apache 2.0 License. See [`LICENSE`](LICENSE) for details.
