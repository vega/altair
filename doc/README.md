# Contributing to Altair Documentation

Altair documentation is written in [reStructuredText](http://docutils.sourceforge.net/rst.html) and compiled into html pages using [Sphinx](http://www.sphinx-doc.org/en/master/). Contributing to the documentation requires some extra dependencies and we have some conventions and plugins that are used to help navigate the docs and generate great Altair visualizations. 

## Building the Documentation locally

Assuming you have followed all the steps for a [development install](../README.md), you will need to also install the dependencies for documentation listed in  `docs/requirements.txt` and install altair locally from the branch you are updating: 

```
cd altair
pip install -r requirements.txt 
pip install -e . # See Altair Readme for further information about installing Altair for development. 
pip install -r doc/requirements.txt # Documentation install 
```
In addition, the sphinx documentation builder needs access to Selenium to support generating images of sample visualizations. You may have selenium already installed but if you do not it can also be installed via pip but is not in the requirements file because of its size and dependencies. 

```
pip install selenium
```

One you have all the dependencies, you can build the documentation using various commands defined in the Makefile. From the `doc` folder, you can use `make help` to see all of the available commands which control the type of documentation you want to generate:

```
$ make help

Please use `make <target>' where <target> is one of
  html       to make standalone HTML files
  dirhtml    to make HTML files named index.html in directories
  singlehtml to make a single large HTML file
  pickle     to make pickle files
  json       to make JSON files
  htmlhelp   to make HTML files and a HTML help project
  qthelp     to make HTML files and a qthelp project
  applehelp  to make an Apple Help Book
  devhelp    to make HTML files and a Devhelp project
  epub       to make an epub
  epub3      to make an epub3
  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
  latexpdf   to make LaTeX files and run them through pdflatex
  latexpdfja to make LaTeX files and run them through platex/dvipdfmx
  text       to make text files
  man        to make manual pages
  texinfo    to make Texinfo files
  info       to make Texinfo files and run them through makeinfo
  gettext    to make PO message catalogs
  changes    to make an overview of all changed/added/deprecated items
  xml        to make Docutils-native XML files
  pseudoxml  to make pseudoxml-XML files for display purposes
  linkcheck  to check all external links for integrity
  doctest    to run all doctests embedded in the documentation (if enabled)
  coverage   to run coverage check of the documentation (if enabled)
  dummy      to check syntax errors of document sources

```
For most updates, run `make html` and the documentation will generate in a sub folder `_build`. You can open `_build/html/index.html` to view the documenation as local static files which should give you a good preview of how any updates will look. Even better, use the command below to serve the static files and you will be able to navigate the whole documentation website. 

```
cd doc/_buld/_html
python -m http.server  # python 3 required
```

## Documentation Conventions

**Adding Examples**

Examples are added to the folders `altair/vegalite/v2/examples` folder. To add an example, save a python file with your plot and a header consisting of a reStructuredText docstring at the top of the file including the title of the example following the docstring and a one line python comment with the category that your example belongs. Here is the format of a example header: 

```
"""
Name of Your Plot
-----------------

A really good description of the example
"""
# category: case studies 
import altair as alt
from vega_datasets import data

# more plot code
```
With this convention, your example will build automatically and be placed on the gallery page. 

**Updating the User Guide**

When updating the user guide the following conventions are helpful: 

* When referring to an Altair class or function preface it with ``:class:`` or ``:func`` and the rendering engine will automatically link it to the appropriate section in the API reference. 
* Link to examples using the following syntax 
    ```
        :ref:`gallery_chart_to_link_to`
    ```
* Link to other parts of the user guide with
    ```
        :ref:`user-guide-filename`
    ```



