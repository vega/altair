"""The gallery threshold annotation should render once, not once per bar."""

import runpy
import xml.etree.ElementTree as et
from pathlib import Path

import pytest


@pytest.mark.parametrize("syntax", ["arguments", "methods"])
def test_threshold_gallery_draws_one_rule_and_label(syntax):
    vl_convert = pytest.importorskip("vl_convert")
    example = (
        Path(__file__).resolve().parents[2]
        / f"examples_{syntax}_syntax"
        / "bar_chart_with_single_threshold.py"
    )
    namespace = runpy.run_path(str(example))
    chart = (
        namespace["bars"]
        + namespace["highlight"]
        + namespace["rule"]
        + namespace["label"]
    )
    root = et.fromstring(vl_convert.vegalite_to_svg(chart.to_dict()))
    counts = {}
    for group in root.iter():
        classes = group.get("class", "").split()
        if "role-mark" in classes:
            for mark in ["rule", "text"]:
                if f"mark-{mark}" in classes:
                    counts[mark] = counts.get(mark, 0) + len(group)
    assert counts == {"rule": 1, "text": 1}
    assert sum(element.text == "hazardous" for element in root.iter()) == 1
