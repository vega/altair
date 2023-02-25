# Vega-Altair <a href="https://altair-viz.github.io/"><img align="right" src="https://altair-viz.github.io/_static/altair-logo-light.png" height="50"></img></a>

*The Vega-Altair open source project is not affiliated with Altair Engineering, Inc.*

[![build status](https://img.shields.io/travis/altair-viz/altair/master.svg?style=flat)](https://travis-ci.org/altair-viz/altair)
[![github actions](https://github.com/altair-viz/altair/workflows/build/badge.svg)](https://github.com/altair-viz/altair/actions?query=workflow%3Abuild)
[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![JOSS Paper](https://joss.theoj.org/papers/10.21105/joss.01057/status.svg)](https://joss.theoj.org/papers/10.21105/joss.01057)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/altair)](https://pypi.org/project/altair)

**Vega-Altair** is a declarative statistical visualization library for Python. With Vega-Altair, you can spend more time understanding your data and its meaning. Vega-Altair's
API is simple, friendly and consistent and built on top of the powerful
[Vega-Lite](https://github.com/vega/vega-lite) JSON specification. This elegant
simplicity produces beautiful and effective visualizations with a minimal amount of code. *Vega-Altair was originally developed by [Jake Vanderplas](https://github.com/jakevdp) and [Brian
Granger](https://github.com/ellisonbg) in close collaboration with the [UW
Interactive Data Lab](https://idl.cs.washington.edu/).*

## Documentation

See [Vega-Altair's Documentation Site](https://altair-viz.github.io) as well as the [Tutorial Notebooks](https://github.com/altair-viz/altair_notebooks). You can
run the notebooks directly in your browser by clicking on one of the following badges:

[![Binder](https://beta.mybinder.org/badge.svg)](https://beta.mybinder.org/v2/gh/altair-viz/altair_notebooks/master)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/altair-viz/altair_notebooks/blob/master/notebooks/Index.ipynb)

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

brush = alt.selection_interval()

points = alt.Chart(source).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.value('lightgray'))
).add_params(
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

## Installation
Vega-Altair can be installed with:
```bash
pip install altair
```

If you are using the conda package manager, the equivalent is:
```bash
conda install altair -c conda-forge
```

For full installation instructions, please see [the documentation](https://altair-viz.github.io/getting_started/installation.html).

## Getting Help
If you have a question that is not addressed in the documentation, 
you can post it on [StackOverflow](https://stackoverflow.com/questions/tagged/altair) using the `altair` tag.
For bugs and feature requests, please open a [Github Issue](https://github.com/altair-viz/altair/issues).

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
Please additionally consider citing the [Vega-Lite](https://vega.github.io/vega-lite/) project, which Vega-Altair is based on: https://dl.acm.org/doi/10.1109/TVCG.2016.2599030
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
