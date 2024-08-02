"""Fills the contents of doc/user_guide/api.rst based on the updated Altair schema."""

from __future__ import annotations

import types
from pathlib import Path
from types import ModuleType
from typing import Final, Iterator

import altair as alt

API_FILENAME: Final = str(Path.cwd() / "doc" / "user_guide" / "api.rst")

API_TEMPLATE: Final = """\
.. _api:

API Reference
=============

This is the class and function reference of Altair, and the following content
is generated automatically from the code documentation strings.
Please refer to the `full user guide <http://altair-viz.github.io>`_ for
further details, as this low-level documentation may not be enough to give
full guidelines on their use.

Top-Level Objects
-----------------
.. currentmodule:: altair

.. autosummary::
   :toctree: generated/toplevel/
   :nosignatures:

   {toplevel_charts}

Encoding Channels
-----------------
.. currentmodule:: altair

.. autosummary::
   :toctree: generated/channels/
   :nosignatures:

   {encoding_wrappers}

API Functions
-------------
.. currentmodule:: altair

.. autosummary::
   :toctree: generated/api/
   :nosignatures:

   {api_functions}

Low-Level Schema Wrappers
-------------------------
.. currentmodule:: altair

.. autosummary::
   :toctree: generated/core/
   :nosignatures:

   {lowlevel_wrappers}

API Utility Classes
-------------------
.. currentmodule:: altair

.. autosummary::
   :toctree: generated/api-cls/
   :nosignatures:

   {api_classes}
"""


def iter_objects(
    mod: ModuleType,
    ignore_private: bool = True,
    restrict_to_type: type | None = None,
    restrict_to_subclass: type | None = None,
) -> Iterator[str]:
    for name in dir(mod):
        obj = getattr(mod, name)
        if ignore_private and name.startswith("_"):
            continue
        if restrict_to_type is not None and not isinstance(obj, restrict_to_type):
            continue
        if restrict_to_subclass is not None and (
            not (isinstance(obj, type) and issubclass(obj, restrict_to_subclass))
        ):
            continue
        if hasattr(obj, "__deprecated__"):
            continue
        yield name


def toplevel_charts() -> list[str]:
    return sorted(iter_objects(alt.api, restrict_to_subclass=alt.TopLevelMixin))  # type: ignore[attr-defined]


def encoding_wrappers() -> list[str]:
    return sorted(iter_objects(alt.channels, restrict_to_subclass=alt.SchemaBase))


def api_functions() -> list[str]:
    # Exclude `typing` functions/SpecialForm(s)
    altair_api_functions = [
        obj_name
        for obj_name in iter_objects(alt.api, restrict_to_type=types.FunctionType)  # type: ignore[attr-defined]
        if obj_name not in {"cast", "overload", "NamedTuple", "TypedDict"}
    ]
    return sorted(altair_api_functions)


def api_classes() -> list[str]:
    # Part of the Public API, but are not inherited from `vega-lite`.
    return ["expr", "When", "Then", "ChainedWhen"]


def lowlevel_wrappers() -> list[str]:
    objects = sorted(iter_objects(alt.schema.core, restrict_to_subclass=alt.SchemaBase))  # type: ignore[attr-defined]
    # The names of these two classes are also used for classes in alt.channels. Due to
    # how imports are set up, these channel classes overwrite the two low-level classes
    # in the top-level Altair namespace. Therefore, they cannot be imported as e.g.
    # altair.Color (which gives you the Channel class) and therefore Sphinx won't
    # be able to produce a documentation page.
    objects = [o for o in objects if o not in {"Color", "Text"}]
    return objects


def write_api_file() -> None:
    print(f"Updating API docs\n  ->{API_FILENAME}")
    sep = "\n   "
    Path(API_FILENAME).write_text(
        API_TEMPLATE.format(
            toplevel_charts=sep.join(toplevel_charts()),
            api_functions=sep.join(api_functions()),
            encoding_wrappers=sep.join(encoding_wrappers()),
            lowlevel_wrappers=sep.join(lowlevel_wrappers()),
            api_classes=sep.join(api_classes()),
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_api_file()
