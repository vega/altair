.. currentmodule:: altair

.. _user-guide-lookup-transform:

Lookup
~~~~~~
The Lookup transform extends a primary data source by looking up values from
another data source; it is similar to a one-sided join. A lookup can be added
at the top level of a chart using the :meth:`Chart.transform_lookup` method.

By way of example, imagine you have two sources of data that you would like
to combine and plot: one is a list of names of people along with their height
and weight, and the other is some information about which groups they belong
to. This example data is available in ``vega_datasets``:

.. altair-plot::
   :output: none

   from vega_datasets import data
   people = data.lookup_people()
   groups = data.lookup_groups()

We know how to visualize each of these datasets separately; for example:

.. altair-plot::

    import altair as alt

    top = alt.Chart(people).mark_square(size=200).encode(
        x=alt.X('age:Q', scale=alt.Scale(zero=False)),
        y=alt.Y('height:Q', scale=alt.Scale(zero=False)),
        color='name:N',
        tooltip='name:N'
    ).properties(
        width=400, height=200
    )

    bottom = alt.Chart(groups).mark_rect().encode(
        x='person:N',
        y='group:O'
    ).properties(
        width=400, height=100
    )

    alt.vconcat(top, bottom)

If we would like to plot features that reference both datasets (for example, the
average age within each group), we need to combine the two datasets.
This can be done either as a data preprocessing step, using tools available
in Pandas, or as part of the visualization using a :class:`~LookupTransform`
in Altair.

Combining Datasets with pandas.merge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pandas provides a wide range of tools for merging and joining datasets; see
`Merge, Join, and Concatenate <https://pandas.pydata.org/pandas-docs/stable/merging.html>`_
for some detailed examples.
For the above data, we can merge the data and create a combined chart as follows:

.. altair-plot::

    import pandas as pd
    merged = pd.merge(groups, people, how='left',
                      left_on='person', right_on='name')

    alt.Chart(merged).mark_bar().encode(
        x='mean(age):Q',
        y='group:O'
    )

We specify a left join, meaning that for each entry of the "person" column in
the groups, we seek the "name" column in people and add the entry to the data.
From this, we can easily create a bar chart representing the mean age in each group.

Combining Datasets with a Lookup Transform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For some data sources (e.g. data available at a URL, or data that is streaming),
it is desirable to have a means of joining data without having to download
it for pre-processing in Pandas.
This is where Altair's :meth:`~Chart.transform_lookup` comes in.
To reproduce the above combined plot by combining datasets within the
chart specification itself, we can do the following:

.. altair-plot::

    alt.Chart(groups).mark_bar().encode(
        x='mean(age):Q',
        y='group:O'
    ).transform_lookup(
        lookup='person',
        from_=alt.LookupData(data=people, key='name',
                             fields=['age', 'height'])
    )

Here ``lookup`` names the field in the groups dataset on which we will match,
and the ``from_`` argument specifies a :class:`~LookupData` structure where
we supply the second dataset, the lookup key, and the fields we would like to
extract.

Example: Lookup Transforms for Geographical Visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Lookup transforms are often particularly important for geographic visualization,
where it is common to combine tabular datasets with datasets that specify
geographic boundaries to be visualized; for example, here is a visualization
of unemployment rates per county in the US:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    counties = alt.topo_feature(data.us_10m.url, 'counties')
    unemp_data = data.unemployment.url

    alt.Chart(counties).mark_geoshape().encode(
        color='rate:Q'
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(unemp_data, 'id', ['rate'])
    ).properties(
        projection={'type': 'albersUsa'},
        width=500, height=300
    )

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_lookup` method is built on the :class:`~LookupTransform`
class, which has the following options:

.. altair-object-table:: altair.LookupTransform
