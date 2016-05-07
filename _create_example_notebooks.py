"""Build example notebooks from scripts in altair.examples"""

import os

import nbformat
from nbformat.v4.nbbase import new_markdown_cell, new_code_cell, new_notebook
from nbconvert.preprocessors import ExecutePreprocessor
from jupyter_client.kernelspec import KernelSpecManager


def get_kernelspec(name):
    ksm = KernelSpecManager()
    kernelspec = ksm.get_kernel_spec(name).to_dict()
    kernelspec['name'] = name
    kernelspec.pop('argv')
    return kernelspec


def create_example_notebook(inputfile, outputfile,
                            execute=True, kernel='python3'):
    with open(inputfile) as f:
        full_code = f.read()

    blocks = (block.strip() for block in full_code.split('\n\n'))

    title = os.path.splitext(os.path.basename(inputfile))[0].replace('_', ' ')
    title = title.capitalize()

    def cells():
        yield new_markdown_cell('# {0}\n\n'
                                '*Notebook auto-generated from ``{1}``*'
                                ''.format(title, inputfile))
        for block in blocks:
            if block.startswith('expected_output'):
                yield new_code_cell('v.to_dict()')
            else:
                yield new_code_cell(block)

            if block.startswith('data ='):
                yield new_code_cell('data.head()')

    kernelspec = get_kernelspec(kernel)
    notebook = new_notebook(cells=list(cells()),
                            metadata={'language': 'python',
                                      'kernelspec': kernelspec})
    if execute:
        ep = ExecutePreprocessor(timeout=600, kernelname='python3')
        path = os.path.dirname(outputfile)
        ep.preprocess(notebook, {'metadata': {'path': path}})

    nbformat.write(notebook, outputfile)


def write_all_examples():
    example_directory = os.path.join('altair', 'examples')
    notebook_directory = os.path.join('notebooks', 'auto_examples')
    print("source directory: {0}".format(example_directory))
    print("destination directory: {0}".format(notebook_directory))
    for examplefile in os.listdir(example_directory):
        if examplefile == '__init__.py' or not examplefile.endswith('.py'):
            continue
        notebookfile = os.path.splitext(examplefile)[0] + '.ipynb'
        print('- {0} -> {1}'.format(examplefile, notebookfile))
        create_example_notebook(inputfile=os.path.join(example_directory,
                                                       examplefile),
                                outputfile=os.path.join(notebook_directory,
                                                        notebookfile))


if __name__ == '__main__':
    write_all_examples()
