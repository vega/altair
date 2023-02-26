.. currentmodule:: altair

.. _user-guide-encoding:

Encodings
---------

The key to creating meaningful visualizations is to map *properties of the data*
to *visual properties* in order to effectively communicate information.
In Altair, this mapping of visual properties to data columns is referred to
as an **encoding**, and is most often expressed through the :meth:`Chart.encode`
method.

For example, here we will visualize the cars dataset using four of the available
**encoding channels** (see :ref:`user-guide-encoding-channels` for details): ``x`` (the x-axis value), ``y`` (the y-axis value),
``color`` (the color of the marker), and ``shape`` (the shape of the point marker):

.. altair-plot::

   import altair as alt
   from vega_datasets import data


   cars = data.cars()

   alt.Chart(cars).mark_point().encode(
       x='Horsepower',
       y='Miles_per_Gallon',
       color='Origin',
       shape='Origin'
   )

Each encoding channel accepts a number of **channel options** (see :ref:`user-guide-encoding-channel-options` for details) which can be used to further configure
the chart. For example, below we adjust the y-axis title and increase the step between the x-axis ticks:

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_point().encode(
        x=alt.X('Horsepower', axis=alt.Axis(tickMinStep=50)),
        y=alt.Y('Miles_per_Gallon', title="Miles per Gallon"),
        color='Origin',
        shape='Origin'
    )


.. _method-based-attribute-setting:

Alternative Syntax for Channel Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair 5.0 introduced an alternative method-based syntax for setting channel options.  In the example above, the ``axis`` option of the ``x`` channel encoding is set using the ``axis`` keyword argument: ``x=alt.X('Horsepower', axis=alt.Axis(tickMinStep=50))``.  To define the same :class:`X` object using the alternative method-based syntax, we can use ``x=alt.X('Horsepower').axis(tickMinStep=50)``.  In other words, the use of the ``axis`` keyword argument is replaced by the use of the ``axis`` method.

The same technique works with all encoding channels and all channel options.  For example, notice how we make the analogous change with respect to the ``title`` option of the ``y`` channel.  The following produces the same chart as the previous example.

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_point().encode(
        x=alt.X('Horsepower').axis(tickMinStep=50),
        y=alt.Y('Miles_per_Gallon').title('Miles per Gallon'),
        color='Origin',
        shape='Origin'
    )

These option-setter methods can also be chained together, as in the following, in which we set the ``axis``, ``bin``, and ``scale`` options of the ``x`` channel by using the corresponding methods (``axis``, ``bin``, and ``scale``).  We can break the ``x`` definition over multiple lines to improve readability.  (This is valid syntax because of the enclosing parentheses from ``encode``.)

.. altair-plot::
    import altair as alt
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_point().encode(
        x=alt.X('Horsepower')
                .axis(ticks=False)
                .bin(maxbins=10)
                .scale(domain=(30,300), reverse=True),
        y=alt.Y('Miles_per_Gallon').title('Miles per Gallon'),
        color='Origin',
        shape='Origin'
    )

.. _encoding-data-types:

Encoding Data Types
~~~~~~~~~~~~~~~~~~~
The details of any mapping depend on the *type* of the data. Altair recognizes
five main data types:

============  ==============  ================================================
Data Type     Shorthand Code  Description
============  ==============  ================================================
quantitative  ``Q``           a continuous real-valued quantity
ordinal       ``O``           a discrete ordered quantity
nominal       ``N``           a discrete unordered category
temporal      ``T``           a time or date value
geojson       ``G``           a geographic shape
============  ==============  ================================================

For data specified as a DataFrame, Altair can automatically determine the
correct data type for each encoding, and creates appropriate scales and
legends to represent the data.

If types are not specified for data input as a DataFrame, Altair defaults to
``quantitative`` for any numeric data, ``temporal`` for date/time data, and
``nominal`` for string data, but be aware that these defaults are by no means
always the correct choice!

The types can either be expressed in a long-form using the channel encoding
classes such as :class:`X` and :class:`Y`, or in short-form using the
:ref:`Shorthand Syntax <shorthand-description>` discussed below.
For example, the following two methods of specifying the type will lead to
identical plots:

.. altair-plot::

   alt.Chart(cars).mark_point().encode(
       x='Acceleration:Q',
       y='Miles_per_Gallon:Q',
       color='Origin:N'
   )

.. altair-plot::

  alt.Chart(cars).mark_point().encode(
      alt.X('Acceleration', type='quantitative'),
      alt.Y('Miles_per_Gallon', type='quantitative'),
      alt.Color('Origin', type='nominal')
  )

The shorthand form, ``x="name:Q"``, is useful for its lack of boilerplate
when doing quick data explorations. The long-form,
``alt.X('name', type='quantitative')``, is useful when doing more fine-tuned
adjustments to the encoding using channel options such as binning, axis, and scale.

Specifying the correct type for your data is important, as it affects the
way Altair represents your encoding in the resulting plot.

.. _type-legend-scale:

Effect of Data Type on Color Scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As an example of this, here we will represent the same data three different ways,
with the color encoded as a *quantitative*, *ordinal*, and *nominal* type,
using three vertically-concatenated charts (see :ref:`vconcat-chart`):

.. altair-plot::

   base = alt.Chart(cars).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q',
   ).properties(
       width=150,
       height=150
   )

   alt.vconcat(
      base.encode(color='Cylinders:Q').properties(title='quantitative'),
      base.encode(color='Cylinders:O').properties(title='ordinal'),
      base.encode(color='Cylinders:N').properties(title='nominal'),
   )

The type specification influences the way Altair, via Vega-Lite, decides on
the color scale to represent the value, and influences whether a discrete
or continuous legend is used.

.. _type-axis-scale:

Effect of Data Type on Axis Scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similarly, for x and y axis encodings, the type used for the data will affect
the scales used and the characteristics of the mark. For example, here is the
difference between a ``quantitative`` and ``ordinal`` scale for an column
that contains integers specifying a year:

.. altair-plot::

    pop = data.population.url

    base = alt.Chart(pop).mark_bar().encode(
        alt.Y('mean(people):Q', title='total population')
    ).properties(
        width=200,
        height=200
    )

    alt.hconcat(
        base.encode(x='year:Q').properties(title='year=quantitative'),
        base.encode(x='year:O').properties(title='year=ordinal')
    )

Because quantitative values do not have an inherent width, the bars do not
fill the entire space between the values.
This view also makes clear the missing year of data that was not immediately
apparent when we treated the years as categories.

This kind of behavior is sometimes surprising to new users, but it emphasizes
the importance of thinking carefully about your data types when visualizing
data: a visual encoding that is suitable for categorical data may not be
suitable for quantitative data, and vice versa.


.. _shorthand-description:

Encoding Shorthands
~~~~~~~~~~~~~~~~~~~

For convenience, Altair allows the specification of the variable name along
with the aggregate and type within a simple shorthand string syntax.
This makes use of the type shorthand codes listed in :ref:`encoding-data-types`
as well as the aggregate names listed in :ref:`encoding-aggregates`.
The following table shows examples of the shorthand specification alongside
the long-form equivalent:

===================  =======================================================
Shorthand            Equivalent long-form
===================  =======================================================
``x='name'``         ``alt.X('name')``
``x='name:Q'``       ``alt.X('name', type='quantitative')``
``x='sum(name)'``    ``alt.X('name', aggregate='sum')``
``x='sum(name):Q'``  ``alt.X('name', aggregate='sum', type='quantitative')``
``x='count():Q'``    ``alt.X(aggregate='count', type='quantitative')``
===================  =======================================================

Escaping special characters in column names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seeing that Altair uses ``:`` as a special character
to indicate the encoding data type,
you might wonder what happens
when the column name in your data includes a colon.
When this is the case
you will need to either rename the column or escape the colon.
This is also true for other special characters
such as ``.`` and ``[]`` which are used to access nested attributes
in some data structures.

The recommended thing to do when you have special characters in a column name
is to rename your columns.
For example, in Pandas you could replace ``:`` with ``_``
via ``df.rename(columns = lambda x: x.replace(':', '_'))``.
If you don't want to rename your columns
you will need to escape the special characters using a backslash:

.. altair-plot::

    import pandas as pd

    source = pd.DataFrame({
        'col:colon': [1, 2, 3],
        'col.period': ['A', 'B', 'C'],
        'col[brackets]': range(3),
    })

    alt.Chart(source).mark_bar().encode(
        x='col\:colon',
        # Remove the backslash in the title
        y=alt.Y('col\.period', title='col.period'),
        # Specify the data type
        color='col\[brackets\]:N',
    )

As can be seen above,
indicating the data type is optional
just as for columns without escaped characters.
Note that the axes titles include the backslashes by default
and you will need to manually set the title strings to remove them.
If you are using the long form syntax for encodings,
you do not need to escape colons as the type is explicit,
e.g. ``alt.X('col:colon', type='quantitative')``
(but periods and brackets still need to be escaped
in the long form syntax unless they are used to index nested data structures).


.. _encoding-aggregates:

Binning and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~

Beyond simple channel encodings, Altair's visualizations are built on the
concept of the database-style grouping and aggregation; that is, the
`split-apply-combine <https://www.jstatsoft.org/article/view/v040i01>`_
abstraction that underpins many data analysis approaches.

For example, building a histogram from a one-dimensional dataset involves
splitting data based on the bin it falls in, aggregating the results within
each bin using a *count* of the data, and then combining the results into
a final figure.

In Altair, such an operation looks like this:

.. altair-plot::

   alt.Chart(cars).mark_bar().encode(
       alt.X('Horsepower', bin=True),
       y='count()'
       # could also use alt.Y(aggregate='count', type='quantitative')
   )

Notice here we use the shorthand version of expressing an encoding channel
(see :ref:`shorthand-description`) with the ``count`` aggregation,
which is the one aggregation that does not require a field to be
specified.

Similarly, we can create a two-dimensional histogram using, for example, the
size of points to indicate counts within the grid (sometimes called
a "Bubble Plot"):

.. altair-plot::

   alt.Chart(cars).mark_point().encode(
       alt.X('Horsepower', bin=True),
       alt.Y('Miles_per_Gallon', bin=True),
       size='count()',
   )

There is no need, however, to limit aggregations to counts alone. For example,
we could similarly create a plot where the color of each point
represents the mean of a third quantity, such as acceleration:

.. altair-plot::

   alt.Chart(cars).mark_circle().encode(
       alt.X('Horsepower', bin=True),
       alt.Y('Miles_per_Gallon', bin=True),
       size='count()',
       color='average(Acceleration):Q'
   )

Aggregation Functions
^^^^^^^^^^^^^^^^^^^^^

In addition to ``count`` and ``average``, there are a large number of available
aggregation functions built into Altair:

=========  ===========================================================================  =====================================
Aggregate  Description                                                                  Example
=========  ===========================================================================  =====================================
argmin     An input data object containing the minimum field value.                     N/A
argmax     An input data object containing the maximum field value.                     :ref:`gallery_line_chart_with_custom_legend`
average    The mean (average) field value. Identical to mean.                           :ref:`gallery_layer_line_color_rule`
count      The total count of data objects in the group.                                :ref:`gallery_simple_heatmap`
distinct   The count of distinct field values.                                          N/A
max        The maximum field value.                                                     :ref:`gallery_boxplot`
mean       The mean (average) field value.                                              :ref:`gallery_scatter_with_layered_histogram`
median     The median field value                                                       :ref:`gallery_boxplot`
min        The minimum field value.                                                     :ref:`gallery_boxplot`
missing    The count of null or undefined field values.                                 N/A
q1         The lower quartile boundary of values.                                       :ref:`gallery_boxplot`
q3         The upper quartile boundary of values.                                       :ref:`gallery_boxplot`
ci0        The lower boundary of the bootstrapped 95% confidence interval of the mean.  :ref:`gallery_sorted_error_bars_with_ci`
ci1        The upper boundary of the bootstrapped 95% confidence interval of the mean.  :ref:`gallery_sorted_error_bars_with_ci`
stderr     The standard error of the field values.                                      N/A
stdev      The sample standard deviation of field values.                               N/A
stdevp     The population standard deviation of field values.                           N/A
sum        The sum of field values.                                                     :ref:`gallery_streamgraph`
valid      The count of field values that are not null or undefined.                    N/A
values     A list of data objects in the group.                                         N/A
variance   The sample variance of field values.                                         N/A
variancep  The population variance of field values.                                     N/A
=========  ===========================================================================  =====================================


Sort Option
~~~~~~~~~~~

Some channels accept a  :class:`sort` option which determines the
order of the scale being used for the channel.
By default the scale is sorted in ascending alphabetical order,
unless an `ordered pandas categorical column <https://pandas.pydata.org/docs/user_guide/categorical.html?highlight=categorical#sorting-and-order>`_ is passed (without an explicit type specification)
in which case Altair will use the column's inherent order to sort the scale.
There are a number of different
options available to change the sort order:

- ``sort='ascending'`` (Default) will sort the field's value in ascending order.
  For string data, this uses standard alphabetical order.
- ``sort='descending'`` will sort the field's value in descending order
- Passing the name of an encoding channel to ``sort``, such as ``"x"`` or ``"y"``, allows for
  sorting by that channel. An optional minus prefix can be used for a descending
  sort. For example ``sort='-x'`` would sort by the x channel in descending order.
- Passing a list to ``sort`` allows you to explicitly set the order in which
  you would like the encoding to appear
- Passing a :class:`EncodingSortField` class to ``sort`` allows you to sort
  an axis by the value of some other field in the dataset.

Here is an example of applying these five different sort approaches on the
x-axis, using the barley dataset:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    barley = data.barley()

    base = alt.Chart(barley).mark_bar().encode(
        y='mean(yield):Q',
        color=alt.Color('mean(yield):Q', legend=None)
    ).properties(width=100, height=100)

    # Sort x in ascending order
    ascending = base.encode(
        alt.X(field='site', type='nominal', sort='ascending')
    ).properties(
        title='Ascending'
    )

    # Sort x in descending order
    descending = base.encode(
        alt.X(field='site', type='nominal', sort='descending')
    ).properties(
        title='Descending'
    )

    # Sort x in an explicitly-specified order
    explicit = base.encode(
        alt.X(field='site', type='nominal',
              sort=['Duluth', 'Grand Rapids', 'Morris',
                    'University Farm', 'Waseca', 'Crookston'])
    ).properties(
        title='Explicit'
    )

    # Sort according to encoding channel
    sortchannel = base.encode(
        alt.X(field='site', type='nominal',
              sort='y')
    ).properties(
        title='By Channel'
    )

    # Sort according to another field
    sortfield = base.encode(
        alt.X(field='site', type='nominal',
              sort=alt.EncodingSortField(field='yield', op='mean'))
    ).properties(
        title='By Yield'
    )

    alt.concat(
        ascending, descending, explicit,
        sortchannel, sortfield,
        columns=3
    )

The last two charts are the same because the default aggregation
(see :ref:`encoding-aggregates`) is ``mean``. To highlight the
difference between sorting via channel and sorting via field consider the
following example where we don't aggregate the data:

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    barley = data.barley()
    base = alt.Chart(barley).mark_point().encode(
        y='yield:Q',
    ).properties(width=200)

    # Sort according to encoding channel
    sortchannel = base.encode(
        alt.X(field='site', type='nominal',
              sort='y')
    ).properties(
        title='By Channel'
    )

    # Sort according to another field
    sortfield = base.encode(
        alt.X(field='site', type='nominal',
              sort=alt.EncodingSortField(field='yield', op='min'))
    ).properties(
        title='By Min Yield'
    )
    sortchannel | sortfield

By passing a :class:`EncodingSortField` class to ``sort`` we have more control over
the sorting process.


Sorting Legends
^^^^^^^^^^^^^^^

While the above examples show sorting of axes by specifying ``sort`` in the
:class:`X` and :class:`Y` encodings, legends can be sorted by specifying
``sort`` in the :class:`Color` encoding:

.. altair-plot::

    alt.Chart(barley).mark_rect().encode(
        alt.X('mean(yield):Q', sort='ascending'),
        alt.Y('site:N', sort='descending'),
        alt.Color('site:N',
            sort=['Morris', 'Duluth', 'Grand Rapids',
                  'University Farm', 'Waseca', 'Crookston']
        )
    )

Here the y-axis is sorted reverse-alphabetically, while the color legend is
sorted in the specified order, beginning with ``'Morris'``.

Datum and Value
~~~~~~~~~~~~~~~

So far we always mapped an encoding channel to a column in our dataset. However, sometimes
it is also useful to map to a single constant value. In Altair, you can do this with

* ``datum``, which encodes a constant domain value via a scale using the same units as the underlying data
* ``value``, which encodes a constant visual value, using absolute units such as an exact position in pixels, the name or RGB value of a color, the name of shape,  etc

``datum`` is particularly useful for annotating a specific data value. 
For example, you can use it with a rule mark to highlight a 
threshold value (e.g., 300 dollars stock price).

.. altair-plot::
    
    import altair as alt
    from vega_datasets import data

    source = data.stocks()
    base = alt.Chart(source)
    lines = base.mark_line().encode(
        x="date:T",
        y="price:Q",
        color="symbol:N"
    )
    rule = base.mark_rule(strokeDash=[2, 2]).encode(
        y=alt.datum(300)
    )

    lines + rule

If we instead used ``alt.value`` in this example, we would position the rule 300 pixels from the top of the chart border rather than at the 300 dollars position. Since the default charts height is 300 pixels, this will show the dotted line just on top of the x-axis -line:

.. altair-plot::

    rule = base.mark_rule(strokeDash=[2, 2]).encode(
        y=alt.value(300)
    )

    lines + rule

If we want to use ``datum``  to highlight a certain year on the x-axis,
we can't simply type in the year as an integer,
but instead need to use ``datum`` together with :class:`DateTime`.
Here we also set the color for the rule to the same one as the line for the symbol ``MSFT``
with ``alt.datum("MSFT")``.

.. altair-plot::
    
    import altair as alt
    from vega_datasets import data

    source = data.stocks()
    base = alt.Chart(source)
    lines = base.mark_line().encode(
        x="date:T",
        y="price:Q",
        color="symbol:N"
    )
    rule = base.mark_rule(strokeDash=[2, 2]).encode(
        x=alt.datum(alt.DateTime(year=2006)),
        color=alt.datum("MSFT")
    )

    lines + rule


Similar to when mapping to a data column, when using ``datum`` different encoding channels 
may support ``band``, ``scale``, ``axis``, ``legend``, ``format``, or ``condition`` properties.
However, data transforms (e.g. ``aggregate``, ``bin``, ``timeUnit``, ``sort``) cannot be applied.

Expanding on the example above, if you would want to color the ``rule`` mark regardless of 
the color scale used for the lines, you can use ``value``, e.g. ``alt.value("red")``:

.. altair-plot::
    
    import altair as alt
    from vega_datasets import data

    source = data.stocks()
    base = alt.Chart(source)
    lines = base.mark_line().encode(
        x="date:T",
        y="price:Q",
        color="symbol:N"
    )
    rule = base.mark_rule(strokeDash=[2, 2]).encode(
        x=alt.datum(alt.DateTime(year=2006)),
        color=alt.value("red")
    )

    lines + rule

One caution is that ``alt.datum`` and ``alt.value`` do not possess the (newly introduced as of Altair 5.0) method-based syntax to set channel options described in :ref:`method-based-attribute-setting`. For example, if you are using ``alt.datum`` for the ``y`` channel encoding and you wish to use an option setter method (e.g., ``scale``), then you can use :class:`YDatum` instead.  Here is a simple example.

.. altair-plot::
    
    import altair as alt

    bar = alt.Chart().mark_bar().encode(
        y=alt.YDatum(220).scale(domain=(0,500)),
        color=alt.value("darkkhaki")
    )

    bar

If you were to instead use ``y=alt.datum(220).scale(domain=(0,500))``, an ``AttributeError`` would be raised, due to the fact that ``alt.datum(220)`` simply returns a Python dictionary and does not possess a ``scale`` attribute.  If you insisted on producing the preceding example using ``alt.datum``, one option would be to use ``y=alt.datum(220, scale={"domain": (0,500)})``.  Nevertheless, the ``alt.YDatum`` approach is strongly preferred to this "by-hand" approach of supplying a dictionary to ``scale``.  As one benefit, tab-completions are available using the ``alt.YDatum`` approach.  For example, typing ``alt.YDatum(220).scale(do`` and hitting ``tab`` in an environment such as JupyterLab will offer ``domain``, ``domainMax``, ``domainMid``, and ``domainMin`` as possible completions.

.. toctree::
   :hidden:

   channels
   channel_options
