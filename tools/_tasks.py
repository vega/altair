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
import tomlkit.exceptions
from tomlkit import toml_file
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

    from _typeshed import SupportsKeysAndGetItem
    from tomlkit import TOMLDocument as _TOMLDocument
    from tomlkit.container import Container as _Container
    from tomlkit.items import Item as _Item

    _KT = TypeVar("_KT")  # Key type.
    _VT = TypeVar("_VT")  # Value type.

    _MappingUpdates: TypeAlias = (
        "SupportsKeysAndGetItem[_KT, _VT] | Iterable[tuple[_KT, _VT]]"
    )


__all__ = ["Commands", "Tasks", "cmd"]


IntoExtras: TypeAlias = "str | Sequence[str] | None"
Extras: TypeAlias = tuple[str, ...]
Commands: TypeAlias = "Iterator[str]"
TaskT = TypeVar("TaskT", bound="Callable[..., Commands]")
IntoRunner: TypeAlias = Literal["hatch", "uv"]
_TaskValueShort: TypeAlias = Sequence[str]
_TaskValueLong: TypeAlias = Mapping[Literal["commands", "extras"], Sequence[str]]
_TaskValue: TypeAlias = "_TaskValueShort | _TaskValueLong"  # noqa: TC008

MergeStrategy: TypeAlias = Literal["replace", "update"]
"""
How to handle adding items to an existing table.

* **"replace"**: Ignore *existing* items entirely. Only *incoming* items are preserved.
* **"update"**: Overwrite *existing* items that match *incoming*. New *incoming* items are appended.
"""


REPO_ROOT: Path = Path(__file__).parent.parent


class _Runner(Protocol):
    run_command: LiteralString

    def with_extras(self, command: str, extras: Extras, /) -> str: ...

    def resolve(self, command: str, extras: Extras, /) -> str:
        """Turn single command text into the env wrappped version."""
        return f"{self.run_command} {self.with_extras(command, extras) if extras else command}"

    def __setattr__(self, name: str, value: Any) -> None:
        tp = type(self).__name__
        msg = f"Unable to set `{tp}.{name} = {value}`\n" f"{tp!r} is immutable."
        raise TypeError(msg)


class _HatchRunner(_Runner):
    run_command = "hatch run"

    def with_extras(self, command: str, extras: Extras, /) -> str:
        if len(extras) == 0:
            return command
        elif len(extras) == 1:
            return f"{extras[0]}:{command}"
        else:
            msg = (
                f"Only supporting single extra environment for `hatch`.\n"
                f"Got: {extras!r}"
            )
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

            from tools._tasks import Tasks

            app = Tasks(runner="hatch")

        Define the commands that compose the task:

            from tools._tasks import Commands

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
        for idx, command in self._iter_commands(commands):
            idxs = f"[{idx}]"
            print(f"{idxs:4} > {command}")
            if dry_run:
                print("...")
            else:
                with DirContext():
                    _run_stream_stdout(command)

    @classmethod
    def from_toml(cls, doc: _TOMLDocument, /, *, runner: IntoRunner) -> Tasks:
        obj = cls(runner=runner)
        for name, value in toml_deep_get(doc, *cls._TABLE_PATH).unwrap().items():
            obj._add(_Task.from_item(name, value))
        return obj

    @classmethod
    def from_path(cls, source: str | Path, /, *, runner: IntoRunner) -> Tasks:
        """Import tasks definitions from a ``.toml`` file."""
        return cls.from_toml(toml_file.TOMLFile(source).read(), runner=runner)

    def to_toml(self, doc: _TOMLDocument | None = None, /) -> _TOMLDocument:
        return toml_deep_set(
            (task.to_item() for task in self._tasks),
            *self._TABLE_PATH,
            doc=doc,
            how="replace",
        )

    def to_path(self, file: str | Path, /) -> None:
        """Export tasks definitions to a ``.toml`` file."""
        tm_file = toml_file.TOMLFile(file)
        doc_in = None if not _is_updating(file) else tm_file.read()
        tm_file.write(self.to_toml(doc_in))

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
            extras = expand._extras or extras
            for c in expand:
                if c == command:
                    yield command, extras
                else:
                    yield from self._expand(c, extras)
        else:
            yield command, extras

    def _resolve(self, command: str, /) -> Commands:
        for expanded, extras in self._expand(command):
            yield self._runner.resolve(expanded, extras)

    def _iter_commands(self, commands: Iterable[str], /) -> Iterator[tuple[int, str]]:
        """Flatten and resolve all commands."""
        yield from enumerate(
            chain.from_iterable(self._resolve(command) for command in commands)
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


class cmd(str):  # noqa: FURB189
    """
    Helpers for invoking the `python command line`_.

    All methods return strings, which can be passed to `subprocess.run`_.

    Notes
    -----
    Subclasses ``str`` purely to convince ``mypy`` that this holds:

        isinstance(cmd("some command"), str)

    .. _python command line:
        https://docs.python.org/3/using/cmdline.html
    .. _subprocess.run:
        https://docs.python.org/3/library/subprocess.html#subprocess.run
    """

    def __new__(cls, *commands: str) -> str:  # type: ignore[misc]
        """
        Execute one or more statements as python code.

        Wraps `python -c`_.

        .. _python -c:
            https://docs.python.org/3/using/cmdline.html#cmdoption-c
        """
        command = ";".join(commands)
        return f"python -c {command!r}"

    @classmethod
    def mod(cls, module_name: str, *args: str) -> str:
        """
        Run the CLI of a standard library module.

        Wraps `python -m`_.

        See `Modules command-line interface`_ for a list of supported modules.

        .. _python -m:
            https://docs.python.org/3/using/cmdline.html#cmdoption-m
        .. _Modules command-line interface:
            https://docs.python.org/3/library/cmdline.html
        """
        return cls._maybe_options(f"python -m {module_name}", args)

    @classmethod
    def script(cls, source: str | Path, *args: str) -> str:
        """
        Execute the python code contained in ``source``.

        Wraps `script`_, (``python <script> [args]``).

        .. _script:
            https://docs.python.org/3/using/cmdline.html#command-line-and-environment
        """
        return cls._maybe_options(f"python {cls._str_path(source)}", args)

    @classmethod
    def mkdir(cls, source: str | Path, /) -> str:
        """
        Platform independent `bash mkdir`_, using ``--parents` option.

        .. _bash mkdir:
            https://ss64.com/bash/mkdir.html
        """
        s = cls._str_path(source)
        return cmd(
            "from pathlib import Path",
            f"Path({s!r}).mkdir(parents=True, exist_ok=True)",
        )

    @classmethod
    def rm_rf(cls, source: str | Path, /) -> str:
        """
        Platform independent `bash rm`_, using ``--recursive --force`` options.

        .. _bash rm:
            https://ss64.com/bash/rm.html
        """
        s = cls._str_path(source)
        if Path(source).is_file():
            return cmd(
                "from pathlib import Path", f"Path({s!r}).unlink(missing_ok=True)"
            )
        else:
            return cmd("import shutil", f"shutil.rmtree({s!r}, ignore_errors=True)")

    @staticmethod
    def _str_path(source: str | Path, /) -> str:
        """
        Normalize to a relative string path.

        - The commands this gets used in can serialize those cross-platform paths.
        - Getting expanded in the python runtime context.
        """
        return Path(source).resolve().relative_to(REPO_ROOT).as_posix()

    @staticmethod
    def _maybe_options(command: str, args: tuple[str, ...] | tuple[()], /) -> str:
        return f'{command} {" ".join(args)}' if args else command


### NOTE: TOML utils


def toml_deep_get(
    doc: _TOMLDocument, *keys: str, populate_missing: bool = False
) -> _Container:
    """
    Get a nested table from ``doc``.

    Parameters
    ----------
    doc
        Container instance.
    *keys
        Path to the target table.
        Each *key* represents a part of a dotted table key.
    populate_missing
        Create intermediate table(s) when any of ``keys`` are not present.

        .. warning::
            Mutates ``doc`` in-place.
    """
    get = _deep_get_default if populate_missing else _deep_get
    it = iter(keys)
    value = get(doc, next(it))
    for key in it:
        value = get(value, key)
    return value


def toml_deep_set(
    m: _MappingUpdates[str, Any],
    *keys: str,
    doc: _TOMLDocument | None = None,
    how: MergeStrategy = "update",
) -> _TOMLDocument:
    """
    Create a table and insert it by following a nested path.

    Parameters
    ----------
    m
        Incoming items to insert into a ``TOMLDocument``.
    *keys
        Path to the target table.
        Each *key* represents a part of a dotted table key.
    doc
        Container instance.
        By default, an empty document is created.
    how
        How to handle adding items to an existing table.
    """
    if doc is None:
        doc = tomlkit.document()
    leaf = toml_deep_get(doc, *keys, populate_missing=True)
    if how == "replace":
        leaf.clear()
    leaf.update(m)
    return doc


def _deep_get(container: _Container, key: str, /) -> _Container:
    item = container.item(key)
    return _unwrap_table(item)


def _deep_get_default(container: _Container, key: str, /) -> _Container:
    try:
        item = container.item(key)
    except tomlkit.exceptions.NonExistentKey:
        container.add(key, tomlkit.table())
        item = container.item(key)
    return _unwrap_table(item)


def _unwrap_table(item: _Item, /) -> _Container:
    if isinstance(item, _Table):
        return item.value
    msg = f"Expected a table, but got: {type(item).__name__!r}\n{item!r}"
    raise TypeError(msg)


def _is_updating(file: str | Path, /) -> bool:
    fp = Path(file)
    return bool(fp.exists() and fp.stat().st_size)
