# Git & Version Control Standards

**Trigger:** Read this file whenever you are executing Git commands or interacting with the repository and version control.

## 🛑 1. Absolute Prohibition on Code Check-Ins (Commits & Pushes)
- **NO AGENT COMMITS:** You MUST NEVER check in, commit, or push code to Git (e.g., `git commit`, `git push`).
- **HUMAN-ONLY AUTHORITY:** Only the interactive human user can perform check-ins and commits.
- **NO MUTATING ACTIONS:** Never execute automated or scripted commit actions. The repository's commit history must only reflect deliberate actions taken by the human developer.

## 🛑 2. Absolute Prohibition on Deletions & Destructive Operations
- **NEVER DELETE IN GIT:** You MUST NEVER attempt to delete anything in Git.
- **FORBIDDEN COMMANDS:** Commands that delete or destroy commits, branches, tags, stashes, or tracked assets are strictly prohibited (e.g., `git rm`, `git branch -d`, `git branch -D`, `git push --delete`, `git reset --hard`, `git clean -fd`, `git tag -d`).
- Always preserve all working tree files, commit objects, and repository history intact.

## 👁️ 3. Read-Only "Get" Commands Permitted (Inspection Only)
- You may execute read-only Git inspection commands ("Get" commands) to view check-ins, revisions, diffs, and repository state:
  - `git status` — View modified, untracked, and staged files.
  - `git log` — View commit history, authors, timestamps, and commit messages.
  - `git show [revision]` — Inspect specific check-ins, commit details, or file revisions.
  - `git diff` — Compare working tree changes against HEAD or prior revisions.
  - `git branch --list` / `git branch -a` — View available local and remote branches.
  - `git rev-parse [revision]` — Inspect commit hashes, branch pointers, or tags.
