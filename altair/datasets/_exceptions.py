from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from altair.datasets._reader import _Backend
    from altair.datasets._typing import Metadata


class AltairDatasetsError(Exception):
    @classmethod
    def from_url(cls, meta: Metadata, /) -> AltairDatasetsError:
        if meta["suffix"] == ".parquet":
            msg = (
                f"{_failed_url(meta)}"
                f"{meta['suffix']!r} datasets require `vegafusion`.\n"
                "See upstream issue for details: https://github.com/vega/vega/issues/3961"
            )
        else:
            msg = (
                f"{cls.from_url.__qualname__}() called for "
                f"unimplemented extension: {meta['suffix']}\n\n{meta!r}"
            )
            raise NotImplementedError(msg)
        return cls(msg)

    @classmethod
    def from_tabular(cls, meta: Metadata, backend_name: str, /) -> AltairDatasetsError:
        install_other = None
        mid = "\n"
        if not meta["is_image"] and not meta["is_tabular"]:
            install_other = "polars"
            if meta["is_spatial"]:
                mid = f"Geospatial data is not supported natively by {backend_name!r}."
            elif meta["is_json"]:
                mid = f"Non-tabular json is not supported natively by {backend_name!r}."
        msg = f"{_failed_tabular(meta)}{mid}{_suggest_url(meta, install_other)}"
        return cls(msg)

    @classmethod
    def from_priority(cls, priority: Sequence[_Backend], /) -> AltairDatasetsError:
        msg = f"Found no supported backend, searched:\n{priority!r}"
        return cls(msg)


def module_not_found(
    backend_name: str, reqs: Sequence[str], missing: str
) -> ModuleNotFoundError:
    if len(reqs) == 1:
        depends = f"{reqs[0]!r} package"
    else:
        depends = ", ".join(f"{req!r}" for req in reqs) + " packages"
    msg = (
        f"Backend {backend_name!r} requires the {depends}, but {missing!r} could not be found.\n"
        f"This can be installed with pip using:\n"
        f"    pip install {missing}\n"
        f"Or with conda using:\n"
        f"    conda install -c conda-forge {missing}"
    )
    return ModuleNotFoundError(msg, name=missing)


def _failed_url(meta: Metadata, /) -> str:
    return f"Unable to load {meta['file_name']!r} via url.\n"


def _failed_tabular(meta: Metadata, /) -> str:
    return f"Unable to load {meta['file_name']!r} as tabular data.\n"


def _suggest_url(meta: Metadata, install_other: str | None = None) -> str:
    other = f" installing `{install_other}` or" if install_other else ""
    return (
        f"\n\nInstead, try{other}:\n\n"
        "    from altair.datasets import url\n"
        f"    url({meta['dataset_name']!r})"
    )


# TODO:
# - Use `AltairDatasetsError`
# - Remove notes from doc
# - Improve message and how data is selected
def implementation_not_found(meta: Metadata, /) -> NotImplementedError:
    """
    Search finished without finding a *declared* incompatibility.

    Notes
    -----
    - New kind of error
    - Previously, every backend had a function assigned
        - But they might not all work
    - Now, only things that are known to be widely safe are added
        - Should probably suggest using a pre-defined backend that supports everything
    - What can reach here?
        - `is_image` (all)
        - `"pandas"` (using inference wont trigger these)
          - `.arrow` (w/o `pyarrow`)
          - `.parquet` (w/o either `pyarrow` or `fastparquet`)
    """
    INDENT = " " * 4
    record = f",\n{INDENT}".join(
        f"{k}={v!r}"
        for k, v in meta.items()
        if not (k.startswith(("is_", "sha", "bytes", "has_")))
        or (v is True and k.startswith("is_"))
    )
    msg = f"Found no implementation that supports:\n{INDENT}{record}"
    return NotImplementedError(msg)
