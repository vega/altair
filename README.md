# Vega-Altair <a href="https://altair-viz.github.io/"><img align="right" src="https://altair-viz.github.io/_static/altair-logo-light.png" height="50"></img></a>

*The Vega-Altair open source project is not affiliated with Altair Engineering, Inc.*

[![build status](https://img.shields.io/travis/altair-viz/altair/master.svg?style=flat)](https://travis-ci.org/altair-viz/altair)
[![github actions](https://github.com/altair-viz/altair/workflows/build/badge.svg)](https://github.com/altair-viz/altair/actions?query=workflow%3Abuild)
[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![JOSS Paper](https://joss.theoj.org/papers/10.21105/joss.01057/status.svg)](https://joss.theoj.org/papers/10.21105/joss.01057)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/altair)](https://pypi.org/project/altair)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/altair-viz/altair_notebooks/master?urlpath=lab/tree/notebooks/Index.ipynb)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altair-viz/altair_notebooks/blob/master/notebooks/Index.ipynb)

[https://altair-viz.github.io](https://altair-viz.github.io)

**Vega-Altair** is a declarative statistical visualization library for Python. With Vega-Altair, you can spend more time understanding your data and its meaning. Vega-Altair's
API is simple, friendly and consistent and built on top of the powerful
[Vega-Lite](https://github.com/vega/vega-lite) JSON specification. This elegant
simplicity produces beautiful and effective visualizations with a minimal amount of code. *Vega-Altair was originally developed by [Jake Vanderplas](https://github.com/jakevdp) and [Brian
Granger](https://github.com/ellisonbg) in close collaboration with the [UW
Interactive Data Lab](https://idl.cs.washington.edu/).*

## Vega-Altair Documentation

See [Vega-Altair's Documentation Site](https://altair-viz.github.io),
as well as Vega-Altair's [Tutorial Notebooks](https://github.com/altair-viz/altair_notebooks).

## Example

Here is an example using Vega-Altair to quickly visualize and display a dataset with the native Vega-Lite renderer in the JupyterLab:

```python
import altair as alt

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
```

![Vega-Altair Visualization](https://raw.githubusercontent.com/altair-viz/altair/master/images/cars.png)

One of the unique features of Vega-Altair, inherited from Vega-Lite, is a declarative grammar of not just visualization, but _interaction_. 
With a few modifications to the example above we can create a linked histogram that is filtered based on a selection of the scatter plot.

```python 
import altair as alt
from vega_datasets import data

source = data.cars()

brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin',
    color='Origin',
    x='count(Origin)'
).transform_filter(
    brush
)

points & bars
```

![Vega-Altair Visualization Gif](https://raw.githubusercontent.com/altair-viz/altair/master/images/cars_scatter_bar.gif)

## Features
* Carefully-designed, declarative Python API.
* Auto-generated internal Python API that guarantees visualizations are type-checked and
  in full conformance with the [Vega-Lite](https://github.com/vega/vega-lite)
  specification.
* Display visualizations in JupyterLab, Jupyter Notebook, Visual Studio Code, on GitHub and
  [nbviewer](https://nbviewer.jupyter.org/), and many more.
* Export visualizations to various formats such as PNG/SVG images, stand-alone HTML pages and the
[Online Vega-Lite Editor](https://vega.github.io/editor/#/).
* Serialize visualizations as JSON files.
* Explore Vega-Altair with dozens of examples in the [Example Gallery](https://altair-viz.github.io/gallery/index.html)

## Installation
Vega-Altair can be installed using:
```bash
pip install altair
```

If you are using the conda package manager, the equivalent is:
```bash
conda install -c conda-forge altair
```

For full installation instructions, please see [the documentation](https://altair-viz.github.io/getting_started/installation.html)

## Example and tutorial notebooks

We maintain a separate Github repository of Jupyter Notebooks that contain an
interactive tutorial and examples:

https://github.com/altair-viz/altair_notebooks

To launch a live notebook server with those notebook using [binder](https://mybinder.org/) or
[Colab](https://colab.research.google.com), click on one of the following badges:

[![Binder](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/altair-viz/altair_notebooks/master)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altair-viz/altair_notebooks/blob/master/notebooks/Index.ipynb)

## Getting Help
If you have a question that is not addressed in the documentation, 
you can post it on [StackOverflow](https://stackoverflow.com/questions/tagged/altair) using the `altair` tag
or ask on the [Vega-Altair Google Group](https://groups.google.com/forum/#!forum/altair-viz).
For bugs and feature requests, please open a [Github Issue](https://github.com/altair-viz/altair/issues).


## Project philosophy

Many excellent plotting libraries exist in Python, including the main ones:

* [Matplotlib](https://matplotlib.org/)
* [Bokeh](https://bokeh.pydata.org/en/latest/)
* [Seaborn](https://seaborn.pydata.org/)
* [Lightning](https://github.com/lightning-viz/lightning)
* [Plotly](https://plot.ly/)
* [Pandas built-in plotting](https://pandas.pydata.org/pandas-docs/stable/visualization.html)
* [HoloViews](https://holoviews.org)
* [VisPy](https://vispy.org/)
* [pygg](https://www.github.com/sirrice/pygg)

Each library does a particular set of things well.

### User challenges

However, such a proliferation of options creates great difficulty for users
as they have to wade through all of these APIs to find which of them is the
best for the task at hand. None of these libraries are optimized for
high-level statistical visualization, so users have to assemble their own
using a mishmash of APIs. For individuals just learning data science, this
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
[Tableau](https://www.tableau.com/) and the [Interactive Data
Lab's](https://idl.cs.washington.edu/)
[Polestar](https://github.com/vega/polestar) and
[Voyager](https://github.com/vega/voyager) are excellent examples of such UIs.

### Design approach and solution

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

## Development
You can find the instructions on how to install the package for development in [the documentation](https://altair-viz.github.io/getting_started/installation.html).

To run the tests, use
```
pytest --doctest-modules altair
```

For information on how to contribute your developments back to the Vega-Altair repository, see
[`CONTRIBUTING.md`](https://github.com/altair-viz/altair/blob/master/CONTRIBUTING.md)

## Citing Vega-Altair
[![JOSS Paper](https://joss.theoj.org/papers/10.21105/joss.01057/status.svg)](https://joss.theoj.org/papers/10.21105/joss.01057)

If you use Vega-Altair in academic work, please consider citing https://joss.theoj.org/papers/10.21105/joss.01057 as

```bib
@article{VanderPlas2018,
    doi = {10.21105/joss.01057},
    url = {https://doi.org/10.21105/joss.01057},
    year = {2018},
    publisher = {The Open Journal},
    volume = {3},
    number = {32},
    pages = {1057},
    author = {Jacob VanderPlas and Brian Granger and Jeffrey Heer and Dominik Moritz and Kanit Wongsuphasawat and Arvind Satyanarayan and Eitan Lees and Ilia Timofeev and Ben Welsh and Scott Sievert},
    title = {Altair: Interactive Statistical Visualizations for Python},
    journal = {Journal of Open Source Software}
}
```
Please additionally consider citing the [vega-lite](https://vega.github.io/vega-lite/) project, which Vega-Altair is based on: https://dl.acm.org/doi/10.1109/TVCG.2016.2599030
```bib
@article{Satyanarayan2017,
    author={Satyanarayan, Arvind and Moritz, Dominik and Wongsuphasawat, Kanit and Heer, Jeffrey},
    title={Vega-Lite: A Grammar of Interactive Graphics},
    journal={IEEE transactions on visualization and computer graphics},
    year={2017},
    volume={23},
    number={1},
    pages={341-350},
    publisher={IEEE}
} 
```

## Whence Vega-Altair?

The Vega project was named after the brightest star in the constellation Lyra; nearby Altair is the [brightest star](https://en.wikipedia.org/wiki/Altair) in the constellation Aquila, and along with Deneb and Vega forms the northern-hemisphere asterism known as the [Summer Triangle](https://en.wikipedia.org/wiki/Summer_Triangle).
