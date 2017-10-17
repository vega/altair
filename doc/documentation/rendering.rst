.. _rendering:

Rendering in Jupyter notebooks
------------------------------

Usually, you will want to render your Altair visualization in your Jupyter notebooks.
The following Jupyter notebook user interfaces can render Altair visualizations:

- `Jupyter Notebook`_ (the ipyvega_ package is required)
- `JupyterLab`_ (built-in support)
- `nteract`_ (built-in-support)

Both JupyterLab_ and nteract_ have builtin rendering for Vega-Lite, so ipyvega_
doesn't need to be installed. However, to get Altair to emit the right data
to render in these more modern frontends, you must call the ``enable_mime_rendering``
function before trying to render a visualization:

.. code-block:: python

    import altair as alt

    # load built-in dataset as a pandas DataFrame
    cars = alt.load_dataset('cars')

    # For rendering in JupyterLab & nteract
    alt.enable_mime_rendering()

    alt.Chart(cars).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    )

Eventually this will not be needed, but is being provided to keep Altair working
without change in the classic Jupyter Notebook.


.. _ipyvega: http://github.com/vega/ipyvega
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _JupyterLab: https://github.com/jupyterlab/jupyterlab
.. _nteract: https://github.com/nteract/nteract