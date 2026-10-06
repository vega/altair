from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tools.datasets.npm import Npm

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize("prefix", ["", "data/"], ids=["legacy", "relative"])
@pytest.mark.parametrize(
    ("tag", "base_url"),
    [
        ("v3.2.1", "https://cdn.jsdelivr.net/npm/vega-datasets@v3.2.1/data/"),
        ("main", "https://cdn.jsdelivr.net/gh/vega/vega-datasets@main/data/"),
    ],
    ids=["npm", "github"],
)
def test_datapackage_resource_paths(
    prefix: str,
    tag: str,
    base_url: str,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    datasets = [
        ("airports", "airports.csv", "csv", "table"),
        ("cars", "cars.json", "json", "table"),
        ("icon_7zip", "7zip.png", "png", "file"),
    ]
    resources = [
        {
            "name": name,
            "path": f"{prefix}{file_name}",
            "format": fmt,
            "type": resource_type,
            "bytes": 1,
            "hash": "sha1:example",
            "schema": None,
        }
        for name, file_name, fmt, resource_type in datasets
    ]

    def read_datapackage(branch_or_tag: str, path: str):
        assert branch_or_tag == tag
        assert path == "datapackage.json"
        return {"resources": resources}

    npm = Npm({"metadata": tmp_path / "metadata.parquet"})
    monkeypatch.setattr(npm, "file", read_datapackage)
    metadata = npm.datapackage(tag=tag).core.collect()

    assert metadata.select("dataset_name", "file_name", "suffix", "url").rows() == [
        (name, file_name, f".{fmt}", f"{base_url}{file_name}")
        for name, file_name, fmt, _ in datasets
    ]
