Declarative Visualization in Python
===================================

.. altair-minigallery::
   :size: 6
   :width: 125px
   :shuffle:
   :seed: 0


Altair is a declarative statistical visualization library for Python, based on
Vega-Lite_.

With Altair, you can spend more time understanding your data and its meaning.
Altair's API is simple, friendly and consistent and built on top of the
powerful Vega-Lite_ visualization grammar. This elegant simplicity produces
beautiful and effective visualizations with a minimal amount of code.

**Note: Altair and the underlying Vega-Lite library are under active
development; new plot types and streamlined plotting interfaces will be
added in future releases. Please stay tuned for
developments in the coming months! -- October 2016**


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

More examples are available in the :ref:`example-gallery`, or you can work
through one of the :ref:`altair-tutorials`. The full documentation listing
is available below.


Documentation
-------------

.. toctree::
   :maxdepth: 2

   installation
   tutorials/index
   documentation/index
   gallery/index
   recipes
   API


Bug Reports & Questions
-----------------------
Altair is BSD-licensed and the source is available on `Github <http://github.com/altair-viz/altair>`_.
If any questions or issues come up as you use Altair, please get in touch via the `Issues <http://github.com/altair-viz/altair/issues>`_ tracker there.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Vega-Lite: http://vega.github.io/vega-lite
