from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from altair.datasets._readers import _Backend
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
    def from_priority(cls, priority: Sequence[_Backend], /) -> AltairDatasetsError:
        msg = f"Found no supported backend, searched:\n{priority!r}"
        return cls(msg)


def module_not_found(
    backend_name: str, reqs: str | tuple[str, ...], missing: str
) -> ModuleNotFoundError:
    if isinstance(reqs, tuple):
        depends = ", ".join(f"{req!r}" for req in reqs) + " packages"
    else:
        depends = f"{reqs!r} package"
    msg = (
        f"Backend {backend_name!r} requires the {depends}, but {missing!r} could not be found.\n"
        f"This can be installed with pip using:\n"
        f"    pip install {missing}\n"
        f"Or with conda using:\n"
        f"    conda install -c conda-forge {missing}"
    )
    return ModuleNotFoundError(msg, name=missing)


def image(meta: Metadata, /) -> AltairDatasetsError:
    msg = f"{_failed_tabular(meta)}\n{_suggest_url(meta)}"
    return AltairDatasetsError(msg)


def geospatial(meta: Metadata, backend_name: str) -> NotImplementedError:
    msg = (
        f"{_failed_tabular(meta)}"
        f"Geospatial data is not supported natively by {backend_name!r}."
        f"{_suggest_url(meta, 'polars')}"
    )
    return NotImplementedError(msg)


def non_tabular_json(meta: Metadata, backend_name: str) -> NotImplementedError:
    msg = (
        f"{_failed_tabular(meta)}"
        f"Non-tabular json is not supported natively by {backend_name!r}."
        f"{_suggest_url(meta, 'polars')}"
    )
    return NotImplementedError(msg)


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
