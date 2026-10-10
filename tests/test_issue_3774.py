"""
Regression tests for https://github.com/vega/altair/issues/3774.

A layer defined on an empty ``alt.Chart()`` carries no data of its own, so in a
layered chart it inherits every row of the parent dataset and its mark is drawn
once per row (e.g. a rule and its label rendered 15 times on top of each other).
Marks that should be drawn once per chart must be bound to a single-row dataset.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from altair.utils.execeval import eval_block

EXAMPLES = [
    Path(__file__).parent
    / "examples_arguments_syntax"
    / "bar_chart_with_single_threshold.py",
    Path(__file__).parent
    / "examples_methods_syntax"
    / "bar_chart_with_single_threshold.py",
]


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda path: path.parent.name)
def test_rule_and_text_layers_have_own_data(example: Path) -> None:
    chart = eval_block(example.read_text())
    spec = chart.to_dict()
    for layer in spec["layer"]:
        mark = layer.get("mark", {})
        mark_type = mark["type"] if isinstance(mark, dict) else mark
        if mark_type in {"rule", "text"}:
            assert "data" in layer, (
                f"{example.parent.name}/{example.name}: the {mark_type!r} layer has no "
                "data of its own, so it inherits every row of the parent chart and is "
                "drawn once per row. Bind it to a single-row dataset instead "
                "(vega/altair#3774)."
            )
