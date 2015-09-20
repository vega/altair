from matplotlib import pyplot as plt
import matplotlib.markers as mmarkers
import pandas as pd
import numpy as np

from cycler import cycler

from .spec import SPEC


def _determine_col_name(agg_shelf, shelf):
    if 'bin' in agg_shelf and agg_shelf.bin:
        agg_coll = '{}_{}_bin'.format(agg_shelf.name, shelf)
    else:
        agg_coll = agg_shelf.name

    return agg_coll


def _vl_line(ax, encoding, data, pl_kw, agg_cols):
    x_name = _determine_col_name(encoding.x, 'x')
    y_name = _determine_col_name(encoding.y, 'y')
    df = data
    if 'aggregate' in encoding.x:
        _agg_cols = [c for c in agg_cols if c != x_name]
        df = _do_aggregate(encoding.x, df, _agg_cols)

    if 'aggregate' in encoding.y:
        _agg_cols = [c for c in agg_cols if c != y_name]
        df = _do_aggregate(encoding.y, df, _agg_cols)

    sty_dict = {}
    sty_dict.update(pl_kw)

    return ax.plot(x_name, y_name, data=df, **pl_kw)


def _vl_area(ax, encoding, data, pl_kw, agg_cols):
    ln, = _vl_line(ax, encoding, data, pl_kw, agg_cols)
    x_data = ln.get_xdata()
    y_data = ln.get_ydata()
    c = ln.get_color()
    area = ax.fill_between(x_data, y_data, color=c)
    return ln, area


def _vl_point(ax, encoding, data, pl_kw, agg_cols):
    pl_kw.setdefault('linestyle', 'none')
    if 'shape' in encoding:
        data_itr = _do_shape(encoding.shape, data, agg_cols)
    else:
        data_itr = [((None, data), {'marker': 'o'})]

    lns = []
    for (k, df), sty in data_itr:
        x_name = _determine_col_name(encoding.x, 'x')
        y_name = _determine_col_name(encoding.y, 'y')

        if 'aggregate' in encoding.x:
            _agg_cols = [c for c in agg_cols if c != x_name]
            df = _do_aggregate(encoding.x, df, _agg_cols)

        if 'aggregate' in encoding.y:
            _agg_cols = [c for c in agg_cols if c != y_name]
            df = _do_aggregate(encoding.y, df, _agg_cols)

        sty_dict = {}
        sty_dict.update(pl_kw)
        sty_dict.update(sty)
        ln = ax.plot(x_name, y_name,  data=df, **sty_dict)
        lns.extend(ln)

    return lns


def _vl_bar(ax, encoding, data, pl_kw, agg_cols):
    return ax.bar(encoding.x.name, encoding.y.name, data=data, **pl_kw)


def _do_shape(shape, data, agg_cols):
    """Sort out how to do shape

    Given an encoding + a possibly reduced DataFrame, return
    an iterator of (gb_key, DataFrame), style kwarg
    """
    filled = shape.filled
    shapes = mmarkers.MarkerStyle.filled_markers
    shape_col = _determine_col_name(shape, 'shape')
    if not filled:
        shapes = shapes + ('x',  '4', '3', '+', '2', '1')

    cyl = cycler('marker', shapes)

    if shape.type == 'Q':
        dig_data, bin_edges = _digitize_col(shape, data)
        data['{}_shape_bin'.format(shape.name)] = dig_data

    if 'aggregate' in shape:
        _agg_cols = [c for c in agg_cols if c != shape_col]
        data = _do_aggregate(shape, data, _agg_cols)

    fill = 'full' if filled else 'none'
    cyl *= cycler('fillstyle', (fill, ))

    gb = data.groupby(shape_col)

    for df, sty in zip(gb, cyl):
        yield df, sty


def _do_aggregate(shelf, data, by_keys):

    agg_method = shelf.aggregate

    binned = data.groupby(by_keys)
    agg_func_name = _AGG_MAP[agg_method]

    data = getattr(binned, agg_func_name)().reset_index()
    return data


def _do_binning(vls, data, bin_key, plot_kwargs):
    encoding = vls.encoding
    shelf = getattr(encoding, bin_key)
    dig, bin_edges = _digitize_col(shelf, data)
    data['{}_{}_bin'.format(shelf.name, bin_key)] = dig
    if vls.marktype == 'bar':
        plot_kwargs['width'] = np.mean(np.diff(bin_edges)) * .9
        plot_kwargs['align'] = 'center'

    return data


def _digitize_col(bin_encoding, data):
    x_name = bin_encoding.name
    d_min, d_max = data[x_name].min(), data[x_name].max()
    bin_count = bin_encoding.bin
    if isinstance(bin_count, bool):
        bin_count = 3
    bin_count = int(bin_count)

    # add one to bin count as we are generating edges here
    bin_edges = np.linspace(d_min, d_max, bin_count + 1, endpoint=True)
    centers = (bin_edges[1:] + bin_edges[:-1]) / 2
    dig = np.digitize(data[x_name], bin_edges, right=True) - 1
    valid_mask = (-1 < dig) * (dig < len(centers))
    ret = np.zeros_like(dig, dtype='float')
    ret[valid_mask] = centers[dig[valid_mask]]
    ret[~valid_mask] = np.nan

    return ret, bin_edges


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
    shelves = ('row', 'col', 'shape', 'size', 'color', 'y', 'x')
    # TODO these seem to be missing from the api.py
    # 'detail', 'text')
    used_cols = list(set(getattr(encoding, k).name
                         for k in shelves if k in encoding))
    data = data[used_cols]

    x_binned = 'bin' in encoding.x and encoding.x.bin
    y_binned = 'bin' in encoding.y and encoding.y.bin
    if x_binned and y_binned:
        raise NotImplementedError("Double binning not done yet")
    agg_cols = []
    for sh in shelves:
        if sh not in encoding:
            continue
        shelf = getattr(encoding, sh)
        if 'bin' in shelf and shelf.bin:
            data = _do_binning(vls, data, sh, plot_kwargs)
        agg_cols.append(_determine_col_name(shelf, sh))

    agg_cols = list(set(agg_cols))

    data = data.dropna()

    plot_func = _MARK_DISPATCHER[vls.marktype]

    has_row = 'row' in encoding
    has_col = 'col' in encoding

    ax_map = {}
    ax_list = None

    if has_col and has_row:
        # sort out the names with respect to binning
        col_name = _determine_col_name(encoding.col, 'col')
        row_name = _determine_col_name(encoding.row, 'row')
        if 'aggregate' in encoding.row:
            _agg_cols = [c for c in agg_cols if c != row_name]
            data = _do_aggregate(encoding.row, data, _agg_cols)

        if 'aggregate' in encoding.col:
            _agg_cols = [c for c in agg_cols if c != col_name]
            data = _do_aggregate(encoding.col, data,  _agg_cols)

        row_labels = data[row_name].unique()
        col_labels = data[col_name].unique()
        grid_keys = [(_['row'], _['col'])
                     for _ in (cycler('row', row_labels) *
                               cycler('col', col_labels))]
        col_num, row_num = len(col_labels), len(row_labels)
        facet_iter = data.groupby([row_name, col_name])
    elif has_col:
        col_name = _determine_col_name(encoding.col, 'col')

        if 'aggregate' in encoding.col:
            _agg_cols = [c for c in agg_cols if c != col_name]
            data = _do_aggregate(encoding.col, data, _agg_cols)

        col_labels = data[col_name].unique()
        col_num, row_num = len(col_labels), 1
        grid_keys = list(col_labels)
        facet_iter = data.groupby(col_name)
    elif has_row:
        row_name = _determine_col_name(encoding.row, 'row')
        if 'aggregate' in encoding.row:
            _agg_cols = [c for c in agg_cols if c != row_name]
            data = _do_aggregate(encoding.row, data, _agg_cols)

        row_labels = data[row_name].unique()
        col_num, row_num = 1, len(row_labels)
        grid_keys = list(row_labels)
        facet_iter = data.groupby(row_name)
    else:
        grid_keys = [None, ]
        col_num, row_num = 1, 1

        def _inner():
            yield None, data
        facet_iter = _inner()

    fig, ax_list = plt.subplots(row_num, col_num,
                                sharex=True, sharey=True,
                                squeeze=False)
    for k, ax in zip(grid_keys, ax_list.ravel()):
        ax_map[k] = ax
        ax.set_prop_cycle(cycler('color', 'k'))
        if 'x' in encoding and ax.rowNum == row_num - 1:
            ax.set_xlabel(encoding.x.name)
        if 'y' in encoding and ax.colNum == 0:
            ax.set_ylabel(encoding.y.name)

    rets = {}
    for k, df in facet_iter:
        ax = ax_map[k]
        _r = plot_func(ax, encoding, df, plot_kwargs, agg_cols)
        rets[k] = _r
        if k:
            ax.set_title(repr(k))

    return rets, ax_map


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
