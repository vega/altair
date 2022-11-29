.. currentmodule:: altair

.. _user-guide-bin-transform:

Bin
~~~
As with :ref:`user-guide-aggregate-transform`, there are two ways to apply
a bin transform in Altair: within the encoding itself, or using a top-level
bin transform.

An common application of a bin transform is when creating a histogram:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    movies = data.movies.url

    alt.Chart(movies).mark_bar().encode(
        alt.X("IMDB_Rating:Q", bin=True),
        y='count()',
    )

But a bin transform can be useful in other applications; for example, here we
bin a continuous field to create a discrete color map:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.Color('Acceleration:Q', bin=alt.Bin(maxbins=5))
    )

In the first case we set ``bin = True``, which uses the default bin settings.
In the second case, we exercise more fine-tuned control over the bin parameters
by passing a :class:`~altair.Bin` object.

If you are using the same bins in multiple chart components, it can be useful
to instead define the binning at the top level, using :meth:`~Chart.transform_bin`
method.

Here is the above histogram created using a top-level bin transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    movies = data.movies.url

    alt.Chart(movies).mark_bar().encode(
        x='binned_rating:O',
        y='count()',
    ).transform_bin(
        'binned_rating', field='IMDB_Rating'
    )

And here is the transformed color scale using a top-level bin transform:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    cars = data.cars.url

    alt.Chart(cars).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color='binned_acc:O'
    ).transform_bin(
        'binned_acc', 'Acceleration', bin=alt.Bin(maxbins=5)
    )

The advantage of the top-level transform is that the same named field can be
used in multiple places in the chart if desired.
Note the slight difference in binning behavior between the encoding-based bins
(which preserve the range of the bins) and the transform-based bins (which
collapse each bin to a single representative value.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_bin` method is built on the :class:`~BinTransform`
class, which has the following options:

.. altair-object-table:: altair.BinTransform
