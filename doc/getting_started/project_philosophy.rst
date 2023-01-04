Project Philosophy
==================

Many excellent plotting libraries exist in Python, including:

* `Matplotlib <https://matplotlib.org/>`_
* `Bokeh <https://bokeh.pydata.org/en/latest/>`_
* `Seaborn <https://seaborn.pydata.org/>`_
* `Lightning <http://lightning-viz.org>`_
* `Plotly <https://plot.ly/>`_
* `Pandas built-in plotting <https://pandas.pydata.org/pandas-docs/stable/visualization.html>`_
* `HoloViews <https://holoviews.org>`_
* `VisPy <https://vispy.org/>`_
* `pygg <https://www.github.com/sirrice/pygg>`_

Each library does a particular set of things well.

User Challenges
---------------

However, such a proliferation of options creates great difficulty for users
as they have to wade through all of these APIs to find which of them is the
best for the task at hand. None of these libraries are optimized for
high-level statistical visualization, so users have to assemble their own
using a mishmash of APIs. For individuals just learning to work with data, this
forces them to focus on learning APIs rather than exploring their data.

Another challenge is current plotting APIs require the user to write code,
even for incidental details of a visualization. This results in an unfortunate
and unnecessary cognitive burden as the visualization type (histogram,
scatterplot, etc.) can often be inferred using basic information such as the
columns of interest and the data types of those columns.

For example, if you are interested in the visualization of two numerical
columns, a scatterplot is almost certainly a good starting point. If you add
a categorical column to that, you probably want to encode that column using
colors or facets. If inferring the visualization proves difficult at times, a
simple user interface can construct a visualization without any coding.
`Tableau <https://www.tableau.com/>`_ and the `Interactive Data
Lab's <https://idl.cs.washington.edu/>`_
`Polestar <https://github.com/vega/polestar>`_ and
`Voyager <https://github.com/vega/voyager>`_ are excellent examples of such UIs.

Design Approach and Solution
----------------------------

We believe that these challenges can be addressed without the creation of yet
another visualization library that has a programmatic API and built-in
rendering. Vega-Altair's approach to building visualizations uses a layered design
that leverages the full capabilities of existing visualization libraries:

1. Create a constrained, simple Python API (Vega-Altair) that is purely declarative
2. Use the API (Vega-Altair) to emit JSON output that follows the Vega-Lite spec
3. Render that spec using existing visualization libraries

This approach enables users to perform exploratory visualizations with a much
simpler API initially, pick an appropriate renderer for their usage case, and
then leverage the full capabilities of that renderer for more advanced plot
customization.

We realize that a declarative API will necessarily be limited compared to the
full programmatic APIs of Matplotlib, Bokeh, etc. That is a deliberate design
choice we feel is needed to simplify the user experience of exploratory
visualization.

You can find a more detailed comparison between Plotly and Altair in
`this StackOverflow answer <https://stackoverflow.com/a/66040502>`.

Whence Vega-Altair?
-------------------

The Vega project was named after the brightest star in the constellation Lyra;
nearby Altair is the `brightest star <https://en.wikipedia.org/wiki/Altair>`_ 
in the constellation Aquila, and along with Deneb and Vega forms 
the northern-hemisphere asterism known as
the `Summer Triangle <https://en.wikipedia.org/wiki/Summer_Triangle>`_.