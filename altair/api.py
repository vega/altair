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
from .schema._wrappers.encoding_channels import CHANNEL_CLASSES, CHANNEL_NAMES

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
# Encoding
#*************************************************************************
class Encoding(schema.Encoding):

    # Position channels
    x = T.Instance(X, default_value=None, allow_none=True)
    y = T.Instance(Y, default_value=None, allow_none=True)
    row = T.Instance(Row, default_value=None, allow_none=True)
    column = T.Instance(Column, default_value=None, allow_none=True)

    # Channels with legends
    color = T.Instance(Color, default_value=None, allow_none=True)
    size = T.Instance(Size, default_value=None, allow_none=True)
    shape = T.Instance(Shape, default_value=None, allow_none=True)
    opacity = T.Instance(Opacity, default_value=None, allow_none=True)

    # Field and order channels
    detail = T.Union([T.Instance(Detail), T.List(T.Instance(Detail))],
                     default_value=None, allow_none=True)
    text = T.Instance(Text, default_value=None, allow_none=True)
    label = T.Instance(Label, default_value=None, allow_none=True)
    path = T.Union([T.Instance(Path), T.List(T.Instance(Path))],
                   default_value=None, allow_none=True)
    order = T.Union([T.Instance(Order), T.List(T.Instance(Order))],
                   default_value=None, allow_none=True)

    parent = T.Instance(schema.BaseObject, default_value=None, allow_none=True)

    skip = ['parent']

    def _infer_types(self, data):
        for attr in CHANNEL_NAMES:
            val = getattr(self, attr)
            if val is not None:
                val._infer_type(data)

    @T.observe(*CHANNEL_NAMES)
    def _channel_changed(self, change):
        new = change['new']
        name = change['name']
        channel = getattr(self, name, None)
        if channel is not None and not getattr(channel, 'type', '') and isinstance(self.parent, Chart):
            meth = getattr(channel, '_infer_type', None)
            if meth is not None:
                meth(self.parent.data)


#*************************************************************************
# Encoding
#*************************************************************************
class Facet(schema.Facet):
    column = T.Instance(Column, allow_none=True, default_value=None)
    row = T.Instance(Row, allow_none=True, default_value=None)

    parent = T.Instance(schema.BaseObject, default_value=None, allow_none=True)

    skip = ['parent']

    def _infer_types(self, data):
        for attr in CHANNEL_NAMES:
            val = getattr(self, attr)
            if val is not None:
                val._infer_type(data)

    @T.observe('row', 'column')
    def _channel_changed(self, change):
        new = change['new']
        name = change['name']
        channel = getattr(self, name, None)
        if channel is not None and not getattr(channel, 'type', '') and isinstance(self.parent, Chart):
            meth = getattr(channel, '_infer_type', None)
            if meth is not None:
                meth(self.parent.data)


#*************************************************************************
# Top-level Objects
#*************************************************************************
class TopLevelMixin(object):
    @classmethod
    def from_dict(cls, dct):
        """Create a Chart from a dict of Vega-Lite JSON."""
        return visitors.FromDict().clsvisit(cls, dct)

    def to_dict(self, data=True):
        """Emit the Vega-Lite JSON for this Chart as as dict."""
        return visitors.ToDict().visit(self, data)

    def _to_code(self, data=None):
        """Emit the CodeGen object used to export this chart to Python code."""
        return visitors.ToCode().visit(self, data)

    def to_altair(self, data=None):
        """Emit the Python code as a string required to created this Chart."""
        return str(self._to_code(data=data))

    # transform method

    def transform_data(self, **kwargs):
        """Set the data transform by keyword args."""
        if self.transform is None:
            self.transform = schema.Transform()
        self.transform.update_traits(**kwargs)
        return self

    # Configuration methods

    def configure(self, *args, **kwargs):
        """Set chart configuration"""
        # Map config trait names to their classes
        name_to_trait = {key: val.klass
                         for key, val in schema.Config.class_traits().items()
                         if isinstance(val, T.Instance)}
        trait_to_name = {v:k for k, v in name_to_trait.items()}

        if len(name_to_trait) != len(trait_to_name):
            raise ValueError("Two Config() traits have the same class. "
                             "(Possibly caused by a vega-lite schema update?)")

        for val in args:
            if val.__class__ in trait_to_name:
                key = trait_to_name[val.__class__]
                if key in kwargs:
                    raise ValueError("{0} specified twice".format(key))
                kwargs[key] = val
            else:
                raise ValueError("unrecognized argument: {0}".format(val))
        if self.config is None:
            self.config = schema.Config()
        self.config.update_traits(**kwargs)
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
            'to_dict', 'from_dict', 'to_altair',
            'mark_area', 'mark_bar', 'mark_line', 'mark_point',
            'mark_text', 'mark_tick', 'mark_circle', 'mark_square',
            'encode', 'transform_data',
            'configure', 'configure_axis', 'configure_cell',
            'configure_legend', 'configure_mark', 'configure_scale',
            'configure_facet_axis', 'configure_facet_cell',
            'configure_facet_grid', 'configure_facet_scale',
            'display',
        ]
        return base+methods

    # Mark methods

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

    # Encoding method

    def encode(self, *args, **kwargs):
        """Define the encoding for the Chart."""
        for key, val in kwargs.items():
            if key in CHANNEL_CLASSES:
                if not isinstance(val, CHANNEL_CLASSES[key]):
                    kwargs[key] = CHANNEL_CLASSES[key](val)
        for item in args:
            if item.channel_name in kwargs:
                raise ValueError('Mulitple value for {0} provided'.format(item.channel_name))
            kwargs[item.channel_name] = item
        if self.encoding is None:
            self.encoding = Encoding()
        self.encoding.update_traits(**kwargs)
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
