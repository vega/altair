.. currentmodule:: altair

.. _user-guide-interactions:

Interactive Charts
==================

One of the unique features of Altair, inherited from Vega-Lite, is a
declarative grammar of not just visualization, but also *interaction*.
This is both convenient and powerful,
as we will see in this section.
There are three core concepts of this grammar:

- Parameters are the basic building blocks in the grammar of interaction.
  They can either be simple variables or more complex selections
  that map user input (e.g., mouse clicks and drags) to data queries.
- Conditions and filters can respond to changes in parameter values
  and update chart elements based on that input.
- Widgets and other chart input elements can bind to parameters
  so that charts can be manipulated via drop-down menus, radio buttons, sliders, legends, etc.

In addition to these concepts,
there are two additional components that enhance the capabilities
of interactive visualizations in Altair:

- Expressions allow for custom calculation via writing basic formulas.
  These can be used for fine-controlled interactivity,
  and are also available outside encodings.
- JupyterCharts allow access to Altair's parameters from Python,
  e.g. printing the values of a selection in the plot.

Further reading
---------------

Once you have worked through the subpages for the topics listed above,
you might wish to look through the :ref:`gallery-category-Interactive Charts` section of the example gallery
for ideas about how they can be applied to more interesting charts.

If you are planning to use Altair charts together with Dashboard packages,
see the section on :ref:`Dashboards <display_dashboards>`.

.. toctree::
   :hidden:

   parameters
   bindings_widgets
   expressions
   jupyter_chart
