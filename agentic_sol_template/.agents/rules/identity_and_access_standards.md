# Least-Privilege Identity & Access Standards
**Trigger:** Read this file whenever you are creating service identities, assigning permissions, or designing authorization controls.

## 1. Strictly Prohibit Default or Broad Admin Identities
- **No Shared Default Accounts:** Never run application workloads or background pipelines under default compute identities, shared admin accounts, or root credentials.
- **No Superuser Roles:** Never grant full administrative privileges (e.g., Administrator, Owner, Superuser) to application runtime identities.
- **Why:** Default and superuser accounts carry broad permissions that violate Zero-Trust architecture and create catastrophic blast radiuses if compromised.

## 2. Dedicated Custom Identity per Workload
- **Granular Workload Identities:** Every independent service, microservice, API, and batch pipeline must operate under its own dedicated custom service identity (e.g., `service-api-runner`, `pipeline-data-processor`).
- **Declarative Identity Management:** All service identities, roles, and permission assignments must be declared in Infrastructure as Code (IaC) alongside the workloads they serve.

## 3. Minimum Permissions Requirement (Least Privilege)
- **Granular Actions Only:** Grant only the specific minimum permissions strictly required for the workload's core functions:
  - Database access: Restrict to specific schemas or tables; separate read-only analytics roles from read-write application roles.
  - Storage access: Grant read or write access scoped specifically to the target bucket or path prefix.
  - Messaging access: Separate publisher permissions from consumer/subscriber permissions.
  - Secret access: Bind read permissions strictly to the individual secret resources needed by that workload.

## 4. Federated Identity & Short-Lived Tokens
- Prefer OpenTofu/Terraform workload identity federation, OIDC token exchange, or IAM role assumption over static long-lived credential keys.
- If tokens or temporary credentials are used, enforce short expiration windows and automated rotation.
