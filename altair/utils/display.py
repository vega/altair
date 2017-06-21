"""
Utilities for displaying Vega/Vega-Lite in modern Jupyter frontends.

Modern Jupyter frontends, such as JupyterLab and nteract, render custom
display using MIME types rather than generic `application/javascript`.

This module contains utilities for displaying Vega/Vega-Lite using custom
MIME types in these frontends.
"""

import json
import os
import uuid

import pandas as pd

from .core import prepare_vega_spec, prepare_vegalite_spec


# The MIME type for Vega 2.x releases.
VEGA_MIME_TYPE = 'application/vnd.vega.v2+json'

# The MIME type for Vega-Lite 1.x releases.
VEGALITE_MIME_TYPE = 'application/vnd.vegalite.v1+json'


def _safe_exists(path):
    """Check path, but don't let exceptions raise"""
    try:
        return os.path.exists(path)
    except Exception:
        return False


def create_vega_mime_bundle(spec, data=None):
    """Create a MIME bundle for Vega given a spec.
    """
    assert isinstance(spec, dict)
    bundle = {}
    bundle['text/plain'] = '<altair.Vega object>'
    bundle[VEGA_MIME_TYPE] = prepare_vega_spec(spec, data=data)
    return bundle


def create_vegalite_mime_bundle(spec, data=None):
    """Create a MIME bundle for Vega-Lite given a spec.
    """
    assert isinstance(spec, dict)
    bundle = {}
    bundle['text/plain'] = '<altair.VegaLite object>'
    bundle[VEGALITE_MIME_TYPE] = prepare_vegalite_spec(spec, data=data)
    return bundle


class Vega(object):
    """A display class for displaying Vega visualizations in the Jupyter frontends.

    Vega expects a spec (a JSON-able dict) and data (dict) argument not
    already-serialized JSON strings. Scalar types (None, number, string) are not
    allowed, only dict containers.
    """

    # wrap data in a property, which warns about passing already-serialized JSON
    _spec = None
    _data = None
    _read_flags = 'r'

    def __init__(self, spec=None, data=None, url=None, filename=None):
        """Create a Vega display object given raw data.
        Parameters
        ----------
        spec : dict
            Vega spec. Not an already-serialized JSON string.
        data : dict
            A dict of Vega datasets where the key is the dataset name and the
            value is the data values. Not an already-serialized JSON string.
            Scalar types (None, number, string) are not allowed, only dict
            or list containers.
        url : unicode
            A URL to download the data from.
        filename : unicode
            Path to a local file to load the data from.
        """

        if spec is not None and isinstance(spec, str):
            if spec.startswith('http') and url is None:
                url = spec
                filename = None
                spec = None
            elif _safe_exists(spec) and filename is None:
                url = None
                filename = spec
                spec = None

        self.spec = spec
        self.data = data
        self.url = url
        self.filename = filename

        self.reload()
        self._check_data()

    def reload(self):
        """Reload the raw spec from file or URL."""
        if self.filename is not None:
            with open(self.filename, self._read_flags) as f:
                self.spec = json.loads(f.read())
        elif self.url is not None:
            try:
                # Deferred import
                try:
                    from urllib.request import urlopen
                except ImportError:
                    from urllib2 import urlopen
                response = urlopen(self.url)
                self.spec = response.read()
                # extract encoding from header, if there is one:
                encoding = None
                for sub in response.headers['content-type'].split(';'):
                    sub = sub.strip()
                    if sub.startswith('charset'):
                        encoding = sub.split('=')[-1].strip()
                        break
                # decode spec, if an encoding was specified
                if encoding:
                    self.spec = self.spec.decode(encoding, 'replace')
            except Exception:
                self.spec = None

    def _check_data(self):
        if self.spec is not None and not isinstance(self.spec, dict):
            raise TypeError("%s expects a JSONable dict, not %r" % \
                (self.__class__.__name__, self.spec))
        if self.data is not None and not isinstance(self.data, dict):
            raise TypeError("%s expects a dict, not %r" % (self.__class__.__name__, self.data))

    @property
    def spec(self):
        """Return the spec."""
        return self._spec

    @property
    def data(self):
        """Return the data."""
        return self._data

    @spec.setter
    def spec(self, spec):
        if isinstance(spec, str):
            # warnings.warn("%s expects a JSONable dict, not %r" % (self.__class__.__name__, spec))
            spec = json.loads(spec)
        self._spec = spec

    @data.setter
    def data(self, data):
        if isinstance(data, str):
            # warnings.warn("%s expects a dict, not %r" % (self.__class__.__name__, data))
            data = json.loads(data)
        self._data = data

    def _repr_mimebundle_(self, include, exclude, **kwargs):
        """Return a MIME bundle for display in Jupyter frontends."""
        return create_vega_mime_bundle(self.spec, self.data)




class VegaLite(Vega):
    """A display class for displaying Vega-Lite visualizations in the Jupyter frontends.

    Vega-Lite expects a spec (a JSON-able dict) and data (dict) argument not
    already-serialized JSON strings. Scalar types (None, number, string) are not
    allowed, only dict containers.
    """

    def __init__(self, spec=None, data=None, url=None, filename=None):
        """Create a VegaLite display object given raw data.

        Parameters
        ----------
        spec : dict
            VegaLite spec. Not an already-serialized JSON string.
        data : dict or list
            VegaLite data. Not an already-serialized JSON string.
            Scalar types (None, number, string) are not allowed, only dict
            or list containers.
        url : unicode
            A URL to download the data from.
        filename : unicode
            Path to a local file to load the data from.
        """

        super(VegaLite, self).__init__(spec=spec, data=data, url=url, filename=filename)

    def _check_data(self):
        if self.spec is not None and not isinstance(self.spec, dict):
            raise TypeError("%s expects a JSONable dict, not %r" % (self.__class__.__name__, self.spec))
        if self.data is not None and not isinstance(self.data, (list, pd.DataFrame)):
            raise TypeError("%s expects a JSONable list or pandas DataFrame, not %r" % (self.__class__.__name__, self.data))
                    
    def _repr_mimebundle_(self, include, exclude, **kwargs):
        """Return a MIME bundle for display in Jupyter frontends."""
        return create_vegalite_mime_bundle(self.spec, self.data)