"""
Dendrogram of Hierarchical Clustering
-------------------------------------
This is a dendrogram from the result of a hierarchical clustering. It's based on the example from
https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html
"""
# category: case studies

import pandas as pd
import altair as alt

den = {
    'dcoord': [[0.0, 0.8187388676087964, 0.8187388676087964, 0.0],
  [0.0, 1.105139508538779, 1.105139508538779, 0.0],
  [0.8187388676087964,
   1.3712698320830048,
   1.3712698320830048,
   1.105139508538779],
  [0.0, 0.9099819926189507, 0.9099819926189507, 0.0],
  [0.0, 1.2539936203984452, 1.2539936203984452, 0.0],
  [0.9099819926189507,
   1.9187528699821954,
   1.9187528699821954,
   1.2539936203984452],
  [1.3712698320830048,
   3.828052620290243,
   3.828052620290243,
   1.9187528699821954],
  [0.0, 1.7604450194955439, 1.7604450194955439, 0.0],
  [0.0, 1.845844754344974, 1.845844754344974, 0.0],
  [1.7604450194955439,
   4.847708507921838,
   4.847708507921838,
   1.845844754344974],
  [0.0, 2.8139388316471536, 2.8139388316471536, 0.0],
  [0.0, 2.8694176394568705, 2.8694176394568705, 0.0],
  [2.8139388316471536,
   6.399406819518539,
   6.399406819518539,
   2.8694176394568705],
  [4.847708507921838,
   12.300396052792589,
   12.300396052792589,
   6.399406819518539],
  [3.828052620290243,
   32.44760699959244,
   32.44760699959244,
   12.300396052792589]],
 'icoord': [[5.0, 5.0, 15.0, 15.0],
  [25.0, 25.0, 35.0, 35.0],
  [10.0, 10.0, 30.0, 30.0],
  [45.0, 45.0, 55.0, 55.0],
  [65.0, 65.0, 75.0, 75.0],
  [50.0, 50.0, 70.0, 70.0],
  [20.0, 20.0, 60.0, 60.0],
  [85.0, 85.0, 95.0, 95.0],
  [105.0, 105.0, 115.0, 115.0],
  [90.0, 90.0, 110.0, 110.0],
  [125.0, 125.0, 135.0, 135.0],
  [145.0, 145.0, 155.0, 155.0],
  [130.0, 130.0, 150.0, 150.0],
  [100.0, 100.0, 140.0, 140.0],
  [40.0, 40.0, 120.0, 120.0]],
 'ivl': [
     '(7)', '(8)', '41', '(5)', '(10)', '(7)', '(4)', '(8)', '(9)', '(15)', '(5)', '(7)', '(4)', '(22)', '(15)', '(23)'
     ],
}

def get_leaf_loc(den):
    """
    Get the location of the leaves
    """
    _from = int(np.array(den["icoord"]).min())
    _to = int(np.array(den["icoord"]).max() + 1)
    return range(_from, _to, 10)

def get_df_coord(den):
    """
    Get coordinate dataframe.
    """
    # if you view the dendrogram as a collection of upside-down "U" shapes, then
    # we can regard the 4 corners of the upside-down "U" as points 1, 2, 3 and 4.
    cols_xk = ["xk1", "xk2", "xk3", "xk4"]
    cols_yk = ["yk1", "yk2", "yk3", "yk4"]

    df_coord = pd.merge(
        pd.DataFrame(den["icoord"], columns=cols_xk),
        pd.DataFrame(den["dcoord"], columns=cols_yk),
        left_index=True,
        right_index=True
    )
    return df_coord

source = get_df_coord(den)
base = alt.Chart(source)

# the U shape is composed of a shoulder plus two arms
shoulder_encoding = [
        alt.X("xk2:Q", title=""),
        alt.X2("xk3:Q"),
        alt.Y("yk2:Q", title="")
]
arm1_encoding = [alt.X("xk1:Q"), alt.Y("yk1:Q"), alt.Y2("yk2:Q")]
arm2_encoding = [alt.X("xk3:Q"), alt.Y("yk3:Q"), alt.Y2("yk4:Q")]

shoulder = base.encode(*shoulder_encoding).mark_rule()
arm1 = base.encode(*arm1_encoding).mark_rule()
arm2 = base.encode(*arm2_encoding).mark_rule()

chart_den = shoulder + arm1 + arm2

df_text = pd.DataFrame(dict(labels=den["ivl"], x=get_leaf_loc(den)))
df_text

chart_text = alt.Chart(
    df_text
).mark_text(
    dy=0, angle=0, align="center"
).encode(
    x = alt.X("x:Q", axis={"grid":False, "title":"Number of points in nodes"}),
    text = alt.Text("labels:N")
)

(
    (chart_den & chart_text)
    .resolve_scale(x="shared")
    .configure(padding={"top":10,"left":10})
    .configure_concat(spacing=0)
    .configure_axis(labels=False, ticks=False, grid=False)
    .properties(title="Hierarchical Clustering Dendrogram")
)