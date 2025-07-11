"""
Interactive Selection of Columns
================================
This example shows how columns can be selected interactively
by accessing the values from selector widgets,
and then compute the difference of the selected columns.
It also illustrates how to use `indexof` to filter
columns based on active selection values.
"""
# category: interactive charts

import pandas as pd
import numpy as np
import altair as alt


# Create timeseries data
rng = np.random.default_rng(905)
ex_ts = pd.DataFrame(
    rng.random((10, 4)),
    columns=['a', 'b', 'c', 'd'],
).assign(
    date=pd.date_range(
        start=pd.to_datetime('2022-02-22')-pd.Timedelta(9, unit='D'),
        end=pd.to_datetime('2022-02-22')).strftime('%Y-%m-%d'),
)

# Create heatmap with selection
select_x = alt.selection_point(fields=['level_0'], name='select_x', value='b')
select_y = alt.selection_point(fields=['level_1'], name='select_y', value='d')
heatmap = alt.Chart(
    ex_ts.drop(columns='date').corr().stack().reset_index().rename(columns={0: 'correlation'}),
    title='Click a tile to compare timeseries',
    height=250,
    width=250,
).mark_rect().encode(
    alt.X('level_0').title(None),
    alt.Y('level_1').title(None),
    alt.Color('correlation').scale(domain=[-1, 1], scheme='blueorange'),
    opacity=alt.when(select_x, select_y).then(alt.value(1)).otherwise(alt.value(0.4)),
).add_params(
    select_x, select_y
)

# Create chart with individual lines/timeseries
base = alt.Chart(
    ex_ts.melt(
        id_vars='date',
        var_name='category',
        value_name='value',
    ),
    height=100,
    width=300,
    title='Individual timeseries',
)
lines = base.transform_filter(
    # If the category is not in the selected values, the returned index is -1
    'indexof(datum.category, select_x.level_0) !== -1'
   '| indexof(datum.category, select_y.level_1) !== -1'
).mark_line().encode(
    alt.X('date:T').axis(labels=False).title(None),
    alt.Y('value').scale(domain=(0, 1)),
    alt.Color('category').legend(orient='top', offset=-20).title(None)
)

# Create chart with difference between lines/timeseries
dynamic_title = alt.Title(alt.expr(f'"Difference " + {select_x.name}.level_0 + " - " + {select_y.name}.level_1'))
# We pivot transform to get each category as a column
lines_diff = base.transform_pivot(
    'category', 'value', groupby=['date']
# In the calculate transform we use the values from the selection to subset the columns to subtract
).transform_calculate(
    difference = f'datum[{select_x.name}.level_0] - datum[{select_y.name}.level_1]'
).mark_line(color='grey').encode(
    alt.X('date:T').axis(format='%Y-%m-%d').title(None),
    alt.Y('difference:Q').scale(domain=(-1, 1)),
).properties(
    title=dynamic_title
)

# Layout the charts
(lines & lines_diff) | heatmap
