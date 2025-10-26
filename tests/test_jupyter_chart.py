from importlib.metadata import version as importlib_version

import pandas as pd
import pytest
from packaging.version import Version

import altair as alt
from altair.datasets import data

# If anywidget is not installed, we will skip the tests in this file.
try:
    import anywidget  # noqa: F401

    has_anywidget = True
except ImportError:
    has_anywidget = False

if has_anywidget:
    from altair.jupyter import jupyter_chart
else:
    jupyter_chart = None  # type: ignore

skip_requires_anywidget = pytest.mark.skipif(
    not has_anywidget, reason="anywidget not importable"
)


try:
    import vegafusion  # noqa: F401

    transformers = ["default", "vegafusion"]
except ImportError:
    transformers = ["default"]

param_transformers = pytest.mark.parametrize("transformer", transformers)


if Version(importlib_version("ipywidgets")) < Version("8.1.4"):
    # See https://github.com/vega/altair/issues/3234#issuecomment-2268515312
    _filterwarn = pytest.mark.filterwarnings(
        "ignore:Deprecated in traitlets 4.1.*:DeprecationWarning"
    )
    jupyter_marks: pytest.MarkDecorator = skip_requires_anywidget(
        _filterwarn(param_transformers)
    )
else:
    jupyter_marks = skip_requires_anywidget(param_transformers)


@jupyter_marks
def test_chart_with_no_interactivity(transformer):
    with alt.data_transformers.enable(transformer):
        source = pd.DataFrame(
            {
                "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
            }
        )

        chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
        widget = alt.JupyterChart(chart)

        if transformer == "vegafusion":
            # With the "vegafusion" transformer, the spec is not computed until the front-end
            # sets the local_tz. Assign this property manually to simulate this.
            widget.local_tz = "UTC"
            assert widget.spec == chart.to_dict(format="vega")
        else:
            assert widget.spec == chart.to_dict()

        # There should be no params or selections initialized
        assert len(widget.selections.trait_values()) == 0
        assert len(widget.params.trait_values()) == 0


@jupyter_marks
def test_interval_selection_example(transformer):
    with alt.data_transformers.enable(transformer):
        source = data.cars()
        brush = alt.selection_interval(name="interval")

        chart = (
            alt.Chart(source)
            .mark_point()
            .encode(
                x="Horsepower:Q",
                y="Miles_per_Gallon:Q",
                color=alt.condition(brush, "Cylinders:O", alt.value("grey")),
            )
            .add_params(brush)
        )

        widget = alt.JupyterChart(chart)

        if transformer == "vegafusion":
            widget.local_tz = "UTC"
            assert widget.spec == chart.to_dict(format="vega")
        else:
            assert widget.spec == chart.to_dict()

        # There should be one selection and zero params
        assert len(widget.selections.trait_values()) == 1
        assert len(widget.params.trait_values()) == 0

        # Check initial interval selection
        selection = widget.selections.interval
        assert isinstance(selection, jupyter_chart.IntervalSelection)
        assert selection.value == {}
        assert selection.store == []

        # Simulate Vega signal update
        store = [
            {
                "unit": "",
                "fields": [
                    {"field": "Horsepower", "channel": "x", "type": "R"},
                    {"field": "Miles_per_Gallon", "channel": "y", "type": "R"},
                ],
                "values": [
                    [40.0, 100],
                    [25, 30],
                ],
            }
        ]
        widget._vl_selections = {
            "interval": {
                "value": {
                    "Horsepower": [40.0, 100],
                    "Miles_per_Gallon": [25, 30],
                },
                "store": store,
            }
        }

        selection = widget.selections.interval
        assert isinstance(selection, jupyter_chart.IntervalSelection)
        assert selection.value == {
            "Horsepower": [40.0, 100],
            "Miles_per_Gallon": [25, 30],
        }
        assert selection.store == store


@jupyter_marks
def test_index_selection_example(transformer):
    with alt.data_transformers.enable(transformer):
        source = data.cars()
        brush = alt.selection_point(name="index")

        chart = (
            alt.Chart(source)
            .mark_point()
            .encode(
                x="Horsepower:Q",
                y="Miles_per_Gallon:Q",
                color=alt.condition(brush, "Cylinders:O", alt.value("grey")),
            )
            .add_params(brush)
        )

        widget = alt.JupyterChart(chart)

        if transformer == "vegafusion":
            widget.local_tz = "UTC"
            assert widget.spec == chart.to_dict(format="vega")
        else:
            assert widget.spec == chart.to_dict()

        # There should be one selection and zero params
        assert len(widget.selections.trait_values()) == 1
        assert len(widget.params.trait_values()) == 0

        # Check initial interval selection
        selection = widget.selections.index
        assert isinstance(selection, jupyter_chart.IndexSelection)
        assert selection.value == []
        assert selection.store == []

        # Simulate Vega signal update
        store = [
            {"unit": "", "_vgsid_": 220},
            {"unit": "", "_vgsid_": 330},
            {"unit": "", "_vgsid_": 341},
        ]

        widget._vl_selections = {
            "index": {
                "value": {
                    "_vgsid_": "Set(220,330,341)",
                    "vlPoint": {
                        "or": [{"_vgsid_": 220}, {"_vgsid_": 330}, {"_vgsid_": 341}]
                    },
                },
                "store": store,
            }
        }

        selection = widget.selections.index
        assert isinstance(selection, jupyter_chart.IndexSelection)
        assert selection.value == [219, 329, 340]
        assert selection.store == store


@jupyter_marks
def test_point_selection(transformer):
    with alt.data_transformers.enable(transformer):
        source = data.cars()
        brush = alt.selection_point(name="point", encodings=["color"], bind="legend")

        chart = (
            alt.Chart(source)
            .mark_point()
            .encode(
                x="Horsepower:Q",
                y="Miles_per_Gallon:Q",
                color=alt.condition(brush, "Cylinders:O", alt.value("grey")),
            )
            .add_params(brush)
        )

        widget = alt.JupyterChart(chart)

        if transformer == "vegafusion":
            widget.local_tz = "UTC"
            assert widget.spec == chart.to_dict(format="vega")
        else:
            assert widget.spec == chart.to_dict()

        # There should be one selection and zero params
        assert len(widget.selections.trait_values()) == 1
        assert len(widget.params.trait_values()) == 0

        # Check initial interval selection
        selection = widget.selections.point
        assert isinstance(selection, jupyter_chart.PointSelection)
        assert selection.value == []
        assert selection.store == []

        # Simulate Vega signal update
        store = [
            {
                "fields": [{"field": "Cylinders", "channel": "color", "type": "E"}],
                "values": [4],
            },
            {
                "fields": [{"field": "Cylinders", "channel": "color", "type": "E"}],
                "values": [5],
            },
        ]

        widget._vl_selections = {
            "point": {
                "value": {
                    "Cylinders": [4, 5],
                    "vlPoint": {"or": [{"Cylinders": 4}, {"Cylinders": 5}]},
                },
                "store": store,
            }
        }

        selection = widget.selections.point
        assert isinstance(selection, jupyter_chart.PointSelection)
        assert selection.value == [{"Cylinders": 4}, {"Cylinders": 5}]
        assert selection.store == store


@jupyter_marks
def test_param_updates(transformer):
    with alt.data_transformers.enable(transformer):
        source = data.cars()
        size_param = alt.param(
            name="size", value=10, bind=alt.binding_range(min=1, max=100)
        )
        chart = (
            alt.Chart(source)
            .mark_point()
            .encode(x="Horsepower:Q", y="Miles_per_Gallon:Q", size=size_param)
            .add_params(size_param)
        )

        widget = alt.JupyterChart(chart)

        # There should be one param and zero selections
        assert len(widget.selections.trait_values()) == 0
        assert len(widget.params.trait_values()) == 1

        # Initial value should match what was provided
        assert widget.params.size == 10

        # Update param from python
        widget.params.size = 50
        assert widget.params.size == 50
