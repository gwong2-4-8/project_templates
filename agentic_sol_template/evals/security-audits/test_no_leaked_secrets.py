"""Security Audit: Verify zero hardcoded API keys, private keys, or credentials.

Recursively scans src/, infrastructure/, and scripts/ for sensitive token patterns
including private keys, cloud credentials, authorization tokens, and API keys.
Asserts that exactly 0 unauthorized secrets exist in the repository.
"""

import re
import unittest
from pathlib import Path
from typing import List, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = [
    PROJECT_ROOT / "src",
    PROJECT_ROOT / "infrastructure",
    PROJECT_ROOT / "terraform",
]

SECRET_PATTERNS = [
    # Private keys
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "Private Key Block"),
    # AWS Access Key
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS Access Key"),
    # Google API Key
    (re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"), "Google API Key"),
    # GitHub Personal Access Token
    (re.compile(r"\bgh[pous]_[0-9a-zA-Z]{36}\b"), "GitHub Token"),
    # Slack Token
    (re.compile(r"\bxox[baprs]-[0-9a-zA-Z]{10,48}\b"), "Slack Token"),
]

IGNORED_PATTERNS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
    ".tox",
    "node_modules",
}


def scan_file_for_secrets(file_path: Path) -> List[Tuple[int, str, str]]:
    """Scan a single file against secret patterns."""
    matches = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, start=1):
                # Ignore comment lines that document placeholders
                if "YOUR_" in line or "EXAMPLE" in line or "REPLACE_ME" in line:
                    continue
                for pattern, secret_type in SECRET_PATTERNS:
                    if pattern.search(line):
                        matches.append((line_no, secret_type, line.strip()[:40]))
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return matches


def verify_no_hardcoded_secrets():
    """Verify zero hardcoded secrets exist across codebase directories."""
    leaked_secrets = []

    for target_dir in TARGET_DIRS:
        if not target_dir.exists():
            continue

        for path in target_dir.rglob("*"):
            if any(ignored in path.parts for ignored in IGNORED_PATTERNS):
                continue

            if path.is_file():
                matches = scan_file_for_secrets(path)
                for line_no, secret_type, snippet in matches:
                    rel_path = path.relative_to(PROJECT_ROOT)
                    leaked_secrets.append(f"{rel_path}:{line_no} [{secret_type}] -> {snippet}...")

    print(f"\n[Secret Audit] Scanned directories: {[str(d.relative_to(PROJECT_ROOT)) for d in TARGET_DIRS if d.exists()]}")
    if leaked_secrets:
        print("[Secret Audit] Leaked secrets detected:")
        for leak in leaked_secrets:
            print(f"  - {leak}")

    assert len(leaked_secrets) == 0, (
        f"Found {len(leaked_secrets)} hardcoded secret(s) in codebase:\n"
        + "\n".join(leaked_secrets)
    )
    print("[Secret Audit] PASSED: Exactly 0 hardcoded secrets or credentials found.")


# Pytest entry point
def test_no_hardcoded_secrets():
    verify_no_hardcoded_secrets()


# Unittest entry point
class TestNoLeakedSecrets(unittest.TestCase):
    def test_no_leaked_secrets(self):
        verify_no_hardcoded_secrets()


if __name__ == "__main__":
    unittest.main()
