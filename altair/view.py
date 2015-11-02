import traitlets as T
import ipywidgets as w

from .api import Viz, Encoding, X, Y, Row, Col, Shape, Size, Color, Shelf, Detail, Text
from .utils import infer_vegalite_type


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


def create_viz_view(viz, shelves=_shelves):
    columns, types = find_columns_and_types(viz.data)
    vbox = w.VBox()
    hbox = w.HBox()
    heading = w.HTML('Mark:', width='221px', height='32px')
    dd = create_dropdown_view(viz, 'marktype')
    hbox.children = [heading, dd]
    if not hasattr(viz, 'encoding'):
        setattr(viz, 'encoding', Encoding())
    encoding = create_encoding_view(viz.encoding, columns, types, shelves=shelves)
    vbox.children = [hbox, encoding]
    return vbox


# Not exposing this yet because of bugs in the renderers that break this.

# def create_render_view(v, shelves=_shelves):
#     render_button = w.Button(description='Render')
#     output = w.Output()
#     render_box = w.VBox()
#     render_box.children = [render_button, output]
#
#     viz_view = create_viz_view(v)
#     hbox = w.HBox()
#     hbox.children = [viz_view, render_box]
#     def on_render(*args):
#         with output:
#             v.render()
#     render_button.on_click(on_render)
#     return hbox

