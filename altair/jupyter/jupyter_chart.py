import anywidget
import traitlets
import pathlib
from typing import Any, Set

import altair as alt
from altair.utils._vegafusion_data import using_vegafusion
from altair import TopLevelSpec
from altair.utils.selection import IndexSelection, PointSelection, IntervalSelection

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
                traitlet_type = traitlets.Any()

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
        if change["name"] in self.traits() and change["old"] != change["new"]:
            self._set_value(change["name"], change["old"])
        raise ValueError(
            "Selections may not be set from Python.\n"
            f"Attempted to set select: {change['name']}"
        )

    def _set_value(self, key, value):
        self.unobserve(self._make_read_only, names=key)
        setattr(self, key, value)
        self.observe(self._make_read_only, names=key)


class JupyterChart(anywidget.AnyWidget):
    _esm = (_here / "js" / "index.js").read_text()
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
                if isinstance(param.name, alt.ParameterName):
                    clean_name = param.name.to_json().strip('"')
                else:
                    clean_name = param.name

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
                            selection_types[clean_name] = "index"
                            empty_selections[clean_name] = IndexSelection(
                                name=clean_name, value=[], store=[]
                            )
                        else:
                            selection_types[clean_name] = "point"
                            empty_selections[clean_name] = PointSelection(
                                name=clean_name, value=[], store=[]
                            )
                    elif select_type == "interval":
                        selection_types[clean_name] = "interval"
                        empty_selections[clean_name] = IntervalSelection(
                            name=clean_name, value={}, store=[]
                        )
                    else:
                        raise ValueError(f"Unexpected selection type {select.type}")
                    selection_watches.append(clean_name)
                    initial_vl_selections[clean_name] = {"value": None, "store": []}
                else:
                    clean_value = param.value if param.value != alt.Undefined else None
                    initial_params[clean_name] = clean_value

        # Handle the params generated by transforms
        for param_name in collect_transform_params(new_chart):
            initial_params[param_name] = None

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
                self.selections._set_value(
                    selection_name,
                    IndexSelection.from_vega(selection_name, signal=value, store=store),
                )
            elif selection_type == "point":
                self.selections._set_value(
                    selection_name,
                    PointSelection.from_vega(selection_name, signal=value, store=store),
                )
            elif selection_type == "interval":
                self.selections._set_value(
                    selection_name,
                    IntervalSelection.from_vega(
                        selection_name, signal=value, store=store
                    ),
                )


def collect_transform_params(chart: TopLevelSpec) -> Set[str]:
    """
    Collect the names of params that are defined by transforms

    Parameters
    ----------
    chart: Chart from which to extract transform params

    Returns
    -------
    set of param names
    """
    transform_params = set()

    # Handle recursive case
    for prop in ("layer", "concat", "hconcat", "vconcat"):
        for child in getattr(chart, prop, []):
            transform_params.update(collect_transform_params(child))

    # Handle chart's own transforms
    transforms = getattr(chart, "transform", [])
    transforms = transforms if transforms != alt.Undefined else []
    for tx in transforms:
        if hasattr(tx, "param"):
            transform_params.add(tx.param)

    return transform_params
