from __future__ import annotations

"""
Deviation ellipse
-----------------------
This example shows bivariate deviation ellipses of petal length and width of three iris species.
"""

from typing import Literal

import numpy as np
import pandas as pd
from scipy.stats import f as ssf

import altair as alt
from vega_datasets import data


def np_ellipse(
    arr: np.ndarray[tuple[int, int], np.dtype[np.float64]],
    conf_level: float = 0.95,
    method: Literal["deviation", "error"] = "deviation",
    segments: int = 100,
):
    """
    Arguments:
        arr:  2D numpy array with 2 columns
        level: confidence level
        method: either 'deviation' (swarning data) or 'error (swarning the mean)'
        segments: number of points describing the ellipse.
    """  # noqa: D205
    n_elements = len(arr)
    # TODO: 
    # - dfn?
    # - dfd?
    # - ssf.ppf?
    #   - Percent point function (inverse of `cdf`) at q of the given RV.
    dfn = 2
    dfd = n_elements - 1
    deviation = np.sqrt(2 * ssf.ppf(conf_level, dfn=dfn, dfd=dfd))
    if method == "deviation":
        radius = deviation
    elif method == "error":
        radius = deviation / np.sqrt(n_elements)
    else:
        msg = "Method should be either 'deviation' or 'error'."
        raise ValueError(msg)
    angles = (np.arange(0, segments + 1)) * 2 * np.pi / segments
    circle = np.vstack((np.cos(angles), np.sin(angles))).T
    center = np.mean(arr, axis=0)
    cov_mat = np.cov(arr.T)
    # TODO: Figure out why so many transpositions
    ellipse = center + (radius * np.dot(circle, np.linalg.cholesky(cov_mat).T).T).T
    return ellipse


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
points = alt.Chart(source).mark_circle().encode(x, y, color)
lines = (
    alt.Chart(ellipse)
    .mark_line(filled=True, fillOpacity=0.2)
    .encode(x, y, color, order="index")
)

chart = lines + points
chart