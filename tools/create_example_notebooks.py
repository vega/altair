"""Build example notebooks from JSON specs in altair.examples"""

import os

import nbformat
from nbformat.v4.nbbase import new_markdown_cell, new_code_cell, new_notebook
from nbconvert.preprocessors import ExecutePreprocessor
from jupyter_client.kernelspec import KernelSpecManager

from altair import *
from altair.examples import iter_examples


INDEX_TEXT = """# Auto-Generated Altair Examples

All the following notebooks are auto-generated from the example specifications
in the [Vega-Lite](http://vega.github.io/vega-lite/) project.
"""


def get_kernelspec(name):
    ksm = KernelSpecManager()
    kernelspec = ksm.get_kernel_spec(name).to_dict()
    kernelspec['name'] = name
    kernelspec.pop('argv')
    return kernelspec


def write_notebook(cells, outputfile, execute=True, kernel='python3'):
    kernelspec = get_kernelspec(kernel)
    notebook = new_notebook(cells=cells,
                            metadata={'language': 'python',
                                      'kernelspec': kernelspec})

    if execute:
        ep = ExecutePreprocessor(timeout=600, kernelname='python3')
        ep.preprocess(notebook,
                      {'metadata': {'path': os.path.dirname(outputfile)}})

    nbformat.write(notebook, outputfile)


def create_example_notebook(filename, spec, notebook_directory,
                            execute=True, kernel='python3', verbose=True,
                            index_dict=None):
    filestem = os.path.splitext(filename)[0]
    full_filename = os.path.join('altair', 'examples', 'json', filename)
    full_filepath = os.path.join('..', '..', full_filename)
    outputfile = filestem + '.ipynb'
    outputfile_full = os.path.join(notebook_directory, outputfile)

    if verbose:
        print(filename)
        print(" -> {0}".format(outputfile_full))

    title = filestem.replace('_', ' ').title()
    description = spec.get('description', '--')
    dataset = os.path.splitext(os.path.basename(spec['data']['url']))[0]

    index_entry = "[{0}]({1}): *{2}*".format(title, outputfile, description)
    if index_dict is not None:
        index_dict[filename] = index_entry

    layer = Layer.from_dict(spec)

    def cells():
        yield new_markdown_cell('<small>*Notebook auto-generated from '
                                '[``{0}``]({1})*</small>\n\n'
                                '# Altair Example: {2}\n\n'
                                '{3}\n\n'.format(full_filename, full_filepath,
                                                 title, description))

        yield new_markdown_cell('## Load Dataset\n'
                                 'The data comes in the form of a Pandas '
                                 'Dataframe:')
        yield new_code_cell('from altair import load_dataset\n'
                            'data = load_dataset("{0}")\n'
                            'data.head()'.format(dataset))

        yield new_markdown_cell('## Define Altair Specification')
        yield new_code_cell('from altair import *  # Load all API methods\n\n'
                            'layer = {0}\n\n'
                            '# IPython rich display will invoke Vega-Lite:\n'
                            'layer'.format(layer.to_altair(data='data')))

        yield new_markdown_cell('## Output Vega-Lite Specification')
        yield new_code_cell('# Generate JSON dict, leaving data out:\n'
                            'layer.to_dict(data=False)')

    write_notebook(list(cells()), outputfile_full,
                   execute=execute, kernel=kernel)


def write_index(notebook_directory, index_dict, kernel='python3'):
    index_listing = '\n'.join('- ' + entry
                              for key, entry in sorted(index_dict.items()))

    cells = [new_markdown_cell(INDEX_TEXT),
             new_markdown_cell(index_listing)]

    write_notebook(cells, os.path.join(notebook_directory, 'Index.ipynb'),
                   execute=False, kernel=kernel)


def write_all_examples(execute=True):
    notebook_directory = os.path.join('..', 'notebooks', 'auto_examples')
    index_dict = {}
    for filename, spec in iter_examples():
        create_example_notebook(filename, spec, notebook_directory,
                                execute=execute, index_dict=index_dict)

    print("writing Index.ipynb")
    write_index(notebook_directory, index_dict)


if __name__ == '__main__':
    write_all_examples(execute=False)
