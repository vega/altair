"""
Main API for Vega-lite spec generation.

DSL mapping Vega types to IPython traitlets.
"""
import six

import pandas as pd

from .schema import *  # TODO: expliticly import all names
from .schema import core, channels, Undefined

from .data import data_transformers, pipe
from ...utils import (infer_vegalite_type, parse_shorthand_plus_data,
                      use_signature, update_subtraits)
from .display import renderers


SCHEMA_URL = "https://vega.github.io/schema/vega-lite/v1.json"


def _get_channels_mapping():
    mapping = {}
    for attr in dir(channels):
        cls = getattr(channels, attr)
        if isinstance(cls, type) and issubclass(cls, SchemaBase):
            mapping[cls] = attr.lower()
    return mapping


#*************************************************************************
# Formula wrapper
# - makes field a required first argument of initialization
# - allows expr trait to be an Expression and processes it properly
#*************************************************************************

# class Formula(schema.Formula):
#     expr = jst.JSONUnion([jst.JSONString(),
#                           jst.JSONInstance(expr.Expression)],
#                          help=schema.Formula.expr.help)
#
#     def __init__(self, field, expr=jst.undefined, **kwargs):
#         super(Formula, self).__init__(field=field, expr=expr, **kwargs)
#
#     def _finalize(self, **kwargs):
#         """Finalize object: convert expr expression to string if necessary"""
#         if isinstance(self.expr, expr.Expression):
#             self.expr = repr(self.expr)
#         super(Formula, self)._finalize(**kwargs)


#*************************************************************************
# Transform wrapper
# - allows filter trait to be an Expression and processes it properly
#*************************************************************************

# class Transform(schema.Transform):
#     filter = jst.JSONUnion([jst.JSONString(),
#                             jst.JSONInstance(expr.Expression),
#                             jst.JSONInstance(schema.EqualFilter),
#                             jst.JSONInstance(schema.RangeFilter),
#                             jst.JSONInstance(schema.OneOfFilter),
#                             jst.JSONArray(jst.JSONUnion([
#                                 jst.JSONString(),
#                                 jst.JSONInstance(expr.Expression),
#                                 jst.JSONInstance(schema.EqualFilter),
#                                 jst.JSONInstance(schema.RangeFilter),
#                                 jst.JSONInstance(schema.OneOfFilter)]))],
#                            help=schema.Transform.filter.help)
#
#     def _finalize(self, **kwargs):
#         """Finalize object: convert filter expressions to string"""
#         convert = lambda f: repr(f) if isinstance(f, expr.Expression) else f
#         self.filter = convert(self.filter)
#         if isinstance(self.filter, list):
#             self.filter = [convert(f) for f in self.filter]
#         super(Transform, self)._finalize(**kwargs)


#*************************************************************************
# Top-level Objects
#*************************************************************************

class TopLevelMixin(object):
    def _prepare_data(self):
        if isinstance(self.data, (dict, core.Data)):
            pass
        elif isinstance(self.data, pd.DataFrame):
            self.data = pipe(self.data, data_transformers.get())
        elif isinstance(self.data, six.string_types):
            self.data = core.Data(url=self.data)

    def to_dict(self, *args, **kwargs):
        # TODO: it's a bit weird that to_dict modifies the object.
        #       Should we create a copy first?
        original_data = getattr(self, 'data', Undefined)
        self._prepare_data()
        # We make use of two context markers:
        # - 'data' points to the data that should be referenced for column type
        #   inference.
        # - 'toplevel' is a boolean flag that is assumed to be true; if it's
        #   true then a "$schema" arg is added to the dict.

        context = kwargs.get('context', {})
        if 'data' not in context and original_data is not Undefined:
            context['data'] = original_data
        if context.get('top_level', True):
            # since this is top-level we add $schema if it's missing
            if '$schema' not in self._kwds:
                self._kwds['$schema'] = SCHEMA_URL
            # subschemas below this one are not top-level
            context['top_level'] = False
        kwargs['context'] = context
        return super(TopLevelMixin, self).to_dict(*args, **kwargs)

    # def savechart(self, outfile, filetype=None):
    #     """Save a chart to file, in either png, svg, json, or html format.
    #
    #     Note that png/svg output requires several nodejs packages to be
    #     installed and correctly configured. Before running this, you must
    #     have nodejs and cairo on your system and use the node package manager
    #     to install the ``canvas`` and ``vega-lite`` packages.
    #
    #     If you are using anaconda, you can set it up this way:
    #
    #         $ conda create -n node-env -c conda-forge python=2.7 cairo nodejs altair
    #         $ source activate node-env
    #         $ npm install canvas vega-lite
    #
    #     The node binaries used here (``vl2vg``, ``vl2png``, ``vl2svg``) will be
    #     installed in the node root directory, which should be automatically
    #     detected by this function.
    #
    #     Parameters
    #     ----------
    #     outfile : str
    #         The output filename
    #     filetype : str (optional)
    #         The filetype to use. One of ('svg', 'png', 'json', 'html').
    #         If not specified, it will be inferred from outfile.
    #     """
    #     if filetype is None:
    #         try:
    #             base, ext = os.path.splitext(outfile)
    #             filetype = ext[1:]
    #         except AttributeError:
    #             raise ValueError('filetype could not be inferred')
    #
    #     if filetype in node.SUPPORTED_FILETYPES:
    #         node.savechart(self, outfile, filetype)
    #     elif filetype == 'json':
    #         if hasattr(outfile, 'write'):
    #             outfile.write(self.to_json())
    #         else:
    #             with open(outfile, 'w') as f:
    #                 f.write(self.to_json())
    #     elif filetype == 'html':
    #         if hasattr(outfile, 'write'):
    #             outfile.write(self.to_html())
    #         else:
    #             with open(outfile, 'w') as f:
    #                 f.write(self.to_html())
    #     else:
    #         supported = node.SUPPORTED_FILETYPES + ['json', 'html']
    #         raise ValueError('Cannot save chart of type {0}; supported'
    #                          'extensions are {1}'.format(filetype, supported))
    #
    # def to_html(self, template=None, title=None, **kwargs):
    #     """Emit a stand-alone HTML document containing this chart.
    #
    #     Parameters
    #     ----------
    #     template : string
    #         The HTML template to use. This should have a format method, which
    #         accepts a "spec" and "title" argument. Note that a standard Python
    #         format string meets these requirements.
    #         By default, uses altair.utils.html.DEFAULT_TEMPLATE.
    #     title : string
    #         The title to use in the document. Default is "Vega-Lite Chart"
    #     kwargs :
    #         additional keywords to be passed to the template
    #
    #     Returns
    #     -------
    #     html : string
    #         A string of HTML representing the chart
    #
    #     See Also
    #     --------
    #     savechart : save a chart representation to file in various formats,
    #                 including HTML
    #     """
    #     from ...utils.html import to_html
    #     return to_html(self.to_dict(), template=template, title=title, **kwargs)
    #
    # def to_dict(self, data=True):
    #     """Emit the JSON representation for this object as as dict.
    #
    #     Parameters
    #     ----------
    #     data : bool
    #         If True (default) then include data in the representation.
    #
    #     Returns
    #     -------
    #     spec : dict
    #         The JSON specification of the chart object.
    #     """
    #     dct = super(TopLevelMixin, self).to_dict(data=data)
    #     dct['$schema'] = schema.vegalite_schema_url
    #     return dct
    #
    # @classmethod
    # def from_dict(cls, dct):
    #     """Instantiate the object from a valid JSON dictionary
    #
    #     Parameters
    #     ----------
    #     dct : dict
    #         The dictionary containing a valid JSON chart specification.
    #
    #     Returns
    #     -------
    #     chart : Chart object
    #         The altair Chart object built from the specification.
    #     """
    #     if '$schema' in dct:
    #         if dct['$schema'] != schema.vegalite_schema_url:
    #             warnings.warn('from_dict: $schema={0} does not match '
    #                           'schema used to build this Altair version '
    #                           '({1}. '
    #                           ''.format(dct['$schema'],
    #                                     schema.vegalite_schema_url))
    #         dct = {k: v for k, v in dct.items() if k != '$schema'}
    #     return super(TopLevelMixin, cls).from_dict(dct)
    #
    # def to_json(self, data=True, sort_keys=True, **kwargs):
    #     """Emit the JSON representation for this object as a string.
    #
    #     Parameters
    #     ----------
    #     data : bool
    #         If True (default) then include data in the representation.
    #     sort_keys : bool
    #         If True (default) then sort the keys in the output
    #     **kwargs
    #         Additional keyword arguments are passed to ``json.dumps()``
    #
    #     Returns
    #     -------
    #     spec : string
    #         The JSON specification of the chart object.
    #     """
    #     kwargs['sort_keys'] = sort_keys
    #     return super(TopLevelMixin, self).to_json(data=data, json_kwds=kwargs)
    #
    # @classmethod
    # def from_json(cls, json_string, **kwargs):
    #     """Instantiate the object from a valid JSON string
    #
    #     Parameters
    #     ----------
    #     spec : string
    #         The string containing a valid JSON chart specification.
    #
    #     Returns
    #     -------
    #     chart : Chart object
    #         The altair Chart object built from the specification.
    #     """
    #     return super(TopLevelMixin, cls).from_json(json_string,
    #                                                json_kwds=kwargs)

    # def to_python(self, data=None):
    #     """Emit the Python code as a string required to created this Chart."""
    #     return super(TopLevelMixin, self).to_python(data=data)

    # # transform method
    # @use_signature(Transform)
    # def transform_data(self, *args, **kwargs):
    #     """Set the data transform by keyword args."""
    #     return update_subtraits(self, 'transform', *args, **kwargs)
    #
    # # Configuration methods
    # @use_signature(Config)
    # def configure(self, *args, **kwargs):
    #     """Set chart configuration"""
    #     return update_subtraits(self, 'config', *args, **kwargs)
    #
    # @use_signature(AxisConfig)
    # def configure_axis(self, *args, **kwargs):
    #     """Configure the chart's axes by keyword args."""
    #     return update_subtraits(self, ('config', 'axis'), *args, **kwargs)
    #
    # @use_signature(CellConfig)
    # def configure_cell(self, *args, **kwargs):
    #     """Configure the chart's cell's by keyword args."""
    #     return update_subtraits(self, ('config', 'cell'), *args, **kwargs)
    #
    # @use_signature(LegendConfig)
    # def configure_legend(self, *args, **kwargs):
    #     """Configure the chart's legend by keyword args."""
    #     return update_subtraits(self, ('config', 'legend'), *args, **kwargs)
    #
    # @use_signature(OverlayConfig)
    # def configure_overlay(self, *args, **kwargs):
    #     """Configure the chart's overlay by keyword args."""
    #     return update_subtraits(self, ('config', 'overlay'), *args, **kwargs)
    #
    # @use_signature(MarkConfig)
    # def configure_mark(self, *args, **kwargs):
    #     """Configure the chart's marks by keyword args."""
    #     return update_subtraits(self, ('config', 'mark'), *args, **kwargs)
    #
    # @use_signature(ScaleConfig)
    # def configure_scale(self, *args, **kwargs):
    #     """Configure the chart's scales by keyword args."""
    #     return update_subtraits(self, ('config', 'scale'), *args, **kwargs)
    #
    # @use_signature(FacetConfig)
    # def configure_facet(self, *args, **kwargs):
    #     """Configure the chart's scales by keyword args."""
    #     return update_subtraits(self, ('config', 'facet'), *args, **kwargs)
    #
    # @use_signature(AxisConfig)
    # def configure_facet_axis(self, *args, **kwargs):
    #     """Configure the facet's axes by keyword args."""
    #     return update_subtraits(self, ('config', 'facet', 'axis'),
    #                             *args, **kwargs)
    #
    # @use_signature(CellConfig)
    # def configure_facet_cell(self, *args, **kwargs):
    #     """Configure the facet's cells by keyword args."""
    #     return update_subtraits(self, ('config', 'facet', 'cell'),
    #                             *args, **kwargs)
    #
    # @use_signature(FacetGridConfig)
    # def configure_facet_grid(self, *args, **kwargs):
    #     """Configure the facet's grid by keyword args."""
    #     return update_subtraits(self, ('config', 'facet', 'grid'),
    #                             *args, **kwargs)
    #
    # @use_signature(FacetScaleConfig)
    # def configure_facet_scale(self, *args, **kwargs):
    #     """Configure the facet's scales by keyword args."""
    #     return update_subtraits(self, ('config', 'facet', 'scale'),
    #                             *args, **kwargs)

    # Display related methods

    def _repr_mimebundle_(self, include, exclude):
        """Return a MIME bundle for display in Jupyter frontends."""
        return renderers.get()(self.to_dict())

    def display(self):
        """Display the Chart using the Jupyter Notebook's rich output.

        To use this in the classic Jupyter Notebook, the ``ipyvega`` package
        must be installed.

        To use this in JupyterLab/nteract, run the ``enable_mime_rendering``
        function first.
        """
        from IPython.display import display
        display(self)

    # def serve(self, ip='127.0.0.1', port=8888, n_retries=50, files=None,
    #           jupyter_warning=True, open_browser=True, http_server=None,
    #           **html_kwargs):
    #     """Open a web browser and visualize the chart
    #
    #     Parameters
    #     ----------
    #     html : string
    #         HTML to serve
    #     ip : string (default = '127.0.0.1')
    #         ip address at which the HTML will be served.
    #     port : int (default = 8888)
    #         the port at which to serve the HTML
    #     n_retries : int (default = 50)
    #         the number of nearby ports to search if the specified port
    #         is already in use.
    #     files : dictionary (optional)
    #         dictionary of extra content to serve
    #     jupyter_warning : bool (optional)
    #         if True (default), then print a warning if this is used
    #         within the Jupyter notebook
    #     open_browser : bool (optional)
    #         if True (default), then open a web browser to the given HTML
    #     http_server : class (optional)
    #         optionally specify an HTTPServer class to use for showing the
    #         figure. The default is Python's basic HTTPServer.
    #     """
    #     from ...utils.server import serve
    #     html = self.to_html(**html_kwargs)
    #     serve(html, ip=ip, port=port, n_retries=n_retries,
    #           files=files, jupyter_warning=jupyter_warning,
    #           open_browser=open_browser, http_server=http_server)

    # def _finalize(self, **kwargs):
    #     self._finalize_data()
    #     # data comes from wrappers, but self.data overrides this if defined
    #     if self.data is not None:
    #         kwargs['data'] = self.data
    #     super(TopLevelMixin, self)._finalize(**kwargs)
    #
    # def _finalize_data(self):
    #     """
    #     This function is called by _finalize() below.
    #
    #     It performs final checks on the data:
    #
    #     * Whether the data attribute contains expressions, and if so it extracts
    #       the appropriate data object and generates the appropriate transforms.
    #     """
    #
    #     # Handle expressions. This transforms expr.DataFrame object into a set
    #     # of transforms and an actual pd.DataFrame. After this block runs,
    #     # self.data is either a URL or a pd.DataFrame or None.
    #     if isinstance(self.data, expr.DataFrame):
    #         columns = self.data._cols
    #         calculated_cols = self.data._calculated_cols
    #         filters = self.data._filters
    #         self.data = self.data._data
    #         if columns is not None and isinstance(self.data, pd.DataFrame):
    #             self.data = self.data[columns]
    #         if calculated_cols:
    #             self.transform_data(calculate=[Formula(field, expr=exp)
    #                                            for field, exp
    #                                            in calculated_cols.items()])
    #         if filters:
    #             filters = [repr(f) for f in filters]
    #             if len(filters) == 1:
    #                 self.transform_data(filter=filters[0])
    #             else:
    #                 self.transform_data(filter=filters)


class Chart(TopLevelMixin, ExtendedUnitSpec):
    def __init__(self, data=Undefined, encoding=Undefined, mark=Undefined,
                 width=400, height=300, **kwargs):
        super(Chart, self).__init__(data=data, encoding=encoding, mark=mark,
                                    width=width, height=height, **kwargs)

    @use_signature(MarkConfig)
    def mark_area(self, **kwargs):
        """Set the mark to 'area' and optionally specify mark properties"""
        self.mark = 'area'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_bar(self, **kwargs):
        """Set the mark to 'bar' and optionally specify mark properties"""
        self.mark = 'bar'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_errorBar(self, **kwargs):
        """Set the mark to 'errorBar' and optionally specify mark properties"""
        self.mark = 'errorBar'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_line(self, **kwargs):
        """Set the mark to 'line' and optionally specify mark properties"""
        self.mark = 'line'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_point(self, **kwargs):
        """Set the mark to 'point' and optionally specify mark properties"""
        self.mark = 'point'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_rule(self, **kwargs):
        """Set the mark to 'rule' and optionally specify mark properties"""
        self.mark = 'rule'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_text(self, **kwargs):
        """Set the mark to 'text' and optionally specify mark properties"""
        self.mark = 'text'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_tick(self, **kwargs):
        """Set the mark to 'tick' and optionally specify mark properties"""
        self.mark = 'tick'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_circle(self, **kwargs):
        """Set the mark to 'circle' and optionally specify mark properties"""
        self.mark = 'circle'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def mark_square(self, **kwargs):
        """Set the mark to 'square' and optionally specify mark properties"""
        self.mark = 'square'
        return self.configure_mark(**kwargs)

    @use_signature(MarkConfig)
    def configure_mark(self, **kwargs):
        return update_subtraits(self, ('config', 'mark'), **kwargs)

    @use_signature(Encoding)
    def encode(self, *args, **kwargs):
        """Define the encoding for the Chart."""
        if args:
            mapping = _get_channels_mapping()
            for arg in args:
                encoding = mapping.get(type(arg), None)
                if encoding is None:
                    raise NotImplementedError("non-keyword arg of type {0}"
                                              "".format(type(arg)))
                if encoding in kwargs:
                    raise ValueError("encode: encoding {0} specified twice"
                                     "".format(encoding))
                kwargs[encoding] = arg

        for prop, field in list(kwargs.items()):
            if not isinstance(field, SchemaBase):
                cls = getattr(channels, prop.title())
                # Don't validate now, because field will be computed
                # as part of the to_dict() call.
                kwargs[prop] = cls.from_dict(field, validate=False)
        return update_subtraits(self, 'encoding', **kwargs)

    # def __add__(self, other):
    #     if isinstance(other, Chart):
    #         lc = LayeredChart()
    #         lc += self
    #         lc += other
    #         return lc
    #     else:
    #         raise TypeError('Can only add Charts/LayeredChart to Chart')
    #
    # @classmethod
    # def from_dict(cls, spec):
    #     if 'layers' in spec:
    #         return LayeredChart.from_dict(spec)
    #     elif 'facet' in spec:
    #         return FacetedChart.from_dict(spec)
    #     else:
    #         return super(Chart, cls).from_dict(spec)


# class LayeredChart(TopLevelMixin, schema.LayerSpec):
#     _data = None
#
#     # Use specialized version of Chart and Transform
#     layers = jst.JSONArray(jst.JSONInstance(Chart),
#                            help=schema.LayerSpec.layers.help)
#     transform = jst.JSONInstance(Transform,
#                                  help=schema.LayerSpec.transform.help)
#
#     def clone(self):
#         """
#         Return a clone of this object, recursively cloning each trait
#         """
#         copy = super(LayeredChart, self).clone()
#         copy._data = self._data
#         return copy
#
#     @property
#     def data(self):
#         return self._data
#
#     @data.setter
#     def data(self, new):
#         if isinstance(new, string_types):
#             self._data = Data(url=new)
#         elif (new is None or isinstance(new, pd.DataFrame)
#               or isinstance(new, expr.DataFrame) or isinstance(new, Data)):
#             self._data = new
#         else:
#             raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))
#
#     _skip_on_export = ['data', '_data']
#
#     def __init__(self, data=None, **kwargs):
#         super(LayeredChart, self).__init__(**kwargs)
#         self.data = data
#
#     # def __dir__(self):
#     #     return [m for m in dir(self.__class__) if m not in dir(T.HasTraits)]
#
#     def set_layers(self, *layers):
#         self.layers = list(layers)
#         return self
#
#     def __iadd__(self, layer):
#         if self.layers is jst.undefined:
#             self.layers = [layer]
#         else:
#             self.layers = self.layers + [layer]
#         return self


# class FacetedChart(TopLevelMixin, schema.FacetSpec):
#     _data = None
#
#     # Use specialized version of Facet, spec, and Transform
#     facet = jst.JSONInstance(Facet, help=schema.FacetSpec.facet.help)
#     spec = jst.JSONUnion([jst.JSONInstance(LayeredChart),
#                           jst.JSONInstance(Chart)],
#                          help=schema.FacetSpec.spec.help)
#     transform = jst.JSONInstance(Transform,
#                                  help=schema.FacetSpec.transform.help)
#
#     def clone(self):
#         """
#         Return a clone of this object, recursively cloning each trait
#         """
#         copy = super(FacetedChart, self).clone()
#         copy._data = self._data
#         return copy
#
#     @property
#     def data(self):
#         return self._data
#
#     @data.setter
#     def data(self, new):
#         if isinstance(new, string_types):
#             self._data = Data(url=new)
#         elif (new is None or isinstance(new, pd.DataFrame)
#               or isinstance(new, expr.DataFrame) or isinstance(new, Data)):
#             self._data = new
#         else:
#             raise TypeError('Expected DataFrame or altair.Data, got: {0}'.format(new))
#
#     _skip_on_export = ['data', '_data']
#
#     def __init__(self, data=None, **kwargs):
#         super(FacetedChart, self).__init__(**kwargs)
#         self.data = data
#
#     # def __dir__(self):
#     #     return [m for m in dir(self.__class__) if m not in dir(T.HasTraits)]
#
#     @use_signature(Facet)
#     def set_facet(self, *args, **kwargs):
#         """Define the facet encoding for the Chart."""
#         return update_subtraits(self, 'facet', *args, **kwargs)
