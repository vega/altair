Altair: Declarative Visualization in Python
===========================================

Altair is a declarative statistical visualization library for Python.

With Altair, you can spend more time understanding your data and its meaning.
Altair's API is simple, friendly and consistent and built on top of the
powerful Vega-Lite_ visualization grammar. This elegant simplicity produces
beautiful and effective visualizations with a minimal amount of code.

Example
-------
Here is an example of using the Altair API to quickly visualize a dataset:

.. altair-plot::

    from altair import Chart, load_dataset

    # load built-in dataset as a pandas DataFrame
    cars = load_dataset('cars')

    Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )

The key idea is that you are declaring links between *data columns* to *encoding channels*, such as the x-axis, y-axis, color, etc. and the rest of the plot details are handled automatically.
Building on this declarative plotting idea, a surprising number of useful plots and visualizations can be created.
For more details, see the documentation below:

Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   tutorials/index
   displaying
   gallery/index
   documentation
   API


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Vega-Lite: http://vega.github.io/vega-lite
