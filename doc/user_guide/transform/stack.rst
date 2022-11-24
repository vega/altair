.. currentmodule:: altair

.. _user-guide-stack-transform:

Stack
~~~~~
The stack transform allows you to compute values associated with stacked versions
of encodings. For example, consider this stacked bar chart:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).mark_bar().encode(
        column='year:O',
        x='yield:Q',
        y='variety:N',
        color='site:N'
    ).properties(width=220)

Implicitly, this data is being grouped and stacked, but what if you would like to
access those stacked values directly?
We can construct that same chart manually using the stack transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.barley()

    alt.Chart(source).transform_stack(
        stack='yield',
        as_=['yield_1', 'yield_2'],
        groupby=['year', 'variety'],
        sort=[alt.SortField('site', 'descending')]
    ).mark_bar().encode(
        column='year:O',
        x=alt.X('yield_1:Q', title='yield'),
        x2='yield_2:Q',
        y='variety:N',
        color='site:N',
        tooltip=['site', 'yield', 'variety']
    ).properties(width=220)

Notice that the bars are now explicitly drawn between values computed and
specified within the x and x2 encodings.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_stack` method is built on the :class:`~StackTransform`
class, which has the following options:

.. altair-object-table:: altair.StackTransform
