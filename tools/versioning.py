"""
Versioning utils, specfic to `vega projects`_.

Includes non-`python` projects.

.. _vega projects:
    https://github.com/vega

Examples
--------
>>> from tools.versioning import VERSIONS  # doctest: +SKIP
>>> VERSIONS["vega-lite"]  # doctest: +SKIP
'v5.20.1'

>>> VERSIONS  # doctest: +SKIP
{'vega-datasets': 'v2.11.0',
 'vega-embed': '6',
 'vega-lite': 'v5.20.1',
 'vegafusion': '1.5.0',
 'vl-convert-python': '1.7.0'}
"""

from __future__ import annotations

import sys
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

if sys.version_info >= (3, 11):
    import tomllib
else:
    # NOTE: See https://github.com/hukkin/tomli?tab=readme-ov-file#building-a-tomlitomllib-compatibility-layer
    import tomli as tomllib  # type: ignore
from packaging.version import parse as parse_version

import vl_convert as vlc
from tools.schemapi.utils import spell_literal

if TYPE_CHECKING:
    from collections.abc import Iterable, Mapping, Sequence

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias

__all__ = ["VERSIONS", "update_all_versions"]

_TABLE_PATH: Sequence[LiteralString] = "tool", "altair", "vega"
_REPO_ROOT: Path = Path(__file__).parent.parent
_JUPYTER_INDEX = "altair/jupyter/js/index.js"

VegaProject: TypeAlias = Literal[
    "vega-datasets", "vega-embed", "vega-lite", "vegafusion", "vl-convert-python"
]
VERSIONS: Mapping[VegaProject, str]


def _read_pyproject_toml(fp: Path | None = None, /) -> dict[str, Any]:
    source = fp or Path(__file__).parent.parent / "pyproject.toml"
    return tomllib.loads(source.read_text("utf-8"))


def _keypath(mapping: Mapping[str, Any], path: Iterable[str], /) -> Any:
    """Get a nested table from ``mapping`` by following ``path``."""
    mut = dict[str, Any](**mapping)
    for key in path:
        mut = mut[key]
    return mut


def update_vega_embed() -> None:
    """Updates the **Vega-Lite** version used in ``JupyterChart``."""
    fp = _REPO_ROOT / _JUPYTER_INDEX
    embed = VERSIONS["vega-embed"]
    vega = parse_version(vlc.get_vega_version()).major
    lite = VERSIONS["vega-lite"].lstrip("v")
    stmt = f'import vegaEmbed from "https://esm.sh/vega-embed@{embed}?deps=vega@{vega}&deps=vega-lite@{lite}";\n'

    with fp.open("r", encoding="utf-8", newline="\n") as f:
        lines = deque(f.readlines())
    lines.popleft()
    print(f"Updating import in {fp.as_posix()!r}, to:\n  {stmt!r}")
    lines.appendleft(stmt)
    with fp.open("w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)


def inline_versions_literal(name: str, /) -> Iterable[str]:
    """
    Yields the ``[tool.altair.vega]`` table as an inline ``dict``.

    Includes a type annotation and docstring.

    Parameters
    ----------
    name
        Variable name for the literal.

    Notes
    -----
    - Write at the bottom of ``altair.utils.schemapi``.
    - Used in ``altair.utils._importers``.
    """
    ann = f"Mapping[{spell_literal(VERSIONS)}, str]"
    table = f"[{'.'.join(_TABLE_PATH)}]"
    yield f"{name}: {ann} = {VERSIONS!r}\n"
    yield '"""\n'
    yield (
        "Version pins for non-``python`` `vega projects`_.\n\n"
        "Notes\n"
        "-----\n"
        f"When cutting a new release, make sure to update ``{table}`` in ``pyproject.toml``.\n\n"
        ".. _vega projects:\n"
        "    https://github.com/vega\n"
    )
    yield '"""\n'


def update_all_versions() -> None:
    print("Updating Vega project pins")
    update_vega_embed()


def __getattr__(name: str) -> Mapping[VegaProject, str]:
    if name == "VERSIONS":
        global VERSIONS
        VERSIONS = _keypath(_read_pyproject_toml(), _TABLE_PATH)
        return VERSIONS
    else:
        msg = f"module {__name__!r} has no attribute {name!r}"
        raise AttributeError(msg)
