

from warnings import warn

_msg = """
The Altair Jupyter notebooks have been moved to this repository:

https://github.com/altair-viz/altair_notebooks

This repository has static versions of the notebooks and a live version deployed using binder.
"""

def tutorial(overwrite=False):
    """Copy the Altair tutorial notebooks into ./AltairTutorial and show a link in the notebook."""
    warn(_msg)
