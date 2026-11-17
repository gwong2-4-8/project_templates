# Automated Verification & Evaluation Suite (`evals/`)

This directory contains the automated test suites, compliance checks, and verification scripts that enforce the Definition of Done for both humans and AI agents.

## Directory Structure
- `evals/security-audits/`: Automated security compliance tests (secret scanning, configuration hygiene).
- Domain unit and integration tests verifying application logic, pipeline output, or infrastructure status.

## Running the Security Audits
```bash
# Install test dependencies
pip install -r evals/security-audits/requirements.txt

# Execute security audits
pytest evals/security-audits/
```
