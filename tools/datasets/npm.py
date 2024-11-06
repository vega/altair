from __future__ import annotations

import json
import urllib.request
from typing import TYPE_CHECKING, Literal

import polars as pl

from tools.datasets import semver
from tools.datasets.models import NpmUrl

if TYPE_CHECKING:
    import sys
    from pathlib import Path

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from tools.datasets.models import NpmPackageMetadataResponse

__all__ = ["Npm"]


class Npm:
    """https://www.jsdelivr.com/docs/data.jsdelivr.com#overview."""

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
        with urllib.request.urlopen(req) as response:
            content: NpmPackageMetadataResponse = json.load(response)
        versions = [
            f"v{tag}"
            for v in content["versions"]
            if (tag := v["version"]) and semver.CANARY not in tag
        ]
        return pl.DataFrame({"tag": versions}).pipe(semver.with_columns)
