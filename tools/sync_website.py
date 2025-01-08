from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
import subprocess as sp
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal

DOC_REPO_ORG: Literal["altair-viz"] = "altair-viz"
GITHUB: Literal["github"] = "github"
WEBSITE: str = f"{DOC_REPO_ORG}.{GITHUB}.io"
DOC_REPO_URL: str = f"https://{GITHUB}.com/{DOC_REPO_ORG}/{WEBSITE}.git"

REPO_DIR: Path = Path(__file__).parent.parent
DOC_DIR: Path = REPO_DIR / "doc"
DOC_BUILD_DIR: Path = DOC_DIR / "_build"
DOC_REPO_DIR: Path = DOC_BUILD_DIR / WEBSITE
DOC_HTML_DIR: Path = DOC_BUILD_DIR / "html"

DOC_BUILD_INFO: Path = DOC_HTML_DIR / ".buildinfo"


CMD_CLONE = f"git clone --filter=blob:none {DOC_REPO_URL}"
"""Partial clone, as we only keep ``./.git/**``."""

CMD_PULL = "git pull"
CMD_HEAD_HASH = "git rev-parse HEAD"
CMD_ADD = "git add . --all --force"
CMD_COMMIT = "git commit -m"
CMD_PUSH = "git push origin master"

COMMIT_MSG_PREFIX = "doc build for commit"
UNTRACKED = ".git"


class SubprocessFailedError(sp.CalledProcessError):
    def __str__(self) -> str:
        s = super().__str__()
        out = self.stderr or self.output
        err = out.decode() if isinstance(out, bytes) else out
        return f"{s}\nOutput:\n{err}"

    @classmethod
    def from_completed_process(cls, p: sp.CompletedProcess, /) -> SubprocessFailedError:
        return cls(p.returncode, p.args, p.stdout, p.stderr)


def _path_repr(fp: Path, /) -> str:
    return f"{fp.relative_to(REPO_DIR).as_posix()!r}"


def run_check(command: sp._CMD, /) -> sp.CompletedProcess[bytes]:
    p = sp.run(command, check=False, capture_output=True)
    if p.returncode:
        raise SubprocessFailedError.from_completed_process(p)
    else:
        return p


def clone_or_sync_repo() -> None:
    os.chdir(DOC_BUILD_DIR)
    if not DOC_REPO_DIR.exists():
        print(f"Cloning repo {WEBSITE!r}\n  -> {_path_repr(DOC_REPO_DIR)}")
        run_check(CMD_CLONE)
    else:
        print(f"Using existing cloned altair directory {_path_repr(DOC_REPO_DIR)}")
        os.chdir(DOC_REPO_DIR)
        print(f"Syncing {WEBSITE!r}\n  -> {_path_repr(DOC_REPO_DIR)} ...")
        run_check(CMD_PULL)


def remove_tracked_files() -> None:
    os.chdir(DOC_REPO_DIR)
    print(f"Removing all tracked files from {_path_repr(DOC_REPO_DIR)} ...")
    for fp in DOC_REPO_DIR.iterdir():
        if fp.name == UNTRACKED:
            continue
        if fp.is_file():
            fp.unlink()
        else:
            shutil.rmtree(fp)


def sync_from_html_build() -> None:
    print(f"Syncing files from {_path_repr(DOC_HTML_DIR)} ...")
    copy_ret = shutil.copytree(DOC_HTML_DIR, DOC_REPO_DIR, dirs_exist_ok=True)
    print(f"Successful copy to: {_path_repr(copy_ret)}")


def generate_commit_message() -> str:
    os.chdir(DOC_REPO_DIR)
    print("Generating commit message ...")
    r = run_check(CMD_HEAD_HASH)
    return f"{COMMIT_MSG_PREFIX} {r.stdout.decode().strip()}"


def current_branch() -> str:
    return run_check(["git", "branch", "--show-current"]).stdout.decode().rstrip()


def add_commit_push_github(msg: str, /) -> None:
    os.chdir(DOC_REPO_DIR)
    print("Pushing ...")
    # NOTE: Ensures the message uses cross-platform escaping
    cmd_commit = *CMD_COMMIT.split(" "), msg
    commands = (CMD_ADD, cmd_commit, CMD_PUSH)
    for command in commands:
        run_check(command)


def ensure_build_html() -> None:
    if not (DOC_HTML_DIR.exists() and DOC_HTML_DIR.is_dir()):
        raise FileNotFoundError(DOC_HTML_DIR)
    if not DOC_BUILD_INFO.exists():
        raise FileNotFoundError(DOC_BUILD_INFO)
    DOC_REPO_DIR.mkdir(parents=True, exist_ok=True)
    mtime = DOC_BUILD_INFO.stat().st_mtime
    modified = dt.datetime.fromtimestamp(mtime, dt.timezone.utc).isoformat(
        " ", "seconds"
    )
    print(f"Docs last build time: {modified!r}")


def main(*, no_commit: bool = False) -> None:
    """
    Make sure these have been run first.

    Commands:

        hatch run doc:clean-all
        hatch run doc:build-html
    """
    ensure_build_html()
    commit_message = generate_commit_message()
    clone_or_sync_repo()
    remove_tracked_files()
    sync_from_html_build()
    branch = current_branch()
    if no_commit:
        print(f"Unused commit message:\n  {commit_message!r}")
    elif branch != "main":
        # FIXME: Unsure how to reproduce the RELEASING.md steps from this PR
        # https://github.com/vega/altair/blob/main/RELEASING.md
        print(f"Unable to push from {branch!r}.\n" "Must be on 'main'.")
    else:
        add_commit_push_github(commit_message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="sync_website.py")
    parser.add_argument("--no-commit", action="store_true")
    args = parser.parse_args()
    main(no_commit=args.no_commit)