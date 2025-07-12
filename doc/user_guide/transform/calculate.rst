.. currentmodule:: altair

.. _user-guide-calculate-transform:

Calculate
~~~~~~~~~
The calculate transform allows the user to define new fields in the dataset
which are calculated from other fields using an expression syntax.

As a simple example, here we take data with a simple input sequence, and compute
a some trigonometric quantities:

.. altair-plot::

    import altair as alt
    import pandas as pd

    data = pd.DataFrame({'t': range(101)})

    alt.Chart(data).mark_line().encode(
        x='x:Q',
        y='y:Q',
        order='t:Q'
    ).transform_calculate(
        x='cos(datum.t * PI / 50)',
        y='sin(datum.t * PI / 25)'
    )

Each argument within ``transform_calculate`` is a `Vega expression`_ string,
which is a well-defined set of javascript-style operations that can be used
to calculate a new field from an existing one.

To streamline building these Vega expressions in Python, Altair provides the
:mod:`expr` module which provides constants and functions to allow
these expressions to be constructed with Python syntax; for example:

.. altair-plot::

    alt.Chart(data).mark_line().encode(
        x='x:Q',
        y='y:Q',
        order='t:Q'
    ).transform_calculate(
        x=alt.expr.cos(alt.datum.t * alt.expr.PI / 50),
        y=alt.expr.sin(alt.datum.t * alt.expr.PI / 25)
    )

Altair expressions are designed to output valid Vega expressions. The benefit of
using them is that proper syntax is ensured by the Python interpreter, and tab
completion of the :mod:`~expr` submodule can be used to explore the
available functions and constants.

These expressions can also be used when constructing a
:ref:`user-guide-filter-transform`, as we shall see next.

Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_calculate` method is built on the :class:`~CalculateTransform`
class, which has the following options:

.. altair-object-table:: altair.CalculateTransform

.. _Vega expression: https://vega.github.io/vega/docs/expressions/
