"""
Deviation ellipse
-----------------------
This example shows bivariate deviation ellipses of petal length and width of three iris species.
"""

import numpy as np
import pandas as pd
from scipy.stats import f as ssf
import altair as alt
from vega_datasets import data

iris = data.iris()

def ellipse(X, level=0.95, method='deviation', npoints=100):
    """
    X: data, 2D numpy array with 2 columns
    level: confidence level
    method: either 'deviation' (swarning data) or 'error (swarning the mean)'
    npoints: number of points describing the ellipse
    """
    cov_mat = np.cov(X.T)
    dfd = X.shape[0]-1
    dfn = 2
    center = np.apply_along_axis(np.mean, arr=X, axis=0) # np.mean(X, axis=0)
    if method == 'deviation':
        radius = np.sqrt(2 * ssf.ppf(q=level, dfn=dfn, dfd=dfd))
    elif method == 'error':
        radius = np.sqrt(2 * ssf.ppf(q=level, dfn=dfn, dfd=dfd)) / np.sqrt(X.shape[0])
    else:
        raise ValueError("Method should be either 'deviation' or 'error'.")
    angles = (np.arange(0,npoints+1)) * 2 * np.pi/npoints
    circle = np.vstack((np.cos(angles), np.sin(angles))).T
    ellipse = center + (radius * np.dot(circle, np.linalg.cholesky(cov_mat).T).T).T
    return ellipse

columns = ['petalLength', 'petalWidth']
petal_ellipse = []
for species in iris.species.unique():
    ell_df = pd.DataFrame(ellipse(X=iris.loc[iris.species == species, columns].as_matrix()),
                                      columns = columns)
    ell_df['species'] = species
    petal_ellipse.append(ell_df)

petal_ellipse = pd.concat(petal_ellipse, axis=0).reset_index()

chart_deviation = alt.Chart(petal_ellipse).mark_line().\
    encode(
        x=alt.X('petalLength', scale=alt.Scale(zero=False)),
        y=alt.Y('petalWidth', scale=alt.Scale(zero=False)),
        color='species',
        order='index')
# works only if chart_deviation is printed here
# chart_deviation

chart_points = alt.Chart(iris).mark_point().\
    encode(
        x=alt.X('petalLength', scale=alt.Scale(zero=False)),
        y=alt.Y('petalWidth', scale=alt.Scale(zero=False)),
        color='species')

chart = chart_points + chart_deviation
chart
