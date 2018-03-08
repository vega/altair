Declarative Visualization in Python
===================================

.. altair-minigallery::
   :size: 6
   :width: 110px
   :indices: 14 23 40 42 44 59

Altair is a declarative statistical visualization library for Python, based on
Vega_ and Vega-Lite_.

With Altair, you can spend more time understanding your data and its meaning.
Altair's API is simple, friendly and consistent and built on top of the
powerful Vega-Lite_ visualization grammar. This elegant simplicity produces
beautiful and effective visualizations with a minimal amount of code.


Example
-------
Here is an example of using the Altair API to quickly visualize a dataset with
an interactive scatter plot:

.. altair-plot::

    import altair as alt

    # load a simple dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

The key idea is that you are declaring links between *data columns* and *visual encoding
channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are
handled automatically. Building on this declarative plotting idea, a surprising number
of useful plots and visualizations can be created using a relatively concise grammar.

Documentation
-------------

.. toctree::
   :maxdepth: 2

   tutorials/index
   gallery/index
   API

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
.. _Vega: http://vega.github.io/vega
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Google Group: https://groups.google.com/forum/#!forum/altair-viz
