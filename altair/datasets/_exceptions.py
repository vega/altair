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
        if meta["is_image"]:
            reason = "Image data is non-tabular."
            return cls(f"{_failed_tabular(meta)}{reason}{_suggest_url(meta)}")
        elif not meta["is_tabular"] or meta["suffix"] in {".arrow", ".parquet"}:
            if meta["suffix"] in {".arrow", ".parquet"}:
                install: tuple[str, ...] = "pyarrow", "polars"
                what = f"{meta['suffix']!r}"
            else:
                install = ("polars",)
                if meta["is_spatial"]:
                    what = "Geospatial data"
                elif meta["is_json"]:
                    what = "Non-tabular json"
                else:
                    what = f"{meta['file_name']!r}"
            reason = _why(what, backend_name)
            return cls(f"{_failed_tabular(meta)}{reason}{_suggest_url(meta, *install)}")
        else:
            return cls(_implementation_not_found(meta))

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


def _why(what: str, backend_name: str, /) -> str:
    return f"{what} is not supported natively by {backend_name!r}."


def _suggest_url(meta: Metadata, *install_other: str) -> str:
    other = ""
    if install_other:
        others = " or ".join(f"`{other}`" for other in install_other)
        other = f" installing {others}, or use"
    return (
        f"\n\nInstead, try{other}:\n"
        "    from altair.datasets import data\n"
        f"    data.{meta['dataset_name']}.url"
    )


def _implementation_not_found(meta: Metadata, /) -> str:
    """Search finished without finding a *declared* incompatibility."""
    INDENT = " " * 4
    record = f",\n{INDENT}".join(
        f"{k}={v!r}"
        for k, v in meta.items()
        if not (k.startswith(("is_", "sha", "bytes", "has_")))
        or (v is True and k.startswith("is_"))
    )
    return f"Found no implementation that supports:\n{INDENT}{record}"
