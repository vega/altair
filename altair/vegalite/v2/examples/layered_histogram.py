"""
Layered Histogram
=================
This example shows how to use opacity to make a layered histogram in Altair.
"""
# category: histograms
import altair as alt

alt.pd.np.random.seed(42)

# Generating Data
df = alt.pd.DataFrame({'Trial A': alt.pd.np.random.normal(0, 0.8, 1000),
                   'Trial B': alt.pd.np.random.normal(-2, 1, 1000),
                   'Trial C': alt.pd.np.random.normal(3, 2, 1000)})

# Tidying Data
df = alt.pd.melt(df, id_vars=df.index.name,
             value_vars=df.columns,
             var_name='Experiment',
             value_name='Measurement')

alt.Chart(df).mark_area(
    opacity=0.3,
    interpolate='step'
).encode(
    alt.X('Measurement', bin=alt.Bin(maxbins=100)),
    alt.Y('count()', stack=None),
    alt.Color(
        'Experiment',
        scale=alt.Scale(range=['#0000ff', '#008000', '#ff0000'])
    )
)
