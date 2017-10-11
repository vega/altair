"""Commands to interact with vega/vega-lite nodejs executables"""
from __future__ import print_function

import os
import json
from contextlib import contextmanager
from xml.etree import ElementTree
from subprocess import Popen, PIPE, check_output, CalledProcessError


COMMANDS = ['vl2vg', 'vl2png', 'vl2svg']
SUPPORTED_FILETYPES = ['png', 'svg']
TEST_SPEC = {'data': {'values': [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}]},
             'encoding': {'x': {'field': 'x', 'type': 'quantitative'},
                          'y': {'field': 'y', 'type': 'quantitative'}},
             'mark': 'point'}


def consistent_with_png(filename):
    """Check that the file has a header consistent with PNG"""
    with open(filename, 'rb') as f:
        arr = f.read()
    return arr.startswith(b'\x89PNG\r\n')


def consistent_with_svg(filename):
    """Check that the file has a structure consistent with SVG"""
    with open(filename) as file_obj:
        element_tag = ""
        try:
            for event, element in ElementTree.iterparse(file_obj, ('start',)):
                element_tag = element.tag
                break
        except ElementTree.ParseError:
            pass
    return element_tag == '{http://www.w3.org/2000/svg}svg'


@contextmanager
def ensure_npm_bin_in_path(verbose=False):
    if verbose:
        print('> npm bin')
    try:
        npm_bin = check_output(['npm', 'bin'])
    except OSError:
        yield
    else:
        if hasattr(npm_bin, 'decode'):
            npm_bin = npm_bin.decode('utf-8')
        npm_bin = npm_bin.strip()

        old_path = os.environ['PATH']

        if npm_bin not in os.environ['PATH'].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + npm_bin
        yield
        os.environ["PATH"] = old_path


def vl_cmd_available(cmd, verbose=False):
    spec = json.dumps(TEST_SPEC)
    with ensure_npm_bin_in_path(verbose):
        try:
            if verbose:
                print('> ' + ' '.join(cmd))
            p = Popen([cmd], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        except OSError:
            return False

        out, err = p.communicate(input='{0}'.format(spec).encode())
    return not p.returncode


def _convert_vegalite_spec(spec, cmd, outfile=None, verbose=False):
    if verbose:
        print('> ' + ' '.join(cmd))
    p = Popen([cmd], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    input_ = '{0}'.format(json.dumps(spec))
    if hasattr(input_, 'encode'):
        input_ = input_.encode()

    out, err = p.communicate(input=input_)
    if p.returncode:
        combined_output = out + b'\nError:\n' + err
        raise CalledProcessError(p.returncode, cmd, output=combined_output)

    if outfile is not None:
        if hasattr(outfile, 'write'):
            outfile.write(out)
        else:
            with open(outfile, 'wb') as f:
                f.write(out)
    else:
        return out


def savechart(chart, filename, filetype=None, verbose=False):
    """Save a chart to png or svg

    Note that this requires several nodejs packages to be installed and
    correctly configured. Before running this, you must have nodejs on
    your system and use the node package manager and install the ``canvas``
    and ``vega-lite`` packages.

    If you are using anaconda, you can set it up this way::

        $ conda create -n node-env -c conda-forge python=2.7 cairo nodejs altair
        $ source activate node-env
        $ npm install canvas vega-lite

    The node binaries used here (``vl2vg``, ``vl2png``, ``vl2svg``) will be
    installed in the node root directory, which should be automatically
    detected by this function.

    Parameters
    ----------
    chart : Altair chart object
        The chart to save
    filename : str
        The output filename
    filetype : str (optional)
        The filetype to use (either 'svg' or 'png'). If not specified,
        it will be inferred from the filename.
    verbose : bool (optional)
        If True (default) then print commands before executing them.
    """
    if filetype is None:
        base, ext = os.path.splitext(filename)
        filetype = ext[1:]

    if filetype not in SUPPORTED_FILETYPES:
        raise ValueError("Filetype {0} not valid: must be one of {1}"
                         "".format(filetype, SUPPORTED_FILETYPES))

    with ensure_npm_bin_in_path(verbose=verbose):
        _convert_vegalite_spec(chart.to_dict(),
                               'vl2' + filetype,
                               outfile=filename,
                               verbose=verbose)
