from __future__ import annotations

import argparse
import os
import subprocess as sp
from typing import TYPE_CHECKING

from tools import fs

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Literal

DOC_REPO_ORG: Literal["altair-viz"] = "altair-viz"
GITHUB: Literal["github"] = "github"
WEBSITE: str = f"{DOC_REPO_ORG}.{GITHUB}.io"
DOC_REPO_URL: str = f"https://{GITHUB}.com/{DOC_REPO_ORG}/{WEBSITE}.git"
DOC_REPO_SSH_URL: str = f"git@{GITHUB}.com:{DOC_REPO_ORG}/{WEBSITE}.git"


DOC_DIR: Path = fs.REPO_ROOT / "doc"
DOC_BUILD_DIR: Path = DOC_DIR / "_build"
DOC_REPO_DIR: Path = DOC_BUILD_DIR / WEBSITE
DOC_HTML_DIR: Path = DOC_BUILD_DIR / "html"
DOC_BUILD_INFO: Path = DOC_HTML_DIR / ".buildinfo"

CMD_CLONE = "git", "clone", DOC_REPO_URL
CMD_PULL = "git", "pull"
CMD_REMOTE_URL = "git", "remote", "get-url", "origin"
CMD_SOURCE_HEAD_HASH = "git", "-C", str(fs.REPO_ROOT), "rev-parse", "HEAD"
CMD_ADD = "git", "add", ".", "--all", "--force"
CMD_STAGED_CHANGES = "git", "diff", "--cached", "--quiet"
CMD_COMMIT = "git", "commit", "-m"
CMD_PUSH = "git", "push", "origin", "master"

COMMIT_MSG_PREFIX = "doc build for commit"
UNTRACKED = ".git"


def clone_or_sync_repo() -> None:
    os.chdir(DOC_BUILD_DIR)
    if not DOC_REPO_DIR.exists():
        print(f"Cloning repo {WEBSITE!r}\n  -> {fs.path_repr(DOC_REPO_DIR)}")
        fs.run_stream_stdout(CMD_CLONE)
    else:
        os.chdir(DOC_REPO_DIR)
        expected_urls = {
            DOC_REPO_URL,
            DOC_REPO_URL.removesuffix(".git"),
            DOC_REPO_SSH_URL,
            DOC_REPO_SSH_URL.removesuffix(".git"),
        }
        actual_url = fs.run_check((*CMD_REMOTE_URL,)).stdout.strip()
        if actual_url not in expected_urls:
            msg = (
                f"Existing docs publish clone has unexpected origin {actual_url!r}. "
                f"Remove {fs.path_repr(DOC_REPO_DIR)} and rerun the publish task."
            )
            raise RuntimeError(msg)
        print(f"Using existing cloned altair directory {fs.path_repr(DOC_REPO_DIR)}")
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
    print("Generating commit message ...")
    return f"{COMMIT_MSG_PREFIX} {fs.run_check(CMD_SOURCE_HEAD_HASH).stdout.strip()}"


def add_commit_push_github(msg: str, /, *, dry_run: bool) -> None:
    os.chdir(DOC_REPO_DIR)
    print("Pushing ...")
    cmd_commit = *CMD_COMMIT, msg
    cmd_push = (*CMD_PUSH, "--dry-run") if dry_run else CMD_PUSH
    fs.run_stream_stdout(CMD_ADD)
    if sp.run(CMD_STAGED_CHANGES, check=False).returncode == 0:
        print("No docs changes to commit.")
    else:
        fs.run_stream_stdout(cmd_commit)
    fs.run_stream_stdout(cmd_push)


def ensure_build_html() -> None:
    if not fs.dir_exists(DOC_HTML_DIR):
        raise FileNotFoundError(DOC_HTML_DIR)
    if not DOC_BUILD_INFO.exists():
        raise FileNotFoundError(DOC_BUILD_INFO)
    time = fs.modified_time(DOC_BUILD_INFO).isoformat(" ", "seconds")
    print(f"Docs last build time: {time!r}")


def main(*, dry_run: bool = False) -> None:
    ensure_build_html()
    commit_message = generate_commit_message()
    clone_or_sync_repo()
    remove_tracked_files()
    sync_from_html_build()
    add_commit_push_github(commit_message, dry_run=dry_run)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="sync_website.py")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
