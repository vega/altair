"""
Horizon Graph
-------------
This example shows how to make a Horizon Graph with 2 layers. (See https://idl.cs.washington.edu/papers/horizon/ for more details on Horizon Graphs.)
"""
# category: area charts
import numpy as np
import pandas as pd
import altair as alt


def horizon(
    source: pd.DataFrame,
    x: str = "x",
    y: str = "y",
    pos_color: str = "blue",
    neg_color: str = "firebrick",
) -> alt.Chart:
    """Plot a horiozon timeseries graph with two layers and offset negative values.

    See https://idl.cs.washington.edu/papers/horizon/ for more details on Horizon Graphs. 
    Your timeseries should be zero-centered before plotting.  

    Args:
        source: the data to plot, in long format (i.e. a x column, and a y column)
        x: the column name containing the 'x' data
        y: the column name containing the 'y' data
        pos_color, neg_color: what color to shade the positive and negative parts of the 
            timeseries
    """
    # We're just splitting into four layers here, using the same split for pos and
    # negative.
    ysplit = max(source[y].max(), abs(source[y].min())) / 2

    # Generate the layers
    charts = []
    for offset in (-1, 0, 1, 2):
        # Set arguments to mark_area depending on whether we're plotting the positive
        # or negative part of the graph
        if offset <= 0:
            area_kwargs = {"color": pos_color}
        else:
            area_kwargs = {"color": neg_color, "y2": ysplit}

        # Generate each layer seperately and append
        chart = (
            alt.Chart(source, height=20)
            .mark_area(clip=True, interpolate="monotone", **area_kwargs)
            .encode(
                alt.X("x", scale=alt.Scale(zero=False, nice=False), axis=None),
                alt.Y(
                    "shifted:Q",
                    scale=alt.Scale(domain=[0, ysplit]),
                    axis=None,
                    title="y",
                ),
                opacity=alt.value(0.36),
            )
            .transform_calculate("shifted", alt.datum.y + offset * ysplit)
        )
        charts.append(chart)

    return alt.layer(*charts)


# Make up some data to plot - sine waves with random noise and a random trend
charts = []
for _ in range(15):
    xs = np.linspace(-15, 15, 300)
    source = pd.DataFrame(
        {
            "x": xs,
            "y": np.sin(xs)
            + 0.4 * np.random.normal(0, 1) * xs
            + np.random.uniform(-0.5, 0.5, size=len(xs)),
        }
    )
    charts.append(horizon(source))

# Stick charts into a vertical frame
alt.vconcat(*charts).resolve_scale(x="shared").configure_view(strokeOpacity=0)
