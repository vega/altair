# Altair

[![build status](http://img.shields.io/travis/ellisonbg/altair/master.svg?style=flat)](https://travis-ci.org/ellisonbg/altair)

High-level declarative visualization library for Python.

This package provides a Python API for building statistical visualizations in a
declarative manner.
This API contains no actual visualization rendering code, but instead emits JSON data structures following the [Vega-Lite](https://github.com/vega/vega-lite) specification.
For convenience, Altair can optionally use [ipyvega](https://github.com/vega/ipyvega) to seamlessly display client-side renderings in the Jupyter notebook.

## Examples

Here is an example of how Altair can be used to quickly visualize a dataset.
The figure is displayed using the native Vega-Lite renderer:

```python
from altair import Layer, load_dataset

# data is loaded as a pandas DataFrame
cars = load_dataset('cars')

Layer(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
```
![Altair Visualization](images/cars.png?raw=true)

For more information and examples of Altair's API, see the [Notebook Examples](notebooks/Index.ipynb).

## Motivation

There are currently many excellent plotting libraries in Python. The main ones are:

* [Matplotlib](http://matplotlib.org/)
* [Bokeh](http://bokeh.pydata.org/en/latest/)
* [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/#)
* [Lightning](http://lightning-viz.org/)
* [Plotly](https://plot.ly/)
* [Pandas built-in plotting](http://pandas.pydata.org/pandas-docs/stable/visualization.html)
* [HoloViews](http://ioam.github.io/holoviews/)
* [VisPy](http://vispy.org/)

Each of these libraries does a certain set of things really well.
However, such a proliferation of options creates great difficulty for users as they have to wade through all of these APIs to find which of them is the best for the task at hand.
For individuals just learning data science, this forces them to focus on learning APIs rather than exploring data.

Another challenge is that all of the current APIs require the user to write code, even for the simplest of visualizations.
This is unfortunate and unnecessary as the type of visualization (histogram, scatterplot, etc.) can often be inferred with basic information such as the columns of interest and the data types of those columns.
For example, if you are interested in a visualization of two numerical columns, a scatterplot is almost certainly a good starting point.
If you add a categorical column to that, you probably want facetted scatterplots.
In cases where the visualization can't be inferred, simple user interfaces can enable the construction of visualizations without any coding. [Tableau](http://www.tableau.com/) and Jeff Heer's
[Polestar](https://github.com/vega/polestar) and [Voyager](https://github.com/vega/voyager) are
excellent examples of such UIs.

We feel that these challenges can be addressed without creation of yet another plotting library.
The approach of Altair is to build visualizations using a layered approach that leverages the full capabilities of existing visualization libraries:

1. A constrained and simple Python API (Altair) that is purely declarative and emits JSON that follows the vega-lite spec.
2. Existing visualization libraries which can render that spec.

This approach enables users to perform exploratory visualizations with a much simpler API initially, pick an appropriate renderer for their usage case, and then leverage the full capabilities of that renderer for more advanced plot customization.

We realize that a declarative API will necessarily be limited compared to the full programatic APIs of Matplotlib, Bokeh, etc. That is a deliberate design choice we feel is needed to simplify the user experience of exploratory visualization.

## Installation

Altair requires the following dependencies:

* [numpy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [py.test](http://pytest.org/latest)

For visualization in the IPython/Jupyter notebook using the Vega-Lite renderer, Altair additionally requires

* [Jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html)
* [ipyvega](https://github.com/vega/ipyvega)

Once the dependencies have been installed, Altair can be installed.
If you have cloned the repository, run the following command from the root of the repository:

```
python setup.py install
```

If you do not wish to clone the repository, you can install using:

```
pip install git+https://github.com/ellisonbg/altair
```

*Coming soon: streamlined installation with [conda](http://conda.pydata.org/).*

## Testing

Altair's test suite uses [py.test](http://pytest.org/latest/).
To run tests, use
```
py.test altair
```

## Feedback and Contribution

We welcome any input, feedback, bug reports, and contributions via [Altair's GitHub Repository](http://github.com/ellisonbg/altair/).
In particular, we would welcome companion efforts from other graphics libraries to render the Vega-Lite specifications output by Altair.
We see this portion of the effort as much bigger than Altair itself: the Vega and Vega-Lite specifications are perhaps the best existing candidates for a principled *lingua franca* of data visualization.

## Whence Altair?

Altair is the [brightest star](https://en.wikipedia.org/wiki/Altair) in the constellation Aquila, and along with Deneb and Vega forms the northern-hemisphere asterism known as the [Summer Triangle](https://en.wikipedia.org/wiki/Summer_Triangle).
