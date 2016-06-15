"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""
import warnings

import traitlets as T
import pandas as pd

from .utils import visitors
from .utils._py3k_compat import string_types

from . import schema

from .schema import AggregateOp
from .schema import AxisConfig
from .schema import AxisOrient
from .schema import Axis
from .schema import Bin
from .schema import CellConfig
from .schema import Config
from .schema import Data
from .schema import DataFormat
from .schema import FacetConfig
from .schema import FacetGridConfig
from .schema import FacetScaleConfig
from .schema import FontStyle
from .schema import FontWeight
from .schema import Formula
from .schema import HorizontalAlign
from .schema import LegendConfig
from .schema import Legend
from .schema import MarkConfig
from .schema import NiceTime
from .schema import Scale
from .schema import ScaleConfig
from .schema import SortField
from .schema import SortOrder
from .schema import StackOffset
from .schema import TimeUnit
from .schema import Transform
from .schema import UnitSpec
from .schema import UnitEncoding
from .schema import VerticalAlign

#*************************************************************************
# Channel Aliases
#*************************************************************************
from .schema import X, Y, Row, Column, Color, Size, Shape, Text, Label, Detail, Opacity, Order, Path
from .schema import Encoding, Facet

#*************************************************************************
# Loading the spec
#*************************************************************************
def load_vegalite_spec(spec):
    """Load a Vega-Lite spec and return an Altair object.

    The spec should be in the form of a Python dictionary.
    """
    if 'layers' in spec:
        return LayeredChart.from_dict(spec)
    elif 'facet' in spec:
        return FacetedChart.from_dict(spec)
    else:
        return Chart.from_dict(spec)


#*************************************************************************
# Top-level Objects
#*************************************************************************
class TopLevelMixin(object):
    def _to_code(self, data=None):
        """Emit the CodeGen object used to export this chart to Python code."""
        return visitors.ToCode().visit(self, data)

    def to_altair(self, data=None):
        """Emit the Python code as a string required to created this Chart."""
        return str(self._to_code(data=data))

    # transform method
    def transform_data(self, *args, **kwargs):
        """Set the data transform by keyword args."""
        if self.transform is None:
            self.transform = schema.Transform()
        self.transform.update_inferred_traits(*args, **kwargs)
        return self

    # Configuration methods
    def configure(self, *args, **kwargs):
        """Set chart configuration"""
        if self.config is None:
            self.config = schema.Config()
        self.config.update_inferred_traits(*args, **kwargs)
        return self

    def configure_axis(self, **kwargs):
        """Configure the chart's axes by keyword args."""
        return self.configure(axis=AxisConfig(**kwargs))

    def configure_cell(self, **kwargs):
        """Configure the chart's cell's by keyword args."""
        return self.configure(cell=CellConfig(**kwargs))

    def configure_legend(self, **kwargs):
        """Configure the chart's legend by keyword args."""
        return self.configure(legend=LegendConfig(**kwargs))

    def configure_mark(self, **kwargs):
        """Configure the chart's marks by keyword args."""
        return self.configure(mark=MarkConfig(**kwargs))

    def configure_scale(self, **kwargs):
        """Configure the chart's scales by keyword args."""
        return self.configure(scale=ScaleConfig(**kwargs))

    def _configure_facet(self, name, klass, **kwargs):
        """Helper method for configure_facet_* methods."""
        if self.config is None:
            self.config = schema.Config()
        facet_config = self.config.facet
        if facet_config is None:
            facet_config = FacetConfig()
        setattr(facet_config, name, klass(**kwargs))
        self.config.facet = facet_config
        return self

    def configure_facet_axis(self, **kwargs):
        """Configure the facet's axes by keyword args."""
        return self._configure_facet('axis', AxisConfig, **kwargs)

    def configure_facet_cell(self, **kwargs):
        """Configure the facet's cells by keyword args."""
        return self._configure_facet('cell', CellConfig, **kwargs)

    def configure_facet_grid(self, **kwargs):
        """Configure the facet's grid by keyword args."""
        return self._configure_facet('grid', FacetGridConfig, **kwargs)

    def configure_facet_scale(self, **kwargs):
        """Configure the facet's scales by keyword args."""
        return self._configure_facet('scale', FacetScaleConfig, **kwargs)

    # Display related methods
    def _ipython_display_(self):
        from IPython.display import display
        from vega import VegaLite
        display(VegaLite(self.to_dict()))

    def display(self):
        from IPython.display import display
        display(self)


class Chart(schema.ExtendedUnitSpec, TopLevelMixin):
    _data = None

    name = T.Unicode()
    description = T.Unicode()
    transform = T.Instance(schema.Transform, default_value=None, allow_none=True)
    mark = T.Enum(schema.Mark().values, default_value='point')
    encoding = T.Instance(Encoding, default_value=None, allow_none=True)
    config = T.Instance(schema.Config, allow_none=True)

    @T.observe('encoding')
    def _encoding_changed(self, change):
        if isinstance(change['new'], Encoding):
            self.encoding.parent = self
            if isinstance(self.data, pd.DataFrame):
                self.encoding._infer_types(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (isinstance(new, pd.DataFrame) or isinstance(new, Data) or new is None):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    skip = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(Chart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        base = super(Chart, self).__dir__()
        methods = [
            'to_altair', 'display',
            'configure', 'configure_axis', 'configure_cell',
            'configure_legend', 'configure_mark', 'configure_scale',
            'configure_facet_axis', 'configure_facet_cell',
            'configure_facet_grid', 'configure_facet_scale',
            'transform_data',
            'mark_area', 'mark_bar', 'mark_line', 'mark_point', 'mark_rule',
            'mark_text', 'mark_tick', 'mark_circle', 'mark_square',
            'encode',
        ]
        return base+methods

    def mark_area(self, **kwargs):
        self.mark = 'area'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_bar(self,**kwargs):
        self.mark = 'bar'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_line(self, **kwargs):
        self.mark = 'line'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_point(self, **kwargs):
        self.mark = 'point'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_rule(self, **kwargs):
        self.mark = 'rule'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_text(self, **kwargs):
        self.mark = 'text'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_tick(self, **kwargs):
        self.mark = 'tick'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_circle(self, **kwargs):
        self.mark = 'circle'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def mark_square(self, **kwargs):
        self.mark = 'square'
        if kwargs:
            self.configure_mark(**kwargs)
        return self

    def encode(self, *args, **kwargs):
        """Define the encoding for the Chart."""
        if self.encoding is None:
            self.encoding = Encoding()
        self.encoding.update_inferred_traits(*args, **kwargs)
        return self


class LayeredChart(schema.LayerSpec, TopLevelMixin):
    _data = None

    name = T.Unicode()
    description = T.Unicode()
    layers = T.List(T.Instance(Chart), allow_none=True, default_value=None)
    transform = T.Instance(schema.Transform, allow_none=True, default_value=None)
    config = T.Instance(schema.Config, allow_none=True, default_value=None)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (isinstance(new, pd.DataFrame) or isinstance(new, Data) or new is None):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    skip = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(LayeredChart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        base = super(Chart, self).__dir__()
        methods = [
            'to_dict', 'from_dict', 'to_altair', 'display',
            'configure', 'configure_axis', 'configure_cell',
            'configure_legend', 'configure_mark', 'configure_scale',
            'configure_facet_axis', 'configure_facet_cell',
            'configure_facet_grid', 'configure_facet_scale',
            'transform_data',
            'set_layers',
        ]
        return base+methods

    def set_layers(self, *layers):
        self.layers = list(layers)
        return self


class FacetedChart(schema.FacetSpec, TopLevelMixin):
    _data = None

    name = T.Unicode()
    description = T.Unicode()
    facet = T.Instance(Facet, allow_none=True, default_value=None)
    spec = T.Union([T.Instance(LayeredChart), T.Instance(Chart)], allow_none=True, default_value=None)
    transform = T.Instance(schema.Transform, allow_none=True, default_value=None)
    config = T.Instance(schema.Config, allow_none=True, default_value=None)

    @T.observe('facet')
    def _facet_changed(self, change):
        if isinstance(change['new'], Facet):
            self.facet.parent = self
            if isinstance(self.data, pd.DataFrame):
                self.facet._infer_types(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (isinstance(new, pd.DataFrame) or isinstance(new, Data) or new is None):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    skip = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(FacetedChart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        base = super(Chart, self).__dir__()
        methods = [
            'to_dict', 'from_dict', 'to_altair', 'display',
            'configure', 'configure_axis', 'configure_cell',
            'configure_legend', 'configure_mark', 'configure_scale',
            'configure_facet_axis', 'configure_facet_cell',
            'configure_facet_grid', 'configure_facet_scale',
            'transform_data',
            'set_facet',
        ]
        return base + methods

    def set_facet(self, *args, **kwargs):
        """Define the encoding for the Chart."""
        if self.facet is None:
            self.facet = Facet()
        self.facet.update_inferred_traits(*args, **kwargs)
        return self
