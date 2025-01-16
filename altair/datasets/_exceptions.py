from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from altair.datasets._readers import _Backend
    from altair.datasets._typing import Metadata


class AltairDatasetsError(Exception):
    # TODO: Rename, try to reduce verbosity of message, link to vegafusion?
    @classmethod
    def url_parquet(cls, meta: Metadata, /) -> AltairDatasetsError:
        name = meta["file_name"]
        msg = (
            f"Currently unable to load {name!r} via url, as '.parquet' datasets require `vegafusion`.\n"
            "See upstream issue for details: https://github.com/vega/vega/issues/3961"
        )
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


# TODO: Give more direct help (e.g. url("7zip"))
def image(meta: Metadata):
    name = meta["file_name"]
    ext = meta["suffix"]
    msg = (
        f"Unable to load {name!r} as tabular data.\n"
        f"{ext!r} datasets are only compatible with `url(...)` or `Loader.url(...)`."
    )
    return AltairDatasetsError(msg)


# TODO: Pass in `meta`
def geospatial(backend_name: str) -> NotImplementedError:
    msg = _suggest_supported(
        f"Geospatial data is not supported natively by {backend_name!r}."
    )
    return NotImplementedError(msg)


# TODO: Pass in `meta`
def non_tabular_json(backend_name: str) -> NotImplementedError:
    msg = _suggest_supported(f"Non-tabular json is not supported {backend_name!r}.")
    return NotImplementedError(msg)


def _suggest_supported(msg: str) -> str:
    return f"{msg}\nTry installing `polars` or using `Loader.url(...)` instead."
