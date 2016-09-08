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

Installation
------------
Altair can be installed via the Python Package Index with the following::

    pip install altair
    pip install --upgrade notebook
    jupyter nbextension install --sys-prefix --py vega

The additional commands serve to set-up the Jupyter notebook to automatically
render Altair plots.
Alternatively, you can install with conda_, which handles the Jupyter notebook
setup within the single install command::

    conda install altair --channel conda-forge

Altair has the following dependencies, all of which are installed by default
with either of the above installation commands:

- Pandas_
- Traitlets_
- IPython_
- `Jupyter Notebook`_ (optional)
- ipyvega_ (optional, if using Jupyter Notebook)


Documentation
-------------

.. toctree::
   :maxdepth: 2

   quickstart
   tutorials
   documentation
   examples
   API


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Vega-Lite: http://vega.github.io/vega-lite
.. _Pandas: http://pandas.pydata.org
.. _traitlets: https://github.com/ipython/traitlets
.. _IPython: https://github.com/ipython/ipython
.. _Jupyter Notebook: https://jupyter.readthedocs.io/en/latest/install.html
.. _ipyvega: http://github.com/vega/ipyvega
.. _conda: http://conda.pydata.org
