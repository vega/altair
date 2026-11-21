"""
Versioning utils, specific to `vega projects`_.

Includes non-`python` projects.

.. _vega projects:
    https://github.com/vega

Examples
--------
>>> from tools.versioning import VERSIONS  # doctest: +SKIP
>>> VERSIONS["vega-lite"]  # doctest: +SKIP
'v6.1.0'

>>> VERSIONS  # doctest: +SKIP
{'vega-datasets': 'v3',
 'vega-embed': '7',
 'vega-lite': 'v6.1.0',
 'vegafusion': '1.5.0',
 'vl-convert-python': '1.8.0'}
"""

from __future__ import annotations

import re
import tomllib
from collections import deque
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal

from packaging.requirements import Requirement
from packaging.version import parse as parse_version

import vl_convert as vlc
from tools.schemapi.utils import spell_literal

if TYPE_CHECKING:
    from collections.abc import (
        ItemsView,
        Iterable,
        Iterator,
        KeysView,
        Mapping,
        Sequence,
    )
    from typing import LiteralString, TypeAlias

__all__ = ["VERSIONS"]

_REPO_ROOT: Path = Path(__file__).parent.parent
_JUPYTER_INDEX = "altair/jupyter/js/index.js"
_PYPROJECT: Literal["pyproject.toml"] = "pyproject.toml"
_LOWER_BOUNDS = frozenset((">=", "==", "~=", "==="))
_CDN_PROJECT_RE = re.compile(
    r"(?P<prefix>https://cdn\.jsdelivr\.net/npm/)"
    r"(?P<project>vega(?:-lite|-embed)?)@"
    r"(?P<version>\d+(?:\.\d+)*)"
)

VegaProjectPy: TypeAlias = Literal["vegafusion", "vl-convert-python"]
VegaProject: TypeAlias = Literal[
    "vega-datasets", "vega-embed", "vega-lite", "vegafusion", "vl-convert-python"
]

VERSIONS: _Versions
"""Singleton ``_Versions`` instance."""


def _read_pyproject_toml(fp: Path | None = None, /) -> dict[str, Any]:
    source = fp or Path(__file__).parent.parent / _PYPROJECT
    return tomllib.loads(source.read_text("utf-8"))


def _keypath(mapping: Mapping[str, Any], path: Iterable[str], /) -> Any:
    """Get a nested table from ``mapping`` by following ``path``."""
    mut = dict[str, Any](**mapping)
    for key in path:
        mut = mut[key]
    return mut


class _Versions:
    _TABLE_PATH: ClassVar[Sequence[LiteralString]] = "tool", "altair", "vega"
    """
    The table header path split by ``"."``::

        [tool.altair.vega] -> "tool", "altair", "vega"
    """
    _PY_DEPS_PATH: ClassVar[Sequence[LiteralString]] = (
        "project",
        "optional-dependencies",
    )
    _PY_DEPS: ClassVar[frozenset[VegaProjectPy]] = frozenset(
        ("vl-convert-python", "vegafusion")
    )

    _CONST_NAME: ClassVar[Literal["VERSIONS"]] = "VERSIONS"
    """Variable name for the exported literal."""

    _mapping: Mapping[VegaProject, str]

    def __init__(self) -> None:
        pyproject = _read_pyproject_toml()
        py_deps = _keypath(pyproject, self._PY_DEPS_PATH)
        js_deps = _keypath(pyproject, self._TABLE_PATH)
        all_deps = chain(js_deps.items(), self._iter_py_deps_versions(py_deps))
        self._mapping = dict(sorted(all_deps))

    def __getitem__(self, key: VegaProject) -> str:
        return self._mapping[key]

    def __repr__(self) -> str:
        return repr(self._mapping)

    def projects(self) -> KeysView[VegaProject]:
        return self._mapping.keys()

    def items(self) -> ItemsView[VegaProject, str]:
        return self._mapping.items()

    @property
    def vlc_vega(self) -> str:
        """
        Returns version of `Vega`_ bundled with `vl-convert`_.

        .. _Vega:
            https://github.com/vega/vega
        .. _vl-convert:
            https://github.com/vega/vl-convert
        """
        return vlc.get_vega_version()

    @property
    def vlc_vega_embed(self) -> str:
        """
        Returns version of `Vega-Embed`_ bundled with `vl-convert`_.

        .. _Vega-Embed:
            https://github.com/vega/vega-embed
        .. _vl-convert:
            https://github.com/vega/vl-convert
        """
        return vlc.get_vega_embed_version()

    @property
    def vlc_vega_themes(self) -> str:
        """
        Returns version of `Vega-Themes`_ bundled with `vl-convert`_.

        .. _Vega-Themes:
            https://github.com/vega/vega-themes
        .. _vl-convert:
            https://github.com/vega/vl-convert.
        """
        return vlc.get_vega_themes_version()

    @property
    def vlc_vegalite(self) -> list[str]:
        """
        Returns versions of `Vega-Lite`_ bundled with `vl-convert`_.

        .. _Vega-Lite:
            https://github.com/vega/vega-lite
        .. _vl-convert:
            https://github.com/vega/vl-convert
        """
        return vlc.get_vegalite_versions()

    @property
    def _annotation(self) -> str:
        return f"Mapping[{spell_literal(self.projects())}, str]"

    @property
    def _header(self) -> str:
        return f"[{'.'.join(self._TABLE_PATH)}]"

    def iter_inline_literal(self) -> Iterator[str]:
        """
        Yields the ``[tool.altair.vega]`` table as an inline ``dict``.

        Includes a type annotation and docstring.

        Notes
        -----
        - Write at the bottom of ``altair.utils.schemapi``.
        - Used in ``altair.utils._importers``.
        """
        yield f"{self._CONST_NAME}: {self._annotation} = {self!r}\n"
        yield '"""\n'
        yield (
            "Version pins for non-``python`` `vega projects`_.\n\n"
            "Notes\n"
            "-----\n"
            f"When cutting a new release, make sure to update ``{self._header}`` in ``pyproject.toml``.\n\n"
            ".. _vega projects:\n"
            "    https://github.com/vega\n"
        )
        yield '"""\n'

    def update_all(self) -> None:
        """Update all static version pins."""
        print("Updating Vega project pins")
        self.update_vega_embed()
        self.update_display()
        self.update_cdn_references()

    def update_vega_embed(self) -> None:
        """Updates the **Vega-Lite** version used in ``JupyterChart``."""
        fp = _REPO_ROOT / _JUPYTER_INDEX
        embed = self["vega-embed"]
        vega = parse_version(self.vlc_vega).major
        vegalite = self["vega-lite"].lstrip("v")
        stmt = f'import vegaEmbed from "https://esm.sh/vega-embed@{embed}?deps=vega@{vega}&deps=vega-lite@{vegalite}";\n'

        with fp.open("r", encoding="utf-8", newline="\n") as f:
            lines = deque(f.readlines())
        lines.popleft()
        print(f"Updating import in {fp.as_posix()!r}, to:\n  {stmt!r}")
        lines.appendleft(stmt)
        with fp.open("w", encoding="utf-8", newline="\n") as f:
            f.writelines(lines)

    def update_display(self) -> None:
        """Update versions and MIME types used by the current display module."""
        vegalite = parse_version(self["vega-lite"].lstrip("v")).major
        vega = parse_version(self.vlc_vega).major
        vega_embed = parse_version(self["vega-embed"].lstrip("v")).major
        fp = _REPO_ROOT / f"altair/vegalite/v{vegalite}/display.py"
        replacements = {
            r'VEGA_VERSION: Final = "\d+(?:\.\d+)*"': (
                f'VEGA_VERSION: Final = "{vega}"'
            ),
            r'VEGAEMBED_VERSION: Final = "\d+(?:\.\d+)*"': (
                f'VEGAEMBED_VERSION: Final = "{vega_embed}"'
            ),
            r"application/vnd\.vegalite\.v\d+\.json": (
                f"application/vnd.vegalite.v{vegalite}.json"
            ),
            r"application/vnd\.vega\.v\d+\.json": (
                f"application/vnd.vega.v{vega}.json"
            ),
        }
        self._replace_patterns(fp, replacements)

    def update_cdn_references(self) -> None:
        """Update CDN major versions in static docs and their regression test."""
        vegalite = parse_version(self["vega-lite"].lstrip("v")).major
        versions = {
            "vega": parse_version(self.vlc_vega).major,
            "vega-lite": vegalite,
            "vega-embed": parse_version(self["vega-embed"].lstrip("v")).major,
        }
        paths = (
            _REPO_ROOT / "doc/_static/chart.html",
            _REPO_ROOT / "doc/user_guide/saving_charts.rst",
            _REPO_ROOT / f"tests/vegalite/v{vegalite}/test_api.py",
        )
        for fp in paths:
            source = fp.read_text("utf-8")

            def replace(match: re.Match[str]) -> str:
                project = match.group("project")
                return f"{match.group('prefix')}{project}@{versions[project]}"

            updated, count = _CDN_PROJECT_RE.subn(replace, source)
            if count != 3:
                msg = f"Expected 3 Vega CDN references in {fp}, found {count}"
                raise ValueError(msg)
            fp.write_text(updated, "utf-8", newline="\n")

    @staticmethod
    def _replace_patterns(fp: Path, replacements: Mapping[str, str]) -> None:
        source = fp.read_text("utf-8")
        for pattern, replacement in replacements.items():
            source, count = re.subn(pattern, replacement, source)
            if count != 1:
                msg = f"Expected one match for {pattern!r} in {fp}, found {count}"
                raise ValueError(msg)
        fp.write_text(source, "utf-8", newline="\n")

    def _iter_py_deps_versions(
        self, dep_groups: dict[str, Sequence[str]], /
    ) -> Iterator[tuple[VegaProjectPy, str]]:
        """
        Extract the name and lower version bound for all Vega python packages.

        Parameters
        ----------
        dep_groups
            Mapping of dependency/extra groups to requirement strings.

            .. note::
                It is expected that this is **either** `project.optional-dependencies`_ or `dependency-groups`_.

        .. _project.optional-dependencies:
            https://packaging.python.org/en/latest/specifications/pyproject-toml/#dependencies-optional-dependencies
        .. _dependency-groups:
            https://peps.python.org/pep-0735/
        """
        for deps in dep_groups.values():
            for req_string in deps:
                req = Requirement(req_string)
                if req.name in self._PY_DEPS:
                    it = (
                        parse_version(sp.version)
                        for sp in req.specifier
                        if sp.operator in _LOWER_BOUNDS
                    )
                    version = str(min(it))
                    yield req.name, version


def __getattr__(name: str) -> _Versions:
    if name == "VERSIONS":
        global VERSIONS
        VERSIONS = _Versions()
        return VERSIONS
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
