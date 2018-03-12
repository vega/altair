.. _importing:

Importing Altair
================

As of Altair 2.0, we are including support for multiple version of both
Vega-Lite (1.x and 2.x) and Vega (2.x and 3.x) in a single Python package.
This section of the documentation describe how you can import the different
versions of the Python APIs.

Vega-Lite
---------

To import the latest version of the Python API for Vega-Lite::

  import altair as alt

**This is the Python API recommended for most users.**

Currently, this points to the Vega-Lite 2.x API, which can be imported
explicitly as::

  from altair.vegalite import v2 as alt

The older, Vega-Lite 1.x Python API is available as::

  from altair.vegalite import v1 as alt

Vega
----

To import the Python API for Vega 3.x, use::

  from altair.vega import v3 as vega

To import the Python API for Vega 2.x, use::

  from altair.vega import v2 as vega

