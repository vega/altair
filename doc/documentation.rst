.. _api-documentation:

Altair Documentation
====================

Altair's core functionality is to produce Vega-Lite JSON specifications, which
specify :ref:`mappings <encoding-reference>` between :ref:`data <defining-data>` and :ref:`graphical markings <mark-reference>`.


.. currentmodule:: altair


.. _defining-data:

Data in Altair
--------------

Each top-level chart object, including :class:`Chart`, :class:`LayeredChart`,
and :class:`FacetedChart`, can take a dataset as its first argument.
The dataset can be specified in one of three ways:

- as a `Pandas DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_
- as a :class:`Data` object
- as a url pointing to a ``json`` or ``csv`` formatted text file

For example, here we specify data via a dataframe:

.. altair-plot::

   from altair import Chart
   import pandas as pd

   data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                        'y': [5, 3, 6, 7, 2]})
   Chart(data).mark_bar().encode(
       x='x',
       y='y',
   )

When data is specified as a DataFrame, the encoding is quite simple, as Altair
uses the data type information provided by Pandas to automatically determine
the data types required in the encoding.

By comparison, here we create the same chart using a :class:`Data` object,
with the data specified as a JSON-style list of records:

.. altair-plot::

   from altair import Chart, Data

   data = Data(values=[{'x': 'A', 'y': 5},
                       {'x': 'B', 'y': 3},
                       {'x': 'C', 'y': 6},
                       {'x': 'D', 'y': 7},
                       {'x': 'E', 'y': 2}])
   Chart(data).mark_bar().encode(
       x='x:O',  # specify ordinal data
       y='y:Q',  # specify quantitative data
   )

notice the extra markup required in the encoding; because Altair cannot infer
the types within a :class:`Data` object, we must specify them manually
(here we use :ref:`shorthand-description` to specify *ordinal* (``O``) for ``x``
and *quantitative* (``Q``) for ``y``; see :ref:`data-types` below).

Similarly, we must also specify the data type when referencing data by URL:

.. altair-plot::

   from altair import Chart

   url = 'https://vega.github.io/vega-datasets/data/cars.json'
   
   Chart(url).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   )

We will further discuss encodings and associated types below.

.. _encoding-reference:

Encodings
---------

*TODO*

.. _data-types:

Data Types
~~~~~~~~~~

*TODO*

.. _encoding-aggregates:

Aggregates
~~~~~~~~~~

*TODO*

.. _shorthand-description:

Encoding Shorthands
~~~~~~~~~~~~~~~~~~~

*TODO*

.. _mark-reference:

Marks
-----

*TODO*

.. _data-transformations:

Data Transformations
--------------------

*TODO*
