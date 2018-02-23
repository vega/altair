import altair as alt
from vega_datasets import data

source = data.jobs.dataframe()

base = source[source['job'] == 'Accountant / Auditor']
    
chart = alt.Chart(base).mark_line().encode(
    x='year:T',
    y=alt.Y('perc', axis=alt.Axis(format='%')),
    color='sex')
