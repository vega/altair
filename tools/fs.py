"""Cross-platform filesystem utilities."""

from __future__ import annotations

import datetime as dt
import shutil
import subprocess as sp
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


__all__ = [
    "REPO_ROOT",
    "copytree",
    "dir_exists",
    "file_exists",
    "mkdir",
    "modified_time",
    "path_repr",
    "rm",
    "run_check",
    "run_stream_stdout",
]

REPO_ROOT: Path = Path(__file__).parent.parent


def mkdir(*sources: str | Path, parents: bool = True) -> None:
    """
    Platform independent `bash mkdir`_, using ``--parents`` option.

    .. _bash mkdir:
        https://ss64.com/bash/mkdir.html
    """
    for source in sources:
        Path(source).mkdir(parents=parents, exist_ok=True)


def rm(*sources: str | Path, force: bool = True) -> None:
    """
    Platform independent `bash rm`_, using ``--recursive``, ``--force`` options.

    .. _bash rm:
        https://ss64.com/bash/rm.html
    """
    for source in sources:
        fp = Path(source)
        if fp.is_file():
            fp.unlink(missing_ok=force)
        else:
            shutil.rmtree(fp, ignore_errors=force)


def copytree(src: str | Path, dst: str | Path, *, force: bool = True):
    """
    Recursively copy a directory tree and return the destination directory.

    Wraps `shutil.copytree`_.

    .. _shutil.copytree:
        https://docs.python.org/3/library/shutil.html#shutil.copytree
    """
    return shutil.copytree(src, dst, dirs_exist_ok=force)


def file_exists(file: str | Path, /) -> bool:
    """Fail on files created using ``Path.touch()``."""
    fp = Path(file)
    return bool(fp.exists() and fp.stat().st_size)


def dir_exists(file: str | Path, /) -> bool:
    fp = Path(file)
    return fp.exists() and fp.is_dir()


def modified_time(file: str | Path, /) -> dt.datetime:
    """UTC datetime when ``file`` was last modified."""
    return dt.datetime.fromtimestamp(Path(file).stat().st_mtime, dt.timezone.utc)


def path_repr(fp: Path, /) -> str:
    """Return string representation w/ ``/``, relative to root of repository."""
    return f"{fp.relative_to(REPO_ROOT).as_posix()!r}"


def _stdout_handler(line: bytes, /) -> None:
    """Pass-through to ``sys.stdout``, without adding whitespace."""
    print(line.decode(), end="")


def run_stream_stdout(
    args: sp._CMD,
    *,
    stdout_handler: Callable[[bytes], None] = _stdout_handler,
) -> sp.CompletedProcess[Any]:
    """
    Mimic `subprocess.run`_, piping stdout back to the caller in real-time*.

    Adapted from `stackoverflow-76626021`_.

    Notes
    -----
    - `pytest`_ is line-by-line
    - `sphinx-build`_ comes out in 3 bursts (over 8 minutes)
    - All others only output a short message (usually 1 line)

    .. _subprocess.run:
        https://docs.python.org/3/library/subprocess.html#subprocess.run
    .. _stackoverflow-76626021:
        https://stackoverflow.com/questions/21953835/run-subprocess-and-print-output-to-logging/76626021#76626021
    .. _pytest:
        https://docs.pytest.org/en/stable/index.html
    .. _sphinx-build:
        https://www.sphinx-doc.org/en/master/man/sphinx-build.html
    """
    with sp.Popen(args, stdout=sp.PIPE, stderr=sp.STDOUT) as process:
        if process.stdout is not None:
            for chunk in process.stdout:
                stdout_handler(chunk)
        else:
            msg = "stdout is None"
            raise NotImplementedError(msg)
    if retcode := process.poll():
        raise sp.CalledProcessError(retcode, process.args)
    return sp.CompletedProcess(process.args, 0)


def run_check(args: sp._CMD, /) -> sp.CompletedProcess[str]:
    """
    Run a command in a `subprocess`_, capturing and decoding output.

    .. _subprocess:
        https://docs.python.org/3/library/subprocess.html#subprocess.run
    """
    return sp.run(args, check=True, capture_output=True, encoding="utf-8")
