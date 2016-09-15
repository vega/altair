import ast
import os
import json

import numpy as np

try:
    import matplotlib
except ImportError:
    matplotlib = None
else:
    matplotlib.use('Agg')  # don't display plots


def exec_then_eval(code, _globals=None, _locals=None):
    """Exec a code block & return evaluation of the last line"""
    # TODO: make this less brittle.
    _globals = _globals or {}
    _locals = _locals or {}

    block = ast.parse(code, mode='exec')
    last = ast.Expression(block.body.pop().value)

    exec(compile(block, '<string>', mode='exec'), _globals, _locals)
    return eval(compile(last, '<string>', mode='eval'), _globals, _locals)


def strip_vl_extension(filename):
    """Strip the vega-lite extension (either vl.json or json) from filename"""
    for ext in ['.vl.json', '.json']:
        if filename.endswith(ext):
            return filename[:-len(ext)]
    else:
        return filename


def padded_thumbnail(im, size=(200, 200), offset=(0, 0)):
    thumb = im[offset[0]: offset[0] + size[0],
               offset[1]: offset[1] + size[1]]

    pad_lengths = (size[0] - thumb.shape[0], size[1] - thumb.shape[1])
    pad_lengths = [(pad_lengths[0] // 2, pad_lengths[0] - pad_lengths[0] // 2),
                   (pad_lengths[1] // 2, pad_lengths[1] - pad_lengths[1] // 2),
                   (0, 0)]
    return np.pad(thumb, pad_lengths, mode='constant', constant_values=(1,))


def create_thumbnail(infile, thumbfile,
                     width=180, height=180,
                     xoffset=0, yoffset=0,
                     cx=0.5, cy=0.6, dpi=100):
    from matplotlib import image
    from matplotlib.pyplot import Figure

    baseout, extout = os.path.splitext(thumbfile)
    im = image.imread(infile)
    thumb = padded_thumbnail(im, (height, width), (yoffset, xoffset))

    extension = extout.lower()

    if extension == '.png':
        from matplotlib.backends.backend_agg \
            import FigureCanvasAgg as FigureCanvas
    elif extension == '.pdf':
        from matplotlib.backends.backend_pdf \
            import FigureCanvasPDF as FigureCanvas
    elif extension == '.svg':
        from matplotlib.backends.backend_svg \
            import FigureCanvasSVG as FigureCanvas
    else:
        raise ValueError("Can only handle extensions 'png', 'svg' or 'pdf'")

    fig = Figure(figsize=(float(width) / dpi, float(height) / dpi), dpi=dpi)
    canvas = FigureCanvas(fig)

    ax = fig.add_axes([0, 0, 1, 1], aspect='auto',
                      frameon=False, xticks=[], yticks=[])

    ax.imshow(thumb, aspect='auto', resample=True,
              interpolation='bilinear')
    fig.savefig(thumbfile, dpi=dpi)
    return fig
