.. _datasets:

Altair Datasets
===============
Altair includes a loader for a number of built-in datasets, available in the
`vega-datasets`_ github repository.
These datasets are used throughout the documentation, and particularly in
the :ref:`example-gallery`.

The list of available datasets can be found using the
:func:`~altair.datasets.list_datasets` function:

>>> from altair.datasets import list_datasets
>>> len(list_datasets())
40
>>> list_datasets()[:5]
['airports', 'anscombe', 'barley', 'birdstrikes', 'budget']

If you would like to load a dataset and use it within a plot, use the
:func:`altair.load_dataset` function:

>>> from altair import load_dataset
>>> data = load_dataset('movies')
>>> print(data.columns)
Index(['Creative_Type', 'Director', 'Distributor', 'IMDB_Rating', 'IMDB_Votes',
       'MPAA_Rating', 'Major_Genre', 'Production_Budget', 'Release_Date',
       'Rotten_Tomatoes_Rating', 'Running_Time_min', 'Source', 'Title',
       'US_DVD_Sales', 'US_Gross', 'Worldwide_Gross'],
      dtype='object')

The data is returned as a Pandas dataframe, which can then be used directly
within Altair:

.. altair-setup::

   from altair import load_dataset
   data = load_dataset('movies')

.. altair-plot::

    from altair import Chart

    Chart(data).mark_tick().encode(
        x='Production_Budget',
        y='MPAA_Rating'
    ).configure_cell(
        width=400
    )

Note that you can also "load" the dataset by url:

>>> url = load_dataset('movies', url_only=True)
>>> url
'https://vega.github.io/vega-datasets/data/movies.json'

Passing data by URL can be more efficient, as the plot specification is not
required to encode the entire dataset within the JSON structure. Keep in mind,
though, that Altair cannot do type inference on data specified by URL, so
you must specify the :ref:`data-types` explicitly:

.. altair-setup::

   url = load_dataset('movies', url_only=True)

.. altair-plot::

    from altair import Chart

    Chart(url).mark_tick().encode(
        x='Production_Budget:Q',
        y='MPAA_Rating:N'
    ).configure_cell(
        width=400
    )

For more examples of visualization using the available datasets, see the
:ref:`example-gallery`.


.. _vega-datasets: https://github.com/vega/vega-datasets
