import json
import pytest

try:
    from IPython import InteractiveShell

    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False
    pass

from altair.vegalite.v5 import VegaLite


DATA_RECORDS = [
    {"amount": 28, "category": "A"},
    {"amount": 55, "category": "B"},
    {"amount": 43, "category": "C"},
    {"amount": 91, "category": "D"},
    {"amount": 81, "category": "E"},
    {"amount": 53, "category": "F"},
    {"amount": 19, "category": "G"},
    {"amount": 87, "category": "H"},
]

if IPYTHON_AVAILABLE:
    _ipshell = InteractiveShell.instance()
    _ipshell.run_cell("%load_ext altair")
    _ipshell.run_cell(
        """
import pandas as pd
table = pd.DataFrame.from_records({})
the_data = table
""".format(
            DATA_RECORDS
        )
    )


VEGALITE_SPEC = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"values": DATA_RECORDS},
    "description": "A simple bar chart with embedded data.",
    "encoding": {
        "x": {"field": "category", "type": "ordinal"},
        "y": {"field": "amount", "type": "quantitative"},
    },
    "mark": {"type": "bar"},
}


@pytest.mark.skipif(not IPYTHON_AVAILABLE, reason="requires ipython")
def test_vegalite_magic_data_included():
    result = _ipshell.run_cell("%%vegalite\n" + json.dumps(VEGALITE_SPEC))
    assert isinstance(result.result, VegaLite)
    assert VEGALITE_SPEC == result.result.spec


@pytest.mark.skipif(not IPYTHON_AVAILABLE, reason="requires ipython")
def test_vegalite_magic_json_flag():
    result = _ipshell.run_cell("%%vegalite --json\n" + json.dumps(VEGALITE_SPEC))
    assert isinstance(result.result, VegaLite)
    assert VEGALITE_SPEC == result.result.spec


@pytest.mark.skipif(not IPYTHON_AVAILABLE, reason="requires ipython")
def test_vegalite_magic_pandas_data():
    spec = {key: val for key, val in VEGALITE_SPEC.items() if key != "data"}
    result = _ipshell.run_cell("%%vegalite table\n" + json.dumps(spec))
    assert isinstance(result.result, VegaLite)
    assert VEGALITE_SPEC == result.result.spec
