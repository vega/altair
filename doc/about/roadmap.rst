.. _roadmap:

Roadmap
=======

This page contains the current roadmap for the Vega-Altair project. The roadmap is
informed by the needs of the Vega-Altair community, and the priorities of the active
project contributors. It's designed to communicate the direction of the project,
but it's not a commitment that these items will be completed in a particular timeframe.
If you would like to help contribute to any of these areas, or suggest new ones,
please `start a discussion <https://github.com/altair-viz/altair/discussions>`_.

Vega-Altair is deeply integrated with other components in the Vega ecosystem,
and as such many items on the roadmap will require work in other projects.
Abbreviations for these projects are included at the end of project descriptions
where relevant:

* *(VL)* — `Vega-Lite <https://vega.github.io/vega-lite/>`_
* *(VG)* — `Vega <https://vega.github.io/vega/>`_
* *(VF)* — `VegaFusion <https://vegafusion.io/>`_
* *(VC)* — `VlConvert <https://github.com/vega/vl-convert>`_

API Ergonomics
--------------
The primary job of the Vega-Altair library is to provide an ergonomic Python
API for generating Vega-Lite JSON specifications, and there are several improvements
here that we would like to investigate.

Areas of focus:

* Improve the syntax for creating condition expressions with two or more
  predicates.

* Explore the possibility of a new operator, ``*``, for modular compositing of sub components.
  See also `Deneb.jl <https://brucala.github.io/Deneb.jl/dev>`_ by @brucala.

* Standardize the API of methods that convert charts into other formats (``alt.Chart().to_<format>``).

* Add type hints to the public API and most of the internals so that users can type check their Altair
  code with a static type  checker such as mypy. This will also make it easier for other packages to
  integrate with Altair.

Documentation
-------------
We want to continue to improve Vega-Altair's official documentation to be more
useful for both beginning and experienced users.

Areas of focus:

* Incorporate a conceptual guide that includes best practices of effective
  data communication.

* Update and extend the tutorial section and replace outdated materials.

* Add usage guide with best practices for publishing Vega-Altair charts in various
  contexts including websites, research papers, embedded dashboards, and interactive
  platforms.

* Add guide on building domain specific visualization packages on top of Vega-Altair.
  For example, Vega-Altair for soccer analytics.

* Add documentation for the expression language that is available throughout the API.

Ecosystem Integration
---------------------
We want Vega-Altair to be well integrated with the PyData ecosystem. It should
work well with popular libraries and ecosystem standards.

Areas of focus:

* Provide integration with the broader Python DataFrame ecosystem (beyond pandas). Ensure
  that all of Vega-Altair's features are available to any DataFrame library that implements the
  `DataFrame Interchange Protocol <https://data-apis.org/dataframe-protocol/latest/index.html>`_.

* Work with dashboard toolkit maintainers to ensure that Vega-Altair is well supported.
  Write documentation for best practices for making Vega-Altair's interactive features
  available in Python.

Gridded Data Support
--------------------
Vega-Altair currently requires tidy tabular data as input, so it is not currently a natural
choice for working with gridded data. We would like to extend the project to include native
support for gridded datasets.

Areas of focus:

* Add support for Python array/tensor interchange protocol (through the ``__dlpack__`` interface)

* Add support for creating charts from Xarray
  `DataArray <https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html>`_
  objects (rendering large arrays may require the performance work described elsewhere).

Increased Coverage of Statistical Charts
----------------------------------------
While Vega-Altair includes support for many types of statistical visualizations,
there are a few important types that are not yet possible.

Areas of focus:

* Add support for 2D density visualizations
  (`vega-lite#6043 <https://github.com/vega/vega-lite/issues/6043>`_) *(VL)*

* Add Violin chart support
  (`vega-lite#3442 <https://github.com/vega/vega-lite/issues/3442>`_) *(VL)*

Map Tile Support
----------------
We want Vega-Altair to provide first-class support for displaying map tiles from
xyz tile providers like OpenStreetMap. Early development is in progress in the
`altair_tiles <https://github.com/altair-viz/altair_tiles>`_ repository.

Scale/Performance Improvements
------------------------------
In the traditional Vega-Altair architecture, a chart's entire input dataset is serialized
to JSON and transferred to the browser for data transformation and rendering. Rendering
itself is then performed by The Vega JavaScript library using the Canvas API (which is
not GPU accelerated). This architecture has many advantages (e.g. chart specifications
are fully self-contained and portable to Python-free rendering environments), but it
is not well suited for creating charts of large datasets.

Through a variety of enhancements, our goal is to allow all Vega-Altair charts to
scale comfortably to over 1 million rows.

Areas of focus:

* Provide optional integration with VegaFusion to automatically
  move data transformation steps from the browser to efficient multi-threaded implementations
  in the Python kernel.

* Utilize binary serialization of datasets in Apache Arrow IPC format between the Python kernel
  and the browser. This will significant reduce serialization time for large unaggregated
  visualizations such as scatter plots.

* Support creating Vega-Altair charts that reference tables in external database systems, and convert
  data transformation steps to SQL that can be evaluated by the database before the results are
  transferred to the Python kernel *(VF)*.

* Add support for GPU accelerated rendering. This will enable rendering of large unnagregated
  visualizations at interactive speeds. For example, pan and zoom interactions on a large scatter
  plot *(VG)*.

Static Image Export
-------------------
Even though Vega-Altair charts are rendered by the Vega JavaScript library, it's important to
provide reliable (and easy to install) support for exporting charts to static images. Image
export was dramatically simplified in Vega-Altair 5.0 with the adoption of VlConvert,
which has no external dependencies on a system web-browser or Node.js installation. Now that
image export is easy to install and easy to use, we want to improve support for publication
workflows.

Areas of focus:

* Support configurable pixel density in PNG image export *(VC)*.

* Support exporting charts to vector PDF files with embedded text *(VC)*.

.. toctree::
   :maxdepth: 1
   :caption: About
   :hidden:

   self
   code_of_conduct
   governance
