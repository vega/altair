Declarative Visualization in Python
===================================

.. altair-minigallery::
   :size: 5
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
development, and the documentation here remains incomplete.
We are currently (October 2017) working on support for Vega-Lite 2.0,
and plan to significantly improve the documentation once that is released.**


Example
-------
Here is an example of using the Altair API to quickly visualize a dataset:

.. altair-plot::

    import altair as alt

    # load built-in dataset as a pandas DataFrame
    cars = alt.load_dataset('cars')

    # Uncomment for rendering in JupyterLab & nteract
    # alt.enable_mime_rendering()

    alt.Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )

The key idea is that you are declaring links between *data columns* and *visual encoding
channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are
handled automatically. Building on this declarative plotting idea, a surprising number
of useful plots and visualizations can be created and a relatively small grammar.

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
   API
   gallery/index
   recipes
   faq

Bug Reports & Questions
-----------------------

Altair is BSD-licensed and the source is available on `GitHub <http://github.com/altair-viz/altair>`_.
If any questions or issues come up as you use Altair, please get in touch via
`Git Issues <http://github.com/altair-viz/altair/issues>`_ or our `Google Group`_.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Google Group: https://groups.google.com/forum/#!forum/altair-viz
