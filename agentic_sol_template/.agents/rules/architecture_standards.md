# Architecture & Infrastructure Standards
**Trigger:** Read this file whenever you are asked to plan, write, or modify Infrastructure as Code (IaC), cloud resources, containers, or architecture components.

## 🏗️ 1. Declarative & Modular Architecture
All infrastructure must be managed declaratively using modern Infrastructure as Code (e.g., Terraform, OpenTofu):
- **Orchestration vs Resources:** Root deployment files (e.g., in `infrastructure/` or `terraform/`) are strictly for orchestration: configuring providers, backend state, and calling modules. Do not define raw resources in the root orchestrator.
- **Reusable Modules:** Reusable infrastructure blocks (compute, storage, databases, networking, messaging) must reside in dedicated module directories (e.g., `infrastructure/modules/` or `terraform-modules/`).
- **No Manual Console Drift:** Avoid creating resources via manual cloud consoles or ad-hoc scripts unless explicitly designing a fast-path prototype. All persistent infrastructure should be captured in code.

## 🔐 2. Authentication & Credential Isolation
- **Service Identity & Role Impersonation:** Deploy resources using dedicated deployment identities or role impersonation.
- **Zero Local Keys:** Never embed service account keys, cloud credentials, or private access tokens in infrastructure configuration files or state files.

## 🏷️ 3. Naming Conventions & Resource Hygiene
- **Naming Consistency:** Follow standard naming conventions:
  - Infrastructure resource blocks: use `snake_case` (e.g., `resource "storage_bucket" "data_lake_raw"`).
  - Cloud identifiers: use `kebab-case` or `snake_case` consistently based on target cloud provider requirements.
  - Global Uniqueness: For resources requiring global uniqueness (e.g., object storage buckets), use dynamic suffixes or random identifiers.
- **Resource Tagging:** Tag all resources with consistent metadata (e.g., `environment`, `project`, `managed-by = "agentic-template"`).

## 🧱 4. Variable Requirements & Validation
- Every variable defined in configuration files MUST include a clear `description` explaining its purpose and format.
- Use validation blocks or schema constraints on required variables to prevent runtime deployment failures.

## 🛑 5. Hard Safety Constraints (NON-NEGOTIABLE)
- **NEVER RUN DESTRUCTIVE OPERATIONS:** You MUST NEVER execute destructive operations (e.g., `terraform destroy`, dropping tables/databases, deleting storage buckets) without explicit, interactive human authorization.
- **NEVER COMMIT STATE FILES:** State files (`*.tfstate`, `*.tfstate.backup`) and sensitive variable definitions (`*.tfvars`) must be strictly ignored by version control.
- **Dry-Run First:** Always run a plan or dry-run inspection (e.g., `terraform plan`) before proposing or executing changes.

## 🔄 6. Post-Deployment: Agent Configuration Synchronization
Immediately after successfully deploying or updating infrastructure:
1. Extract the newly deployed output variables (endpoints, bucket names, database connection parameters).
2. Update the corresponding keys in `agent-config.json` at the workspace root.
3. Keep the file synchronized so application services in `src/` can read live endpoints dynamically.
