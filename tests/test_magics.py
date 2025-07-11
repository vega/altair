from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

from altair.vegalite.v6.display import VegaLite
from tests import skip_requires_ipython

if TYPE_CHECKING:
    from IPython.core.interactiveshell import InteractiveShell


@pytest.fixture
def records() -> list[dict[str, Any]]:
    return [
        {"amount": 28, "category": "A"},
        {"amount": 55, "category": "B"},
        {"amount": 43, "category": "C"},
        {"amount": 91, "category": "D"},
        {"amount": 81, "category": "E"},
        {"amount": 53, "category": "F"},
        {"amount": 19, "category": "G"},
        {"amount": 87, "category": "H"},
    ]


@pytest.fixture
def vl_spec(records) -> dict[str, Any]:
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
        "data": {"values": records},
        "description": "A simple bar chart with embedded data.",
        "encoding": {
            "x": {"field": "category", "type": "ordinal"},
            "y": {"field": "amount", "type": "quantitative"},
        },
        "mark": {"type": "bar"},
    }


@pytest.fixture
def ipshell(records) -> InteractiveShell:
    from IPython.core.interactiveshell import InteractiveShell

    shell = InteractiveShell.instance()
    shell.run_cell("%load_ext altair")
    shell.run_cell(
        f"import pandas as pd\n"
        f"table = pd.DataFrame.from_records({records})\n"
        f"the_data = table"
    )
    return shell


@skip_requires_ipython
def test_vegalite_magic_data_included(ipshell, vl_spec) -> None:
    result = ipshell.run_cell("%%vegalite\n" + json.dumps(vl_spec))
    assert isinstance(result.result, VegaLite)
    assert result.result.spec == vl_spec


@skip_requires_ipython
def test_vegalite_magic_json_flag(ipshell, vl_spec) -> None:
    result = ipshell.run_cell("%%vegalite --json\n" + json.dumps(vl_spec))
    assert isinstance(result.result, VegaLite)
    assert result.result.spec == vl_spec


@skip_requires_ipython
def test_vegalite_magic_pandas_data(ipshell, vl_spec) -> None:
    spec = {key: val for key, val in vl_spec.items() if key != "data"}
    result = ipshell.run_cell("%%vegalite table\n" + json.dumps(spec))
    assert isinstance(result.result, VegaLite)
    assert result.result.spec == vl_spec
