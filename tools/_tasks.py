from __future__ import annotations

import argparse
import os
import subprocess as sp
import sys
from collections import deque
from collections.abc import Mapping, Sequence
from contextlib import AbstractContextManager
from functools import partial
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal, TypeVar

import tomlkit
from tomlkit.items import Table as _Table

if sys.version_info >= (3, 12):
    from typing import Protocol
else:
    from typing_extensions import Protocol


if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

    from tomlkit import TOMLDocument as _TOMLDocument
    from tomlkit.container import Container as _Container


__all__ = ["Commands", "Tasks"]


IntoExtras: TypeAlias = "str | Sequence[str] | None"
Extras: TypeAlias = tuple[str, ...]
Commands: TypeAlias = "Iterator[str]"
TaskT = TypeVar("TaskT", bound="Callable[..., Commands]")
IntoRunner: TypeAlias = Literal["hatch", "uv"]
_TaskValueShort: TypeAlias = Sequence[str]
_TaskValueLong: TypeAlias = Mapping[Literal["commands", "extras"], Sequence[str]]
_TaskValue: TypeAlias = "_TaskValueShort | _TaskValueLong"  # noqa: TC008

REPO_ROOT: Path = Path(__file__).parent.parent


class _Runner(Protocol):
    run_command: LiteralString

    def with_extras(self, command: str, extras: Extras, /) -> str: ...

    def resolve(self, command: str, extras: Extras, /) -> str:
        """Turn single command text into the env wrappped version."""
        cmd = self.with_extras(command, extras) if extras else command
        return f"{self.run_command} {cmd}"

    def __setattr__(self, name: str, value: Any) -> None:
        tp = type(self).__name__
        msg = f"Unable to set `{tp}.{name} = {value}`\n" f"{tp!r} is immutable."
        raise TypeError(msg)


class _HatchRunner(_Runner):
    run_command = "hatch run"

    def with_extras(self, command: str, extras: Extras, /) -> str:
        if len(extras) == 0:
            return command
        elif len(extras) > 1:
            return f"{extras[0]}:{command}"
        else:
            msg = "Only supporting single extra environment for `hatch`"
            raise NotImplementedError(msg)


class _UvRunner(_Runner):
    run_command = "uv run"

    def with_extras(self, command: str, extras: Extras, /) -> str:
        if len(extras) == 0:
            return command
        options = " ".join(f"--extra {ext}" for ext in extras)
        return f"{options} {command}"


class Tasks:
    _mapping: dict[str, _Task]
    _tasks: deque[_Task]
    _runner: _Runner
    _TABLE_PATH: ClassVar[Sequence[LiteralString]] = "tool", "altair", "tasks"

    def __init__(self, *, runner: IntoRunner) -> None:
        self._runner = _into_runner(runner)
        self._mapping = {}
        self._tasks = deque()

    def task(
        self, alias: str | None = None, *, extras: IntoExtras = None
    ) -> Callable[[TaskT], TaskT]:
        r"""
        Decorate a generator function for use as a runnable task.

        Parameters
        ----------
        alias
            Alternative name which can invoke the task.
            The actual function name can always be used.
        extras
            Any `optional-dependencies`_ required to run the task.

        .. _optional-dependencies:
            https://packaging.python.org/en/latest/specifications/pyproject-toml/#dependencies-optional-dependencies

        Examples
        --------
        Create an app:

            from altair.tools._tasks import Tasks

            app = Tasks(runner="hatch")

        Define the commands that compose the task:

            from altair.tools._tasks import Commands

            @app.task()
            def my_task() -> Commands:
                yield 'python -c "print(\"doing some work!\")"'
                yield "ruff check ."
                yield "pytest"

        Other tasks can refer to any previously declared tasks:

            @app.task()
            def my_other_task() -> Commands:
                yield "my_task"
                yield "ruff format"
        """

        def decorator(fn: TaskT, /) -> TaskT:
            self._add(_Task(fn, alias, extras))
            return fn

        return decorator

    def run(self, commands: Iterable[str], /, *, dry_run: bool = False) -> None:
        """Run commands/tasks in *some* environment."""
        commands = (commands,) if isinstance(commands, str) else tuple(commands)
        print(
            f'{"Tasks (dry run)" if dry_run else "Tasks"}\n' f'[{", ".join(commands)}]'
        )
        for idx, cmd in self._iter_commands(commands):
            idxs = f"[{idx}]"
            print(f"{idxs:4} > {cmd}")
            if dry_run:
                print("...")
            else:
                with DirContext():
                    _run_stream_stdout(cmd)

    @classmethod
    def from_toml(cls, doc: _TOMLDocument, /, *, runner: IntoRunner) -> Tasks:
        obj = cls(runner=runner)
        for name, value in toml_deep_get(doc, *cls._TABLE_PATH).items():
            obj._add(_Task.from_item(name, value))
        return obj

    @classmethod
    def from_path(cls, source: str | Path, /, *, runner: IntoRunner) -> Tasks:
        doc = tomlkit.parse(Path(source).read_text("utf-8"))
        return cls.from_toml(doc, runner=runner)

    def to_toml(self) -> _TOMLDocument:
        return toml_deep_set(
            (task.to_item() for task in self._tasks), *self._TABLE_PATH
        )

    def to_path(self, file: str | Path, /) -> None:
        """Export tasks definitions to a ``.toml`` file."""
        Path(file).write_text(self.to_toml().as_string(), encoding="utf-8")

    def parser(self, prog: str, /) -> argparse.ArgumentParser:
        """Returns a command line argument parser."""
        indent = len(f"usage: {prog} ") * " "
        parser = argparse.ArgumentParser(
            prog=prog,
            usage=f"{prog} [-h] [--dry-run]\n{indent}command\n{indent}[commands, ...]",
            description="Temporary solution until `uv run` can be used as a task runner.  \n"
            "https://github.com/astral-sh/uv/issues/5903#issuecomment-2558137515",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            default=False,
            help="Print resolved tasks to console, but run nothing",
        )
        parser.add_argument(
            "commands",
            nargs="+",
            choices=tuple(self._mapping),
            help="One or more pre-defined tasks",
            metavar=self._metavar(),
        )
        return parser

    def _add(self, task: _Task, /) -> None:
        for name in task.names:
            if name in self._mapping:
                msg = (
                    f"Duplicate task names are not allowed.\n"
                    f"{name!r} matches existing task:\n{self._mapping[name]!r}"
                )
                raise TypeError(msg)
            self._mapping[name] = task
        self._tasks.append(task)

    def _expand(
        self, command: str, extras: Extras = (), /
    ) -> Iterator[tuple[str, Extras]]:
        if expand := self._mapping.get(command):
            sub_extras = expand._extras or extras
            for cmd in expand:
                yield from self._expand(cmd, sub_extras)
        else:
            yield command, extras

    def _resolve(self, command: str, /) -> Commands:
        for cmd, extras in self._expand(command):
            yield self._runner.resolve(cmd, extras)

    def _iter_commands(self, commands: Iterable[str], /) -> Iterator[tuple[int, str]]:
        """Flatten and resolve all commands."""
        yield from enumerate(
            chain.from_iterable(self._resolve(cmd) for cmd in commands)
        )

    def _metavar(self) -> str:
        """
        Helper to format command aliases when using ``--help``.

        The default formatting doesn't play nicely with a high number of choices.
        """
        return "\n  ".join(", ".join(task._rev_names()) for task in self._tasks)


class _Task:
    _fn: Callable[..., Commands]
    _name: str
    _alias: str | None
    _extras: Extras

    def __init__(
        self, fn: Callable[..., Commands], alias: str | None, extras: IntoExtras, /
    ) -> None:
        if fn.__name__ == alias:
            nm = fn.__name__
            msg = (
                f"`alias` should not match the function name {nm!r}.\n"
                f"Instead, try:\n"
                f"    @app.{Tasks.task.__name__}()\n"
                f"    def {nm}() -> Iterator[str]: ..."
            )
            raise TypeError(msg)

        self._fn = fn
        self._name = fn.__name__
        self._alias = alias
        self._extras = _into_extras(extras)

    @classmethod
    def from_dict(cls, mapping: Mapping[str, _TaskValue], /) -> _Task:
        name = next(iter(mapping))
        return cls.from_item(name, mapping[name])

    @classmethod
    def from_item(cls, name: str, value: _TaskValue, /) -> _Task:
        extras: IntoExtras = None
        if isinstance(value, Mapping):
            commands = value["commands"]
            extras = value["extras"]
        else:
            commands = value
        obj = cls.__new__(cls)
        obj._fn = partial(iter, commands)
        obj._name = name
        obj._alias = None
        obj._extras = _into_extras(extras)
        return obj

    def to_dict(self) -> dict[str, _TaskValue]:
        return {self.name: self._to_value()}

    def to_item(self) -> tuple[str, _TaskValue]:
        """Short/long form (with name)."""
        return self.name, self._to_value()

    def _to_value(self) -> _TaskValue:
        """Short/long form (excluding name)."""
        if self._extras:
            return {"commands": self.commands, "extras": self._extras}
        return self.commands

    @property
    def names(self) -> Iterator[str]:
        if self._alias:
            yield from (self._name, self._alias)
        else:
            yield self._name

    def _rev_names(self) -> Iterator[str]:
        if self._alias:
            yield from (self._alias, self._name)
        else:
            yield self._name

    def __iter__(self) -> Commands:
        yield from self._fn()

    @property
    def commands(self) -> tuple[str, ...]:
        return tuple(self)

    @property
    def name(self) -> str:
        """Prefer alias over function name."""
        return self._alias or self._name


### NOTE: conversion/init helpers


def _into_runner(runner: IntoRunner, /) -> _Runner:
    if runner == "hatch":
        return _HatchRunner()
    elif runner == "uv":
        return _UvRunner()
    else:
        msg = f"Unrecognized runner: {runner!r}"
        raise TypeError(msg)


def _into_extras(arg: IntoExtras, /) -> Extras:
    if arg is None:
        return ()
    elif isinstance(arg, str):
        return (arg,)
    elif isinstance(arg, Sequence):
        return tuple(arg)
    else:
        msg = f"{type(arg).__name__!r}, {arg!r}"
        raise TypeError(msg)


### NOTE: subprocess utils


def _stdout_handler(line: bytes, /) -> None:
    """Pass-through to ``sys.stdout``, without adding whitespace."""
    print(line.decode(), end="")


def _run_stream_stdout(
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


class DirContext(AbstractContextManager):
    """Restore working directory if changed during a block."""

    def __init__(self) -> None:
        self._orig_directory: Path

    def __enter__(self) -> DirContext:
        self._orig_directory = Path.cwd()
        return self

    def __exit__(self, *args) -> None:
        if Path.cwd() != self._orig_directory:
            os.chdir(self._orig_directory)


def str_path(source: str | Path, /) -> str:
    """
    Normalize to a relative string path.

    The commands this gets used in can serialize those cross-platform paths.
    - Getting expanded in the python runtime context.
    """
    return Path(source).resolve().relative_to(REPO_ROOT).as_posix()


def py_cmd(command: str, /) -> str:
    return f"python -c {command!r}"


def rm_rf_cmd(source: str | Path, /) -> str:
    s = str_path(source)
    if Path(source).is_file():
        command = f"from pathlib import Path;Path({s!r}).unlink(missing_ok=True)"
    else:
        command = f"import shutil;shutil.rmtree({s!r}, ignore_errors=True)"
    return py_cmd(command)


def mkdir_cmd(source: str | Path, /) -> str:
    s = str_path(source)
    return py_cmd(f"from pathlib import Path;Path({s!r}).mkdir(exist_ok=True)")


### NOTE: TOML utils


def _deep_get(container: _Container, key: str, /) -> _Container:
    item = container.item(key)
    if isinstance(item, _Table):
        return item.value
    else:
        raise TypeError(type(item))


def toml_deep_get(doc: _TOMLDocument, *keys: str) -> dict[str, Any]:
    it = iter(keys)
    value = _deep_get(doc, next(it))
    for key in it:
        value = _deep_get(value, key)
    return value.unwrap()


def toml_deep_set(
    m: Iterable[tuple[Any, Any]], *keys: str, doc: _TOMLDocument | None = None
) -> _TOMLDocument:
    it = reversed(keys)
    name = next(it)
    leaf = tomlkit.table()
    leaf.update(m)
    for key in it:
        stem = tomlkit.table()
        stem.append(name, leaf)
        name = key
        leaf = stem
    if doc is not None:
        msg = "Need to implement adding to existing toml"
        raise NotImplementedError(msg)
    doc = tomlkit.document()
    doc.append(name, leaf)
    return doc
