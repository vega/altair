LONG_DESCRIPTION = """
Altair: A declarative statistical visualization library for Python.

http://altair-viz.github.io/

This package provides a Python API for building statistical visualizations
in a declarative manner. This API contains no actual visualization rendering
code, but instead emits JSON data structures following the `Vega-Lite`_
specification. For convenience, Altair can optionally use `ipyvega`_ to
seamlessly display client-side renderings in the Jupyter notebook.

.. image:: https://raw.githubusercontent.com/altair-viz/altair/master/images/cars.png

See the `Altair Documentation`_ for tutorials, detailed installation
instructions, and examples.
See the `Altair Github Repository`_ for issues, bug reports, and contributions.

.. _Altair Github Repository: http://github.com/altair-viz/altair/
.. _Altair Documentation: http://altair-viz.github.io/
.. _Vega-Lite: https://github.com/vega/vega-lite
"""

import io
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#==============================================================================
# Utilities
#==============================================================================

def read(path, encoding='utf-8'):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def get_install_requirements(path):
    content = read(path)
    return [
        req
        for req in content.split("\n")
        if req != '' and not req.startswith('#')
    ]


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

HERE = os.path.abspath(os.path.dirname(__file__))

# From https://github.com/jupyterlab/jupyterlab/blob/master/setupbase.py, BSD licensed
def find_packages(top=HERE):
    """
    Find all of the packages.
    """
    packages = []
    for d, dirs, _ in os.walk(top, followlinks=True):
        if os.path.exists(os.path.join(d, '__init__.py')):
            packages.append(os.path.relpath(d, top).replace(os.path.sep, '.'))
        elif d != top:
            # Do not look for packages in subfolders if current is not a package
            dirs[:] = []
    return packages

#==============================================================================
# Variables
#==============================================================================



DESCRIPTION         = "Altair: A declarative statistical visualization library for Python."
NAME                = "altair"
PACKAGES            = find_packages()
AUTHOR              = "Brian E. Granger / Jake VanderPlas"
AUTHOR_EMAIL        = "jakevdp@gmail.com"
URL                 = 'http://altair-viz.github.io'
DOWNLOAD_URL        = 'http://github.com/altair-viz/altair/'
LICENSE             = 'BSD 3-clause'
INSTALL_REQUIRES    = get_install_requirements("requirements.txt")
DEV_REQUIRES        = get_install_requirements("requirements_dev.txt")
VERSION             = version('altair/__init__.py')


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
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      extras_require={
        'dev': DEV_REQUIRES
      },
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'],
     )
