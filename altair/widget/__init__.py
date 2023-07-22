import anywidget  # type: ignore
import traitlets
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Union

import altair as alt
from altair.utils._vegafusion_data import using_vegafusion
from altair.vegalite.v5.schema.core import TopLevelSpec

_here = pathlib.Path(__file__).parent


@dataclass
class Param:
    name: str
    value: Any


@dataclass
class IndexSelectionParam:
    name: str
    value: List[int]
    _store: List[Dict[str, Any]]


@dataclass
class PointSelectionParam:
    name: str
    value: List[Dict[str, Any]]
    _store: List[Dict[str, Any]]


@dataclass
class IntervalSelectionParam:
    name: str
    value: Dict[str, list]
    _store: List[Dict[str, Any]]


class ChartWidget(anywidget.AnyWidget):
    _esm = _here / "static" / "index.js"
    _css = r"""
    .vega-embed {
        overflow: visible;
    }
    """

    chart = traitlets.Instance(TopLevelSpec)
    spec = traitlets.Dict().tag(sync=True)
    selections = traitlets.Dict()
    params = traitlets.Dict()

    _selection_types = traitlets.Dict()
    _selection_watches = traitlets.List().tag(sync=True)
    _selections = traitlets.Dict().tag(sync=True)

    _param_watches = traitlets.List().tag(sync=True)
    _params = traitlets.Dict().tag(sync=True)

    @traitlets.observe("chart")
    def _on_change_chart(self, change):
        new_chart = change.new

        params = getattr(new_chart, "params", [])
        selection_watches = []
        selection_types = {}
        param_watches = []
        if params is not alt.Undefined:
            for param in new_chart.params:
                select = getattr(param, "select", alt.Undefined)

                if select != alt.Undefined:
                    if not isinstance(select, dict):
                        select = select.to_dict()

                    select_type = select["type"]
                    if select_type == "point":
                        if not select.get("fields", None) and not select.get("encodings", None):
                            # Point selection with no associated fields or encodings specified.
                            # This is an index-based selection
                            selection_types[param.name] = "index"
                        else:
                            selection_types[param.name] = "point"
                    elif select_type == "interval":
                        selection_types[param.name] = "interval"
                    else:
                        raise ValueError(f"Unexpected selection type {select.type}")
                    selection_watches.append(param.name)
                else:
                    param_watches.append(param.name)

        # Update properties all together
        with self.hold_sync():
            if using_vegafusion():
                self.spec = new_chart.to_dict(format="vega")
            else:
                self.spec = new_chart.to_dict()
            self._selection_types = selection_types
            self._selection_watches = selection_watches
            self._param_watches = param_watches

    @traitlets.observe("_selections")
    def _on_change_selections(self, change):
        new_selections = {}
        for selection_name, selection_dict in change.new.items():
            value = selection_dict["value"]
            store = selection_dict["store"]
            selection_type = self._selection_types[selection_name]
            if selection_type == "index":
                points = value.get("vlPoint", {}).get("or", [])
                indices = [p["_vgsid_"] - 1 for p in points]
                new_selections[selection_name] = IndexSelectionParam(
                    name=selection_name, value=indices, _store=store
                )
            elif selection_type == "point":
                points = value.get("vlPoint", {}).get("or", [])
                new_selections[selection_name] = PointSelectionParam(
                    name=selection_name, value=points, _store=store
                )
            elif selection_type == "interval":
                new_selections[selection_name] = IntervalSelectionParam(
                    name=selection_name, value=value, _store=store
                )

        self.selections = new_selections

    @traitlets.observe("_params")
    def _on_change_params(self, change):
        new_params = {}
        for param_name, param_dict in change.new.items():
            new_params[param_name] = Param(name=param_name, **param_dict)
        self.params = new_params
