"""
Deviation ellipse
-----------------
This example shows bivariate deviation ellipses of petal length and width of three iris species.
"""

# category: distributions
from __future__ import annotations

from typing import Literal

import numpy as np
import pandas as pd
from scipy.stats import f as F

import altair as alt
from vega_datasets import data


def np_ellipse(
    arr: np.ndarray[tuple[int, int], np.dtype[np.float64]],
    conf_level: float = 0.95,
    method: Literal["deviation", "error"] = "deviation",
    segments: int = 50,
):
    """
    Calculate confidence interval ellipse.

    Parameters
    ----------
    arr
        numpy array with 2 columns
    conf_level
        lower tail probability
    method
        either 'deviation' (swarning data) or 'error (swarning the mean)'
    segments
        number of points describing the ellipse.
    """
    n_elements = len(arr)
    # Degrees of freedom of the chi-squared distribution in the **numerator**
    dfn = 2
    # Degrees of freedom of the chi-squared distribution in the **denominator**
    dfd = n_elements - 1
    # Percent point function at `conf_level` of an F continuous random variable
    quantile = F.ppf(conf_level, dfn=dfn, dfd=dfd)
    deviation = np.sqrt(2 * quantile)
    if method == "deviation":
        radius = deviation
    elif method == "error":
        radius = deviation / np.sqrt(n_elements)
    else:
        msg = "Method should be either 'deviation' or 'error'."
        raise ValueError(msg)
    angles = np.arange(0, segments) * 2 * np.pi / segments
    circle = np.column_stack((np.cos(angles), np.sin(angles)))
    center = np.mean(arr, axis=0)
    cov_mat = np.cov(arr, rowvar=False)
    return center + radius * (circle @ np.linalg.cholesky(cov_mat).T)


def pd_ellipse(
    df: pd.DataFrame, col_x: str, col_y: str, col_group: str
) -> pd.DataFrame:
    cols = col_x, col_y
    groups = []
    # TODO: Rewrite in a more readable way
    categories = df[col_group].unique()
    for category in categories:
        sliced = df.loc[df[col_group] == category, cols]
        ell_df = pd.DataFrame(np_ellipse(sliced.to_numpy()), columns=cols) # type: ignore
        ell_df[col_group] = category
        groups.append(ell_df)
    return pd.concat(groups).reset_index()


col_x = "petalLength"
col_y = "petalWidth"
col_group = "species"
x = alt.X(col_x, scale=alt.Scale(zero=False))
y = alt.Y(col_y, scale=alt.Scale(zero=False))
color = alt.Color(col_group)

source = data.iris()
ellipse = pd_ellipse(source, col_x=col_x, col_y=col_y, col_group=col_group)
points = alt.Chart(source).mark_circle(size=50, tooltip=True).encode(x, y, color)
lines = (
    alt.Chart(ellipse)
    .mark_line(filled=True, fillOpacity=0.2)
    .encode(x, y, color, order="index")
)

chart = (lines + points).properties(height=500, width=500)
chart