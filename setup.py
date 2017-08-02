LONG_DESCRIPTION = """
Altair: A declarative statistical visualization library for Python.

http://altair-viz.github.io/

This package provides a Python API for building statistical visualizations
in a declarative manner. This API contains no actual visualization rendering
code, but instead emits JSON data structures following the `Vega-Lite`_
specification. For convenience, Altair can optionally use `ipyvega`_ to
seamlessly display client-side renderings in the Jupyter notebook.

.. image:: https://raw.githubusercontent.com/altair-viz/altair/master/images/cars.png

Please note that if you wish to use altair in the Jupyter Notebook, the
`ipyvega`_ notebook extension must be enabled as follows::

    $ pip install altair
    $ pip install --upgrade notebook
    $ jupyter nbextension install --sys-prefix --py vega

See the `Altair Documentation`_ for tutorials, detailed installation
instructions, and examples.
See the `Altair Github Repository`_ for issues, bug reports, and contributions.

.. _Altair Github Repository: http://github.com/altair-viz/altair/
.. _Altair Documentation: http://altair-viz.github.io/
.. _Vega-Lite: https://github.com/vega/vega-lite
.. _ipyvega: https://github.com/vega/ipyvega
"""

DESCRIPTION         = "Altair: A declarative statistical visualization library for Python."
NAME                = "altair"
PACKAGES            = ['altair',
                       'altair.tests',
                       'altair.datasets',
                       'altair.datasets.tests',
                       'altair.examples',
                       'altair.examples.tests',
                       'altair.expr',
                       'altair.expr.tests',
                       'altair.utils',
                       'altair.utils.tests',
                       'altair.schema',
                       'altair.schema._interface',
                       'altair.schema._interface.tests',
                       ]
PACKAGE_DATA        = {'altair': ['notebooks/*.ipynb',
                                  'notebooks/*.html',
                                  'notebooks/auto_examples/*.ipynb',
                                  'schema/*.json',
                                  'examples/*.json',
                                  'examples/json/*.json',
                                  'datasets/*.json',
                                  'expr/*.json']}
AUTHOR              = "Brian E. Granger / Jake VanderPlas"
AUTHOR_EMAIL        = "ellisonbg@gmail.com / jakevdp@cs.washington.edu"
URL                 = 'http://altair-viz.github.io'
DOWNLOAD_URL        = 'http://github.com/altair-viz/altair/'
LICENSE             = 'BSD 3-clause'
INSTALL_REQUIRES    = ['traitlets>=4.3.1','ipython','pandas','vega>=0.4.4']


import io
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(path, encoding='utf-8'):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def version(path):
    """Obtain the packge version from a python file e.g. pkg/__init__.py

    See <https://packaging.python.org/en/latest/single_source_version.html>.
    """
    version_file = read(path)
    version_match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = version('altair/__init__.py')


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      install_requires=INSTALL_REQUIRES,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
     )
