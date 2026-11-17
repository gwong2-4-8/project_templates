I have just initialized a new solution from the generic agentic template. I need you to execute the scaffolding setup autonomously.

First, ask me for the "Project Name" (or "Solution Name"). Wait for my response.

Once I provide the project name, convert my input into two formats:
1. `kebab-case` (e.g., if I say "Customer Portal", format it as `customer-portal`)
2. `snake_case` (e.g., if I say "Customer Portal", format it as `customer_portal`)

After you have those two formats, execute the following steps in this EXACT order:

### Step 1: Update Environment Configuration
- Open `agent-config.json` and replace the placeholder identifiers (`YOUR_PROJECT_ID`, `solution_database`, etc.) with appropriate values incorporating the `kebab-case` and `snake_case` names.

### Step 2: Universal Symlinks Verification
Run the following commands in the terminal at the root of the workspace to ensure agent routing symlinks exist:
```bash
ln -sf AGENTS.md .cursorrules
ln -sf AGENTS.md .clinerules
ln -sf AGENTS.md CLAUDE.md
ln -sf AGENTS.md GEMINI.md
```

### Step 3: Content Updates & Placeholders
- Search the workspace for `[REPLACE_ME]` or `YOUR_PROJECT_ID`. 
- Update `README.md` and `AUTHORS.md` with the new project name.
- Update `docs/llms.txt` with the new solution name.

### Step 4: Directory & Architecture Verification
Ensure the following base directories exist:
- `.agents/rules/`
- `.agents/skills/`
- `docs/requirements/`
- `docs/design/`
- `evals/security-audits/`
- `src/app/`
- `src/pipelines/`
- `src/scripts/`

### Step 5: Spec Ledger Synchronization
Run the spec ledger to initialize the design index:
```bash
python3 .agents/skills/spec-ledger/scripts/run.py
```

### Step 6: Security Verification
Run the baseline security audits to verify a clean state:
```bash
pytest evals/security-audits/
```

Do not ask for permission between steps. Execute the pipeline and report back when finished with a summary of the initialized workspace.
