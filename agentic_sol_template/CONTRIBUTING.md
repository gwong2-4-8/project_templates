# Contributing to the Agentic Solution Template

We welcome contributions to improve this Intent-Driven Engineering template!

## Guiding Principles
1. **Cloud & Vendor Agnostic:** Core rules, instructions, and templates must remain portable and free of vendor locks or proprietary assumptions.
2. **Intent-Driven Engineering:** Keep the separation of concerns clean across all 7 layers (Router, Rules, Skills, Context, Evals, Knowledge, Execution).
3. **Progressive Disclosure:** Keep `AGENTS.md` lean. Put domain-specific guidance in `.agents/rules/` and operational logic in `.agents/skills/`.
4. **Safety & Zero-Trust:** Never check in credentials, API keys, or hardcoded environment configurations.

## Contribution Workflow
1. Fork the repository and create a feature branch (`feature/my-enhancement`).
2. Adhere to code quality and linting standards.
3. Add or update automated verification tests under `evals/`.
4. Verify that `pytest evals/security-audits/` passes with zero leaked secrets.
5. Submit a Pull Request with a clear description of the enhancement.
