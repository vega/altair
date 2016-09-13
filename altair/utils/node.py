"""
Utilities for using nodejs packages for generating png & svg
"""
from __future__ import print_function

import os
import tempfile


__all__ = ['savechart', 'savechart_available']

SUPPORTED_FILETYPES = ['png', 'svg']


class _NodeExecutor(object):
    """Class to execute vega/vega-lite conversion commands in nodejs

    Parameters
    ----------
    node_bin_dir : str
        The directory containing binary executables installed by node.
        If not specified, then ``npm root`` will be used to find it.
    verbose : bool (optional)
        If True (default) then print commands before executing them.
    """
    def __init__(self, node_bin_dir=None, verbose=True):
        self.verbose = verbose
        self.node_bin_dir = os.path.abspath(node_bin_dir or self.npm_root)

    def _exec(self, executable, inputfile, outputfile):
        full_executable = os.path.join(self.node_bin_dir, executable)
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

    @property
    def npm_root(self):
        rootdir = os.popen('npm root').read().strip()
        if not os.path.exists(rootdir):
            raise ValueError('npm root did not return a valid filename')
        return os.path.join(rootdir, '.bin')

    def savechart_available(self):
        try:
            root = self.npm_root
        except:
            return False
        else:
            root = root.strip()
            if not os.path.exists(root):
                return False
            else:
                L = os.listdir(root)
                return ('vl2vg' in L and 'vg2png' in L and 'vg2svg' in L)


def savechart_available(node_bin_dir=None):
    node = _NodeExecutor(node_bin_dir=node_bin_dir)
    return node.savechart_available()
        


def savechart(chart, filename, filetype=None,
              node_bin_dir=None, verbose=False):
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
        The directory containing binary executables installed by node.
        If not specified, then ``npm root`` will be used to determine it.
    verbose : bool (optional)
        If True (default) then print commands before executing them.
    """
    if filetype is None:
        base, ext = os.path.splitext(filename)
        filetype = ext[1:]

    if filetype not in SUPPORTED_FILETYPES:
        raise ValueError("Filetype {0} not valid: must be one of {1}"
                         "".format(filetype, SUPPORTED_FILETYPES))

    node = _NodeExecutor(node_bin_dir=node_bin_dir,
                         verbose=verbose)
    if not node.savechart_available():
        raise ValueError("Must install and configure nodejs tools "
                         "to use savechart")
        
    with tempfile.NamedTemporaryFile(suffix='.json') as f:
        with open(f.name, 'w') as ff:
            ff.write(chart.to_json())
        getattr(node, 'vl2' + filetype)(f.name, filename)
