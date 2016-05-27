LONG_DESCRIPTION = """
Altair: High-level declarative visualization library for Python
===============================================================

This package exposes a Python API for building statistical visualizations in a
declarative manner. This API contains no actual visualization rendering code,
but instead just emits JSON data that follows the
`vega-lite <https://github.com/vega/vega-lite>`_ specification.

Actual plotting code is done by renderers that are provided by other plotting
libraries. For the purpose or prototyping, we are shipping a Matplotlib
rendered in Altair.
"""

DESCRIPTION         = "Altair: Python Visualization with Vega Lite"
NAME                = "altair"
PACKAGES            = ['altair',
                       'altair.tests',
                       'altair.datasets',
                       'altair.examples',
                       'altair.examples.tests',
                       'altair.utils',
                       'altair.utils.tests',
                       'altair.schema',
                       'altair.schema._generated',
                       'altair.schema._generated.tests']
PACKAGE_DATA        = {'altair': ['schema/*.json',
                                  'examples/json/*.json',
                                  'datasets/*.json']}
AUTHOR              = "Jupyter Development Team",
AUTHOR_EMAIL        = "jupyter@googlegroups.org",
URL                 = 'http://github.com/ellisonbg/altair/'
DOWNLOAD_URL        = 'http://github.com/ellisonbg/altair/'
LICENSE             = 'BSD 3-clause'

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
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'],
     )
