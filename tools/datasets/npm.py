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
    """
    CDN access for vega-datasets with VegaFusion compatibility.

    Uses GitHub Raw as the primary CDN for VegaFusion compatibility.
    """

    _opener: ClassVar[OpenerDirector] = urllib.request.build_opener()

    def __init__(
        self,
        paths: PathMap,
        *,
        package: LiteralString = "vega-datasets",
    ) -> None:
        self.paths: PathMap = paths
        self._url: NpmUrl = NpmUrl(
            CDN=f"https://cdn.jsdelivr.net/npm/{package}@",
            GH=f"https://raw.githubusercontent.com/vega/{package}/",
        )

    def _prefix(self, version: BranchOrTag, /) -> LiteralString:
        # Use GitHub Raw for all versions (VegaFusion compatible)
        # TODO: Track VegaFusion HTTP client issue: https://github.com/vega/vegafusion/issues/569
        #       jsdelivr CDN URLs cause "Content-Length Header missing from response" errors
        #       Previous code: return f"{self.url.GH if is_branch(version) else self.url.CDN}{version}/"
        return f"{self.url.GH}{version}/"

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
        Request a file from GitHub Raw or jsdelivr endpoints.

        Parameters
        ----------
        branch_or_tag
            Version of the file, see `branches`_ and `tags`_.
        path
            Relative filepath from the root of the repo.

        Notes
        -----
        Uses GitHub Raw as primary CDN for VegaFusion compatibility.

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
