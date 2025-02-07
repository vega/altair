from __future__ import annotations

import json
import string
import urllib.request
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal, NamedTuple
from urllib.request import Request

from tools.datasets import datapackage

if TYPE_CHECKING:
    import sys
    from urllib.request import OpenerDirector

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    if sys.version_info >= (3, 10):
        from typing import TypeAlias
    else:
        from typing_extensions import TypeAlias
    from tools.datasets import PathMap
    from tools.datasets.datapackage import DataPackage

    BranchOrTag: TypeAlias = 'Literal["main"] | LiteralString'


__all__ = ["Npm"]


class NpmUrl(NamedTuple):
    CDN: LiteralString
    GH: LiteralString


class Npm:
    """https://www.jsdelivr.com/docs/data.jsdelivr.com#overview."""

    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def __init__(
        self,
        paths: PathMap,
        *,
        jsdelivr: Literal["jsdelivr"] = "jsdelivr",
        npm: Literal["npm"] = "npm",
        package: LiteralString = "vega-datasets",
    ) -> None:
        self.paths: PathMap = paths
        self._url: NpmUrl = NpmUrl(
            CDN=f"https://cdn.{jsdelivr}.net/{npm}/{package}@",
            GH=f"https://cdn.{jsdelivr}.net/gh/vega/{package}@",
        )

    def _prefix(self, version: BranchOrTag, /) -> LiteralString:
        return f"{self.url.GH if is_branch(version) else self.url.CDN}{version}/"

    def dataset_base_url(self, version: BranchOrTag, /) -> LiteralString:
        """Common url prefix for all datasets derived from ``version``."""
        return f"{self._prefix(version)}data/"

    @property
    def url(self) -> NpmUrl:
        return self._url

    def file(
        self,
        branch_or_tag: BranchOrTag,
        path: str,
        /,
    ) -> Any:
        """
        Request a file from `jsdelivr`  `npm`_ or `GitHub`_ endpoints.

        Parameters
        ----------
        branch_or_tag
            Version of the file, see `branches`_ and `tags`_.
        path
            Relative filepath from the root of the repo.

        .. _npm:
            https://www.jsdelivr.com/documentation#id-npm
        .. _GitHub:
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
        req = Request(f"{self._prefix(branch_or_tag)}{path}", headers=headers)
        with self._opener.open(req) as response:
            return read_fn(response)

    def datapackage(self, *, tag: LiteralString) -> DataPackage:
        return datapackage.DataPackage(
            self.file(tag, "datapackage.json"),
            self.dataset_base_url(tag),
            self.paths["metadata"],
        )


def is_branch(s: BranchOrTag, /) -> bool:
    return s == "main" or not (s.startswith(tuple("v" + string.digits)))
