from matplotlib import pyplot as plt
import matplotlib.markers as mmarkers
import pandas as pd
import numpy as np

from cycler import cycler

from .spec import SPEC


def _vl_line(ax, encoding, data, pl_kw):
    return ax.plot(encoding.x.name, encoding.y.name, data=data,
                   **pl_kw)


def _vl_area(ax, encoding, data, pl_kw):
    ln, = ax.plot(encoding.x.name, encoding.y.name, data=data, **pl_kw)
    area = ax.fill_between(encoding.x.name, encoding.y.name,
                           data=data, **pl_kw)
    return ln, area


def _vl_point(ax, encoding, data, pl_kw):
    pl_kw.setdefault('linestyle', 'none')
    if 'shape' in encoding:
        data_itr = _do_shape(encoding.shape, data)
    else:
        data_itr = [((None, data), {'marker': 'o'})]

    lns = []
    for (k, df), sty in data_itr:
        sty_dict = {}
        sty_dict.update(pl_kw)
        sty_dict.update(sty)
        ln = ax.plot(encoding.x.name, encoding.y.name, data=df, **sty_dict)
        lns.extend(ln)

    return lns


def _vl_bar(ax, encoding, data, pl_kw):
    return ax.bar(encoding.x.name, encoding.y.name, data=data, **pl_kw)


def _do_shape(shape, data):
    """Sort out how to do shape

    Given an encoding + a possibly reduced DataFrame, return
    an iterator of (gb_key, DataFrame), style kwarg
    """
    filled = shape.filled
    shapes = mmarkers.MarkerStyle.filled_markers

    if not filled:
        shapes = shapes + ('x',  '4', '3', '+', '2', '1')

    cyl = cycler('marker', shapes)

    if shape.type == 'Q':
        data, bin_edges = _digitize_col(shape, data)

    fill = 'full' if filled else 'none'
    cyl *= cycler('fillstyle', (fill, ))

    gb = data.groupby(shape.name)

    for df, sty in zip(gb, cyl):
        yield df, sty


def _do_aggregate(encoding, data, agg_key, by_key):
    agg_coll = getattr(encoding, agg_key).name
    by_coll = getattr(encoding, by_key).name
    agg_method = getattr(encoding, agg_key).aggregate
    binned = data[agg_coll].groupby(data[by_coll])
    agg_func_name = _AGG_MAP[agg_method]

    data = getattr(binned, agg_func_name)().reset_index()
    return data


def _do_binning(vls, data, bin_key, plot_kwargs):
    encoding = vls.encoding
    data, bin_edges = _digitize_col(getattr(encoding, bin_key), data)
    if vls.marktype == 'bar':
        plot_kwargs['width'] = np.mean(np.diff(bin_edges)) * .9
        plot_kwargs['align'] = 'center'

    return data


def _digitize_col(bin_encoding, data):
    x_name = bin_encoding.name
    d_min, d_max = data[x_name].min(), data[x_name].max()
    bin_count = bin_encoding.bin
    if isinstance(bin_count, bool):
        bin_count = 15
    bin_count = int(bin_count)

    # add one to bin count as we are generating edges here
    bin_edges = np.linspace(d_min, d_max, bin_count + 1, endpoint=True)
    centers = (bin_edges[1:] + bin_edges[:-1]) / 2
    dig = np.digitize(data[x_name], bin_edges, right=True) - 1
    valid_mask = (-1 < dig) * (dig < len(centers))
    data[x_name][valid_mask] = centers[dig[valid_mask]]
    data[x_name][~valid_mask] = np.nan

    return data, bin_edges


def render(vls, data=None):
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
    plot_kwargs = {}
    encoding = vls.encoding
    if data is None:
        data = vls.data
    data = pd.DataFrame(data)

    # x_binned = 'bin' in encoding.x and encoding.x.bin
    # y_binned = 'bin' in encoding.y and encoding.y.bin
    x_binned = True and encoding.x.bin
    y_binned = True and encoding.y.bin
    if x_binned and y_binned:
        raise NotImplementedError("Double binning not done yet")
    if x_binned:
        data = _do_binning(vls, data, 'x', plot_kwargs)
    elif y_binned:
        data = _do_binning(vls, data, 'y', plot_kwargs)

    if encoding.y.aggregate:
        data = _do_aggregate(encoding, data, 'y', 'x')

    if encoding.x.aggregate:
        data = _do_aggregate(encoding, data, 'x', 'y')

    plot_func = _MARK_DISPATCHER[vls.marktype]
    fig, ax = plt.subplots()
    ax.set_prop_cycle(cycler('color', 'k'))
    ax.set_xlabel(encoding.x.name)
    ax.set_ylabel(encoding.y.name)
    return plot_func(ax, encoding, data, plot_kwargs)


_MARK_DISPATCHER = {'area': _vl_area,      # fill below line
                    'bar': _vl_bar,        # bar
                    'circle': None,        # ??
                    'line': _vl_line,      # line
                    'point': _vl_point,    # scatter
                    'square': None,        # ??
                    'text': None,          # ??
                    'tick': None}          # ??

_AGG_MAP = {"avg": 'mean',
            "sum": 'sum',
            "min": 'min',
            "max": 'max',
            "count": 'count'}
