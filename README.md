# Altair

[![build status](http://img.shields.io/travis/ellisonbg/altair/master.svg?style=flat)](https://travis-ci.org/ellisonbg/altair)

A High-level declarative visualization library for Python.

Altair provides a Python API for building statistical visualizations in a declarative
manner. By statistical visualization we mean:

* The data source is a data frame that consists of column of different data types (quantitative, ordinal, nominal and date/time).
* The data frame is in a [tidy format](http://vita.had.co.nz/papers/tidy-data.pdf)
  where the rows correspond to samples and the colunms correspond the observed variables.
* The visual encoding (position, color, size, shape, facetting, etc.) of the different
  columns is intimately related to the groupby operation of Pandas and SQL.

The Altair API contains no actual visualization rendering code, but instead emits JSON
data structures following the [Vega-Lite](https://github.com/vega/vega-lite)
specification. For convenience, Altair can optionally use
[ipyvega](https://github.com/vega/ipyvega) to seamlessly display client-side renderings
in the Jupyter notebook.

Altair is developed by [Brian Granger](https://github.com/ellisonbg) and [Jake Vanderplas](https://github.com/jakevdp) in close collaboration with the [Interactive Data Lab](http://idl.cs.washington.edu/) at the University of Washington.

## Features

* Carefully-designed, declarative Python API based on
  [traitlets](https://github.com/ipython/traitlets).
* Auto-generated internal Python API that guarantees visualizations are type-checked and
  in full conformance with the [Vega-Lite](https://github.com/vega/vega-lite)
  specification.
* Auto-generate Altair Python code from a Vega-Lite JSON spec.
* Display visualizations in the live Jupyter Notebook, on GitHub and
  [nbviewer](http://nbviewer.jupyter.org/).
* Export visualizations to PNG images, stand-alone HTML pages and the online [Vega-Lite
  Editor](https://vega.github.io/vega-editor/?mode=vega-lite).
* Serialize visualizations as JSON files.
* Explore Altair with 40 example datasets.

## Examples

Here is an example of how Altair can be used to quickly visualize a dataset. The figure
is displayed using the native Vega-Lite renderer:

```python
from altair import Chart, load_dataset

# data is loaded as a pandas DataFrame
cars = load_dataset('cars')

Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
```
![Altair Visualization](images/cars.png?raw=true)

For more information and examples of Altair's API, see the [Altair
Documentation](notebooks/01-Index.ipynb).

Alternatively, you can explore the documentation yourself as runnable Jupyter Notebooks.
To immediately download the Altair Documentation as notebooks, run the following code
from a Jupyter Notebook:

```python
from altair import tutorial
tutorial()
```

## Philosophy

There are currently many excellent plotting libraries in Python. The main ones are:

* [Matplotlib](http://matplotlib.org/)
* [Bokeh](http://bokeh.pydata.org/en/latest/)
* [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/#)
* [Lightning](http://lightning-viz.org/)
* [Plotly](https://plot.ly/)
* [Pandas built-in plotting](http://pandas.pydata.org/pandas-docs/stable/visualization.html)
* [HoloViews](http://ioam.github.io/holoviews/)
* [VisPy](http://vispy.org/)

Each of these libraries does a certain set of things really well. However, such a
proliferation of options creates great difficulty for users as they have to wade through
all of these APIs to find which of them is the best for the task at hand. Furthermore,
because none of these libraries are optimized for high-level statistical visualization,
users have to assemble their own using a mish-mash of APIs. For individuals just
learning data science, this forces them to focus on learning APIs rather than exploring
their data.

Another challenge is that all of the current APIs require the user to write code,
even for incidental aspects of a visulization. This is unfortunate and
unnecessary as the type of visualization (histogram, scatterplot, etc.) can often
be inferred with basic information such as the columns of interest and the data
types of those columns. For example, if you are interested in a visualization of
two numerical columns, a scatterplot is almost certainly a good starting point.
If you add a categorical column to that, you probably want to encode that column
using colors or facets. In cases where the visualization can't be inferred,
simple user interfaces can enable the construction of visualizations without any
coding. [Tableau](http://www.tableau.com/) and the [Interactive Data
Lab's](http://idl.cs.washington.edu/)
[Polestar](https://github.com/vega/polestar) and
[Voyager](https://github.com/vega/voyager) are excellent examples of such UIs.

We feel that these challenges can be addressed without creation of yet another
visualization library that has a programmatic API and built-in rendering. The approach
of Altair is to build visualizations using a layered approach that leverages the full
capabilities of existing visualization libraries:

1. A constrained and simple Python API (Altair) that is purely declarative and
emits JSON that follows the Vega-Lite spec.
2. Existing visualization libraries which can render that spec.

This approach enables users to perform exploratory visualizations with a much simpler API initially, pick an appropriate renderer for their usage case, and then leverage the full capabilities of that renderer for more advanced plot customization.

We realize that a declarative API will necessarily be limited compared to the full programatic APIs of Matplotlib, Bokeh, etc. That is a deliberate design choice we feel is needed to simplify the user experience of exploratory visualization.

## Installation

Altair requires the following dependencies:

* [numpy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [py.test](http://pytest.org/latest)

For visualization in the IPython/Jupyter notebook using the Vega-Lite renderer, Altair additionally requires

* [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html)
* [ipyvega](https://github.com/vega/ipyvega)

Assuming you have NumPy, Pandas and the Jupyter Notebook installed, ipyvega and Altair can be installed with the following commands:

```
pip install altair
jupyter nbextension install --sys-prefix --py vega
```

*Coming soon: streamlined installation with [conda](http://conda.pydata.org/).*

## Development install

If you have cloned the repository, run the following command from the root of the repository:

```
pip install -e .
```

If you do not wish to clone the repository, you can install using:

```
pip install git+https://github.com/ellisonbg/altair
```

## Testing

Altair's test suite uses [py.test](http://pytest.org/latest/).
To run tests, use
```
py.test altair
```

## Feedback and Contribution

We welcome any input, feedback, bug reports, and contributions via [Altair's
GitHub Repository](http://github.com/ellisonbg/altair/). In particular, we
welcome companion efforts from other visualization libraries to render the Vega-Lite
specifications output by Altair. We see this portion of the effort as much bigger
than Altair itself: the Vega and Vega-Lite specifications are perhaps the best
existing candidates for a principled *lingua franca* of data visualization.

## Whence Altair?

Altair is the [brightest star](https://en.wikipedia.org/wiki/Altair) in the constellation Aquila, and along with Deneb and Vega forms the northern-hemisphere asterism known as the [Summer Triangle](https://en.wikipedia.org/wiki/Summer_Triangle).
