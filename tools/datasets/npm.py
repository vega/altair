from __future__ import annotations

import json
import urllib.request
from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal

import polars as pl

from tools.datasets import semver
from tools.datasets.models import NpmUrl

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    if sys.version_info >= (3, 13):
        from typing import TypeIs
    else:
        from typing_extensions import TypeIs
    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.datasets._typing import Extension
    from tools.datasets.models import NpmPackageMetadataResponse

    ReadFn: TypeAlias = Callable[..., pl.DataFrame]

__all__ = ["Npm"]


def is_ext_supported(suffix: str) -> TypeIs[Extension]:
    return suffix in {".csv", ".json", ".tsv", ".arrow"}


class Npm:
    """https://www.jsdelivr.com/docs/data.jsdelivr.com#overview."""

    _read_fn: ClassVar[dict[Extension, ReadFn]] = {
        ".csv": pl.read_csv,
        ".json": pl.read_json,
        ".tsv": partial(pl.read_csv, separator="\t"),
        ".arrow": partial(pl.read_ipc, use_pyarrow=True),
    }
    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def __init__(
        self,
        output_dir: Path,
        name_tags: str,
        *,
        jsdelivr: Literal["jsdelivr"] = "jsdelivr",
        npm: Literal["npm"] = "npm",
        package: LiteralString = "vega-datasets",
        jsdelivr_version: LiteralString = "v1",
    ) -> None:
        output_dir.mkdir(exist_ok=True)
        self._paths: dict[Literal["tags"], Path] = {
            "tags": output_dir / f"{name_tags}.parquet"
        }
        self._url: NpmUrl = NpmUrl(
            CDN=f"https://cdn.{jsdelivr}.net/{npm}/{package}@",
            TAGS=f"https://data.{jsdelivr}.com/{jsdelivr_version}/packages/{npm}/{package}",
        )

    @property
    def url(self) -> NpmUrl:
        return self._url

    @classmethod
    def reader_from(cls, url: str, /) -> ReadFn:
        suffix = Path(url).suffix
        if is_ext_supported(suffix):
            return cls._read_fn[suffix]
        else:
            msg = f"Unexpected file extension {suffix!r}, from:\n{url}"
            raise NotImplementedError(msg)

    def dataset(self, url: str, /, **kwds: Any) -> pl.DataFrame:
        """
        Fetch a remote dataset.

        Parameters
        ----------
        url
            Full path to a known dataset.
        **kwds
            Arguments passed to the underlying read function.
        """
        fn = self.reader_from(url)
        with self._opener.open(url) as f:
            return fn(f.read(), **kwds)

    def tags(self) -> pl.DataFrame:
        """
        Request, parse tags from `Get package metadata`_.

        Notes
        -----
        - Ignores canary releases
        - ``npm`` can accept either, but this endpoint returns without "v":

            {tag}
            v{tag}

        .. _Get package metadata:
            https://www.jsdelivr.com/docs/data.jsdelivr.com#get-/v1/packages/npm/-package-
        """
        req = urllib.request.Request(
            self.url.TAGS, headers={"Accept": "application/json"}
        )
        with self._opener.open(req) as response:
            content: NpmPackageMetadataResponse = json.load(response)
        versions = [
            f"v{tag}"
            for v in content["versions"]
            if (tag := v["version"]) and semver.CANARY not in tag
        ]
        return pl.DataFrame({"tag": versions}).pipe(semver.with_columns)
