"""Configuration Hygiene Audit: Verify agent-config.json structure and safety.

Verifies that:
1. agent-config.json exists and is valid JSON.
2. Required architectural configuration keys are present.
3. No plain-text passwords or secret keys are stored in configuration.
"""

import json
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "agent-config.json"


def verify_configuration_hygiene():
    """Verify configuration file validity and absence of sensitive tokens."""
    assert CONFIG_PATH.exists(), f"Missing required configuration file: {CONFIG_PATH}"

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            raise AssertionError(f"agent-config.json is malformed JSON: {e}")

    # Check required keys
    required_keys = ["environment", "project-id", "region", "database-name"]
    for key in required_keys:
        assert key in config, f"Missing required key '{key}' in agent-config.json"

    # Check for forbidden sensitive keywords in config values
    forbidden_tokens = ["password", "secret_key", "private_key", "bearer "]
    for key, val in config.items():
        if isinstance(val, str):
            for token in forbidden_tokens:
                assert token not in val.lower(), (
                    f"Possible secret detected in agent-config.json key '{key}': contains '{token}'"
                )

    print("\n[Config Audit] PASSED: agent-config.json is valid and clean.")


# Pytest entry point
def test_configuration_hygiene():
    verify_configuration_hygiene()


# Unittest entry point
class TestConfigHygiene(unittest.TestCase):
    def test_hygiene(self):
        verify_configuration_hygiene()


if __name__ == "__main__":
    unittest.main()
