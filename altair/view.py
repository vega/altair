import traitlets as T
import ipywidgets as w

from .api import Encoding, X, Y, Row, Col, Shape, Size, Color, Detail, Text, use_renderer
from .utils import infer_vegalite_type


class AltairWidget(w.FlexBox):
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

    def __init__(self, viz, shelves=_shelves, renderer='lightning', **kwargs):
        kwargs['orientation'] = 'vertical'
        super(AltairWidget, self).__init__((), **kwargs)

        use_renderer(renderer)

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

        self.widget = w.HBox()

        # Create output area
        self.output = w.HBox()
        self.output.children = []

        # Create widget
        self.controls = self._create_left_pane()

        self.widget.children = [self.controls, self.output]

        self.children = [self.widget]

    def on_render_viz(self, *args):
        self._clear_output()

        to_display = w.Textarea(value=str(self.viz))

        # TODO: how to display properly?
        # to_display = w.Output()
        # with to_display:
        #     self.viz.render()

        self.output.children = [to_display]

        return self.render()

    def _clear_output(self):
        for c in self.output.children:
            c.visible = False
            method = getattr(c, 'clear_output', None)
            if method is not None:
                method()

        self.output.children = []

    def _create_left_pane(self):
        # Create types of viz hbox
        viz_types_hbox = self._create_viz_types_buttons()

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

        # TODO: Could not express this method succinctly as on_press always ends up calling viz.text()
        # for some reason

        # hbox.children = [heading]
        #
        # for mark in ['Area', 'Line', 'Bar', 'Point', 'Tick', 'Circle', 'Square', 'Text']:
        #     button = w.Button(description=mark)
        #
        #     def on_press(*args):
        #         viz_mark_method = getattr(self.viz, mark.lower())
        #         viz_mark_method()
        #         return self.on_render_viz()
        #
        #     button.on_click(on_press)
        #     hbox.children = hbox.children + (button,)

        def on_render_area(*args):
            self.viz.area()
            return self.on_render_viz()

        def on_render_line(*args):
            self.viz.line()
            return self.on_render_viz()

        def on_render_bar(*args):
            self.viz.bar()
            return self.on_render_viz()

        def on_render_point(*args):
            self.viz.point()
            return self.on_render_viz()

        def on_render_tick(*args):
            self.viz.tick()
            return self.on_render_viz()

        def on_render_circle(*args):
            self.viz.circle()
            return self.on_render_viz()

        def on_render_square(*args):
            self.viz.square()
            return self.on_render_viz()

        def on_render_text(*args):
            self.viz.text()
            return self.on_render_viz()

        area_button = w.Button(description='Area')
        area_button.on_click(on_render_area)

        line_button = w.Button(description='Line')
        line_button.on_click(on_render_line)

        bar_button = w.Button(description='Bar')
        bar_button.on_click(on_render_bar)

        point_button = w.Button(description='Point')
        point_button.on_click(on_render_point)

        tick_button = w.Button(description='Tick')
        tick_button.on_click(on_render_tick)

        circle_button = w.Button(description='Circle')
        circle_button.on_click(on_render_circle)

        square_button = w.Button(description='Square')
        square_button.on_click(on_render_square)

        text_button = w.Button(description='Text')
        text_button.on_click(on_render_text)

        hbox.children = [heading, area_button, line_button, bar_button, point_button, tick_button, circle_button,
                         square_button, text_button]

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

            return self.on_render_viz()

        def on_type_changed(name, value):
            return self.on_render_viz()

        T.link((model, 'name'), (column_view, 'value'))
        T.link((type_view, 'value'), (model, 'type'))
        column_view.on_trait_change(on_column_changed, 'value')
        type_view.on_trait_change(on_type_changed, 'value')
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
