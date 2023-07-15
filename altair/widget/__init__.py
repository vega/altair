import anywidget
import traitlets
import pathlib

_here = pathlib.Path(__file__).parent


class ChartWidget(anywidget.AnyWidget):
    _esm = _here / "static" / "index.js"
    spec = traitlets.Unicode().tag(sync=True)
    selection = traitlets.Dict().tag(sync=True)
