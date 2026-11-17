# Execution Layer (`src/`)

This directory is the single source of truth for all application source code, data pipelines, and database scripts.

## Directory Taxonomy
- `src/app/`: Web applications, APIs, microservices, UI components, and Dockerfiles.
- `src/pipelines/`: Data engineering pipelines, streaming consumers, and batch processing jobs.
- `src/scripts/`: Database DDL, migration scripts, seeding utilities, and operational scripts.

## Standards & Best Practices
- **Dynamic Configuration:** Code must read environment variables dynamically from the operating system or `agent-config.json`. Never hardcode hostnames, database names, or credentials.
- **Zero-Trust Security:** Applications must enforce input validation, transport encryption, and secure authentication.
- **Modular Packaging:** Keep services decoupled with their own local `requirements.txt` or package manifests.
