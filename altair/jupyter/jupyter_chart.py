import anywidget
import traitlets
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List

import altair as alt
from altair.utils._vegafusion_data import using_vegafusion
from altair.vegalite.v5.schema.core import TopLevelSpec

_here = pathlib.Path(__file__).parent


class Params(traitlets.HasTraits):
    """
    Traitlet class storing a JupyterChart's params
    """
    def __init__(self, trait_values):
        super().__init__()

        for key, value in trait_values.items():
            if isinstance(value, int):
                traitlet_type = traitlets.Int()
            elif isinstance(value, float):
                traitlet_type = traitlets.Float()
            elif isinstance(value, str):
                traitlet_type = traitlets.Unicode()
            elif isinstance(value, list):
                traitlet_type = traitlets.List()
            elif isinstance(value, dict):
                traitlet_type = traitlets.Dict()
            else:
                raise ValueError(f"Unexpected param type: {type(value)}")

            # Add the new trait.
            self.add_traits(**{key: traitlet_type})

            # Set the trait's value.
            setattr(self, key, value)

    def __repr__(self):
        return f"Params({self.trait_values()})"


class Selections(traitlets.HasTraits):
    """
    Traitlet class storing a JupyterChart's selections
    """
    def __init__(self, trait_values):
        super().__init__()

        for key, value in trait_values.items():
            if isinstance(value, IndexSelection):
                traitlet_type = traitlets.Instance(IndexSelection)
            elif isinstance(value, PointSelection):
                traitlet_type = traitlets.Instance(PointSelection)
            elif isinstance(value, IntervalSelection):
                traitlet_type = traitlets.Instance(IntervalSelection)
            else:
                raise ValueError(f"Unexpected selection type: {type(value)}")

            # Add the new trait.
            self.add_traits(**{key: traitlet_type})

            # Set the trait's value.
            setattr(self, key, value)

            # Make read-only
            self.observe(self._make_read_only, names=key)

    def __repr__(self):
        return f"Selections({self.trait_values()})"

    def _make_read_only(self, change):
        """
        Work around to make traits read-only, but still allow us to change
        them internally
        """
        if change['name'] in self.traits() and change['old'] != change['new']:
            self._set_value(change['name'], change['old'])
        raise ValueError(
            "Selections may not be set from Python.\n"
            f"Attempted to set select: {change['name']}"
        )

    def _set_value(self, key, value):
        self.unobserve(self._make_read_only, names=key)
        setattr(self, key, value)
        self.observe(self._make_read_only, names=key)


@dataclass(frozen=True, eq=True)
class IndexSelection:
    """
    An IndexSelection represents the state of an Altair
    point selection (as constructed by alt.selection_point())
    when neither the fields nor encodings arguments are specified.

    The value field is a list of zero-based indices into the
    selected dataset.

    Note: These indices only apply to the input DataFrame
    for charts that do not include aggregations (e.g. a scatter chart).
    """

    name: str
    value: List[int]
    store: List[Dict[str, Any]]


@dataclass(frozen=True, eq=True)
class PointSelection:
    """
    A PointSelection represents the state of an Altair
    point selection (as constructed by alt.selection_point())
    when the fields or encodings arguments are specified.

    The value field is a list of dicts of the form:
        [{"dim1": 1, "dim2": "A"}, {"dim1": 2, "dim2": "BB"}]

    where "dim1" and "dim2" are dataset columns and the dict values
    correspond to the specific selected values.
    """

    name: str
    value: List[Dict[str, Any]]
    store: List[Dict[str, Any]]


@dataclass(frozen=True, eq=True)
class IntervalSelection:
    """
    An IntervalSelection represents the state of an Altair
    interval selection (as constructed by alt.selection_interval()).

    The value field is a dict of the form:
        {"dim1": [0, 10], "dim2": ["A", "BB", "CCC"]}

    where "dim1" and "dim2" are dataset columns and the dict values
    correspond to the selected range.
    """

    name: str
    value: Dict[str, list]
    store: List[Dict[str, Any]]


class JupyterChart(anywidget.AnyWidget):
    _esm = _here / "js" / "index.js"
    _css = r"""
    .vega-embed {
        /* Make sure action menu isn't cut off */
        overflow: visible;
    }
    """

    # Public traitlets
    chart = traitlets.Instance(TopLevelSpec)
    spec = traitlets.Dict().tag(sync=True)
    debounce_wait = traitlets.Float(default_value=10).tag(sync=True)

    # Internal selection traitlets
    _selection_types = traitlets.Dict()
    _vl_selections = traitlets.Dict().tag(sync=True)

    # Internal param traitlets
    _params = traitlets.Dict().tag(sync=True)

    def __init__(self, chart: TopLevelSpec, debounce_wait: int = 10, **kwargs: Any):
        """
        Jupyter Widget for displaying and updating Altair Charts, and
        retrieving selection and parameter values

        Parameters
        ----------
        chart: Chart
            Altair Chart instance
        debounce_wait: int
             Debouncing wait time in milliseconds
        """
        self.params = Params({})
        self.selections = Selections({})
        super().__init__(chart=chart, debounce_wait=debounce_wait, **kwargs)

    @traitlets.observe("chart")
    def _on_change_chart(self, change):
        """
        Internal callback function that updates the JupyterChart's internal
        state when the wrapped Chart instance changes
        """
        new_chart = change.new

        params = getattr(new_chart, "params", [])
        selection_watches = []
        selection_types = {}
        initial_params = {}
        initial_vl_selections = {}
        empty_selections = {}

        if params is not alt.Undefined:
            for param in new_chart.params:
                select = getattr(param, "select", alt.Undefined)

                if select != alt.Undefined:
                    if not isinstance(select, dict):
                        select = select.to_dict()

                    select_type = select["type"]
                    if select_type == "point":
                        if not (
                            select.get("fields", None) or select.get("encodings", None)
                        ):
                            # Point selection with no associated fields or encodings specified.
                            # This is an index-based selection
                            selection_types[param.name] = "index"
                            empty_selections[param.name] = IndexSelection(name=param.name, value=[], store=[])
                        else:
                            selection_types[param.name] = "point"
                            empty_selections[param.name] = PointSelection(name=param.name, value=[], store=[])
                    elif select_type == "interval":
                        selection_types[param.name] = "interval"
                        empty_selections[param.name] = IntervalSelection(name=param.name, value={}, store=[])
                    else:
                        raise ValueError(f"Unexpected selection type {select.type}")
                    selection_watches.append(param.name)
                    initial_vl_selections[param.name] = {"value": None, "store": []}
                else:
                    clean_value = param.value if param.value != alt.Undefined else None
                    initial_params[param.name] = clean_value

        # Setup params
        self.params = Params(initial_params)

        def on_param_traitlet_changed(param_change):
            new_params = dict(self._params)
            new_params[param_change["name"]] = param_change["new"]
            self._params = new_params

        self.params.observe(on_param_traitlet_changed)

        # Setup selections
        self.selections = Selections(empty_selections)

        # Update properties all together
        with self.hold_sync():
            if using_vegafusion():
                self.spec = new_chart.to_dict(format="vega")
            else:
                self.spec = new_chart.to_dict()
            self._selection_types = selection_types
            self._vl_selections = initial_vl_selections
            self._params = initial_params

    @traitlets.observe("_params")
    def _on_change_params(self, change):
        for param_name, value in change.new.items():
            setattr(self.params, param_name, value)

    @traitlets.observe("_vl_selections")
    def _on_change_selections(self, change):
        """
        Internal callback function that updates the JupyterChart's public
        selections traitlet in response to changes that the JavaScript logic
        makes to the internal _selections traitlet.
        """
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

                self.selections._set_value(selection_name, IndexSelection(
                    name=selection_name, value=indices, store=store
                ))
            elif selection_type == "point":
                if value is None:
                    points = []
                else:
                    points = value.get("vlPoint", {}).get("or", [])

                self.selections._set_value(selection_name, PointSelection(
                    name=selection_name, value=points, store=store
                ))
            elif selection_type == "interval":
                if value is None:
                    value = {}

                self.selections._set_value(selection_name, IntervalSelection(
                    name=selection_name, value=value, store=store
                ))
