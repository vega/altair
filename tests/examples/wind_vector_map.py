"""
Wind Vector Map
---------------
An example showing a vector array map showing wind speed and direction using ``wedge``
as shape for ``mark_point`` and ``angle`` encoding for the wind direction.
This is adapted from this corresponding Vega-Lite Example:
`Wind Vector Map <https://vega.github.io/vega-lite/examples/point_angle_windvector.html>`_
with an added base map.
"""
# category: maps
import altair as alt
from vega_datasets import data

df_wind = data.windvectors()
data_world = alt.topo_feature(data.world_110m.url, "countries")

wedge = (
    alt.Chart(df_wind)
    .mark_point(shape="wedge", filled=True)
    .encode(
        latitude="latitude",
        longitude="longitude",
        color=alt.Color(
            "dir", scale=alt.Scale(domain=[0, 360], scheme="rainbow"), legend=None
        ),
        angle=alt.Angle("dir", scale=alt.Scale(domain=[0, 360], range=[180, 540])),
        size=alt.Size("speed", scale=alt.Scale(rangeMax=500)),
    )
    .project("equalEarth")
)

xmin, xmax, ymin, ymax = (
    df_wind.longitude.min(),
    df_wind.longitude.max(),
    df_wind.latitude.min(),
    df_wind.latitude.max(),
)

# clockwise, left-hand-rule
extent = [
    {
        "type": "Polygon",
        "coordinates": (
            (
                (xmax, ymax),
                (xmax, ymin),
                (xmin, ymin),
                (xmin, ymax),
                (xmax, ymax),
            ),
        ),
    }
]

# use fit combined with clip=True
base = (
    alt.Chart(data_world)
    .mark_geoshape(clip=True, fill="lightgray", stroke="black", strokeWidth=0.5)
    .project(type="equalEarth", fit=extent)
)

base + wedge