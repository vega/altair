import traitlets as T
import ipywidgets as w
import qgrid
import json
from qgrid.grid import QGridWidget, defaults

from .api import Encoding, X, Y, Row, Col, Shape, Size, Color, Detail, Text
from .utils import infer_vegalite_type


class AltairWidget(object):
    _shelves = ('x', 'y', 'row', 'col', 'shape', 'color', 'size', 'detail', 'text')

    _shelf_types = {
        'x': X,
        'y': Y,
        'row': Row,
        'col': Col,
        'shape': Shape,
        'color': Color,
        'detail': Detail,
        'text': Text,
        'size': Size
    }

    def __init__(self, viz, shelves=_shelves):
        self.viz = viz
        self.shelves = shelves

        self._shelf_view_factories = {
            'x': self._create_shelf_view,
            'y': self._create_shelf_view,
            'row': self._create_shelf_view,
            'col': self._create_shelf_view,
            'shape': self._create_shelf_view,
            'color': self._create_shelf_view,
            'detail': self._create_shelf_view,
            'text': self._create_shelf_view,
            'size': self._create_shelf_view
        }

        # Create output area
        self.output = w.HBox()
        self.output.children = []

        # Create widget
        self.controls = self._create_left_pane()
        self.widget = w.HBox()
        self.widget.children = [self.controls, self.output]

    def render(self):
        return self.widget

    def on_render_viz(self, *args):
        self._clear_output()

        self.output.children = [w.Textarea(value=str(self.viz))]

        return self.render()

    def on_render_table(self, *args):
        self._clear_output()

        data = self.viz.data
        df = data  # TODO: Make df robust if data is not pd.df and is dict
        widget = self._get_qgrid_widget(df)
        self.output.children = [widget]

        return self.render()

    def _clear_output(self):
        for c in self.output.children:
            c.visible = False

        self.output.children = []

    def _create_left_pane(self):
        # Create types of viz hbox
        viz_types_hbox = self._create_viz_types_buttons()

        # TODO: Append render to types. This should be automatic afterwards.

        # Create vbox for shelves
        shelves_view = self._create_shelves_controls()

        # Create left pane with all controls
        left_pane = w.VBox()
        left_pane.children = [viz_types_hbox, shelves_view]

        return left_pane

    def _create_shelves_controls(self):
        columns, types = self._find_columns_and_types(self.viz.data)
        vbox = w.VBox()
        if not hasattr(self.viz, 'encoding'):
            setattr(self.viz, 'encoding', Encoding())
        encoding = self._create_encoding_view(columns, types)
        vbox.children = [encoding]
        return vbox

    def _create_viz_types_buttons(self):
        hbox = w.HBox()

        heading = w.HTML('Mark:', width='50px', height='32px')

        def on_render_area(*args):
            self.viz.area()
            return self.on_render_viz()

        def on_render_line(*args):
            self.viz.line()
            return self.on_render_viz()

        def on_render_bar(*args):
            self.viz.bar()
            return self.on_render_viz()

        table_button = w.Button(description='Table')
        table_button.on_click(self.on_render_table)

        area_button = w.Button(description='Area')
        area_button.on_click(on_render_area)

        line_button = w.Button(description='Line')
        line_button.on_click(on_render_line)

        bar_button = w.Button(description='Bar')
        bar_button.on_click(on_render_bar)

        hbox.children = [heading, table_button, area_button, line_button, bar_button]
        return hbox

    def _create_encoding_view(self, columns, types):
        enc = self.viz.encoding

        vbox = w.VBox()
        children = list()
        children.append(w.HTML('Encoding:', width='148px', height='32px'))

        for shelf in self.shelves:
            if getattr(enc, shelf, None) is None:
                setattr(enc, shelf, self._shelf_types[shelf](''))
            factory = self._shelf_view_factories[shelf]
            view = factory(getattr(enc, shelf), columns, types)
            children.append(view)

        vbox.children = children
        return vbox

    def _create_shelf_view(self, model, columns, types):
        opts = list(zip(['-']+columns, ['']+columns))
        column_view = w.Dropdown(options=opts, description=model.shelf_name, value='')
        type_view = w.Dropdown(options={'Q': 'Q', 'T': 'T', 'O': 'O', 'N': 'N'}, value='Q')
        shelf_view = w.HBox([column_view, type_view])

        def on_column_changed(name, value):
            if value == '':
                type_view.value = 'Q'
            else:
                index = columns.index(value)
                type_view.value = types[index]

            return self.on_render_viz

        column_view.on_trait_change(on_column_changed, 'value')
        T.link((model, 'name'), (column_view, 'value'))
        T.link((type_view, 'value'), (model, 'type'))
        return shelf_view

    @staticmethod
    def _find_columns_and_types(df):
        columns = []
        types = []
        for c in df.columns:
            t = infer_vegalite_type(df[c])
            columns.append(c)
            types.append(t)
        return columns, types

    @staticmethod
    def _create_dropdown_view(parent, attr):
        options = parent.traits()[attr].values
        value = getattr(parent, attr)
        dd = w.Dropdown(options=options, value=value)
        T.link((parent, attr), (dd, 'value'))
        return dd

    @staticmethod
    def _get_qgrid_widget(df):
        # remote_js = defaults.remote_js
        precision = defaults.precision
        grid_options = {'forceFitColumns': False, 'defaultColumnWidth': 100}
        return QGridWidget(df=df,
                           precision=precision,
                           grid_options=json.dumps(grid_options),
                           remote_js=False)
