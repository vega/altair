#!/usr/bin/env python3
"""
Generate nightly version for Altair.

This script creates a version string based on the current date and commit hash.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def get_git_commit():
    """Get the short commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "unknown"


def get_latest_nightly_commit():
    """Get the commit hash of the latest nightly build."""
    try:
        # Get the latest nightly tag
        result = subprocess.run(
            ["git", "tag", "--list", "nightly-*", "--sort=-version:refname"],
            capture_output=True,
            text=True,
            check=True,
        )
        tags = result.stdout.strip().split("\n")
        if not tags or tags[0] == "":
            return None

        latest_tag = tags[0]
        # Get the commit hash for this tag
        result = subprocess.run(
            ["git", "rev-list", "-n", "1", latest_tag],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def has_changes_since_last_nightly():
    """Check if there are changes since the last nightly build."""
    latest_nightly_commit = get_latest_nightly_commit()
    if latest_nightly_commit is None:
        return True  # No previous nightly builds, so we should build

    current_commit = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
    ).stdout.strip()

    return latest_nightly_commit != current_commit


def generate_nightly_version():
    """Generate a nightly version string."""
    date = datetime.now().strftime("%Y%m%d")
    commit = get_git_commit()
    return f"{date}.dev0+{commit}"


def update_version_files(version):
    """Update version in __init__.py and conf.py."""
    # Update altair/__init__.py
    init_file = Path("altair/__init__.py")
    if init_file.exists():
        content = init_file.read_text()
        # Replace version line
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("__version__"):
                lines[i] = f'__version__ = "{version}"'
                break
        init_file.write_text("\n".join(lines))

    # Update doc/conf.py
    conf_file = Path("doc/conf.py")
    if conf_file.exists():
        content = conf_file.read_text()
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("release ="):
                lines[i] = f'release = "{version}"'
                break
        conf_file.write_text("\n".join(lines))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--check-changes":
        if has_changes_since_last_nightly():
            print("true")
            sys.exit(0)
        else:
            print("false")
            sys.exit(1)

    version = generate_nightly_version()
    print(f"Generated nightly version: {version}")

    if len(sys.argv) > 1 and sys.argv[1] == "--update":
        update_version_files(version)
        print("Updated version files")

    print(version)
