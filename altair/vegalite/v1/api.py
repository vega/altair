"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""

import functools
import operator
import os
import uuid
import warnings

import pandas as pd
import traitlets as T

from . import schema
from .. import expr
from .display import renderers
from ...utils import node
from ...utils._py3k_compat import string_types
from .schema import jstraitlets as jst
from .schema import (Axis, AxisConfig, Bin, CellConfig, Color, Column, Config,
                     Data, DataFormat, DateTime, Detail, Encoding, EqualFilter,
                     Facet, FacetConfig, FacetGridConfig, FacetScaleConfig,
                     FontStyle, FontWeight, HorizontalAlign, Label, Legend,
                     LegendConfig, MarkConfig, NiceTime, OneOfFilter, Opacity,
                     Order, OverlayConfig, Path, RangeFilter, Row, Scale,
                     ScaleConfig, Shape, Size, SortField, SortOrder,
                     StackOffset, Text, TimeUnit, UnitEncoding, UnitSpec,
                     VerticalAlign, X, Y)
from .traitlet_utils import update_subtraits


class FieldError(Exception):
    """Raised if a channel has a field related error.

    This is raised if a channel has no field name or if the field name is
    not found as the column name of the ``DataFrame``.
    """


#*************************************************************************
# Channel Aliases
#*************************************************************************



def use_signature(Obj):
    """Apply call signature and documentation of Obj to the decorated method"""
    def decorate(f):
        # call-signature of f is exposed via __wrapped__.
        # we want it to mimic Obj.__init__
        f.__wrapped__ = Obj.__init__
        f._uses_signature = Obj

        # Supplement the docstring of f with information from Obj
        f.__doc__ += Obj.__doc__[Obj.__doc__.index('\n'):]
        return f
    return decorate


#*************************************************************************
# Formula wrapper
# - makes field a required first argument of initialization
# - allows expr trait to be an Expression and processes it properly
#*************************************************************************

class Formula(schema.Formula):
    expr = jst.JSONUnion([jst.JSONString(),
                          jst.JSONInstance(expr.Expression)],
                         help=schema.Formula.expr.help)

    def __init__(self, field, expr=jst.undefined, **kwargs):
        super(Formula, self).__init__(field=field, expr=expr, **kwargs)

    def _finalize(self, **kwargs):
        """Finalize object: convert expr expression to string if necessary"""
        if isinstance(self.expr, expr.Expression):
            self.expr = repr(self.expr)
        super(Formula, self)._finalize(**kwargs)


#*************************************************************************
# Transform wrapper
# - allows filter trait to be an Expression and processes it properly
#*************************************************************************

class Transform(schema.Transform):
    filter = jst.JSONUnion([jst.JSONString(),
                            jst.JSONInstance(expr.Expression),
                            jst.JSONInstance(schema.EqualFilter),
                            jst.JSONInstance(schema.RangeFilter),
                            jst.JSONInstance(schema.OneOfFilter),
                            jst.JSONArray(jst.JSONUnion([
                                jst.JSONString(),
                                jst.JSONInstance(expr.Expression),
                                jst.JSONInstance(schema.EqualFilter),
                                jst.JSONInstance(schema.RangeFilter),
                                jst.JSONInstance(schema.OneOfFilter)]))],
                           help=schema.Transform.filter.help)

    def _finalize(self, **kwargs):
        """Finalize object: convert filter expressions to string"""
        convert = lambda f: repr(f) if isinstance(f, expr.Expression) else f
        self.filter = convert(self.filter)
        if isinstance(self.filter, list):
            self.filter = [convert(f) for f in self.filter]
        super(Transform, self)._finalize(**kwargs)


#*************************************************************************
# Top-level Objects
#*************************************************************************

class TopLevelMixin(object):

    @staticmethod
    def _png_output_available():
        return node.vl_cmd_available('vl2png')

    @staticmethod
    def _svg_output_available():
        return node.vl_cmd_available('vl2svg')

    def savechart(self, outfile, filetype=None):
        """Save a chart to file, in either png, svg, json, or html format.

        Note that png/svg output requires several nodejs packages to be
        installed and correctly configured. Before running this, you must
        have nodejs and cairo on your system and use the node package manager
        to install the ``canvas`` and ``vega-lite`` packages.

        If you are using anaconda, you can set it up this way:

            $ conda create -n node-env -c conda-forge python=2.7 cairo nodejs altair
            $ source activate node-env
            $ npm install canvas vega-lite

        The node binaries used here (``vl2vg``, ``vl2png``, ``vl2svg``) will be
        installed in the node root directory, which should be automatically
        detected by this function.

        Parameters
        ----------
        outfile : str
            The output filename
        filetype : str (optional)
            The filetype to use. One of ('svg', 'png', 'json', 'html').
            If not specified, it will be inferred from outfile.
        """
        if filetype is None:
            try:
                base, ext = os.path.splitext(outfile)
                filetype = ext[1:]
            except AttributeError:
                raise ValueError('filetype could not be inferred')

        if filetype in node.SUPPORTED_FILETYPES:
            node.savechart(self, outfile, filetype)
        elif filetype == 'json':
            if hasattr(outfile, 'write'):
                outfile.write(self.to_json())
            else:
                with open(outfile, 'w') as f:
                    f.write(self.to_json())
        elif filetype == 'html':
            if hasattr(outfile, 'write'):
                outfile.write(self.to_html())
            else:
                with open(outfile, 'w') as f:
                    f.write(self.to_html())
        else:
            supported = node.SUPPORTED_FILETYPES + ['json', 'html']
            raise ValueError('Cannot save chart of type {0}; supported'
                             'extensions are {1}'.format(filetype, supported))

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

        See Also
        --------
        savechart : save a chart representation to file in various formats,
                    including HTML
        """
        from ...utils.html import to_html
        return to_html(self.to_dict(validate_columns=True), template=template, title=title, **kwargs)

    def to_dict(self, data=True, validate_columns=False):
        """Emit the JSON representation for this object as as dict.

        Parameters
        ----------
        data : bool
            If True (default) then include data in the representation.
        validate_columns : bool
            If True (default is False) raise FieldError if there are missing or misspelled
            column names. This only actually raises if self.validate_columns is also set
            (it defaults to True).

        Returns
        -------
        spec : dict
            The JSON specification of the chart object.
        """
        dct = super(TopLevelMixin, self).to_dict(data=data, validate_columns=validate_columns)
        dct['$schema'] = schema.vegalite_schema_url
        return dct

    @classmethod
    def from_dict(cls, dct):
        """Instantiate the object from a valid JSON dictionary

        Parameters
        ----------
        dct : dict
            The dictionary containing a valid JSON chart specification.

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        if '$schema' in dct:
            if dct['$schema'] != schema.vegalite_schema_url:
                warnings.warn('from_dict: $schema={0} does not match '
                              'schema used to build this Altair version '
                              '({1}. '
                              ''.format(dct['$schema'],
                                        schema.vegalite_schema_url))
            dct = {k: v for k, v in dct.items() if k != '$schema'}
        return super(TopLevelMixin, cls).from_dict(dct)

    def to_json(self, data=True, sort_keys=True, **kwargs):
        """Emit the JSON representation for this object as a string.

        Parameters
        ----------
        data : bool
            If True (default) then include data in the representation.
        sort_keys : bool
            If True (default) then sort the keys in the output
        **kwargs
            Additional keyword arguments are passed to ``json.dumps()``

        Returns
        -------
        spec : string
            The JSON specification of the chart object.
        """
        kwargs['sort_keys'] = sort_keys
        return super(TopLevelMixin, self).to_json(data=data, json_kwds=kwargs)

    @classmethod
    def from_json(cls, json_string, **kwargs):
        """Instantiate the object from a valid JSON string

        Parameters
        ----------
        spec : string
            The string containing a valid JSON chart specification.

        Returns
        -------
        chart : Chart object
            The altair Chart object built from the specification.
        """
        return super(TopLevelMixin, cls).from_json(json_string,
                                                   json_kwds=kwargs)

    def to_python(self, data=None):
        """Emit the Python code as a string required to created this Chart."""
        return super(TopLevelMixin, self).to_python(data=data)

    # transform method
    @use_signature(schema.Transform)
    def transform_data(self, *args, **kwargs):
        """Set the data transform by keyword args."""
        return update_subtraits(self, 'transform', *args, **kwargs)

    # Configuration methods
    @use_signature(schema.Config)
    def configure(self, *args, **kwargs):
        """Set chart configuration"""
        return update_subtraits(self, 'config', *args, **kwargs)

    @use_signature(AxisConfig)
    def configure_axis(self, *args, **kwargs):
        """Configure the chart's axes by keyword args."""
        return update_subtraits(self, ('config', 'axis'), *args, **kwargs)

    @use_signature(CellConfig)
    def configure_cell(self, *args, **kwargs):
        """Configure the chart's cell's by keyword args."""
        return update_subtraits(self, ('config', 'cell'), *args, **kwargs)

    @use_signature(LegendConfig)
    def configure_legend(self, *args, **kwargs):
        """Configure the chart's legend by keyword args."""
        return update_subtraits(self, ('config', 'legend'), *args, **kwargs)

    @use_signature(OverlayConfig)
    def configure_overlay(self, *args, **kwargs):
        """Configure the chart's overlay by keyword args."""
        return update_subtraits(self, ('config', 'overlay'), *args, **kwargs)

    @use_signature(MarkConfig)
    def configure_mark(self, *args, **kwargs):
        """Configure the chart's marks by keyword args."""
        return update_subtraits(self, ('config', 'mark'), *args, **kwargs)

    @use_signature(ScaleConfig)
    def configure_scale(self, *args, **kwargs):
        """Configure the chart's scales by keyword args."""
        return update_subtraits(self, ('config', 'scale'), *args, **kwargs)

    @use_signature(FacetConfig)
    def configure_facet(self, *args, **kwargs):
        """Configure the chart's scales by keyword args."""
        return update_subtraits(self, ('config', 'facet'), *args, **kwargs)

    @use_signature(AxisConfig)
    def configure_facet_axis(self, *args, **kwargs):
        """Configure the facet's axes by keyword args."""
        return update_subtraits(self, ('config', 'facet', 'axis'),
                                *args, **kwargs)

    @use_signature(CellConfig)
    def configure_facet_cell(self, *args, **kwargs):
        """Configure the facet's cells by keyword args."""
        return update_subtraits(self, ('config', 'facet', 'cell'),
                                *args, **kwargs)

    @use_signature(FacetGridConfig)
    def configure_facet_grid(self, *args, **kwargs):
        """Configure the facet's grid by keyword args."""
        return update_subtraits(self, ('config', 'facet', 'grid'),
                                *args, **kwargs)

    @use_signature(FacetScaleConfig)
    def configure_facet_scale(self, *args, **kwargs):
        """Configure the facet's scales by keyword args."""
        return update_subtraits(self, ('config', 'facet', 'scale'),
                                *args, **kwargs)

    # Display related methods

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        if self.renderers is not None:
            return self.renderers.get()(self.spec)
        else:
            return {}

    def display(self):
        """Display the Chart using the Jupyter Notebook's rich output.

        To use this in the classic Jupyter Notebook, the ``ipyvega`` package
        must be installed.

        To use this in JupyterLab/nteract, run the ``enable_mime_rendering``
        function first.
        """
        from IPython.display import display
        display(self)

    def serve(self, ip='127.0.0.1', port=8888, n_retries=50, files=None,
              jupyter_warning=True, open_browser=True, http_server=None,
              **html_kwargs):
        """Open a web browser and visualize the chart

        Parameters
        ----------
        html : string
            HTML to serve
        ip : string (default = '127.0.0.1')
            ip address at which the HTML will be served.
        port : int (default = 8888)
            the port at which to serve the HTML
        n_retries : int (default = 50)
            the number of nearby ports to search if the specified port
            is already in use.
        files : dictionary (optional)
            dictionary of extra content to serve
        jupyter_warning : bool (optional)
            if True (default), then print a warning if this is used
            within the Jupyter notebook
        open_browser : bool (optional)
            if True (default), then open a web browser to the given HTML
        http_server : class (optional)
            optionally specify an HTTPServer class to use for showing the
            figure. The default is Python's basic HTTPServer.
        """
        from ...utils.server import serve
        html = self.to_html(**html_kwargs)
        serve(html, ip=ip, port=port, n_retries=n_retries,
              files=files, jupyter_warning=jupyter_warning,
              open_browser=open_browser, http_server=http_server)

    def _finalize(self, **kwargs):
        self._finalize_data()
        # data comes from wrappers, but self.data overrides this if defined
        if self.data is not None:
            kwargs['data'] = self.data
        super(TopLevelMixin, self)._finalize(**kwargs)

    def _finalize_data(self):
        """
        This function is called by _finalize() below.

        It performs final checks on the data:

        * Whether the data attribute contains expressions, and if so it extracts
          the appropriate data object and generates the appropriate transforms.
        """

        # Handle expressions. This transforms expr.DataFrame object into a set
        # of transforms and an actual pd.DataFrame. After this block runs,
        # self.data is either a URL or a pd.DataFrame or None.
        if isinstance(self.data, expr.DataFrame):
            columns = self.data._cols
            calculated_cols = self.data._calculated_cols
            filters = self.data._filters
            self.data = self.data._data
            if columns is not None and isinstance(self.data, pd.DataFrame):
                self.data = self.data[columns]
            if calculated_cols:
                self.transform_data(calculate=[Formula(field, expr=exp)
                                               for field, exp
                                               in calculated_cols.items()])
            if filters:
                filters = [repr(f) for f in filters]
                if len(filters) == 1:
                    self.transform_data(filter=filters[0])
                else:
                    self.transform_data(filter=filters)


class Chart(TopLevelMixin, schema.ExtendedUnitSpec):
    _data = None

    # use specialized version of Encoding and Transform
    encoding = jst.JSONInstance(Encoding,
                                help=schema.ExtendedUnitSpec.encoding.help)
    transform = jst.JSONInstance(Transform,
                                 help=schema.ExtendedUnitSpec.transform.help)
    mark = schema.Mark(default_value='point', help="""The mark type.""")

    def clone(self):
        """
        Return a clone of this object, recursively cloning each trait
        """
        copy = super(Chart, self).clone()
        copy._data = self._data
        return copy

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (new is None or isinstance(new, pd.DataFrame)
              or isinstance(new, expr.DataFrame) or isinstance(new, Data)):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    _skip_on_export = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(Chart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        return [m for m in dir(self.__class__) if m not in dir(T.HasTraits)]

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
    def mark_errorBar(self, *args, **kwargs):
        """Set the mark to 'errorBar' and optionally specify mark properties"""
        self.mark = 'errorBar'
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
        return update_subtraits(self, 'encoding', *args, **kwargs)

    def __add__(self, other):
        if isinstance(other, Chart):
            lc = LayeredChart()
            lc += self
            lc += other
            return lc
        else:
            raise TypeError('Can only add Charts/LayeredChart to Chart')

    @classmethod
    def from_dict(cls, spec):
        if 'layers' in spec:
            return LayeredChart.from_dict(spec)
        elif 'facet' in spec:
            return FacetedChart.from_dict(spec)
        else:
            return super(Chart, cls).from_dict(spec)


class LayeredChart(TopLevelMixin, schema.LayerSpec):
    _data = None

    # Use specialized version of Chart and Transform
    layers = jst.JSONArray(jst.JSONInstance(Chart),
                           help=schema.LayerSpec.layers.help)
    transform = jst.JSONInstance(Transform,
                                 help=schema.LayerSpec.transform.help)

    def clone(self):
        """
        Return a clone of this object, recursively cloning each trait
        """
        copy = super(LayeredChart, self).clone()
        copy._data = self._data
        return copy

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (new is None or isinstance(new, pd.DataFrame)
              or isinstance(new, expr.DataFrame) or isinstance(new, Data)):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    _skip_on_export = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(LayeredChart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        return [m for m in dir(self.__class__) if m not in dir(T.HasTraits)]

    def set_layers(self, *layers):
        self.layers = list(layers)
        return self

    def __iadd__(self, layer):
        if self.layers is jst.undefined:
            self.layers = [layer]
        else:
            self.layers = self.layers + [layer]
        return self


class FacetedChart(TopLevelMixin, schema.FacetSpec):
    _data = None

    # Use specialized version of Facet, spec, and Transform
    facet = jst.JSONInstance(Facet, help=schema.FacetSpec.facet.help)
    spec = jst.JSONUnion([jst.JSONInstance(LayeredChart),
                          jst.JSONInstance(Chart)],
                         help=schema.FacetSpec.spec.help)
    transform = jst.JSONInstance(Transform,
                                 help=schema.FacetSpec.transform.help)

    def clone(self):
        """
        Return a clone of this object, recursively cloning each trait
        """
        copy = super(FacetedChart, self).clone()
        copy._data = self._data
        return copy

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        if isinstance(new, string_types):
            self._data = Data(url=new)
        elif (new is None or isinstance(new, pd.DataFrame)
              or isinstance(new, expr.DataFrame) or isinstance(new, Data)):
            self._data = new
        else:
            raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))

    _skip_on_export = ['data', '_data']

    def __init__(self, data=None, **kwargs):
        super(FacetedChart, self).__init__(**kwargs)
        self.data = data

    def __dir__(self):
        return [m for m in dir(self.__class__) if m not in dir(T.HasTraits)]

    @use_signature(Facet)
    def set_facet(self, *args, **kwargs):
        """Define the facet encoding for the Chart."""
        return update_subtraits(self, 'facet', *args, **kwargs)
