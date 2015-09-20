"""
Altair HTML renderer. Uses native vega-lite/vega rendering
"""

import os
import json
import numpy


def render(spec, width=None, height=None):
    """
    Render spec using native vega-lite parser/Vega renderer.

    Parameters
    ----------
    spec: Altair spec
    width: int
    height: int
    """

    from jinja2 import Template, escape

    if width is not None:
        spec.vlconfig.width = width
    else:
        width = spec.vlconfig.width
    if height is not None:
        spec.vlconfig.height = height
    else:
        height = spec.vlconfig.height

    location = os.path.join(os.path.dirname(__file__),
                            'templates/template.html')
    base = open(location).read()
    d = spec.to_dict()

    class NumpyConvert(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.generic):
                return numpy.asscalar(obj)
            return json.JSONEncoder.default(self, obj)

    spec = escape(json.dumps(d, cls=NumpyConvert))
    fields = {'spec': spec, 'width': width, 'height': height}
    t = Template(base)
    html = t.render(**fields)
    return html
