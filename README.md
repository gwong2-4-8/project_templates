# Project Templates

A curated collection of production-grade, architectural project templates designed for modern AI Engineering, autonomous agent development, and enterprise solution engineering.

---

## 📦 Available Templates

### 🤖 [`agentic_sol_template/`](agentic_sol_template/)
> **Production-Ready, Vendor-Agnostic Agentic Solution Engineering Template**

An enterprise blueprint for building software, data platforms, and cloud architectures using **Intent-Driven Engineering** and autonomous AI coding agents (Antigravity CLI, Claude Code, Cursor, Gemini CLI, Windsurf, Cline).

#### Key Highlights & Architectural Features:
- **7-Layer Taxonomy:** Separates global routing, governance rules, tool skills, intent specifications, automated evals, knowledge graphs, and execution code.
- **Spec Ledger Synchronization (`.agents/skills/spec-ledger`):** Employs SHA-256 hash validation to guarantee AI agents never overwrite or drift from human design specifications.
- **Modular Governance Guardrails (`.agents/rules/`):** Dynamic, progressive-disclosure rules enforcing zero-trust security, least-privilege identity, immutable git boundaries, and clean secrets vaulting.
- **Universal Multi-Agent Compatibility:** Zero-duplication symlink architecture supporting all major agentic IDEs via `AGENTS.md`.
- **Automated Evals & Security Gates (`evals/`):** Pre-configured pytest/unittest harnesses auditing secret leakage, token hygiene, and configuration safety.

👉 **[Explore the `agentic_sol_template` README & Documentation](agentic_sol_template/README.md)**

---

## 🚀 How to Use These Templates

1. Navigate to the desired template folder (e.g., `cd agentic_sol_template`).
2. Follow the detailed quick start guide and scaffolding prompt in that directory.
3. Scaffold your project with your preferred AI coding agent or IDE.

---

## 📄 License

All templates in this repository are licensed under the Apache 2.0 License. See individual template directories for specific details.
