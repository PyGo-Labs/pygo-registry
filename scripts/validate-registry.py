#!/usr/bin/env python3
"""Validate the PyGo module registry JSON."""

import json
import re
import sys


def validate_registry(registry_path: str) -> None:
    with open(registry_path) as f:
        registry = json.load(f)

    # Validate top-level structure
    if not registry.get("version"):
        print("ERROR: Missing 'version' field")
        sys.exit(1)

    if "modules" not in registry or not isinstance(registry["modules"], list):
        print("ERROR: Missing 'modules' array")
        sys.exit(1)

    required_fields = [
        "name",
        "version",
        "description",
        "author",
        "repository",
        "license",
        "category",
    ]

    seen_names = set()

    for i, mod in enumerate(registry["modules"]):
        # Check required fields
        for field in required_fields:
            if field not in mod:
                print(f"ERROR: Module #{i} ({mod.get('name', 'unknown')}) missing field: {field}")
                sys.exit(1)

        # Check for duplicate module names
        if mod["name"] in seen_names:
            print(f"ERROR: Duplicate module name: {mod['name']}")
            sys.exit(1)
        seen_names.add(mod["name"])

        # Validate version format (semver)
        if not re.match(r"^\d+\.\d+\.\d+", mod["version"]):
            print(f"ERROR: Module '{mod['name']}' has invalid version: {mod['version']}")
            sys.exit(1)

        # Validate repository URL
        if not mod["repository"].startswith("https://github.com/"):
            print(f"ERROR: Module '{mod['name']}' repository must be a GitHub URL")
            sys.exit(1)

        # Validate download URL if present
        if "download_url" in mod and mod["download_url"]:
            if not mod["download_url"].startswith("https://"):
                print(f"ERROR: Module '{mod['name']}' download_url must be an HTTPS URL")
                sys.exit(1)

        print(f"  ✓ {mod['name']} v{mod['version']} ({mod['license']})")

    print(f"\n✅ Valid registry with {len(registry['modules'])} modules")


if __name__ == "__main__":
    validate_registry("registry.json")
