.. _user-guide-data:

Specifying Data in Altair
-------------------------

.. currentmodule:: altair

Each top-level chart object (i.e. :class:`Chart`, :class:`LayerChart`,
and :class:`VConcatChart`, :class:`HConcatChart`, :class:`RepeatChart`,
:class:`FacetChart`) accepts a dataset as its first argument.
The dataset can be specified in one of three ways:

- as a `Pandas DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_
- as a :class:`Data` or related object (i.e. :class:`UrlData`, :class:`InlineData`, :class:`NamedData`)
- as a url string pointing to a ``json`` or ``csv`` formatted text file

For example, here we specify data via a DataFrame:

.. altair-plot::

   import altair as alt
   import pandas as pd

   data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                        'y': [5, 3, 6, 7, 2]})
   alt.Chart(data).mark_bar().encode(
       x='x',
       y='y',
   )

When data is specified as a DataFrame, the encoding is quite simple, as Altair
uses the data type information provided by Pandas to automatically determine
the data types required in the encoding.

By comparison, here we create the same chart using a :class:`Data` object,
with the data specified as a JSON-style list of records:

.. altair-plot::

   import altair as alt

   data = alt.Data(values=[{'x': 'A', 'y': 5},
                           {'x': 'B', 'y': 3},
                           {'x': 'C', 'y': 6},
                           {'x': 'D', 'y': 7},
                           {'x': 'E', 'y': 2}])
   alt.Chart(data).mark_bar().encode(
       x='x:O',  # specify ordinal data
       y='y:Q',  # specify quantitative data
   )

notice the extra markup required in the encoding; because Altair cannot infer
the types within a :class:`Data` object, we must specify them manually
(here we use :ref:`shorthand-description` to specify *ordinal* (``O``) for ``x``
and *quantitative* (``Q``) for ``y``; see :ref:`encoding-data-types`).

Similarly, we must also specify the data type when referencing data by URL:

.. altair-plot::

    import altair as alt
    from vega_datasets import data
    url = data.cars.url

    alt.Chart(url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q'
    )

We will further discuss encodings and associated types in :ref:`user-guide-encoding`, next.


.. _data-in-index:

Including Index Data
~~~~~~~~~~~~~~~~~~~~
By design Altair only accesses dataframe columns, not dataframe indices.
At times, relevant data appears in the index. For example:

.. altair-plot::
   :output: repr

   import numpy as np
   rand = np.random.RandomState(0)

   data = pd.DataFrame({'value': rand.randn(100).cumsum()},
                       index=pd.date_range('2018', freq='D', periods=100))
   data.head()
   
If you would like the index to be available to the chart, you can explicitly
turn it into a column using the ``reset_index()`` method of Pandas dataframes:

.. altair-plot::

   alt.Chart(data.reset_index()).mark_line().encode(
       x='index:T',
       y='value:Q'
   )

If the index object does not have a ``name`` attribute set, the resulting
column will be called ``"index"``.
More information is available in the
`Pandas documentation <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html>`_.


.. _data-long-vs-wide:

Long-form vs. Wide-form Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are two common conventions for storing data in a dataframe, sometimes called
*long-form* and *wide-form*. Both are sensible patterns for storing data in
a tabular format; briefly, the difference is this:

- **wide-form data** has one row per *independent variable*, with metadata
  recorded in the *row and column labels*.
- **long-form data** has one row per *observation*, with metadata recorded
  within the table as *values*.

Altair's grammar works best with **long-form** data, in which each row
corresponds to a single observation along with its metadata.

A concrete example will help in making this distinction more clear.
Consider a dataset consisting of stock prices of several companies over time.
The wide-form version of the data might be arranged as follows:

.. altair-plot::
    :output: repr
    :chart-var-name: wide_form

    wide_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01'],
                              'AAPL': [189.95, 182.22, 198.08],
                              'AMZN': [89.15, 90.56, 92.64],
                              'GOOG': [707.00, 693.00, 691.48]})
    print(wide_form)

Notice that each row corresponds to a single time-stamp (here time is the
independent variable), while metadata for each observation
(i.e. company name) is stored within the column labels.

The long-form version of the same data might look like this:

.. altair-plot::
    :output: repr
    :chart-var-name: long_form

    long_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01',
                                       '2007-10-01', '2007-11-01', '2007-12-01',
                                       '2007-10-01', '2007-11-01', '2007-12-01'],
                              'company': ['AAPL', 'AAPL', 'AAPL',
                                          'AMZN', 'AMZN', 'AMZN',
                                          'GOOG', 'GOOG', 'GOOG'],
                              'price': [189.95, 182.22, 198.08,
                                         89.15,  90.56,  92.64,
                                        707.00, 693.00, 691.48]})
    print(long_form)

Notice here that each row contains a single observation (i.e. price), along
with the metadata for this observation (the date and company name).
Importantly, the column and index labels no longer contain any useful metadata.

As mentioned above, Altair works best with this long-form data, because relevant
data and metadata are stored within the table itself, rather than within the
labels of rows and columns:

.. altair-plot::

    alt.Chart(long_form).mark_line().encode(
      x='Date:T',
      y='price:Q',
      color='company:N'
    )

Wide-form data can be similarly visualized using e.g. layering
(see :ref:`layer-chart`), but it is far less convenient within Altair's grammar.

If you would like to convert data from wide-form to long-form, there are two possible
approaches: it can be done as a preprocessing step using pandas, or as a transform
step within the chart itself. We will detail to two approaches below.

.. _data-converting-long-form:

Converting Between Long-form and Wide-form: Pandas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This sort of data manipulation can be done as a preprocessing step using Pandas_,
and is discussed in detail in the `Reshaping and Pivot Tables`_ section of the
Pandas documentation.

For converting wide-form data to the long-form data used by Altair, the ``melt``
method of dataframes can be used. The first argument to ``melt`` is the column
or list of columns to treat as index variables; the remaining columns will
be combined into an indicator variable and a value variable whose names can
be optionally specified:

.. altair-plot::
    :output: repr

    wide_form.melt('Date', var_name='company', value_name='price')

For more information on the ``melt`` method, see the `Pandas melt documentation`_.

In case you would like to undo this operation and convert from long-form back
to wide-form, the ``pivot`` method of dataframes is useful.

.. altair-plot::
    :output: repr

    long_form.pivot(index='Date', columns='company', values='price').reset_index()

For more information on the ``pivot`` method, see the `Pandas pivot documentation`_.

Converting Between Long-form and Wide-form: Fold Transform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to avoid data preprocessing, you can reshape your data using Altair's
Fold Transform (see :ref:`user-guide-fold-transform` for a full discussion).
With it, the above chart can be reproduced as follows:

.. altair-plot::
   
    alt.Chart(wide_form).transform_fold(
        ['AAPL', 'AMZN', 'GOOG'],
        as_=['company', 'price']
    ).mark_line().encode(
        x='Date:T',
        y='price:Q',
        color='company:N'
    )

Notice that unlike the pandas ``melt`` function we must explicitly specify the columns
to be folded. The ``as_`` argument is optional, with the default being ``["key", "value"]``.

.. _Pandas: http://pandas.pydata.org/
.. _Pandas pivot documentation: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.pivot.html
.. _Pandas melt documentation: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.melt.html#pandas.DataFrame.melt
.. _Reshaping and Pivot Tables: https://pandas.pydata.org/pandas-docs/stable/reshaping.html
