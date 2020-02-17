.. currentmodule:: altair

.. _user-guide-resolve:

Scale and Guide Resolution
--------------------------
When creating compound charts (see :ref:`user-guide-compound`), altair defaults
to using shared chart scales and guides (e.g. axes, legends, etc.).
This default can be adjusted using the :meth:`Chart.resolve_scale`,
:meth:`Chart.resolve_axis`, and :meth:`Chart.resolve_legend` functions.

For example, suppose you would like to concatenate two charts with separate
color scales; the default behavior is for the color scale to be created for
a union of the two color encoding domains:

.. altair-plot::

   import altair as alt
   from vega_datasets import data
   
   source = data.cars()
   
   base = alt.Chart(source).mark_point().encode(
       x='Horsepower:Q',
       y='Miles_per_Gallon:Q'
   ).properties(
       width=200,
       height=200
   )
   
   alt.concat(
       base.encode(color='Origin:N'),
       base.encode(color='Cylinders:O')
   )

This default can be changed by setting the scale resolution for the color to
``"independent"`` (rather than the default, ``"shared"``):

.. altair-plot::
   
   alt.concat(
       base.encode(color='Origin:N'),
       base.encode(color='Cylinders:O')
   ).resolve_scale(
       color='independent'
   )

Dual Y Axis
~~~~~~~~~~~

A common technique for combining chart containing different measures is using a
dual y axis. There are two strategies to achieve this result using altair. The
first is to manually specify the mark color and associated axis title color of
each layer. 

.. altair-plot::

    import altair as alt
    from vega_datasets import data

    source = data.cars()

    base = alt.Chart(source).encode(
            alt.X('year(Year):T')
    )

    line_A = base.mark_line(color='#5276A7').encode(
        alt.Y('average(Horsepower):Q', axis=alt.Axis(titleColor='#5276A7'))
    )

    line_B = base.mark_line(color='#F18727').encode(
        alt.Y('average(Miles_per_Gallon):Q', axis=alt.Axis(titleColor='#F18727'))
    )

    alt.layer(line_A, line_B).resolve_scale(y='independent')

In this case the axis colors act as a pseudo-legend. Alternatively if you want
a legend some transformations must be applied. Legends are only created in
Vega-Lite to represent an encoding.

.. altair-plot::

    base = alt.Chart(source).mark_line().transform_fold(
        ['Horsepower', 'Miles_per_Gallon'],
        as_=['Measure', 'Value']
    ).encode(
        alt.Color('Measure:N'),
        alt.X('year(Year):T')
    )

    line_A = base.transform_filter(
        alt.datum.Measure == 'Horsepower'
    ).encode(
        alt.Y('average(Value):Q', axis=alt.Axis(title='Horsepower')),
    )

    line_B = base.transform_filter(
        alt.datum.Measure == 'Miles_per_Gallon'
    ).encode(
        alt.Y('average(Value):Q',axis=alt.Axis(title='Miles_per_Gallon'))
    )

    alt.layer(line_A, line_B).resolve_scale(y='independent')

Note that dual axis charts might be misleading about
relationships in your data. For further reading on the topic see `The case against dual axis
charts <https://blog.datawrapper.de/dualaxis/>`__ by Lisa Charlotte Rost.
