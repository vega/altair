# Altair

High-level declarative visualization library for Python.

This package exposes a Python API for building statistical visualizations in a
declarative manner. This API contains no actual visualization rendering code, but instead
just emits JSON data that follows the [vega-lite](https://github.com/vega/vega-lite)
specification.

Actual plotting code is done by renderers that are provided by other plotting libraries.
For the purpose or prototyping, we are shipping both a Matplotlib renderer and a simple embeddable HTML renderer in Altair.

# Motivation

There are currently many excellent plotting libraries in Python. The main ones are:

* [Matplotlib](http://matplotlib.org/)
* [Bokeh](http://bokeh.pydata.org/en/latest/)
* [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/#)
* [Lightning](http://lightning-viz.org/)
* [Plotly](https://plot.ly/)
* [Pandas built-in plotting](http://pandas.pydata.org/pandas-docs/stable/visualization.html)
* [HoloViews](http://ioam.github.io/holoviews/)

Each of these libraries does a certain set of things really well. However, this situation creates great difficulty for users as they have to wade through all of these APIs to find which of them is the best for the task at hand. For individuals just learning data science, this forces them to focus on APIs rather than concepts (and the data!).

Another challenge is that all of the current APIs require the user to write code, even for the
simplest of visualizations. This is unfortunate and unnecessary as the type of visualization
(histogram, scatterplot, etc.) can often be inferred with basic information such as the columns of
interest and the data types of those columns. For example if you are interested in a visualization
of two numerical columns, a scatterplot is almost certainly a good starting point. If you add a
categorical column to that, you probably want facetted scatterplots. In cases where the
visualization can't be inferred, simple user interfaces can enable the construction of
visualizations without any coding. [Tableau](http://www.tableau.com/) and Jeff Heer's
[Polestar](https://github.com/vega/polestar) and [Voyager](https://github.com/vega/voyager) are
excellent examples of such UIs.

We feel that these two challenges can be addressed without creating yet another plotting library. The approach we are taking here is to build a layered approach for creating visualizations that leverages the full capabilties of existing visualization libraries:

1. A constrained and simple Python API (Altair) that is purely declarative and emits JSON that follows the vega-lite spec.
2. Existing visualization libraries which can render that spec.

This approach enables users to peform exploratory visualizations with a much simpler API initially, pick an appropriate renderer for their usage case, and then leverage the full capabilities of that renderer for more advanced work and customization.

We realize that a declarative API will necessarily be limited compared to the full programatic APIs of Matplotlib, Bokeh, etc. That is a deliberate design choice we feel is needed to simplify the user experience of exploratory visualization.

## Testing

We are writing tests using [py.test](http://pytest.org/latest/). The run the Altair test suite, run:

	py.test altair

## Notes on vega-lite

This section contains some notes about our experience in using the `vega-lite` JSON
specification:

* It is odd that the `bin` property can either be a `bool` or an object with a single
  `maxbins` attribute. Would make more sense to have a `bins` attribute that is an integer
  that is `0` when no binning should be used and an integer to set the bins.
* There is a good amount of complexity implicit in the vega-lite spec that is difficult
  to infer from the JSON spec itself. A main example is the subtle interplay between
  aggregation and binning.

  - if multiple columns are aggregated what is the order in which the aggregation is computed?
    - how does aggregated data re-enter the computations?
  - if any columns are binned, do you always group against the binned versions for the columns?
  - what to do in cases where the a Q column is used for something that needs to be discrete?
    - difference between ints and floats?
  - are colors always low-number discrete or 'continuous'?
  - is size always low-number discrete or 'continuous'?
