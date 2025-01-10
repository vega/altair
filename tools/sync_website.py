from __future__ import annotations

import argparse
import os
from typing import TYPE_CHECKING

from tools import fs

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Literal

DOC_REPO_ORG: Literal["altair-viz"] = "altair-viz"
GITHUB: Literal["github"] = "github"
WEBSITE: str = f"{DOC_REPO_ORG}.{GITHUB}.io"
DOC_REPO_URL: str = f"https://{GITHUB}.com/{DOC_REPO_ORG}/{WEBSITE}.git"


DOC_DIR: Path = fs.REPO_ROOT / "doc"
DOC_BUILD_DIR: Path = DOC_DIR / "_build"
DOC_REPO_DIR: Path = DOC_BUILD_DIR / WEBSITE
DOC_HTML_DIR: Path = DOC_BUILD_DIR / "html"

DOC_BUILD_INFO: Path = DOC_HTML_DIR / ".buildinfo"

CMD_CLONE = "git", "clone", DOC_REPO_URL
CMD_PULL = "git pull"
CMD_HEAD_HASH = "git rev-parse HEAD"
CMD_ADD = "git", "add", ".", "--all", "--force"
CMD_COMMIT = "git", "commit", "-m"
CMD_PUSH = "git", "push", "origin", "master", "--dry-run"

COMMIT_MSG_PREFIX = "doc build for commit"
UNTRACKED = ".git"


def clone_or_sync_repo() -> None:
    os.chdir(DOC_BUILD_DIR)
    if not DOC_REPO_DIR.exists():
        print(f"Cloning repo {WEBSITE!r}\n  -> {fs.path_repr(DOC_REPO_DIR)}")
        fs.run_stream_stdout(CMD_CLONE)
    else:
        print(f"Using existing cloned altair directory {fs.path_repr(DOC_REPO_DIR)}")
        os.chdir(DOC_REPO_DIR)
        print(f"Syncing {WEBSITE!r}\n  -> {fs.path_repr(DOC_REPO_DIR)} ...")
        fs.run_stream_stdout(CMD_PULL)


def remove_tracked_files() -> None:
    os.chdir(DOC_REPO_DIR)
    print(f"Removing all tracked files from {fs.path_repr(DOC_REPO_DIR)} ...")
    for fp in DOC_REPO_DIR.iterdir():
        if fp.name == UNTRACKED:
            continue
        fs.rm(fp)


def sync_from_html_build() -> None:
    print(f"Syncing files from {fs.path_repr(DOC_HTML_DIR)} ...")
    copy_ret = fs.copytree(DOC_HTML_DIR, DOC_REPO_DIR)
    print(f"Successful copy to: {fs.path_repr(copy_ret)}")


def generate_commit_message() -> str:
    os.chdir(DOC_REPO_DIR)
    print("Generating commit message ...")
    return f"{COMMIT_MSG_PREFIX} {fs.run_check(CMD_HEAD_HASH).stdout.strip()}"


def current_branch() -> str:
    return fs.run_check(["git", "branch", "--show-current"]).stdout.rstrip()


def add_commit_push_github(msg: str, /) -> None:
    os.chdir(DOC_REPO_DIR)
    print("Pushing ...")
    # NOTE: Ensures the message uses cross-platform escaping
    cmd_commit = *CMD_COMMIT, msg
    commands = (CMD_ADD, cmd_commit, CMD_PUSH)
    for command in commands:
        fs.run_stream_stdout(command)


def ensure_build_html() -> None:
    if not fs.dir_exists(DOC_HTML_DIR):
        raise FileNotFoundError(DOC_HTML_DIR)
    if not DOC_BUILD_INFO.exists():
        raise FileNotFoundError(DOC_BUILD_INFO)
    fs.mkdir(DOC_REPO_DIR)
    time = fs.modified_time(DOC_BUILD_INFO).isoformat(" ", "seconds")
    print(f"Docs last build time: {time!r}")


def main(*, no_commit: bool = False) -> None:
    ensure_build_html()
    commit_message = generate_commit_message()
    clone_or_sync_repo()
    remove_tracked_files()
    sync_from_html_build()
    branch = current_branch()  # noqa: F841
    if no_commit:
        print(f"Unused commit message:\n  {commit_message!r}")
    else:
        add_commit_push_github(commit_message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="sync_website.py")
    parser.add_argument("--no-commit", action="store_true")
    args = parser.parse_args()
    main(no_commit=args.no_commit)
