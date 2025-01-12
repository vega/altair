from __future__ import annotations

import json
import urllib.request
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal

import polars as pl

from tools.datasets import datapackage, semver
from tools.datasets.models import NpmUrl

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from altair.datasets._typing import Version
    from tools.datasets.models import (
        FlPackage,
        NpmPackageMetadataResponse,
        ParsedPackage,
    )


__all__ = ["Npm"]


class Npm:
    """https://www.jsdelivr.com/docs/data.jsdelivr.com#overview."""

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
        self._paths: dict[Literal["tags", "datapackage"], Path] = {
            "tags": output_dir / f"{name_tags}.parquet",
            "datapackage": output_dir / "datapackage.json",
        }
        self._url: NpmUrl = NpmUrl(
            CDN=f"https://cdn.{jsdelivr}.net/{npm}/{package}@",
            TAGS=f"https://data.{jsdelivr}.com/{jsdelivr_version}/packages/{npm}/{package}",
            GH=f"https://cdn.{jsdelivr}.net/gh/vega/{package}@",
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
        with self._opener.open(req) as response:
            content: NpmPackageMetadataResponse = json.load(response)
        versions = [
            f"v{tag}"
            for v in content["versions"]
            if (tag := v["version"]) and semver.CANARY not in tag
        ]
        return pl.DataFrame({"tag": versions}).pipe(semver.with_columns)

    def file_gh(
        self,
        branch_or_tag: Literal["main"] | Version | LiteralString,
        path: str,
        /,
    ) -> Any:
        """
        Request a file from the `jsdelivr GitHub`_ endpoint.

        Parameters
        ----------
        branch_or_tag
            Version of the file, see `branches`_ and `tags`_.
        path
            Relative filepath from the root of the repo.

        .. _jsdelivr GitHub:
            https://www.jsdelivr.com/documentation#id-github
        .. _branches:
            https://github.com/vega/vega-datasets/branches
        .. _tags:
            https://github.com/vega/vega-datasets/tags
        """
        path = path.lstrip("./")
        suffix = Path(path).suffix
        if suffix == ".json":
            headers = {"Accept": "application/json"}
            read_fn = json.load
        else:
            raise NotImplementedError(path, suffix)
        req = urllib.request.Request(
            f"{self.url.GH}{branch_or_tag}/{path}", headers=headers
        )
        with self._opener.open(req) as response:
            return read_fn(response)

    def datapackage(
        self, *, tag: LiteralString | None = None, frozen: bool = False
    ) -> ParsedPackage:
        pkg: FlPackage = (
            json.loads(self._paths["datapackage"].read_text("utf-8"))
            if frozen
            else self.file_gh(tag or "main", "datapackage.json")
        )
        return datapackage.parse_package(pkg)
