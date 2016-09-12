"""
Utilities for using nodejs packages for generating png & svg
"""
from __future__ import print_function

import os
import tempfile
import random


__all__ = ['savechart']

NODE_BIN_DIR = os.path.expanduser('~/node_modules/.bin')
SUPPORTED_FILETYPES = ['png', 'svg']


class NodeExecutor(object):
    """Class to execute vega/vega-lite conversion commands in nodejs

    Parameters
    ----------
    node_bin_dir : str
        The directory containing binary executables installed by node
    verbose : bool (optional)
        If True (default) then print commands before executing them.
    """
    def __init__(self, node_bin_dir=NODE_BIN_DIR, verbose=True):
        self.verbose = verbose
        self.node_bin_dir = node_bin_dir

    def _exec(self, executable, inputfile, outputfile):
        full_executable = os.path.join(NODE_BIN_DIR, executable)
        if not os.path.exists(full_executable):
            raise ValueError('{0} not found'.format(full_executable))
        command = '{0} {1} > {2}'.format(full_executable,
                                         inputfile,
                                         outputfile)
        if self.verbose:
            print('>', command)
        os.system(command)

    def _chain(self, executable1, executable2, inputfile, outputfile):
        with tempfile.NamedTemporaryFile(suffix='.json') as f:
            self._exec(executable1, inputfile, f.name)
            self._exec(executable2, f.name, outputfile)

    def vl2vg(self, inputfile, outputfile):
        return _exec('vl2vg', inputfile, outputfile)

    def vg2png(self, inputfile, outputfile):
        return _exec('vl2vg', inputfile, outputfile)

    def vg2svg(self, inputfile, outputfile):
        return _exec('vl2vg', inputfile, outputfile)

    def vl2png(self, inputfile, outputfile):
        self._chain('vl2vg', 'vg2png', inputfile, outputfile)

    def vl2svg(self, inputfile, outputfile):
        self._chain('vl2vg', 'vg2svg', inputfile, outputfile)


def savechart(chart, filename, filetype=None,
              node_bin_dir=NODE_BIN_DIR, verbose=True):
    """EXPERIMENTAL means of saving a chart to png or svg

    Note that this requires several nodejs packages to be installed and
    correctly configured. Before running this, you must use the node
    package manager and install:

        $ npm install canvas vega-lite

    The binaries used here (``vl2vg``, ``vg2png``, ``vg2svg``) will be
    installed in the node binary directory, which should be passed supplied
    via the ``node_bin_dir`` argument.

    Parameters
    ----------
    chart : Altair chart object
        The chart to save
    filename : str
        The output filename
    filetype : str (optional)
        The filetype to use (either 'svg' or 'png'). If not specified,
        it will be inferred from the filename.
    node_bin_dir : str
        The directory containing binary executables installed by node
    verbose : bool (optional)
        If True (default) then print commands before executing them.
    """
    node = NodeExecutor(node_bin_dir=node_bin_dir,
                        verbose=verbose)

    if filetype is None:
        base, ext = os.path.splitext(filename)
        filetype = ext[1:]

    if filetype not in SUPPORTED_FILETYPES:
        raise ValueError("Filetype {0} not valid: must be one of {1}"
                         "".format(filetype, SUPPORTED_FILETYPES))
        
    with tempfile.NamedTemporaryFile(suffix='.json') as f:
        with open(f.name, 'w') as ff:
            ff.write(chart.to_json())
        getattr(node, 'vl2' + filetype)(f.name, filename)
