import traitlets as T
import ipywidgets as w
import qgrid
import json
from qgrid.grid import QGridWidget, defaults
from IPython.display import display
import pandas as pd

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

        qgrid.nbinstall(overwrite=True)
        qgrid.set_defaults(remote_js=True, precision=4)

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
        self.output = w.Output()
        self.output.children = []

        # Create widget
        self.widget = self._create_render_view()

    def render(self):
        return self.widget

    def on_render(self, *args):
        with self.output:
            # Not exposing this yet because of bugs in the renderers that break this.
            # Printing instead.
            # v.render()
            # print(self.viz)
            pass
        self._clear_output()
        to_render = w.Textarea(value=str(self.viz))
        self.output.children = [to_render]

    def _clear_output(self):
        for c in self.output.children:
            print(c)
            c.visible = False
        self.output.clear_output()

    def _create_render_view(self):
        # Create render button
        render_button = w.Button(description='Render', width=20)
        render_button.on_click(self.on_render)

        # Create types of viz hbox
        viz_types_hbox = self._create_viz_types_buttons()

        # TODO: Append render to types. This should be automatic afterwards.

        # Create vbox for shelves
        shelves_view = self._create_viz_view()

        # Create left pane with all controls
        left_pane = w.VBox()
        left_pane.children = [render_button, viz_types_hbox, shelves_view]

        final_pane = w.HBox()
        final_pane.children = [left_pane, self.output]

        return final_pane

    def _create_viz_view(self):
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

        def on_render_table(*args):
            with self.output:
                self.output.clear_output()

                data = self.viz.data
                if isinstance(data, pd.Series):
                    df = pd.DataFrame(data)
                else:
                    df = data
                display(self._get_qgrid_widget(df))

                # display(data)

        def on_render_area(*args):
            with self.output:
                self.viz.area()
                self.output.clear_output()
                print(self.viz)

        def on_render_line(*args):
            with self.output:
                self.viz.line()
                self.output.clear_output()
                print(self.viz)

        def on_render_bar(*args):
            with self.output:
                self.viz.bar()
                self.output.clear_output()
                print(self.viz)

        table_button = w.Button(description='Table')
        table_button.on_click(on_render_table)

        area_button = w.Button(description='Area')
        area_button.on_click(on_render_area)

        line_button = w.Button(description='Line')
        line_button.on_click(on_render_line)

        bar_button = w.Button(description='Bar')
        bar_button.on_click(on_render_bar)

        hbox.children = [heading, table_button, area_button, line_button, bar_button]
        return hbox

    @staticmethod
    def _create_shelf_view(model, columns, types):
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

    @staticmethod
    def _get_qgrid_widget(df):
        # remote_js = defaults.remote_js
        precision = defaults.precision
        grid_options = {'forceFitColumns': False, 'defaultColumnWidth': 100}
        return QGridWidget(df=df,
                           precision=precision,
                           grid_options=json.dumps(grid_options),
                           remote_js=False)
