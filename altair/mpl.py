from matplotlib import pyplot as plt
import pandas as pd
from .spec import SPEC


def _vl_line(ax, encoding, data):
    return ax.plot(encoding.x.name, encoding.y.name, data=data)


def _vl_area(ax, encoding, data):
    ln, = ax.plot(encoding.x.name, encoding.y.name, data=data)
    area = ax.fill_between(encoding.x.name, encoding.y.name, data=data)
    return ln, area


def _vl_point(ax, encoding, data):
    ln, = ax.plot(encoding.x.name, encoding.y.name, data=data,
                  linestyle='none', marker='o')
    return ln,


def _vl_bar(ax, encoding, data):
    return ax.bar(encoding.x.name, encoding.y.name, data=data)


def render(vls):
    """Render a vega-lite spec using matplotlib

    Parameters
    ----------
    vls : dict
        A dictionary complying with the vega-lite spec

    Returns
    -------
    fig : Figure
        The figure created

    ax_list : list
        The list of axes created

    arts : dict
        Dictionary keyed on Axes of the artists created
    """

    encoding = vls.encoding
    data = vls.data
    plot_func = _MARK_DISPATCHER[vls.marktype]
    fig, ax = plt.subplots()

    return plot_func(ax, encoding, data)


_MARK_DISPATCHER = {'area': _vl_area,      # fill below line
                    'bar': _vl_bar,        # bar
                    'circle': None,        # ??
                    'line': _vl_line,      # line
                    'point': _vl_point,    # scatter
                    'square': None,        # ??
                    'text': None,          # ??
                    'tick': None}          # ??
