from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tools import versioning

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def versions(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> versioning._Versions:
    monkeypatch.setattr(versioning, "_REPO_ROOT", tmp_path)
    result = object.__new__(versioning._Versions)
    result._mapping = {
        "vega-datasets": "v3.3.1",
        "vega-embed": "v7.0.2",
        "vega-lite": "v6.4.1",
        "vegafusion": "2.0.3",
        "vl-convert-python": "1.9.0",
    }
    return result


def test_update_display(versions: versioning._Versions, tmp_path: Path) -> None:
    fp = tmp_path / "altair/vegalite/v6/display.py"
    fp.parent.mkdir(parents=True)
    fp.write_text(
        """\
VEGA_VERSION: Final = "5"
VEGAEMBED_VERSION: Final = "6"
VEGALITE_MIME_TYPE: Final = "application/vnd.vegalite.v5.json"
VEGA_MIME_TYPE: Final = "application/vnd.vega.v5.json"
""",
        "utf-8",
    )

    versions.update_display()

    assert fp.read_text("utf-8").splitlines() == [
        'VEGA_VERSION: Final = "6"',
        'VEGAEMBED_VERSION: Final = "7"',
        'VEGALITE_MIME_TYPE: Final = "application/vnd.vegalite.v6.json"',
        'VEGA_MIME_TYPE: Final = "application/vnd.vega.v6.json"',
    ]


def test_update_cdn_references(versions: versioning._Versions, tmp_path: Path) -> None:
    paths = (
        tmp_path / "doc/_static/chart.html",
        tmp_path / "doc/user_guide/saving_charts.rst",
        tmp_path / "tests/vegalite/v6/test_api.py",
    )
    source = """\
https://cdn.jsdelivr.net/npm/vega@5
https://cdn.jsdelivr.net/npm/vega-lite@5.2.0
https://cdn.jsdelivr.net/npm/vega-embed@6"""
    for fp in paths:
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(source, "utf-8")

    versions.update_cdn_references()

    expected = """\
https://cdn.jsdelivr.net/npm/vega@6
https://cdn.jsdelivr.net/npm/vega-lite@6
https://cdn.jsdelivr.net/npm/vega-embed@7"""
    for fp in paths:
        assert fp.read_text("utf-8") == expected


def test_update_cdn_references_checks_expected_count(
    versions: versioning._Versions, tmp_path: Path
) -> None:
    fp = tmp_path / "doc/_static/chart.html"
    fp.parent.mkdir(parents=True)
    fp.write_text("https://cdn.jsdelivr.net/npm/vega@5", "utf-8")

    with pytest.raises(ValueError, match="Expected 3 Vega CDN references"):
        versions.update_cdn_references()
