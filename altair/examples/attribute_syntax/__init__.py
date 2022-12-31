import os


def iter_attribute_syntax():
    """Iterate over the examples in this directory.

    Each item is a dict with the following keys:
    - "name" : the unique name of the example
    - "filename" : the full file path to the example
    """
    attribute_syntax_dir = os.path.abspath(os.path.dirname(__file__))
    for filename in os.listdir(attribute_syntax_dir):
        name, ext = os.path.splitext(filename)
        if name.startswith("_") or ext != ".py":
            continue
        yield {"name": name, "filename": os.path.join(attribute_syntax_dir, filename)}
