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
class SelectionParam:
    name: str
    value: Union[List[int], Dict[str, list]]
    _store: List[Dict[str, Any]]

    @classmethod
    def from_vega(cls, name: str, value: dict, store: List[Dict[str, Any]]):
        points = value.get("vlPoint", {}).get("or", None)
        if points is not None:
            # Transpose values e.g.
            #  from [{"a": 1, "b": "A"}, {"a": 2, "b": "B"}]
            #    to  {"a": [1, 2], "b": ["A", "B"]}
            selection_value: Union[dict, list] = {}
            for point in points:
                for k, v in point.items():
                    value.setdefault(k, []).append(v)

            # _vgsid_ is one-based. subtract 1 to be zero-indexed
            if list(value.keys()) == ["_vgsid_"]:
                selection_value = [i - 1 for i in value["_vgsid_"]]
        else:
            selection_value = value

        return SelectionParam(name=name, value=selection_value, _store=store)


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

    _selection_watches = traitlets.List().tag(sync=True)
    _selections = traitlets.Dict().tag(sync=True)

    _param_watches = traitlets.List().tag(sync=True)
    _params = traitlets.Dict().tag(sync=True)

    @traitlets.observe("chart")
    def _on_change_chart(self, change):
        new_chart = change.new

        params = getattr(new_chart, "params", [])
        selection_watches = []
        param_watches = []
        if params is not alt.Undefined:
            for param in new_chart.params:
                select = getattr(param, "select", alt.Undefined)
                if select != alt.Undefined:
                    selection_watches.append(param.name)
                else:
                    param_watches.append(param.name)

        # Update properties all together
        with self.hold_sync():
            if using_vegafusion():
                self.spec = new_chart.to_dict(format="vega")
            else:
                self.spec = new_chart.to_dict()
            self._selection_watches = selection_watches
            self._param_watches = param_watches

    @traitlets.observe("_selections")
    def _on_change_selections(self, change):
        new_selections = {}
        for selection_name, selection_dict in change.new.items():
            new_selections[selection_name] = SelectionParam.from_vega(
                name=selection_name, **selection_dict
            )
        self.selections = new_selections

    @traitlets.observe("_params")
    def _on_change_params(self, change):
        new_params = {}
        for param_name, param_dict in change.new.items():
            new_params[param_name] = Param(name=param_name, **param_dict)
        self.params = new_params
