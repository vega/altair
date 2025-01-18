from __future__ import annotations

import json
import string
import urllib.request
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal, NamedTuple

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
    from tools.datasets.models import Package

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

    def dataset_base_url(self, version: BranchOrTag, /) -> LiteralString:
        """
        Common url prefix for all datasets derived from ``version``.

        Notes
        -----
        - Encodes the endpoint at this stage
            - Use github if its the only option (since its slower otherwise)
            - npm only has releases/tags (not branches)
        """
        return f"{self.url.GH if is_branch(version) else self.url.CDN}{version}/data/"

    @property
    def url(self) -> NpmUrl:
        return self._url

    def file_gh(
        self,
        branch_or_tag: BranchOrTag,
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

    def datapackage(self, *, tag: LiteralString, frozen: bool = False) -> DataPackage:
        pkg: Package = (
            json.loads(self.paths["datapackage"].read_text("utf-8"))
            if frozen
            else self.file_gh(tag, "datapackage.json")
        )
        return datapackage.DataPackage(
            pkg, self.dataset_base_url(tag), self.paths["metadata"]
        )


def is_branch(s: BranchOrTag, /) -> bool:
    return s == "main" or not (s.startswith(tuple("v" + string.digits)))
