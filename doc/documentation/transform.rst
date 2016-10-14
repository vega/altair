.. _data-transformations:

Data Transformations
--------------------

.. currentmodule:: altair

Altair provides a data transformation API that allows both *filtering* and
*transformation* of values within the plot renderer. Within Vega-Lite, filter
and transforms operations are specified in terms of *javascript strings* which
make use of Vega's
`Expression Documentation <https://github.com/vega/vega/wiki/Expressions>`_.
Altair provides a Python-style interface to generate these expressions without
having to create the strings manually; this can be done either via a direct
functional expression interface, or via a Pandas-like dataframe interface.
We will see examples of both of these below.

For example, consider this visualization of the historical US population,
split by age and gender:

.. altair-plot::

    from altair import Chart, Color, Scale

    data = 'https://vega.github.io/vega-datasets/data/population.json'
    pink_blue = Scale(range=["lightblue", "pink"])

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('sex:N', scale=pink_blue)
    )

This visualization shows that on average over the course of history, the
younger population has far outnumbered the older population.

1. We might wish to zero-in on a particular year, rather than taking a
   mean over all years.
2. The "1" and "2" labels for gender are not all that informative; we should
   probably be change them to "Male" and "Female" for clarity.

We could certainly accomplish this by downloading the dataset, manipulating it
in, say, pandas, and building a chart using the result, but it would be nice to
do this within the Altair spec itself so that we can use the original data
source.

Vega-Lite allows for this via a ``transform`` field within the plot specification,
and Atltair provides a Pandas-style interface by which these transform fields
can be specified.

To demonstrate this, let's remake the plot using this interface to filter
the data by year, and to create a new column which maps the *1/2* labels
to "Male"/"Female":

.. altair-plot::

    from altair import Chart, Color, Scale, expr

    pink_blue = Scale(range=["pink", "lightblue"])

    # this does not actually download data;
    # just puts a dataframe-like interface around the URL reference
    data = expr.DataFrame('https://vega.github.io/vega-datasets/data/population.json')

    # Add a new column to the data
    data['gender'] = expr.where(data.sex == 1, "Male", "Female")

    # Create a filtered version of the data
    data2000 = data[data.year == 2000]

    Chart(data2000).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('gender:N', scale=pink_blue)
    )

Creating and manipulating the data this way generates appropriate code that
is stored in the spec and then evaluated at the time the plot is generated.
We can see this by printing the resulting specification:

>>> from altair import Chart, expr
>>> data = expr.DataFrame('data.json')
>>> data['gender'] = expr.where(data.sex == 1, "Male", "Female")
>>> data2000 = data[data.year == 2000]
>>> print(Chart(data2000).to_json(indent=2))
{
  "data": {
    "url": "data.json"
  },
  "transform": {
    "calculate": [
      {
        "expr": "if((datum.sex==1),'Male','Female')",
        "field": "gender"
      }
    ],
    "filter": "(datum.year==2000)"
  }
}

Notice that in the resulting specification the ``data`` field contains only the
URL, and the additional information has been encoded within a ``transform``
field using the
`Expression Interface <https://github.com/vega/vega/wiki/Expressions>`_ provided
by the Vega package.

If you would prefer to add these field manually rather than using the :class:`expr.DataFrame`
interface, the :meth:`~Chart.transform_data` method and related :class:`~Transform`
class gives you functional access to these attributes using the :mod:`vega.expr` syntax:

.. altair-setup::

    from altair import Chart, Color, Scale, Formula, expr
    pink_blue = Scale(range=["pink", "lightblue"])

.. altair-plot::

    data = 'https://vega.github.io/vega-datasets/data/population.json'

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('gender:N', scale=pink_blue)
    ).transform_data(
        calculate=[Formula('gender', expr.where(expr.df.sex==1,'Male','Female'))],
        filter=(expr.df.year == 2000)
    )

Or if you really like to do things by hand, the raw javascript strings can be
passed instead:

.. altair-setup::

   data = 'https://vega.github.io/vega-datasets/data/population.json'

.. altair-plot::

    Chart(data).mark_bar().encode(
        x='age:O',
        y='mean(people):Q',
        color=Color('gender:N', scale=pink_blue)
    ).transform_data(
        calculate=[Formula('gender', 'if(datum.sex == 1, "M", "F")')],
        filter=('datum.year == 2000')
    )

While in all these cases the data manipulation could be done as a preprocessing
step, embedding the processed data directly in the URL, this sort of simple
manipulation of an existing data source can lead to much more compact and efficient
plot specifications.

The :ref:`gallery_bar_grouped` example shows a more refined view of this
same dataset using some of these techniques.
