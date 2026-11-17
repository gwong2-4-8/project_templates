# Infrastructure as Code (`infrastructure/`)

This directory houses declarative Infrastructure as Code (IaC) configurations (Terraform, OpenTofu, or cloud templates).

## Layout & Organization
- `infrastructure/`: Root orchestration files (`main.tf`, `variables.tf`, `outputs.tf`).
- `infrastructure/modules/`: Parameterized, reusable infrastructure modules (networking, compute, storage, databases, IAM).

## Guidelines
- **No Resources in Root Orchestration:** Use root configurations to wire providers and call parameterized modules.
- **State File Hygiene:** Never commit `*.tfstate`, `*.tfstate.backup`, or `*.tfvars` files to version control.
- **Dry-Run Inspection:** Always run dry-run plans before applying changes.
