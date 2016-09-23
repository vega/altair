import os

import numpy as np

try:
    import matplotlib
except ImportError:
    matplotlib = None
else:
    matplotlib.use('Agg')  # don't display plots


def padded_thumbnail(im, size=(200, 200), offset=(0, 0), zoom=1):
    offset = list(offset)
    for i in range(len(offset)):
        if 0 <= offset[i] < 1:
            offset[i] = int(offset[i] * im.shape[i])
    size = [int(zoom * s) for s in size]

    thumb = im[offset[0]: offset[0] + size[0],
               offset[1]: offset[1] + size[1]]

    pad_lengths = (size[0] - thumb.shape[0], size[1] - thumb.shape[1])
    pad_lengths = [(pad_lengths[0] // 2, pad_lengths[0] - pad_lengths[0] // 2),
                   (pad_lengths[1] // 2, pad_lengths[1] - pad_lengths[1] // 2),
                   (0, 0)]
    return np.pad(thumb, pad_lengths, mode='constant', constant_values=(1,))


def create_thumbnail(infile, thumbfile,
                     width=180, height=180,
                     xoffset=0, yoffset=0, zoom=1,
                     cx=0.5, cy=0.6, dpi=100):
    from matplotlib import image
    from matplotlib.pyplot import Figure

    baseout, extout = os.path.splitext(thumbfile)
    im = image.imread(infile)
    thumb = padded_thumbnail(im, (height, width), (yoffset, xoffset), zoom)

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
