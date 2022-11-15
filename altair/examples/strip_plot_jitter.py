"""
Strip Plot with Jitter
---------
In this chart, we encode the ``Major_Genre`` column from the ``movies`` dataset in the ``y``-channel. In the default presentation of this data, it would be difficult to gauge the relative frequencies with which different values occur because there would be so much overlap. To address this, we use the ``yOffset`` channel to incorporate a random offset (jittering). The example is shown twice, on the left side using normally distributed and on the right side using uniformally distributed jitter.
"""
# category: distributions
import altair as alt
from vega_datasets import data

source = data.movies.url

gaussian_jitter = alt.Chart(source, title='Normally distributed jitter').mark_circle(size=8).encode(
    y="Major_Genre:N",
    x="IMDB_Rating:Q",
    yOffset="jitter:Q",
    color=alt.Color('Major_Genre:N', legend=None)
).transform_calculate(
    # Generate Gaussian jitter with a Box-Muller transform
    jitter="sqrt(-2*log(random()))*cos(2*PI*random())"
)

uniform_jitter = gaussian_jitter.transform_calculate(
    # Generate uniform jitter
    jitter='random()'
).encode(
    y=alt.Y('Major_Genre:N', axis=None)
).properties(
    title='Uniformly distributed jitter'
)

(gaussian_jitter | uniform_jitter).resolve_scale(yOffset='independent')
