"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""
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


def use_signature(Obj):
    """Apply call signature and documentation of Obj to the decorated method"""
    def decorate(f):
        # call-signature of f is exposed via __wrapped__.
        # we want it to mimic Obj.__init__
        f.__wrapped__ = Obj.__init__

        # Supplement the docstring of f with information from Obj
        f.__doc__ += Obj.__doc__[Obj.__doc__.index('\n'):]
        return f
    return decorate


#*************************************************************************
# Top-level Objects
#*************************************************************************
class TopLevelMixin(object):
    def to_html(self, template=None, title=None, **kwargs):
        """Emit a stand-alone HTML document containing this chart.

        Parameters
        ----------
        template : string
            The HTML template to use. This should have a format method, which
            accepts a "spec" and "title" argument. Note that a standard Python
            format string meets these requirements.
            By default, uses altair.utils.html.DEFAULT_TEMPLATE.
        title : string
            The title to use in the document. Default is "Vega-Lite Chart"
        kwargs :
            additional keywords to be passed to the template

        Returns
        -------
        html : string
            A string of HTML representing the chart
        """
        from .utils.html import to_html
        return to_html(self.to_dict(), template=template, title=title)

    def _to_code(self, data=None):
        """Emit the CodeGen object used to export this chart to Python code."""
        # do not call _finalize(), as we want the output code
        # to reflect the exact input
        return visitors.ToCode().visit(self, data=data)

    def to_altair(self, data=None):
        """Emit the Python code as a string required to created this Chart."""
        return str(self._to_code(data=data))

    # transform method
    @use_signature(schema.Transform)
    def transform_data(self, *args, **kwargs):
        """Set the data transform by keyword args."""
        return self.update_subtraits('transform', *args, **kwargs)

    # Configuration methods
    @use_signature(schema.Config)
    def configure(self, *args, **kwargs):
        """Set chart configuration"""
        return self.update_subtraits('config', *args, **kwargs)

    @use_signature(AxisConfig)
    def configure_axis(self, *args, **kwargs):
        """Configure the chart's axes by keyword args."""
        return self.update_subtraits(('config', 'axis'), *args, **kwargs)

    @use_signature(CellConfig)
    def configure_cell(self, *args, **kwargs):
        """Configure the chart's cell's by keyword args."""
        return self.update_subtraits(('config', 'cell'), *args, **kwargs)

    @use_signature(LegendConfig)
    def configure_legend(self, *args, **kwargs):
        """Configure the chart's legend by keyword args."""
        return self.update_subtraits(('config', 'legend'), *args, **kwargs)

    @use_signature(MarkConfig)
    def configure_mark(self, *args, **kwargs):
        """Configure the chart's marks by keyword args."""
        return self.update_subtraits(('config', 'mark'), *args, **kwargs)

    @use_signature(ScaleConfig)
    def configure_scale(self, *args, **kwargs):
        """Configure the chart's scales by keyword args."""
        return self.update_subtraits(('config', 'scale'), *args, **kwargs)

    @use_signature(FacetConfig)
    def configure_facet(self, *args, **kwargs):
        """Configure the chart's scales by keyword args."""
        return self.update_subtraits(('config', 'facet'), *args, **kwargs)

    @use_signature(AxisConfig)
    def configure_facet_axis(self, *args, **kwargs):
        """Configure the facet's axes by keyword args."""
        return self.update_subtraits(('config', 'facet', 'axis'),
                                     *args, **kwargs)

    @use_signature(CellConfig)
    def configure_facet_cell(self, *args, **kwargs):
        """Configure the facet's cells by keyword args."""
        return self.update_subtraits(('config', 'facet', 'cell'),
                                     *args, **kwargs)

    @use_signature(FacetGridConfig)
    def configure_facet_grid(self, *args, **kwargs):
        """Configure the facet's grid by keyword args."""
        return self.update_subtraits(('config', 'facet', 'grid'),
                                     *args, **kwargs)

    @use_signature(FacetScaleConfig)
    def configure_facet_scale(self, *args, **kwargs):
        """Configure the facet's scales by keyword args."""
        return self.update_subtraits(('config', 'facet', 'scale'),
                                     *args, **kwargs)

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

    @use_signature(MarkConfig)
    def mark_area(self, *args, **kwargs):
        """Set the mark to 'area' and optionally specify mark properties"""
        self.mark = 'area'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_bar(self, *args, **kwargs):
        """Set the mark to 'bar' and optionally specify mark properties"""
        self.mark = 'bar'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_line(self, *args, **kwargs):
        """Set the mark to 'line' and optionally specify mark properties"""
        self.mark = 'line'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_point(self, *args, **kwargs):
        """Set the mark to 'point' and optionally specify mark properties"""
        self.mark = 'point'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_rule(self, *args, **kwargs):
        """Set the mark to 'rule' and optionally specify mark properties"""
        self.mark = 'rule'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_text(self, *args, **kwargs):
        """Set the mark to 'text' and optionally specify mark properties"""
        self.mark = 'text'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_tick(self, *args, **kwargs):
        """Set the mark to 'tick' and optionally specify mark properties"""
        self.mark = 'tick'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_circle(self, *args, **kwargs):
        """Set the mark to 'circle' and optionally specify mark properties"""
        self.mark = 'circle'
        return self.configure_mark(*args, **kwargs)

    @use_signature(MarkConfig)
    def mark_square(self, *args, **kwargs):
        """Set the mark to 'square' and optionally specify mark properties"""
        self.mark = 'square'
        return self.configure_mark(*args, **kwargs)

    @use_signature(Encoding)
    def encode(self, *args, **kwargs):
        """Define the encoding for the Chart."""
        return self.update_subtraits('encoding', *args, **kwargs)

    def _finalize(self, **kwargs):
        # data comes from wrappers, but self.data overrides this if defined
        if self.data is not None:
            kwargs['data'] = self.data
        super(Chart, self)._finalize(**kwargs)

    def __add__(self, other):
        if isinstance(other, Chart):
            lc = LayeredChart()
            lc += self
            lc += other
            return lc
        else:
            raise TypeError('Can only add Charts/LayeredChart to Chart')
    

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

    def _finalize(self, **kwargs):
        # data comes from wrappers, but self.data overrides this if defined
        if self.data is not None:
            kwargs['data'] = self.data
        super(LayeredChart, self)._finalize(**kwargs)

    def __iadd__(self, layer):
        if self.layers is None:
            self.layers = [layer]
        else:
            self.layers = self.layers + [layer]
        return self
    

class FacetedChart(schema.FacetSpec, TopLevelMixin):
    _data = None

    name = T.Unicode()
    description = T.Unicode()
    facet = T.Instance(Facet, allow_none=True, default_value=None)
    spec = T.Union([T.Instance(LayeredChart), T.Instance(Chart)], allow_none=True, default_value=None)
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

    @use_signature(Facet)
    def set_facet(self, *args, **kwargs):
        """Define the facet encoding for the Chart."""
        return self.update_subtraits('facet', *args, **kwargs)

    def _finalize(self, **kwargs):
        # data comes from wrappers, but self.data overrides this if defined
        if self.data is not None:
            kwargs['data'] = self.data
        super(FacetedChart, self)._finalize(**kwargs)
