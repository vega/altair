Declarative Visualization in Python
===================================

Altair is a declarative statistical visualization library for Python, based on
Vega-Lite_.

With Altair, you can spend more time understanding your data and its meaning.
Altair's API is simple, friendly and consistent and built on top of the
powerful Vega-Lite_ visualization grammar. This elegant simplicity produces
beautiful and effective visualizations with a minimal amount of code.

**Note: Altair and the underlying Vega-Lite library are under active
development. We are currently (March 2018) working on a 2.0 release, and
this documentation site is under construction.**


Example
-------
Here is an example of using the Altair API to quickly visualize a dataset with
an interactive scatter plot:

.. altair-plot::

    import altair as alt

    # load built-in dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

The key idea is that you are declaring links between *data columns* and *visual encoding
channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are
handled automatically. Building on this declarative plotting idea, a surprising number
of useful plots and visualizations can be created and a relatively small grammar.


Documentation
-------------

.. toctree::
   :maxdepth: 2

Bug Reports & Questions
-----------------------

Altair is BSD-licensed and the source is available on `GitHub`_. If any
questions or issues come up as you use Altair, please get in touch via
`Git Issues`_ or our `Google Group`_.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _GitHub: http://github.com/altair-viz/altair
.. _Git Issues: http://github.com/altair-viz/altair/issues
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Google Group: https://groups.google.com/forum/#!forum/altair-viz
