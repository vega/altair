"""
Stem and Leaf Plot
------------------
This example shows how to make a stem and leaf plot.
"""
# category: other charts
import altair as alt

# Generating random data
alt.pd.np.random.seed(42)
df = alt.pd.DataFrame({'samples': alt.pd.np.random.normal(50, 15, 100).astype(int).astype(str)})

# Splitting stem and leaf
df['stem'] = df['samples'].str[:-1]
df['leaf'] = df['samples'].str[-1]

df = df.sort_values(by=['stem', 'leaf'])

# Determining leaf position
df['position'] = df.groupby('stem').cumcount().add(1)

# Creating stem and leaf plot
alt.Chart(df).mark_text(
    align='left',
    baseline='middle',
    dx=-5
).encode(
    alt.X('position:Q',
        axis=alt.Axis(title='', ticks=False, labels=False, grid=False)
    ),
    alt.Y('stem:N', axis=alt.Axis(title='', tickSize=0)),
    text='leaf:N'
).configure_axis(
    labelFontSize=20
).configure_text(
    fontSize=20
)
