import anywidget  # type: ignore
import traitlets
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List, Union

import altair as alt
from altair.utils._vegafusion_data import using_vegafusion
from altair.vegalite.v5.schema.core import TopLevelSpec

_here = pathlib.Path(__file__).parent


@dataclass(frozen=True, eq=True)
class Param:
    name: str
    value: Any


@dataclass(frozen=True, eq=True)
class IndexSelectionParam:
    name: str
    value: List[int]
    _store: List[Dict[str, Any]]


@dataclass(frozen=True, eq=True)
class PointSelectionParam:
    name: str
    value: List[Dict[str, Any]]
    _store: List[Dict[str, Any]]


@dataclass(frozen=True, eq=True)
class IntervalSelectionParam:
    name: str
    value: Dict[str, list]
    _store: List[Dict[str, Any]]


class ChartWidget(anywidget.AnyWidget):
    _esm = _here / "static" / "index.js"
    _css = r"""
    .vega-embed {
        /* Make sure action menu isn't cut off */
        overflow: visible;
    }
    """

    # Public traitlets
    chart = traitlets.Instance(TopLevelSpec)
    spec = traitlets.Dict().tag(sync=True)
    selections = traitlets.Dict()
    params = traitlets.Dict()
    debounce_wait = traitlets.Float(default_value=10).tag(sync=True)

    # Internal selection traitlets
    _selection_types = traitlets.Dict()
    _selection_watches = traitlets.List().tag(sync=True)
    _selections = traitlets.Dict().tag(sync=True)

    # Internal param traitlets
    _param_watches = traitlets.List().tag(sync=True)
    _params = traitlets.Dict().tag(sync=True)

    def __init__(self, chart, debounce_wait=10, **kwargs: Any):
        super().__init__(chart=chart, debounce_wait=debounce_wait, **kwargs)

    def set_params(self, *args: Param):
        updates = []
        for param in args:
            if param.name not in self.params:
                raise ValueError(f"No param named {param.name}")
            clean_value = param.value if param.value != alt.Undefined else None
            updates.append({
                "name": param.name,
                "value": clean_value,
            })

        # Update params directly so that they are set immediately
        # after this function returns
        new_params = dict(self._params)
        for param in args:
            clean_value = param.value if param.value != alt.Undefined else None
            new_params[param.name] = {"value": clean_value}
        self._params = new_params

        self.send({
            "type": "setParams",
            "updates": updates
        })

    @traitlets.observe("chart")
    def _on_change_chart(self, change):
        new_chart = change.new

        params = getattr(new_chart, "params", [])
        selection_watches = []
        selection_types = {}
        param_watches = []
        initial_params = dict()
        initial_selections = dict()

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
                    initial_selections[param.name] = {"value": None, "store": []}
                else:
                    param_watches.append(param.name)
                    clean_value = param.value if param.value != alt.Undefined else None
                    initial_params[param.name] = {"value": clean_value}

        # Update properties all together
        with self.hold_sync():
            if using_vegafusion():
                self.spec = new_chart.to_dict(format="vega")
            else:
                self.spec = new_chart.to_dict()
            self._selection_types = selection_types
            self._selection_watches = selection_watches
            self._selections = initial_selections

            self._param_watches = param_watches
            self._params = initial_params

    @traitlets.observe("_selections")
    def _on_change_selections(self, change):
        new_selections = {}
        for selection_name, selection_dict in change.new.items():
            value = selection_dict["value"]
            store = selection_dict["store"]
            selection_type = self._selection_types[selection_name]
            if selection_type == "index":
                if value is None:
                    indices = []
                else:
                    points = value.get("vlPoint", {}).get("or", [])
                    indices = [p["_vgsid_"] - 1 for p in points]
                new_selections[selection_name] = IndexSelectionParam(
                    name=selection_name, value=indices, _store=store
                )
            elif selection_type == "point":
                if value is None:
                    points = []
                else:
                    points = value.get("vlPoint", {}).get("or", [])
                new_selections[selection_name] = PointSelectionParam(
                    name=selection_name, value=points, _store=store
                )
            elif selection_type == "interval":
                if value is None:
                    value = {}
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
