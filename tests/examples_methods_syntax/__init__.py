import os


def iter_examples_methods_syntax():
    """Iterate over the examples in this directory.

    Each item is a dict with the following keys:
    - "name" : the unique name of the example
    - "filename" : the full file path to the example
    """
    examples_methods_syntax_dir = os.path.abspath(os.path.dirname(__file__))
    for filename in os.listdir(examples_methods_syntax_dir):
        name, ext = os.path.splitext(filename)
        if name.startswith("_") or ext != ".py":
            continue
        yield {
            "name": name,
            "filename": os.path.join(examples_methods_syntax_dir, filename),
        }
