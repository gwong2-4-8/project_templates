# Zero-Trust Secrets Management Standards
**Trigger:** Read this file whenever you are handling credentials, API keys, connection strings, or environment variables.

## 1. Zero Plain-Text Credentials Policy (NON-NEGOTIABLE)
- **Strictly Prohibited:** Hardcoding plain-text credentials, API keys, service identities, private keys, database passwords, connection strings, or authorization tokens anywhere in this repository is strictly forbidden.
- **Scope of Prohibition:**
  - Configuration files: `agent-config.json`, `.env`, `.env.*`
  - Infrastructure code: `*.tf`, `*.tfvars`, state files
  - Application source code and documentation: `*.py`, `*.js`, `*.ts`, `*.sh`, `*.md`, `*.json`, `*.yaml`, `*.yml`
- **Git Safety Standard:** Under no circumstances should plain-text secrets or sensitive credential files be committed or staged in version control. All agents and developers must strictly adhere to [@.agents/rules/git_standards.md](git_standards.md) for Git safety invariants.

## 2. Dynamic Runtime Environment Injection
- **Environment Variable Isolation:** Applications must read secrets directly from standard operating system environment variables (e.g., `os.environ.get("API_KEY")` or `os.environ.get("DATABASE_URL")`) at runtime.
- **Configuration Decoupling:** Non-sensitive configuration (hostnames, regions, ports) lives in `agent-config.json`, while sensitive values (passwords, private keys, access tokens) are injected securely by the deployment environment or secret manager.
- **Template Hygiene:** Use `.env.example` or documentation placeholders (e.g., `YOUR_API_KEY_HERE`) to demonstrate required environment variables without committing actual secrets.

## 3. Secret Vaulting & Secure Key Management
- In cloud and production environments, sensitive values must be stored in a dedicated Secret Manager or Key Vault service.
- Workloads should retrieve secrets either via runtime platform mounting (e.g., container secret mounts) or through identity-based IAM role access to the vault.
- Never grant broad global access to secret stores; grant access exclusively per secret to the specific workload identity requiring it.

## 4. Automated Secret Scanning Verification
- Before completing any task or marking a design specification implemented, the codebase must pass the automated secret scanning suite located in `evals/security-audits/test_no_leaked_secrets.py`.
