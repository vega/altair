.. _importing:

Importing Altair
================

As of Altair 2.0, we include support for multiple versions of both
Vega-Lite (1.x and 2.x) and Vega (2.x and 3.x) in a single Python package.
This section of the documentation describes how you can import the different
versions of the Python APIs.

.. note::

  We strongly recommend all users transition to Vega-Lite 2.x and Vega 3.x.
  These versions support many new features, are more stable, and Altair 2.0
  works best with them.

Vega-Lite
---------

To import the latest version of the Python API for Vega-Lite::

  import altair as alt

**This is the Python API recommended for most users.**

Currently, this points to the Vega-Lite 2.x API, which can be imported
explicitly as::

  import altair.vegalite.v2 as alt

The older, Vega-Lite 1.x Python API is available as::

  import altair.vegalite.v1 as alt

Vega
----

To import the Python API for Vega 3.x, use::

  import altair.vega.v3 as vega

To import the Python API for Vega 2.x, use::

  import altair.vega.v2 as vega

