.. currentmodule:: altair

.. _user-guide-extent-transform:

Extent
~~~~~~
The extent transform can be used to find the extent of a field and stores the result in a :ref:`parameter <parameters>`.

As an example, consider the following dataset:

.. altair-plot::
    :output: none
   
    import pandas as pd
    df = pd.DataFrame(
        [
            {"a": "A", "b": 28},
            {"a": "B", "b": 55},
            {"a": "C", "b": 43},
            {"a": "D", "b": 91},
            {"a": "E", "b": 81},
            {"a": "F", "b": 53},
            {"a": "G", "b": 19},
            {"a": "H", "b": 87},
            {"a": "I", "b": 52},
        ]
    )
    
We can use the extent transform to extract the minimum and maximum values of column ``b`` and then use those values to place rules:

.. altair-plot::
    
    import altair as alt
    
    base = alt.Chart(df, title="A Simple Bar Chart with Lines at Extents").transform_extent(
        extent="b", param="b_extent"
    )
    bars = base.mark_bar().encode(x="b", y="a")
    lower_extent_rule = base.mark_rule(stroke="firebrick").encode(
        x=alt.value(alt.expr("scale('x', b_extent[0])"))
    )
    upper_extent_rule = base.mark_rule(stroke="firebrick").encode(
        x=alt.value(alt.expr("scale('x', b_extent[1])"))
    )
    bars + lower_extent_rule + upper_extent_rule


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_extent` method is built on the :class:`~ExtentTransform`
class, which has the following options:

.. altair-object-table:: altair.ExtentTransform
