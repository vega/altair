from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INIT_FILE = ROOT / "altair" / "__init__.py"
CONF_FILE = ROOT / "doc" / "conf.py"
VERSION_RE = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)(?:dev)?$")


def _parse_version(version: str) -> tuple[int, int, int]:
    match = VERSION_RE.match(version)
    if match is None:
        msg = f"Expected a version like '6.2.0' or '6.2.0dev', got {version!r}"
        raise ValueError(msg)
    return tuple(int(part) for part in match.groups())


def _normalize_version(version: str) -> str:
    _parse_version(version)
    return version.removeprefix("v")


def _read_current_version() -> str:
    match = re.search(r'^__version__ = "([^"]+)"$', INIT_FILE.read_text(), re.MULTILINE)
    if match is None:
        msg = f"Could not find __version__ in {INIT_FILE}"
        raise RuntimeError(msg)
    return match.group(1)


def _next_dev_version(release_version: str, current_version: str) -> str:
    release_version = _normalize_version(release_version)
    current_version = _normalize_version(current_version)
    release_parts = _parse_version(release_version)
    current_parts = _parse_version(current_version)
    if current_version.endswith("dev") and current_parts > release_parts:
        return current_version
    major, minor, _patch = release_parts
    return f"{major}.{minor + 1}.0dev"


def _replace(path: Path, pattern: str, replacement: str) -> None:
    content = path.read_text()
    updated = re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if updated == content:
        msg = f"Could not update version in {path}"
        raise RuntimeError(msg)
    path.write_text(updated)


def _update_version(version: str) -> None:
    version = _normalize_version(version)
    _replace(INIT_FILE, r'^__version__ = ".*"$', f'__version__ = "{version}"')
    _replace(CONF_FILE, r'^version = ".*"$', f'version = "{version}"')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", nargs="?", help="Version to write to release files")
    parser.add_argument(
        "--get",
        action="store_true",
        help="Print the current version from altair/__init__.py",
    )
    parser.add_argument(
        "--next-dev",
        nargs=2,
        metavar=("RELEASE_VERSION", "CURRENT_VERSION"),
        help="Print the next development version after RELEASE_VERSION",
    )
    args = parser.parse_args()

    if args.get:
        print(_read_current_version())
        return
    if args.next_dev is not None:
        print(_next_dev_version(*args.next_dev))
        return
    if args.version is None:
        parser.error("provide a version, --get, or --next-dev")
    _update_version(args.version)


if __name__ == "__main__":
    main()
