import traitlets as T
import ipywidgets as w

from .api import Encoding, X, Y, Row, Col, Shape, Size, Color, Detail, Text
from .utils import infer_vegalite_type


import qgrid
qgrid.nbinstall(overwrite=True)
qgrid.set_defaults(remote_js=True, precision=4)
import json
from qgrid.grid import QGridWidget, defaults
from IPython.display import display, HTML
import pandas as pd


# ip = get_ipython()
# ip.display_formatter.ipython_display_formatter.for_type_by_name('pandas.core.frame',
#                                                                 'DataFrame',
#                                                                 display_dataframe)
# ip.display_formatter.ipython_display_formatter.for_type_by_name('pandas.core.series',
#                                                                 'Series',
#                                                                 display_dataframe)

class AltairWidget(object):

    def __init__(self, **kwargs):
        pass


def get_qgrid_widget(df):
    # remote_js = defaults.remote_js
    precision = defaults.precision
    grid_options = {'forceFitColumns': False, 'defaultColumnWidth': 100}
    return QGridWidget(df=df,
                       precision=precision,
                       grid_options=json.dumps(grid_options),
                       remote_js=False)




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

def create_dropdown_view(parent, attr):
    options = parent.traits()[attr].values
    value = getattr(parent, attr)
    dd = w.Dropdown(options=options, value=value)
    T.link((parent, attr), (dd, 'value'))
    return dd


def find_columns_and_types(df):
    columns = []
    types = []
    for c in df.columns:
        t = infer_vegalite_type(df[c])
        columns.append(c)
        types.append(t)
    return columns, types


def create_shelf_view(model, columns, types):
    opts = list(zip(['-']+columns, ['']+columns))
    column_view = w.Dropdown(options=opts, description=model.shelf_name, value='')
    type_view = w.Dropdown(options={'Q':'Q','T':'T','O':'O','N':'N'}, value='Q')
    shelf_view = w.HBox([column_view, type_view])
    def on_column_changed(name, value):
        if value == '':
            type_view.value = 'Q'
        else:
            index = columns.index(value)
            type_view.value = types[index]
    column_view.on_trait_change(on_column_changed, 'value')
    T.link((model, 'name'),(column_view, 'value'))
    T.link((type_view, 'value'), (model, 'type'))
    return shelf_view


_shelf_view_factories = {
    'x': create_shelf_view,
    'y': create_shelf_view,
    'row': create_shelf_view,
    'col': create_shelf_view,
    'shape': create_shelf_view,
    'color': create_shelf_view,
    'detail': create_shelf_view,
    'text': create_shelf_view,
    'size': create_shelf_view
}


def create_encoding_view(enc, columns, types, shelves=_shelves):
    vbox = w.VBox()
    children = []
    children.append(w.HTML('Encoding:', width='148px', height='32px'))

    for shelf in shelves:
        if getattr(enc, shelf, None) is None:
            setattr(enc, shelf, _shelf_types[shelf](''))
        factory = _shelf_view_factories[shelf]
        view = factory(getattr(enc, shelf), columns, types)
        children.append(view)
    
    vbox.children = children
    return vbox


def create_viz_types_buttons(viz, output):
    hbox = w.HBox()

    heading = w.HTML('Mark:', width='50px', height='32px')

    def on_render_table(*args):
        with output:
            output.clear_output()

            data = viz.data
            if isinstance(data, pd.Series):
                df = pd.DataFrame(data)
            else:
                df = data
            display(get_qgrid_widget(df))

            # display(data)

    def on_render_area(*args):
        with output:
            viz.area()
            output.clear_output()
            print(viz)

    def on_render_line(*args):
        with output:
            viz.line()
            output.clear_output()
            print(viz)

    def on_render_bar(*args):
        with output:
            viz.bar()
            output.clear_output()
            print(viz)

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


def create_viz_view(viz, shelves=_shelves):
    columns, types = find_columns_and_types(viz.data)
    vbox = w.VBox()
    if not hasattr(viz, 'encoding'):
        setattr(viz, 'encoding', Encoding())
    encoding = create_encoding_view(viz.encoding, columns, types, shelves=shelves)
    vbox.children = [encoding]
    return vbox


def create_render_view(v, shelves=_shelves):
    # Create output area
    output = w.Output()

    # Create render button that currently prints v
    render_button = w.Button(description='Render', width=20)
    def on_render(*args):
        with output:
            # Not exposing this yet because of bugs in the renderers that break this.
            # Printing instead.
            # v.render()
            output.clear_output()
            print(v)
    render_button.on_click(on_render)

    # Create types of viz hbox
    viz_types_hbox = create_viz_types_buttons(v, output)

    # Append render to types. This should be automatic afterwards.
    # viz_types_hbox.children.append(render_button)

    # Create vbox for shelves
    shelves_view = create_viz_view(v, shelves)

    # Create left pane with all controls
    left_pane = w.VBox()
    left_pane.children = [render_button, viz_types_hbox, shelves_view]

    final_pane = w.HBox()
    final_pane.children = [left_pane, output]

    return final_pane
