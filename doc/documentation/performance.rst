.. _performance-considerations:

Peformance Considerations
-------------------------

.. currentmodule:: altair

When you render Altair visualizations in the Jupyter Notebook, Altair sends your entire dataset
to the browser. Upon receiving it, the Jupyter user interface renders the visualization
and saves the dataset in the notebook cell. This model has a number of performance consequences.

Notebook file size
==================

If you have a Jupyter Notebook file, it will embed the full dataset for each and every Altair
visualization within it. For example, if you have 10 visualizations, each with a 10MB DataFrame,
the notebook will store ``10x10MB = 100MB`` of data, leading to potentially large notebook file
sizes. We are working on optimizations that will reduce this effect, but having the full dataset
in the browser is required for the interactive features of VegaLite 2.0. If you run into this
issue, we recommend clearing the outputs of the notebook before saving.

Maximum rows
============

By default, Altair will raise an exception if your dataset has more than 5000 rows. This is
designed to provide a guard to prevent sending large datasets to the browser by accident.
The maximum allowed rows can be changed by setting the :attr:`.max_rows` attribute
of the :class:`Chart` to an integer value that is greater than or equal to the number of rows in your
dataset:

.. code-block:: python

    c = Chart(large_dataset)
    c.max_rows = len(large_dataset)
