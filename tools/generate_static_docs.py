"""Render and write to `./doc/_static/.*` files."""

from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Literal, Mapping

output_dir = Path.cwd() / "doc" / "_static"

TARGETS: Mapping[str, str] = {
    "tests.altair_theme_test.render_theme_test": "vega-altair_theme_test.html",
}
"""
Maps qualified function name to output file name.

The rendering function should have a signature like::

    def render() -> bytes | str: ...
"""


def render_write(qual_name: str, output: Path) -> None:
    module_name, func_name = qual_name.rsplit(".", 1)
    mod = import_module(module_name)
    if (func := getattr(mod, func_name)) and callable(func):
        content = func()
        kwds: dict[Literal["mode", "encoding"], Any]
        if isinstance(content, str):
            kwds = {"mode": "w", "encoding": "utf-8"}
        elif isinstance(content, bytes):
            kwds = {"mode": "wb"}
        else:
            raise TypeError(content)
        with output.open(**kwds) as f:  # type: ignore[misc]
            f.write(content)
    else:
        raise TypeError(mod, func_name)


def write_static_docs() -> None:
    print("Updating static docs")
    for qual_name, output_file_name in TARGETS.items():
        output: Path = output_dir / output_file_name
        print(f" {qual_name}\n  ->{output!s}")
        render_write(qual_name, output)


if __name__ == "__main__":
    write_static_docs()
