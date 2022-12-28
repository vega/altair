.. currentmodule:: altair

.. _user-guide-boxplot-marks:

Box Plot
~~~~~~~~~

A box plot summarizes a distribution of quantitative values using a set of summary statistics. The median tick in the box represents the median. The lower and upper parts of the box represent the first and third quartile respectively. Depending on the type of box plot, the ends of the whiskers can represent multiple things.

To create a box plot, use the ``mark_boxplot`` method.

Box Plot Mark Properties
^^^^^^^^^^^^^^^^^^^^^^^^
A box plot's mark definition can contain the following properties:

.. altair-object-table:: altair.BoxPlotDef
   :properties: extent orient size color opacity

Besides the properties listed above, ``box``, ``median``, ``rule``, ``outliers``, and ``ticks`` can be used to specify the underlying mark properties for different parts of the box plots as well.

Types of Box Plot
^^^^^^^^^^^^^^^^^
Altair supports two types of box plots, defined by the ``extent`` property in the mark definition object.

1. Tukey Box Plot is the default box plot in Altair. For a Tukey box plot, the whisker spans from the smallest data to the largest data within the range [Q1 - k * IQR, Q3 + k * IQR] where Q1 and Q3 are the first and third quartiles while IQR is the interquartile range (Q3-Q1). In this type of box plot, you can specify the constant k by setting the ``extent``. If there are outlier points beyond the whisker, they will be displayed using point marks.
By default, the extent is ``1.5``.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_boxplot().encode(
        alt.X("Miles_per_Gallon:Q", scale=alt.Scale(zero=False))
    )


2. ``min-max`` Box Plot is a box plot where the lower and upper whiskers are defined as the min and max respectively. No points will be considered as outliers for this type of box plots.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_boxplot(extent="min-max").encode(
        alt.X("Miles_per_Gallon:Q", scale=alt.Scale(zero=False)),
        alt.Y("Origin:N"),
    )


Dimension and Orientation
^^^^^^^^^^^^^^^^^^^^^^^^^
Altair supports bot 1D and 2D box plots:

1D box plot shows the distribution of a continuous field.
A box plot’s orientation is automatically determined by the continuous field axis. For example, you can create a vertical 1D box plot by encoding a continuous field on the y axis.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_boxplot().encode(
        alt.Y("Miles_per_Gallon:Q", scale=alt.Scale(zero=False))
    )

2D box plot shows the distribution of a continuous field, broken down by categories.

For 2D box plots with one continuous field and one discrete field, the box plot will be horizontal if the continuous field is on the x axis.

Color, Size, and Opacity Encoding Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can customize the color, size, and opacity of the box in the box plot by using the ``color``, ``size``, and ``opacity`` encoding channels. The ``size`` is applied to only the box and median tick. The ``color`` is applied to only the box and the outlier points. Meanwhile, the ``opacity`` is applied to the whole ``boxplot``.

An example of a box plot where the ``color`` encoding channel is specified.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_boxplot(extent="min-max").encode(
        alt.X("Origin:N"),
        alt.Y("Miles_per_Gallon:Q", scale=alt.Scale(zero=False)),
        alt.Color("Origin:N", legend=None),
    )


Tooltip Encoding Channels
^^^^^^^^^^^^^^^^^^^^^^^^^

You can add custom tooltips to box plots. The custom tooltip will override the default box plot's tooltips.

If the field in the tooltip encoding is unaggregated, it replaces the tooltips of the outlier marks. On the other hand, if the field in the tooltip encoding is aggregated, it replaces the tooltips of the box and whisker marks.

.. altair-plot::
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    alt.Chart(source).mark_boxplot(extent="min-max").encode(
        alt.X("Miles_per_Gallon:Q", scale=alt.Scale(zero=False)),
        alt.Y("Origin:N"),
        alt.Tooltip("mean(Miles_per_Gallon)"),
    )

