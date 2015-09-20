import os
import jinja2
import json
import numpy

def render(spec, width=None, height=None):
    """
    Render a vega specification to html.

    Uses a template to embed the specified visualization
    into html that can be rendered in the browser. Useful
    for visualization in notebooks.

    Parameters
    ----------
    spec : altair.api.Viz object
        Represents the visualization to be rendered to html

    width : int, optional, default=None
        Width in pixels

    height : int, optional, default=None
        Height in pixels
    """

    from jinja2 import Template, escape

    if width is not None:
        spec.config.width = width
    else:
        width = spec.config.width
    if height is not None:
        spec.config.height = height
    else:
        height = spec.config.height

    location = os.path.join(os.path.dirname(__file__), 'templates/template.html')
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

def save(spec, fname, overwrite=False, width=None, height=None):
    """
    Save an html-rendering of a vega specification to a file.

    Parameters
    ----------
    spec : altair.api.Viz object
        Represents the visualization spec to be rendered to html

    fname : str 
        Name of file to write to

    overwrite : boolean, optional, default=False
        Whether to overwrite an existing file.
        If false, will raise an error if file already exists.

    width : int, optional, default=None
        Width in pixels.

    height : int, optional, default=None
        Height in pixels.
    """

    exists = os.path.exists(fname)

    if exists is True:
        if overwrite is False:
            raise ValueError("File '%s' exists and overwrite is False" % fname)
        else:
            os.remove(fname)

    blob = render(spec, width, height)

    with open(fname, 'w') as f:
        f.write(blob)