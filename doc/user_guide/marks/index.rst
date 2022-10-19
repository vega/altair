.. currentmodule:: altair

.. _user-guide-mark:

Marks
-----

We saw in :ref:`user-guide-encoding` that the :meth:`~Chart.encode` method is
used to map columns to visual attributes of the plot.
The ``mark`` property is what specifies how exactly those attributes
should be represented on the plot.

Altair provides a number of basic mark properties
(the mark properties column links to the Vega-Lite documentation
that allows you to interactively explore the effects of modifying each property):

=========================================  =========================================  ================================================================================
Mark                                       Method                                     Description
=========================================  =========================================  ================================================================================
:ref:`user-guide-mark-geoshape`            :meth:`~Chart.mark_geoshape`               Visualization containing spatial data
=========================================  =========================================  ================================================================================


.. toctree::
   :hidden:

   geoshape